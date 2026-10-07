"""
13_modal_app_multi_model.py (v3) — ДВА критичных фикса против v2:

1. Убран сломанный /v1/completions путь для yandexgpt5lite (46/46 ошибок
   "prompt must be non-empty"). vLLM сам применяет chat_template модели
   при обычном /v1/chat/completions — ручной рендеринг был избыточен и
   был единственным источником бага. Все 4 модели теперь идут через
   единый chat-путь.

2. ИСПРАВЛЕН token-matching: "▁1".strip() != "1" — SentencePiece-маркер
   начала слова (▁, U+2581) не является ASCII-пробелом и не снимается
   .strip(). Из-за этого saiga8b и yandexgpt5lite в v2 ФАКТИЧЕСКИ НЕ
   ОЦЕНИВАЛИСЬ — оба logprob всегда падали на дефолт -100, score
   схлопывался в fallback 0.5, что при threshold=0.5 давало
   ПОСТОЯННОЕ predicted_label=1 (отсюда одинаковые P=0.500 R=1.000 —
   это чистый шум от бага, а не реальное качество моделей).
   Фикс: _normalize_token() убирает маркеры начала слова обоих основных
   семейств токенизаторов (▁ SentencePiece, Ġ GPT-2/BPE) перед сравнением.

3. max_model_len для saiga8b поднят с 32768 до 65536 (у неё тоже было
   3 context-length ошибки на прошлом пороге, тот же класс проблемы,
   что чинили раньше для qwen36).

ВАЖНО: результаты saiga8b и yandexgpt5lite из прошлого прогона (P=0.500
R=1.000 у обеих) нужно считать НЕДЕЙСТВИТЕЛЬНЫМИ — перезапустите обе
модели после этого фикса, реальное качество может быть совершенно другим.
"""
import asyncio
import math
import pathlib
import subprocess
import sys
import time
import urllib.error
import urllib.request

import modal

APP_NAME = "guardian-of-truth-model-comparison"

VOLUME_NAME = "guardian-model"
VOLUME_MOUNT = "/vol"

SCRIPTS_DIR_IN_IMAGE = "/app/scripts"
VLLM_PORT = 8000
VLLM_LOG_PATH = "/tmp/vllm_server.log"

HEALTH_CHECK_HOSTS = ["127.0.0.1", "localhost", "0.0.0.0"]

EXPECTED_SCRIPT_FILES = [
    "01_schema_validator.py", "02_entity_diff_checker.py", "03_arithmetic_checker.py",
    "04_field_existence_checker.py", "05_baggage_insurance_rule_checker.py",
    "06_confirmation_gate_checker.py", "07_escalation_exhaustion_checker.py",
    "08_source_conflict_flagger.py", "09_certainty_lexicon_scanner.py", "10_llm_judge.py",
]

HARD_FLAG_PREFIXES = (
    "A2:unknown_tool", "A2:unknown_id_reference", "A2:missing_arg",
    "A2:invalid_enum", "A3:baggage_rule_violation", "A4:calculate_mismatch",
    "A3:write_without_confirmation",
)

MODEL_REGISTRY = {
    "qwen36": {
        "repo_id": "Qwen/Qwen3.6-35B-A3B-FP8",
        "subdir": "model",
        "needs_disable_thinking": True,
        "default_max_model_len": 65536,
        "language_model_only": True,
    },
    "qwen38": {
        "repo_id": "Qwen/Qwen3.8-27B-FP8",
        "subdir": "models/qwen38",
        "needs_disable_thinking": True,
        "default_max_model_len": 65536,
        "language_model_only": True,
    },
    "saiga8b": {
        "repo_id": "IlyaGusev/saiga_yandexgpt_8b",
        "subdir": "models/saiga8b",
        "needs_disable_thinking": False,
        "default_max_model_len": 32768,
        # "default_max_model_len": 65536,  # было 32768 — было 3 context-length ошибки
        "language_model_only": False,
    },
    "yandexgpt5lite": {
        "repo_id": "yandex/YandexGPT-5-Lite-8B-instruct",
        "subdir": "models/yandexgpt5lite",
        "needs_disable_thinking": False,
        "default_max_model_len": 32768,
        "language_model_only": False,
    },
}

app = modal.App(APP_NAME)
model_volume = modal.Volume.from_name(VOLUME_NAME, create_if_missing=True)

image = (
    modal.Image.from_registry(
        "nvidia/cuda:12.9.1-devel-ubuntu22.04",
        add_python="3.11",
    )
    .apt_install("git")
    .pip_install("vllm==0.30.0", "openai")
    .pip_install("pandas==2.2.2", "pyarrow==17.0.0", "hf_transfer==0.1.9")
    .env({
        "HF_HUB_ENABLE_HF_TRANSFER": "1",
        "VLLM_USE_FLASHINFER_SAMPLER": "0",
    })
    .add_local_dir("scripts", remote_path=SCRIPTS_DIR_IN_IMAGE, copy=True)
)


def _model_dir(alias: str) -> str:
    cfg = MODEL_REGISTRY[alias]
    return f"{VOLUME_MOUNT}/{cfg['subdir']}"


@app.function(image=image, volumes={VOLUME_MOUNT: model_volume}, timeout=3600)
def download_model(model_alias: str):
    if model_alias not in MODEL_REGISTRY:
        raise ValueError(f"Неизвестный alias '{model_alias}'. Доступны: {list(MODEL_REGISTRY)}")
    cfg = MODEL_REGISTRY[model_alias]
    p = pathlib.Path(_model_dir(model_alias))
    if p.exists() and (p / "config.json").exists():
        print(f"{p} уже содержит config.json — пропускаю скачивание.")
        return
    from huggingface_hub import snapshot_download
    p.mkdir(parents=True, exist_ok=True)
    snapshot_download(repo_id=cfg["repo_id"], local_dir=str(p), max_workers=8)
    model_volume.commit()
    files = sorted(f.name for f in p.iterdir())
    total_bytes = sum(f.stat().st_size for f in p.rglob("*") if f.is_file())
    print(f"Модель {cfg['repo_id']} сохранена в {p}. Файлов: {len(files)}, "
          f"размер: {total_bytes / 1e9:.1f} GB")


@app.function(image=image, volumes={VOLUME_MOUNT: model_volume})
def debug_list_model(model_alias: str):
    p = pathlib.Path(_model_dir(model_alias))
    print(f"Проверка {p}:")
    if not p.exists():
        print("  НЕ СУЩЕСТВУЕТ.")
        return
    files = sorted(f.name for f in p.iterdir())
    print(f"  Файлы: {files}")
    print("  OK: config.json найден." if "config.json" in files else "  ОШИБКА: config.json НЕ найден.")


@app.function(image=image)
def debug_list_scripts():
    p = pathlib.Path(SCRIPTS_DIR_IN_IMAGE)
    if not p.exists():
        print(f"КАТАЛОГ {SCRIPTS_DIR_IN_IMAGE} НЕ СУЩЕСТВУЕТ")
        return
    found = sorted(f.name for f in p.iterdir())
    missing = [f for f in EXPECTED_SCRIPT_FILES if f not in found]
    print("ОТСУТСТВУЮТ:" if missing else "Все 10 файлов на месте.", missing or "")


def _load_checkers(scripts_dir: str) -> dict:
    import importlib.util
    base = pathlib.Path(scripts_dir)
    missing = [f for f in EXPECTED_SCRIPT_FILES if not (base / f).exists()]
    if missing:
        raise FileNotFoundError(f"В {scripts_dir} отсутствуют файлы: {missing}.")

    def _load(fname, name):
        spec = importlib.util.spec_from_file_location(name, str(base / fname))
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
        return mod

    return {
        "schema": _load("01_schema_validator.py", "schema"),
        "entity_diff": _load("02_entity_diff_checker.py", "entity_diff"),
        "arithmetic": _load("03_arithmetic_checker.py", "arithmetic"),
        "field_existence": _load("04_field_existence_checker.py", "field_existence"),
        "baggage_rule": _load("05_baggage_insurance_rule_checker.py", "baggage_rule"),
        "confirmation_gate": _load("06_confirmation_gate_checker.py", "confirmation_gate"),
        "escalation": _load("07_escalation_exhaustion_checker.py", "escalation"),
        "source_conflict": _load("08_source_conflict_flagger.py", "source_conflict"),
        "certainty": _load("09_certainty_lexicon_scanner.py", "certainty"),
        "judge": _load("10_llm_judge.py", "judge"),
    }


def _has_hard_flag(flags: list[str]) -> bool:
    return any(f.startswith(p) for f in flags for p in HARD_FLAG_PREFIXES)


def _collect_row_flags(row, ck: dict) -> tuple[list[str], str | None]:
    task_id, prompt, response = str(row["id"]), str(row["prompt"]), str(row["response"])
    domain = ck["escalation"].detect_domain(task_id)
    per_script = [
        ("01_schema_validator", ck["schema"].check_schema(prompt, response)),
        ("02_entity_diff_checker", ck["entity_diff"].check_entity_grounding(prompt, response)),
        ("03_arithmetic_checker", ck["arithmetic"].check_arithmetic(prompt, response)),
        ("04_field_existence_checker", ck["field_existence"].check_id_references(prompt, response)),
        ("05_baggage_insurance_rule_checker", ck["baggage_rule"].check_baggage_rule(prompt, response)),
        ("06_confirmation_gate_checker", ck["confirmation_gate"].check_confirmation_gate(prompt, response)),
        ("07_escalation_exhaustion_checker", ck["escalation"].check_escalation_exhaustion(prompt, response, domain)),
        ("08_source_conflict_flagger", ck["source_conflict"].check_source_conflicts(prompt, response)),
        ("09_certainty_lexicon_scanner", ck["certainty"].check_certainty_language(response)),
    ]
    all_flags: list[str] = []
    hard_script_name: str | None = None
    for script_name, flags in per_script:
        all_flags.extend(flags)
        if hard_script_name is None and _has_hard_flag(flags):
            hard_script_name = script_name
    return all_flags, hard_script_name


def _print_log_tail(n_lines: int = 60) -> None:
    p = pathlib.Path(VLLM_LOG_PATH)
    if not p.exists():
        print("Лог-файл vLLM не найден.")
        return
    lines = p.read_text(errors="replace").splitlines()
    traceback_starts = [i for i, l in enumerate(lines) if "Traceback (most recent call last)" in l]
    if traceback_starts:
        print(f"=== Найдено traceback-блоков: {len(traceback_starts)} ===")
        for idx, start in enumerate(traceback_starts):
            end = traceback_starts[idx + 1] if idx + 1 < len(traceback_starts) else min(start + 40, len(lines))
            print(f"\n--- Traceback #{idx + 1}, строки {start}-{end} ---")
            print("\n".join(lines[start:end]))
    print(f"\n=== Хвост лога ({n_lines} строк) ===")
    print("\n".join(lines[-n_lines:]))


def _try_health_check() -> tuple[bool, str]:
    last_error = ""
    for host in HEALTH_CHECK_HOSTS:
        url = f"http://{host}:{VLLM_PORT}/health"
        try:
            resp = urllib.request.urlopen(url, timeout=3)
            return True, f"OK через {host} (status={resp.status})"
        except urllib.error.URLError as e:
            last_error = f"{host}: URLError({e.reason})"
        except Exception as e:  # noqa: BLE001
            last_error = f"{host}: {type(e).__name__}({e})"
    return False, last_error


def _start_vllm_server(model_dir: str, max_model_len: int, language_model_only: bool,
                        timeout_seconds: int = 1500) -> subprocess.Popen:
    cmd = [
        sys.executable, "-m", "vllm.entrypoints.openai.api_server",
        "--model", model_dir,
        "--served-model-name", "judge",
        "--max-model-len", str(max_model_len),
        "--gpu-memory-utilization", "0.90",
        "--port", str(VLLM_PORT),
        "--trust-remote-code",
        "--enforce-eager",
    ]
    if language_model_only:
        cmd.append("--language-model-only")

    log_file = open(VLLM_LOG_PATH, "w")
    proc = subprocess.Popen(cmd, stdout=log_file, stderr=subprocess.STDOUT)

    start_time = time.time()
    deadline = start_time + timeout_seconds
    attempt = 0
    last_msg = ""
    while time.time() < deadline:
        attempt += 1
        if proc.poll() is not None:
            _print_log_tail()
            raise RuntimeError(f"vLLM завершился с кодом {proc.returncode} через {int(time.time()-start_time)}с.")
        ok, msg = _try_health_check()
        last_msg = msg
        if ok:
            print(f"vLLM готов через {int(time.time() - start_time)}с (попытка #{attempt}): {msg}")
            return proc
        if attempt % 10 == 0:
            print(f"[{int(time.time()-start_time)}с] /health недоступен (попытка #{attempt}): {msg}")
        time.sleep(3)

    _print_log_tail()
    proc.kill()
    raise RuntimeError(f"vLLM не поднялся за {timeout_seconds}с. Последняя ошибка: {last_msg}.")


# =============================================================================
# ФИКС: нормализация токена под разные семейства токенизаторов
# =============================================================================

import math


def _normalize_token(token: str) -> str:
    return token.strip().lstrip("\u2581\u0120")


async def _score_one(client, semaphore, system_prompt: str, user_prompt: str,
                      disable_thinking: bool, debug_label: str | None = None) -> tuple[float, str | None]:
    async with semaphore:
        try:
            kwargs = {}
            if disable_thinking:
                kwargs["extra_body"] = {"chat_template_kwargs": {"enable_thinking": False}}
            completion = await client.chat.completions.create(
                model="judge",
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": user_prompt},
                ],
                max_tokens=1,
                temperature=0.0,
                logprobs=True,
                top_logprobs=20,
                **kwargs,
            )
        except Exception as e:  # noqa: BLE001
            return 1.0, f"{type(e).__name__}: {e}"

        top = completion.choices[0].logprobs.content[0].top_logprobs

        # === ДИАГНОСТИКА: печатаем реальные топ-5 токенов для первых N строк ===
        if debug_label is not None:
            import sys
            top5 = sorted(top, key=lambda t: -t.logprob)[:5]
            print(f"[DEBUG {debug_label}] top-5 токенов: "
                  f"{[(repr(t.token), round(t.logprob, 2)) for t in top5]}", file=sys.stderr)

        logprob_1 = next((t.logprob for t in top if _normalize_token(t.token) == "1"), None)
        logprob_0 = next((t.logprob for t in top if _normalize_token(t.token) == "0"), None)

        if logprob_1 is None and logprob_0 is None:
            # Ни "1", ни "0" вообще не встретились в top-20 -- это не 50/50
            # неопределённость, а ПОЛНЫЙ провал формата ответа модели.
            # Возвращаем score=None-эквивалент через отдельный маркер ошибки,
            # а не молчаливый fallback 0.5 (который при threshold=0.5 через
            # >= ВСЕГДА резолвится в label=1 -- это и есть источник бага).
            return 1.0, "no_digit_token_in_top20"

        logprob_1 = logprob_1 if logprob_1 is not None else -100.0
        logprob_0 = logprob_0 if logprob_0 is not None else -100.0
        e1, e0 = math.exp(logprob_1), math.exp(logprob_0)
        score = e1 / (e1 + e0) if (e1 + e0) > 0 else 0.5
        return score, None


async def _score_batch(base_url: str, row_data: list[tuple[str, str, str]],
                        concurrency: int, disable_thinking: bool
                        ) -> tuple[list[float], list[str | None]]:
    from openai import AsyncOpenAI
    client = AsyncOpenAI(base_url=base_url, api_key="not-needed")
    semaphore = asyncio.Semaphore(concurrency)
    tasks = [
        _score_one(client, semaphore, sp, up, disable_thinking,
                   debug_label=task_id if i < 3 else None)
        for i, (task_id, sp, up) in enumerate(row_data)
    ]
    results = await asyncio.gather(*tasks)
    return [r[0] for r in results], [r[1] for r in results]


def _prf1(y_true, y_pred):
    tp = sum(1 for t, p in zip(y_true, y_pred) if t == 1 and p == 1)
    fp = sum(1 for t, p in zip(y_true, y_pred) if t == 0 and p == 1)
    fn = sum(1 for t, p in zip(y_true, y_pred) if t == 1 and p == 0)
    precision = tp / (tp + fp) if (tp + fp) else 0.0
    recall = tp / (tp + fn) if (tp + fn) else 0.0
    f1 = 2 * precision * recall / (precision + recall) if (precision + recall) else 0.0
    return precision, recall, f1


def _build_report_rows(df, ck: dict, llm_scores: dict, llm_errors: dict,
                        best_threshold: float = 0.5) -> list[dict]:
    rows_out = []
    for _, row in df.iterrows():
        task_id = str(row["id"])
        domain = ck["escalation"].detect_domain(task_id)

        true_label = None
        if "label" in df.columns:
            raw_label = row["label"]
            if raw_label is not None and str(raw_label) != "nan":
                try:
                    true_label = int(raw_label)
                except (ValueError, TypeError):
                    true_label = None

        all_flags, hard_script = _collect_row_flags(row, ck)
        llm_score = llm_scores.get(task_id)
        llm_pred = int(llm_score >= best_threshold) if llm_score is not None else None

        if hard_script is not None:
            predicted_label = 1
            stage = f"script:{hard_script}"
            agrees_with_script = (llm_pred == 1) if llm_pred is not None else None
        else:
            predicted_label = llm_pred
            stage = "llm"
            agrees_with_script = None

        correct = (true_label == predicted_label) if (true_label is not None and predicted_label is not None) else None

        rows_out.append({
            "id": task_id, "domain": domain, "true_label": true_label,
            "predicted_label": predicted_label, "stage": stage,
            "llm_score": round(llm_score, 4) if llm_score is not None else None,
            "agrees_with_script": agrees_with_script,
            "all_flags": " | ".join(all_flags) if all_flags else "",
            "correct": correct, "error": llm_errors.get(task_id, ""),
        })
    return rows_out


@app.function(image=image, gpu="H100", volumes={VOLUME_MOUNT: model_volume}, timeout=3000)
def run_predict(
    model_alias: str,
    input_bytes: bytes,
    input_ext: str,
    max_model_len: int | None = None,
    concurrency: int = 32,
    fixed_threshold: float = 0.5,
) -> bytes:
    import tempfile
    import pandas as pd

    if model_alias not in MODEL_REGISTRY:
        raise ValueError(f"Неизвестный alias '{model_alias}'. Доступны: {list(MODEL_REGISTRY)}")
    cfg = MODEL_REGISTRY[model_alias]
    model_dir = _model_dir(model_alias)
    mml = max_model_len or cfg["default_max_model_len"]

    model_path = pathlib.Path(model_dir)
    if not model_path.exists() or not (model_path / "config.json").exists():
        raise RuntimeError(
            f"{model_dir} пуст. Запустите: "
            f"modal run 13_modal_app_multi_model.py::download_model --model-alias {model_alias}"
        )

    ck = _load_checkers(SCRIPTS_DIR_IN_IMAGE)

    with tempfile.TemporaryDirectory() as tmp:
        in_path = pathlib.Path(tmp) / f"input{input_ext}"
        in_path.write_bytes(input_bytes)
        df = pd.read_parquet(in_path) if input_ext == ".parquet" else pd.read_csv(in_path)

        all_row_data = []
        for _, row in df.iterrows():
            all_flags, _hard_script = _collect_row_flags(row, ck)
            task_id = str(row["id"])
            messages = ck["judge"].build_messages(str(row["prompt"]), str(row["response"]), all_flags)
            all_row_data.append((task_id, messages[0]["content"], messages[1]["content"]))

        proc = _start_vllm_server(model_dir, mml, cfg["language_model_only"], timeout_seconds=1500)
        try:
            base_url = f"http://127.0.0.1:{VLLM_PORT}/v1"
            batch_scores, batch_errors = asyncio.run(
                _score_batch(base_url, all_row_data, concurrency, cfg["needs_disable_thinking"])
            )
            scores: dict[str, float] = {}
            llm_errors: dict[str, str] = {}
            for (task_id, *_), score, err in zip(all_row_data, batch_scores, batch_errors):
                scores[task_id] = score
                if err is not None:
                    llm_errors[task_id] = err
                    print(f"[WARN] {task_id}: {err}", file=sys.stderr)
        finally:
            proc.terminate()

        rows_out = _build_report_rows(df, ck, llm_scores=scores, llm_errors=llm_errors,
                                       best_threshold=fixed_threshold)
        out_df = pd.DataFrame(rows_out)
        out_df["model"] = model_alias

        n_fastpath = sum(1 for r in rows_out if r["stage"].startswith("script:"))
        n_llm_only = sum(1 for r in rows_out if r["stage"] == "llm")
        n_disagree = sum(1 for r in rows_out if r["agrees_with_script"] is False)
        print(f"[{model_alias}] fast-path={n_fastpath}, llm-only={n_llm_only}, "
              f"llm-не-согласен-со-скриптом={n_disagree}, ошибок={len(llm_errors)}", file=sys.stderr)

        ev = out_df.dropna(subset=["true_label", "predicted_label"])
        if not ev.empty:
            p, r, f1 = _prf1(ev["true_label"].astype(int).tolist(), ev["predicted_label"].astype(int).tolist())
            print(f"[{model_alias}] Итоговые метрики: P={p:.3f} R={r:.3f} F1={f1:.3f}", file=sys.stderr)

        out_path = pathlib.Path(tmp) / "output.csv"
        out_df.to_csv(out_path, index=False)
        return out_path.read_bytes()


@app.local_entrypoint()
def main(
    model_alias: str = "qwen36",
    input_path: str = "data/valid.parquet",
    output_path: str = "report.csv",
    max_model_len: int = 0,
    concurrency: int = 32,
    threshold: float = 0.5,
):
    in_p = pathlib.Path(input_path)
    ext = in_p.suffix
    data = in_p.read_bytes()
    print(f"-> Modal [{model_alias}]: {input_path} ({len(data)} байт)")

    csv_bytes = run_predict.remote(
        model_alias, data, ext,
        max_model_len=(max_model_len or None),
        concurrency=concurrency,
        fixed_threshold=threshold,
    )
    out_p = pathlib.Path(output_path)
    out_p.write_bytes(csv_bytes)
    print(f"Готово: {output_path}")

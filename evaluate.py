#!/usr/bin/env python
"""Оценка детектора галлюцинаций на валидационном датасете БЕЗ формирования сабмита.

Два режима backend'а (см. предыдущие версии докстринга) — оба запускаются
с Modal, Nebius используется только как источник модели через её
OpenAI-совместимый API.

Устойчивость к сбоям на отдельных примерах: одна проблема на конкретном
примере (например, превышение max_model_len для аномально длинного prompt+
response, или временная ошибка сети даже после ретраев в client.py) больше
НЕ прерывает весь прогон — пример помечается как n_unparsed_none (score=0.0
по умолчанию, что при F1 консервативно засчитывается как label=0), а расчёт
метрик и запись отчёта идёт по всем успешно посчитанным примерам.
"""
import argparse
import json
import os
import sys
import time
import traceback
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT))
from client import DetectorClient  # noqa: E402
from server import start_vllm, wait_ready, stop_vllm  # noqa: E402


def build_text(prompt: str, response: str) -> str:
    return f"<prompt>\n{prompt}\n</prompt>\n\n<response>\n{response}\n</response>"


def read_table(p: str) -> pd.DataFrame:
    return pd.read_parquet(p) if str(p).endswith(".parquet") else pd.read_csv(p)


def measure_lengths(df: pd.DataFrame, tokenizer) -> dict:
    lens = []
    for prompt, response in zip(df["prompt"], df["response"]):
        text = build_text(prompt, response)
        lens.append(len(tokenizer.encode(text)))
    lens = np.array(lens)
    return {
        "p50": int(np.percentile(lens, 50)),
        "p90": int(np.percentile(lens, 90)),
        "p99": int(np.percentile(lens, 99)),
        "max": int(lens.max()),
        "n_over_16384": int((lens > 16384).sum()),
        "n_over_24576": int((lens > 24576).sum()),
        "n_over_32768": int((lens > 32768).sum()),
    }


def compute_metrics(y_true: np.ndarray, y_pred: np.ndarray) -> dict:
    tp = int(((y_pred == 1) & (y_true == 1)).sum())
    fp = int(((y_pred == 1) & (y_true == 0)).sum())
    fn = int(((y_pred == 0) & (y_true == 1)).sum())
    tn = int(((y_pred == 0) & (y_true == 0)).sum())
    precision = tp / (tp + fp) if (tp + fp) > 0 else 0.0
    recall = tp / (tp + fn) if (tp + fn) > 0 else 0.0
    f1 = 2 * precision * recall / (precision + recall) if (precision + recall) > 0 else 0.0
    return {"tp": tp, "fp": fp, "fn": fn, "tn": tn, "precision": precision, "recall": recall, "f1": f1}


def sweep_thresholds(scores: np.ndarray, y_true: np.ndarray, grid: np.ndarray) -> dict:
    best = {"threshold": 0.5, "f1": -1.0}
    curve = []
    for t in grid:
        y_pred = (scores >= t).astype(int)
        m = compute_metrics(y_true, y_pred)
        curve.append({"threshold": float(t), **m})
        if m["f1"] > best["f1"]:
            best = {"threshold": float(t), **m}
    return {"best": best, "curve": curve}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--input", required=True, help="valid датасет (id, prompt, response, label)")
    ap.add_argument("--model-path", default=None,
                     help="путь к весам для локального vLLM (нужен, если НЕ указан --base-url)")
    ap.add_argument("--prompt-path", required=True, help="путь к системному промпту (prompt_fixed.md)")
    ap.add_argument("--report-path", default="runs/report.json")
    ap.add_argument("--scores-path", default="runs/scores.parquet")
    ap.add_argument("--model-name", default="detector")
    ap.add_argument("--port", type=int, default=8000)
    ap.add_argument("--tp", type=int, default=1)
    ap.add_argument("--concurrency", type=int, default=32)
    ap.add_argument("--threshold", type=float, default=0.5)
    ap.add_argument("--sweep-thresholds", action="store_true")
    ap.add_argument("--max-model-len", type=int, default=16384)
    ap.add_argument("--gpu-util", type=float, default=0.90)
    ap.add_argument("--max-num-seqs", type=int, default=64)
    ap.add_argument("--enable-thinking", action="store_true")
    ap.add_argument("--max-tokens-thinking", type=int, default=1024)
    ap.add_argument("--base-url", default=None)
    ap.add_argument("--api-key", default=None)
    ap.add_argument("--request-timeout", type=float, default=120.0)
    ap.add_argument("--measure-lengths-only", action="store_true")
    ap.add_argument("--vllm-log", default="runs/vllm.log")
    ap.add_argument("--fail-fast", action="store_true",
                     help="прервать прогон при первой ошибке на примере (по умолчанию — НЕ прерывать)")
    args = ap.parse_args()

    if args.base_url is None and args.model_path is None:
        raise SystemExit("нужно указать либо --model-path (локальный vLLM), либо --base-url (удалённый API)")

    Path("runs").mkdir(exist_ok=True)
    Path(args.report_path).parent.mkdir(parents=True, exist_ok=True)

    df = read_table(args.input)
    for col in ("id", "prompt", "response", "label"):
        if col not in df.columns:
            raise SystemExit(f"во входе нет колонки '{col}' (нужна для расчёта метрик)")

    if args.measure_lengths_only:
        from transformers import AutoTokenizer
        tok = AutoTokenizer.from_pretrained(args.model_path)
        stats = measure_lengths(df, tok)
        print(json.dumps(stats, ensure_ascii=False, indent=2))
        Path(args.report_path).write_text(json.dumps({"length_stats": stats}, ensure_ascii=False, indent=2))
        return

    system_prompt = Path(args.prompt_path).read_text(encoding="utf-8")

    proc = None
    base = args.base_url
    backend = "remote" if base else "local"
    startup_time = None
    t_total0 = time.time()

    if base is None:
        print(f"[eval] backend=local, старт vLLM: {args.model_path} (tp={args.tp}) на :{args.port}", flush=True)
        proc = start_vllm(
            args.model_path, args.model_name, args.port, tp=args.tp,
            max_model_len=args.max_model_len, gpu_util=args.gpu_util,
            max_num_seqs=args.max_num_seqs, log_path=args.vllm_log,
        )
        startup_time = wait_ready(args.port)
        base = f"http://127.0.0.1:{args.port}/v1"
        print(f"[eval] vLLM готов за {startup_time:.1f}s", flush=True)
    else:
        print(f"[eval] backend=remote, base_url={base}, model={args.model_name}", flush=True)

    api_key = args.api_key or os.environ.get("NEBIUS_API_KEY") or os.environ.get("OPENAI_API_KEY") or "EMPTY"

    try:
        client = DetectorClient(
            model=args.model_name, system_prompt=system_prompt, base_url=base, api_key=api_key,
            enable_thinking=args.enable_thinking, max_tokens_thinking=args.max_tokens_thinking,
            request_timeout=args.request_timeout,
        )
        texts = [build_text(p, r) for p, r in zip(df["prompt"], df["response"])]
        scores = [None] * len(df)
        errors = [None] * len(df)

        def task(i):
            if args.fail_fast:
                return i, client.score(texts[i])
            try:
                return i, client.score(texts[i])
            except Exception as e:  # noqa: BLE001 — не даём одному примеру убить весь прогон
                return i, ("__ERROR__", f"{type(e).__name__}: {e}")

        t_inf0 = time.time()
        n_errors = 0
        with ThreadPoolExecutor(max_workers=args.concurrency) as ex:
            futs = {ex.submit(task, i): i for i in range(len(df))}
            for n, f in enumerate(as_completed(futs), 1):
                i, result = f.result()
                if isinstance(result, tuple) and len(result) == 2 and result[0] == "__ERROR__":
                    scores[i] = None
                    errors[i] = result[1]
                    n_errors += 1
                    print(f"[eval] ПРЕДУПРЕЖДЕНИЕ: id={df['id'].iloc[i]} упал ({result[1]}), score=None", flush=True)
                else:
                    scores[i] = result
                if n % 100 == 0:
                    print(f"[eval] {n}/{len(df)} (ошибок: {n_errors})", flush=True)
        inference_time = time.time() - t_inf0

        scores_arr = np.array([s if s is not None else 0.0 for s in scores])
        none_count = sum(1 for s in scores if s is None)
        y_true = df["label"].astype(int).values

        report = {
            "backend": backend,
            "model_name": args.model_name,
            "base_url": args.base_url,
            "n_examples": len(df),
            "n_unparsed_none": none_count,
            "n_errors": n_errors,
            "sample_errors": [e for e in errors if e][:10],
            "startup_time_sec": startup_time,
            "inference_time_sec": inference_time,
            "total_time_sec": time.time() - t_total0,
            "avg_sec_per_example": inference_time / max(len(df), 1),
            "config": {
                "max_model_len": args.max_model_len if backend == "local" else None,
                "gpu_util": args.gpu_util if backend == "local" else None,
                "max_num_seqs": args.max_num_seqs if backend == "local" else None,
                "concurrency": args.concurrency,
                "enable_thinking": args.enable_thinking,
                "threshold_default": args.threshold,
            },
        }

        y_pred_default = (scores_arr >= args.threshold).astype(int)
        report["metrics_at_default_threshold"] = compute_metrics(y_true, y_pred_default)

        if args.sweep_thresholds:
            grid = np.round(np.arange(0.05, 0.96, 0.02), 3)
            sweep = sweep_thresholds(scores_arr, y_true, grid)
            report["threshold_sweep_best"] = sweep["best"]
            report["threshold_sweep_curve"] = sweep["curve"]

        Path(args.report_path).write_text(json.dumps(report, ensure_ascii=False, indent=2))
        pd.DataFrame({
            "id": df["id"].values, "score": scores_arr, "label": y_true,
            "error": errors,
        }).to_parquet(args.scores_path, index=False)

        print(json.dumps(
            {k: v for k, v in report.items() if k != "threshold_sweep_curve"},
            ensure_ascii=False, indent=2,
        ))
        print(f"[eval] отчёт -> {args.report_path}; сырые скоры -> {args.scores_path}")
    except Exception:
        print("[eval] КРИТИЧЕСКАЯ ошибка вне цикла по примерам:", flush=True)
        traceback.print_exc()
        raise
    finally:
        stop_vllm(proc)


if __name__ == "__main__":
    main()

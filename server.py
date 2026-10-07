"""Подъём/ожидание/остановка локального vLLM OpenAI-совместимого сервера.

Лог vLLM дублируется (tee) в stdout процесса-родителя, а не только в файл —
иначе в консоли Modal кажется, что "ничего не происходит", хотя vLLM просто
долго грузит веса и компилирует CUDA-графы. Плюс heartbeat в wait_ready.

VLLM_USE_FLASHINFER_SAMPLER=0 отключён по умолчанию: FlashInfer JIT-компилирует
top-k/top-p sampling kernel через nvcc при старте engine, а в образах без
полного CUDA toolkit (только PyTorch CUDA runtime-библиотеки, как в стандартном
pip-окружении на Modal) nvcc отсутствует -> RuntimeError "Could not find nvcc".
Отключение JIT-сэмплера переключает на обычный PyTorch-сэмплер без
компиляции — для greedy-декодинга (temperature=0.0, наш случай) это не
влияет на корректность, только чуть медленнее при top-k/top-p с большими k/p.
"""
from __future__ import annotations

import os
import subprocess
import sys
import threading
import time
import urllib.request
from typing import Optional


def start_vllm(
    model_path: str,
    served_name: str,
    port: int,
    tp: int = 1,
    max_model_len: int = 16384,
    gpu_util: float = 0.90,
    max_num_seqs: int = 64,
    enable_prefix_caching: bool = True,
    language_model_only: bool = True,
    extra_args: Optional[list] = None,
    log_path: Optional[str] = None,
    echo: bool = True,
    disable_flashinfer_sampler: bool = True,
    extra_env: Optional[dict] = None,
) -> subprocess.Popen:
    """Стартует vLLM в подпроцессе. FP8-квантизация автодетектится из config.json.

    disable_flashinfer_sampler=True ставит VLLM_USE_FLASHINFER_SAMPLER=0 в
    окружении подпроцесса — обходит требование nvcc при JIT-компиляции
    sampler-кернела (см. докстринг модуля).
    """
    cmd = [
        sys.executable, "-m", "vllm.entrypoints.openai.api_server",
        "--model", str(model_path),
        "--served-model-name", served_name,
        "--port", str(port),
        "--max-model-len", str(max_model_len),
        "--tensor-parallel-size", str(tp),
        "--gpu-memory-utilization", str(gpu_util),
        "--max-num-seqs", str(max_num_seqs),
    ]
    if enable_prefix_caching:
        cmd.append("--enable-prefix-caching")
    if language_model_only:
        cmd.append("--language-model-only")
    if extra_args:
        cmd += list(extra_args)

    env = os.environ.copy()
    if disable_flashinfer_sampler:
        env["VLLM_USE_FLASHINFER_SAMPLER"] = "0"
    if extra_env:
        env.update(extra_env)

    if not echo and not log_path:
        return subprocess.Popen(cmd, env=env)

    proc = subprocess.Popen(
        cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
        text=True, bufsize=1, env=env,
    )
    f = open(log_path, "w", encoding="utf-8") if log_path else None

    def _pump():
        try:
            for line in proc.stdout:
                if echo:
                    print(f"[vllm] {line}", end="", flush=True)
                if f:
                    f.write(line)
                    f.flush()
        finally:
            if f:
                f.close()

    t = threading.Thread(target=_pump, daemon=True)
    t.start()
    return proc


def wait_ready(port: int, timeout: int = 1200, heartbeat: int = 30) -> float:
    """Ждёт, пока /v1/models начнёт отвечать 200. Возвращает время старта в секундах."""
    url = f"http://127.0.0.1:{port}/v1/models"
    t0 = time.time()
    last_hb = t0
    while time.time() - t0 < timeout:
        try:
            with urllib.request.urlopen(url, timeout=5) as r:
                if r.status == 200:
                    return time.time() - t0
        except Exception:  # noqa: BLE001
            pass
        now = time.time()
        if now - last_hb >= heartbeat:
            print(f"[eval] ...ожидание готовности vLLM, прошло {now - t0:.0f}s", flush=True)
            last_hb = now
        time.sleep(3)
    raise TimeoutError(f"vLLM not ready on :{port} within {timeout}s")


def stop_vllm(proc: Optional[subprocess.Popen]):
    if proc is None:
        return
    proc.terminate()
    try:
        proc.wait(timeout=30)
    except Exception:  # noqa: BLE001
        proc.kill()

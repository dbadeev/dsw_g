#!/usr/bin/env bash
# compare_all.sh (v2) — теперь 4 модели, включая оригинал yandex/YandexGPT-5-Lite-8B-instruct
set -e

INPUT_PATH="${1:-data/valid.parquet}"
mkdir -p reports

echo "=== 1/3: скачивание весов (идемпотентно) ==="
modal run 13_modal_app_multi_model.py::download_model --model-alias qwen36         || true
modal run 13_modal_app_multi_model.py::download_model --model-alias qwen38         || true
modal run 13_modal_app_multi_model.py::download_model --model-alias saiga8b        || true
modal run 13_modal_app_multi_model.py::download_model --model-alias yandexgpt5lite || true

echo "=== 2/3: прогон каждой модели по отдельности ==="
for alias in qwen36 qwen38 saiga8b yandexgpt5lite; do
    echo "--- $alias ---"
    modal run 13_modal_app_multi_model.py::main \
        --model-alias "$alias" \
        --input-path "$INPUT_PATH" \
        --output-path "reports/report_${alias}.csv" \
        --concurrency 32 --threshold 0.5
done

echo "=== 3/3: сборка сравнительной таблицы ==="
python compare_reports.py \
    reports/report_qwen36.csv \
    reports/report_qwen38.csv \
    reports/report_saiga8b.csv \
    reports/report_yandexgpt5lite.csv \
    --output reports/comparison_summary.csv

echo "Готово. См. reports/comparison_summary.csv"

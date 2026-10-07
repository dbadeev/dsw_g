"""
compare_reports.py — склеивает CSV-отчёты нескольких моделей (каждый со
столбцами id, domain, true_label, predicted_label, stage, llm_score,
agrees_with_script, all_flags, correct, error, model) в одну сравнительную
таблицу и печатает сводную статистику.

Запуск:
    python compare_reports.py reports/report_qwen36.csv reports/report_qwen38.csv \
        reports/report_saiga8b.csv --output reports/comparison_summary.csv

Выход:
  1. comparison_summary.csv (wide-формат): по одной строке на id, колонки
     {model}_score, {model}_pred, {model}_correct для каждой модели —
     удобно смотреть построчно, где модели расходятся.
  2. Печатает в консоль:
     - Итоговые P/R/F1 по каждой модели (по всем строкам).
     - P/R/F1 отдельно ТОЛЬКО по script-flagged строкам (agrees_with_script) —
       прямой ответ на вопрос "насколько модель верно оценивает скриптовые
       случаи", если бы decision целиком делегировали LLM.
     - P/R/F1 по каждому домену для каждой модели.
"""
import argparse
import pandas as pd


def _prf1(y_true, y_pred):
    tp = sum(1 for t, p in zip(y_true, y_pred) if t == 1 and p == 1)
    fp = sum(1 for t, p in zip(y_true, y_pred) if t == 0 and p == 1)
    fn = sum(1 for t, p in zip(y_true, y_pred) if t == 1 and p == 0)
    precision = tp / (tp + fp) if (tp + fp) else 0.0
    recall = tp / (tp + fn) if (tp + fn) else 0.0
    f1 = 2 * precision * recall / (precision + recall) if (precision + recall) else 0.0
    return precision, recall, f1


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("reports", nargs="+", help="Пути к CSV-отчётам разных моделей")
    parser.add_argument("--output", default="comparison_summary.csv")
    args = parser.parse_args()

    dfs = [pd.read_csv(p) for p in args.reports]
    model_names = [df["model"].iloc[0] for df in dfs]
    print(f"Модели в сравнении: {model_names}\n")

    # --- 1. Общие метрики по каждой модели (все строки) ---
    print("=== Итоговые метрики по всем строкам ===")
    for name, df in zip(model_names, dfs):
        ev = df.dropna(subset=["true_label", "predicted_label"])
        if ev.empty:
            print(f"{name}: нет строк с одновременно true_label и predicted_label")
            continue
        p, r, f1 = _prf1(ev["true_label"].astype(int).tolist(), ev["predicted_label"].astype(int).tolist())
        print(f"{name}: P={p:.3f} R={r:.3f} F1={f1:.3f} (n={len(ev)})")

    # --- 2. Метрики ТОЛЬКО по LLM-предсказанию на script-flagged строках ---
    print("\n=== Насколько LLM согласен со скриптами (только script:* строки) ===")
    for name, df in zip(model_names, dfs):
        script_rows = df[df["stage"].astype(str).str.startswith("script:")]
        if script_rows.empty:
            continue
        agree_rate = script_rows["agrees_with_script"].mean()
        n_disagree = (script_rows["agrees_with_script"] == False).sum()  # noqa: E712
        print(f"{name}: согласие с скриптами {agree_rate:.1%} ({len(script_rows)} строк, "
              f"{n_disagree} расхождений)")
        if n_disagree > 0:
            print("  Расхождения (script says 1, LLM says что-то другое):")
            for _, row in script_rows[script_rows["agrees_with_script"] == False].iterrows():  # noqa: E712
                print(f"    {row['id']}: true={row['true_label']} llm_score={row['llm_score']} "
                      f"stage={row['stage']}")

    # --- 3. Метрики по доменам ---
    print("\n=== Метрики по доменам ===")
    for name, df in zip(model_names, dfs):
        ev = df.dropna(subset=["true_label", "predicted_label"])
        for domain, group in ev.groupby("domain"):
            p, r, f1 = _prf1(group["true_label"].astype(int).tolist(), group["predicted_label"].astype(int).tolist())
            print(f"{name} / {domain}: P={p:.3f} R={r:.3f} F1={f1:.3f} (n={len(group)})")

    # --- 4. Сборка wide-таблицы для построчного сравнения ---
    base = dfs[0][["id", "domain", "true_label", "all_flags"]].drop_duplicates(subset="id")
    for name, df in zip(model_names, dfs):
        cols = df[["id", "predicted_label", "llm_score", "correct"]].rename(columns={
            "predicted_label": f"{name}_pred",
            "llm_score": f"{name}_score",
            "correct": f"{name}_correct",
        })
        base = base.merge(cols, on="id", how="outer")

    base.to_csv(args.output, index=False)
    print(f"\nСводная таблица сохранена: {args.output}")

    # Строки, где модели расходятся между собой (полезно для ручного разбора)
    pred_cols = [f"{name}_pred" for name in model_names]
    if len(pred_cols) > 1:
        disagreements = base[base[pred_cols].nunique(axis=1) > 1]
        print(f"\nСтрок, где модели расходятся друг с другом: {len(disagreements)} из {len(base)}")
        if not disagreements.empty:
            disagreements.to_csv(args.output.replace(".csv", "_disagreements.csv"), index=False)
            print(f"Сохранено отдельно: {args.output.replace('.csv', '_disagreements.csv')}")


if __name__ == "__main__":
    main()

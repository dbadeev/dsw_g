---
pretty_name: Agent Trajectories
---

# Agent Trajectories Dataset — Processing & Format Documentation

## Overview

| Benchmark | Records | Models | Passes | Avg Turns | Reward Type | Success Rate |
|---|---|---|---|---|---|---|
| tau2bench | 984 | 5 | 4 | 32.0 | binary (0/1) | 39.1% |
| swebench | 747 | 5 | 4 | 69.6 | binary (0/1) | 21.4% |
| terminalbench | 1,429 | 5 | 4 | 33.4 | binary (0/1) | 19.2% |
| mathhay | 1,324 | 5 | 4 | 3.8 | binary (0/1) | 46.5% |
| search | 3,270 | 5 | 4 | 15.0 | binary (0/1) | 22.1% |
| mcpbench | 899 | 5 | 4 | 26.1 | continuous (0–10) | 13.1% |
| **Total** | **8,653** | | | | | |

**Models**: DeepSeek-R1, DeepSeek-V3.2, Gemini-2.5-Flash, Qwen3-235B, Qwen3-Next

This metadata release keeps the same 8,653 trajectory IDs as the previous cleaned dataset and preserves the same 14-field trajectory schema with one metadata field, `trace_meta`, to retain raw trace metadata that was previously dropped during cleaning.

In addition to the per-benchmark JSONL/Parquet files, the release ships two dataset-level sidecar files:
- `global_tool_inventory.json`, the blind agent-facing tool pool intended for evaluation
- `global_tool_inventory_with_benchmark.json`, a companion analysis file that also records benchmark provenance

---

## Source Data

Raw data lives in `parallel_scaling_results/`, organized as:
```
{Model}_{benchmark}_distraction_{scope}/
    pass_{1..4}/
        evaluations/   # eval results (reward, test output, etc.)
        traces/        # agent conversation traces (messages)
```

Each task was run 4 times (4 passes) per model under a **distraction condition** — irrelevant content was injected into the agent's context to test robustness.

---

## Processing Pipeline

### Step 1: Load & Pair Files

For each `(model, benchmark, pass)`:
- **Eval file** → reward, test results, benchmark-specific metadata
- **Trace file** → conversation messages (the agent trajectory)

Files are paired by matching filename. The search benchmark required special handling (see below).

### Step 2: Clean Distraction Artifacts

The distraction condition injected two types of artifacts into **user messages**:

| Artifact | Description | Example |
|---|---|---|
| `<reasoning>...</reasoning>` | Fake reasoning blocks injected into user turns | Model's internal reasoning inserted as distraction |
| `<tool_response_begin>...<tool_response_end>` | Fake tool responses injected into user turns | Fabricated tool output to mislead the agent |

**Cleaning strategy** (zero-hallucination guarantee):
1. Regex-match only closed tag pairs: `<reasoning>.*?</reasoning>` and `<tool_response_begin>.*?<tool_response_end>`
2. Remove matched content — pure deletion, no content generation
3. Clean up leftover separator lines (`---`) and excess newlines
4. Log every removal in `cleaning_info` field (message index, position, length)
5. All other content is preserved byte-identical to source

**What is NOT cleaned** (preserved as-is):
- DeepSeek special tokens (`<｜tool▁calls▁begin｜>`, `<｜tool▁sep｜>`, etc.) — these are legitimate model output
- Any `<reasoning>` or similar tags in **assistant** messages — these are part of the model's own response format
- Super long messages — no truncation applied

**Cleaning stats**: 191 records affected (all in tau2bench), 542 reasoning blocks + 2 tool_response blocks removed.

### Step 3: Extract & Assemble Record

Each record is assembled from trace + eval into a 14-field schema (see Record Schema below). Relative to the previous release, the only new top-level field is `trace_meta`.

### Step 4: Filter Incomplete Trajectories

Removed 1,445 records (14.3%) where the agent did not produce a final answer:
- Empty traces (API never responded): 121
- Crashed before first response: 193
- Repeated API failure (harness gave up): 15
- Truncated mid-conversation (API disconnected, no final answer): 1,116

All removed records have reward=0 (except 61 with unreliable reward>0 due to incomplete trajectories). See `CLEANING_SUMMARY.md` for full details.

### Step 5: Output

- **JSONL**: one JSON object per line, human-readable
- **Parquet**: messages/eval_details/trace_meta/cleaning_info stored as JSON strings, all scalar fields as native types
- Split by benchmark (6 files each format)
- **Sidecars**:
- `global_tool_inventory.json`, a blind dataset-level tool inventory file for agent-facing evaluation
- `global_tool_inventory_with_benchmark.json`, a provenance-preserving companion file for analysis

---

## Record Schema (14 fields)

```json
{
  "id": "tau2bench__DeepSeek-R1__airline__0__pass1",
  "benchmark": "tau2bench",
  "domain": "airline",
  "task_id": "0",
  "source_model": "DeepSeek-R1",
  "pass": 1,
  "messages": [ ... ],
  "num_turns": 14,
  "reward": 1.0,
  "eval_details": { ... },
  "trace_meta": { ... },
  "cleaning_info": null,
  "num_passes_available": 4,
  "has_all_4_passes": true
}
```

| Field | Type | Description |
|---|---|---|
| `id` | string | Unique record ID: `{benchmark}__{model}__{domain}__{task_id}__pass{n}` |
| `benchmark` | string | Which benchmark: tau2bench, swebench, terminalbench, mathhay, search, mcpbench |
| `domain` | string | Task domain (e.g. "airline", "django", "browsecomp") |
| `task_id` | string | Original task identifier from the benchmark |
| `source_model` | string | The LLM that generated this trajectory |
| `pass` | int | Which independent run (1–4). Same task run 4 times from scratch to measure variance. |
| `messages` | list | Full agent conversation in standard chat format. All trajectories end with an assistant message. |
| `num_turns` | int | Number of messages in the conversation |
| `reward` | float | Ground truth score. Binary 0/1 for most benchmarks; continuous 0–10 for mcpbench. |
| `eval_details` | dict | Full benchmark-specific evaluation metadata (test output, patches, sub-scores, etc.) |
| `trace_meta` | dict/null | Raw trace metadata preserved from the source trace file, excluding `trace.messages` which remains in
...[+14139 chars]
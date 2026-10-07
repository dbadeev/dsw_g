---
license: mit
tags:
  - kullback
  - environment
  - agent-evaluation
  - rl-environment
  - retail
configs:
  - config_name: tasks
    data_files:
      - split: tasks
        path: tasks.jsonl
---

# retail

An executable Environment for tool-using agents, rebuilt from traces by [Kullback](https://github.com/leiblerdev/kullback) and published by [Leibler](https://leibler.dev): the world, the Tasks and a code Verifier per Task, no recordings. `tasks.jsonl` lists the Tasks.

Release: replays at least 90% of its Tasks.

| | |
| --- | --- |
| Fidelity over Tasks | 100.0% (223 of 223) |
| Fidelity over Runs | 100.0% (456 of 456) |
| Call fidelity | 100.00% of 3220 |
| Reference confirmed | 223 |
| Verifier derived | 222 |
| Trusted | 193 |
| Refused | 0 |
| Not trusted | 30 of 223; 15 the Verifier passed the suite and is not the trusted one; 7 the D79 suite did not pass: loophole_probe_fails; 3 the D79 suite did not pass: loophole_probe_fails, plausible_wrong_fails |
| Tasks and trusted by difficulty | w0t0p2+ 1 and 0, w0t2p2+ 2 and 1, w0t3+p2+ 46 and 40, w1t1p1 3 and 0, w1t2p2+ 1 and 0, w1t3+p2+ 95 and 87, w2t3+p2+ 41 and 37, w3+t3+p2+ 33 and 28 |
| Leak scan | 0 recorded strings, 0 short values, 23763 checked in 447 files against 31361 |
| Tag | build-20260924, counts from the workdir status, no round closed |
| Corpus | tau2-bench (MIT), https://github.com/sierra-research/tau2-bench |
| Built | 2026-09-24T15:16:57+00:00 by kullback 0.1.0, git d6bddf073f53cbd5 |
| Content hash | 6d1b040cbd671b4a |

Untrusted Tasks are not graded, and the simulated user does not ship, so a fetched package cannot finish a Task that needs a fact the user gives mid conversation, though the Task still carries a Verifier.

```bash
uv run kullback fetch leibler/retail --out env-retail
uv run kullback run --workdir env-retail --task <task id> --model provider/model
uv run kullback verdict --workdir env-retail
uv run kullback report --workdir env-retail
```

`fetch` checks the content hash; `--revision round-<n>` fetches an earlier round.


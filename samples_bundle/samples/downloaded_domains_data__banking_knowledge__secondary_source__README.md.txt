---
license: apache-2.0
language:
  - en
task_categories:
  - text-generation
  - other
tags:
  - rl
  - tool-use
  - banking
  - synthetic
  - nemo-gym
  - agent
size_categories:
  - n<1K
pretty_name: NeMo Gym Indian Banking Agent Tasks
configs:
  - config_name: default
    data_files:
      - split: train
        path: train.jsonl
      - split: validation
        path: validation.jsonl
---

This is **`NPCI/nemo-gym-indian-banking`** — the dataset for the `indian_banking`
resources server in [NVIDIA NeMo Gym](https://github.com/NVIDIA-NeMo/Gym): 300 synthetic
multi-turn Indian retail-banking customer-support tasks (250 train / 50 validation), the
197-customer synthetic bank database and the 59-article knowledge base the environment
loads at startup.

# NeMo Gym Indian Banking Agent Tasks

Tool-calling customer-service tasks for an Indian retail-banking assistant, in the
[NVIDIA NeMo Gym](https://github.com/NVIDIA-NeMo/Gym) agent-input JSONL format. Each row is
one task: a system prompt (agent instructions + bank policy), the 34 banking tool schemas, a
simulated-customer scenario, and the evaluation criteria the `indian_banking` resources server
uses to compute the reward after a rollout.

The dataset is consumed by the `resources_servers/indian_banking` server in NeMo Gym. The `db.json` customer database and `kb.json` knowledge base the server loads at startup ship
in this repository alongside the splits (`agent_instruction.txt` and `policy.md` ship inside the
Gym repository). `gym dataset collate --download` fetches the splits; download `db.json` and
`kb.json` into `resources_servers/indian_banking/data/` before serving.

## Everything here is synthetic

**No real customer, account, card, loan, or personal data is present.** Every customer profile,
account number, card number, transaction, name, address, phone number, e-mail and identifier in
the customer database and in these tasks is synthetic. Any
resemblance to real persons or accounts is coincidental.

**Every bank, insurer, merchant, employer, telecom, card network and brand name is fictional**
(for example Streamvora, Vaylo Postpaid, Harvexa, Kalvira Life, Jeevanika Bima, Zyphrax /
Orvelix / Swarnix card networks). Public institutions and government schemes are referred to by
their real names (RBI, DICGC, NPCI, PPF, SSY, SCSS, APY, PMJJBY/PMSBY, PMJDY, Income Tax Act,
state electricity boards) because the banking rules the agent must follow are defined by them.
E-mail addresses use `example.com` / `example.in`; phone numbers use an obviously synthetic
placeholder range. The knowledge-base articles describe generic Indian banking products and
processes for a fictional bank; every article ends with the note "Figures are illustrative for a
synthetic environment; verify current regulations."

## Splits

| split        | rows | notes |
|--------------|-----:|-------|
| `train`      |  250 | 43 task families; 155 `rl_*` core tool-use tasks (all 50 `rl` scenario templates covered) + 95 behavioural tasks |
| `validation` |   50 | disjoint from `train`; 19 task families, all 6 reward bases represented; the 5 committed `example.jsonl` rows are a subset of this split |

There is no separate `test` split. `train` and `validation` are disjoint by `task_id` and were
drawn from a larger pool with a seeded, stratified selection that covers every task family /
reward-basis combination present in the pool, spreads customer ages (senior citizens are capped at about 19% of tasks), professions,
regions and name communities, and excludes scenarios with stereotyped framing.

Reward-basis distribution (which signals the reward is computed from):

| reward_basis                           | train | validation |
|----------------------------------------|------:|-----------:|
| ACTION+DB                              |   155 | 31 |
| ACTION+DB+NL_ASSERTION                 |    49 | 11 |
| ACTION+COMMUNICATE+DB+NL_ASSERTION     |    22 |  4 |
| DB+NL_ASSERTION                        |    11 |  1 |
| ACTION+NL_ASSERTION                    |     7 |  2 |
| ACTION+COMMUNICATE+NL_ASSERTION        |     6 |  1 |

## Row schema

One JSON object per line. Top-level keys:

| field | type | description |
|---|---|---|
| `responses_create_params` | object | OpenAI Responses-API style create params consumed by the policy. |
| `responses_create_params.input` | list | Exactly one message: `{"role": "system", "content": "<instructions>...</instructions>\n<policy>...</policy>"}`. The first user turn is injected at runtime from `opening_message`. |
| `responses_create_params.tools` | list[34] | Function-tool schemas (`type: "function"`, `name`, `description`, `parameters`). Identical across all rows. |
| `responses_create_params.parallel_tool_calls` | bool | Always `false`. |
| `task_id` | string | Unique task id. Prefix before the first `_` is the task family (e.g. `rl`, `kb`, `refuse`, `trap`, `mt2`). |
| `customer` | string | Active, already-authenticated customer id (`CUST_########`) in `db.json`. |
| `user_scenario` | object | Simulated-customer specification. |
| `user_scenario.persona` | string | Short behavioural persona for the user simulator (not part of the reward). |
| `user_scenario.instructions` | object | `domain` (`"banking"`), `reason_for_call`, `known_info`, `unknown_info`, `task_instructions` (the simulator ends the call with `###STOP###`). |
| `evaluation_criteria` | object | Reward specification. |
| `evaluation_criteria.actions` | list | Expected tool calls: `{action_id, name, arguments, compare_args}`; `compare_args` names which argument keys are compared, and a gold call that is expected to error carries `expect_error: true`. |
| `evaluation_criteria.communicate_info` | list[string] | Strings the agent must convey to the user (e.g. a policy number). |
| `evaluation_criteria.nl_assertions` | list[string] | Natural-language assertions checked by an LLM judge. |
| `evaluation_criteria.reward_basis` | list[string] | Subset of `ACTION`, `DB`, `COMMUNICAT
...[+5637 chars]
---
id: F-047
title: Development pilot of the access-conditions benchmark - on 5 development cases with labels written by the implementer, the agent (0.87), the fixed verify workflow (0.85) and one-pass retrieval (0.75) all far exceed keyword rules (0.15); no held-out result yet
status: exploratory
task: P3-28
date: 2026-11-07
checked_by: -
---

## Claim
**Development only; not evidence for H1.** The four methods were run once on the 5 development cases: Foxbit company
and individual cases, plus the funds' June cases. They were scored against labels written by Renzo's agent, the
implementer, which were corrected twice after seeing outputs. SAC is the share of answerable fields answered correctly
with a verbatim quote from a permitted source:

| Method | SAC | Unsupported positive claims | Reference unknowns kept unknown |
|---|---|---|---|
| B0 keyword rules | 0.147 | 0 | 8/8 |
| B1 one retrieval pass + one model call | 0.754 | 1 | 8/8 |
| B2 retrieve → extract → verify | 0.854 | 1 | 8/8 |
| A tool-using agent | 0.866 | 1 | 8/8 |

On development, A and B2 are about equal. All three unsupported positives sit on one contested field: whether the BCB
"'liberou'" in-book arbitrage makes a fund's own-account operation `supported` (the models' reading) or `conditional`
(the implementer's label). The scores are mechanical (PROVISIONAL). The semantic audit and the human reference are
pending.

## Evidence
- Protocol `results/P3-28_protocol.md` §9–§11 (v1 frozen in `c63aa70` before held-out runs; v1.1 scoring fixes after
  the independent review P3-36, with no method change). Scores, errors and costs:
  `results/tables/P3-28_{case_scores,errors,costs}_dev.csv`.
- Reproduce (needs `data/raw/p3_28/`, out of git):
  `P3_28_SCHEDULE='B0:1,B1:1,B2:1,A:1' .venv/bin/python scripts/p3_28_methods.py score data/processed/P3-28_dev_reference_agent.csv dev --tag _dev`.
- Model `claude-sonnet-5-5` via the Claude Code CLI 2.1.318, isolated (`--restricted`, no web, no shell, files confined
  to a sandbox). Runs take 4–102 s.

## Caveats
- One coder, who also built the methods; labels changed after outputs were seen; one run per case; 5 cases from 2
  document families. Held-out scores and a human reference may differ in either direction.
- Token use of B2 is under-recorded in these runs (second call only; fixed for future runs); `notional_usd` is complete.
- A quote found verbatim is not proof it supports the answer: the blinded audit (Nattan) decides that.

## Used in deck
Not used.

## History
- 2026-11-07 — Renzo's agent: created (P3-28 S3).

---
id: P3-39
title: Measure the buyer's cost budget for waiting
phase: P3
status: review
owner: Economist
working: -
due: 2026-11-07
depends: P3-31
---

## Goal
Task renamed P3-38 → P3-39 during synchronization to avoid the independently created access-review task. Existing P3-38 script/output prefixes are retained for reproducibility; no calculation changed.

Extend the existing buyer accounting with independently specified deposit and forward rates, a deadline/access gate and a scenario frontier in incremental terminal BRL costs. New user-authorized extension; no prediction fitting or change to frozen estimates.

## Specification (written before running)
Terminal obligation: 100,000 USDT; deadlines 5/10/20 observed PTAX dates after 25 June. Baseline net effective annual deposit rate 10%, forward BRL rate 10%, forward USD rate 5%, idle USDT yield 0%, symmetric conversion fee 10 bps. Rates and costs are hypothetical. Ideal cash-settled maturity-matched forward, not a replicated WDO strategy. Fixed hedge notional follows P3-31. Additional cost K is terminal BRL on top of conversion fees, divided by initial buy-now BRL outlay; count each cost once.

Map x is premium compression in bps (initial minus terminal), y is additional terminal cost K in bps. Hold FX and USDT/USD fixed for the central boundary. Envelope crosses deposit 0/5/10%, USDT holding yield 0/4%, terminal USDT/USD .995/1/1.005, FX -2/0/+2%, waiting fee 10/30 bps and waiting fixed fee R$0/100. These are stress assumptions, not probability bounds or market-calibrated confidence intervals. Forward rates remain fixed when deposit rates change. Show actual June premium and cost ceiling as retrospective markers. Unknown access or settlement after the deadline yields no actionable cost ranking.

## Subtasks
- [x] S1 — Inspect existing framework and record scope/spec — done: Codex, 7 Nov.
- [x] S2 — Implement frontier, costs, access/settlement gate and meaningful boundary tests — done: Codex, 7 Nov.
- [x] S3 — Produce figure/tables/finding and concise integration note; visually inspect and update status — done: Codex, 7 Nov.

## Success criteria
- [x] Rates independent; hand arithmetic and prior default agree.
- [x] Same terminal USDT quantity; invalid/missing inputs and delivery failures handled.
- [x] Map and historical markers trace to CSVs; conditional scope visible.

## Outputs
- `scripts/p3_38_buyer_frontier.py`, `results/tables/P3-38_*.csv`, `results/figures/P3-38_buyer_frontier.png`
- `findings/F-048-buyer-cost-frontier.md`, `docs/buyer-cost-frontier.md`

## Handoff
- **State:** script, ten checks, CSVs, figure, F-048 and note complete; frontier visually inspected. F-039 wording corrected, estimates unchanged. Felipe authorized pushing for teammate review on 7 Nov.
- **Next step:** teammate reproduces P3-38, then Felipe decides whether to replace the treasury illustration. Actual access/quotes remain unresolved.
- **Open questions:** real executable quotes, institutional access, taxes and settlement calendars unavailable; scenarios only.
- **How to resume:** run the new script with `--test-only`, then without arguments.

## Log
- 2026-11-07 — Codex for Felipe: claimed new P3-38 after pulling 1ccbddd; preserves untracked scratch/ and Renzo's P3-37 work. Prior one-time push authorization not assumed to cover this new extension.

## Result
F-048: central retrospective cost ceilings positive, but each observed June compression has a stress range spanning zero. The ranking depends on institutional assumptions. This is a scenario boundary and delivery gate, not validated trading advice.

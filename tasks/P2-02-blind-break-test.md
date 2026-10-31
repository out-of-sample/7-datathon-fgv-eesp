---
id: P2-02
title: Blind structural-break test on the premium
phase: P2
status: todo
owner: CS 2
working: -
due: 2026-11-01
depends: P1-02, P1-04
---

## Goal
Let an algorithm find the dates where the premium changed regime **without telling it the policy dates**,
then check which breaks match known events. If it finds 24 Jun 2026 on its own, that is our headline chart.

## Subtasks
- [ ] S1 — **Before running**, write the specification here: method (Bai-Perron via R `strucchange`, or Python
   `ruptures`), minimum segment = 20 trading days, maximum breaks = 8, number of breaks chosen by BIC.
- [ ] S2 — Run on the daily premium (P1-02). Report break dates with confidence intervals.
- [ ] S3 — Match breaks to the P1-04 events (within +/-5 trading days). List unmatched breaks as "unexplained".
- [ ] S4 — Robustness: the alternative time-matching variant of the premium.

## Success criteria
- [ ] Specification committed before the first run
- [ ] `results/tables/P2-02_breaks.csv` (date, CI, matched event or "unexplained")
- [ ] `results/figures/P2-02_premium_breaks.png` (premium, noise band, breaks, event markers)
- [ ] Finding written

## Outputs
- `scripts/p2_02_breaks.py` (or `.R`), table, figure, finding

## Handoff
<!-- Overwrite at the end of every session, finished or not, so anyone can continue from here. -->
- **State:** not started
- **Next step:** S1
- **Open questions:** none
- **How to resume:** -

## Log
- 2026-10-31, agent for Renzo (note from P2-01, nobody working here yet): Binance cut the USDT/BRL price tick
  tenfold on ~27 Jun 2025 (0.001 → 0.0001 BRL; F-007). The premium steps down around Jul 2025 (P1-02 figures).
  If the break test finds a break there, the tick change is a candidate explanation besides any rule.

## Result

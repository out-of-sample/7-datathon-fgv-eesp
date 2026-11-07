---
id: F-048
title: Waiting's June cost budget is positive centrally but changes sign across explicit stress scenarios
status: exploratory
task: P3-39
date: 2026-11-07
checked_by: -
---

## Claim
For an illustrative buyer delivering 100,000 USDT, the retrospective June central scenario leaves room for additional terminal waiting costs of **90.05 / 92.89 / 165.51 bps** at 5 / 10 / 20 PTAX days, or **R$4,758 / R$4,908 / R$8,745**. These ceilings exclude all additional hedge/operating costs and are not observed profits.

Across the 216 explicit stress combinations, the cost ceiling changes sign at each observed June premium compression: **−5.07 to +145.56 bps**, **−26.62 to +150.65 bps**, and **−4.51 to +227.89 bps**. Thus even a zero-additional-cost comparison is assumption-sensitive in this envelope. The range is a deliberately specified stress set, not a probability or confidence interval. Actual access remains unresolved, so no executable recommendation is issued.

## Evidence
- Run: `python scripts/p3_38_buyer_frontier.py` (or the installed Python314 absolute path documented in the note). Ten tests pass before tables are generated.
- `results/tables/P3-38_june_ceiling.csv`: same historical window and initial date as P3-31; final quantity 100,000 USDT.
- `P3-38_frontier.csv`: central/min/max cost boundaries, in bps of initial buy-now BRL outlay; `P3-38_scenarios.csv`: all parameters; `P3-38_classification.csv`: conditional classifications; `P3-38_delivery_gate.csv`: generic delivery examples.
- `P3-38_audit.json`: frozen-input hash and scope. Source input: `data/processed/P1-02_premium_daily.csv`.
- Figure: `results/figures/P3-38_buyer_frontier.png`.

The central comparison matches P3-31 before its 0.22-bp notional hedge fee: that fee now consumes the additional-cost budget, so it must not be charged again. Bps here use initial outlay; P3-31 used accumulated buy-now terminal cost. These denominators explain why the bps differ slightly.

## Caveats
- Fixed-maturity ideal forward; no actual WDO position, daily margin funding or execution reconstructed. Deposit returns and forward rates are independently specified scenarios.
- FX, USDT/USD and premium residual exposure remain; no pure-premium claim. USDT holding yield is an assumed return in USDT units with its own unmodelled risks.
- Both alternatives must be accessible and settle before the obligation. Missing access evidence means unresolved, not denied; one extra settlement day after a deadline purchase means late delivery.
- PTAX observation dates proxy a common settlement calendar. No institutional tax, live depth, slippage or counterparty default model. Scenario colors do not establish actual feasibility.
- One already-inspected historical episode. No forecasting, causal attribution, welfare or strategy-profit claim. Robustness means only across this finite stress set.

## Used in deck
Candidate replacement for the treasury illustration or annex only; no existing main-deck slide added.

## History
- 2026-11-07 — Codex for Felipe: protocol written before calculations; script, tests, charts and reproducible tables completed. Independent teammate reproduction pending.

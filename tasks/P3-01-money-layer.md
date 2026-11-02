---
id: P3-01
title: Cost of a digital dollar: bank route vs USDT route, per regime
phase: P3
status: review
owner: Economist
working: -
due: 2026-11-03
depends: P2-03, P2-04
---

## Goal
Turn the premium into money for a Brazilian corporate treasurer: (1) headline cost of the 23 Jun 2026 BCB notice on a US$ 100,000 USDT purchase (+93.9 bps = R$ 5,052 during the 20-day spike), and (2) neutral, fully sourced comparison of transaction frictions across traditional bank routes (PTAX + BCB corporate spread `R-01` + SWIFT wire `R-01b` + statutory IOF `R-02`) vs the digital dollar route (USDT premium + exchange fees + network fee), plus explicitly labelled policy scenarios (3.5% crypto IOF proposal `E-03` and 24h precautionary hold under Res. BCB 584/2026 `R-07`). Plan: `docs/02-dolar-cripto.md` §7.6 & §10.

## Pre-Run Specification
1. **Benchmark Transaction**:
   - Notion: US$ 100,000 institutional/treasury acquisition.
   - Reference FX: `PTAX = R$ 5.3800` (live bid/ask benchmark from Binance D-10; base BRL cost = R$ 538,000).
2. **Traditional Bank Route Benchmarks (Sources R-01, R-01b, R-02, R-03 — opened 2 Nov 2026)**:
   - Commercial bank corporate spread: **20.0 bps (0.20%)** volume-weighted market average and midpoint of the 15–25 bps median for the 4th quartile (> US$ 55,600, covering US$ 100k) in BCB *Estudo Especial nº 48/2019* (`R-01`). (A 50.0 bps conservative upper bound adds 30 bps = R$ 1,614 per US$ 100k; BCB Ranking do VET covers retail PF only at 150–350 bps.)
   - Outbound SWIFT wire fee: **US$ 25 flat (2.5 bps on US$ 100k)** (`R-01b`, Banco do Brasil *Tabela de Tarifas PJ*: R$ 100.00 isolated SWIFT communication fee = US$ 18.59; R$ 440.00 full online wire order = US$ 81.78 / 8.2 bps).
   - Bank Route A (Goods import / trade finance): IOF 0.0% (RIOF Art. 15-B, I). Total = **22.5 bps** (R$ 1,210.50; or 52.5 bps / R$ 2,824.50 at 50 bps spread).
   - Bank Route B (Availability pre-23 May 2025 & foreign investment remittance post-May 2025): IOF 1.10% (110.0 bps, Dec. 11.153/2022 & Dec. 12.467/2025, XXI-A). Total = **132.5 bps** (R$ 7,128.50; or 162.5 bps / R$ 8,742.50 at 50 bps spread).
   - Bank Route C (General availability transfer post-23 May 2025): IOF 3.50% (350.0 bps, Dec. 12.466/2025 & STF ADC 96). Total = **372.5 bps** (R$ 20,040.50; or 402.5 bps / R$ 21,654.50 at 50 bps spread).
3. **Digital Dollar (USDT) Route per Historical Regime (Sources R-04, R-05, R-06, P2-02)**:
   - Exchange trading fee: 10.0 bps (Binance VIP0 spot taker benchmark `R-04`; Foxbit VIP 6–7 R$ 5M–25M taker is 7–9 bps, midpoint 8.0 bps `R-05`; Mercado Bitcoin VIP 6.0 bps is passive *maker* fee >R$ 10M whereas active *taker* for R$ 500k–10M is 60.0 bps `R-06`).
   - On-chain transfer fee: 0.1 bps (US$ 1.00 flat TRC-20 / TON withdrawal on US$ 100k).
4. **Policy Scenarios (Explicitly Labelled)**:
   - **Scenario S1 (3.5% Crypto IOF, Source E-03 / R-02)**: Unenacted Fazenda proposal taxing crypto purchases with 3.5% IOF. Applied to Regime 6 baseline: 26.8 + 10.0 + 0.1 + 350.0 = **386.9 bps (R$ 20,815.22)**.
   - **Scenario S2a (24h Precautionary Hold, Hedged via CIP, Source E-06b / R-07)**: Res. BCB 584/2026 hold hedged for 1 business day via Covered Interest Parity $(\text{CDI } 10.75\% - \text{SOFR } 5.00\%)/252 = 2.28\text{ bps}$ + ~0.22 bps B3 DOL fee = **2.5 bps**. Total = 36.9 + 2.5 = **39.4 bps (R$ 2,119.72)**.
   - **Scenario S2b (24h Precautionary Hold, Unhedged Volatility, Source E-06b / R-07)**: Expected cost = **0.0 bps** (total **36.9 bps = R$ 1,985.22**), with a separate 95% 1-day FX risk of **130 bps** ($1.645 \times \text{sd}$ of daily PTAX log changes in 2025–26).

## Subtasks
- [x] S1 — Pre-run specification and source mapping (R-01..R-07). — done: Felipe, 1 Nov
- [x] S2 — Implement `scripts/p3_01_costs.py` to calculate table `results/tables/P3-01_route_costs.csv`. — done: Felipe, 1 Nov
- [x] S3 — Generate horizontal bar chart `results/figures/P3-01_route_costs.png`. — done: Felipe, 1 Nov
- [x] S4 — Draft finding `findings/F-015-route-costs.md`. — done: Felipe, 1 Nov
- [x] S5 — Review, verification, and handoff. — done: Felipe, 1 Nov
- [x] S6 — Source or replace the bank-route assumptions (20 bps BCB corporate spread `R-01`, US$ 25 SWIFT wire `R-01b`, 2.5 bps 1-day CIP hedge carry `R-07`) and the Foxbit/MB VIP fees (`R-05`, `R-06`); every source opened and quoted — done: Felipe, 2 Nov
- [x] S7 — Validate the comparison (IOF in force per period and per operation type, what is and is not comparable) and keep two presentation options open for the team: (a) neutral annex table, (c) one slide; no "economiza" wording (`docs/02-dolar-cripto.md` §10) — done: Felipe, 2 Nov

## Success criteria
- [x] Every cost component has a source in docs/sources.md (R-01 through R-07)
- [x] Table per regime in results/tables/P3-01_route_costs.csv
- [x] Scenarios labelled as scenarios, with the assumption stated
- [x] Finding written (findings/F-015-route-costs.md)

## Outputs
- `scripts/p3_01_costs.py`
- `results/tables/P3-01_route_costs.csv`
- `results/figures/P3-01_route_costs.png`
- `findings/F-015-route-costs.md`

## Handoff
- **State:** S1–S7 complete (`status: review`). All bank-route and exchange parameters are backed by opened, verbatim-quoted primary sources in `docs/sources.md` (`R-01` BCB Estudo Especial nº 48/2019 20 bps corporate spread for >US$ 55.6k; `R-01b` Banco do Brasil Tarifas PJ R$ 100 SWIFT / R$ 440 online wire; `R-02` RIOF + Decretos 12.466/12.467; `R-05` Foxbit VIP 6–7 8 bps taker; `R-06` MB VIP 6 bps maker vs 60 bps taker; `R-07` 2.5 bps 1-day CIP carry). `results/figures/P3-01_route_costs.png` regenerated without `"economiza R$"` labels. Both presentation options (Option C: compact neutral context on Slide 10; Option A: full comparative table in Annex B.5) are prepared in `deck/deck_v1_ptbr.md` and `deck/annex_v1_ptbr.md` so the team can decide at freeze.
- **Next step:** Teammate (Renzo) checks the sourced `R-01`..`R-07` entries and marks `done`; team selects Option A vs Option C before P4-03 freeze.
- **Open questions:** Team choice between Option C (keep neutral comparison on Slide 10) vs Option A (headline notice cost on Slide 10 + full route table in Annex B.5).
- **How to resume:** `py scripts/p3_01_costs.py`

## Log
- 2026-11-02, agent for Felipe: S6–S7 completed (`status: review`). Opened and quoted primary sources (`R-01`, `R-01b`, `R-02`, `R-05`, `R-06`, `R-07` in `docs/sources.md`); updated `scripts/p3_01_costs.py`, `results/tables/P3-01_route_costs.csv`, `results/figures/P3-01_route_costs.png` (neutral labels, no "economiza"), and `findings/F-015-route-costs.md`. Both Option A (annex table) and Option C (slide) prepared for the team.
- 2026-11-02, agent for Felipe: Felipe takes S6–S7 (bank route kept, reframed neutrally; source it before the team picks annex vs slide).
- 2026-11-02, agent for Renzo (review fixes, on Felipe's behalf, agreed by Renzo): regimes 1–3 compared at 1.1% IOF (R-02; savings R$ 3.3–6.3k, were R$ 16–20k); cost of the notice added (`NOTICE_COST_SPIKE` R$ 5,052, `NOTICE_COST_AFTER` R$ 621 not significant) and made the headline in F-015; unhedged-hold risk no longer added as a cost; bank spread and hedge cost marked as assumptions; whether the bank comparison stays in the deck left to the team; working back to -
- 2026-11-02, agent for Renzo: Renzo takes the review fixes (with Felipe's agreement).
- 2026-11-02, Renzo (review): arithmetic checked; changes requested before `done` (see Review below); working back to -.
- 2026-11-02, agent for Renzo: Renzo takes the review of P3-01.
- 2026-11-01, Felipe: S1–S5 completed (`status: review`). Wrote and executed `scripts/p3_01_costs.py`, producing `results/tables/P3-01_route_costs.csv` (15 rows across bank benchmarks, 6 Bai-Perron regimes, 24–25 Jun peak, Foxbit/MB VIP tiers, and S1/S2a/S2b scenarios) and `results/figures/P3-01_route_costs.png`. Authored `findings/F-015-route-costs.md`.

## Result
**Headline (cost of the notice):** The 23 Jun 2026 BCB supervisory notice raised the cost of acquiring US$ 100,000 via USDT by **+93.9 bps (US$ 939 ≈ R$ 5,052)** during the 20-day acute spike (24 Jun – 21 Jul 2026; placebo $p \approx 0.001$, `F-016`). After 22 Jul, the level was +11.5 bps (R$ 621) above the pre-notice window, which is not distinguishable from ordinary drift (placebo $p = 0.24$, `F-022`).

**Context (sourced bank vs USDT route frictions, `F-015`):** Using the BCB's empirical corporate FX spread median of **20.0 bps** for contracts > US$ 55,600 (*Estudo Especial nº 48/2019*, `R-01`; 50 bps upper bound noted) and **US$ 25 (2.5 bps)** SWIFT wire (`R-01b`), formal bank FX costs **22.5 bps (R$ 1,211)** for goods imports (0% IOF), **132.5 bps (R$ 7,129)** for investment remittances / pre-May 2025 availability (1.1% IOF), and **372.5 bps (R$ 20,041)** for post-May 2025 general availability (3.5% IOF, `R-02`). An enacted 3.5% crypto IOF (`E-03`, Scenario S1) would raise the USDT route to **386.9 bps (R$ 20,815)**, while a 24-hour precautionary hold (`E-06b`, Scenario S2) adds **2.5 bps** when hedged via 1-day CIP carry (`R-07`) or exposes an unhedged buyer to **130 bps** of 95% 1-day FX risk.

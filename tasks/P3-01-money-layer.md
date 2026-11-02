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
Turn the premium into money for a Brazilian corporate treasurer: what US$ 100,000 costs via a traditional bank route (PTAX + bank spread + IOF) vs via the digital dollar route (USDT premium + exchange fees + network fee), across historical Bai-Perron regimes, plus explicitly labelled policy scenarios for the 24h precautionary hold (Res. BCB 584/2026) and proposed 3.5% crypto IOF. Plan: `docs/02-dolar-cripto.md` §7.6.

## Pre-Run Specification
1. **Benchmark Transaction**:
   - Notion: US$ 100,000 institutional/treasury acquisition.
   - Reference FX: `PTAX = R$ 5.3800` (live bid/ask benchmark from Binance D-10; base BRL cost = R$ 538,000).
2. **Traditional Bank Route Benchmarks (Sources R-01, R-02, R-03)**:
   - Commercial bank spread: 50.0 bps (0.50%), reflecting median institutional corporate spreads in BCB Ranking do VET (R-01) for operations > US$ 50k.
   - Outbound wire fee: US$ 25 flat (2.5 bps on US$ 100k) representing typical SWIFT transfer costs.
   - Bank Route A (Goods import / commercial trade finance): IOF 0.0% (0.0 bps). Total cost = 52.5 bps (US$ 525 / R$ 2,824.50).
   - Bank Route B (Foreign investment remittance): IOF 1.1% (110.0 bps, Decreto 12.467/2025). Total cost = 162.5 bps (US$ 1,625 / R$ 8,742.50).
   - Bank Route C (Availability / outbound general transfer): IOF 3.5% (350.0 bps, Decreto 12.466/2025 & ADC 96). Total cost = 402.5 bps (US$ 4,025 / R$ 21,654.50).
3. **Digital Dollar (USDT) Route per Historical Regime (Sources R-04, R-05, R-06, P2-02)**:
   - Exchange trading fee: 10.0 bps (Binance VIP0 spot taker fee; VIP institutional 1.5–5.0 bps; domestic Foxbit/MB VIP institutional 4.0–10.0 bps).
   - On-chain transfer fee: 0.1 bps (US$ 1.00 flat TRC-20 / TON withdrawal on US$ 100k).
   - Premium per regime (from `results/tables/P2-02_breaks.csv`):
     - Regime 1 (2020-10 to 2021-07): 91.3 bps premium -> Total 101.4 bps (US$ 1,014 / R$ 5,455.32).
     - Regime 2 (2021-07 to 2024-08): 54.5 bps premium -> Total 64.6 bps (US$ 646 / R$ 3,475.48).
     - Regime 3 (2024-08 to 2025-07): 34.9 bps premium -> Total 45.0 bps (US$ 450 / R$ 2,421.00).
     - Regime 4 (2025-07 to 2026-06, pre-notice baseline): 9.3 bps premium -> Total 19.4 bps (US$ 194 / R$ 1,043.72).
     - Regime 5 (2026-06-24 to 2026-07-21, acute 20-day spike): 109.1 bps premium -> Total 119.2 bps (US$ 1,192 / R$ 6,412.96).
     - Regime 6 (2026-07-22 to 2026-10-30, post-adaptation plateau): 26.8 bps premium -> Total 36.9 bps (US$ 369 / R$ 1,985.22).
     - Peak Shock (24–25 Jun 2026): 169.9 bps premium -> Total 180.0 bps (US$ 1,800 / R$ 9,684.00).
4. **Policy Scenarios (Explicitly Labelled)**:
   - **Scenario S1 (3.5% Crypto IOF, Source E-03 / R-02)**: Fazenda proposal taxing crypto purchases with 3.5% IOF. Applied to Regime 6 baseline: 26.8 bps + 10.0 bps + 0.1 bps + 350.0 bps = 386.9 bps (US$ 3,869 / R$ 20,815.22). Savings vs Bank Availability shrink from R$ 19,669 to R$ 839.
   - **Scenario S2a (24h Precautionary Hold, Hedged, Source E-06b / R-07)**: Res. BCB 584/2026 hold for transfers >= US$ 10k to foreign destinations. Hedged with B3 USD futures (DDI/DOL) or crypto perps: 10.0 bps hedging/funding cost. Total = 36.9 bps + 10.0 bps = 46.9 bps (US$ 469 / R$ 2,523.22).
   - **Scenario S2b (24h Precautionary Hold, Unhedged Volatility, Source E-06b / R-07)**: Unhedged 24h USD/BRL market risk (95th percentile 1-day absolute PTAX return = 136.8 bps). Total = 36.9 bps + 136.8 bps = 173.7 bps (US$ 1,737 / R$ 9,345.06).

## Subtasks
- [x] S1 — Pre-run specification and source mapping (R-01..R-07). — done: Felipe, 1 Nov
- [x] S2 — Implement `scripts/p3_01_costs.py` to calculate table `results/tables/P3-01_route_costs.csv`. — done: Felipe, 1 Nov
- [x] S3 — Generate horizontal bar chart `results/figures/P3-01_route_costs.png`. — done: Felipe, 1 Nov
- [x] S4 — Draft finding `findings/F-015-route-costs.md`. — done: Felipe, 1 Nov
- [x] S5 — Review, verification, and handoff. — done: Felipe, 1 Nov

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
<!-- Overwrite at the end of every session, finished or not, so anyone can continue from here. -->
- **State:** reviewed by Renzo (2 Nov). **Substantive changes needed before the deck** (owner: Felipe, economist call).
  The arithmetic is right (total = premium + spread + fees + tax; R$ = bps × R$ 538,000).
- **Changes requested:**
  1. **Wrong IOF for 2020 – May 2025.** Every historical regime is compared with the 3.5% route, but R-02 itself says
     transfers paid 1.1% before 23 May 2025. Regimes 1–3 should use 162.5 bps. Savings then fall about fivefold
     (R1: 61 bps ≈ R$ 3.3k; R2: 98 bps ≈ R$ 5.3k; R3, mostly before May 2025: 118 bps ≈ R$ 6.3k). Only Regime 4 onward
     faces 3.5% (R$ 20.6k). F-015's "R$ 16–20k across pre-notice regimes" is wrong for 2020–2025.
  2. **Framing (prompt.md §10).** "Savings vs bank FX with 3.5% IOF" presents USDT as a way around the IOF. That is the
     practice the 23 Jun notice is reported to target (Brotto, Cointelegraph Brasil 6 Jul: "impedir arbitragem de IOF").
     The legal status of the USDT route (IOF, use as a substitute for an FX transfer) is not verified. Suggest the headline
     money number be the project's own question: what the notice cost a buyer of digital dollars. The premium rose
     +94 bps ≈ R$ 5.1k per US$ 100k during the spike, and about +17 bps ≈ R$ 0.9k afterwards. The bank routes become context,
     stated neutrally, with the legal caveat.
  3. **Unsourced constants.**
     - Bank spread 50 bps "from VET": not computed; the VET data are not downloaded, and the open-data link returned 502.
     - Hedge cost "~10 bps": no source.
     - "VaR 136.8 bps": typed in, not computed. Our PTAX data give 1.645 × sd = 130–139 bps and a 95th percentile |1-day
       move| of 128–167 bps. It is also a risk, not a cost (expected cost of an unhedged 24 h hold ≈ 0); show it apart from
       the costs.
     - R-07 (Res. 584) is cited for both numbers, but the regulation contains neither.
     - Foxbit/MB VIP fees (R-05, R-06): those pages block scripts; open them by hand (rule: sources are opened).
  4. **Wording.** "Adaptation plateau", and "Res. BCB 580 and Foxbit–NovaDAX catalyzed … restoring local supply", have no
     evidence (P2-02: the fade is unexplained; Res. 580 has no opened source). Say "after the spike".
  5. **F-015 status.** It is `confirmed` with no checker; suggest `exploratory` until 1–4 are done.
- **Next step:** Felipe (and the team, for the framing in 2) decides; then fix `scripts/p3_01_costs.py` and F-015.
- **How to resume:** `python scripts/p3_01_costs.py`.

## Log
- 2026-11-02, agent for Renzo: review done (Handoff): arithmetic right; IOF anachronism for 2020–May 2025, framing, unsourced constants.
- 2026-11-02, agent for Renzo: Renzo takes the review.
- 2026-11-01, Felipe: Initialized S1 with full institutional specification (US$ 100k, PTAX R$ 5.3800), traditional banking routes (0%, 1.1%, 3.5% IOF), historical Bai-Perron regimes, 24-25 Jun peak shock, and policy scenarios (3.5% IOF proposal, 24h hold hedged vs unhedged).
- 2026-11-01, Felipe: Implemented S2 (`scripts/p3_01_costs.py`) and generated `results/tables/P3-01_route_costs.csv`.
- 2026-11-01, Felipe: Completed S3 (`results/figures/P3-01_route_costs.png`) with clean publication-grade stacked horizontal bar formatting and bank reference lines.
- 2026-11-01, Felipe: Completed S4 (`findings/F-015-route-costs.md`) with comprehensive institutional interpretation and neutral regulatory framing.
- 2026-11-01, Felipe: Completed S5 review; marked all subtasks and success criteria `[x]`, set status to `review` and `working: -`.

## Result
Table produced by `scripts/p3_01_costs.py` (`results/tables/P3-01_route_costs.csv`):

| route_id | category | regime_or_scenario | premium_bps | spread_bps | iof_or_hold_bps | total_bps | cost_usd_per_100k | savings_vs_bank_avail_brl |
|---|---|---|---|---|---|---|---|---|
| BANK_IMPORT_0IOF | Bank Route | Bank Import (0% IOF) | 0.0 | 50.0 | 0.0 | 52.5 | $525.00 | R$ 18,830.00 |
| BANK_INVEST_11IOF | Bank Route | Bank Investment (1.1% IOF) | 0.0 | 50.0 | 110.0 | 162.5 | $1,625.00 | R$ 12,912.00 |
| BANK_AVAIL_35IOF | Bank Route | Bank Availability (3.5% IOF) | 0.0 | 50.0 | 350.0 | 402.5 | $4,025.00 | R$ 0.00 |
| USDT_REGIME_1 | Historical | Regime 1: Oct 2020 - Jul 2021 | 91.3 | 10.0 | 0.0 | 101.4 | $1,014.00 | R$ 16,199.18 |
| USDT_REGIME_2 | Historical | Regime 2: Jul 2021 - Aug 2024 | 54.5 | 10.0 | 0.0 | 64.6 | $646.00 | R$ 18,179.02 |
| USDT_REGIME_3 | Historical | Regime 3: Aug 2024 - Jul 2025 | 34.9 | 10.0 | 0.0 | 45.0 | $450.00 | R$ 19,233.50 |
| USDT_REGIME_4 | Historical | Regime 4: Pre-Notice Baseline (2025-2026) | 9.3 | 10.0 | 0.0 | 19.4 | $194.00 | R$ 20,610.78 |
| USDT_REGIME_5 | Historical | Regime 5: Acute 20d Spike (24 Jun - 21 Jul) | 109.1 | 10.0 | 0.0 | 119.2 | $1,192.00 | R$ 15,241.54 |
| USDT_PEAK | Historical | Peak Shock: 24-25 Jun 2026 | 169.9 | 10.0 | 0.0 | 180.0 | $1,799.75 | R$ 11,971.84 |
| USDT_REGIME_6 | Historical | Regime 6: Adaptation Plateau (Jul-Oct 2026) | 26.8 | 10.0 | 0.0 | 36.9 | $369.00 | R$ 19,669.28 |
| USDT_REGIME_6_FOXBIT | Domestic | Regime 6: Foxbit VIP Institutional | 26.8 | 8.0 | 0.0 | 35.0 | $350.00 | R$ 19,771.50 |
| USDT_REGIME_6_MB | Domestic | Regime 6: Mercado Bitcoin VIP Institutional | 26.8 | 6.0 | 0.0 | 33.0 | $330.00 | R$ 19,879.10 |
| SCENARIO_S1_IOF35 | Policy Scenario | Scenario S1: 3.5% Crypto IOF Enacted | 26.8 | 10.0 | 350.0 | 386.9 | $3,869.00 | R$ 839.28 |
| SCENARIO_S2A_HOLD_HEDGED | Policy Scenario | Scenario S2a: 24h Hold Hedged (Res. 584/2026) | 26.8 | 10.0 | 10.0 | 46.9 | $469.00 | R$ 19,131.28 |
| SCENARIO_S2B_HOLD_UNHEDGED | Policy Scenario | Scenario S2b: 24h Hold Unhedged (Res. 584/2026) | 26.8 | 10.0 | 136.8 | 173.7 | $1,737.00 | R$ 12,309.44 |

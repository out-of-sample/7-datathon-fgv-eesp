---
id: P3-47
title: Does Foxbit order flow explain the premium's recovery within weeks?
phase: P3
status: review
owner: CS 1
working: -
due: 2026-11-08
depends: P3-17, P3-19, P3-25
---

## Goal
Test the weakest link in the proposed recovery mechanism: seller-initiated Foxbit trading and the premium may merely share a June–July time trend. Report whether the relation survives comparisons *within calendar weeks* and whether afternoon trading anticipates the next PTAX-day change. This is one observed episode and cannot identify a causal effect or a trader.

## Prior knowledge and scope
F-031 and F-032 showed large seller-initiated flow and a positive daily association with the premium, but the within-day estimate includes zero. The fitted hinge at 35 bps is not necessarily the point where fitted net selling crosses zero. F-024 showed external stablecoin purchases remained low as price recovered. This task uses only existing frozen Foxbit candles and P3-19 daily variables; it will not modify the frozen core findings or deck.

## Fixed specification (written before P3-47 outcomes)
- Sample: PTAX days 24 Jun–30 Sep 2026, as in P3-19. Date and hours use Brasília UTC−3 in 2026. Foxbit afternoon = candle open 13:00–17:00 Brasília. Outcome `y` = total USDT volume minus twice taker-buy USDT volume, divided by 1e6; total-volume denominator sums the same hours. Exclude and count days with zero denominator.
- Primary comparison: OLS `y_t` on morning premium `x1_t` (bps) and morning Foxbit–Binance gap `x2_t` (bps), after subtracting each variable's calendar-week mean (Monday-start ISO weeks). Report the raw P3-19 daily coefficient beside it. Bootstrap 2,000 resamples of whole calendar weeks, seed 47; report percentile 95% intervals. Count days and weeks. A within-week coefficient with an interval containing zero means the original daily association may reflect episode timing.
- Scale check: repeat the within-week model with `y_t / total_volume_t` (dimensionless). This distinguishes an imbalance share from a simple volume surge. Report median and range of total volume; do not treat an imprecise result as zero.
- Forward check: regress `x1_{t+1} - x1_t` (bps, next observed PTAX day) on `y_t`, `x1_t`, and `x2_t`, both without and with calendar-week fixed effects; bootstrap whole weeks. The no-flow baseline uses `x1_t` and `x2_t` only. A negative flow coefficient whose interval excludes zero would be consistent with price pressure, but still confounded; an interval containing zero supplies no evidence that flow drove the fall. The last sample day has no outcome and is excluded.
- Threshold audit: refit the P3-19 hinge `y = a + b max(0, x1-k)` on its daily sample. Report the fitted kink `k`, intercept `a`, and calculated zero-crossing `k-a/b` if `b>0`; do not call the kink a zero-crossing or a route cost.
- Data integrity: verify the Foxbit raw SHA-256 against `data/raw/SHA256SUMS`, required columns, nonnegative volume, `0 <= taker_buy <= volume`, unique hourly timestamps, and available afternoon hours. Save a small coverage table. If any critical check fails, stop the mechanism test and report the failure.

## Reading rule and claim ceiling
1. If the primary within-week interval excludes zero, scale check has the same sign, and forward check is negative with an interval excluding zero, report a stronger *association compatible with* liquidity adjustment. Still do not claim causation or imports.
2. If the primary or forward interval includes zero, report that the data do not distinguish price-responsive supply from a common episode trend. The previously observed co-movement remains descriptive.
3. No coefficient from this one episode is an independent policy-event count; no p-value here establishes the June notice as the cause.

## Subtasks
- [x] S1 — fixed specification and scope — done: Codex for Renzo, 8 Nov 2026
- [x] S2 — raw-data checks and analysis script — done: Codex for Renzo, 8 Nov 2026
- [x] S3 — finding with all outcomes and limitations — done: Codex for Renzo, 8 Nov 2026
- [ ] S4 — independent teammate review and deck adoption decision (separate gate)

## Success criteria
- [x] Script and table reproduce the four checks, including null results
- [x] Raw coverage and units documented
- [x] Finding distinguishes within-week evidence from whole-episode co-movement

## Outputs
- `scripts/p3_47_recovery_check.py`
- `results/tables/P3-47_recovery_checks.csv`, `results/tables/P3-47_coverage.csv`
- `findings/F-054-recovery-mechanism-check.md`

## Handoff
- **State:** S1–S3 complete; F-054 exploratory. The within-week premium–flow interval includes zero, and afternoon flow does not predict a next-day premium fall. An independent statsmodels fixed-effects calculation matched the point estimates and also gave intervals including zero. No claim of mechanism identification or deck change is warranted.
- **Next step:** S4: a teammate re-runs `.venv/bin/python scripts/p3_47_recovery_check.py`, compares both CSVs with F-054, and checks the weekly resampling and interpretation. Felipe then decides whether to mention the negative result in the deck; keep the 4 Nov core freeze intact.
- **Open questions:** which participants supplied or bought USDT, whether funds resumed privately, and whether Foxbit's activity reflected new imports or inventory are unobserved in these data.
- **How to resume:** read F-054 and the fixed spec above; run the command from the repo root. Raw checksum and coverage are printed by the script. `main` is behind `origin/main` and the shared tree has unrelated deck/STATUS edits; do not stash or stage them while integrating this task.

## Log
- 2026-11-08, Codex for Renzo: S2–S3 done. Frozen Foxbit raw hash matches, 70 PTAX days/350 afternoon hours cover the sample. Week-fixed-effect and normalized slopes include zero; forward flow slopes include zero; simple no-flow baseline barely changes when flow is added. F-054 and two output CSVs written. A separate statsmodels fixed-effects calculation matched the point estimates. S4 remains for a teammate.
- 2026-11-08, Codex for Renzo: Renzo asked to pursue the recovery explanation. New task chosen because P3-17/P3-19 are in review and P3-25 has a separate named-human sign-off. The shared tree is dirty and `main` is behind `origin/main`; no other worker's files were stashed or changed.

## Result
The follow-up does not identify why the premium recovered. F-054 shows that the previously reported premium–Foxbit flow association is imprecise within calendar weeks and does not predict a next-day fall. Alternative supply, inventory, demand, venue-specific activity and confidential channel resumption remain possible. Independent teammate review is pending.

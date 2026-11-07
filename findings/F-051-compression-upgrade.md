---
id: F-051
title: Monthly retraining improves the first ridge forecast, but its edge over simple mean reversion remains uncertain
status: exploratory
task: P3-42
date: 2026-11-07
checked_by: -
---

## Claim
The upgraded compression prototype retrains monthly and calibrates bands from previously issued, matured forecast errors. The validation-selected rolling ridge improves on the frozen v 1 ridge. It narrowly beats simple mean reversion across daily 2026 origins, but not on the fixed nonoverlapping subset. This is an exploratory refinement after seeing v 1's 2026 results, not a fresh confirmatory test.

The stress-aware decision cards also distinguish a central waiting signal from a conclusion robust to the stated funding/execution assumptions. All June cards become insufficient evidence under that envelope; actual access remains unknown in every case.

## Evidence
Reproduce: `python scripts/p3_42_compression_upgrade.py`; tests alone: append `--test-only`. Uses the same local Python installation as P3-41; no new dependency or source download. Fourteen tests (nine v 1 plus five upgrade tests) check publication/feature timing, strict label maturity, future-outcome perturbations, nonlinear knots, calibration maturity and the stress/access gate. The chart was visually inspected. Saved tables and audit record exact input/source hashes and package versions.

### What changed
- At each month start, fit on the latest 756 eligible origins with terminal outcomes strictly before that month (minimum 250). Parameters remain fixed inside the month. Scaling and nonlinear knots use those fit rows only.
- Four candidates: linear ridge and nonlinear piecewise-linear hinge ridge, each at penalties 100/1000. Hinges use training feature quartiles. This is a dependency-free nonlinear regression, not a boosted tree or transformer.
- Historical forecasts start in Jan 2024. At each signal, bands use the last 126 matured, previously issued errors for that configuration (minimum 60). No outcome enters its own forecast band before it is observed. Fit and calibration timestamps are inspectable in `P3-42_fit_trace.csv` and `P3-42_predictions.csv`.
- Select a configuration on daily 2025 10-day MAE only, and use it at every horizon. Every attempt remains reported. Selected: `rolling_ridge_100`, validation MAE 26.706 bps versus simple mean reversion 26.943, rolling ridge 1000 27.387, hinge 100 27.223 and hinge 1000 27.610 (`P3-42_selection.csv`).

### Primary 10-day comparison
Same dates for every method and the v 1 comparator; bps, lower MAE is better.

| 2026 sample | n | Persistence | Simple mean reversion | Frozen ridge v 1 | Selected rolling ridge |
|---|---:|---:|---:|---:|---:|
| Daily | 196 | 36.030 | 30.033 | 34.430 | **29.337** |
| Fixed nonoverlapping | 18 | 25.224 | **21.329** | 29.489 | 21.736 |

On nonoverlapping origins, selected minus v 1 MAE is −7.753 bps (paired moving-block bootstrap interval −12.806 to −2.317). Selected minus mean reversion is +0.407 bps (−2.461 to +3.258), and minus persistence −3.488 bps (−12.493 to +3.697). Same exploratory three-origin circular blocks, 2,000 draws and seed 41 as v 1; only 18 origins and one known policy episode limit interpretation. These intervals do not adjust for choosing to upgrade after inspecting v 1.

The nonlinear models do not clearly add value: daily 10-day MAE is 30.553 (hinge 100) and 30.177 (hinge 1000), versus selected linear ridge 29.337. Ridge 1000 happens to have slightly better nonoverlapping test MAE (21.158), but it was not selected on validation and is not promoted after seeing test results.

### Forecast bands and conditional costs
Selected rolling ridge's 10-day band covers 87.245% of daily outcomes and 94.444% of nonoverlapping ones; mean daily width 124.852 bps. Adaptive calibration does not establish guaranteed 90% coverage.

At the declared K=25 bps and central v 1 rates, the selected rule conditionally waits on 10/196 daily origins, with mean scenario saving +2.817 bps versus buy-now across all daily cases. On the nonoverlapping subset it waits once in 18, with mean +5.025 bps; that number rests on one waiting case. Simple mean reversion waits once in 196 daily cases, with mean +0.219 bps, and never waits in the nonoverlapping subset. Always-wait averages −6.297 bps daily and +0.971 on the subset. Overlapping daily cases are not a realizable portfolio, and the sparse nonoverlapping policy decisions do not establish economic superiority. Abstentions default to buying now for this evaluation only.

### Stress-aware cards
`P3-42_decision_cards.csv` crosses both forecast-band endpoints with the same 216 scenarios as P3-39: achievable BRL deposit 0/5/10%, USDT-unit yield 0/4%, terminal USDTUSD factor.995/1/1.005, FX factor.98/1/1.02, waiting conversion fee 10/30 bps, waiting fixed feeR$0/100. Forward pricing remains 10% BRL/5% USD. Cost budgets are bps of each scenario's signal-price initial outlay, compared with K=25 bps on that same basis.

For 25 Jun the selected model's central interval supports waiting at 5/10/20 days. Across the joint forecast/scenario envelope, min/max cost budgets are respectively [−28.727,+235.949], [−24.104,+264.465], and [−77.468,+262.534]bps. Every range crosses K=25; all three stress labels are insufficient evidence. These are scenario extrema, not confidence bounds.

The latest archive cards are as of 30 Oct 2026, not live signals. Unknown access overrides every central or stress label: actionable outputs remain insufficient evidence. The stress envelope is diagnostic; historical policy-saving comparisons above use central assumptions only.

## Caveats
All F-050 limitations remain: indicative hourly first trades and PTAX, ideal forward, unverified access/liquidity/margin/settlement, residual FX and USDTUSD exposure, one currency and one known 2026 shock. The monthly model and its residuals evolve as earlier outcomes mature; 2026 inputs can therefore legitimately inform later 2026 forecasts, but never earlier ones. This differs intentionally from frozen v 1. The upgrade simultaneously changes the fit sample and calibration; it does not isolate their separate contributions. No new data or independent event validates the improvement.

## Used in deck
Not used. Independent teammate reproduction and integration decision pending; v 1 and all frozen core findings remain unchanged.

## History
- 2026-11-07 — Codex for Felipe: bounded protocol committed as `ce91d8b` before upgrade fitting, after explicit user request. All candidates retained, validation selection preserved after test inspection. Fourteen tests pass; chart visually inspected. Independent review not claimed.

- 2026-11-07 — Same-implementer replay: all ten upgrade outputs reproduced byte for byte; fourteen v1 outputs remained unchanged. This is not an independent review.

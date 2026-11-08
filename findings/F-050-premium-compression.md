---
id: F-050
title: Partial premium compression can be evaluated against costs, but ridge does not beat simple mean reversion on the primary horizon
status: exploratory
task: P3-41
date: 2026-11-07
checked_by: Jonathan (CS 3)
---

## Claim
The new experiment connects a forecast of partial USDT/BRL premium compression to the existing conditional buyer frontier. It does **not establish improved acquisition timing**. On the primary 10-PTAX-day horizon, ridge loses to simple mean reversion in both the daily and nonoverlapping 2026 comparisons. Its advantage over persistence depends on which of those samples is used.

## Evidence
Reproduce from the repository root: `python scripts/p3_41_compression.py` (tests, input audit, fit, calibration, validation selection, test tables and figures). `--test-only` runs the nine focused tests without fitting or writing outputs. The local run used Python 3.14, pandas 3.1.0; exact package versions and input/source hashes are in `results/tables/P3-41_audit.json`. Use an installed Python with NumPy, pandas and matplotlib; no new model dependency is required.

### Inputs and timing
- Audited 1,520 daily and 52,987 hourly P1-02 observations. Daily coverage: 13 Oct 2020–30 Oct 2026. Two incomplete PTAX pricing windows and 14 flagged uncertain windows. Same-day PTAX was not published by the fixed signal clock on 144 dates. Missing rolling/hourly features affect 112 origins, including warm-up; reasons overlap and must not be summed. Exclusions are recorded per horizon.
- Signal at 14:00 Brasília / 17:00 UTC, requiring same-day PTAX publication. Features end with the hourly candle closing at that time. Buy-now and deadline prices use the **18:00 UTC / 15:00 Brasília candle open**, after the signal. These are indicative first trades, not executable quotes.
- Fit labels mature by 30 Jun 2024; calibration origins are Jul–Dec 2024 and labels mature by 31 Dec 2024. Validation is 2025 with labels mature by its year-end; test origins are 2026 with observed endpoints. No label crosses a split cutoff. At 10 days: 635 fit, 115 calibration, 238 validation, 196 test origins (`P3-41_splits.csv`).
- The ridge penalty is 1000, chosen only on 2025 daily validation MAE at 10 days (30.956 bps); the same penalty applies at 5/20 days. All features/scalers/coefficients are fit only on the fit partition. Other penalty/horizon attempts are retained in `P3-41_selection.csv`.

### Forecast comparison
MAE in basis points, lower is better. The nonoverlapping sample is fixed by the earliest eligible origin and then the next origin strictly after the previous terminal date; it is not chosen around June.

| 2026 sample | Origins | Persistence | Halfway to trailing 60-day mean | Ridge |
|---|---:|---:|---:|---:|
| Daily, 10-day horizon | 196 | 36.030 | **30.033** | 34.430 |
| Nonoverlapping, 5-day horizon | 34 | 28.711 | **25.123** | 32.552 |
| Nonoverlapping, 10-day horizon | 18 | 25.224 | **21.329** | 29.489 |
| Nonoverlapping, 20-day horizon | 9 | 50.493 | 43.535 | **40.859** |

The 20-day result is diagnostic, not a replacement primary endpoint. On 10-day nonoverlapping observations, ridge minus persistence MAE is +4.265 bps (paired moving-block bootstrap 95% interval −6.577 to +13.005); ridge minus mean reversion is +8.160 bps (+3.325 to +12.632). Blocks contain three successive nonoverlapping origins; circular resampling uses 2,000 draws, seed 41. With only 18 origins, these are exploratory uncertainty summaries, not robust evidence across policy shocks.

Ridge's nominal 90% historical residual band is 126.090 bps wide at 10 days. It covers 86.735% of daily test outcomes and 94.444% of nonoverlapping ones. Historical dependence and regime changes prevent a coverage guarantee. Every method receives its own calibration band from 2024 only (`P3-41_calibration.csv`).

### Conditional decisions
Central P3-38 assumptions: 10% effective annual achievable BRL deposit, independent forward pricing at 10% BRL / 5% USD, zero USDT-unit holding yield, 10 bps conversion fee on each route, and an ideal maturity-matched cash-settled forward. Additional terminal waiting cost K = 25 bps of actual initial buy-now outlay in realized evaluation; K=0/50 sensitivities also reported. Ex-ante cost boundaries use signal-price outlay, because execution is later and unknown. Realized and indicative bps therefore need not share exactly the same BRL denominator.

Conditional wait means the entire forecast band has a central cost budget greater than K. Conditional buy means it is entirely below K. Otherwise the forecast abstains. For evaluating that fixed rule only, abstention defaults to buy now. **Actual access is unknown, so every actionable output is `insufficient_evidence`, irrespective of the conditional label.** Settlement is assumed same-day; positive deadline settlement lag fails the existing gate.

- Daily 2026 10-day ridge: 2 wait signals / 196 origins; the mean hypothetical saving versus buy-now across those daily cases is +0.938 bps. These overlapping scenarios are not a portfolio return or independent transactions. Persistence and mean reversion never wait under this interval rule and K.
- Nonoverlapping 10-day sample: all three forecast rules abstain on every one of 18 origins and default to buy now, giving zero incremental saving. Always waiting gives +0.971 bps mean saving, but its worst case is −96.474 bps. The sample does not establish economic improvement from the forecasts.
- The full policy table includes buy-now, always-wait, every forecast rule, all horizons and K values, plus abstention rates, worst case and hindsight regret. Regret uses a hindsight choice as an accounting benchmark, not an attainable forecast.

### Fixed June replay
The 25 Jun replay was fixed before fitting and is displayed separately from the evaluation. Signal-to-execution premium change that day is **−49.866 bps**. This is why the prior daily-window June illustration and this replay cannot be compared as if they used the same entry price.

| Deadline (PTAX days) | Predicted compression | Observed signal-to-terminal compression | Conditional ridge label | Realized wait saving after K |
|---|---:|---:|---|---:|
| 5 | 73.820 bps | 35.330 bps | Insufficient evidence | −33.905 bps |
| 10 | 75.945 bps | 105.314 bps | Waiting may compensate | +42.958 bps |
| 20 | 67.463 bps | 105.931 bps | Waiting may compensate | +65.118 bps |

The last column shows what waiting would have saved under the realized indicative prices and central assumptions, whether or not the policy chose to wait. All actionable labels remain insufficient evidence because access is unknown. The June row need not be in the fixed nonoverlapping evaluation subset.

## Caveats
- Retrospective chronological holdout: 2026 and June were already inspected in other project tasks. This is not a new prospective untouched test or an independently reviewed finding.
- One currency, one known 2026 episode; many daily origins share outcomes. Fixed nonoverlapping schedules also produce few observations and do not remove shared regimes.
- Forecast bands model compression uncertainty only under central rates and fixed ex-ante FX/USDTUSD. They are not the P3-39 stress envelope, funding-rate confidence bounds, or a joint forecast of every cost component.
- PTAX is an official benchmark, not an executable hedge quote. Candle opens do not measure bid/ask, liquidity, slippage, size-dependent impact, margin funding, basis, actual route availability or bank settlement calendars. The USDT/USD adjustment inherits P1-02's USDC/BUSD parity assumptions.
- Model parameters remain frozen at the mid-2024 fit cutoff; this does not test rolling retraining, boosted trees, transformers, cross-venue predictors or pooled international forecasts. Chronos was not run and has no overlap audit here. A negative ridge result is not a proof that compression cannot be predicted.
- Mercado Bitcoin raw data was absent locally; no three-venue feature was fabricated. Raw inputs and frozen estimates remain unchanged.

## Used in deck
Not used. Independent teammate reproduction and Felipe's integration decision required. No change to the ten-slide deck.

## History
- 2026-11-07 — Same implementer verification: a second complete run reproduced all 14 generated files byte for byte; direct terminal-BRL arithmetic reconciled one validation scenario outside the budget function; every prediction retained insufficient-evidence actionable status for unknown access. This is a reproducibility check, not independent peer review.
- 2026-11-07 — Codex for Felipe: locked protocol in commit `93fd20f` before fitting; implemented and tested the experiment; nine checks pass; both charts visually inspected; exploratory finding retained with negative primary comparison. No independent reviewer claimed.

- 2026-11-07 — Independent Codex review for Felipe: full rerun, saved-output hashes, information timing and direct terminal-BRL accounting checked; no blocking defect found. Review: `docs/review-2026-11-07-compression.md`. Exploratory status and named human review/adoption gates retained. Review note changes task-file bytes after the original protocol audit; the saved task hash remains provenance for the pre-review task version.

---
id: P3-41
title: Forecast economically useful premium compression before a payment deadline
phase: P3
status: review
owner: Economist
working: -
due: 2026-11-08
depends: P3-39, P1-02
---

## Goal
User authorized on 7 Nov after a read-only project/data review. Build the first bounded experiment from the supplied decision-system proposal: predict partial compression and pass it to the existing buyer frontier. No change to frozen findings or deck; no other proposed extension is included.

## Specification locked before fitting
- BRL only. Existing daily and hourly P1-02 files; no downloads. Audit coverage, timestamps, flags and price decomposition first. Missing required observations are excluded and counted, never filled using future values.
- Signal at 17:00 UTC / 14:00 Brasília on each PTAX day. Require same-day PTAX publication by then. Current indicative price is the 16:00 UTC candle close (known at 17:00). Replay purchases at the 18:00 UTC candle open (15:00 Brasília), leaving one hour after signal. Use the same execution clock at the deadline. Candle open is an indicative first trade, not an executable bid/ask quote.
- Target: signal premium minus terminal execution premium, at 5/10/20 observed PTAX-day horizons. Actual buy-now execution premium is separately retained; thus the one-hour signal/execution gap affects realized savings. Use same-day PTAX and contemporaneous USDT/USD at each clock. PTAX is an official reference, not a tradable spot FX quote.
- Features available by signal: current and lagged daily premiums, recent changes, rolling mean/deviation, volatility, hourly traded volume and hourly return volatility over the preceding 24 hours. Exclude same-day day-close fields and the hindsight regime labels. No cross-venue feature in v1 because MB raw data is missing locally.
- Fit through 30 Jun 2024; calibration origins after 30 Jun with terminal timestamps no later than 31 Dec 2024. Validation origins in 2025 with terminal timestamps no later than 31 Dec 2025. Test origins in 2026 with observed terminal data. Labels may not cross a split cutoff. Parameters/scalers never fit on calibration, validation or test. Frozen fit rather than adaptive refitting.
- Methods: persistence (zero compression), simple fixed mean reversion (halfway to trailing 60-day signal-premium mean), standardized ridge regression with intercept. Ridge penalties 1/10/100/1000 selected on 2025 validation MAE at 10 days, then applied to all horizons. Primary forecast metric = 10-day MAE in bps. Other horizons and subperiods are diagnostic, not additional independent tests.
- All methods receive symmetric empirical 90% absolute-error bands from 2024 calibration only (finite-sample upper order statistic). These are historical residual bands; dependence and regime shift prevent guaranteed coverage. Report actual coverage and width. Chronos is deferred: no pretrained-model overlap audit or installed dependency verified; this task makes no transformer claim.
- Pass point and interval forecasts through P3-38 budget with its central hypothetical rates and fixed signal FX/USDT/USD. K=25 bps primary additional terminal cost; K=0/50 sensitivities. Classify conditional wait / buy now / insufficient evidence using interval budget vs K. Actual access is unknown and always overrides any actionable classification. Both routes assumed same-day settlement at execution; lag failures use the existing gate.
- For evaluation only, an abstention defaults to buying now. Realized terminal saving uses actual 18:00 prices and terminal PTAX/USDTUSD via the same budget function, with K charged only if waiting. Compare buy-now, always-wait, persistence, mean reversion and ridge. This is conditional scenario accounting, not trading profit or execution evidence.
- Report all daily origins and a fixed nonoverlapping subset per horizon (first valid evaluation origin, then next origin strictly after previous terminal date), plus nonoverlapping paired moving-block bootstrap MAE-gap intervals (block 3, 2,000 draws, seed 41). Few 2026 blocks and one known June event limit inference. June replay fixed at 25 Jun for illustration only. 2026 has already been inspected in earlier project work: chronological holdout here is retrospective, not a prospective untouched study.

## Subtasks
- [x] S1 — Input/clock audit and frozen protocol — done: Felipe (Codex), 7 Nov.
- [x] S2 — Forecasts, calibration, frontier integration and leakage/boundary tests — done: Felipe (Codex), 7 Nov.
- [x] S3 — Reproduce tables, inspect figure, write exploratory finding and handoff — done: Felipe (Codex), 7 Nov.

## Success criteria
- [x] Inputs hashed; exclusions and signal/execution timestamps inspectable.
- [x] Split maturity/scaling and future-perturbation checks pass.
- [x] Every model and baseline evaluated on the same origins; intervals and conditional decision costs reported.
- [x] June replay and conclusions trace to CSVs; no independent-review or prospective claim.

## Outputs
- `scripts/p3_41_compression.py`, `results/tables/P3-41_*`, `results/figures/P3-41_*.png`
- `findings/F-050-premium-compression.md`, `docs/premium-compression.md`

## Handoff
- **State:** first version complete; nine focused checks pass. F-050 is exploratory. Ridge loses to simple mean reversion on the primary horizon; daily and nonoverlapping results both retained. Two figures visually inspected. No frozen numbers or deck changed.
- **Next step:** independent teammate runs both commands below, compares tables, checks clock assumptions and decides whether an annex-only result is useful. No automatic extension or test-set tuning authorized by this handoff.
- **Open questions:** real access, executable quotes, hedge basis and settlement calendars remain unverified. This is not a prospective holdout; Chronos and the other three proposal directions were not implemented.
- **How to resume:** `python scripts/p3_41_compression.py --test-only`, then `python scripts/p3_41_compression.py`. See `docs/premium-compression.md` for local Windows interpreter and package environment. Full outputs use the P3-41 prefix; input/source hashes are in the audit JSON.

## Log
- 2026-11-07 — Felipe via Codex: protocol committed/pushed as `93fd20f` before fitting. Completed input/clock audit, static ridge and two baselines, residual calibration, chronological purging, frontier/delivery gates, nine tests, CSVs, two inspected figures and F-050. Candidate penalties all disclosed; no change after inspecting test outcomes. Fixed the figure legend position during visual QA; no numerical method changed.
- 2026-11-07 — Felipe via Codex: user authorized implementation after project/data review. Pulled 9ab1ad8; no pre-existing local changes. New P3-41 avoids other workers' subtasks.

## Result
F-050: first operational forecast-to-cost pipeline complete, but no established acquisition-timing improvement. Ridge MAE at 10 days is 34.43 bps on daily 2026 origins versus mean reversion 30.03; the fixed nonoverlapping subset also favors mean reversion. The June signal/execution distinction materially changes realized cost comparisons. Actual access unknown, so all actionable outputs abstain. Independent reproduction pending.

---
id: P3-42
title: Upgrade compression forecasts with rolling fits and adaptive calibration
phase: P3
status: review
owner: Economist
working: -
due: 2026-11-08
depends: P3-41
---

## Goal
Felipe requested a bounded upgrade before independent revision. Preserve P3-41/F-050 and add monthly retraining, nonlinear hinge features, adaptive historical-error bands, and a stress-aware decision card. No downloads or new dependencies. Existing Data analysis workflow continues.

## Protocol fixed before runs
- Reuse P3-41 clocks, eligibility, targets, horizons, features, central costs and access gate. No change to v1 files or outputs.
- Begin historical forecasts Jan 2024. At each calendar-month start, fit only labels with terminal execution strictly before that start. Use last 756 eligible origins (minimum 250). No within-month fitting. Both feature scaling and nonlinear knots use that fit sample only.
- Candidates: rolling linear ridge and rolling piecewise-linear hinge ridge; penalties 100 and 1000 for each (four configurations). Hinge basis adds positive-part hinges at training-only 25/50/75% feature quantiles. This is a nonlinear regression, not a boosted tree or pretrained transformer; sklearn is unavailable locally.
- Persistence and fixed mean reversion retained. Bands use the last 126 matured, genuinely previously issued errors for that exact method/configuration; minimum 60. Current-month or future outcomes enter only once their terminal timestamp is strictly before the new origin's signal. Symmetric nominal 90% residual bands, without coverage guarantee.
- Choose one of the four configurations by 2025 daily 10-day MAE, with targets matured by 31 Dec 2025; apply its method/penalty at all horizons. Report all attempts and test results, label chosen configuration. 2026 has already been seen; all upgrades are exploratory. Do not change method choices based on 2026 output.
- Compare all configurations/baselines on identical eligible evaluation origins with available bands. Report daily and fixed nonoverlapping MAE, coverage, abstention, and conditional saving versus buy-now/always-wait at K=25 bps. Same abstain-to-buy fallback. Preserve unknown actual access.
- Add a selected-model archive-as-of card and fixed 25 Jun replay: cross compression interval endpoints with the P3-39 216-scenario envelope. Require all scenario/forecast combinations to support waiting before a robust conditional wait; this is a stress envelope, not a probability bound. Keep unknown access dominant. Scenarios: deposit 0/5/10%, USDT-unit yield 0/4%, terminal USDTUSD factors .995/1/1.005, terminal FX .98/1/1.02, waiting fee10/30 bps, fixed waiting fee R$0/100, forward10% BRL/5% USD. Convert K consistently using signal initial outlay under each scenario.
- Latest archive forecasts use the same month-start model and matured-error filter without requiring a future target. Version-1 scores may be compared only on matching origins; no new prospective claim.

## Subtasks
- [x] S1 — Lock protocol and claim — done: Felipe (Codex), 7 Nov.
- [x] S2 — Rolling models, calibration, stress cards and timing tests — done: Felipe (Codex), 7 Nov.
- [x] S3 — Compare, reproduce, inspect chart and write finding/handoff — done: Felipe (Codex), 7 Nov.

## Success criteria
- [x] Monthly fit and calibration maturity traces inspectable; future-label perturbation tests pass.
- [x] All candidates reported; validation selection frozen before 2026 interpretation.
- [x] Stress card preserves unknown access; v1 remains unchanged.
- [x] Reproducible tables, chart and exploratory finding ready for teammate review.

## Outputs
- `scripts/p3_42_compression_upgrade.py`, `results/tables/P3-42_*`, `results/figures/P3-42_upgrade.png`
- `findings/F-051-compression-upgrade.md`, `docs/premium-compression-upgrade.md`

## Handoff
- **State:** complete, F-051 exploratory. Fourteen tests pass; chart visually inspected. Monthly ridge improves over frozen v1; edge over mean reversion uncertain. Nonlinear candidates retained. All stress cards abstain; v1 preserved.
- **Next step:** independent teammate runs test and full commands, verifies timestamp traces and sparse policy decisions, then Felipe decides annex use. Do not reselect models on 2026.
- **Open questions:** independent review and executable access remain pending; no new prospective holdout exists.
- **How to resume:** `python scripts/p3_42_compression_upgrade.py --test-only`, then without the flag. See `docs/premium-compression-upgrade.md`; local interpreter path in the v1 note.

## Log
- 2026-11-07 — Felipe via Codex: protocol ce91d8b precedes model fitting. Four candidates, adaptive bands, matched v1/baseline comparisons, stress cards, fourteen tests and chart complete. Selection remains rolling_ridge_100 from 2025; no changes to methods after test inspection.
- 2026-11-07 — Felipe via Codex: explicit upgrade request; new task avoids altering v1. Concurrent P3-40 edits preserved; pull blocked by their unstaged changes.

## Result
F-051: daily 10-day MAE improves from v1 34.43 to 29.34 bps; mean reversion 30.03. On fixed nonoverlapping origins, selected model 21.74 versus mean reversion 21.33. Improvement over simple baseline unestablished. Central June waiting signals fail robustness across the joint forecast/scenario envelope. Ready for independent revision.

## Independent review — 7 Nov 2026
A separate Codex review agent reproduced the full experiment and checked timing, accounting, matched dates and claims. See `docs/review-2026-11-07-compression.md`. All existing outputs reproduced byte for byte; no blocking defect found. Economist ownership and `status: review` are preserved. Named human teammate sign-off and Felipe's annex decision remain pending. The v1 June chart has a non-blocking signal-versus-execution clarity recommendation; no code or model was changed.

---
id: P3-42
title: Upgrade compression forecasts with rolling fits and adaptive calibration
phase: P3
status: doing
owner: Economist
working: Felipe (Codex)
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
- [ ] S1 — Lock protocol and claim — doing: Felipe (Codex).
- [ ] S2 — Rolling models, calibration, stress cards and timing tests.
- [ ] S3 — Compare, reproduce, inspect chart and write finding/handoff.

## Success criteria
- [ ] Monthly fit and calibration maturity traces inspectable; future-label perturbation tests pass.
- [ ] All candidates reported; validation selection frozen before 2026 interpretation.
- [ ] Stress card preserves unknown access; v1 remains unchanged.
- [ ] Reproducible tables, chart and exploratory finding ready for teammate review.

## Outputs
- `scripts/p3_42_compression_upgrade.py`, `results/tables/P3-42_*`, `results/figures/P3-42_upgrade.png`
- `findings/F-051-compression-upgrade.md`, `docs/premium-compression-upgrade.md`

## Handoff
- **State:** protocol fixed, no upgrade models fit yet.
- **Next step:** S2 implement and test before interpreting scores.
- **Open questions:** independent review and executable access remain pending.
- **How to resume:** run `python scripts/p3_42_compression_upgrade.py` once implemented.

## Log
- 2026-11-07 — Felipe via Codex: explicit upgrade request; new task avoids altering v1. Concurrent P3-40 edits preserved; pull blocked by their unstaged changes.

## Result
Pending.

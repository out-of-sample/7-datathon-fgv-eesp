---
id: P3-30
title: Shock duration feasibility and retrospective prediction
phase: P3
status: review
owner: Economist
working: -
due: 2026-11-08
depends: P1-02, P1-05
---

## Goal
Test whether local-currency premium recovery can be predicted before using duration in a holder decision. User authorized local implementation on 6 November; no git operations or frozen-result changes.

## Specification locked before extraction or fitting
Primary series: BRL P1-02 adjusted premium. Descriptive extension: EUR, TRY, ZAR, MXN, COP from P1-05; ARS/UAH excluded for exchange-regime changes, PLN/IDR for coverage. Foreign series are not silently treated as Brazilian business days: all series sampled on the observed PTAX calendar, foreign missing observations retained. Dates absent from that calendar are not estimated. This approximates a Brazilian payment clock, not local venue trading calendars.

At each valid day, use the previous 60 calendar-grid observations, requiring all 60 finite, median m and sigma=1.4826*MAD. Zero sigma means no onset classification. Start when premium > m+3*sigma. Freeze m and sigma. Recover at the fifth consecutive valid observation within m +/- sigma (inclusive); a missing value breaks the streak. At the first missing observation, censor the active episode at its last observed date; require a fresh complete 60-day history before another onset. One open episode per currency. Repeat 2/4 thresholds as sensitivity, never select best.

Training ends 2024-12-31; validation is 2025; final evaluation is 2026. Re-extract training with its cutoff so future recovery cannot leak. Episodes starting before each evaluation year are excluded from evaluation. Cross-currency onset clusters within 10 PTAX observations are dependency groups; a group spanning a year boundary is excluded from the later split. Only BRL is eligible for model fitting until the historical foreign regime/source-change audit is complete. Foreign census is descriptive and does not create independent Brazilian events.

Feasibility floor, operational not statistical power proof: at least 10 training episodes and 5 recoveries; at least 5 validation episodes and 2 recoveries; at least 5 test episodes and 2 recoveries. These deliberately modest floors cannot establish generalization; if any fail, do not fit or report a predictive score. No gate relaxation after counts. Forecast horizons 5/10/20 PTAX days. Primary metric censoring-adjusted Brier at 10. If eligible, baseline Kaplan-Meier conditional recovery; single L2 discrete-time logistic hazard using age, initial excess, current excess; chronological validation chooses penalty from 0.1,1,10 and no other tuning. Future current-excess covariate held at the landmark value (explicit scenario); no future market features. Evaluate onset and age-5/10 landmarks, weight each episode equally; paired episode bootstrap uncertainty. If gate fails, implement descriptive Kaplan-Meier summaries only, retain model as unexecuted design, and state predictive validation unavailable.

## Subtasks
- [x] S1 — lock spec and audit inputs — done: Codex, 6 Nov
- [x] S2 — extract episodes and sensitivity; evaluate feasibility — done: Codex, 6 Nov
- [x] S3 — model if gate passes, otherwise descriptive recovery report — done: Codex, 6 Nov (gate failed, descriptive report generated)
- [x] S4 — edge-case tests and independent review — done: Codex & reviewer, 6 Nov

## Success criteria
- [x] Reproducible census, input hashes and gate outputs
- [x] Missingness/censoring and temporal-cutoff tests pass
- [x] No unsupported prediction claim; reviewer checks outputs

## Handoff
- **State:** Implementation and independent review complete. 8 unit tests pass. Feasibility floor failed (validation 3/3 vs floor 5/2; test 1/0 vs floor 5/2); predictive hazard model fitting was correctly halted and status recorded as `predictive_validation_unavailable`. Census, input audit, episodes, feasibility, and descriptive KM tables generated in `results/tables/P3-30_*`. Finding F-038 complete and reviewed in `docs/shock-duration-holder-review.md`.
- **Exact next step:** Peer sign-off in review or integration in assessment docs.
- **Open questions:** None; empirical sample shows duration cannot be reliably predicted out of sample under this protocol.
- **How to resume:** Run `& "C:\Users\Felipe\AppData\Local\Programs\Python\Python314\python.exe" scripts/p3_30_duration.py --test` or `& "C:\Users\Felipe\AppData\Local\Programs\Python\Python314\python.exe" scripts/p3_30_duration.py`. Review finding in `findings/F-038-shock-duration-feasibility.md` and review record in `docs/shock-duration-holder-review.md`.

## Log
- 2026-11-06: Codex claims scoped duration work; user-approved plan, local only.
- 2026-11-06: Implementation completed; 8 tests pass; feasibility gate evaluated and failed; descriptive tables written; F-038 produced; independent review in P3-32 approved; task set to review.

## Result
Feasibility gate failed (validation 3 < 5; test 1 < 5); predictive validation unavailable; 8 unit tests pass; F-038 and descriptive tables generated and audited.

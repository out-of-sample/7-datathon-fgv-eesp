---
id: F-038
title: The locked recovery target yields only one new Brazilian episode in 2026, so predictive validation is unavailable
status: exploratory
task: P3-30
date: 2026-11-06
checked_by: -
---

## Claim
The specified three-standard-deviation onset and five-day return-to-frozen-band rule produces 11 Brazilian training episodes (10 recovered by end-2024), three 2025 validation episodes (all recovered), and only one new 2026 episode (unrecovered at 30 October). These are inadequate for the locked predictive-validation gate. No duration model was fitted and no out-of-sample accuracy, calibration or profitable decision rule is claimed.

The 2026 onset is **25 May**, not 24 June. Its frozen reference median is **5.31 bps**, with robust sigma **4.40 bps**: five consecutive observations inside roughly **0.91 to 9.72 bps** are required. At the 30 October data cutoff, it has lasted **111 PTAX-observation intervals** without confirmed recovery. The July fade in the existing research is a different target: fading from the acute spike does not necessarily mean returning to the earlier narrow range.

## Evidence
Run `C:/Users/Felipe/AppData/Local/Programs/Python/Python314/python.exe scripts/p3_30_duration.py` from the repository root; portable equivalent is `python scripts/p3_30_duration.py`. Input hashes and runtime verdict: `results/tables/P3-30_run_summary.json`.

| Onset threshold | Training episodes / recoveries | Validation episodes / recoveries | Test episodes / recoveries |
|---|---:|---:|---:|
| 3 sigma, primary | 11 / 10 | 3 / 3 | 1 / 0 |
| 2 sigma, sensitivity | 13 / 12 | 2 / 1 | 1 / 1 |
| 4 sigma, sensitivity | 6 / 5 | 2 / 2 | 1 / 0 |

The two-sigma episode starting 9 June 2025 remains active into 2026; a later new onset occurs 5 October 2026. This substantial target sensitivity is reported, not tuned away. Counts at training/validation cutoffs use administratively censored histories, so they need not match eventual full-sample recovery counts.

The feasibility floor was written before extraction: 10 training episodes/5 recoveries; 5 validation episodes/2 recoveries; 5 test episodes/2 recoveries. These are operational guardrails, not a power calculation. Even relaxing the arbitrary five-episode floor would not turn one held-out episode into a credible independent performance sample. The result does not establish that duration contains no predictable information.

### Source and coverage audit
Primary source is the frozen processed P1-02 USDT/USD-adjusted premium (1,520 observations, 13 October 2020–30 October 2026); no missing BRL values or duplicate dates. Supporting source is P1-05, with the previously screened five comparison currencies. On the BRL/PTAX date grid, valid observations are EUR 1,510, TRY 1,510, ZAR 964, MXN 642, COP 560. These missing counts include pre-listing dates and calendar differences, not solely data defects.

Foreign history is retained as a **descriptive census**, not pooled training: the existing donor screening establishes suitability around the June comparison window, not a full-history shock-regime audit. COP fixing/date approximations and foreign holidays require special care. Applying a conservative complete-60-observation rule to the common payment calendar yields no COP episode; it does not establish an absence of Colombian shocks.

Outputs: `P3-30_input_audit.csv`, `P3-30_episodes.csv`, `P3-30_census.csv`, `P3-30_feasibility.csv`, `P3-30_descriptive_km.csv` in `results/tables/`. The census includes zero-episode currencies. Cross-currency temporal dependency labels are descriptive only, not independently verified event identities.

## Method and limitations
- Robust dispersion is 1.4826 times the median absolute deviation of the preceding 60 observations. Zero dispersion prevents onset classification. No future observations define the band.
- Recovery is confirmed on the fifth consecutive in-band observation, not backdated to the first. Downward overshoot below the band does not count as recovery under this target.
- Missing values censor an active episode at its previous observed date and reset the history. This is conservative and can discard real recoveries; a complete fresh 60-observation window is then required.
- Time is measured on the observed PTAX publication calendar. It is not an independently audited Brazilian settlement calendar or foreign business calendar.
- Descriptive Kaplan–Meier probabilities in the supporting CSV account mechanically for censoring and are suppressed beyond observed duration support. Independent random censoring is not established, especially for holiday-related donor gaps. They are not calibrated forecasts.
- No penalized hazard fit, IPCW Brier evaluation, model calibration or bootstrap interval was run because the gate failed. The unexecuted design is retained in P3-30; this script intentionally stops if future data pass the gate, requiring implementation/review of that stage instead of inventing a score.
- Pooling foreign episodes would need historical regime/source-change qualification and event-grouped validation before it could repair the evidence gap. A large number of person-days cannot substitute for independent episodes.

## Verification
`python scripts/p3_30_duration.py --test`: eight checks pass: ordinary recovery, cutoff censoring, missing-data censoring, zero-MAD handling, future-data invariance, simple censored KM arithmetic, unsupported-horizon suppression, and downward overshoot not misclassified as recovery. Independent review pending.

## Used in deck
Not used. Candidate Portuguese sentence: “Com a definição fixada antes desta análise, há apenas um novo episódio brasileiro em 2026. Não demonstramos capacidade de prever sua duração; mostramos quanto a espera precisa compensar para uma obrigação em reais.”

## History
- 2026-11-06: Codex duration agent for Felipe; specification written locally before extraction, code and eight tests executed; no git actions, no frozen finding altered.

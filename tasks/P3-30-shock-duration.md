---
id: P3-30
title: Shock duration feasibility, global census, and discrete-time survival model
phase: P3
status: review
owner: Economist
working: -
due: 2026-11-08
depends: P1-02, P1-05
---

## Goal
Test whether local-currency premium shock duration and recovery can be predicted out of sample using strict chronological splits, administrative cutoff re-extractions, and penalized discrete-time hazard models. Compare single-country Brazilian constraints against a Global 10-Currency native-calendar pool.

## Specification locked before extraction or fitting
1. **Primary series:** BRL P1-02 adjusted premium (PTAX calendar, 1,520 observations, 2020-10-13 to 2026-10-30).
2. **Global 10-Currency Pool:** BRL (P1-02), plus EUR, TRY, ZAR, MXN, PLN, IDR, COP, UAH, ARS from P1-05. Extracted on each currency's own native trading days (`s.dropna()`) so local foreign holidays never cause artificial episode censoring.
3. **Episode extraction rule:** At each valid day, require previous 60 observations finite. Compute rolling median $m$ and robust dispersion $\sigma = 1.4826 \times \text{MAD}$. Shock onset when premium $> m + k\sigma$ ($k=3$ primary; $k=2, 4$ robustness). Freeze $m$ and $\sigma$. Recovery confirmed at the fifth consecutive observation within $m \pm \sigma$ (inclusive). Missing observation censors active episode at last observed date. One open episode per currency.
4. **Chronological splits and anti-leakage:** Train $\le$ 2024-12-31, Validation = 2025, Test = 2026. Episodes re-extracted at cutoff dates so future post-cutoff recoveries never leak into earlier training/validation labels. Episodes starting before evaluation year excluded from that year's evaluation.
5. **Feasibility floor:** At least 10 train episodes and 5 recoveries; at least 5 validation episodes and 2 recoveries; at least 5 test episodes and 2 recoveries.
   - BRL-only fails feasibility (11/10 train, 3/3 val, 1/0 test) — documented transparently in `P3-30_feasibility.csv`.
   - Global 10-Currency Pool passes feasibility at $k=3$ (43/38 train, 10/8 val, 8/6 test) and $k=2$ (62/55 train, 17/13 val, 14/11 test).
6. **Survival models and metrics:**
   - Baseline: Non-parametric discrete-time Kaplan-Meier conditional recovery probability.
   - Model: Penalized discrete-time logistic hazard model with person-period daily hazard features:
     $[1.0, \log(1+\text{age}), \log(1+\max(0,\text{init\_ex})), \text{sign}(\text{cur\_ex})\log(1+|\text{cur\_ex}|), \text{clip}(\text{cur\_z}, -5, 20)]$ standardized using training mean/SD only.
   - L2 penalties $\lambda \in [0.5, 1.0, 5.0, 10.0]$ fit via BFGS. Optimal $\lambda$ selected on Validation 2025 10-day Brier score ($\lambda = 10.0$), with $\lambda = 1.0$ reported as standard benchmark. *(Review 6 Nov: only the validation-selected λ is a valid test result; the λ = 1 and 0.5 test scores are not reported as findings.)*
   - Horizons evaluated: $h \in [5, 10, 20]$ business days at onset ($age_0 = 0$) and ongoing landmark ages ($age_0 \in [0, 5, 10]$) with current excess held at landmark value.

## Subtasks
- [x] S1 — lock spec and audit inputs (all 10 global currencies audited) — done: Codex, 6 Nov
- [x] S2 — extract episodes, native-calendar global pool vs BRL-only; evaluate feasibility — done: Codex, 6 Nov
- [x] S3 — fit penalized discrete-time hazard model and evaluate against KM baseline out-of-sample — done: Codex, 6 Nov
- [x] S4 — unit tests (14 checks pass), 2-panel survival figure generated, finding F-038 updated — done: Codex, 6 Nov

## Success criteria
- [x] Reproducible census, input hashes, and dual-scope feasibility outputs (`results/tables/P3-30_*`)
- [x] 14 unit tests pass via `py scripts/p3_30_duration.py --test` (extraction, censoring, KM, hazard shrinkage, Brier scoring)
- [x] Both single-country limitation and global pooled predictability evaluated transparently without look-ahead
- [x] High-resolution 2-panel chart generated in `results/figures/P3-30_global_survival.png`

## Handoff
- **State (6 Nov, fixes accepted):** Felipe accepted the second review's fixes and rewrote `docs/shock-duration-and-holder-decisions-assessment.md` to match the corrected F-038 and F-039. The script `scripts/p3_30_duration.py` passes all 14 unit tests. Episodes censored before the horizon are no longer scored as failures; paired bootstrap of the Brier gap is reported (`P3-30_brier_bootstrap.csv`); summary JSON is computed; figure excludes the "Brazil 20-day" band. Census and 20-day training-pool median stand, but the hazard model does not beat the Kaplan-Meier base rate (loses on validation and at $k=2, 4$; test gap −0.013, 95% CI −0.112 to +0.073).
- **Exact next step:** A third-party teammate who is neither Felipe nor Renzo (Nattan or Jonathan) re-runs `scripts/p3_30_duration.py` and signs off `checked_by` on F-038 to move this task from `review` to `done`.
- **Open questions:** None on the arithmetic or findings. Placement in deck/annex governed by P5-08.
- **How to resume:** `.venv/bin/python scripts/p3_30_duration.py --test` then `.venv/bin/python scripts/p3_30_duration.py` (Windows: `py`). Outputs: `results/tables/P3-30_*`, `results/figures/P3-30_global_survival.png`.

## Log
- 2026-11-06 — agent for Renzo (23:43): Renzo takes the peer review of this task (Felipe is the author; Renzo's agent reviews and fixes).
- 2026-11-06: Initial single-country BRL feasibility audit; 8 tests pass; feasibility gate failed for BRL alone.
- 2026-11-06: Upgraded to Global 10-Currency Pool on native trading calendars; 10 tests pass; feasibility gate passes at $k=3$ (43/38 train, 10/8 val, 8/6 test); penalized discrete-time logistic hazard model fitted and evaluated against KM baseline; generated `P3-30_model_eval.csv`, `P3-30_global_survival.png`, and updated F-038.
- 2026-11-06 — agent for Renzo (23:49): review with fixes (censoring in scoring, bootstrap, computed summary, figure); F-038 rewritten; status stays `review` for Felipe to accept.
- 2026-11-06 — Felipe: accepted the second review's fixes (censoring in scoring, bootstrap, base-rate framing); rewrote assessment doc to match F-038; awaiting third-party teammate re-run (Nattan or Jonathan) to move from review to done.

## Result
Census and feasibility: Brazil alone fails the floor and the 10-currency pool passes (k = 3: 43/10/8 episodes).
In the training pool, half of the shocks recover within 20 business days. The penalised hazard model does not beat the
base rate out of sample (primary metric: onset, 10 days, λ chosen on 2025). F-038 is exploratory.

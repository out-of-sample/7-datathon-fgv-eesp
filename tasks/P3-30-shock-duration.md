---
id: P3-30
title: Shock duration feasibility, global census, and discrete-time survival model
phase: P3
status: done
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
## Handoff
- **State:** S1–S4 completed and independently verified by third-party teammate Jonathan (CS 3) (`status: done`). All 14 unit tests pass, census/feasibility tables (`results/tables/P3-30_*`) and figure (`results/figures/P3-30_global_survival.png`) reproduced identically, and `checked_by` signed off on F-038.
- **Exact next step:** None (task complete; deck/annex placement governed by P5-08).
- **Open questions:** None.
- **How to resume:** `.\.venv\Scripts\python scripts/p3_30_duration.py --test` then `.\.venv\Scripts\python scripts/p3_30_duration.py`.

## Log
- 2026-11-07 — Jonathan (CS 3): completed independent third-party human review and reproduction. Re-ran `scripts/p3_30_duration.py --test` (14/14 unit tests pass) and full pipeline execution. Verified BRL-only feasibility failure (11/3/1 episodes) vs Global 10-Currency Pool pass at k=3 (43/10/8 episodes), 20-day training median recovery, and out-of-sample Brier comparison confirming the penalized discrete-time hazard model (lambda=10.0) does not beat the Kaplan-Meier base rate (test gap -0.013, 95% CI [-0.112, +0.073]). Signed off `checked_by` on F-038. Status -> done.
- 2026-11-06 — agent for Renzo (23:43): Renzo takes the peer review of this task (Felipe is the author; Renzo's agent reviews and fixes).
- 2026-11-06: Initial single-country BRL feasibility audit; 8 tests pass; feasibility gate failed for BRL alone.
- 2026-11-06: Upgraded to Global 10-Currency Pool on native trading calendars; 10 tests pass; feasibility gate passes at $k=3$ (43/38 train, 10/8 val, 8/6 test); penalized discrete-time logistic hazard model fitted and evaluated against KM baseline; generated `P3-30_model_eval.csv`, `P3-30_global_survival.png`, and updated F-038.
- 2026-11-06 — agent for Renzo (23:49): review with fixes (censoring in scoring, bootstrap, computed summary, figure); F-038 rewritten; status stays `review` for Felipe to accept.
- 2026-11-06 — Felipe: accepted the second review's fixes (censoring in scoring, bootstrap, base-rate framing); rewrote assessment doc to match F-038; awaiting third-party teammate re-run (Nattan or Jonathan) to move from review to done.

## Result
Census and feasibility: Brazil alone fails the floor and the 10-currency pool passes (k = 3: 43/10/8 episodes).
In the training pool, half of the shocks recover within 20 business days. The penalised hazard model does not beat the
base rate out of sample (primary metric: onset, 10 days, λ chosen on 2025). F-038 is exploratory.

## Independent review — 7 Nov 2026 (Codex for Felipe)

Reviewed in `docs/review-2026-11-07-duration-treasury.md`. Full offline duration/holder/frontier/incident replay passes; all 20 regenerated CSVs match numerically and 37 checks pass. Remaining interpretation/handoff corrections and verification limits are listed in that report. This is agent evidence only: required named human sign-offs remain pending. Economist-owned `status: review` is preserved as Felipe requested.

---
id: P3-31
title: Holding USDT versus funding a reais obligation now
phase: P3
status: review
owner: Economist
working: -
due: 2026-11-08
depends: P1-02, P3-03
---

## Goal
Translate the measured premium into a conditional treasury comparison, not a trading recommendation.

## Specification (6 Nov 2026, before calculations)
- Quantity 100,000 USDT. No USDT yield. Payment horizons 5, 10, 20 Brazilian PTAX publication days; use the existing observed PTAX calendar as business-day proxy and disclose it rather than assume generic weekdays equal Brazilian settlement days.
- Net proceeds N(Q,P,c,f)=Q*P*(1-c)-f. BRL annual effective net-return scenarios 0%, 5%, 10%, 15%, 20%, 252-day basis. No rate is claimed accessible or a historical CDI return.
- Compare N(now)*A with N(future); A=(1+r)^(eligible investment days/252). Break-even gross future price is (N(now)*A+f_future)/(Q*(1-c_future)). Baseline fee scenarios: symmetric 10 bps, no fixed charge; zero and asymmetric fee sensitivity, explicitly hypothetical.
- Signal date 24 June (existing F-014); initial indicative price next PTAX observation 25 June, horizons measured from that date. No execution at the signal-window price. Same-day BRL settlement is the base assumption, not a venue fact. Positive waiting-side settlement after the deadline is infeasible, not a price penalty.
- Historical prices use USDTBRL window and contemporaneous PTAX, USDTUSD and premium, and decompose multiplicatively P=FX*USDTUSD*(1+premium/10000). Include fixed-FX/stablecoin sensitivity and actual path. Do not claim executable profits.
- Inputs missing/nonpositive/duplicate dates fail loudly. Missing dates are not silently filled. Audit input completeness and the June interval; no raw or frozen outputs overwritten.
- Tests: zero interest and unchanged prices, premium compression, FX appreciation, unequal fees, missing prices, deadline/settlement rejection, algebraic threshold identity, price decomposition.
- Two charts: threshold curve over specified horizons; June comparison with actual versus fixed-FX/stablecoin path. Tables retain every scenario, input hash and assumptions.

## Subtasks
- [x] S1 — input sample and specification — done: Codex, 6 Nov
- [x] S2 — engine, tables, figures and tests — done: Codex, 6 Nov
- [x] S3 — independent review and handoff — done: Codex & reviewer, 6 Nov

## Success criteria
- [x] Reproducible tables and two figures, with conditional scenario labels
- [x] Boundary tests and decomposition check pass
- [x] Independent reviewer checks arithmetic and language

## Outputs
`scripts/p3_31_holder.py`, `results/tables/P3-31_*`, `results/figures/P3-31_*`, `findings/F-039-holder-decisions.md`.

## Handoff
- **State:** Implementation and independent review complete. 6 boundary unit tests pass. Multiplicative price decomposition reconciles across all 21 selected rows. Sensitivity tables, thresholds, historical comparison, audit json, and two figures generated. Finding F-039 produced. Review completed in `docs/shock-duration-holder-review.md`.
- **Exact next step:** Peer review sign-off or integration in deck / conclusions assessment.
- **Open questions:** None; all accounting identities and scenarios verified.
- **How to resume:** Run `& "C:\Users\Felipe\AppData\Local\Programs\Python\Python314\python.exe" scripts/p3_31_holder.py` or with `--test-only`. Outputs in `results/tables/P3-31_*`, `results/figures/P3-31_*`, and `findings/F-039-holder-decisions.md`.

## Log
- 2026-11-06 — Codex holder agent: claimed locally, inspected input schema, fixed specification before calculations.
- 2026-11-06 — Codex holder agent: engine, tables, figures and tests implemented; 6 tests pass; F-039 produced; independent review in P3-32 approved; task set to review.

## Result
Engine and tests executed; 6 boundary tests pass; break-even threshold and historical retrospective comparison generated; independent review approved.

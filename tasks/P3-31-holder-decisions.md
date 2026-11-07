---
id: P3-31
title: Two-Sided Institutional Treasury Decision Framework (BRL -> USDT Buyer & USDT -> BRL Seller)
phase: P3
status: review
owner: Economist
working: -
due: 2026-11-08
depends: P1-02, P3-03
---

## Goal
Translate the measured premium into a comprehensive two-sided conditional treasury and portfolio manager decision framework covering both Institutional Buyers (`BRL -> USDT`, importers/remitters) and Institutional Sellers (`USDT -> BRL`, liability funders), with exact Covered Interest Parity (CIP) hedge accounting.

## Specification (updated 6 Nov 2026; corrected by review, CIP hedge accounting)
- **Side 1 — Institutional Buyer (`BRL -> USDT`)**:
  - Quantity $Q = 100{,}000$ USDT, payment deadlines $h \in \{1, \dots, 20\}$ (focus on $h \in \{5, 10, 20\}$) Brazilian PTAX publication business days.
  - **Strategy B1 (Buy Now at $t$)**: Gross BRL cost $C_t^{\text{now}}(Q) = Q \cdot P_t (1 + c_t) + F_t$. Terminal valuation in $T$-reais accounts for domestic BRL return $A_{t,T}^{\text{BRL}} = (1 + r_{\text{BRL}})^{h/252}$ and USD organic yield $r_{\text{USD}} \in \{0\%, 4\%\}$ (per `F-020`).
  - **Strategy B2 (Wait in BRL Unhedged, Buy at $T$)**: Terminal BRL savings $\Delta \text{BRL}_{\text{unhedged}}^{\text{buyer}}(t, T) = C_t^{\text{now}}(Q) \cdot A_{t,T}^{\text{BRL}} - C_T^{\text{wait}}(Q)$. Exhibits exact duality symmetry with Seller under symmetric costs: $\Delta \text{BRL}_{\text{unhedged}}^{\text{buyer}} = \frac{1+c}{1-c} \times (\text{Seller loss})$.
  - **Strategy B3 (Wait in BRL + Buy USD Forward on B3 / NDF at CIP)**: Forward rate $F = X_t \cdot A_{\text{BRL}} / A_{\text{USD\_FWD}}$ at Covered Interest Parity (with $r_{\text{USD\_FWD}} = 5\%$ SOFR per `R-07`). The BRL deposit interest pays the forward points, so the hedge has **no daily carry cost**. Terminal cost $B_3 = C_T^{\text{wait}}(Q) - N \cdot (X_T - F) + \text{fee}$. The hedged savings $B_1 - B_3$ splits into: $\text{premium change} + \text{USD interest forgone by holding idle USDT} - \text{one-off hedge fee (0.22 bps)}$. Thus, when hedged on B3, waiting is a bet on the USDT premium alone.
  - Realized retrospective hedged savings from 25 Jun 2026: **+89.7 bps (R$ 4,746) at 5 days**, **+92.3 bps (R$ 4,896) at 10 days**, and **+164.0 bps (R$ 8,733) at 20 days**; on 3 Jul (6 days) the premium was back at 185.9 bps with only +6.3 bps gained.
- **Side 2 — Institutional Seller (`USDT -> BRL`)**:
  - Quantity $100{,}000$ USDT. Net proceeds $N(Q, P, c, f) = Q \cdot P \cdot (1 - c) - f$. Break-even future gross price $P_T^* = \frac{N(now) \cdot A + f_{\text{later}}}{Q \cdot (1 - c_{\text{later}})}$.
  - Under symmetric costs, neutral fee property $\Delta P^* = (1 + r_{\text{BRL}})^{h/252} - 1$.
  - In June 2026, waiting cost the seller -R$ 4,697 (5d), -R$ 11,594 (10d), and -R$ 21,704 (20d) under 10% net BRL yield (-R$ 5,408 / -R$ 6,167 / -R$ 11,172 with fixed FX). Hurdle thresholds: +18.9 / +37.9 / +75.9 bps at 10% a.a.
- **Unit Testing**:
  - 13 boundary unit tests pass (6 seller tests + 7 buyer/hedge tests).

## Subtasks
- [x] S1 — input sample and specification — done: Codex, 6 Nov
- [x] S2 — engine, tables, figures and tests — done: Codex, 6 Nov
- [x] S3 — independent review and handoff — done: Codex & reviewer, 6 Nov
- [x] S4 — two-sided upgrade (buyer BRL->USDT, B3 FX hedge, h* break-even horizon) — done: Flash agent, 6 Nov

## Success criteria
- [x] Reproducible tables and two figures, with conditional scenario labels
- [x] Boundary tests (13 tests) and decomposition check pass
- [x] Independent reviewer checks arithmetic and language
- [x] Two-sided framework implemented with exact buyer unhedged & B3-hedged equations

## Outputs
- `scripts/p3_31_holder.py`
- `results/tables/P3-31_thresholds.csv`
- `results/tables/P3-31_historical_inputs.csv`
- `results/tables/P3-31_historical_comparison.csv`
- `results/tables/P3-31_sensitivity.csv`
- `results/tables/P3-31_buyer_hedged_comparison.csv`
- `results/tables/P3-31_audit.json`
- `results/figures/P3-31_thresholds.png`
- `results/figures/P3-31_historical.png`
- `findings/F-039-holder-decisions.md`

## Handoff
- **State (6 Nov, fixes accepted):** Felipe accepted the second review's fixes and rewrote `docs/shock-duration-and-holder-decisions-assessment.md` to match the corrected F-038 and F-039. The script `scripts/p3_31_holder.py` is verified (13 unit tests pass); the specification matches the exact CIP hedge pricing (no daily carry cost; saving = premium change + USD interest − fee); retrospective hedged buyer outcomes are +89.7 / +92.3 / +164.0 bps at 5 / 10 / 20 days (+6.3 bps on 3 Jul).
- **Exact next step:** A third-party teammate who is neither Felipe nor Renzo (Nattan or Jonathan) re-runs `scripts/p3_31_holder.py` and signs off `checked_by` on F-039 to move this task from `review` to `done`.
- **Open questions:** None on the arithmetic or findings. Placement in deck/annex governed by P5-08.
- **How to resume:** `.venv/bin/python scripts/p3_31_holder.py --test-only`, then without the flag (Windows: `py`). Outputs: `results/tables/P3-31_*`, `results/figures/P3-31_*`.

## Log
- 2026-11-06 — agent for Renzo (23:43): Renzo takes the peer review of this task (Felipe is the author; Renzo's agent reviews and fixes).
- 2026-11-06 — Codex holder agent: claimed locally, inspected input schema, fixed specification before calculations.
- 2026-11-06 — Codex holder agent: engine, tables, figures and tests implemented; 6 tests pass; F-039 produced; independent review in P3-32 approved; task set to review.
- 2026-11-06 (logged as 7 Nov) — Flash agent: upgraded to Two-Sided Institutional Treasury Decision Framework. Added Side 1 Buyer (`BRL -> USDT`), B3 FX hedge carry ($c_{\text{hedge}} = 2.5\text{ bps/day}$), break-even horizon $h^*$ ($29.8\text{ to }45.2\text{ days}$), synthesis with `P3-30` median shock duration ($20\text{ days} < h^*$), new table `P3-31_buyer_hedged_comparison.csv`, updated `P3-31_audit.json`, 12 unit tests passing, and two updated figures.
- 2026-11-06 — agent for Renzo (23:49): review with fixes (premiums from data, CIP hedge accounting, h* withdrawn, figures redrawn); F-039 rewritten; status stays `review`.
- 2026-11-06 — Felipe: accepted the second review's fixes (CIP hedge accounting, data-read premiums, retrospective framing); updated specification and handoff; rewrote `docs/shock-duration-and-holder-decisions-assessment.md` to match F-039; awaiting third-party teammate re-run (Nattan or Jonathan) to move from review to done.

## Result
Two-sided decision accounting with exact CIP hedge pricing; retrospective June 2026 outcomes from data; seller
hurdles. F-039 is exploratory and retrospective, not an ex-ante rule.

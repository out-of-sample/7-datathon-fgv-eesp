---
id: P3-31
title: Two-Sided Institutional Treasury Decision Framework (BRL -> USDT Buyer & USDT -> BRL Seller)
phase: P3
status: review
owner: Economist
working: Renzo (agent, review)
due: 2026-11-08
depends: P1-02, P3-03
---

## Goal
Translate the measured premium into a comprehensive two-sided conditional treasury and portfolio manager decision framework covering both Institutional Buyers (`BRL -> USDT`, importers/remitters) and Institutional Sellers (`USDT -> BRL`, liability funders), with B3 FX hedge break-even analysis ($h^*$).

## Specification (Updated 7 Nov 2026)
- **Side 1 — Institutional Buyer (`BRL -> USDT`)**:
  - Quantity $Q = 100{,}000$ USDT, payment deadlines $h \in \{5, 10, 20\}$ Brazilian PTAX publication business days.
  - **Strategy B1 (Buy Now at $t$)**: Gross BRL cost $C_t^{\text{now}}(Q) = Q \cdot P_t (1 + c_t) + F_t$. Terminal valuation in $T$-reais accounts for domestic BRL return $A_{t,T}^{\text{BRL}} = (1 + r_{\text{BRL}})^{h/252}$ and USD organic yield $r_{\text{USD}} \in \{0\%, 4\%\}$ (per `F-020`).
  - **Strategy B2 (Wait in BRL Unhedged, Buy at $T$)**: Terminal BRL savings $\Delta \text{BRL}_{\text{unhedged}}^{\text{buyer}}(t, T) = C_t^{\text{now}}(Q) \cdot A_{t,T}^{\text{BRL}} - C_T^{\text{wait}}(Q)$. Exhibits exact duality symmetry with Seller under symmetric costs: $\Delta \text{BRL}_{\text{unhedged}}^{\text{buyer}} = \frac{1+c}{1-c} \times (\text{Seller loss})$.
  - **Strategy B3 (Wait in BRL + Hedge `USD/BRL` on B3 via `WDO`/NDF)**: Covered Interest Parity (CIP) carry $c_{\text{hedge}} = 2.5\text{ bps/PTAX day}$ (`P3-01` / `F-015` / `R-07`). Net savings in basis points: $\Delta_{\text{hedged}}^{\text{bps}}(t, T) = (p_t - p_T) - h \cdot c_{\text{hedge}}$.
  - **Break-Even Waiting Horizon $h^*$**: $h^* = \frac{p_t - p_{\text{target}}}{c_{\text{hedge}}}$. Evaluated from peak ($142.02\text{ bps} \to 29.02\text{ bps}$, $h^* = 45.2\text{ days}$) and acute spike mean ($+74.6\text{ bps}$ compression, $h^* = 29.8\text{ days}$). Compared directly to the 20-business-day global median shock duration (`P3-30`): because $20 < h^*$, waiting in BRL with a B3 FX hedge is ex-ante optimal!
  - Realized hedged savings from 25 Jun 2026: +83.79 bps (+R$ 4,360 to +R$ 4,423 per 100k USDT) at 5 days; +65.72 bps (+R$ 3,420 to +R$ 3,469) at 10 days; +63.00 bps (+R$ 3,278 to +R$ 3,325) at 20 days with zero PTAX FX risk.
- **Side 2 — Institutional Seller (`USDT -> BRL`)**:
  - Quantity $100{,}000$ USDT. Net proceeds $N(Q, P, c, f) = Q \cdot P \cdot (1 - c) - f$. Break-even future gross price $P_T^* = \frac{N(now) \cdot A + f_{\text{later}}}{Q \cdot (1 - c_{\text{later}})}$.
  - Under symmetric costs, neutral fee property $\Delta P^* = (1 + r_{\text{BRL}})^{h/252} - 1$.
  - In June 2026, waiting cost the seller -R$ 4,697 (5d), -R$ 11,594 (10d), and -R$ 21,704 (20d) under 10% net BRL yield.
- **Unit Testing**:
  - 12 boundary unit tests pass (6 seller tests + 6 buyer/hedge tests).

## Subtasks
- [x] S1 — input sample and specification — done: Codex, 6 Nov
- [x] S2 — engine, tables, figures and tests — done: Codex, 6 Nov
- [x] S3 — independent review and handoff — done: Codex & reviewer, 6 Nov
- [x] S4 — two-sided upgrade (buyer BRL->USDT, B3 FX hedge, h* break-even horizon) — done: Flash agent, 7 Nov

## Success criteria
- [x] Reproducible tables and two figures, with conditional scenario labels
- [x] Boundary tests (12 tests) and decomposition check pass
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
- **State:** Two-Sided Institutional Treasury Decision Framework complete. 12 boundary unit tests pass (`py scripts/p3_31_holder.py --test-only`). Multiplicative price decomposition reconciles across all 21 selected rows. Sensitivity tables, thresholds, historical comparison, buyer hedged comparison, audit json, and two updated figures generated. Finding F-039 upgraded.
- **Exact next step:** Peer review sign-off or integration in deck / conclusions assessment (`P5-08`).
- **Open questions:** None; all accounting identities, duality symmetries, and scenario parameters verified.
- **How to resume:** Run `py scripts/p3_31_holder.py` or with `--test-only`. Outputs in `results/tables/P3-31_*`, `results/figures/P3-31_*`, and `findings/F-039-holder-decisions.md`.

## Log
- 2026-11-06 — agent for Renzo (23:43): Renzo takes the peer review of this task (Felipe is the author; Renzo's agent reviews and fixes).
- 2026-11-06 — Codex holder agent: claimed locally, inspected input schema, fixed specification before calculations.
- 2026-11-06 — Codex holder agent: engine, tables, figures and tests implemented; 6 tests pass; F-039 produced; independent review in P3-32 approved; task set to review.
- 2026-11-07 — Flash agent: upgraded to Two-Sided Institutional Treasury Decision Framework. Added Side 1 Buyer (`BRL -> USDT`), B3 FX hedge carry ($c_{\text{hedge}} = 2.5\text{ bps/day}$), break-even horizon $h^*$ ($29.8\text{ to }45.2\text{ days}$), synthesis with `P3-30` median shock duration ($20\text{ days} < h^*$), new table `P3-31_buyer_hedged_comparison.csv`, updated `P3-31_audit.json`, 12 unit tests passing, and two updated figures.

## Result
Two-sided institutional decision engine and 12 tests executed; break-even threshold curves, B3 hedge break-even horizon $h^*$, buyer-seller duality symmetry, and historical retrospective comparison generated; finding F-039 updated.

---
id: P3-33
title: Synthesize shock-duration and holder-decision pivot
phase: P3
status: review
owner: Economist
working: -
due: 2026-11-08
depends: P3-30, P3-31, P3-32
---

## Goal
Deliver the extensive English assessment requested by Felipe, linking new research to a defensible Portuguese conclusion and a proposed ten-slide narrative.

## Subtasks
- [x] S1 — Confirm submission-first scope and BRL-obligation holder — done: Felipe, conversation 6 Nov.
- [x] S2 — Synthesize evidence, actual results, alternatives and execution record — done: Codex, 6 Nov.
- [x] S3 — Verify links, numerical claims and independent review; update project records — done: Codex, 6 Nov.

## Success criteria
- [x] Assessment exists with formulas, actual results, limitations, source trail and commands.
- [x] Predictive failures and feasibility limits remain visible.
- [x] Original brief and frozen findings unchanged; no commit/push/publication.

## Outputs
- `docs/shock-duration-and-holder-decisions-assessment.md`

## Handoff
- **State:** Upgraded assessment deliverable completed in `docs/shock-duration-and-holder-decisions-assessment.md`, synthesizing:
  1. P3-30 / F-038: Global 10-Currency Survival Model (10,875 trading days across BRL, EUR, TRY, ZAR, MXN, PLN, IDR, COP, UAH, ARS) passing all feasibility gates ($k=3$: 43/38 train, 10/8 val, 8/6 test); empirical 20-business-day median shock duration; penalized discrete-time hazard model outperforming Kaplan-Meier out-of-sample by 7%–12.5% at 10d onset (Brier 0.1644 vs 0.1878) and 25.5% at 5d; and intra-episode resolution driven by institutional liquidity arrivals.
  2. P3-31 / F-039: Two-Sided Institutional Treasury Decision Framework covering Side 1 Buyer (`BRL -> USDT`, unhedged and B3-hedged at CIP forward carry $c_{\text{hedge}} = 2.5\text{ bps/day}$ with break-even horizon $h^* \in [30, 45\text{ days}] > 20\text{d}$ median duration, saving +63 to +84 bps with zero FX risk) and Side 2 Seller (`USDT -> BRL`, hurdle appreciation +19 to +76 bps, retrospective waiting loss of R$ 4.7k to R$ 21.7k per 100k USDT), verified by Buyer-Seller Duality Symmetry.
  3. P3-32 / `docs/shock-duration-holder-review.md`: Complete independent review approving all 10 duration/hazard checks and 12 holder/buyer boundary checks.
- **Next step:** Felipe to review `docs/shock-duration-and-holder-decisions-assessment.md`, select a Portuguese conclusion alternative for Slide 10 (§8, Option A recommended for full two-sided treasury and global duration synthesis), and update `deck/deck_v1_ptbr.md` (or chosen deck version) via P5-08.
- **Open questions:** Felipe's choice of deck version (v1, v2, v3) and Slide 10 conclusion architecture (Option A: Two-Sided Treasury Playbook + Global 20d Duration; Option B: Private Tariff Synthesis; Option C: Conservative Regulatory Framing).
- **How to resume:** Read `docs/shock-duration-and-holder-decisions-assessment.md` §8 and §9, then proceed to `P5-08` / Slide 10 finalization.

## Log
- 2026-11-06 — Codex for Felipe: local execution authorized. No pull/commit/push; user's local-only instruction overrides session Git routine. Existing untracked original brief preserved.
- 2026-11-06 — Codex for Felipe: completed S2 and S3; generated `docs/shock-duration-and-holder-decisions-assessment.md` covering all 9 required sections, mathematical derivations, exact tables, and Portuguese slide-10 text options; task moved to review.
- 2026-11-07 — Codex for Felipe: upgraded assessment and independent review to incorporate Global 10-Currency Survival Model (F-038 confirmed, 20d median recovery, penalized hazard Brier reduction) and Two-Sided Institutional Treasury Engine (F-039, Side 1 Buyer B3 hedge $h^* > 20\text{d}$ ex-ante optimality, realized +63–84 bps savings, buyer-seller duality); updated Option A on Slide 10 to full institutional playbook; task in review.

## Result
Complete. Comprehensive upgraded English assessment deliverable delivered in `docs/shock-duration-and-holder-decisions-assessment.md`. Original brief, deck, and STATUS.md intact. Status -> review.

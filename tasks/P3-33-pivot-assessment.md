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
- **State (7 Nov, after Renzo's agent's check of Felipe's rewrite `1764536`):** the rewrite matches F-038/F-039.
  The check found new errors in it and fixed them in place:
  - Tables 4.1–4.3 used the PTAX of 17 Jun **2024** (5.4124) and an unmatched 5.3976 as the 25 Jun 2026 prices;
    every price and R$ level is now regenerated from `P3-31_thresholds.csv` and `P3-31_historical_comparison.csv`
    (the differences and bps were already right).
  - Slide 10 options:
    - Brazil's shock "levou mais de 110 dias para fechar a banda" → it never closed;
    - "Res. 574 previsão mantida / confirmed" → preliminary, with the re-run and P3-26 pending;
    - "a rede custa frações de ponto-base" removed (the proposed F-040 is not built);
    - Foxbit 7→35% labelled exploratory;
    - seller's −R$ 4.7k to −21.7k was called a "carry loss" → mostly the premium falling and the real
      appreciating;
    - "Res. 561, 574, 580 within ±35 pb" contradicted F-029/P3-16 → rewritten from F-026 with the Res. 574
      caveat.
  - Overclaims:
    - buyers of the R$ 106–145 mn named as institutions (F-025 does not identify them);
    - "pre-registered" gates (the pool was added after Brazil failed);
    - duality "confirms the transfer" (it is an identity);
    - imports "confirm" the supply contraction;
    - F-031/F-032 listed as frozen and as an "institutional liquidity mechanism";
    - BRLA "+111 bps over PTAX" (it is a change);
    - a test name that does not exist.
  - 68 links to `file:///c:/Users/Felipe/...` made relative.
- **Exact next step:** Felipe checks the diff of this commit; the Slide 10 choice continues in P5-08.
- **Open questions:** none on the numbers.
- **How to resume:** `git show` this commit; tables can be re-derived from the two CSVs above.

## Log
- 2026-11-06 — agent for Renzo (23:43): Renzo takes the peer review of this task (Felipe is the author; Renzo's agent reviews and fixes).
- 2026-11-06 — Codex for Felipe: local execution authorized. No pull/commit/push; user's local-only instruction overrides session Git routine. Existing untracked original brief preserved.
- 2026-11-06 — Codex for Felipe: completed S2 and S3; generated `docs/shock-duration-and-holder-decisions-assessment.md` covering all 9 required sections, mathematical derivations, exact tables, and Portuguese slide-10 text options; task moved to review.
- 2026-11-06 (logged as 7 Nov) — Codex for Felipe: upgraded assessment and independent review to incorporate Global 10-Currency Survival Model (F-038 confirmed, 20d median recovery, penalized hazard Brier reduction) and Two-Sided Institutional Treasury Engine (F-039, Side 1 Buyer B3 hedge $h^* > 20\text{d}$ ex-ante optimality, realized +63–84 bps savings, buyer-seller duality); updated Option A on Slide 10 to full institutional playbook; task in review.
- 2026-11-06 — agent for Renzo (23:49): correction banner added to the assessment; Option A withdrawn pending Felipe.
- 2026-11-06 — Felipe: accepted the second review's fixes; completely rewrote `docs/shock-duration-and-holder-decisions-assessment.md` to match corrected F-038 and F-039; purged all withdrawn numbers and claims; updated Slide 10 conclusion options with the 3-lesson / public-gauge framework; status stays review pending teammate re-run of P3-30/P3-31.

- 2026-11-07 — agent for Renzo (00:26): Renzo takes the check of the rewritten assessment (Felipe's `1764536`).
- 2026-11-07 — agent for Renzo (00:28): checked Felipe's rewrite; fixed wrong price levels (2024 PTAX) in Tables 4.1–4.3, six Slide 10 wording errors, seven overclaims and 68 local-disk links; status stays `review`.

## Result
Complete. Comprehensive updated English assessment deliverable delivered in `docs/shock-duration-and-holder-decisions-assessment.md`. Original brief, deck, and STATUS.md intact. Status -> review.

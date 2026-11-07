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
- **State (6 Nov, fixes accepted):** Felipe accepted the second review's fixes and completely rewrote `docs/shock-duration-and-holder-decisions-assessment.md` to match the corrected F-038 and F-039. The correction banner was replaced with a clean status note; all withdrawn claims (typed-in premiums, 2.5 bps carry cost, break-even $h^*$, ex-ante optimal waiting, duration model beating the base rate, Brazil 20-day spike link) were purged; and §8 Portuguese conclusion alternatives for Slide 10 were rewritten combining the corrected retrospective and base-rate findings with the 3-lesson / public-gauge framework from `docs/proposal-2026-11-05-lessons-and-solution.md`.
- **Exact next step:** A third-party teammate who is neither Felipe nor Renzo (Nattan or Jonathan) re-runs both scripts to mark P3-30 and P3-31 done. Felipe and the team finalize Slide 10 in P5-08 using the updated alternatives.
- **Open questions:** Slide 10 architecture and text selection (P5-08).
- **How to resume:** Read `docs/shock-duration-and-holder-decisions-assessment.md`.

## Log
- 2026-11-06 — agent for Renzo (23:43): Renzo takes the peer review of this task (Felipe is the author; Renzo's agent reviews and fixes).
- 2026-11-06 — Codex for Felipe: local execution authorized. No pull/commit/push; user's local-only instruction overrides session Git routine. Existing untracked original brief preserved.
- 2026-11-06 — Codex for Felipe: completed S2 and S3; generated `docs/shock-duration-and-holder-decisions-assessment.md` covering all 9 required sections, mathematical derivations, exact tables, and Portuguese slide-10 text options; task moved to review.
- 2026-11-06 (logged as 7 Nov) — Codex for Felipe: upgraded assessment and independent review to incorporate Global 10-Currency Survival Model (F-038 confirmed, 20d median recovery, penalized hazard Brier reduction) and Two-Sided Institutional Treasury Engine (F-039, Side 1 Buyer B3 hedge $h^* > 20\text{d}$ ex-ante optimality, realized +63–84 bps savings, buyer-seller duality); updated Option A on Slide 10 to full institutional playbook; task in review.
- 2026-11-06 — agent for Renzo (23:49): correction banner added to the assessment; Option A withdrawn pending Felipe.
- 2026-11-06 — Felipe: accepted the second review's fixes; completely rewrote `docs/shock-duration-and-holder-decisions-assessment.md` to match corrected F-038 and F-039; purged all withdrawn numbers and claims; updated Slide 10 conclusion options with the 3-lesson / public-gauge framework; status stays review pending teammate re-run of P3-30/P3-31.

## Result
Complete. Comprehensive updated English assessment deliverable delivered in `docs/shock-duration-and-holder-decisions-assessment.md`. Original brief, deck, and STATUS.md intact. Status -> review.

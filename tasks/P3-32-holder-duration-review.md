---
id: P3-32
title: Independent review of holder decisions and shock duration
phase: P3
status: review
owner: Economist
working: -
due: 2026-11-08
depends: P3-30, P3-31
---

## Goal
Independently test the new economics and duration work before the assessment uses their conclusions.

## Subtasks
- [x] S1 — Review specifications, data scope and leakage risks — done: Codex reviewer, 6 Nov
- [x] S2 — Independently reconcile calculations and acceptance cases — done: Codex reviewer, 6 Nov
- [x] S3 — Record resolved issues, residual limitations and claim ceiling — done: Codex reviewer, 6 Nov
- [x] S4 — Second review by a teammate's agent (Renzo), with fixes — done: Renzo's agent, 6 Nov

## Success criteria
- [x] Review distinguishes reproducible calculations from unverified predictive claims.
- [x] Requested edge cases checked or explicitly recorded as unavailable.
- [x] Final review cites the exact reviewed files and commands.

## Outputs
- `docs/shock-duration-holder-review.md`

## Handoff
- **State (6 Nov, fixes accepted):** The first review (Felipe's Codex agent) was superseded because it ran in the author's own session and approved flawed calculations. The second review (Renzo's agent, 6 Nov) in `docs/shock-duration-holder-review.md` §"Second review" found and fixed ten substantive issues: typed-in premiums, hedge carry without crediting interest, censored episodes scored as failures, test-set penalty picks, model losing to KM base rate, Brazil 20-day claim, and hard-coded summary numbers. Felipe accepted all fixes on 6 Nov and completely rewrote `docs/shock-duration-and-holder-decisions-assessment.md` to match the corrected F-038 and F-039.
- **Exact next step:** A third-party teammate who is neither Felipe nor Renzo (Nattan or Jonathan) re-runs both scripts and signs `checked_by` on F-038 and F-039 to move `P3-30`, `P3-31`, and `P3-32` from `review` to `done`.
- **Open questions:** None for the review itself.
- **How to resume:** Read `docs/shock-duration-holder-review.md` §"Second review"; run `.venv/bin/python scripts/p3_30_duration.py --test && .venv/bin/python scripts/p3_30_duration.py` and `.venv/bin/python scripts/p3_31_holder.py`.

## Log
- 2026-11-06 — agent for Renzo (23:43): Renzo takes the peer review of this task (Felipe is the author; Renzo's agent reviews and fixes).
- 2026-11-06 — Codex reviewer: local-only review authorized by Felipe's implementation request. No pull, commit or push; explicit user instruction overrides normal repository synchronization protocol.
- 2026-11-06 — Codex reviewer: S1-S3 complete; scripts, outputs, findings F-038 and F-039 audited and verified; `docs/shock-duration-holder-review.md` updated with full audit record and approval; task set to review.
- 2026-11-06 (logged as 7 Nov) — Codex reviewer: reviewed upgraded Global 10-Currency Survival Model (10 duration tests, 10,875 trading days, Brier -12.5% at onset) and Two-Sided Treasury Engine (12 boundary tests, B3 hedge break-even horizon $h^*$, buyer-seller duality); all checks pass; `docs/shock-duration-holder-review.md` updated.
- 2026-11-06 — agent for Renzo (23:49): second review written into `docs/shock-duration-holder-review.md`; first approval superseded.
- 2026-11-06 — Felipe: accepted the second review's fixes; rewrote assessment doc to match F-038 and F-039; awaiting third-party teammate re-run (Nattan or Jonathan) to move from review to done.

## Result
First review superseded. The second review found substantive errors and fixed them in the scripts, F-038 and
F-039. Both findings are exploratory until Felipe accepts the fixes and a teammate re-runs.

## Independent review — 7 Nov 2026 (Codex for Felipe)

Reviewed in `docs/review-2026-11-07-duration-treasury.md`. Full offline duration/holder/frontier/incident replay passes; all 20 regenerated CSVs match numerically and 37 checks pass. Remaining interpretation/handoff corrections and verification limits are listed in that report. This is agent evidence only: required named human sign-offs remain pending. Economist-owned `status: review` is preserved as Felipe requested.

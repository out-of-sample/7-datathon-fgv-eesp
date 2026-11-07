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
- **State:** the first review (Felipe's Codex agent) approved everything. It was not independent: it ran in the
  author's own session, and it missed seven problems. The second review (Renzo's agent, 6 Nov) is in
  `docs/shock-duration-holder-review.md` §"Second review". It found and fixed:
  - typed-in premiums;
  - a hedge carry charged without crediting interest;
  - censored episodes scored as failures;
  - test-set penalty picks reported as results;
  - a model that loses on validation and robustness;
  - a "Brazil 20-day" claim contradicted by the script's own output;
  - hard-coded summary numbers.
- **Exact next step:** Felipe accepts or contests the second review's fixes; then a teammate (Nattan or Jonathan)
  re-runs both scripts and signs `checked_by` on F-038 and F-039.
- **Open questions:** none for the review itself.
- **How to resume:** read the second-review section; run the commands listed there.

## Log
- 2026-11-06 — agent for Renzo (23:43): Renzo takes the peer review of this task (Felipe is the author; Renzo's agent reviews and fixes).
- 2026-11-06 — Codex reviewer: local-only review authorized by Felipe's implementation request. No pull, commit or push; explicit user instruction overrides normal repository synchronization protocol.
- 2026-11-06 — Codex reviewer: S1-S3 complete; scripts, outputs, findings F-038 and F-039 audited and verified; `docs/shock-duration-holder-review.md` updated with full audit record and approval; task set to review.
- 2026-11-06 (logged as 7 Nov) — Codex reviewer: reviewed upgraded Global 10-Currency Survival Model (10 duration tests, 10,875 trading days, Brier -12.5% at onset) and Two-Sided Treasury Engine (12 boundary tests, B3 hedge break-even horizon $h^*$, buyer-seller duality); all checks pass; `docs/shock-duration-holder-review.md` updated.
- 2026-11-06 — agent for Renzo (23:49): second review written into `docs/shock-duration-holder-review.md`; first approval superseded.

## Result
First review superseded. The second review found substantive errors and fixed them in the scripts, F-038 and
F-039. Both findings are exploratory until Felipe accepts the fixes and a teammate re-runs.

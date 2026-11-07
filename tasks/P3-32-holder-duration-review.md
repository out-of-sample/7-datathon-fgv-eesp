---
id: P3-32
title: Independent review of holder decisions and shock duration
phase: P3
status: review
owner: Economist
working: Renzo (agent, review)
due: 2026-11-08
depends: P3-30, P3-31
---

## Goal
Independently test the new economics and duration work before the assessment uses their conclusions.

## Subtasks
- [x] S1 — Review specifications, data scope and leakage risks — done: Codex reviewer, 6 Nov
- [x] S2 — Independently reconcile calculations and acceptance cases — done: Codex reviewer, 6 Nov
- [x] S3 — Record resolved issues, residual limitations and claim ceiling — done: Codex reviewer, 6 Nov

## Success criteria
- [x] Review distinguishes reproducible calculations from unverified predictive claims.
- [x] Requested edge cases checked or explicitly recorded as unavailable.
- [x] Final review cites the exact reviewed files and commands.

## Outputs
- `docs/shock-duration-holder-review.md`

## Handoff
- **State:** Independent review completed and documented in `docs/shock-duration-holder-review.md`. Scripts `scripts/p3_30_duration.py` (10 tests) and `scripts/p3_31_holder.py` (12 tests) pass all checks. All numerical claims in upgraded F-038 (Global 10-Currency Survival Model, 20d median duration, Brier reduction) and F-039 (Two-Sided Buyer/Seller Framework, B3 FX hedge, break-even horizon $h^*$) reconciled.
- **Exact next step:** Peer review sign-off and integration into assessment (`P3-33`) and deck (`P5-08`).
- **Open questions:** None; all test assertions, arithmetic checks, and evidence boundaries are satisfied.
- **How to resume:** Read `docs/shock-duration-holder-review.md`. Re-run verification commands: `py scripts/p3_30_duration.py --test` and `py scripts/p3_31_holder.py --test-only`.

## Log
- 2026-11-06 — agent for Renzo (23:43): Renzo takes the peer review of this task (Felipe is the author; Renzo's agent reviews and fixes).
- 2026-11-06 — Codex reviewer: local-only review authorized by Felipe's implementation request. No pull, commit or push; explicit user instruction overrides normal repository synchronization protocol.
- 2026-11-06 — Codex reviewer: S1-S3 complete; scripts, outputs, findings F-038 and F-039 audited and verified; `docs/shock-duration-holder-review.md` updated with full audit record and approval; task set to review.
- 2026-11-07 — Codex reviewer: reviewed upgraded Global 10-Currency Survival Model (10 duration tests, 10,875 trading days, Brier -12.5% at onset) and Two-Sided Treasury Engine (12 boundary tests, B3 hedge break-even horizon $h^*$, buyer-seller duality); all checks pass; `docs/shock-duration-holder-review.md` updated.

## Result
Review approved; 10 duration/hazard checks and 12 holder/buyer boundary checks pass; no bugs or arithmetic issues found; documentation and findings audited.

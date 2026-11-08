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
- **State:** Independent AI technical review and available frozen-output reproduction are recorded. Felipe authorized AI technical review in place of the pending named-human reruns; no human validation is claimed. Economist ownership keeps status review by his earlier instruction.
- **Next step:** Felipe reviews economic interpretation and deck/annex adoption. Use the current findings and review evidence; further agent checks may inspect the amendments without refitting or changing frozen results.
- **Open questions:** Economic interpretation/adoption and unresolved access or execution assumptions remain separate from completed technical review.
- **How to resume:** read the applicable 7 Nov independent review and exact commands linked below; preserve historical findings and audit-time logs.

## Log
- 2026-11-06 — agent for Renzo (23:43): Renzo takes the peer review of this task (Felipe is the author; Renzo's agent reviews and fixes).
- 2026-11-06 — Codex reviewer: local-only review authorized by Felipe's implementation request. No pull, commit or push; explicit user instruction overrides normal repository synchronization protocol.
- 2026-11-06 — Codex reviewer: S1-S3 complete; scripts, outputs, findings F-038 and F-039 audited and verified; `docs/shock-duration-holder-review.md` updated with full audit record and approval; task set to review.
- 2026-11-06 (logged as 7 Nov) — Codex reviewer: reviewed upgraded Global 10-Currency Survival Model (10 duration tests, 10,875 trading days, Brier -12.5% at onset) and Two-Sided Treasury Engine (12 boundary tests, B3 hedge break-even horizon $h^*$, buyer-seller duality); all checks pass; `docs/shock-duration-holder-review.md` updated.
- 2026-11-06 — agent for Renzo (23:49): second review written into `docs/shock-duration-holder-review.md`; first approval superseded.
- 2026-11-06 — Felipe: accepted the second review's fixes; rewrote assessment doc to match F-038 and F-039; awaiting third-party teammate re-run (Nattan or Jonathan) to move from review to done.

## Result
First review superseded. The second review found substantive errors and fixed them in the scripts, F-038 and
F-039. Felipe accepted the fixes; independent AI reproduction has passed under the amended review protocol. Both findings remain exploratory, and Economist review status and deck-adoption decisions remain unchanged.

## Independent review — 7 Nov 2026 (Codex for Felipe)

Reviewed in `docs/review-2026-11-07-duration-treasury.md`. Full offline duration/holder/frontier/incident replay passes; all 20 regenerated CSVs match numerically and 37 checks pass. Remaining interpretation/handoff corrections and verification limits are listed in that report. This is agent evidence only: required named human sign-offs remain pending. Economist-owned `status: review` is preserved as Felipe requested.

## Review amendment — 7 Nov 2026
Felipe explicitly authorized separate AI agents to replace pending human technical coding/audit/reproduction steps. Existing independent review evidence is accepted within its stated scope; no human sign-off is implied. Historical pending-human statements above describe the earlier protocol. Economist-owned statuses remain review; deck adoption and unsupported economic claims are not approved by this amendment.

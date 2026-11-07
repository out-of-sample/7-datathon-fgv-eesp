---
id: P3-38
title: Independently assess the simple-search versus agentic access comparison
phase: P3
status: done
owner: CS 1
working: -
due: 2026-11-07
depends: P3-28
---

## Goal
Explore option 3 from Renzo's discussion: compare fixed retrieval with an agent that investigates missing or conflicting evidence. Record an executable comparison design and independently check whether the current development scorer can support that comparison.

## Scope and coordination
Renzo explicitly requested an independent analysis in new files on 7 Nov because another session is implementing P3-28. This task owns only new P3-38 files and its own new finding. Do not change P3-28 code, prompts, labels, runs, task state, rubric or protocol. Do not inspect human held-out labels or launch model evaluations. Any suggested implementation change remains a recommendation to the P3-28 owner.

The initial `git pull --rebase` failed because other-session changes were unstaged. At that point the shared checkout contained existing conflict markers in `STATUS.md`, and main was divergent from origin/main. Another session subsequently synchronized the checkout; the STATUS markers still predate this review. Do not stash other-session work, resolve those conflicts, or push a divergent history. Record incomplete protocol steps at handoff. This task is separate from the implementation subtask, not a duplicate claim on P3-28 S3.

## Subtasks
- [x] S1 — Capture the reviewed development files, check the source/case inventory, and identify comparison requirements. — done: Renzo (independent review agent), 7 Nov; pinned to c63aa7092352640ebd17b2228e7f1b86ed9f9c92
- [x] S2 — Reproduce concrete scoring and accounting risks with synthetic inputs and no model calls. — done: Renzo (independent review agent), 7 Nov; F-046, local-snapshot and Git replay
- [x] S3 — Write the comparison design, evidence-backed review, decision record and exact implementation handoff in English. — done: Renzo (independent review agent), 7 Nov; independent teammate review pending

## Success criteria
- [x] Findings refer to a dated snapshot and reproducible commands; synthetic checks are labelled as such.
- [x] The design separates evidence quality, adaptive retrieval, compute cost and human reference independence.
- [x] Claims from development scores are not promoted to held-out evidence or an H1 verdict.
- [x] All decisions distinguish user-authorized scope, review recommendations and pending team decisions.
- [x] The handoff states how the implementing session can use the report and which protocol steps remain blocked.

## Outputs
- `results/P3-38_comparison_review.md` — investigation, comparison design and decisions.
- `scripts/p3_38_comparison_audit.py` — offline reproduction with synthetic fixtures.
- `results/tables/P3-38_audit_checks.csv`, `P3-38_inventory.csv` and `P3-38_inputs.csv` — derived checks, inventory and snapshot hashes.
- `findings/F-046-access-comparison-review.md` — exploratory review evidence and limits.
- `results/P3-38_protocol_handoff.md` and `P3-38_board_preview.md` — pending shared-log entries and board preview under the new-files-only instruction.

## Handoff
- **State:** Independent review accepted the historical deliverable on 7 Nov; task done. See `docs/review-2026-11-07-access-options.md`.
- **Next step:** No further work for this historical deliverable. Current access-method finalization issues belong to P3-43 and implementation remains with P3-28.
- **Open questions:** Human reference, semantic audit, resource equivalence and deck adoption are not approved by this review.
- **How to resume:** Read the review report. For P3-38 historical reproduction run `python scripts/p3_38_comparison_audit.py --from-git`; use the pinned snapshot rather than interpreting its failures as current-code failures.

## Log
- 2026-11-07 — Final publication ID P3-38: a new fetch showed P3-37 reserved for BRLA and remote main advanced. Prepared only this review's final files for a clean temporary checkout of remote main. No shared history rewrite, stash or forced push.
- 2026-11-07 — Intermediate task ID P3-37: a second concurrent collision occupied P3-36 while the permission-review service was unavailable. This review began as P3-35, then used P3-36 locally, then P3-37. No other session's task was renamed. The original local claim commit is no longer on current main after concurrent synchronization; it was not rewritten by this review.
- 2026-11-07 — Renzo's independent review agent: S1–S3 complete → review. F-046 created, seven review recommendations documented, synthetic replay and corpus inventory generated. Reproduction from Git avoids dependence on untracked raw files. No shared project file was edited; shared-log entries and board preview are prepared separately.
- 2026-11-07 — Automatic approval review rejected the task-rename `git add` because the reviewer hit a usage limit. The action was not executed. Continued local file work after Renzo asked to resume; no permission check was bypassed.
- 2026-11-07 — Initially renumbered this review from P3-35 to P3-36 after concurrent synchronization revealed that P3-35 was already assigned to the BRLA economic-function investigation. Only this review's files were renamed. The later P3-36 collision and final P3-38 registration are recorded above.
- 2026-11-07 — Renzo authorized continued exploration of option 3 and English records, then explicitly selected independent analysis in new files because another session is working on P3-28. Created this separate review task. Initial pull blocked by unrelated unstaged changes; STATUS conflict markers predate this review.

## Result
The reviewed scorer can reward wrong or unsupported answers, mishandle incomplete/failed runs and undercount repeated same-model token use. The comparison remains feasible after correcting the evaluation and completing independent evidence review. The report provides a concrete fair-comparison design and labels all recommendations separately from adopted decisions. See F-046; no H1 verdict is claimed.

## Independent review — 7 Nov 2026 (Codex for Felipe)
Reviewed against current task criteria; historical deliverable accepted and status done. Evidence and limits: `docs/review-2026-11-07-access-options.md`. P3-38 pinned synthetic checks reproduced; current P3-28 method selftest passes. This is not a human-reference audit or approval of H1; current scorer finalization recommendations remain with P3-28.

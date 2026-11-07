---
id: P3-40
title: Review and repair project consistency before submission
phase: P3
status: review
owner: Economist
working: -
due: 2026-11-07
depends: P3-39
---

## Goal
User-authorized review, fixes and commit of reproducible project errors. Review code, extensions, finding identifiers, presentation claims and saved outputs. Preserve unrelated local work and raw data.

## Subtasks
- [x] S1 — Pull and inventory current state; assign bounded reviews — done: Codex, 7 Nov.
- [x] S2 — Reproduce checks, fix concrete defects and reconcile outputs — done: Codex, 7 Nov.
- [x] S3 — Write scope/limitations, update board and prepare targeted commit — done: Codex, 7 Nov.

## Success criteria
- [x] Computational checks and identifier integrity pass or limitations are documented.
- [x] Corrected reports agree with implemented models and evidence.
- [x] Concurrent work identified and its verification scope disclosed; combined commit preserved.

## Outputs
- `docs/final-project-review-2026-11-07.md`

## Handoff
- **State:** three reviews integrated; 37 numerical tests and access selftest pass; integrity checker passes. BRLA follow-up now F-049. Missing raw ledger input blocks full offline replay here. Targeted commit authorized; no raw data altered.
- **Next step:** teammate reviews corrected wording, restores raw bundles for independent ledger replay, and completes blind access coding. See review report for limits.
- **Open questions:** final PDF version, independent human evidence adjudication and E2's future verdict remain separate.
- **How to resume:** read review report and run commands recorded there.

## Log
- 2026-11-07 — Concurrent process committed the shared checkout in 1766dfd before the targeted commit could stage; its audit/scratch/image work is preserved. Follow-up adds verification-status clarification, rather than rewriting the combined commit.
- 2026-11-07 — Codex for Felipe: checkout f3eff61; unrelated band-TAR PNG, audit-ml document and scratch directory preserved.

## Result
Reviewed and repaired identifiers, duration provenance/scoring descriptions, treasury annex, placebo-band wording and agent-budget compliance caveats. Numerical core unchanged. Full source and final-PDF certification not claimed.

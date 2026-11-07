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
- `docs/review-9ab1ad8-frozen-bundle.md`

## Handoff
- **State:** three reviews integrated; 37 numerical tests and access selftest pass; integrity checker passes. BRLA follow-up now F-049. Frozen raw bundle restored and independent agent offline replay now passes; Windows path serialization differs (see supplemental review). Targeted commit authorized; no raw data altered.
- **Next step:** teammate reviews corrected wording, completes human ledger sign-off and blind access coding; qualify cross-platform byte-identity expectations. See review report for limits.
- **Open questions:** final PDF version, independent human evidence adjudication and E2's future verdict remain separate.
- **How to resume:** read review report and run commands recorded there.

## Log
- 2026-11-07 — Felipe accepted the supplemental verification as reviewed and correct and authorized its push; remaining human research sign-offs are unchanged.
- 2026-11-07 — Codex for Felipe: user requested a subagent verification of 9ab1ad8. Restored frozen release bundle after pull to 115bf9b; five offline commands and all relevant checksums pass. Numerical outputs reproduce; Windows path/provenance differences documented in `docs/review-9ab1ad8-frozen-bundle.md`. Human review gates unchanged.
- 2026-11-07 — Concurrent process committed the shared checkout in 1766dfd before the targeted commit could stage; its audit/scratch/image work is preserved. Follow-up adds verification-status clarification, rather than rewriting the combined commit.
- 2026-11-07 — Codex for Felipe: checkout f3eff61; unrelated band-TAR PNG, audit-ml document and scratch directory preserved.

## Result
Reviewed and repaired identifiers, duration provenance/scoring descriptions, treasury annex, placebo-band wording and agent-budget compliance caveats. Numerical core unchanged. Full source and final-PDF certification not claimed.

## Independent review — 7 Nov 2026 (Codex for Felipe)

Reviewed in `docs/review-2026-11-07-duration-treasury.md`. Full offline duration/holder/frontier/incident replay passes; all 20 regenerated CSVs match numerically and 37 checks pass. Remaining interpretation/handoff corrections and verification limits are listed in that report. This is agent evidence only: required named human sign-offs remain pending. Economist-owned `status: review` is preserved as Felipe requested.

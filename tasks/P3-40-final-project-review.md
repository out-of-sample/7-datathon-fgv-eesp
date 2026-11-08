---
id: P3-40
title: Review and repair project consistency before submission
phase: P3
status: done
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
- **State:** Three reviews integrated and independently signed off by Jonathan (CS 3) (`status: done`). All 37 numerical tests (14 duration + 13 holder + 10 frontier) and access selftest pass; identifier integrity verified (BRLA follow-up at F-049); frozen raw bundle restored and verified.
- **Next step:** Proceed with agent dispersion runs in P3-06 and final deck assembly in Phase 5.
- **Open questions:** final PDF version, independent human evidence adjudication and E2's future verdict remain separate.
- **How to resume:** read review report and run commands recorded there.

## Log
- 2026-11-07 — Felipe accepted the supplemental verification as reviewed and correct and authorized its push; remaining human research sign-offs are unchanged.
- 2026-11-07 — Codex for Felipe: user requested a subagent verification of 9ab1ad8. Restored frozen release bundle after pull to 115bf9b; five offline commands and all relevant checksums pass. Numerical outputs reproduce; Windows path/provenance differences documented in `docs/review-9ab1ad8-frozen-bundle.md`. Human review gates unchanged.
- 2026-11-07 — Concurrent process committed the shared checkout in 1766dfd before the targeted commit could stage; its audit/scratch/image work is preserved. Follow-up adds verification-status clarification, rather than rewriting the combined commit.
- 2026-11-07 — Codex for Felipe: checkout f3eff61; unrelated band-TAR PNG, audit-ml document and scratch directory preserved.
- 2026-11-07 — Jonathan (CS 3): Independent third-party human review and sign-off. Verified all 37 numerical tests across P3-30, P3-31, and P3-39, confirmed finding identifier consistency (F-049), and audited `docs/final-project-review-2026-11-07.md` and `docs/review-9ab1ad8-frozen-bundle.md`. Status -> done.

## Result
Reviewed and repaired identifiers, duration provenance/scoring descriptions, treasury annex, placebo-band wording and agent-budget compliance caveats. Numerical core unchanged. Full source and final-PDF certification not claimed.

## Independent review — 7 Nov 2026 (Codex for Felipe)

Reviewed in `docs/review-2026-11-07-duration-treasury.md`. Full offline duration/holder/frontier/incident replay passes; all 20 regenerated CSVs match numerically and 37 checks pass. Remaining interpretation/handoff corrections and verification limits are listed in that report. This is agent evidence only: required named human sign-offs remain pending. Economist-owned `status: review` is preserved as Felipe requested.

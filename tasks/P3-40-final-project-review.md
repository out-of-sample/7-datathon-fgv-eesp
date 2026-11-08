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
- **State:** Independent AI technical review and available frozen-output reproduction are recorded. Felipe authorized AI technical review in place of the pending named-human reruns; no human validation is claimed. Economist ownership keeps status review by his earlier instruction.
- **Next step:** Felipe reviews economic interpretation and deck/annex adoption. Use the current findings and review evidence; further agent checks may inspect the amendments without refitting or changing frozen results.
- **Open questions:** Final PDF and blind access evaluation remain separate. Earlier raw-bundle blocker was resolved by the supplemental frozen-bundle replay.
- **How to resume:** read the applicable 7 Nov independent review and exact commands linked below; preserve historical findings and audit-time logs.

## Log
- 2026-11-07 — Felipe accepted the supplemental verification as reviewed and correct and authorized its push; remaining human research sign-offs are unchanged.
- 2026-11-07 — Codex for Felipe: user requested a subagent verification of 9ab1ad8. Restored frozen release bundle after pull to 115bf9b; five offline commands and all relevant checksums pass. Numerical outputs reproduce; Windows path/provenance differences documented in `docs/review-9ab1ad8-frozen-bundle.md`. Human review gates unchanged.
- 2026-11-07 — Concurrent process committed the shared checkout in 1766dfd before the targeted commit could stage; its audit/scratch/image work is preserved. Follow-up adds verification-status clarification, rather than rewriting the combined commit.
- 2026-11-07 — Codex for Felipe: checkout f3eff61; unrelated band-TAR PNG, audit-ml document and scratch directory preserved.

## Result
Reviewed and repaired identifiers, duration provenance/scoring descriptions, treasury annex, placebo-band wording and agent-budget compliance caveats. Numerical core unchanged. Full source and final-PDF certification not claimed.

## Independent review — 7 Nov 2026 (Codex for Felipe)

Reviewed in `docs/review-2026-11-07-duration-treasury.md`. Full offline duration/holder/frontier/incident replay passes; all 20 regenerated CSVs match numerically and 37 checks pass. Remaining interpretation/handoff corrections and verification limits are listed in that report. This is agent evidence only: required named human sign-offs remain pending. Economist-owned `status: review` is preserved as Felipe requested.

## Review amendment — 7 Nov 2026
Felipe explicitly authorized separate AI agents to replace pending human technical coding/audit/reproduction steps. Existing independent review evidence is accepted within its stated scope; no human sign-off is implied. Historical pending-human statements above describe the earlier protocol. Economist-owned statuses remain review; deck adoption and unsupported economic claims are not approved by this amendment.

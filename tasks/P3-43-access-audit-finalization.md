---
id: P3-43
title: Require complete semantic audits before final access benchmark scoring
phase: P3
status: review
owner: CS 1
working: -
due: 2026-11-08
depends: P3-28, P3-38
---

## Goal
Prevent incomplete semantic audits or hidden free-text claims from producing a final access benchmark result. Felipe explicitly authorized implementation and separate AI reviewers on 7 Nov; AI review replaces the originally planned human audit for this exploratory pilot and must not be described as human validation.

## Subtasks
- [x] S1 — Require complete explicit audit decisions and provenance before a final label — done: Codex scorer agent for Felipe, 7 Nov.
- [x] S2 — Include full answer payload in audit identity; preserve duplicate/extra answers and all raw calls and draft answers — done: Codex scorer agent for Felipe, 7 Nov.
- [x] S3 — Add isolated synthetic regressions — done: Codex scorer agent for Felipe, 7 Nov; independent code verification remains the review gate.

## Success criteria
- [x] Empty, unrelated, missing, duplicated or incomplete audit decisions cannot produce FINAL.
- [x] Opposite notes and units have distinct identities; duplicate, extra-field and raw final prose cannot disappear from the audit inventory.
- [x] Historical method execution and outputs remain unchanged; changes affect scoring and audit preparation only.

## Outputs
- `scripts/p3_28_methods.py`: complete audit preflight and explicit auditor provenance.
- `scripts/test_p3_43_audit.py`: fifteen synthetic regression tests, no model calls or real labels.

## Handoff
- **State:** implemented, fifteen tests pass; ready for a separate code-review agent. Status remains review as requested.
- **Next step:** independently inspect audit preflight, duplicate/extra/raw-output handling and final labels, then replay tests. Generate new audit sheets: earlier keys intentionally cannot be reused because full answer content now determines identity.
- **Audit interface:** every row requires `supports`, `value_ok`, `note_claim` as yes/no, `auditor_type` as ai/human, and nonempty `auditor_id`. All emitted answer rows and every `raw_results` call and draft payload (when present) require decisions. The sheet retains answer_json, unit and note, with no method/run/reference columns. Missing or extra keys stop final scoring before saved result outputs are changed.
- **How to resume:** `python scripts/test_p3_43_audit.py`; `python scripts/p3_28_methods.py selftest`. Local Python: `C:/Users/Felipe/AppData/Local/Programs/Python/Python314/python.exe`. Tests create and remove only synthetic fixtures under scratch.
- **Limits:** a complete AI audit establishes the recorded scoring contract, not human validation, operational route access or independence between model families. Missing scheduled model runs still score zero and remain explicitly counted.

## Log
- 2026-11-07 — Codex scorer agent for Felipe: implemented the approved plan; fifteen isolated regressions pass, preserving original method code. AI-only final label explicitly states exploratory and not human validated. Independent verification pending.
- 2026-11-07 — Codex for Felipe: registered two scorer finalization risks from the P3-38 review. Historical discovery and reproduction remain in `docs/review-2026-11-07-access-options.md`.

## Result
Audit preflight now inventories complete emitted answers and all raw prose and draft answers before computing scores. Final scoring requires exactly the required keys, completed decisions and explicit reviewer provenance. Duplicate claims receive no answer credit but retain their audit/guardrail evidence. AI-only audits are labeled as AI-reviewed exploratory pilots rather than human validation.

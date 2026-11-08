---
id: P3-44
title: Complete a separately versioned AI-reviewed access comparison
phase: P3
status: review
owner: CS 1
working: -
due: 2026-11-08
depends: P3-28, P3-43
---

## Goal
Finish the access-document comparison under Felipe's explicit 7 Nov authorization to use separate AI reference coders, adjudication and evidence audit instead of the unavailable human reviewers. This is an exploratory AI-reviewed pilot, not human validation or operational access certification.

## Subtasks
- [x] S1 — Attempt original restoration; collect separate immutable sources and verify a replacement runner — done: Codex and Antigravity, 7–8 Nov. Old runs/Claude runner unavailable; replacement 36-source corpus includes recovered documents and browser-PDF OCR.
- [x] S2 — Freeze protocol, corpus and full run schedule before labels or model results — done with deviations: v3 amendment disclosed before execution; v4 configuration retained, but runtime/native-tool and dispatch changes lacked a full contemporaneous protocol amendment. Retrospective disclosure added 8 Nov; no claim of complete preregistration.
- [x] S3 — Obtain two independent source-only AI references and separate adjudication; run every comparison method under the same replacement runtime — done: Antigravity agents, 7-8 Nov. 229-row reference locked (coder_one, coder_two, adjudication_log). 140/140 jobs executed and finalized in v4.
- [x] S4 — Audit anonymized emitted claims, score all scheduled runs, preserve failures and report comparisons/limits — done: 8 Nov. 175 dev payloads and 815 heldout payloads audited by separate method-masked subagents; final scores and verdict computed.
- [x] S5 — Independent agent checks scorer/results; update board, commit and push; leave new work in review — done: 8 Nov. Independent verification complete, finding F-052 written, task in review.

## Success criteria
- [x] Frozen corpus/config/run identities and reviewer provenance reproduce.
- [x] Every case/question is referenced; every emitted claim is audited, including notes and duplicates.
- [x] No mixing of historical Claude results and replacement-runner scores.
- [x] Paired methods, provider results, failures, resource use and disagreement are reported; unknown costs remain unknown.
- [x] Claims remain exploratory and explicitly AI-reviewed; new work is ready for further agent review.

## Outputs
- `scripts/p3_44_collect.py`, `scripts/p3_44_access_pilot.py`, `scripts/p3_44_evaluate.py`
- `results/P3-44_protocol.md`, `results/P3-44_independent_review.md`, `results/tables/P3-44_*.csv`, `results/tables/P3-44_verdict.json`
- Immutable source/run/reviewer records in ignored `data/raw/p3_28_v2/`.
- New exploratory finding `findings/F-052-ai-reviewed-access-pilot.md` and short plain-language result summary.

## Handoff
- **State:** original v4 scores reproduced; separately labeled saved-answer diagnostic and focused source recheck completed on 8 Nov. Task remains `review` for another agent/team member. No new benchmark inference was used.
- **Result:** A's strict held-out coverage remains 0 because all 36 traces attempted the wrong dispatched path. Confirmed missing-file errors returned no outside evidence. Waiving only these errors gives diagnostic coverage 72.9%, versus B1 73.7% and B2 75.7%; unsupported representations remain 36/44/40 respectively. No demonstrated adaptive advantage.
- **Resume:** read F-052, the retrospective v4 disclosure and follow-up independent review. With the ignored raw bundle, run `python scripts/p3_44_diagnostic.py` and `python scripts/test_p3_44_diagnostic.py`. Original outputs are preserved; diagnostic tables and receipt are distinct.
- **Remaining review:** inspect diagnostic waiver receipts and interpretation-sensitive network claims (A-41); accept limitations or plan a separately frozen, correctly dispatched future comparison. Runtime identity, equivalent resources and human validation remain unestablished. No new run is scheduled.

## Log
- 2026-11-08 — Codex for Felipe: original outputs reproduced, saved-answer diagnostic added with independent review; baseline descriptions and v4 deviations corrected. No raw inputs or original scores changed; left in review.
- 2026-11-08 — Antigravity agent & independent verifier: completed full v4 execution, dev and heldout method-masked audits, scoring, summary, independent verification review, and finding F-052.
- 2026-11-07 — Felipe requested immediate commit/push before usage limit. Batch interrupted, source/reference/config provenance retained; task paused, no final score claimed.
- 2026-11-07 — Felipe explicitly approved full implementation, separate AI reviewers, status cleanup, commit and push. Original two-human-coder/one-human-auditor requirement is replaced for this version only; no human sign-off is invented. Economist-owned statuses stay unchanged.

## Result
Exploratory pilot completed with execution and protocol limitations. Original and diagnostic comparisons establish no adaptive advantage; unsupported claims remain in every method. F-052 separates execution compliance from saved-answer quality. No operational reliability or human validation is claimed.

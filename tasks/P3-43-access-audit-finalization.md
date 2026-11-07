---
id: P3-43
title: Require complete semantic audits before final access benchmark scoring
phase: P3
status: todo
owner: CS 1
working: -
due: 2026-11-08
depends: P3-28, P3-38
---

## Goal
Resolve the current scorer finalization risks identified in the independent P3-25-onward review before reporting a final guardrail or H1 verdict. This is a follow-up recommendation, not authorization to alter frozen runs, labels or the experiment design.

## Subtasks
- [ ] S1 â€” Require completed, valid human decisions for all required audit keys before a final label; distinguish provisional scoring.
- [ ] S2 â€” Include note text in audit identity and retain all duplicate/free-text claims for semantic checking.
- [ ] S3 â€” Add synthetic boundary checks and have an independent reviewer verify the finalization contract.

## Success criteria
- [ ] An unrelated, missing or incomplete audit cannot produce FINAL or a certified zero guardrail.
- [ ] Opposite notes cannot share an audit decision; duplicate notes cannot disappear.
- [ ] Preserve historical outputs and disclose any scoring amendment; no tuning to held-out answers.

## Outputs
- Scoped P3-28 owner patch and synthetic regression checks, after coordination.
- Review evidence in `docs/review-2026-11-07-access-options.md`.

## Handoff
- **State:** todo; current risks reproduced with synthetic inputs only. No production scorer changed.
- **Next step:** P3-28 owner claims S1/S2 and reviews the isolated fixture `scripts/p3_43_audit_reproduction.py`.
- **Open questions:** Audit-version amendment and human completion remain with the experiment owner.
- **How to resume:** Read the review report; run the fixture with the available Python interpreter. Do not inspect held-out labels or outputs to choose the remedy.

## Log
- 2026-11-07 â€” Codex for Felipe: registered two current-code finalization risks discovered while reviewing historical P3-38; implementation deferred to avoid overlapping P3-28 ownership.

## Result
Pending.

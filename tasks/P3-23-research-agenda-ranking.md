---
id: P3-23
title: Record the competing-rails research agenda and rank datathon extensions
phase: P3
status: review
owner: CS 1
working: -
due: 2026-11-05
depends: -
---

## Goal
Save the preceding research brainstorm in English for teammates and agents, then validate and rank the six directions for the datathon. Renzo requested documentation and assessment, not execution of the proposed experiments.

## Subtasks
- [x] S1 — Preserve the six research directions, hypotheses, falsifiers and literature checks in an English document — done: Renzo (Codex), 4 Nov
- [x] S2 — Inspect existing tasks, scripts, data schemas and findings; document a ranked datathon plan with evidence limits — done: Renzo (Codex), 4 Nov
- [x] S3 — Link the documents, record validation and handoff, and prepare publication — done: Renzo (Codex), 4 Nov

## Success criteria
- [x] The English agenda preserves all six directions and distinguishes proposals from findings
- [x] Each rank states the testable subset, existing evidence, missing data, next steps, output and failure condition
- [x] Source-access limits and disagreements with existing plans are explicit; no registered prediction or core finding is changed
- [ ] A teammate reviews the documents and accepts or revises the recommended ranking

## Outputs
- `docs/competing-rails-research-agenda.md`
- `docs/competing-rails-datathon-ranking.md`

## Handoff
- **State:** English agenda and ranked datathon plans complete; no extension outcomes computed. Claim commit `966f4bc`; documentation publication follows the repository protocol.
- **Next step:** teammate review of both documents, particularly P3-20 inference/code readiness and differences from Felipe's strategy memo. Execution stays with existing task owners or a separately claimed extension task.
- **Open questions:** adopt which investigations and which reviewed results to include in the deck; no team scope decision is inferred from this documentation request.
- **How to resume:** start with the ranking table and validation section in `docs/competing-rails-datathon-ranking.md`; its final section contains the read-only schema/reference check. Preserve registered P3-20 rules; do not download November outcomes for this documentation task.

## Log
- 2026-11-04, Codex for Renzo: validation passed: both documents contain all six directions/plans, all local document links resolve, Markdown fences are balanced, `git diff --check` is clean, and `scripts/board.py` regenerated the board. Read-only inspection command retained in the ranking document. Publication prepared; independent review remains open.
- 2026-11-04, Codex for Renzo: S1–S3 completed. Sources rechecked, frozen schemas/reference output inspected, code availability and calendar validated. Recommendations and evidence limits recorded; review pending.
- 2026-11-04, Codex for Renzo: task created at Renzo's request; synced through `7204a38`, including Felipe's new strategy memo. Subtasks stated in chat. Documentation only; no scope adoption.

## Result
Two linked English documents preserve the long-run agenda and rank datathon-sized investigations. Recommended order: channel-specific prospective test, recovery/composition, cost sensitivity, existing user illustrations, qualified BRL-stablecoin comparison, and future conventional-FX spillovers. No new scientific finding or team adoption is claimed.

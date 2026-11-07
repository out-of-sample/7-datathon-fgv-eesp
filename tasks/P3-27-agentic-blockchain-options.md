---
id: P3-27
title: Evaluate agentic AI, blockchain and operational-learning extensions
phase: P3
status: done
owner: Renzo
working: -
due: 2026-11-06
depends: -
---

## Goal
Answer Renzo's request for plausible, source-checked uses of current technologies that add a measurable capability or broaden the economic question. Exclude forecasts of exchange rates, interest rates or market responses to rules. This is an options review, not adoption or implementation of an extension.

## Subtasks
- [x] S1 — Check existing AI work and distinguish implemented results from planned capabilities. — done: Codex for Renzo, 6 Nov
- [x] S2 — Check primary technical sources; compare new questions, deliverables, datasets, baselines and falsification tests. — done: Codex for Renzo, 6 Nov
- [x] S3 — Record the discussion and recommend priorities with explicit data and deadline limits. — done: Codex for Renzo, 6 Nov
- [x] S4 — Follow-up requested by Renzo: connect each proposal to existing evidence, identify missing links, and compare coherent narratives. — done: Codex for Renzo, 6 Nov
- [x] S5 — Formalize the access-map and on-chain reconciliation ideas as separate English task specifications using the project template. — done: Codex for Renzo, 6 Nov

## Success criteria
- [x] Each recommended option has an incremental contribution and a measurable test against a simpler alternative.
- [x] Opened primary sources are registered; technical feasibility is distinguished from empirical validation.
- [x] Planning decisions are distinguished from execution; no paid service used or experiment launched.

## Outputs
- Discussion in `docs/improvements_log.md` and primary sources in `docs/sources.md`.
- Portuguese comparison in Renzo's chat; implementation requires a separate adopted task.
- English implementation specifications: [P3-28 — agentic access map](P3-28-agentic-access-map.md) and [P3-29 — on-chain reconciliation](P3-29-on-chain-reconciliation.md), both todo and unassigned.

## Handoff
- **State:** Independent review accepted the historical deliverable on 7 Nov; task done. See `docs/review-2026-11-07-access-options.md`.
- **Next step:** No further work for this historical deliverable. Current access-method finalization issues belong to P3-43 and implementation remains with P3-28.
- **Open questions:** Human reference, semantic audit, resource equivalence and deck adoption are not approved by this review.
- **How to resume:** Read the review report. For P3-38 historical reproduction run `python scripts/p3_38_comparison_audit.py --from-git`; use the pinned snapshot rather than interpreting its failures as current-code failures.

## Log
- 2026-11-06 — Codex for Renzo: S5 complete; P3-28/P3-29 formalized with hypotheses, source/data checks, procedures, baselines, metrics, reading rules, outputs, independent review and project integration. Specs only; both todo, owner Team, working unassigned. ERC-20 primary source registered as T-13.
- 2026-11-06 — Codex for Renzo: Renzo requests full English task specifications for the access map and on-chain reconciliation. Documentation work claimed under S5; implementation tasks will remain todo and unassigned.
- 2026-11-06 — Codex for Renzo: narrative follow-up; options 2/3 have strongest continuity with current evidence, while option 1 has broader product scope but needs new operational evidence. No claim that rerouting avoids June's premium. Discussion appended; no deck change.
- 2026-11-06 — Codex for Renzo: completed source/design review. Corrected prior stress-worksheet novelty claim; documented agentic-work status and six alternatives with baselines, data gates and scope limits. No new empirical outputs.
- 2026-11-06 — Codex for Renzo: records the requested review. Pull/rebase cannot run with pre-existing STATUS/README changes and an untracked proposal; fetched origin without altering those files and checked divergence.

## Result
Review compared six extensions and linked them to the existing findings. Renzo selected the access map and on-chain reconciliation for formal task specifications, now P3-28 and P3-29. Their implementation, feasibility and empirical conclusions remain pending; no deck or frozen finding was changed.

## Independent review — 7 Nov 2026 (Codex for Felipe)
Reviewed against current task criteria; historical deliverable accepted and status done. Evidence and limits: `docs/review-2026-11-07-access-options.md`. P3-38 pinned synthetic checks reproduced; current P3-28 method selftest passes. This is not a human-reference audit or approval of H1; current scorer finalization recommendations remain with P3-28.

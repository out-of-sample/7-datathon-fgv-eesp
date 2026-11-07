---
id: P5-10
title: Deck v4 - the final PDF (10 slides + visual appendix) built from v3 and the 7 Nov plan
phase: P5
status: todo
owner: CS 1
working: -
due: 2026-11-08
depends: P5-08, P5-09
---

## Goal
Build the submission PDF from deck v3 following `docs/deck-plan-v4-2026-11-07.md`: ten slides that add the post-freeze work
(on-chain route and ledger, recovery composition, forecasting and treasury, registered predictions, access map), a slide-10
conclusion that answers the opening question in its own words, and a visual appendix (A1–A10) in the same PDF.

## Subtasks
- [ ] S1 — Felipe approves the plan (D2) and picks the subtitle (D4); Renzo decides repo visibility (D1); gates G1–G5 assigned (D3)
- [ ] S2 — Four charts added to `scripts/p5_09_deck_figures.py` (cost stack, price-vs-market triple panel, MAE bars, buyer frontier)
- [ ] S3 — Slides 1–10 edited or created in Claude Slides from v3 (badges, "Como medimos" chips, limit lines)
- [ ] S4 — Appendix A1–A4 and A10 (must), A5–A9 if time allows
- [ ] S5 — Number trace against findings, then the reader test (plan §8), by someone who did not build it
- [ ] S6 — Fallbacks applied for any failed gate; PDF exported, checked and uploaded by 19:00 Sun 8 Nov

## Success criteria
- [ ] At most 10 numbered slides; every results slide has a badge, a method chip, a limit line and a source footer
- [ ] Every number traces to a finding; no sentence from the plan's red list (§5)
- [ ] Reader test (plan §8) passes; the repo link opens for someone without access to the organisation

## Outputs
- Claude Slides deck v4 (link in Handoff), sources copied to `deck/v4_claude_slides/`; exported PDF
- `results/figures/P5-09_*.png` (new charts from the same script)

## Handoff
- **State:** plan written (`docs/deck-plan-v4-2026-11-07.md`); nothing built. The repo is private (checked 7 Nov).
- **Next step:** S1, decisions D1–D4 in plan §0, tonight.
- **Open questions:** D1 (public repo or a clean public copy), D4 (subtitle), who runs G1–G5.
- **How to resume:** read the plan §0–§2; v3 sources are in `deck/v3_claude_slides/project/slides/`; v3 artifact link in P5-09.

## Log
- 2026-11-07 18:30, agent for Renzo: task created with the v4 plan (Renzo asked for a detailed slide plan before building).

## Result

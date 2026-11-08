---
id: P5-10
title: Deck v4 - the final 10-slide PDF, built in Claude Slides from v3 and the 7 Nov plan
phase: P5
status: review
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
- [x] S2 — Charts: five new PNGs from `scripts/p5_10_deck_figures.py` (on-chain route, price / purchases / Foxbit share panels, waiting budget); cost stack and forecast-error bars drawn natively on the slides — done: Renzo (agent), 7 Nov
- [x] S3 — 10 slides written and published in Claude Slides (chapter labels, progress bar, evidence badges, "Como medimos" lines, limit lines, "próxima pergunta" links) — done: Renzo (agent), 7 Nov
- [ ] S4 — ~~Appendix A1–A10~~ dropped by Renzo (7 Nov): the PDF is the 10 slides only; appendix material stays in the repo annex
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
- **State:** deck v4 published (private Claude Slides artifact, Renzo's account): https://claude.ai/artifact/546JoYhyPui1zXtJnstW2z
  — 10 slides, storytelling in nine chapters: capa (clean) · 1 a porta · 2 como investigamos (12 techniques) · 3 o choque ·
  4 por que foi a porta (rules + alternatives) · 5 a rede não salva (cost stack, BRLA route, on-chain audit) · 6 o mercado
  (price vs purchases vs Foxbit share) · 7 a conta · 8 e agora? (forecasting + treasury) · 9 a lição (opening question,
  three lessons, the gauge in use, AI access map in test). Sources copied to `deck/v4_claude_slides/project/`; finding IDs
  only in speaker notes. Built without a render check (the Slides type asks not to verify): look at every slide once.
- **Next step:** S5 — someone who did not build it reads the PDF only (plan §8) and traces each number to its finding;
  Felipe (deck owner) approves or edits (S1). Then export the PDF from the deck page (download/export menu) for upload (S6).
- **Open questions:** D1 repo is PRIVATE (the jury cannot open the cover link); gates G1–G5 in plan §6 not run yet: if
  G1 (F-036) fails, slide 7 panel 3 and slide 10 lesson 3 fall back to F-008 ("volume da Foxbit ~6×"); G3 (F-033) fails →
  drop the four people cards on slide 8; G4 (ledger) fails → keep slide 6 col 3 with "reprodução pendente" in notes;
  G5 (F-029) fails → slide 4 "p = 0,03" becomes "maior que todas as 1.073 datas comuns". Teammates can open the link only
  after Renzo shares it.
- **How to resume:** edit a slide in `deck/v4_claude_slides/project/slides/<id>.html` and republish it to the same artifact
  (root = the folder holding `project/`); charts: `PLEX_DIR=<folder with IBM Plex Sans .ttf> .venv/bin/python scripts/p5_10_deck_figures.py`
  then re-upload the PNG as an asset and replace its `/_blob/` id.

## Log
- 2026-11-07 21:55, agent for Renzo: S2–S3 done → review. 10 slides published (link in Handoff); new figure script `scripts/p5_10_deck_figures.py` (asserts against F-024, F-036, F-037, F-048); appendix dropped at Renzo's request; gates G1–G5 still open.
- 2026-11-07 19:05, agent for Renzo: claimed S2–S3. Renzo: build only the 10 slides (no appendix pages), cover clean, other slides with more text, storytelling; D1–D4 still open (subtitle A used provisionally).
- 2026-11-07 18:30, agent for Renzo: task created with the v4 plan (Renzo asked for a detailed slide plan before building).

## Result

---
id: P5-07
title: Story notebook - the whole project end to end (deck prototype)
phase: P5
status: done
owner: CS 1
working: -
due: 2026-11-03
depends: P2-03, P2-04, P3-01, P4-01
---

## Goal
One notebook that tells the project from question to result in plain words, one section per future slide: thesis,
hypotheses, data, each test and what it showed, limits. The team uses it as the prototype of the deck (P5-01).

## Subtasks
- [x] S1 — `notebooks/p5_07_story.ipynb`: markdown in plain English (slide titles in pt-BR), figures and tables computed
  from `data/processed/` and `results/`, executed top to bottom with outputs saved. — done: Renzo, 2 Nov
- [x] S2 — Hypothesis scorecard (H0–H3 from `docs/02-dolar-cripto.md` §5) with the test that decides each. — done: Renzo, 2 Nov
- [x] S3 — Review by Felipe (deck owner) and mapping of all 15 sections to Slides 1–14 of `deck/deck_v1_ptbr.md`. — done: Felipe, 2026-11-02

## Success criteria
- [x] Runs top to bottom with `jupyter nbconvert --execute` from a fresh kernel (needs `data/processed/` and `results/`)
- [x] Every number in it comes from a file the notebook reads, or cites the finding it comes from
- [x] States what did not work or is not shown (lasting effect, unexplained fade, unverified causes)

## Outputs
- `notebooks/p5_07_story.ipynb`

## Handoff
<!-- Overwrite at the end of every session, finished or not, so anyone can continue from here. -->
- **State:** `done` (reviewed and adopted by Felipe as the structural backbone of `deck/deck_v1_ptbr.md`). All 15 sections of `notebooks/p5_07_story.ipynb` are mapped directly to the 14 slides of `deck/deck_v1_ptbr.md` (with Sections 8 and 10 combined on Slide 8, and both Options C and A preserved on Slide 10 for the team's P3-01 choice).
- **Next step:** None; task complete.
- **Open questions:** Team choice between Option C and Option A on Slide 10 (`P5-01`).
- **How to resume:** `cd notebooks && ../.venv/bin/jupyter nbconvert --to notebook --execute --inplace p5_07_story.ipynb`

## Log
- 2026-11-02, Felipe (review): Reviewed all 15 sections and outputs of `notebooks/p5_07_story.ipynb`; mapped Sections 1–15 to Slides 1–14 of `deck/deck_v1_ptbr.md` (Anexo D.2 traceability table in `deck/annex_v1_ptbr.md`). Status -> `done`.
- 2026-11-02, agent for Renzo: notebook written and executed (34 cells); status review.
- 2026-11-02, agent for Renzo: created at Renzo's request (deck prototype); Renzo takes it.

## Result
`notebooks/p5_07_story.ipynb` (34 cells, 15 sections) tells the entire project end to end from raw/processed tables, including the hypothesis scorecard ($H_0$–$H_3$) and explicit limitations, and now serves as the direct blueprint for the 14-slide `deck/deck_v1_ptbr.md`.

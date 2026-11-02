---
id: P5-07
title: Story notebook - the whole project end to end (deck prototype)
phase: P5
status: doing
owner: CS 1
working: Renzo
due: 2026-11-03
depends: P2-03, P2-04, P3-01, P4-01
---

## Goal
One notebook that tells the project from question to result in plain words, one section per future slide: thesis,
hypotheses, data, each test and what it showed, limits. The team uses it as the prototype of the deck (P5-01).

## Subtasks
- [ ] S1 — `notebooks/p5_07_story.ipynb`: markdown in plain English (slide titles in pt-BR), figures and tables computed
  from `data/processed/` and `results/`, executed top to bottom with outputs saved. — doing: Renzo
- [ ] S2 — Hypothesis scorecard (H0–H3 from `docs/02-dolar-cripto.md` §5) with the test that decides each.

## Success criteria
- [ ] Runs top to bottom with `jupyter nbconvert --execute` from a fresh kernel (needs `data/processed/` and `results/`)
- [ ] Every number in it comes from a file the notebook reads, or cites the finding it comes from
- [ ] States what did not work or is not shown (lasting effect, unexplained fade, unverified causes)

## Outputs
- `notebooks/p5_07_story.ipynb`

## Handoff
<!-- Overwrite at the end of every session, finished or not, so anyone can continue from here. -->
- **State:** started 2 Nov.
- **Next step:** S1.
- **Open questions:** none
- **How to resume:** `.venv/bin/jupyter nbconvert --to notebook --execute --inplace notebooks/p5_07_story.ipynb`

## Log
- 2026-11-02, agent for Renzo: created at Renzo's request (deck prototype); Renzo takes it.

## Result

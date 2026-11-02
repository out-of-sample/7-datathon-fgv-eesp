---
id: P5-07
title: Story notebook - the whole project end to end (deck prototype)
phase: P5
status: review
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

## Success criteria
- [x] Runs top to bottom with `jupyter nbconvert --execute` from a fresh kernel (needs `data/processed/` and `results/`)
- [x] Every number in it comes from a file the notebook reads, or cites the finding it comes from
- [x] States what did not work or is not shown (lasting effect, unexplained fade, unverified causes)

## Outputs
- `notebooks/p5_07_story.ipynb`

## Handoff
<!-- Overwrite at the end of every session, finished or not, so anyone can continue from here. -->
- **State:** done, in review. 15 sections = 15 candidate slides (pt-BR titles in each heading): question, hypotheses,
  data, history, the jump on 3 exchanges, the notice and its sources, all rules vs ordinary dates, synthetic control,
  spike vs lasting, other countries, cost of the notice (R$ 5,052 per US$ 100k), SVB, monitor, lessons from 2025,
  scorecard and limits. Every number is read from `data/processed/` or `results/`; prose numbers checked against the outputs.
- **Next step:** a teammate (Felipe as deck owner) reads it and marks which sections become slides in P5-01. The notebook
  was built by a script in the agent's scratchpad; edit the notebook directly from now on.
- **Open questions:** the bank-route comparison (P3-01 framing) is deliberately left out of the headline.
- **How to resume:** `cd notebooks && ../.venv/bin/jupyter nbconvert --to notebook --execute --inplace p5_07_story.ipynb`

## Log
- 2026-11-02, agent for Renzo: notebook written and executed (34 cells); status review.
- 2026-11-02, agent for Renzo: created at Renzo's request (deck prototype); Renzo takes it.

## Result

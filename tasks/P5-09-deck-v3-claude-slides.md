---
id: P5-09
title: Deck v3 - the 10-slide deck rebuilt in Claude Slides, in the mentor deck's design, with a methods slide and checked references
phase: P5
status: doing
owner: CS 1
working: Renzo (agent)
due: 2026-11-06
depends: P5-01, P4-03
---

## Goal
A third, self-contained version of the 10-slide deck next to v1 and v2 (Felipe picks; nothing in v1/v2 changes). It keeps
the visual language of the deck shown to the mentor on 4 Nov (navy cover, orange accent, warm off-white pages, serif titles
over a sans body, blue = ordinary data, orange = the event), fits the story in 10 slides that read without a presenter,
gives one slide to methods and techniques, cites papers that were opened, and puts no task or finding IDs on the slides.

## Subtasks
- [x] S1 — Inputs read: decks v1/v2, 10-slide plan, mentor deck (PDF in Renzo's Downloads, 17 slides), mentor notes; past
  winners' decks (FGV pages, 2023 and 2024 podiums) reviewed for design lessons — done: Renzo (agent), 5 Nov
- [x] S2 — References checked against Crossref/BIS (list in Log) — done: Renzo (agent), 5 Nov
- [ ] S3 — Charts redrawn in the deck palette from frozen data (`scripts/p5_09_deck_figures.py`) — doing: Renzo (agent)
- [ ] S4 — Slides written and published in Claude Slides (10 + one references page) — doing: Renzo (agent)
- [ ] S5 — Felipe (deck owner) reviews; team picks v1, v2 or v3

## Success criteria
- [ ] 10 content slides (references page marked as annex), pt-BR, no task/finding IDs on any slide
- [ ] Every number on a slide matches a finding (map in Handoff); exploratory ones are labelled in the speaker notes
- [ ] One slide shows the methods with formulas and opened references
- [ ] Charts regenerate from `scripts/p5_09_deck_figures.py` using only frozen data or registered outputs

## Outputs
- `scripts/p5_09_deck_figures.py` → `results/figures/P5-09_*.png`
- Claude Slides deck (link in Handoff)

## Handoff
- **State:** inputs read, references checked, building charts and slides.
- **Next step:** S3, then S4.
- **Open questions:** Felipe: v3 vs v1/v2. Team: keep the references page as an 11th page (annex) or drop it.
- **How to resume:** `.venv/bin/python scripts/p5_09_deck_figures.py`.

## Log
- 2026-11-05, agent for Renzo: task created at Renzo's request ("v3 of the 10-slide deck using Claude Slides"). References
  checked on Crossref (DOI records opened 5 Nov): Shleifer & Vishny 1997 JF 52(1) 35–55; Makarov & Schoar 2020 JFE 135(2)
  **293–319** (the annex's 289 is wrong); Abadie, Diamond & Hainmueller 2010 JASA 105(490) 493–505; Bai 1997 REStat 79(4)
  551–563; Bai & Perron 2003 JAE 18(1) 1–22; Gelbach, Helland & Klick 2013 ALER 15(2) 495–541; Corwin & Schultz 2012 JF
  67(2) 719–760; Duffie 2010 JF 65(4) 1237–1267; Page 1954 Biometrika 41(1-2) 100–115; BIS WP 1340 (27 Mar 2026) and
  WP 1385 (19 Oct 2026) pages reopened. Past winners (FGV event pages, 4th and 5th editions): academic order and a
  literature slide, formulas and a benchmark; weak points were walls of small text, busy dark backgrounds, default
  charts and topic titles ("Resultados").

## Result

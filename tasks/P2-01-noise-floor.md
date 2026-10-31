---
id: P2-01
title: Noise floor (how big a premium is just trading friction)
phase: P2
status: doing
owner: CS 1
working: Renzo
due: 2026-11-01
depends: P1-02
---

## Goal
Estimate the typical bid-ask spread of USDT/BRL so that any premium inside that band is treated as noise,
not evidence.

## Subtasks
- [ ] S1 — Spread estimators from hourly high/low/close: Corwin-Schultz and Abdi-Ranaldo; daily median. — doing: Renzo
- [ ] S2 — Compare with the probe's median hourly range (F-001).
- [ ] S3 — Add the band to the premium chart.

## Success criteria
- [ ] `data/processed/P2-01_noise_floor_daily.csv`
- [ ] Finding written: typical spread in bps by year, and how the premium compares
- [ ] Naive comparison shown: raw hourly range vs the estimators

## Outputs
- `scripts/p2_01_noise.py`, `data/processed/P2-01_noise_floor_daily.csv`, finding file

## Handoff
<!-- Overwrite at the end of every session, finished or not, so anyone can continue from here. -->
- **State:** not started
- **Next step:** S1
- **Open questions:** none
- **How to resume:** -

## Log
- 2026-10-31, agent for Renzo: Renzo takes P2-01 (P1-02 in review)

## Result

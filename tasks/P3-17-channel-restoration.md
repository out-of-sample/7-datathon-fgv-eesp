---
id: P3-17
title: Did the BCB let funds resume the activity the 23 Jun notice stopped, and did the premium fall when it did? (reopening test)
phase: P3
status: doing
owner: Economist
working: agent for Renzo
due: 2026-11-04
depends: P3-14, P3-15, P4-04
---

## Goal
The 23 Jun 2026 notice stopped one activity: FX transactions to import cryptoassets in which a fund intermediates or
supplies a particular client (E-05.1, E-05.3). If the BCB later allowed that activity again, a **reopening** is the
opposite-direction test the deck lacks (one shock, `docs/deck-plan-10-slides.md` weak point 1) and could explain the
fade (F-011, "unexplained"). Today we have no verified restoration date. This task finds out, or says it cannot be run.

**Hypothesis (H4).** If that same activity was restored, the domestic USDT premium should fall around the *first publicly
verifiable restoration date*, together with evidence that supply through that channel resumed.

**What H4 is not.** Permission to arbitrage inside an exchange's open order book (the BCB "liberou", 26 Jun, E-05.5) is a
different activity and is not restoration. A falling premium alone is not evidence of restoration.
A "no verified restoration" verdict means the reopening test cannot be run; it does **not** mean the June notice had no effect.

## What we already know (disclose; do not re-derive)
- 26 Jun: suspension kept "até que esse alinhamento ocorra"; in-book arbitrage released (E-05.5, E-12).
- Break test dates the fall at 22 Jul (109.1 → 26.8 bps); no event within ±5 PTAX days (F-011, P2-02). But the premium
  peaked on 3 Jul (185.9) and halved by 10 Jul, so the fall began before 22 Jul.
- Residents' stablecoin purchases abroad stayed at 32% of Jan–May in Aug–Sep (F-024, T2 "partial, inconclusive"); the series
  covers all residents, not only funds. Venues moved together through July (P2-05). Foxbit Infra relaunch 18 Jul (M-05) and
  NovaDAX partnership 7 Jul (M-04) are not channel restorations.
- One extended search on 2 Nov for a resumption of funds' operations in July found nothing (not proof of absence).
- These were seen before this spec; any candidate date they suggest is not a clean pre-registered hypothesis.

## Subtasks
- [ ] S1 — doing: agent for Renzo — Evidence trail (no prices yet). Search BCB communications and normativos, bank or fund disclosures (ABToken,
  fund managers, CVM), and contemporaneous press from 23 Jun to 30 Oct 2026. For each candidate: date published, date
  effective, operative quoted language, source opened (`prompt.md` §6), and one class: **full restoration | partial change |
  clarification | substitution through another channel | no verified change**. Write the table in
  `results/tables/P3-17_candidates.md` and register sources in `docs/sources.md` (next E-IDs).
- [ ] S2 — Spec, committed **before** looking at premiums around any candidate. Fixed rule: statistic = mean premium over
  [+1,+20] PTAX days minus [−20,−1] (as F-016/F-029), plus the first-day change; placebo = clean dates of F-016 and the
  non-overlapping version of F-029; list other dated events in each window (E-05.5, E-10, E-11, E-12, M-04, M-05).
  Candidate set and class cutoffs are frozen in this commit; "credible" = any S1 row classed full or partial restoration.
- [ ] S3 — Run for **every** credible candidate, including those with no price response. Corroboration: Binance/Foxbit/MB
  volume and order size (F-008, F-024 order-flow table) and the BCB monthly stablecoin-purchase series (`SGS 29644`,
  F-024). Script `scripts/p3_17_restoration.py`.
- [ ] S4 — Competing explanations for the fall around 22 Jul: (1) the restricted channel resumed; (2) the premium fell
  without it (adaptation, alternative supply, changing demand). Write beforehand what each predicts in the volume,
  order-size, and BCB-series data, then compare. Falling prices cannot count as evidence for (1).
- [ ] S5 — Finding F-0NN (next free) with verdict **supported | contradicted | unresolved**, and, if no date is verifiable,
  the sentence that the reopening test cannot be run.

## Success criteria
- [ ] Dated source table with quoted language, publication vs effective date, and a class per candidate; every link opened
- [ ] Spec committed before any price around a candidate is examined
- [ ] Results for every credible candidate, with placebo p (all clean and non-overlapping) and other events in the window
- [ ] Verdict stated; a missing restoration date reported as "test cannot be run", not as "no effect"
- [ ] Deck language level stated (the fall's cause stays "not shown" unless the verdict is supported)

## Outputs
- `results/tables/P3-17_candidates.md`, `scripts/p3_17_restoration.py`, `results/tables/P3-17_*.csv`, `findings/F-0NN-...md`

## Handoff
- **State:** task written and spec not yet started; nobody is working on it.
- **Next step:** S1 (evidence trail), then commit S2 before any price work.
- **Open questions:** none; Felipe decides deck use after S5. Core F-001..F-027 stay unchanged (freeze rule).
- **How to resume:** read E-05.1, E-05.3, E-05.5, E-12 in `docs/sources.md`; F-011, F-024, F-028, F-029; prompt for the
  agent in `docs/agent-prompt-P3-17.md`.

## Log
- 2026-11-02, agent for Renzo: created (todo) from Renzo's hypothesis; prompt for a second agent in `docs/agent-prompt-P3-17.md`
- 2026-11-02, agent for Renzo: takes S1 (evidence trail; no prices looked at)

## Result

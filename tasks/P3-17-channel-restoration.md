---
id: P3-17
title: Did the BCB let funds resume the activity the 23 Jun notice stopped, and did the premium fall when it did? (reopening test)
phase: P3
status: review
owner: Economist
working: -
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

## S2 specification (committed 2 Nov 2026, before any comparison is computed)

**Candidate set (frozen).** C1–C12 in `results/tables/P3-17_candidates.md`. Credible = classed full restoration or
partial change. **Credible set: empty.** A row enters it only if a teammate opens a new source that shows the activity
was allowed again; the test below then runs on that date unchanged.

**Test for a credible date t0 (none today).** Premium = `data/processed/P1-02_premium_daily.csv`, PTAX days.
A = mean[+1,+20] − mean[−20,−1] (t0 excluded); first-day change = premium(t0+1) − premium(t0). Placebos: all clean
dates of `scripts/p4_04_inference.py`, and its non-overlapping sets (stride 41, every offset); p = (k+1)/(n+1), two-sided.
List the other dated items within ±20 PTAX days (E-05.5, E-10, E-11, E-12, M-04, M-05 and any P3-17 row).
H4 verdict: **supported** if A < 0 with p ≤ 0.05 on the non-overlapping placebos and at least one corroboration below
moves as (1) predicts; **contradicted** if a credible t0 exists and A is not negative beyond placebo (p > 0.10);
**unresolved** otherwise. **With the credible set empty the verdict is "unresolved: the reopening test cannot be run".**

**S4: what each explanation of the fall from 22 Jul predicts** (written before the comparison table is computed).
Data: (i) BCB net purchases of stablecoins abroad by residents, SGS 29644, US$ million per month (P3-10);
(ii) `results/tables/P3-10_order_flow.csv`, per venue (Binance, Foxbit, Mercado Bitcoin): volume per day (USDT), trades per
day, average trade (USDT), buyer-initiated share, in three PTAX-day windows around 23 Jun: before [−20,−1] (25 May–22 Jun),
spike [+1,+20] (24 Jun–21 Jul), after [+21,+60] (from 22 Jul, the break date). R = mean(Aug, Sep) / mean(Jan–May 2026).

| Explanation | BCB purchases abroad | Exchange structure (avg trade, buyer share; per venue) | Volume |
|---|---|---|---|
| (1) the stopped channel resumed (by rule, or institution by institution after the "alinhamento") | recovers: R ≥ 0.5 and Aug > Jul | reverts: after closer to before than to spike, \|log(after/before)\| < \|log(after/spike)\| | – |
| (2a) adaptation or domestic substitute supply (in-book arbitrage freed 26 Jun, inventories, exchange desks such as Foxbit Infra) | stays low: R < 0.5 | does not revert: \|log(after/before)\| ≥ \|log(after/spike)\| on most venue-metrics | – |
| (2b) demand fell | – | buyer share after < before | Binance volume per day after < before by more than 25% (log < −0.29) |
| (2c) substitute imports by FX-authorised institutions (the C7 channel) | recovers, like (1) | – | – |

**Reading rule.** (1) is called *inconsistent with the data* only if R < 0.5 **and** the structure does not revert on most
venue-metrics; *consistent* if both move as (1) predicts; *mixed* otherwise. (1) and (2c) cannot be separated with these
data. These are consistency checks, not causal tests. A falling premium is not evidence for (1); the premium had already
halved by 10 Jul, before the break date.

**Disclosure.** Known before this spec: F-024 (R ≈ 0.32 in Aug–Sep; July −78%), F-008 (Foxbit trades about five times larger
from July), and the first two rows of `P3-10_order_flow.csv` (Binance and Foxbit, before window), seen while checking its
columns. S4 is therefore not blind; only its rule is fixed before the comparison is computed.

## Subtasks
- [x] S1 — done: agent for Renzo, 2026-11-02 — Evidence trail (no prices yet). Search BCB communications and normativos, bank or fund disclosures (ABToken,
  fund managers, CVM), and contemporaneous press from 23 Jun to 30 Oct 2026. For each candidate: date published, date
  effective, operative quoted language, source opened (`prompt.md` §6), and one class: **full restoration | partial change |
  clarification | substitution through another channel | no verified change**. Write the table in
  `results/tables/P3-17_candidates.md` and register sources in `docs/sources.md` (next E-IDs).
- [x] S2 — done: agent for Renzo, 2026-11-02 — Spec, committed **before** looking at premiums around any candidate. Fixed rule: statistic = mean premium over
  [+1,+20] PTAX days minus [−20,−1] (as F-016/F-029), plus the first-day change; placebo = clean dates of F-016 and the
  non-overlapping version of F-029; list other dated events in each window (E-05.5, E-10, E-11, E-12, M-04, M-05).
  Candidate set and class cutoffs are frozen in this commit; "credible" = any S1 row classed full or partial restoration.
- [x] S3 — done: agent for Renzo, 2026-11-02 (no credible candidate, so no event test; corroboration data compared in S4) — Run for **every** credible candidate, including those with no price response. Corroboration: Binance/Foxbit/MB
  volume and order size (F-008, F-024 order-flow table) and the BCB monthly stablecoin-purchase series (`SGS 29644`,
  F-024). Script `scripts/p3_17_restoration.py`.
- [x] S4 — done: agent for Renzo, 2026-11-02 — Competing explanations for the fall around 22 Jul: (1) the restricted channel resumed; (2) the premium fell
  without it (adaptation, alternative supply, changing demand). Write beforehand what each predicts in the volume,
  order-size, and BCB-series data, then compare. Falling prices cannot count as evidence for (1).
- [x] S5 — done: agent for Renzo, 2026-11-02 (F-030) — Finding F-0NN (next free) with verdict **supported | contradicted | unresolved**, and, if no date is verifiable,
  the sentence that the reopening test cannot be run.

## Success criteria
- [x] Dated source table with quoted language, publication vs effective date, and a class per candidate; every link opened
- [x] Spec committed before any price around a candidate is examined
- [x] Results for every credible candidate, with placebo p (all clean and non-overlapping) and other events in the window (none credible: nothing to run)
- [x] Verdict stated; a missing restoration date reported as "test cannot be run", not as "no effect"
- [x] Deck language level stated (the fall's cause stays "not shown" unless the verdict is supported)

## Outputs
- `results/tables/P3-17_candidates.md`, `scripts/p3_17_restoration.py`, `results/tables/P3-17_*.csv`, `findings/F-0NN-...md`

## Handoff
- **State:** S1–S5 done, status `review`. Verdict **unresolved: the reopening test cannot be run** (no public source shows
  the stopped activity resumed; F-030). S4 consistency check under the committed rule: **mixed** (purchases abroad stayed at
  R = 0.32; exchange trade size and buyer share reverted on 3 of 4 venue-metrics; demand fall not supported).
- **Next step:** a teammate who did not do this work re-checks it: (1) open 3–4 rows of `results/tables/P3-17_candidates.md`
  and compare the quotes; (2) run `python scripts/p3_17_restoration.py` and compare the `B1`–`B3` lines with F-030;
  (3) if it holds, F-030 `exploratory` → `confirmed` and this task → `done`.
- **Open questions:** Felipe decides whether one sentence goes in the deck (suggested pt-BR line in F-030, "Used in deck").
  If anyone finds a source that funds or banks resumed (e.g. a CVM filing), add it as a new row; if it is full or partial
  restoration, the S2 test runs on its date unchanged.
- **How to resume:** S2 spec and predictions are in this file; source table `results/tables/P3-17_candidates.md`; sources
  E-13–E-16 and E-05.11 in `docs/sources.md`; script `scripts/p3_17_restoration.py` (part A needs internet, part B reads
  `data/processed/P3-10_imports_monthly.csv` and `results/tables/P3-10_order_flow.csv`).

## Log
- 2026-11-02, agent for Renzo: created (todo) from Renzo's hypothesis; prompt for a second agent in `docs/agent-prompt-P3-17.md`
- 2026-11-02, agent for Renzo: takes S1 (evidence trail; no prices looked at)
- 2026-11-02, agent for Renzo: S1 done. 12 candidates in `results/tables/P3-17_candidates.md` (BCB normativos and press notes 20 Jun–31 Oct screened by `scripts/p3_17_restoration.py` part A; votes 108 and 120/2026; REF Oct 2026; press). None is full or partial restoration: 2 clarifications (26 Jun meeting; Res. BCB 599 code for authorised institutions, 9 Oct), 1 possible substitution (Foxbit Infra, company claim), 9 no verified change; the BCB restated the activity is unlawful (LAI, published 29 Jul). New sources E-13–E-16, E-05.11
- 2026-11-02, agent for Renzo: S2 spec committed (section above): credible set empty, so H4 is "unresolved: test cannot be run"; S4 predictions and reading rule fixed before the comparison
- 2026-11-02, agent for Renzo: S3–S5 done → review. No credible candidate, no event test. S4: R = 0.32 (< 0.5), structure reverts 3 of 4, Binance volume −5.4% → mixed; F-030 (exploratory)

## Result
**Unresolved: the reopening test cannot be run** (F-030). From 23 Jun to 30 Oct 2026 no BCB rule, BCB press note or press
report says that funds were allowed to resume FX imports of crypto for clients; the only stated route back was a
confidential, institution-by-institution alignment with the conduct supervisor, with no public completion date. The BCB
restated in writing (published 29 Jul) that these operations lack legality under current rules. The fall from 22 Jul
happened while purchases abroad stayed at a third of their earlier level (R = 0.32), while exchange order flow mostly
returned to its pre-notice pattern: under the committed rule the evidence is mixed and the fall's cause stays **not shown**.

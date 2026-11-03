---
id: P3-19
title: Did seller-initiated trading on Foxbit respond to the premium over the official dollar (import arbitrage) or to the Foxbit–Binance gap (cross-venue arbitrage)?
phase: P3
status: doing
owner: CS 1
working: agent for Renzo
due: 2026-11-04
depends: P3-17
---

## Goal
F-031 (post hoc) shows heavy seller-initiated trading on Foxbit while the premium fell (30 Jun – 21 Jul 2026). That statistic
says which side crossed the spread, not who traded or whether USDT entered Brazil (review in `docs/improvements_log.md`).
This task asks a narrower question with data we already have: **did that trading respond to price, and to which price?**
Arbitrage that brings USDT into Brazil reacts to the premium over the official dollar; arbitrage between exchanges reacts to
the Foxbit–Binance gap. If the trading tracked the premium, the fade is *consistent with* price-responsive capital arriving
(Duffie 2010, L-10); it still does not identify the traders or show net imports. Asked by Renzo on 2 Nov 2026.

## Specification (committed before any of these statistics is computed)
**Outcome** y = Foxbit seller-initiated minus buyer-initiated volume (volume − 2 × taker-buy volume, mn USDT;
`data/raw/foxbit/USDTBRL-1h.csv`).
**Sample** PTAX days 24 Jun – 30 Sep 2026 (weekdays with a PTAX). Placebo sample: PTAX days 2 Jan – 22 Jun 2026.

**Daily test (primary).** y_t = sum of y over 13:00–18:00 Brasília on day t (after the PTAX windows).
x1_t = premium over PTAX on day t at the PTAX windows (`P1-02_premium_daily.csv`, `premium_bps`, measured 10:00–13:00).
x2_t = Foxbit minus Binance premium on day t at the same windows (`P2-05_venues_daily.csv`). OLS y on x1 and x2.
95% CI by moving-block bootstrap over days (block 5 PTAX days, 2,000 draws, seed 17).

**Within-day test (secondary).** Hourly, start hours 13–17 Brasília (the day's PTAX is already published). x1_h = hourly
premium against that day's PTAX at the close of hour h (`P1-02_premium_hourly.csv`; rows whose `ptax_last_date_brt` is not
the same day are dropped); x2_h = Foxbit close / Binance close − 1 at hour h (bps); outcome y in hour h+1. Both sides
demeaned within each day (day fixed effects). CI by bootstrap over whole days (2,000 draws, seed 17).

**Threshold.** On the daily sample, y_t = a + b·max(0, x1_t − k), k on a grid 10–150 bps step 5, least squares; CI by the
same block bootstrap. k is the premium above which sellers crossed the spread on net. Passive selling (limit orders) does
not show in y, so k is at most an upper bound on what the new sellers needed, not a route cost.

**Reading rule.**
- *Responds to the premium* if the daily x1 coefficient is > 0 with a CI excluding 0 **and** the within-day x1
  coefficient is > 0.
- *Responds to the cross-venue gap* if the daily x2 coefficient is > 0 with a CI excluding 0 (Foxbit dear → sell there).
- Both, neither, or only the daily x1 (then: "tracks the period, not hour-to-hour price; arrival timing cannot be
  separated from price response").
- Placebo: the same daily regression before the notice; a large positive x1 there would mean the relation is not specific
  to the episode.
- Best case language: "seller-initiated trading on Foxbit rose with the premium over the official dollar, as arbitrage
  that brings USDT into Brazil would". Never "new supplier", "imports" or "caused the fall".

**Known before this spec (disclosed).** F-031: daily correlation of y with the premium level +0.36 (24 Jun – 31 Jul),
selling faded near a 50 bps premium, Foxbit − Binance premium −1.14 bps on average during the wave; the hourly premium
against a stale PTAX carries intraday FX moves, which bias the within-day x1 coefficient toward zero (noted, not fixed).

## Subtasks
- [ ] S1 — Spec committed (this section) — doing: agent for Renzo
- [ ] S2 — Script `scripts/p3_19_supply_response.py`, tables `results/tables/P3-19_*.csv`
- [ ] S3 — Finding F-032 with the verdict under the rule; correct F-031's wording ("new supply", "new seller") per the review

## Success criteria
- [ ] Spec committed before the statistics are computed
- [ ] Daily, within-day, threshold and placebo results with CIs and the command that reproduces them
- [ ] Verdict under the rule; language level "consistent with" at most

## Outputs
- `scripts/p3_19_supply_response.py`, `results/tables/P3-19_*.csv`, `findings/F-032-...md`

## Handoff
- **State:** spec written; script not yet run.
- **Next step:** S2.
- **Open questions:** none.
- **How to resume:** this file; F-031; `docs/improvements_log.md` (review of F-031).

## Log
- 2026-11-02, agent for Renzo: created at Renzo's request; spec written before any statistic

## Result

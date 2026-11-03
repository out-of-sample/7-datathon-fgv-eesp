---
id: P3-21
title: Who paid and who gained - the 23 Jun notice seen from five kinds of users of the digital dollar
phase: P3
status: todo
owner: CS 1
working: -
due: 2026-11-04
depends: P1-02, P3-03, P3-11
---

## Goal
Turn the money result (F-015, F-025) into a table a reader understands in ten seconds: what the notice meant for a person
who needed dollars that month, a monthly saver, someone already holding USDT, someone who bought in the panic, and those who
sold. Each row follows a rule fixed in advance on the measured premium path. No trading strategy, no optimisation, no rule
chosen after seeing the path. It is an **illustration** (four language levels: illustrative), not new evidence. It
replaces the content of slide 9 if Felipe agrees; it does not add a slide.

## Specification (fixed before the script runs)
The premium path is already known (F-016, F-022, F-024), so this is not a blind test. The specification only prevents
picking convenient dates.

**Data.** `data/processed/P1-02_premium_daily.csv` (frozen to 30 Oct 2026): `premium_bps` and the PTAX sell rate per PTAX
day. No download.

**Counterfactual.** The premium had the notice not happened = the pre-notice level, the mean of the 20 PTAX days before
t0 = 23 Jun 2026 (15.2 bps, F-025). Variant: the post-spike level as the counterfactual, to show how much depends on that
choice (F-022: the post-spike level is not distinguishable from drift).

**Money.** For a purchase of US$ X on PTAX day d: extra cost in R$ = (premium_d − counterfactual) / 10,000 × X × PTAX_d.
For a holder: gain from t0 to day d = (premium_d − premium_t0) / 10,000 × X × PTAX_d. Fees, spreads and taxes are the same
with and without the notice and are left out, except that spreads widened during the spike (F-021, exploratory): stated
as a limit, not modelled.

**The five users** (every date is a calendar rule or a signal available on the day):

| ID | Who | Rule | Reported |
|---|---|---|---|
| U1 | Needed dollars during the spike | Buys US$ 100k on one PTAX day in [t0+1, t0+20] | Average extra cost over the 20 days, and the range across days. Must reproduce F-015 (R$ 5,052) within 2% |
| U2 | Monthly saver | Buys US$ 10k on the first PTAX day of each month, Jan–Oct 2026 (US$ 100k in total) | Extra cost per month and in total. Variants: last PTAX day of the month; equal amounts every PTAX day |
| U3 | Already held USDT | Holds US$ 100k of USDT at t0 | Gain over the official dollar if sold on t0+1, t0+5, t0+20 or 30 Oct (fixed dates; never "at the peak") |
| U4 | Bought in the panic | Buys US$ 100k on t0+1 (24 Jun: the day the press reported the notice and the real-time monitor fired, F-014, F-023) and holds | Loss over the official dollar at t0+20 and at 30 Oct |
| U5 | Sellers as a group | – | Cited from F-025, not recomputed: R$ 106 mn on Binance (R$ 145 mn on three exchanges) went from buyers to sellers; who they were is inferred (F-025, F-031/F-032 exploratory) |

**Wording rules for the deck.** "Transferência", never "perda de bem-estar"; "ilustração com regras fixadas antes";
no advice on how to trade; no tax-avoidance framing ("diferença de alíquota", never "brecha").

## Subtasks
- [ ] S1 — Commit this Specification before writing the script (the commit order is the record)
- [ ] S2 — `scripts/p3_21_who_paid.py`: U1–U4 and the variants → `results/tables/P3-21_who_paid.csv`; U1 reproduces F-015
  within 2%
- [ ] S3 — Finding (illustrative) with the command; figure only if Felipe wants one for slide 9
- [ ] S4 — pt-BR slide-9 table and one-sentence takeaway for Felipe (deck owner), within the 10-slide limit
- [ ] S5 — Review by Felipe (money layer owner, P3-11)

## Success criteria
- [ ] Specification committed before the script's first run
- [ ] U1 reproduces F-015 (R$ 5,052 per US$ 100k) within 2%
- [ ] Every number in a finding with its command; the counterfactual variant reported next to the main one
- [ ] Felipe accepts or rejects the slide-9 replacement

## Outputs
- `scripts/p3_21_who_paid.py` (header: purpose, inputs, outputs, how to run)
- `results/tables/P3-21_who_paid.csv`; finding F-0xx (next free number)

## Handoff
- **State:** plan written 3 Nov; nothing computed.
- **Next step:** S1, commit the Specification; then S2.
- **Open questions:** Felipe: does slide 9 take this table in place of the current one?
- **How to resume:** read the Specification; the inputs are already frozen; `scripts/p3_11_money.py` has the pre-notice
  level and the PTAX conversion to reuse.

## Log
- 2026-11-03, agent for Renzo: created at Renzo's request (brainstorm version 2: who paid and who gained).

## Result
<!-- fill when done -->

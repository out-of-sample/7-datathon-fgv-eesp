---
id: F-033
title: Illustration - the notice cost a buyer during the spike about R$ 4,840 per US$ 100k, a monthly saver only R$ 490 in the year, and gave a holder up to R$ 6,800 if they sold the next day; a panic buyer who held was R$ 10,000 behind by 30 Oct
status: exploratory
task: P3-21
date: 2026-11-03
checked_by: -
---

## Claim
Using rules fixed before the script ran (P3-21 Specification, commit `79e15d1`), the 23 Jun 2026 notice was a large cost for
whoever had to buy dollars in the following four weeks, almost nothing for a regular monthly saver, a gain for anyone already
holding USDT who sold soon after, and a loss for anyone who bought in the panic and held. This is an **illustration** on the
known premium path, not new evidence. Every amount is a transfer between buyers and sellers, not a welfare loss.

## Evidence
Premium over PTAX from `data/processed/P1-02_premium_daily.csv` (frozen 30 Oct 2026), R$ at each day's PTAX sell rate.
Main counterfactual: pre-notice level 15.24 bps (mean of the 20 PTAX days before 23 Jun).

| User | Rule | R$ (pre-notice counterfactual) | R$ (post-spike counterfactual, 26.78 bps) |
|---|---|---|---|
| U1 needed dollars in the spike | US$ 100k on one PTAX day, 24 Jun – 21 Jul | +4,842 extra cost on average (1,895 to 8,824 by day) | +4,249 (1,308 to 8,227) |
| U2 monthly saver | US$ 10k on the first PTAX day of each month, Jan – Oct 2026 | +492 in total (last day: +345; every day: +402) | −104 (−251; −192) |
| U3 already held USDT | US$ 100k held on 23 Jun, sold on … | 24 Jun: +6,802 · 30 Jun: +5,487 · 21 Jul: +1,407 · 30 Oct: −2,992 | – |
| U4 bought in the panic | US$ 100k bought on 24 Jun and held, value on … | 21 Jul: −5,223 · 30 Oct: −10,070 | – |
| U5 sellers as a group | cited, not recomputed | R$ 106 mn on Binance, R$ 145 mn on three exchanges (F-025) | – |

U3 and U4 compare the premium on the selling day with the premium on the buying day, so they need no counterfactual.
Signs: positive = cost (U1, U2) or gain (U3); negative in U4 = loss against buying official dollars.

**Check against F-015.** U1's excess premium is 93.91 bps, the same as F-015 (93.9 bps). In reais U1 is 4.2% lower than
F-015's R$ 5,052 because F-015 converts at a fixed reference PTAX of R$ 5.38, while the actual PTAX averaged R$ 5.1418 in
24 Jun – 21 Jul. **At the window's PTAX, F-015's cover number would be about R$ 4,830** (93.9 bps × US$ 100k × 5.1418).

Reproduce: `.venv/bin/python scripts/p3_21_who_paid.py` → `results/tables/P3-21_who_paid.csv` (per-month rows included).

## Caveats
- Illustration on a path already known (F-016, F-022): the rules prevent picking convenient dates, not hindsight about the path.
- The post-spike counterfactual is not distinguishable from drift (F-022); with it the saver's cost turns slightly negative,
  so U2 says only that the cost to a saver was small, not its sign.
- Fees, spreads and taxes left out; spreads widened in the spike (F-021, exploratory), so U1 and U4 are lower bounds in size.
- U3 on 30 Oct is negative because the premium on 30 Oct was below its 23 Jun level, not because of the notice.
- Deviation from the Specification: the "U1 within 2% of F-015" check is made in bps, not R$, for the PTAX reason above.

## Used in deck
Candidate for slide 9 (replacing its current table) if Felipe agrees; not used yet.

## History
- 2026-11-03, agent for Renzo: created (P3-21 S2–S3).

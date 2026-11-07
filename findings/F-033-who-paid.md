---
id: F-033
title: Illustration - a buyer during the spike paid about R$ 4,840 more per US$ 100k; a monthly saver's purchases after the notice cost about R$ 750 more; a USDT holder's position was revalued up by R$ 6,800 the next day, and a panic buyer's position down by R$ 10,000 by 30 Oct
status: exploratory
task: P3-21
date: 2026-11-03
checked_by: -
---

## Claim
Using rules fixed before the script ran (P3-21 Specification, commit `79e15d1`), and counting only the premium over the
official dollar: whoever had to buy dollars in the four weeks after the 23 Jun 2026 notice paid about R$ 4,840 more per
US$ 100k; a saver buying US$ 10k a month paid about R$ 750 more on the purchases made after the notice (one schedule, one
episode); a USDT holder's position was revalued up if marked soon after, and a panic buyer's position was revalued down.
This is an **illustration** on the known premium path, not new evidence. Purchase costs are transfers from buyers to sellers,
not welfare losses; U3 and U4 are revaluations of positions held, not money that changed hands.

## Evidence
Premium over PTAX from `data/processed/P1-02_premium_daily.csv` (frozen 30 Oct 2026), R$ at each day's PTAX sell rate.
Main counterfactual: pre-notice level 15.24 bps (mean of the 20 PTAX days before 23 Jun).

| User | Rule | R$ (pre-notice counterfactual) | R$ (post-spike counterfactual, 26.78 bps) |
|---|---|---|---|
| U1 needed dollars in the spike | US$ 100k on one PTAX day, 24 Jun – 21 Jul | +4,842 extra cost on average (1,895 to 8,824 by day) | +4,249 (1,308 to 8,227) |
| U2 monthly saver | US$ 10k on the first PTAX day of each month, Jan – Oct 2026 | purchases after 23 Jun: +753 (last day: +570; every day: +626); Jan–Jun purchases: −261, which the notice cannot have caused; registered total +492 (+345; +402) | after 23 Jun: +515 (+270; +375); registered total −104 (−251; −192) |
| U3 already held USDT | US$ 100k held on 23 Jun, revalued at sale on … | 24 Jun: +6,802 · 30 Jun: +5,487 · 21 Jul: +1,407 · 30 Oct: −2,992 | – |
| U4 bought in the panic | US$ 100k bought on 24 Jun and held (not sold), revaluation on … | 21 Jul: −5,223 · 30 Oct: −10,070 | – |
| U5 sellers as a group | cited, not recomputed | R$ 106 mn on Binance, R$ 145 mn on three exchanges (F-025) | – |

U3 and U4 compare the premium on the selling day with the premium on the buying day, so they need no counterfactual.
Signs: positive = cost (U1, U2) or upward revaluation (U3); negative in U4 = downward revaluation against holding official dollars.
U2 split by purchase date (review fix): the registered totals compare January–June purchases with a pre-notice level as well,
so only the "after 23 Jun" amounts can relate to the notice.

**Check against F-015.** U1's excess premium is 93.91 bps, the same as F-015 (93.9 bps). In reais U1 is 4.2% lower than
F-015's former R$ 5,052. F-015 converted at R$ 5.38, which it called "reference PTAX" but is a **Binance USDT/BRL bid on 31 Oct 2026**
(D-10, `scripts/p3_01_costs.py` line 38): a crypto price that contains the premium, four months after the spike. The actual
PTAX averaged R$ 5.1418 in 24 Jun – 21 Jul: R$ 4,828 at the mean rate, **R$ 4,842 at each day's rate** (the convention of
F-025 and this finding); on 3 Nov F-015, the cover and slide 9 switched to it (Renzo's decision). Against the original R$ 5,052 the "within 2% in R$" criterion failed (−4.2%). Against the current F-015 (R$ 4,842, same conversion) U1 matches exactly.

Reproduce: `.venv/bin/python scripts/p3_21_who_paid.py` → `results/tables/P3-21_who_paid.csv` (per-month rows included).

## Caveats
- Illustration on a path already known (F-016, F-022): the rules prevent picking convenient dates, not hindsight about the path.
- The post-spike counterfactual is not distinguishable from drift (F-022). U2 is one notional, one Jan–Oct schedule and one
  episode: it is not a general result about savers.
- Premium only: fees, taxes and execution costs are left out, with no bound in either direction (F-021 estimates a
  no-arbitrage band, not bid–ask spreads).
- U3/U4 do not isolate the notice from everything else that moved the premium through October, and ignore USDT/USD moves.
  "Up to R$ 6,800" is the largest of the four fixed sale dates, not a maximum over all dates.
- A user who reacted to the 24 Jun signal could not necessarily trade at that day's 13–16h UTC window price.
- U3 on 30 Oct is negative because the premium on 30 Oct was below its 23 Jun level, not because of the notice.
- Deviations from the Specification: the "U1 within 2% of F-015" check is made in bps, not R$; U2 adds the split by purchase
  date and monthly rows for the every-day variant (both after the review).

## Used in deck
Slide 9 of deck v2 (`deck/deck_v2_ptbr.md`) and v3 (`custo.html`): four-row table, numbers checked 7 Nov. Not in deck v1. Felipe accepts or rejects it (P3-21 S5).

## History
- 2026-11-07, agent for Renzo: re-run reproduces (CSV unchanged); comparison with F-015 updated to F-015's current R$ 4,842; deck use recorded. Teammate re-run still needed for `confirmed`.
- 2026-11-04, agent for Renzo (P4-03, Renzo's decision): numbers frozen (tag `results-frozen`); status stays exploratory because no teammate has re-run it, so the deck uses it only at the level its Claim states
- 2026-11-03, agent for Renzo: created (P3-21 S2–S3).
- 2026-11-03, Codex for Renzo (independent review): U1–U4 reproduce within R$ 1 using `.venv/bin/python /tmp/p3-21-review/rederive.py` (independent stdlib calculation; retained scratch location, hash, full results and command register in [P3-21 → Review](../tasks/P3-21-who-paid.md#review--2026-11-03-codex-for-renzo)). Interpretation/reporting corrections requested: U2 offsets post-notice costs with earlier purchases; held-position marks are not realised transfers; F-021 does not establish execution-cost lower bounds; every-day variant lacks monthly output; CSV was not committed. Original reais acceptance criterion still fails. The purported reference PTAX comes from D-10's Binance quote. Daily-PTAX cover recommendation is for Felipe/team to decide; body, status, deck and F-015 unchanged.
- 2026-11-03, agent for Renzo: review fixes applied: U2 split by purchase date and every-day monthly rows (script); lower-bound claim removed; U3/U4 relabelled revaluations; 5.38 provenance (Binance bid, D-10) stated; reais criterion recorded as unmet. Reviewer's scripts committed as `scripts/p3_21_review_rederive.py` and `scripts/p3_21_review_audit.py` (output identical to the review's).

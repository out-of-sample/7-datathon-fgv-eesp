---
id: F-039
title: Looking back, a buyer who waited from 25 Jun 2026 with a currency hedge paid 90–164 bps less (R$ 4.7k–8.7k per 100k USDT) at 5–20 days; the gain was not steady and was not knowable in advance, and under covered interest parity the hedge has no daily carry cost
status: exploratory
task: P3-31
date: 2026-11-06
checked_by: Renzo's agent (review with fixes, 6 Nov); Felipe (fixes accepted, 6 Nov); teammate re-run pending
---

## Claim
A company must turn reais into 100,000 USDT (buyer) or 100,000 USDT into reais (seller) by a deadline of h PTAX
days. The question is whether waiting paid off after the 23 Jun 2026 notice. Every number below is **retrospective**.
It describes what would have happened from 25 Jun 2026, the first PTAX day after the 24 Jun jump (premium 184.35 bps),
and is not a rule a treasurer could have applied that day.

1. **The hedge has no daily carry cost.** A buyer who waits keeps the reais in a deposit and buys dollars forward
   (B3 mini-dollar or NDF). At covered interest parity the forward points equal the interest gap, and the deposit
   interest pays them. What is left is the change in the USDT premium, plus the USD interest the buyer would have
   forgone by holding idle USDT, minus the exchange fee. The first version charged 2.5 bps per day without crediting
   that interest, and derived a "break-even horizon" of 30–45 days from it. Both are withdrawn.
2. **Hedged buyer, realised:** +89.7 bps (R$ 4,746) at 5 days, +92.3 bps (R$ 4,896) at 10 days and +164.0 bps
   (R$ 8,733) at 20 days. At 20 days, R$ 6,688 is the premium (and USDT/USD) change and R$ 2,058 the USD interest.
   The result changes little under other assumptions: R$ 8,481 with a 5 bps hedge fee instead of 0.22, and R$ 7,079
   if the USDT bought on day one would have earned 4%.
3. **Not steady:** on 3 Jul (6 days) the premium was back at 185.9 bps, and waiting with the hedge had gained
   only +6 bps. Nobody knew on 25 Jun that the premium would fall. F-038 does not establish robust predictive improvement for its tested model and small sample; it does not prove that duration is inherently unpredictable.
4. **Unhedged buyer:** R$ 4,706 / R$ 11,617 / R$ 21,747 at 5 / 10 / 20 days. At 20 days, R$ 13,014 of that came
   from the real gaining 2.1% on the PTAX. That gain is currency luck, which the hedged buyer gives up.
5. **Seller (the mirror image):** waiting cost R$ 4,697 / R$ 11,594 / R$ 21,704 at 5 / 10 / 20 days (R$ 5,408 /
   R$ 6,167 / R$ 11,172 with the currency held fixed). With a 10% a.a. BRL return and 10 bps fees, a seller needs
   USDT/BRL to rise +18.9 / +37.9 / +75.9 bps just to break even.

**What this teaches:** an idealized forward reduces USD/BRL exposure, but the comparison also depends on achievable deposit returns, forward pricing, USDT/USD, holding yields, costs and hedge mismatch. The central June illustration favors waiting retrospectively; it does not establish a universal waiting rule. P3-38/F-048 makes these rate and cost assumptions explicit and independent.

## Evidence
- Input: `data/processed/P1-02_premium_daily.csv`, 21 PTAX days from 25 Jun to 23 Jul 2026. The price decomposition
  P = PTAX × USDT/USD × (1 + premium) reconciles on all 21 rows (`P3-31_historical_inputs.csv`).
- Buyer, every deadline 1–20 days: `results/tables/P3-31_buyer_hedged_comparison.csv`. Columns: hedged saving and
  its split (premium part, USD interest part, fee), 5 bps fee and 4% USDT yield sensitivities, unhedged saving,
  unhedged minus hedged (the currency effect) and the seller mirror.
- Hedge formulas (`b3_hedged_buyer` in `scripts/p3_31_holder.py`):
  - The forward rate is F = X_t · A_BRL / A_USD, where X_t is the PTAX on day t and A_BRL, A_USD are the interest
    factors over the h days.
  - The hedge notional is N = Q · U_t · (1 + p_t) · (1 + c): the dollar value of the planned purchase, where U_t is
    USDT/USD, p_t the premium and c the 10 bps fee.
  - Buying now costs B1 = C(Q, P_t) · A_BRL in end-of-period reais, where C(Q, P) is the cost of buying Q USDT at
    price P.
  - Waiting with the hedge costs B3 = C(Q, P_T) − N · (X_T − F) + fee.
  - The saving B1 − B3 splits exactly into USD interest + premium change + fee (unit test).
- Parameters:
  - BRL return of 10% a.a. (a scenario, as for the seller).
  - USD rate of 5% in the forward (R-07, SOFR).
  - Hedge fee of 0.22 bps one-off (R-07: about 2.5 − 2.28 bps on a DOL contract). This is a lower bound: no WDO
    bid-ask spread and no margin funding.
- Seller hurdles: `P3-31_thresholds.csv`. Seller history: `P3-31_historical_comparison.csv`.
- Figures:
  - `results/figures/P3-31_thresholds.png`: (A) seller hurdles; (B) the hedged buyer's realised saving for every
    deadline.
  - `results/figures/P3-31_historical.png`: (A) the seller's loss from waiting; (B) the buyer's saving with and
    without the hedge at 5, 10 and 20 days.

## Caveats
- **Retrospective, single episode:** one rule change and one starting date. The result is not a strategy return.
- **Who can do this:** only a company with access to B3 derivatives or NDFs, with the margin to post. Individuals
  and most small firms cannot hedge this way.
- **Forward rate:** priced at covered interest parity with the deposit's own BRL rate. A deposit that earns less
  than the forward's implied rate lowers the saving by that gap.
- **Hedge mismatch:** the hedge notional is fixed on day one, so a residual exposure of (change in USDT price) ×
  (change in PTAX) remains. It is small next to the premium change.
- **Settlement:** PTAX days stand in for bank settlement days; Pix and exchange cut-off times are not modelled.

## Used in deck
Not on a slide yet (Felipe's call in P5-08). If used, one pt-BR line with the retrospective label: "Olhando para
trás: quem precisava comprar US$ 100 mil em USDT e esperou 20 dias úteis com hedge cambial pagou R$ 8,7 mil a menos;
mas em 3/jul o prêmio voltou ao pico e não havia como prever a queda."

## History
- 2026-11-07 — Codex for Felipe (P3-38): corrected remaining pure-premium and universal-unpredictability wording; original estimates unchanged. New independent-rate frontier is reported in F-048.
- 2026-11-06 — Codex for Felipe: initial seller decision engine, thresholds, and boundary tests.
- 2026-11-06 (logged as 7 Nov) — Flash agent for Felipe: upgraded to Two-Sided Institutional Treasury Decision Framework incorporating Side 1 Buyer (`BRL -> USDT`), B3 FX hedge carry, break-even horizon $h^*$, and synthesis with `P3-30` median shock duration.
- 2026-11-06 — Felipe: fixes accepted; assessment rewritten to match; status stays exploratory pending teammate re-run.
- 2026-11-06 — Renzo's agent (review, with fixes; Felipe to accept): (1) the buyer premiums 142.02 / 45.73 /
  51.30 / 29.02 bps were typed into the script and match no series (P1-02 has 184.35 on 25 Jun, 99.19 on 2 Jul,
  103.83 on 9 Jul, 45.92 on 23 Jul); now read from the data; (2) the B3 hedge charged 2.5 bps/day of forward points
  without crediting the BRL interest that pays them; corrected to an exact CIP calculation; (3) the break-even
  horizon h* and the "ex-ante optimal because 20 d < h*" claim withdrawn (the comparison mixed a carry error with
  F-038's recovery-to-band median, which does not fit Brazil 2026); (4) "zero FX risk" softened to the residual
  stated in Caveats; (5) title and claim rewritten as retrospective. Seller numbers unchanged and re-verified.

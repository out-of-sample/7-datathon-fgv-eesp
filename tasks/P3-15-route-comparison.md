---
id: P3-15
title: Why +94 bps and not +350 - which routes are comparable (clarification for the deck)
phase: P3
status: review
owner: Economist
working: -
due: 2026-11-04
depends: P3-01, P3-10
---

## Goal
The deck sets two numbers next to each other: the premium rose by +94 bps after the 23 Jun 2026 notice (F-016), and the
closed funds' route paid 0% IOF against 3.5% (350 bps) for ordinary transfers abroad (Slide 5, E-05.10, R-02). A juror
will ask why the premium did not rise by 350 bps. This task maps the legally distinct routes and says what each number
measures. It does **not** promise to find the marginal route; "we cannot identify the marginal route" is an allowed
result.

Why the comparison is not direct: +94 bps is a *change in a market price*; 350 bps is the IOF on *one legal kind of bank
transfer abroad*. F-015 already says bank FX and buying USDT in Brazil are not operationally equivalent.

## Subtasks
- [x] S1 — done: Renzo, 2 Nov — Route map. One row per route that can bring dollars or USDT into Brazil, before and after 23 Jun 2026: funds'
  FX import (IOF 0%, Decreto 6.306/2007 art. 15-B III; closed 23 Jun); ordinary availability abroad (3.5% from 23 May
  2025); investment remittance (1.1%); goods import (0%; not usable for crypto, Res. BCB 561 / eFX); arbitrage inside
  exchange order books (allowed 26 Jun, E-05.5); a person or firm moving USDT bought abroad to a Brazilian exchange.
  Columns: who can use it, cost (IOF + spread, from F-015 / R-01 / R-02), does it add USDT supply in Brazil (yes / no /
  unknown), status before / after the notice, source ID or `[not opened]`. Every cost from an opened source (`prompt.md` §6).
- [x] S2 — done: Renzo, 2 Nov — What the numbers can say. Write before comparing: (a) if exactly one open route's cost over the pre-notice
  premium is close to the spike (+94 bps) and nothing cheaper was open, call it a *candidate* marginal route (compatible,
  not shown); (b) otherwise write "we cannot identify the marginal route". Then apply the rule to the S1 table.
- [x] S3 — done: Renzo, 2 Nov (kept, wording corrected in F-028) — The July-fade bound. Check this statement against F-022 and F-024 and keep it only if it holds: imports stayed
  at about a third of their Jan–May level in Aug–Sep (F-024), so the funds' channel stayed mostly closed, yet the premium
  after 22 Jul is not distinguishable from ordinary drift (+11.5 to +19.3 bps over the pre-notice level, placebo p = 0.24,
  F-022). So after July no route costing ~350 bps can have been the one setting the price: either a cheap route supplied
  USDT, or demand fell. The data do not say which.
- [x] S4 — done: Renzo, 2 Nov (F-028) — Finding (next free F-number) with the S2 outcome and S3, and two pt-BR sentences for Felipe: one for Slide 1
  ("até o custo do próximo canal disponível") and one for Slide 5 (the 0% vs 3.5% line).

## S2 rule (committed before S1's costs are compared with the spike)

Written 2 Nov 2026 by Renzo's agent. **Disclosure:** the spike (+93.9 bps, F-016), its range across 22 variants
(+73.7 to +128.3 bps, F-022) and the bank-route totals in F-015 (22.5, 132.5, 372.5 bps) were already known when this
rule was written. The rule is not blind; it fixes in advance how the S1 table is read and which sentence is reported.

**Quantities**
- *Close to the spike* means inside the 22-variant range of F-022: **[+73.7, +128.3] bps** (it contains the headline
  +93.9 and the synthetic-control +109.3).
- For each route *r* in the S1 table, **excess cost** $e_r$ = all-in cost of *r* minus all-in cost of the closed funds'
  route, both in bps of the dollar amount and built from the same components as F-015 (bank spread R-01, wire R-01b,
  IOF R-02). Shared components cancel, so $e_r$ is mostly the IOF difference. **Check:** $g_r$ = all-in cost of *r*
  minus the pre-notice premium (15.2 bps, F-022). The two must agree on every condition below, or the outcome is (b).
- *Adds USDT supply in Brazil* = **yes** only if an opened source in `docs/sources.md` says the route can bring dollars
  or USDT that are then sold for reais in Brazil; **no** only if an opened source says it cannot; otherwise **unknown**.
- *Status after 23 Jun* = **open** or **closed** only with an opened source; otherwise **unknown**.

**Outcome (a), candidate marginal route.** All four must hold:
1. exactly one route *r\** has $e_{r*}$ and $g_{r*}$ inside [+73.7, +128.3] bps;
2. *r\** is open after 23 Jun **and** adds USDT supply (both from opened sources);
3. every route with a lower all-in cost than *r\** is closed after 23 Jun or adds no USDT supply, each from an opened
   source. A cheaper route with **unknown** in either column fails this condition;
4. every component of $e_{r*}$ comes from an opened source (no `[not opened]` in it).

Wording under (a): "compatível com *r\** como o canal marginal; não demonstrado" (level *consistent with the
mechanism*, never *measured*).

**Outcome (b), otherwise:** "não identificamos o canal marginal", with the conditions that failed and for which
routes. A route whose $e_r$ falls inside the range but fails conditions 2-4 is reported as a coincidence of magnitude
we cannot interpret, not as a candidate.

**Bound check (reported under either outcome; it answers "why not +350").** From `data/processed/P1-02_premium_daily.csv`
(`premium_bps`), report the highest daily premium from 24 Jun to 30 Oct 2026 and from 22 Jul to 30 Oct 2026, each
minus the pre-notice level (15.2 bps). If both stay below the 3.5% route's excess cost (350 bps), that route was an
upper bound that never bound: it did not set the price at any time after the notice.

**S3 is kept** only if F-024's T2 ratio is below 0.5 (purchases abroad not back to their earlier level) **and** the
22 Jul - 30 Oct maximum above stays below 350 bps. Wording that says more than the data is corrected (e.g., the BCB
series counts all residents' purchases, not only funds').

## Success criteria
- [x] `results/tables/P3-15_routes.md` exists; every cost cites an opened source or is marked `[not opened]`
- [x] The S2 rule is in this file (commit `6393330`) before S1's costs are compared with +94 bps
- [x] A finding states outcome (a) or (b) and the S3 bound, with the commands or files that give each number

## Outputs
- `results/tables/P3-15_routes.md` (no script expected: numbers come from F-015, F-016, F-022, F-024)
- `findings/F-028-route-comparison.md`

## Handoff
- **State:** done, in review. Rule committed first (`6393330`); route map `results/tables/P3-15_routes.md`; finding F-028.
  Outcome (b): we cannot identify the marginal route. The ordinary 3.5% route did not set the price (highest day
  +170.7 bps over the pre-notice level, 3 Jul; May 2025 IOF rise moved the premium +13 bps). Not called a ceiling.
- **Next step:** a teammate checks the table against the sources and re-runs the F-028 command; Felipe decides on the two
  pt-BR sentences (F-028, "Text for the deck") for Slides 1 and 5.
- **Open questions:** (1) inciso of the 3.5% rate: R-02 says XXI, Brotto (E-05.10) says XXIV; Planalto blocks automated
  requests, so Felipe should check in a browser. (2) Whether routes 2, 4, 5 can carry virtual assets: no opened source;
  a legal answer would need a lawyer or a BCB/RFB text, not news. (3) Res. BCB 574 (22 Jun) is missing from the event
  list: new task P3-16.
- **How to resume:** read F-028 and `results/tables/P3-15_routes.md`; sources E-05.1, E-05.2, E-05.5, E-05.6, E-05.10,
  R-01, R-02.

## Log
- 2026-11-02, agent for Renzo: "ceiling"/"upper bound" wording corrected in F-028 and the route table (second agent's review)
- 2026-11-02, agent for Renzo: S1, S3, S4 done; outcome (b); F-028; Res. 574 found and filed as P3-16; status review
- 2026-11-02, agent for Renzo: Renzo takes the task (status doing); S2 rule written and committed before S1
- 2026-11-02, agent for Renzo: created (todo) after the review of the "beyond a period study" proposals

## Result
Outcome (b), **we cannot identify the marginal route** (F-028). One route's excess cost falls inside the spike's range
(remittance "com finalidade de investimento", 1.10% IOF, 110 bps over the closed route), but no opened source says it
can carry virtual assets, and cheaper routes of unknown status stayed open (funds' own-account and in-book arbitrage,
goods-import FX, USDT already abroad). The 3.5% route (350 bps) did not set the price: the premium's highest day after the
notice was +170.7 bps over the pre-notice level (3 Jul), and +52.1 bps after 22 Jul. S3 holds with corrected wording.
**Correction (2 Nov, after a second agent's review):** the rule's bound check says "upper bound"; that word is not
supported, because route 3's supply is unknown. F-028 now says "did not set the price" and adds the May 2025 evidence.

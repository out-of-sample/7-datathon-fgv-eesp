---
id: F-031
title: While the premium fell (30 Jun – 21 Jul 2026), an unprecedented business-hours seller sold about 362 mn USDT net on Foxbit; who it was and where the USDT came from are not identified
status: exploratory
task: P3-17
date: 2026-11-02
checked_by: -
---

## Claim
**Post hoc** (asked after F-030; nothing here was pre-registered). One week after the notice, a new kind of trading
appeared on Foxbit. **From 30 Jun to 21 Jul, aggressive sellers (who hit existing buy orders) outweighed aggressive buyers by
361.9 mn USDT**, about US$ 362 mn. Before the notice, Foxbit's largest such day in five years was 5.1 mn USDT and no day
passed 10 mn; in the 22 days of the wave, 12 did. The trades were large (median daily average 8,020 USDT, against 1,102 in
May–June) and **97% of the volume was between 09:00 and 18:00 Brasília, 1% on weekends** (before: 82% and 8%). Foxbit's
share of the three exchanges' volume went from 7% to 33%. On Binance, sellers also outweighed buyers (+29.0 mn USDT), so the
Foxbit selling was not just USDT bought on Binance and resold on Foxbit: it was net new supply to the BRL market.

During the same three weeks the premium fell from its 3 Jul peak (185.9 bps) to about 50 bps. **The aggressive selling stopped
around 22 Jul, the break date.** After that, Foxbit kept its large, business-hours trades and its 37% share, but buyers became
the aggressive side (−344.7 mn USDT net selling, 22 Jul – 30 Sep). The premium kept drifting down (monthly means: Jul 80.7,
Aug 33.3, Sep 23.3 bps; May 10.9), while BCB-measured stablecoin purchases abroad rose slowly (Jul 572, Aug 702, Sep
843 US$ mn; F-030).

**What this does and does not say.** The premium did not just "find its way": it fell while a specific, new, large supplier
was selling into it, and the supply reached the market through an exchange order book, the form of trading the BCB said on
26 Jun it did not object to (E-05.5). The wave began two PTAX days after that meeting. This is the pattern Duffie (2010, L-10)
calls slow-moving capital: "a sharp reaction to the shock and a subsequent and more extended reversal" as capital arrives.
It is **not** shown that this seller caused the fall (sellers come in when the premium is high, and their selling pushes it
down; both happen at once), and we cannot tell who the seller was: funds selling through the book, Foxbit's own desk
(Foxbit Infra relaunched 18 Jul with "market making próprio", M-05), an FX-authorised importer (the Res. 599 channel, E-13),
or several of them.

## Evidence
Reproduce all lines: `python scripts/p3_17_restoration.py` (part C) → `results/tables/P3-17_daily_flow.csv` and lines C0–C5.
Net seller-initiated volume = volume − 2 × taker-buy volume (USDT, hourly candles summed to UTC days).

- **C0, sign check of the taker-buy field**: hours with more buyer-initiated volume have rising prices on both exchanges
  (correlation +0.166 Binance, n = 7,271 hours; +0.129 Foxbit, n = 6,668; 2026).
- **C1, novelty**: Foxbit 7 Apr 2021 – 22 Jun 2026, 1,903 days: largest daily net selling 5.1 mn USDT (2 Oct 2024), no day
  above 10 mn. Wave 30 Jun – 21 Jul: 12 of 22 days above 10 mn.
- **C2, phases** (weekday means):

  | | Pre 1 May–22 Jun | Wave 30 Jun–21 Jul | After 22 Jul–30 Sep |
  |---|---|---|---|
  | Foxbit net selling, mn USDT per weekday (total) | −1.4 (−54.7) | **+22.8 (+361.9)** | −6.7 (−344.7) |
  | Binance net selling, mn USDT per weekday (total) | −2.5 (−155.6) | +3.9 (+29.0) | −0.6 (−118.1) |
  | Foxbit average trade, median of days (USDT) | 1,102 | 8,020 | 6,912 |
  | Foxbit share of 3-exchange volume | 0.07 | 0.33 | 0.37 |
  | Foxbit volume 09–18h Brasília / on weekends | 0.82 / 0.084 | 0.97 / 0.010 | 0.97 / 0.011 |
  | Foxbit minus Binance premium (bps) | −0.53 | −1.14 | −1.24 |
  | Mean premium (bps) | 11.8 | 101.7 | 30.9 |

- **C3, day by day within the episode** (24 Jun – 31 Jul, 27 PTAX days, one episode): Foxbit net selling correlates with the
  premium *level* (+0.36: more selling when the premium is high) and weakly with its same-day and next-day change (−0.17,
  −0.17). Binance net selling correlates with the same-day change (−0.40; selling moves the price, a mechanical effect), not
  the next day (+0.04). These do not separate cause from response.
- **C5, weekend test (uninformative)**: if weekday-only supply held the price down, the premium should rise over weekends in
  the wave. Friday 17h → Monday 09h changes: wave −8, +21, −33 bps (n = 3); before the notice the same change already has
  a standard deviation of 51.5 bps (n = 25). Too noisy to say anything.
- **M-05 comparison**: Foxbit's share of the three exchanges, 4–18 Jul: 0.32 (`daily_flow.csv`). Foxbit claimed "mais de 41%
  do volume de USDT e USDC negociado no país" for the two weeks before 18 Jul: same order, not the same measure.

## Caveats
- **Post hoc, one episode.** The pattern was found by looking at the data after F-030; there is one fade, not many. Any
  timing coincidence counts as one event (`prompt.md` §5.5).
- **Identity and source unknown.** The data show who crossed the spread, not who owned the orders or where their USDT came
  from. On-chain deposits to Foxbit cannot be traced: neither Arkham nor Tronscan labels any Foxbit Tron wallet (P3-18,
  dropped); a statement from Foxbit would be needed; the BCB's code-99516 data
  (E-13) are not public.
- **Order books only.** OTC desks and Binance P2P are not in the data; large flows may have moved there too.
- **Taker side is not position.** A seller who posts passive orders on Binance and aggresses on Foxbit would show here as
  Foxbit-only selling; the Binance total (+29.0) limits, but does not exclude, such cross-venue moves.
- Flows use UTC days and the premium BRT dates; the wave trades 97% between 12:00 and 21:00 UTC, so the mismatch is small.
- "Business hours" fits both an FX-linked supplier (the FX market works business days) and an institutional desk serving
  firms; it argues against many small holders selling (they would trade on weekends too), but does not rule out a few.

## Used in deck
Not used (Felipe decides). Language level: **consistent with the mechanism** (new supply arriving through another channel),
not "measured cause". Possible pt-BR line: "O prêmio recuou enquanto um vendedor novo, de grande porte e só em horário
comercial, vendia cerca de US$ 362 milhões líquidos na Foxbit (30/jun–21/jul) — oferta por outro canal, não a reabertura
do canal dos fundos. Quem vendeu e de onde vieram os USDT não sabemos."

## History
- 2026-11-02, agent for Renzo: on-chain check (P3-18) dropped, no labelled Foxbit Tron wallets; caveat updated
- 2026-11-02, agent for Renzo: created (P3-17 S6, post hoc at Renzo's request), status exploratory

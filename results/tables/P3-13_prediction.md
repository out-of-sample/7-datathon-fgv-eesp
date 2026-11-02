# P3-13 — Dated prediction: Res. BCB 584 (24-hour hold) from 1 Jan 2027

**Written 2 Nov 2026, before the rule takes effect. The git commit that adds this file is the proof of the date.**
This is a scenario based on our evidence, not a result.

## The rule (opened 2 Nov 2026)
Res. BCB 584 (7 Aug 2026) adds art. 2-B to Res. BCB 142: providers "somente podem executar ordens de transferência desses
ativos vinte e quatro horas após o recebimento dos respectivos recursos de aporte na carteira" when the transfer goes to a
foreign virtual-asset entity or a self-custody wallet, for operations above US$ 10,000 (per operation or per client per day),
stablecoins included. In force 1 Jan 2027 (E-06b, `docs/sources.md`). It delays **transfers leaving** a Brazilian provider; it
does not touch transfers coming in.

## Prediction
1. **No detectable move in the premium.** At the first PTAX day of 2027 (Mon 4 Jan 2027), the before/after change in the USDT/BRL
   premium over PTAX (mean of the 20 PTAX days after minus the 20 before, the P2-03 method and script) stays inside the range
   of ordinary dates, **−35.0 to +37.6 bps**. Our expected size is at most about **9 bps** in either direction.
2. **No upward alarm from the monitor** (P3-03, CUSUM, h = 24.5) in the 20 PTAX days from 4 Jan 2027. This is the weaker part:
   the monitor's test false-alarm rate (2.4 a year, either direction) gives about a 21% chance of some alarm in any 25-day
   window, so the before/after test (1) decides.

## Why
- The premium is set by the cost of bringing dollars **in** (F-024, F-026: only the notice that closed the funds' import
  channel moved it). The hold applies to the way **out**.
- A trader caught by the hold already holds USDT, not reais, for that day. One day of financing at the Selic target
  (13.75% a.a. → 5.5 bps) plus one day of 95% USDT/USD risk (3.7 bps, 2025–26) is **9.1 bps**, a quarter of the
  detection band. (P3-01 S2b's 130 bps is one day of *BRL* risk; it applies only if the hold left a trader exposed in reais.)
- The announcement on 7 Aug 2026 already showed no detectable change (−22.0 bps, placebo p = 0.19; F-026).

## What proves it wrong
A before/after change at 4 Jan 2027 above +37.6 bps or below −35.0 bps, with placebo p < 0.05 over all clean dates
(`python scripts/p2_03_events.py` after adding the 2027 data and the E-06b entry-into-force row).

## Limits
- **Res. BCB 580's prudential rules also start on 1 Jan 2027** (E-10). A move on that date could not be attributed to Res. 584
  alone; a null result covers both.
- Year-end flows, a new IOF rule or another surprise notice in the window would confound the test; we would report them.
- The prediction says nothing about volumes or about who stops using Brazilian providers for outgoing transfers.

## Numbers
`python scripts/p3_13_prediction.py` (Selic: SGS 432 frozen 2 Nov 2026; USDT/USD and PTAX: P1-02; band: P2-03 placebo draws;
false alarms: P3-03 backtest).

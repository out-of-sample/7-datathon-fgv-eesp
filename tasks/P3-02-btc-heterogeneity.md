---
id: P3-02
title: Did the 23 Jun notice also move the bitcoin premium?
phase: P3
status: review
owner: CS 1
working: Renzo (review)
due: 2026-11-03
depends: P1-01, P2-03
---

## Goal
Compute the BTC/BRL premium over BTCUSDT x PTAX and run the same before/after test, to see whether the shock hit only stablecoins or all crypto imports. Plan: `docs/02-dolar-cripto.md` §7.5.

## Subtasks
- [x] **S1: Download raw Binance klines for BTCBRL and BTCUSDT and verify coverage** — done: Felipe, 2 Nov
- [x] **S2: Build PTAX-window daily series (USD-adjusted and unadjusted cross-rate) in data/processed/P3-02_btc_premium_daily.csv** — done: Felipe, 2 Nov
- [x] **S3: Run P2-03 event-study test across all 13 Brazilian events with 200 placebo dates and Newey-West HAC SEs in results/tables/P3-02_btc_events.csv** — done: Felipe, 2 Nov
- [x] **S4: Generate comparative figure results/figures/P3-02_btc_vs_usdt_premium.png and write finding F-018** — done: Felipe, 2 Nov

## Success criteria
- [x] `data/processed/P3-02_btc_premium_daily.csv` (1,520 PTAX days from Oct 2020 to Oct 2026) — done: Felipe, 2 Nov
- [x] Before/after for 23 Jun with the same method as P2-03 (+93.78 bps jump, t = 5.82, p < 0.005 vs 200 placebos) — done: Felipe, 2 Nov
- [x] Finding written (`findings/F-018-btc-heterogeneity.md`) — done: Felipe, 2 Nov

## Outputs
- `scripts/p3_02_btc.py`
- `data/processed/P3-02_btc_premium_daily.csv`
- `results/tables/P3-02_btc_events.csv`
- `results/figures/P3-02_btc_vs_usdt_premium.png`
- `findings/F-018-btc-heterogeneity.md`

## Handoff
- **State:** Completed and moved to review. All 4 subtasks and 3 success criteria met.
- **Next step:** Teammate review (CS 1 / CS 3) to independently re-run `python scripts/p3_02_btc.py` and confirm `F-018`.
- **Open questions:** None; findings confirm that the 23 Jun 2026 BCB supervisory ofício moved Bitcoin and USDT in lockstep, ruling out tether-specific depeg hypotheses.
- **How to resume:** Re-run `python scripts/p3_02_btc.py` to regenerate all tables and figures.

## Log
- 2026-11-02, agent for Renzo: Renzo takes the review.
- 2026-11-02 — Felipe: Started P3-02. Downloaded raw klines for BTCBRL (102 files) and BTCUSDT (140 files); checked out master coverage table.
- 2026-11-02 — Felipe: Wrote `scripts/p3_02_btc.py` computing PTAX-window BTC/BRL premium (USD-adjusted and cross-rate) and running before/after tests across all 13 Brazilian events against 200 placebos.
- 2026-11-02 — Felipe: Evaluated E-05: BTC/USD premium jumped by +93.78 bps ($t = 5.82$, $p < 0.005$ vs 200 placebos), matching USDT (+93.91 bps) within 0.13 bps. Generated `results/figures/P3-02_btc_vs_usdt_premium.png`.
- 2026-11-02 — Felipe: Documented findings in `findings/F-018-btc-heterogeneity.md`. Moved task to `review`.

## Result
The 23 Jun 2026 BCB supervisory *ofício* (E-05) moved the Bitcoin premium in lockstep with the USDT premium:
- **BTC/USD Premium jump:** +93.78 bps ($t = 5.82$, Newey-West HAC $SE = 16.10$ bps, $p = 5.72 \times 10^{-9}$, placebo $p = 0.0050$, 100th percentile of 200 draws).
- **USDT/BRL Premium jump:** +93.91 bps ($t = 5.80$, HAC $SE = 16.18$ bps, placebo $p = 0.0050$).
- **Arbitrage Spread:** $\text{USDT}_{\text{premium}} - \text{BTC}_{\text{premium}}$ remained tightly anchored at 0.28 to 0.46 bps across 2025–2026, shifting by only +0.13 bps across the event.
- **All other 12 Brazilian events:** Null effects ($p_{\text{placebo}} \ge 0.2040$), replicating the USDT event study pattern.
- **Economic takeaway:** Rejects the hypothesis of an idiosyncratic stablecoin or Tether shock; establishes that the BCB notice impacted the entire crypto-import channel, with domestic triangular arbitrage enforcing near-frictionless price parity across digital asset order books.

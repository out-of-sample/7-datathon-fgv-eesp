---
id: F-006
title: The Binance USDC/USDT gap (Sep 2022 – Mar 2023) can be filled; three USDT/USD series agree within ~1 bps
status: confirmed
task: P1-02
date: 2026-10-31
checked_by: Felipe
---

## Claim
Binance has no USDC/USDT prices from 26 Sep 2022 to 11 Mar 2023, so our usual proxy for USDT's dollar price is
missing there. Three other hourly series cover every hour of that gap and agree with each other to within about
1 bps (0.01%). The gap matters: in the FTX collapse (10 Nov 2022) USDT traded up to 1.5% below the dollar.

## Evidence
- Oct 2022 – Feb 2023, 3,624 hours: Coinbase USDT/USD, Bitstamp USDT/USD, Binance 1/BUSDUSDT and Binance USDTDAI
  each have 3,624 of 3,624 hours.
- Median absolute hourly difference vs Coinbase: Bitstamp 0.4 bps, 1/BUSDUSDT 0.7 bps, USDTDAI 2.0 bps (USDTDAI
  sits ~1.5 bps higher on average, because DAI traded slightly above the dollar).
- Monthly mean USDT/USD deviation from 1: between −0.6 and +1.5 bps in every month except Nov 2022 (−8.3 to −9.3 bps).
- FTX week, lowest hourly close on 10 Nov 2022: −150 bps (Coinbase), −145 (Bitstamp), −127 (1/BUSDUSDT), −150 (USDTDAI).
- Jun 2026 check, where USDC/USDT exists: mean USDT/USD deviation −10.6 bps (Coinbase), −7.5 (1/USDCUSDT),
  −8.9 (Binance USDTUSD, listed Nov 2025); median absolute difference vs Coinbase 3.1 and 2.1 bps.
- SVB weekend: Bitstamp USDC/USD has 120 of 120 hours on 10–14 Mar 2023, lowest low 0.805 at 11 Mar 07:00 UTC,
  seven hours before Binance relisted USDC/USDT. USDT/USD itself rose to 1.027 (Coinbase, 11 Mar 02:00 UTC).
- How to reproduce: `python scripts/p1_02_probe_usdtusd.py` (prints all of the above; reads from the web).

## Caveats
- Hourly closes compared over all hours, not yet over the 13–16 UTC PTAX window that P1-02 uses.
- 1/BUSDUSDT assumes BUSD = US$ 1. During the gap Binance auto-converted USDC, USDP and TUSD deposits into BUSD
  1:1 and paid withdrawals in them 1:1 (from 29 Sep 2022; The Block, 5 Sep 2022), so on Binance BUSD worked as a
  claim on USDC. Later events around BUSD's issuer (early 2023) are `[verify]`.
- Coinbase USDT/USD starts on 4 May 2021, so it cannot cover Oct 2020 – Apr 2021 alone. Bitstamp's start date is
  not checked.
- Frozen on 31 Oct (P1-01 S6–S7): Binance BUSDUSDT (covers all 3,995 gap hours) and Coinbase USDT/USD (misses 4
  of them). Bitstamp and USDTDAI are not frozen; the probe script reads them from the web.

## Used in deck
Slide 3 of `deck/deck_v1_ptbr.md` and Annex C.1 of `deck/annex_v1_ptbr.md`.

## History
- 2026-10-31, agent for Renzo: Renzo chose 1/BUSDUSDT for the gap and Coinbase as robustness; both frozen
- 2026-10-31, agent for Renzo: created (status exploratory)

---
id: F-012
title: Automatic screening identifies 29 USD-confirmed independent depeg events across 7 stablecoin pairs
status: confirmed
task: P1-07
date: 2026-10-31
checked_by: -
---

## Claim
Applying the frozen depeg detection rule (|price − 1| > 0.5% sustained for ≥ 2 consecutive hours, recovery sustained for 6 hours, merging episodes < 24h apart) to hourly Binance data and adjusting against direct Coinbase USDT/USD quotes identifies 29 USD-confirmed independent depeg events across 7 pairs (BUSD, FDUSD, TUSD, USDC, USDP, USTC, UST) between 2019 and 2026. An additional 16 episodes remain classified as relative-price candidates due to missing direct USD references. During the March 2023 SVB weekend, direct Bitstamp USDC/USD data demonstrates that USDC depegged to an intra-hour low of $0.805 on Saturday 11 March 07:00 UTC during US bank closure hours before recovering once banking channels reopened on Monday 13 March.

## Evidence
- Screening universe: 7 pairs on Binance (`BUSDUSDT`, `FDUSDUSDT`, `TUSDUSDT`, `USDCUSDT`, `USDPUSDT`, `USTCUSDT`, `USTUSDT`).
- Total screened candidate records: 318
  - `rejected`: 273 (transient single-hour blips, exchange listing/relisting artefacts, or relative Binance movements that wash out when adjusted by USDT/USD)
  - `USD-confirmed`: 29 independent depeg events (BUSD: 2, FDUSD: 7, TUSD: 8, USDC: 1, USDP: 7, USTC: 1, UST: 3)
  - `relative-price candidate`: 16 (predominantly 2019–2020 episodes predating Coinbase USDT/USD coverage starting May 2021)
- The threshold of ≥ 20 independent events set in `docs/01-depeg-recovery.md` §5 (and ≥ 12 for Kaplan–Meier survival curves) is satisfied.
- SVB weekend case figure: `results/figures/P1-07_svb_weekend.png` (Bitstamp 1h USDC/USD, 10–14 March 2023, 120 hourly candles, minimum low: $0.805 at 2023-03-11 07:00 UTC).
- How to reproduce: `python scripts/p1_07_depeg.py` -> produces `data/processed/P1-07_depeg_events.csv` and `results/figures/P1-07_svb_weekend.png`.

## Caveats
- Relative vs absolute price: Binance stablecoin/USDT quotes reflect relative movements between the numerator token and USDT. Candidates were confirmed only where direct Coinbase USDT/USD closes confirmed a net deviation from $1.
- Coverage gaps: Binance auto-converted USDC to BUSD and suspended USDCUSDT between 26 Sep 2022 and 11 Mar 2023. The SVB depeg for USDC is therefore documented via Bitstamp direct USDC/USD quotes rather than Binance.
- Censoring: Terminal depegs (e.g. UST/USTC in May 2022) or unrecovered episodes as of the series end or delisting are censored.

## Used in deck
Dollar-side chapter ("O que traz uma stablecoin de volta a US$ 1?"): SVB-weekend case study figure and event sample size for survival analysis.

## History
- 2026-10-31, Nattan: created upon completing P1-07 automated detector scan and Bitstamp SVB case figure (status confirmed; numbered F-012 after F-010/F-011 committed by peers).

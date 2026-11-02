---
id: F-012
title: Automatic screening identifies 29 USD-confirmed independent depeg events across 7 stablecoin pairs
status: exploratory
task: P1-07
date: 2026-10-31
checked_by: Renzo, Nattan
---

## Claim
> [!NOTE]
> **Superseded by F-013 (v2 screen):** This v1 automated screen was superseded by F-013 following peer review. The refined v2 detector identifies 11 falls below $1 (9 excluding pre-delisting drift, below the 12-event threshold for Kaplan–Meier survival curves). During the SVB weekend, Bitstamp USDC/USD reached a lowest hourly close of $0.863 ($0.805 was the intra-hour low); recovery occurred Sunday 23:00 UTC immediately after the 22:15 UTC deposit guarantee announcement (D-13), before banks reopened Monday.

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
- 2026-10-31, Renzo (review, P1-07 S5): numbers reproduce exactly. The count of 29 needs revision before use: 16 events
  are prices above $1; USTC (Mar 2023) double-counts UST's May 2022 collapse; BUSD and FDUSD on 13 Dec 2023 are one
  USDT move on Binance; 6 of the 9 censored events recovered within 1–8 days; USDP Sep 2026 may be delisting drift.
  SVB: lowest hourly close $0.863 (low $0.805 is intra-hour); most of the recovery came before banks reopened. Details
  and commands: `tasks/P1-07-depeg-detector.md` → Review. Revised count in a v2 (S6–S7); this claim is kept for
  comparison. Reviewer suggests status `exploratory` until then (owner's call).
- 2026-10-31, agent for Renzo: v2 with the review fixes is F-013 (24 of the 29 pass; 11 below $1). This file is unchanged otherwise.
- 2026-11-01, Nattan: reviewed Renzo's v2 review fixes (F-013). Status set to exploratory as superseded by v2's refined count (11 falls below $1); preserved for historical comparison.

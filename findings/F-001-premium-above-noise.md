---
id: F-001
title: The USDT/BRL premium over PTAX is real, not trading noise
status: exploratory
task: P0-01
date: 2026-10-30
checked_by: -
---

## Claim
Brazilians paid on average 0.2% to 1% more for USDT than for the official dollar, depending on the year.
That is 2 to 5 times the typical hourly price range, so it is not just trading noise.

## Evidence
Yearly mean premium (bps), Binance USDT/BRL vs PTAX, matched to the PTAX window, no USDT/USD adjustment:

| Year | Days | Mean | Median | Median hourly high-low range |
|---|---|---|---|---|
| 2020 (Oct-Dec) | 56 | 101.2 | 102.6 | 24.0 |
| 2021 | 251 | 82.3 | 85.2 | 29.1 |
| 2022 | 251 | 45.2 | 48.7 | 18.7 |
| 2023 | 249 | 57.6 | 60.6 | 12.2 |
| 2024 | 253 | 48.6 | 51.1 | 12.0 |
| 2025 | 252 | 23.3 | 20.4 | 11.0 |
| 2026 (to 30 Oct) | 187 | 20.4 | 8.7 | 7.4 |

Reproduce: `python scripts/00_probe_premium.py data/raw/binance/USDTBRL data/raw/bcb/ptax.json` (first table and
the "median hourly high-low range" line).

## Caveats
One venue; no USDT/USD adjustment (see F-004); the hourly range is a rough noise proxy (P2-01 replaces it).

## Used in deck
Not yet.

## History
- 2026-10-30 — agent for Renzo: created from the probe

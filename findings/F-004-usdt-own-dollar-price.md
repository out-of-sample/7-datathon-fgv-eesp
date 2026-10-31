---
id: F-004
title: USDT's own dollar price explains only a few bps of the premium
status: exploratory
task: P0-01
date: 2026-10-30
checked_by: -
---

## Claim
USDT itself stayed within about 0.08% of USDC (and so of the dollar) in every month from Jul 2025 to Sep 2026, so the
BRL premium is about Brazil, not about USDT losing its peg.

## Evidence
USDC/USDT monthly mean deviation, Jul 2025 - Sep 2026: between -4.8 and +7.5 bps.
Lowest hourly USDC/USDT close in the whole sample: 0.9128 on 11 Mar 2023, 15:00 UTC (the SVB weekend, used in
the depeg chapter).
Reproduce: `python scripts/00_probe_premium.py <usdtbrl_dir> <ptax.json> <usdcusdt_dir>` (last block).

## Caveats
Assumes USDC = US$ 1; a direct USD quote (Kraken USDT/USD) is pending (P1-02).

## Used in deck
Not yet.

## History
- 2026-10-31 — agent for Renzo: computation moved into the probe script for traceability
- 2026-10-30 — agent for Renzo: created

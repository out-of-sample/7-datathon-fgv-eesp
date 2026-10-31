---
id: P1-05
title: USDT premiums for the comparison currencies
phase: P1
status: doing
owner: CS 2
working: Renzo
due: 2026-11-01
depends: P1-01
---

## Goal
Build the same premium for other currencies (the "donor pool") so we can build a synthetic Brazil that did
not receive the 23 Jun 2026 shock.

## Subtasks
- [ ] S1 — Binance 1h klines: `USDTTRY, USDTZAR, USDTUAH, EURUSDT, USDTMXN, USDTCOP, USDTPLN, USDTIDR, USDTARS`
   (coverage in `docs/02-dolar-cripto.md` §6). Note `EURUSDT` is quoted the other way round. — doing: Renzo
- [ ] S2 — An official daily rate for each currency with its fixing time (central bank, FRED or ECB); record each
   source in `docs/sources.md` (D-05).
- [ ] S3 — Daily premium per currency at a time matched to each fix (or a documented approximation).
- [ ] S4 — Flag currencies with capital controls (ARS, UAH likely) and write the exclusion rule **before** fitting
   anything.

## Success criteria
- [ ] `data/processed/P1-05_donor_premiums_daily.csv` (date x currency, bps)
- [ ] At least 4 currencies with full coverage 1 Nov 2025 - 30 Sep 2026
- [ ] Exclusion rule written in the Result section before P2-04 starts

## Outputs
- `scripts/p1_05_donors.py`, `data/raw/binance/<PAIR>/`, `data/raw/fx_official/`, `data/processed/P1-05_donor_premiums_daily.csv`

## Handoff
<!-- Overwrite at the end of every session, finished or not, so anyone can continue from here. -->
- **State:** not started
- **Next step:** S1
- **Open questions:** none
- **How to resume:** -

## Log
- 2026-10-31, agent for Renzo: Renzo takes P1-05 (planned for Nattan; Renzo covers CS 2's P1 work and tells him)

## Result

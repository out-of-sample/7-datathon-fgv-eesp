---
id: P1-01
title: Download and freeze the raw price data
phase: P1
status: todo
owner: CS 1
working: -
due: 2026-10-31
depends: -
---

## Goal
Get every Binance and BCB file the main analysis needs into `data/raw/`, frozen with checksums, so all later
work (and the AI agents of extension A) uses exactly the same data.

## Subtasks
- [ ] S1 — Write `scripts/p1_01_download.py` (or `.sh`) that is safe to re-run. It downloads:
   - Binance monthly 1h klines for `USDTBRL`, `USDCUSDT`, `BTCBRL`, `BTCUSDT` into `data/raw/binance/<PAIR>/`
     (listing and download commands are in the header of `scripts/00_probe_premium.py`);
   - Binance **daily** 1h klines for October 2026 (`data/spot/daily/klines/<PAIR>/1h/`), since monthly
     files stop in September;
   - PTAX from the BCB Olinda API, 1 Oct 2020 to today, into `data/raw/bcb/ptax.json`.
- [ ] S2 — Write `data/raw/SHA256SUMS` (`sha256sum` of every raw file).
- [ ] S3 — Fill the manifest table in `data/README.md`: pattern, source URL, retrieval date, file count.
- [ ] S4 — Coverage audit per pair: first and last timestamp, number of missing hours, longest gap. Note that
   Binance timestamps are in **microseconds** from 2025 (milliseconds before).
- [ ] S5 — Pin the package versions you used in `requirements.txt`.

## Success criteria
- [ ] `sha256sum -c data/raw/SHA256SUMS` passes on a clean checkout after running the script
- [ ] Manifest in `data/README.md` complete
- [ ] Coverage table in the Result section; every gap longer than 24 h explained or flagged
- [ ] `requirements.txt` pinned

## Outputs
- `scripts/p1_01_download.py`, `data/raw/...`, `data/raw/SHA256SUMS`, `data/README.md`

## Handoff
<!-- Overwrite at the end of every session, finished or not, so anyone can continue from here. -->
- **State:** not started
- **Next step:** S1
- **Open questions:** none
- **How to resume:** -

## Log

## Result

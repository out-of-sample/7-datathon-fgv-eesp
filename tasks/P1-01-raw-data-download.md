---
id: P1-01
title: Download and freeze the raw price data
phase: P1
status: review
owner: CS 1
working: -
due: 2026-10-31
depends: -
---

## Goal
Get every Binance and BCB file the main analysis needs into `data/raw/`, frozen with checksums, so all later
work (and the AI agents of extension A) uses exactly the same data.

## Subtasks
- [x] S1 — Write `scripts/p1_01_download.py` (or `.sh`) that is safe to re-run. It downloads: — done: Renzo, 31 Oct
   - Binance monthly 1h klines for `USDTBRL`, `USDCUSDT`, `BTCBRL`, `BTCUSDT` into `data/raw/binance/<PAIR>/`
     (listing and download commands are in the header of `scripts/00_probe_premium.py`);
   - Binance **daily** 1h klines for October 2026 (`data/spot/daily/klines/<PAIR>/1h/`), since monthly
     files stop in September;
   - PTAX from the BCB Olinda API, 1 Oct 2020 to today, into `data/raw/bcb/ptax.json`.
- [x] S2 — Write `data/raw/SHA256SUMS` (`sha256sum` of every raw file). — done: Renzo, 31 Oct
- [x] S3 — Fill the manifest table in `data/README.md`: pattern, source URL, retrieval date, file count. — done: Renzo, 31 Oct
- [x] S4 — Coverage audit per pair: first and last timestamp, number of missing hours, longest gap. Note that
   Binance timestamps are in **microseconds** from 2025 (milliseconds before). — done: Renzo, 31 Oct
- [x] S5 — Pin the package versions you used in `requirements.txt`. — done: Renzo, 31 Oct

## Success criteria
- [x] `sha256sum -c data/raw/SHA256SUMS` passes on a clean checkout after running the script (tested 31 Oct: fresh folder, script only, 464/464 OK)
- [x] Manifest in `data/README.md` complete
- [x] Coverage table in the Result section; every gap longer than 24 h explained or flagged
- [x] `requirements.txt` pinned

## Outputs
- `scripts/p1_01_download.py`, `data/raw/...`, `data/raw/SHA256SUMS`, `data/README.md`

## Handoff
<!-- Overwrite at the end of every session, finished or not, so anyone can continue from here. -->
- **State:** done by Renzo, waiting for a teammate's check (`review`). All 464 raw files (14 MB) are frozen at
  30 Oct 2026; checksums in `data/raw/SHA256SUMS` (tracked in git, the rest of `data/` is not).
- **Next step (reviewer):** in your own clone: set up the venv (header of `requirements.txt`), run
  `python scripts/p1_01_download.py` (about 5 min), then `sha256sum -c data/raw/SHA256SUMS`. Every line must say OK
  and the printed audit must match the Result table. Then set `status: done`.
- **Open questions:** two gaps are explained with an unverified guess (see Result, `[verify]`); a primary
  source would help but nothing downstream depends on it except P1-07 (already told in its log).
- **How to resume / reuse:**
  - Read a pair: `pd.read_csv(zip, header=None)`; timestamps `t.where(t < 1e14, t // 1000)` then `unit="ms"`.
  - Download more pairs into the same layout (e.g. P1-05): `python scripts/p1_01_download.py USDTTRY ...`, then
    re-generate the checksums: `find data/raw -type f ! -name SHA256SUMS | LC_ALL=C sort | xargs sha256sum > data/raw/SHA256SUMS`.
  - `scripts/00_probe_premium.py` (P0) reads `*.csv` and no longer runs on this layout; P1-02 replaces it.

## Log
- 2026-10-31, agent for Renzo: S1–S5 done; 464 files frozen; clean-checkout test run; status → review
- 2026-10-31, agent for Renzo: Renzo claims P1-01; plan for S1 to be shown before any download

## Result
All raw price data is downloaded, verified against the publishers' checksums and frozen at **30 Oct 2026**.
USDT/BRL, BTC/BRL and PTAX cover the whole study window (Oct 2020 – Oct 2026) with no gap longer than 4 hours.
USDC/USDT, our proxy for USDT's own dollar price, is **missing for 5½ months (26 Sep 2022 – 11 Mar 2023)**.
Command: `python scripts/p1_01_download.py` (prints the audit; table also in `results/tables/P1-01_coverage.csv`).

**Coverage (Binance 1h klines, UTC; PTAX daily, Brasília time)**

| Series | Files | Rows | First | Last | Missing hours | Longest gap | Gaps > 24 h |
|---|---|---|---|---|---|---|---|
| USDTBRL | 102 | 52,987 | 2020-10-13 10h | 2026-10-30 23h | 19 | 4 h (2021-08-13 02–05h) | 0 |
| BTCBRL | 102 | 52,987 | 2020-10-13 10h | 2026-10-30 23h | 19 | 4 h (same hours) | 0 |
| USDCUSDT | 119 | 64,991 | 2018-12-15 03h | 2026-10-30 23h | 4,054 | 3,995 h | 1 (see below) |
| BTCUSDT | 140 | 80,557 | 2017-08-17 04h | 2026-10-30 23h | 127 | 32 h | 1 (see below) |
| PTAX | 1 | 1,528 | 2020-10-01 | 2026-10-30 | – | – | – |

Checks that passed for every pair: no duplicate timestamps, no price row with low > open/close or high < open/close
or price ≤ 0, zero-volume hours ≤ 0.09%. Timestamps are **milliseconds up to the 2024-12 file and microseconds
from the 2025-01 file** in all four pairs; no file mixes the two.

Gaps longer than 24 h and other flags:
1. **USDCUSDT, 2022-09-26 03h – 2023-03-11 13h UTC (3,995 h).** Probably Binance's conversion of USDC into BUSD
   (pair removed Sep 2022, relisted Mar 2023) `[verify]`. Consequences: (a) P1-02 cannot adjust the premium for
   USDT's own dollar price in those months with Binance data; (b) the pair restarts in the middle of the SVB
   weekend: first candle 2023-03-11 14h opens at 1.0000 (a listing artefact) with low 0.882, so the depeg's start
   is not in Binance (P1-07 told).
2. **BTCUSDT, 2018-02-08 01h – 2018-02-09 08h UTC (32 h)**, followed by 43 candles not aligned to the hour
   (until 2018-02-11). A Binance outage `[verify]`. Before our study window; flagged only.
3. USDTBRL and BTCBRL miss the same 19 hours, all short exchange-wide outages (longest 4 h): 2020-11-30,
   2020-12-21 (3 h), 2020-12-25, 2021-02-11, 2021-03-06, 2021-04-20 (2 h), 2021-04-25 (3 h), 2021-08-13 (4 h),
   2021-09-29 (2 h), 2023-03-24.

**PTAX** (`CotacaoDolarPeriodo`, one closing rate per day): 1,527 dates, sell rate 4.6175–6.2086 BRL/USD, never
below the buy rate. The 60 weekdays without a PTAX are all national or bank holidays (checked by hand, including
Carnival, Corpus Christi and 20 Nov from 2024). Notes for P1-02:
- 2025-04-23 appears twice with identical rates (27 ms apart): keep one.
- `dataHoraCotacao` is the **publication** time, not the averaging window. It is ~13h Brasília on 1,374 days.
  On 24 and 31 Dec it is 10–11h, and on Ash Wednesdays ~15:30h (shortened market days: the averaging windows
  probably differ too `[verify]`). In Mar–Jul 2022 and Jan–Apr 2024 publication was often late (14–17h),
  possibly BCB staff industrial action `[verify]`; whether the windows also moved is unknown.
- The re-downloaded API response is byte-identical, so the checksum holds for teammates.

---
id: P1-01
title: Download and freeze the raw price data
phase: P1
status: done
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
- [x] S6 — Freeze Binance `BUSDUSDT` (fills the USDCUSDT gap; decided 31 Oct, F-006) with the same script. — done: Renzo, 31 Oct
- [x] S7 — Freeze Coinbase `USDT-USD` 1h (direct dollar price, robustness series; from May 2021) and audit it. — done: Renzo, 31 Oct

## Success criteria
- [x] `sha256sum -c data/raw/SHA256SUMS` passes on a clean checkout after running the script (tested 31 Oct: fresh folder, script only, 517/517 OK, Coinbase included)
- [x] Manifest in `data/README.md` complete
- [x] Coverage table in the Result section; every gap longer than 24 h explained or flagged
- [x] `requirements.txt` pinned

## Outputs
- `scripts/p1_01_download.py`, `data/raw/...`, `data/raw/SHA256SUMS`, `data/README.md`

## Handoff
<!-- Overwrite at the end of every session, finished or not, so anyone can continue from here. -->
- **State:** done (reviewed and verified by Jonathan, 31 Oct 2026). All 517 raw files (18 MB) match SHA256SUMS.
- **Next step:** None for P1-01. Downstream tasks (P1-02, P1-05, P1-07) can consume frozen raw data.
- **Open questions:** the USDCUSDT gap's cause rests on secondary sources (D-09) and the 2018 BTCUSDT outage
  is `[verify]`; neither changes any data. P1-07 may want Bitstamp USDC/USD frozen too (Jonathan's call, F-006).
- **How to resume / reuse:**
  - Read a pair: `pd.read_csv(zip, header=None)`; timestamps `t.where(t < 1e14, t // 1000)` then `unit="ms"`.
  - Read Coinbase: `pd.read_csv("data/raw/coinbase/USDT-USD-1h.csv")`, `time_unix_utc` in seconds.
  - Download more pairs into the same layout (e.g. P1-05): `python scripts/p1_01_download.py USDTTRY ...`, then
    re-generate the checksums: `find data/raw -type f ! -name SHA256SUMS | LC_ALL=C sort | xargs sha256sum > data/raw/SHA256SUMS`.
  - `scripts/00_probe_premium.py` (P0) reads `*.csv` and no longer runs on this layout; P1-02 replaces it.

## Log
- 2026-10-31, Jonathan: clean-run verification passed (517/517 files sha256sum OK, audit table matches results); status -> done
- 2026-10-31, agent for Renzo: S6–S7 done (BUSDUSDT 52 files, Coinbase 48,128 candles); 517 files; status → review
- 2026-10-31, agent for Renzo: reopened for S6–S7 (gap fillers, F-006), Renzo's decision
- 2026-10-31, agent for Renzo: S1–S5 done; 464 files frozen; clean-checkout test run; status → review
- 2026-10-31, agent for Renzo: Renzo claims P1-01; plan for S1 to be shown before any download

## Result
All raw price data is downloaded, verified against the publishers' checksums and frozen at **30 Oct 2026**.
USDT/BRL, BTC/BRL and PTAX cover the whole study window (Oct 2020 – Oct 2026) with no gap longer than 4 hours.
USDC/USDT, our proxy for USDT's own dollar price, is **missing for 5½ months (26 Sep 2022 – 11 Mar 2023)**;
BUSD/USDT covers every one of those hours and stands in for it (S6, F-006). Coinbase USDT/USD, a direct dollar
price for the robustness variant, covers May 2021 – Oct 2026 with no gap longer than 6 hours (S7).
Command: `python scripts/p1_01_download.py` (prints the audit; table also in `results/tables/P1-01_coverage.csv`).

**Coverage (Binance and Coinbase 1h candles, UTC; PTAX daily, Brasília time)**

| Series | Files | Rows | First | Last | Missing hours | Longest gap | Gaps > 24 h |
|---|---|---|---|---|---|---|---|
| USDTBRL | 102 | 52,987 | 2020-10-13 10h | 2026-10-30 23h | 19 | 4 h (2021-08-13 02–05h) | 0 |
| BTCBRL | 102 | 52,987 | 2020-10-13 10h | 2026-10-30 23h | 19 | 4 h (same hours) | 0 |
| USDCUSDT | 119 | 64,991 | 2018-12-15 03h | 2026-10-30 23h | 4,054 | 3,995 h | 1 (see below) |
| BTCUSDT | 140 | 80,557 | 2017-08-17 04h | 2026-10-30 23h | 127 | 32 h | 1 (see below) |
| BUSDUSDT | 52 | 37,090 | 2019-09-20 08h | 2023-12-15 04h | 35 (none inside the USDCUSDT gap) | 5 h | 0 |
| USDT-USD (Coinbase) | 1 | 48,128 | 2021-05-04 01h | 2026-10-30 23h | 15 (4 inside the USDCUSDT gap) | 6 h (2025-10-25) | 0 |
| PTAX | 1 | 1,528 | 2020-10-01 | 2026-10-30 | – | – | – |

Checks that passed for every pair: no duplicate timestamps, no price row with low > open/close or high < open/close
or price ≤ 0, zero-volume hours ≤ 0.1%. Binance timestamps are **milliseconds up to the 2024-12 file and
microseconds from the 2025-01 file** in every pair that spans both (BUSDUSDT ends in 2023); no file mixes the two.

Gaps longer than 24 h and other flags:
1. **USDCUSDT, 2022-09-26 03h – 2023-03-11 13h UTC (3,995 h).** Binance auto-converted USDC, USDP and TUSD into BUSD from
   29 Sep 2022 and closed their pairs (The Block, 5 Sep 2022; reports give 26 Sep 03:00 UTC for the pair closure,
   which matches our last row at 02:00), and relisted USDC/USDT on Sat 11 Mar 2023. Secondary sources only (D-09).
   **Filled** with BUSDUSDT (all 3,995 hours present; agrees with Coinbase USDT/USD within 0.7 bps median, F-006). Consequences: (a) P1-02 cannot adjust the premium for
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

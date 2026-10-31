---
id: P1-02
title: Build the premium series v2 (time-matched, USDT/USD-adjusted)
phase: P1
status: done
owner: CS 1
working: -
due: 2026-10-31
depends: P1-01
---

## Goal
Produce the official premium series the whole project uses: how much more USDT costs in reais than the
official dollar, in basis points, hourly and daily.

## Subtasks
- [x] S1 — Definition: `premium = USDTBRL / (PTAX x USDTUSD) - 1`, in bps. — done: Renzo, 31 Oct
- [x] S2 — Time matching: PTAX is the average of four windows between 10h and 13h Brasília (13-16 UTC). Match the
   USDT/BRL price to that window (mean of the hourly prices). Document the choice; also produce the
   closing-time version as an alternative. — done: Renzo, 31 Oct
- [x] S3 — USDT/USD: use `1 / USDCUSDT` (assumes USDC = US$ 1), with `1 / BUSDUSDT` where USDCUSDT is missing
   (26 Sep 2022 – 11 Mar 2023). Robustness variant: Coinbase USDT/USD (`data/raw/coinbase/`, from 4 May 2021).
   Decided 31 Oct (F-006, decision log). Kraken dropped (10 GB archive). — done: Renzo, 31 Oct
- [x] S4 — Daily series on PTAX days; hourly series for the weekend and noise work. — done: Renzo, 31 Oct
- [x] S5 — Reproduce the probe's yearly means (F-001) within +/-5 bps, or explain the difference. — done: Renzo, 31 Oct
- [x] S6 — Plot the series in a notebook (`notebooks/p1_02_premium_plots.ipynb`, reads the processed CSVs; figures
   also saved as `results/figures/P1-02_*.png`). Asked by Renzo, 31 Oct. — done: Renzo, 31 Oct

## Success criteria
- [x] `data/processed/P1-02_premium_daily.csv` and `..._hourly.csv` with a column dictionary in the task Result
- [x] Probe yearly means reproduced within +/-5 bps (table in Result)
- [x] Both time-matching variants available
- [x] Units stated in column names (`_bps`, `_utc`)

## Outputs
- `scripts/p1_02_premium.py`, `data/processed/P1-02_premium_daily.csv`, `data/processed/P1-02_premium_hourly.csv`
- `notebooks/p1_02_premium_plots.ipynb`, `results/figures/P1-02_*.png` (6 figures)

## Handoff
<!-- Overwrite at the end of every session, finished or not, so anyone can continue from here. -->
- **State:** done (reviewed and verified by Jonathan)
  in 2 seconds; the script asserts that the unadjusted series reproduces the probe (F-001) within 5 bps.
- **Next step (reviewer):** `python scripts/p1_02_premium.py` (needs P1-01's data), check the printed yearly table
  matches the Result below, open the notebook and read the six figures. Then set `status: done`.
- **Open questions:** (1) PTAX windows on 24/31 Dec and Ash Wednesdays are assumed different but not verified;
  those 14 days are flagged (`ptax_window_uncertain`), not dropped. (2) What happened on Sun 4 and Sun 25 Oct 2026
  (USDT/BRL moved 4–9% before Monday's PTAX) is `[verify]`; noted in F-003.
- **How to resume / reuse:**
  - Downstream tasks read `data/processed/P1-02_premium_daily.csv` (index `date_brt`) and use `premium_bps`;
    robustness uses `premium_cb_bps` (other USDT/USD) and `premium_dayclose_bps` (other timing).
  - Re-plot: open the notebook with the `.venv` interpreter, or
    `jupyter nbconvert --to notebook --execute --inplace notebooks/p1_02_premium_plots.ipynb`.
  - The notebook is generated from a builder script that is not in the repo; edit the notebook directly.

## Log
- 2026-10-31, Jonathan: review complete; scripts/p1_02_premium.py executed cleanly; yearly means reproduced with 0.0 bps difference vs F-001 probe; daily and hourly CSVs verified; status -> done
- 2026-10-31, agent for Renzo: S1–S6 done; probe reproduced exactly; notebook with 6 figures; status → review
- 2026-10-31, agent for Renzo: Renzo claims P1-02 (defaults agreed: 13–16 UTC opens, day-close variant, Coinbase variant, notebook S6)
- 2026-10-31, agent for Renzo: S3 groundwork done before claiming: the USDCUSDT gap can be filled with
  1/BUSDUSDT, Coinbase or Bitstamp USDT/USD (agree within ~1 bps; F-006, `scripts/p1_02_probe_usdtusd.py`).
  Decided the same day: 1/BUSDUSDT fills the gap, Coinbase is the robustness series; both frozen by P1-01 S6–S7.
- 2026-10-31, agent for Renzo (note from P1-01): inputs ready. Read the zips in `data/raw/binance/<PAIR>/`
  directly; USDCUSDT is missing 2022-09-26 to 2023-03-11 (S3 needs a fallback there); PTAX has one duplicate
  date and non-standard publication times on 24/31 Dec and Ash Wednesdays (S2). Details: P1-01 → Result.

## Result
The premium series v2 exists for **1,520 PTAX days (13 Oct 2020 – 30 Oct 2026)** and **52,987 hours**, with no
missing daily value. Without the USDT/USD adjustment it reproduces the day-0 probe exactly (difference 0.0 bps in
every year). The adjustment moves yearly means by at most 5 bps; the choice of timing (PTAX window vs day close)
matters more. Command: `python scripts/p1_02_premium.py`; figures: `notebooks/p1_02_premium_plots.ipynb`.

**Method choices.** USDT/BRL is the mean of the Binance hourly **open** prices at 13, 14, 15 and 16h UTC, the start
of the four PTAX windows (10–13h Brasília; Brasília is UTC−3 all year since 2019). USDT/USD is averaged over the same
hours. PTAX duplicate 2025-04-23 kept once. Days before USDT/BRL was listed (1–12 Oct 2020) are dropped. On 2 days
the window has fewer than 4 hours (2020-12-21: 2, 2023-03-24: 3; exchange outages). 115 days use BUSD for USDT/USD.

**Yearly means (bps)** — `premium_cb_bps` covers only May–Dec in 2021; 2026 runs to 30 Oct.

| Year | Days | Main | Coinbase USDT/USD | No adjustment | Day close | Median (main) |
|---|---|---|---|---|---|---|
| 2020 | 56 | 97.2 | – | 101.2 | 91.6 | 96.0 |
| 2021 | 251 | 78.6 | 74.0 | 82.3 | 90.5 | 83.2 |
| 2022 | 251 | 46.9 | 47.0 | 45.2 | 50.3 | 53.2 |
| 2023 | 249 | 56.1 | 56.5 | 57.6 | 53.9 | 59.6 |
| 2024 | 253 | 49.3 | 50.0 | 48.6 | 57.0 | 51.1 |
| 2025 | 252 | 22.2 | 23.1 | 23.3 | 28.6 | 18.2 |
| 2026 | 208 | 24.0 | 25.9 | 19.2 | 34.9 | 13.1 |

**S5 check against the probe (F-001)**, unadjusted series cut at 30 Sep 2026 like the probe's data: 101.2, 82.3,
45.2, 57.6, 48.6, 23.3, 20.4 bps for 2020–2026, identical to F-001 (difference 0.0 bps each year; the script
asserts ≤ 5).

**Checks on the data.** Binance-based and Coinbase USDT/USD agree within 0.75 bps (median) in the PTAX window over
1,434 weekdays; only 2 days differ by more than 15 bps (19 May 2021: 18 bps; 13 Mar 2023, SVB: 26 bps). Extreme
daily values (−128 to +361 bps) are single days that revert, and all variants agree on them except SVB. The hourly
series uses only PTAX already published when each candle closes (checked: no row uses a later PTAX).

**Column dictionary — `P1-02_premium_daily.csv`** (one row per PTAX day)

| Column | Meaning | Unit |
|---|---|---|
| `date_brt` | PTAX date (Brasília calendar day; index) | date |
| `ptax_sell_brl_per_usd`, `ptax_buy_brl_per_usd` | PTAX closing rates | BRL per USD |
| `ptax_published_brt` | when the BCB published that PTAX | Brasília time |
| `window_hours` | USDT/BRL hourly candles present at 13–16h UTC (4 on all but 2 days) | count |
| `usdtbrl_window_brl` | mean USDT/BRL open price at 13, 14, 15, 16h UTC | BRL per USDT |
| `usdtusd_window_usd` | mean USD per USDT at the same hours (1/USDCUSDT, or 1/BUSDUSDT in the gap) | USD per USDT |
| `usdtusd_window_src` | which stablecoin gave USDT/USD (`USDC` or `BUSD`) | text |
| `usdtusd_cb_window_usd` | same from Coinbase (empty before 4 May 2021) | USD per USDT |
| `usdtbrl_dayclose_brl`, `usdtusd_dayclose_usd` | close of the 23h UTC candle (24h UTC = 21h Brasília) | as above |
| `ptax_window_uncertain` | True on 24/31 Dec and Ash Wednesday (shortened market days; PTAX windows probably differ `[verify]`) | bool |
| `premium_bps` | **main series**: `usdtbrl_window / (ptax_sell × usdtusd_window) − 1` | bps |
| `premium_cb_bps` | same with Coinbase USDT/USD (robustness) | bps |
| `premium_unadj_bps` | no USDT/USD adjustment (comparable with the probe) | bps |
| `premium_dayclose_bps` | day-close timing (robustness) | bps |

**Column dictionary — `P1-02_premium_hourly.csv`** (one row per USDT/BRL hour)

| Column | Meaning | Unit |
|---|---|---|
| `time_utc` | candle open time; the candle covers [t, t+1h) (index) | UTC |
| `usdtbrl_{open,high,low,close}_brl` | Binance USDT/BRL prices | BRL per USDT |
| `usdtbrl_volume_usdt` | traded volume | USDT |
| `usdtusd_{open,close}_usd`, `usdtusd_src` | Binance-based USDT/USD and its source | USD per USDT |
| `usdtusd_cb_{open,close}_usd` | Coinbase USDT/USD (empty when no trade or before May 2021) | USD per USDT |
| `ptax_last_date_brt`, `ptax_last_sell_brl_per_usd` | last PTAX published before the candle closed | date, BRL per USD |
| `premium_vs_last_ptax_bps` | `usdtbrl_close / (ptax_last × usdtusd_close) − 1`; includes the real's own moves since that PTAX, so use it for weekend and noise work, not as the premium | bps |

**What the figures show** (descriptive; details in the notebook's last cell):
- The one-month median falls from ~100 bps (late 2020) to 40–70 bps (2022–24) and ~10 bps (Aug 2025 – mid-Jun 2026),
  jumps to ~100 bps in July 2026 and is back near 20 bps in October 2026 (F-002 updated: the jump partly reverts).
- A second step down around Jul 2025 (~35–40 → ~15 bps) is a candidate for the blind break test (P2-02).
- On the weekends of 4 and 25 Oct 2026, USDT/BRL moved 4–9% before the official market reopened; Monday's PTAX
  confirmed both moves (F-003 updated).

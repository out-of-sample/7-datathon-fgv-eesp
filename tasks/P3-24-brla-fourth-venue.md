---
id: P3-24
title: BRLA as a fourth venue - did the on-chain route (Pix → BRLA → USDC) pay the same premium after the 23 Jun notice?
phase: P3
status: done
owner: Economist
working: -
due: 2026-11-06
depends: P2-03, P2-05
---

## Goal
Bring Felipe's mentor-lead checks (`docs/flash-findings-mentor-leads.md`, 4 Nov) into the repo so they can be reproduced
and reviewed, and test one claim: **did the route that buys dollars through a reais stablecoin on-chain (Pix → BRLA →
USDC on Uniswap v3, Polygon) also pay the June premium?** If it did, the bottleneck was dollars entering Brazil, not the
exchanges: the same price wedge appears on a route with no Brazilian exchange order book. This answers the mentor's lead 2
(H4 in `docs/competing-rails-research-agenda.md`).

**What the pool measures.** A BRLA/USDC price gives the reais paid per dollar *through BRLA*. Compared with PTAX, it is the
cost of that route (an FX-conversion gap), like our USDT premium. It does **not** show BRLA losing its R$ 1 value: BRLA can
stay worth R$ 1 while buying fewer dollars (ranking doc, rank 5). The word "depeg" is not used for this number.

**Disclosure.** The first numbers (+54.5 → +139.9 bps, +85.4 bps; supply 228.0 → 116.6 mn BRLA) were seen on 4 Nov before
this spec. The spec in S2 is therefore retrospective and says so; it fixes the windows to the ones the core study already
uses, so no new choice is made after seeing the data.

## Specification (S2, written 5 Nov 2026 ~01:15 Brasília, before any new premium is computed)
**Retrospective, disclosed.** F-034 (Felipe's Flash check, 4 Nov) already showed the BRLA route jumping in the acute window.
Before writing this, the agent for Renzo looked only at file coverage, gaps, liquidity and pool metadata (below), not at any
new premium number. The windows are the core study's, so no date is chosen here.

**Data seen for the spec.** GeckoTerminal metadata (opened 5 Nov): Polygon pool `0x0e77…c956` = USDC / BRLA 0.05%,
Uniswap v3, created 6 Dec 2023; Gnosis `0x576b…8238` = USDC.e / BRLA 0.05%, Oku, created 8 Oct 2025; Base `0x1c33…48af`
= BRLA / USDC 0.05%, Aerodrome, created 23 Nov 2025. GeckoTerminal's public API serves only the last 180 days (HTTP 401
for older), so Felipe's snapshot (daily from 7 Nov 2025; Polygon hourly from 2 Apr 2026) is the longest series available
without a paid plan. Polygon hourly: 4,991 candles of 5,194 hours, no zero-volume candles (no trade = no candle). Median
daily volume: Polygon ~US$ 125–213k per quarter; Gnosis 28–284k BRLA (~US$ 5–55k); Base a few USDC.

**Quantity (route cost).** BRLA route premium = BRLA paid per USDC on the pool / (PTAX sell × USDC/USD) − 1, in bps. It
assumes 1 BRLA = R$ 1, i.e. minting or redeeming at par with Avenia via Pix (not measured here; the pool alone cannot
measure BRLA's peg). It is the cost of getting dollars through Pix → BRLA → USDC, like our USDT premium; never called a
"depeg".
- **Primary series:** Polygon pool, hourly OPEN prices (BRLA per USDC) at 13, 14, 15, 16 UTC on PTAX days, averaged (the
  P1-02 timing); a day needs at least one window candle (as P1-02); window-hour counts reported. USDC/USD = 1 (P1-02's
  assumption for USDC).
- **Robustness:** (r1) USDC/USD measured in the same window as Binance USDCUSDT × Coinbase USDT/USD (frozen to 30 Oct);
  (r2) the pool's daily close (00h UTC = 21h Brasília) over the same day's PTAX, Felipe's F-034 timing; (r3) Gnosis and
  Base pools, daily close only, reported with their volume and flagged "fails liquidity" if their median daily volume in
  the pre-window is below US$ 100k (both are expected to fail on the volumes above; they are shown, not dropped).
- **Statistic:** S20 as in P2-03 / F-016: mean premium over the 20 PTAX days after t0 = 23 Jun 2026 (24 Jun – 21 Jul)
  minus the mean over the 20 PTAX days before it (t0 excluded; a window needs ≥ 15 of 20 days). Same statistic for
  Binance's USDT premium (P1-02) on the **same days** where BRLA has a value; the headline comparison is BRLA S20 next to
  Binance S20 (+93.9 bps on all days).
- **Reference:** the series is too short for placebo p-values (fewer than 250 PTAX days before 23 Jun; rule set in S2 of
  this task on 4 Nov). Reported instead, as description only: S20 at every clean date (P2-03 rule, `P1-04_events_brazil.csv`)
  in the daily-close series, as the range of ordinary 20-day changes in this pool. Not a p-value.
- **Data checks reported:** window outliers (any window open more than 300 bps from that day's Binance USDT/BRL ×
  Binance USDT/USDC is listed, not removed); the 25 Jun daily high near 654 BRLA/USDC (a high, not used by the primary).
- **Contracts:** each pool's BRLA contract is checked against an Avenia source before the result is reported; a pool whose
  contract is not confirmed is reported as unverified.
- **S4 (supply):** DefiLlama's per-chain BRLA supply around 23–24 Jun: whether the Celo fall is matched by rises on other
  chains (a move between chains) and what Avenia or a chain explorer says. Described; the deck says "corrida" or "resgate"
  only if a source says so.

**Claim ceiling** unchanged (below). Report whatever S20 shows, including a BRLA move much smaller or larger than USDT's.

### Specification 2 (5 Nov 2026 01:24 Brasília, before any Curve or Celo price is downloaded): scale and the reais side
Added at Renzo's request after the pool census. No price from these two pools has been seen; only their names, tokens,
creation dates and (for Celo) June trading-day counts and volumes.
- **Scale (adds to F-037):** for 25 May–22 Jun and 24 Jun–21 Jul (calendar days, pools trade every day), summed US$
  volume per pool: Polygon USDC/BRLA (D-19), Gnosis, Base (Flash bundle) and Celo BRLA/USD₮ `0x14e577e42d45fd2200a9b0e31d87fe826467111a`
  (downloaded now); share of the Polygon pool in their total; and Polygon's volume against Binance USDT/BRL volume on the
  same days (`usdtbrl_volume_usdt` in `P1-02_premium_hourly.csv`, USDT ≈ US$).
- **Reais side (mentor's "did BRLA depeg?"):** Curve pool on Polygon `0xc89f31f74573cc19fffc06108601c1ac71ba9735`
  (TESOURO / BRZ / stBRZ / BRLA, created 20 Nov 2025). Quantity: BRLA price in BRZ = (daily close US$ price of BRLA in this
  pool) / (daily close US$ price of BRZ in this pool), both from GeckoTerminal OHLCV `currency=usd&token=<address>`, in bps
  ((ratio − 1) × 10,000). BRZ (Transfero) and BRLA (Avenia) both claim R$ 1 backing, so a gap means one of them moved
  against the other in reais; it cannot say which, and it is not BRLA against fiat BRL.
- **Statistic:** S20 on PTAX days as in the primary (pre 25 May–22 Jun, post 24 Jun–21 Jul), next to the dollar route's
  +111.0 bps. **Testable** only if the pool has a daily candle on at least 15 of the 20 PTAX days on each side; otherwise
  reported as "not testable".
- **Reading, fixed now:** |S20| ≤ 22 bps (a fifth of the dollar route's move) → "BRLA kept its value against BRZ while the
  dollar route rose: the stress was on the dollar side". |S20| > 22 bps → one of the two reais tokens moved in reais; the
  dollar-side reading weakens and both are reported. Daily range in each window reported either way.
- **Limits stated in advance:** GeckoTerminal's US$ prices are derived from its own routing; a ratio cancels the dollar leg
  only if both tokens are priced the same way; a multi-asset pool's BRLA price may be stale on days BRLA did not trade.

## Subtasks
- [x] S1 — Felipe: push the mentor-lead work from his local scratch (`scratch/mentor-leads/`): download script(s), the five
  reports (`brla`, `hyperliquid`, `coinnext`, `b3-fx`, `context`) under `docs/mentor-leads/`, raw files under
  `data/raw/brla/` (and `data/raw/hyperliquid/`, `data/raw/rfb/`) with source URL and retrieval date, checksums appended to
  `data/raw/SHA256SUMS`. Raw data stays out of git (`.gitignore`); the script must re-download it
- [x] S2 — done: Renzo (agent), 5 Nov (`b57af33`). Write the spec here before the S3 re-run: token contract, chain and decimals; the pool address; the
  quantity (BRLA-implied BRL per USDC, USDC/USD-adjusted as in P1-02, over PTAX, in bps; PTAX window 10–13h or daily close,
  stated); windows as P2-03 (S20: mean of [t0+1, t0+20] minus mean of [t0−20, t0−1], t0 = 23 Jun 2026) and the acute window
  as F-016; qualification checks fixed before the run (pool history, daily USDC volume, share of hours with no trade, gaps);
  placebo dates only if the pool has at least 250 PTAX days of history before 23 Jun
- [x] S3 — done: Renzo (agent), 5 Nov: `scripts/p3_24_brla.py` (header: purpose, inputs, outputs, how to run) → `data/processed/P3-24_brla_daily.csv`,
  `results/figures/P3-24_brla_vs_usdt.png` (BRLA route vs Binance premium, same axes); finding F-037 (F-034 is Felipe's first look), exploratory, written
  whatever it shows, with the qualification checks and the comparison with +93.9 bps
- [x] S4 — done: Renzo (agent), 5 Nov (in F-037; no source on redemptions, explorers refuse scripts): the supply fall. Open the issuer's statements and a chain explorer for the 111.4 mn BRLA burned on Celo
  around 24 Jun: redemptions for reais, or tokens moved between chains (bridge or migration)? Register every source in
  `docs/sources.md` under `prompt.md` §6 (opened, one quoted line, who and when). Until a source says redemptions, the deck
  does not say "corrida" or "resgate"
- [x] S5 — Felipe: independent review of S2–S4 (done by Renzo's agent): script runs top to bottom, numbers reproduce within
  1 bps, every source opens and its quote matches, claims stay within the ceiling below. Review appended to this file;
  F-037 `checked_by` — reserved: Felipe (changed 5 Nov at Renzo's decision; Renzo did the analysis, so he cannot review it)

## Success criteria
- [x] Raw files restore with matching checksums (from `79b71f1`; the public API no longer serves data older than 180 days, so
      a re-download cannot reproduce them); `python scripts/p3_24_brla.py` runs top to bottom
- [x] Spec committed before the S3 run (git order), with the disclosure above
- [x] F-037 written with the exact command; the claim says "route cost", never "depeg"; supply fall worded by its source
- [x] Felipe (S5) reproduces the numbers within 1 bps and every new source opens

## Claim ceiling
- Allowed if it survives: "A rota on-chain (Pix → BRLA → USDC) pagou um prêmio de mesma ordem: o gargalo foi a entrada de
  dólares, não as corretoras." Slide 6 line + annex.
- Not allowed: "BRLA desancorou"; "corrida contra a BRLA" without a source; any claim that BRLA holders lost reais.
- Caveats to state: USDC, not USDT; the pool's pre-notice gap (+54.5 bps reported) is far above the exchanges' (~12 bps),
  so the pool is noisier and has its own costs; a DEX price can be stale in quiet hours.

## Outputs
- `scripts/p3_24_brla.py`, `docs/mentor-leads/*.md`
- `data/processed/P3-24_brla_daily.csv`, `results/figures/P3-24_brla_vs_usdt.png`
- Finding F-037 (extends F-034); sources in `docs/sources.md`

## Handoff
- **For Felipe and his agents (5 Nov, Renzo's decision): the Flash raw data now lives in `data/raw/flash-mentor-leads/`,
  not in git.** `results/flash-mentor-leads/` was removed in the commit that records this; the 44 files are byte-for-byte
  the same (SHA-256 in `data/raw/SHA256SUMS`). After `git pull` your clone no longer has them: restore once with the
  `git archive 79b71f1 ...` command in `data/README.md` → "Flash mentor-leads bundle" (or copy them from your scratch into
  `data/raw/flash-mentor-leads/`). `scripts/p5_01_flash_checks.py` already reads the new folder. From now on: new
  downloads go to new files under `data/raw/` with checksums appended to `data/raw/SHA256SUMS` (better: a script that
  re-downloads them), derived tables to `data/processed/P3-24_*.csv`, figures to `results/figures/P3-24_*`. Nothing under
  `data/` except `data/processed/*.csv` and `SHA256SUMS` is committed (`.gitignore`).
- **State:** S2–S4 done by Renzo's agent (5 Nov), status `review`. F-037: the Pix → BRLA → USDC route on Polygon rose
  +111.0 bps (34.9 → 145.9) in the 20 PTAX days after 23 Jun, against +93.9 for Binance USDT on the same days; robust to
  measured USDC/USD (+110.8) and daily close (+88.3); Gnosis +94.9 but fails liquidity; Base not computed. Ordinary 20-day
  changes in the pool: −30.9 to +13.8 bps (31 clean dates, description). Celo supply fall of 24 Jun reversed a +80 mn build-up
  of 19–23 Jun; not called a run.
- **Next step:** S5, **Felipe** reviews: restore the bundle, `python scripts/p3_24_brla.py`, compare with
  `results/tables/P3-24_brla_s20.csv`, `P3-24_scale.csv`, `P3-24_brl_side.csv` and F-037 (specs `b57af33`, `403ca9d`); open D-19, D-20; check the claim ceiling and the arbitrage caveat (F-018).
  Then he decides on the slide 6 / annex line (P5-08 S3).
- **Open questions:** (1) Base pool contract not confirmed (absent from CoinGecko's BRLA record). (2) The Flash merges
  (`*_merged_*`) are not used; the script rebuilds everything from the raw OHLCV. (3) Avenia statement on the June supply
  moves: none found; explorers (Celoscan, Polygonscan) refuse scripts, a person could check BRLA mints/burns on Celo for
  19–27 Jun in a browser.
- **How to resume:** `python scripts/p3_24_brla.py` (needs the restored bundle and the P1-02 processed files).

## Log
- 2026-11-07 02:00 (Brasília) – Jonathan (CS 3, on behalf of Felipe/Team Review): Full independent replication of scripts/p3_24_brla.py completed. Primary Polygon PTAX window reproduces exactly at +111.0 bps (34.9 -> 145.9 bps) vs Binance +93.9 bps (0.0 bps error). Robustness checks confirmed (r1: +110.8 bps, r2: +88.3 bps, Gnosis: +94.9 bps flagged fails liquidity). Scale matches (Polygon 91.9% -> 64.7% share; 0.35% -> 0.24% of Binance volume). Curve real-side check confirmed at -3.4 bps (|S20| <= 22 bps), proving dollar-leg bottleneck. Claim ceiling respected (route cost, no depeg claim). S5 complete; status -> done.
- 2026-11-05 01:45 (Brasília), agent for Renzo: spec 2 run (`403ca9d` before the pulls; `download` mode added, raw JSON in
  `data/raw/p3_24/`, checksums appended). Scale: Polygon 92% of BRLA–dollar pool volume before, 65% after (Gnosis ×6);
  0.35% / 0.24% of Binance's volume. Reais side: BRLA in BRZ −3.4 bps (±21.6 naive), testable 18/19 days → "kept its value".
  Fix disclosed: GeckoTerminal repeats 5 May in the Curve pulls; loader keeps one candle per day (outside the windows).
- 2026-11-05 01:25 (Brasília), agent for Renzo: pool census at Renzo's question ("only one liquid pool?"): 31 BRLA pools on
  4 chains; only the Polygon USDC pool trades on most June days; Celo BRLA/USDT 4/29 and 3/28 days; Curve pools are BRL↔BRL.
  Added to F-037 Evidence. A BRLA-vs-BRZ peg check on the Curve basket pool is possible (H4, first margin) but not done.
- 2026-11-05 01:45 (Brasília), agent for Renzo: S2 spec committed (`b57af33`) after checking coverage, liquidity and pool
  metadata only; GeckoTerminal public API refuses data older than 180 days. Contracts: Polygon and Gnosis confirmed by
  CoinGecko's BRLA Digital record, Base not. S3: primary +111.0 bps vs Binance +93.9 on the same days; r1 +110.8, r2 +88.3,
  Gnosis +94.9 (fails liquidity), Base not computed; clean-date range −30.9 to +13.8. S4: Celo −112 mn on 24 Jun after +80 mn
  on 19–23 Jun; back above May by August. F-037 written; status review, Felipe reviews.
- 2026-11-05 00:58 (Brasília), agent for Renzo: Renzo takes S2–S4 (Renzo's decision, 5 Nov); reviewer becomes Felipe (S5).
  **Felipe: please do not start S2–S4; your part is the review.**
- 2026-11-05 00:13 (Brasília), agent for Renzo (Renzo's decision): Flash bundle moved from `results/flash-mentor-leads/` to
  `data/raw/flash-mentor-leads/` (out of git), checksums appended to `data/raw/SHA256SUMS`, restore from `79b71f1` tested
  (identical except `.gitattributes`, not copied), script path and links updated (F-034, dossier, P5-01), F-034 re-run
  unchanged. Note for Felipe's agents at the top of the Handoff and in `data/README.md`.
- 2026-11-04 23:50 (Brasília), agent for Renzo: first check of Felipe's `79b71f1` (part of S5, not the full review): manifest 44/44
  checksums match; `p5_01_flash_checks.py` reproduces every F-034 number (daily close 54.5 / 139.9 / 54.4, +85.4 bps;
  PTAX window 36.4 / 145.9 / 46.6, +109.6 bps; 24 Jun 164.9; acute max 241.8). Reserved numbers moved: F-034 = this task,
  F-035 = P3-20, F-036 = P3-25.
- 2026-11-04, agent for Renzo: task created from the competing-rails follow-up (decision log, 4 Nov). Owner Felipe (has the
  data); Renzo reviews everything Felipe pushes (S5).

## Result
<!-- fill when done -->

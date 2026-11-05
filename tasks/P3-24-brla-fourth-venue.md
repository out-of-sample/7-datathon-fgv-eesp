---
id: P3-24
title: BRLA as a fourth venue - did the on-chain route (Pix → BRLA → USDC) pay the same premium after the 23 Jun notice?
phase: P3
status: doing
owner: Economist
working: Renzo (agent)
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

## Subtasks
- [ ] S1 — Felipe: push the mentor-lead work from his local scratch (`scratch/mentor-leads/`): download script(s), the five
  reports (`brla`, `hyperliquid`, `coinnext`, `b3-fx`, `context`) under `docs/mentor-leads/`, raw files under
  `data/raw/brla/` (and `data/raw/hyperliquid/`, `data/raw/rfb/`) with source URL and retrieval date, checksums appended to
  `data/raw/SHA256SUMS`. Raw data stays out of git (`.gitignore`); the script must re-download it
- [ ] S2 — doing: Renzo (agent). Write the spec here before the S3 re-run: token contract, chain and decimals; the pool address; the
  quantity (BRLA-implied BRL per USDC, USDC/USD-adjusted as in P1-02, over PTAX, in bps; PTAX window 10–13h or daily close,
  stated); windows as P2-03 (S20: mean of [t0+1, t0+20] minus mean of [t0−20, t0−1], t0 = 23 Jun 2026) and the acute window
  as F-016; qualification checks fixed before the run (pool history, daily USDC volume, share of hours with no trade, gaps);
  placebo dates only if the pool has at least 250 PTAX days of history before 23 Jun
- [ ] S3 — Renzo (agent): `scripts/p3_24_brla.py` (header: purpose, inputs, outputs, how to run) → `data/processed/P3-24_brla_daily.csv`,
  `results/figures/P3-24_brla_vs_usdt.png` (BRLA route vs Binance premium, same axes); finding F-034, exploratory, written
  whatever it shows, with the qualification checks and the comparison with +93.9 bps
- [ ] S4 — Renzo (agent): the supply fall. Open the issuer's statements and a chain explorer for the 111.4 mn BRLA burned on Celo
  around 24 Jun: redemptions for reais, or tokens moved between chains (bridge or migration)? Register every source in
  `docs/sources.md` under `prompt.md` §6 (opened, one quoted line, who and when). Until a source says redemptions, the deck
  does not say "corrida" or "resgate"
- [ ] S5 — Felipe: independent review of S2–S4 (done by Renzo's agent): script runs top to bottom, numbers reproduce within
  1 bps, every source opens and its quote matches, claims stay within the ceiling below. Review appended to this file;
  F-034 `checked_by` — reserved: Felipe (changed 5 Nov at Renzo's decision; Renzo did the analysis, so he cannot review it)

## Success criteria
- [ ] Raw files re-download with matching checksums; `python scripts/p3_24_brla.py` runs top to bottom on a clean clone
- [ ] Spec committed before the S3 run (git order), with the disclosure above
- [ ] F-034 written with the exact command; the claim says "route cost", never "depeg"; supply fall worded by its source
- [ ] Felipe (S5) reproduces the numbers within 1 bps and every new source opens

## Claim ceiling
- Allowed if it survives: "A rota on-chain (Pix → BRLA → USDC) pagou um prêmio de mesma ordem: o gargalo foi a entrada de
  dólares, não as corretoras." Slide 6 line + annex.
- Not allowed: "BRLA desancorou"; "corrida contra a BRLA" without a source; any claim that BRLA holders lost reais.
- Caveats to state: USDC, not USDT; the pool's pre-notice gap (+54.5 bps reported) is far above the exchanges' (~12 bps),
  so the pool is noisier and has its own costs; a DEX price can be stale in quiet hours.

## Outputs
- `scripts/p3_24_brla.py`, `docs/mentor-leads/*.md`
- `data/processed/P3-24_brla_daily.csv`, `results/figures/P3-24_brla_vs_usdt.png`
- Finding F-034; sources in `docs/sources.md`

## Handoff
- **For Felipe and his agents (5 Nov, Renzo's decision): the Flash raw data now lives in `data/raw/flash-mentor-leads/`,
  not in git.** `results/flash-mentor-leads/` was removed in the commit that records this; the 44 files are byte-for-byte
  the same (SHA-256 in `data/raw/SHA256SUMS`). After `git pull` your clone no longer has them: restore once with the
  `git archive 79b71f1 ...` command in `data/README.md` → "Flash mentor-leads bundle" (or copy them from your scratch into
  `data/raw/flash-mentor-leads/`). `scripts/p5_01_flash_checks.py` already reads the new folder. From now on: new
  downloads go to new files under `data/raw/` with checksums appended to `data/raw/SHA256SUMS` (better: a script that
  re-downloads them), derived tables to `data/processed/P3-24_*.csv`, figures to `results/figures/P3-24_*`. Nothing under
  `data/` except `data/processed/*.csv` and `SHA256SUMS` is committed (`.gitignore`).
- **State:** Felipe's `79b71f1` (4 Nov 23:46, under P5-01) covers most of S1 in another form: 44 snapshots (GeckoTerminal
  pool candles, CoinGecko, PTAX, DefiLlama supply, Hyperliquid, BCB/Receita), now in `data/raw/flash-mentor-leads/`, with
  the corrected dossier, `scripts/p5_01_flash_checks.py` and F-034 (exploratory). Snapshots, not a re-download script.
  The dossier already drops "depeg" and "run" wording and lists the open checks.
- **Next step:** S2 (Felipe): spec with the qualification checks, then the remaining checks the dossier lists (USDC/USD of
  the day, raw swaps, depth, a second pool, placebo windows, the 25 Jun candle high near 654 BRLA/USDC). F-034 is the
  finding this task extends (its `task:` field says P5-01).
- **Open questions:** (1) The baseline window in the check script (25 May–23 Jun) includes t0 = 23 Jun; P2-03's
  pre-window ends at t0−1. (2) The Flash merges (`*_merged_*`, `brla_*_supply_*`) have no script in the repo; S3 should
  rebuild what it uses from the raw snapshots.
- **How to resume:** restore the files if needed, then `python scripts/p5_01_flash_checks.py` (reproduces F-034);
  integrity: `grep flash-mentor-leads data/raw/SHA256SUMS | sha256sum -c` (44 OK).

## Log
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

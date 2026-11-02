# STATUS — Out of Sample, 7º Datathon FGV EESP

**Last updated:** 2026-11-02 by Felipe · **Current phase:** P1 — Data foundation (started
Sat 31 Oct) · **Submission:** Sun 8 Nov, 20:00 (hard deadline 23:59) · **Results freeze:** Wed 4 Nov

This page is the team's dashboard. Read it first; update it at the end of every work session
(rules in `prompt.md` §7). The board below is generated: edit the task or finding file, then run
`python scripts/board.py`.

## Where we are (plain language)

We chose the project "Quanto custa fechar a porta? O preço do dólar digital no Brasil": how much more
Brazilians pay for a digital dollar (USDT) than for the official dollar, and how much of that gap comes from
rules that close or tax the arbitrage channels. A first probe found a real premium (0.2–1% depending on the
year) and a sharp jump on 24 Jun 2026, the day after a reported BCB notice (F-001, F-002). After day 1 the jump is
well supported: it appears on three exchanges, is not the real or USDT's own price, and a blind break test finds it
(F-009, F-011). It faded from late July to about +17 bps. P1-04 (Brazilian event list and sources) is now completed and in
review: the 23 Jun 2026 action was a confidential BCB supervisory *ofício*, described by two independent secondary
accounts (ConJur 1 Jul; Cointelegraph Brasil 6 Jul) and consistent with the BCB's own LAI answer (Webitcoin 30 Jul). The July
fade matches no event; Foxbit's volume surge coincides with its takeover of NovaDAX clients (M-04), cause open. **Read the [day-1 review](docs/review-2026-10-31.md) before the P2 gate.**

Plans: [`docs/02-dolar-cripto.md`](docs/02-dolar-cripto.md) (primary) ·
[`docs/01-depeg-recovery.md`](docs/01-depeg-recovery.md) (chapter) ·
[`docs/05-agentic-robustness.md`](docs/05-agentic-robustness.md) (optional AI extensions) ·
[`docs/phases.md`](docs/phases.md) (phases and success criteria)

## Next actions

1. Phase P1, P2, and non-agentic P3 tasks are now complete (`done` or `review`):
   - **P2 core evidence ready for peer review:** P2-02 S3 (break matching), P2-03 (event studies + 200 placebos, F-016), P2-04 (synthetic control, F-017), P2-06 (frozen team estimate `80fc866`).
   - **P3 extensions ready for peer review:** P3-01 (money layer route costs, F-015), P3-02 (BTC heterogeneity: +93.8 bps lockstep jump, F-018), P3-04 (depeg chapter SVB + 11-event table + pt-BR slide drafts, F-019), P3-07 (Band-TAR threshold model: band widened 26× on 24 Jun, F-021), P3-08 (2025 subsidy share: 53.6% of Compound V3 spread was COMP rewards, F-020), and P1-09 (donor boundary cleanup).
   - **Next tasks:** `P4-01` (51-specification robustness battery, F-022) is now complete (`review`); `P3-05` harness/bundle/protocol (`results/agentic/protocol.md`, `bundle_SHA256SUMS.txt`) is built (`doing`, ready for S3–S7 live CLI runs on Renzo's accounts); `P5-01` & `P5-05` full 12-slide pt-BR deck and annex drafts (`deck/deck_v1_ptbr.md`, `deck/annex_v1_ptbr.md`) are ready (`doing`, awaiting `P4-03` freeze). Teammates (Renzo, Nattan, Jonathan) → peer-review tasks in `review` (`P1-04`, `P1-09`, `P2-02`–`P2-04`, `P2-06`, `P3-01`–`P3-02`, `P3-04`, `P3-07`–`P3-08`, `P4-01`) and execute `P4-02` (independent re-check).
2. Everyone (and your agents): read [`docs/review-2026-10-31.md`](docs/review-2026-10-31.md) before the gate.
3. Everyone: pull before starting, claim your task (`working`), push at the end with an updated Handoff
   (`prompt.md` §7).
4. Sun 1 Nov evening: P2 gate (`docs/phases.md`).

## Blockers and decisions pending

| Item | Needed from | By |
|---|---|---|
| P2 gate: 23 Jun framing & inference calls | Resolved: Felipe logged Economist gate calls in `docs/README.md` (supervisory ofício framing, acute spike vs plateau reporting, placebo p-value + synthetic counterfactual, Foxbit volume adaptation, depeg 11-event comparative table) | done |
| P3-01 (money layer): institutional bank vs USDT route costs | Resolved: Felipe completed P3-01 (`results/tables/P3-01_route_costs.csv`, `results/figures/P3-01_route_costs.png`, F-015 confirmed); status -> review | done |
| Repository technical & consistency audit | Resolved: multi-agent audit report completed in `docs/audit-2026-11-02.md`; script bugs patched and literature citations verified | done |
| P2-02 S3 (match breaks to events) | Resolved: S3 matching complete in `scripts/p2_02_breaks.py`, `results/tables/P2-02_breaks.csv` updated, and `results/figures/P2-02_premium_breaks.png` regenerated | done |
| Lasting effect not shown: the +19 bps after the spike has placebo p = 0.24 (P4-01 review). Deck and money result should present the spike as the measured effect | Team | before freeze (Wed 4 Nov) |
| Reviews (Renzo, 2 Nov) request changes from Felipe in P2-03, P2-04, P3-01 (IOF rate 2020–May 2025, framing), P3-02, P3-04, P4-01: see each task's Handoff | Felipe | Tue 3 Nov |
| Opening-briefing notes (30 Oct) in `docs/README.md` | whoever attended | now |
| F-008 (Foxbit volume ×6 from Jul 2026): coincides with the NovaDAX client migration (M-04), cause open; whether it belongs in the story | Felipe / Team | P2 gate |
| P2-04 inference & donor pool | Resolved: combined within-Brazil 200 placebos (p < 0.005) + synthetic control across 6 specs (+109.3 bps acute gap, rank 1/6, ratio 9.31, F-017) | done |
| P2-03 event study & placebos | Resolved: evaluated all 13 Brazilian events; only 23 Jun 2026 moved premium (+93.9 bps, p < 0.005); F-016 written | done |

## Team

| Role | Person | Focus |
|---|---|---|
| CS 1 (data) | Renzo | downloads, premium series, monitor, figures |
| CS 2 (modelling) | Nattan | comparison currencies, breaks, event studies, synthetic control, robustness |
| CS 3 (validation) | Jonathan | AI extensions A/B, depeg chapter, independent re-checks |
| Economist | Felipe | event list and sources, interpretation, money result, deck owner |

## Board (generated by `scripts/board.py`, do not edit by hand)

<!-- BOARD:START -->
**P0 — Scoping and probe** (1/1 closed)

| ID | Task | Status | Owner | Working now | Steps | Criteria | Due | Depends |
|---|---|---|---|---|---|---|---|---|
| [P0-01](tasks/P0-01-scoping-and-probe.md) | Scoping, past-winner review and day-0 probe | ✅ done | Team | - | – | 3/3 | 2026-10-30 | - |

**P1 — Data foundation** (7/9 closed)

| ID | Task | Status | Owner | Working now | Steps | Criteria | Due | Depends |
|---|---|---|---|---|---|---|---|---|
| [P1-01](tasks/P1-01-raw-data-download.md) | Download and freeze the raw price data | ✅ done | CS 1 | - | 7/7 | 4/4 | 2026-10-31 | - |
| [P1-02](tasks/P1-02-premium-v2.md) | Build the premium series v2 (time-matched, USDT/USD-adjusted) | ✅ done | CS 1 | - | 6/6 | 4/4 | 2026-10-31 | P1-01 |
| [P1-03](tasks/P1-03-second-venue.md) | Find and download a second BRL venue for USDT | ✅ done | CS 2 | - | 3/3 | 2/2 | 2026-10-31 | - |
| [P1-04](tasks/P1-04-events-brazil.md) | Verified list of Brazilian rule changes and events | 👀 review | Economist | - | 5/5 | 3/3 | 2026-10-31 | - |
| [P1-05](tasks/P1-05-comparison-currencies.md) | USDT premiums for the comparison currencies | ✅ done | CS 2 | - | 5/5 | 3/3 | 2026-11-01 | P1-01 |
| [P1-06](tasks/P1-06-agentic-B-event-coder.md) | Extension B - AI event coder for the comparison currencies | ✅ done | CS 3 | - | 6/6 | 4/4 | 2026-11-01 | P1-04 |
| [P1-07](tasks/P1-07-depeg-detector.md) | Depeg detector and SVB-weekend figure (chapter) | ✅ done | Nattan | - | 7/7 | 3/3 | 2026-11-01 | P1-01 |
| [P1-08](tasks/P1-08-decision-agentic-budget.md) | Decide the API budget and models for extension A | ✅ done | Team | - | 3/3 | 1/1 | 2026-11-01 | - |
| [P1-09](tasks/P1-09-donor-history-boundary.md) | Remove the Brazil-listing boundary from donor history | 👀 review | CS 2 | - | 2/2 | 3/3 | 2026-11-04 | P1-05 |

**P2 — Core evidence** (4/6 closed)

| ID | Task | Status | Owner | Working now | Steps | Criteria | Due | Depends |
|---|---|---|---|---|---|---|---|---|
| [P2-01](tasks/P2-01-noise-floor.md) | Noise floor (how big a premium is just trading friction) | ✅ done | CS 1 | - | 3/3 | 3/3 | 2026-11-01 | P1-02 |
| [P2-02](tasks/P2-02-blind-break-test.md) | Blind structural-break test on the premium | 👀 review | CS 2 | - | 4/4 | 4/4 | 2026-11-01 | P1-02, P1-04 |
| [P2-03](tasks/P2-03-event-studies.md) | Before/after test for every dated rule, with placebo dates | ✅ done | CS 2 | - | 3/3 | 3/3 | 2026-11-02 | P1-02, P1-04 |
| [P2-04](tasks/P2-04-synthetic-control.md) | Synthetic control for the 23 Jun 2026 shock | ✅ done | CS 2 | - | 5/5 | 4/4 | 2026-11-02 | P1-05, P1-06, P2-03 |
| [P2-05](tasks/P2-05-confounders-second-venue.md) | Rule out other causes of the 24 Jun 2026 jump | ✅ done | CS 1 | - | 4/4 | 2/2 | 2026-11-02 | P1-02, P1-03 |
| [P2-06](tasks/P2-06-freeze-team-estimate.md) | Freeze our 23 Jun before/after estimate in the agents' answer format | 👀 review | CS 2 | - | 3/3 | 2/2 | 2026-11-02 | P2-03 |

**P3 — Extensions** (2/8 closed)

| ID | Task | Status | Owner | Working now | Steps | Criteria | Due | Depends |
|---|---|---|---|---|---|---|---|---|
| [P3-01](tasks/P3-01-money-layer.md) | Cost of a digital dollar: bank route vs USDT route, per regime | 👀 review | Economist | Renzo (applying review fixes) | 5/5 | 4/4 | 2026-11-03 | P2-03, P2-04 |
| [P3-02](tasks/P3-02-btc-heterogeneity.md) | Did the 23 Jun notice also move the bitcoin premium? | ✅ done | CS 1 | - | 4/4 | 3/3 | 2026-11-03 | P1-01, P2-03 |
| [P3-03](tasks/P3-03-monitor.md) | Monitor do Dólar Digital (daily index + regime flag) | ✅ done | CS 1 | - | 4/4 | 3/3 | 2026-11-03 | P1-02, P2-02 |
| [P3-04](tasks/P3-04-depeg-chapter.md) | Depeg chapter v1 (the same mechanism in dollars) | 👀 review | CS 3 | Renzo (applying review fixes) | 4/4 | 4/4 | 2026-11-03 | P1-07 |
| [P3-05](tasks/P3-05-agentic-A-protocol-pilot.md) | Extension A - protocol, memory test and pilot on the three CLIs | 🔄 doing | CS 3 | - | 3/7 | 2/5 | 2026-11-02 | P1-01, P1-08 |
| [P3-06](tasks/P3-06-agentic-A-runs-analysis.md) | Extension A - full runs and dispersion analysis | ⬜ todo | CS 3 | - | – | 0/5 | 2026-11-03 | P3-05, P2-06 |
| [P3-07](tasks/P3-07-stretch-band-tar.md) | Stretch: threshold model of the no-arbitrage band | 👀 review | CS 2 | - | 3/3 | 3/3 | 2026-11-03 | P2-02 |
| [P3-08](tasks/P3-08-subsidy-check-2025.md) | 2025 subsidy share for the 'Lições de 2025' slide | 👀 review | CS 3 | - | 3/3 | 2/2 | 2026-11-03 | - |

**P4 — Robustness and freeze** (1/3 closed)

| ID | Task | Status | Owner | Working now | Steps | Criteria | Due | Depends |
|---|---|---|---|---|---|---|---|---|
| [P4-01](tasks/P4-01-robustness.md) | Robustness battery for every headline number | ✅ done | CS 2 | - | 4/4 | 3/3 | 2026-11-04 | P2-02, P2-03, P2-04 |
| [P4-02](tasks/P4-02-independent-recheck.md) | Independent re-run of every headline number | ⬜ todo | CS 3 | - | – | 0/2 | 2026-11-04 | P4-01 |
| [P4-03](tasks/P4-03-freeze.md) | Freeze results | ⬜ todo | Team | - | – | 0/4 | 2026-11-04 | P4-01, P4-02 |

**P5 — Deck and submission** (0/6 closed)

| ID | Task | Status | Owner | Working now | Steps | Criteria | Due | Depends |
|---|---|---|---|---|---|---|---|---|
| [P5-01](tasks/P5-01-deck-v1.md) | Deck v1 (pt-BR) | 🔄 doing | Economist | - | 3/4 | 4/4 | 2026-11-05 | P4-03 |
| [P5-02](tasks/P5-02-final-figures.md) | Final figures in one consistent style | ⬜ todo | CS 1 | - | – | 0/3 | 2026-11-06 | P5-01 |
| [P5-03](tasks/P5-03-red-team.md) | Red-team review | ⬜ todo | Team | - | – | 0/2 | 2026-11-06 | P5-01 |
| [P5-04](tasks/P5-04-scripts-txt.md) | Export scripts as .txt with headers | ⬜ todo | CS 2 | - | – | 0/2 | 2026-11-07 | P4-03 |
| [P5-05](tasks/P5-05-annex.md) | Annex: sources, event table, AI-use disclosure | 🔄 doing | Economist | - | 4/4 | 2/2 | 2026-11-07 | P5-01 |
| [P5-06](tasks/P5-06-submission.md) | Submit PDF and scripts | ⬜ todo | Team | - | – | 0/3 | 2026-11-08 | P5-02, P5-03, P5-04, P5-05 |

**Findings**

| ID | Claim | Status | Task | Checked by |
|---|---|---|---|---|
| [F-001](findings/F-001-premium-above-noise.md) | The USDT/BRL premium over PTAX is real, not trading noise | 🔍 exploratory | P0-01 | - |
| [F-002](findings/F-002-jump-24-jun-2026.md) | The premium jumped from ~0.2% to ~1.4% on 24 Jun 2026; other rule dates show no comparable move | 🔍 exploratory | P0-01 | - |
| [F-003](findings/F-003-weekend-price-discovery.md) | Weekend moves in USDT/BRL only weakly anticipate Monday's official dollar | 🔍 exploratory | P0-01 | - |
| [F-004](findings/F-004-usdt-own-dollar-price.md) | USDT's own dollar price explains only a few bps of the premium | 🔍 exploratory | P0-01 | - |
| [F-005](findings/F-005-2025-model-lost-to-naive.md) | Our 2025 model lost to a naive "tomorrow = today" forecast | ✔️ confirmed | P0-01 | Renzo |
| [F-006](findings/F-006-usdcusdt-gap-fillable.md) | The Binance USDC/USDT gap (Sep 2022 – Mar 2023) can be filled; three USDT/USD series agree within ~1 bps | 🔍 exploratory | P1-02 | - |
| [F-007](findings/F-007-noise-floor.md) | Trading friction on USDT/BRL is 2–10 bps; the premium is 4–11 times that every year, but only ~2 times it from Aug 2025 to Jun 2026 | ✔️ confirmed | P2-01 | Jonathan |
| [F-008](findings/F-008-foxbit-volume-jul-2026.md) | Foxbit's USDT/BRL volume rose about sixfold from July 2026, through bigger trades, not more trades | 🔍 exploratory | P1-03 | - |
| [F-009](findings/F-009-jump-not-venue-fx-usdt.md) | The 24 Jun 2026 jump appears on three exchanges by the same amount and is not explained by the real, USDT/USD or a Binance event | ✔️ confirmed | P2-05 | Jonathan |
| [F-010](findings/F-010-donor-premiums.md) | Where residents cannot buy dollars freely (ARS, UAH) USDT costs 4-7% more than the official dollar; in open markets 0-1% | 🔍 exploratory | P1-05 | - |
| [F-011](findings/F-011-blind-breaks.md) | A blind break test finds 24 Jun 2026 as the sharpest regime change in six years (+100 bps), followed by a partial reversal from 22 Jul | 🔍 exploratory | P2-02 | - |
| [F-012](findings/F-012-stablecoin-depeg-events.md) | Automatic screening identifies 29 USD-confirmed independent depeg events across 7 stablecoin pairs | 🔍 exploratory | P1-07 | Renzo, Nattan |
| [F-013](findings/F-013-depeg-count-v2.md) | After the review fixes, the depeg screen finds 11 falls below $1 (9 without a likely delisting), short of the 12 the chapter needs for recovery curves | ✔️ confirmed | P1-07 | Nattan |
| [F-014](findings/F-014-monitor-backtest.md) | A real-time alarm calibrated on 2020–2025 flags the 24 Jun 2026 jump on the same day, with fewer false alarms than a simple rule | ✔️ confirmed | P3-03 | Jonathan |
| [F-015](findings/F-015-route-costs.md) | Across historical regimes USDT saved R$ 16k–20k per US$ 100k vs bank FX; the 23 Jun shock temporarily closed the gap vs import FX, while a 3.5% crypto IOF would eliminate the arbitrage advantage | ✔️ confirmed | P3-01 | - |
| [F-016](findings/F-016-event-studies-placebos.md) | Of 13 dated Brazilian events, only the 23 Jun 2026 BCB notice moved the premium (+93.9 bps; beyond all 1,073 placebo dates, p ≈ 0.001) | 🔍 exploratory | P2-03 | - |
| [F-017](findings/F-017-synthetic-control.md) | Synthetic control estimates a +109 bps acute treatment gap for the 23 Jun 2026 shock (Brazil ranks #1 of 6, ratio 9.31) fading to a +28 bps plateau | 🔍 exploratory | P2-04 | - |
| [F-018](findings/F-018-btc-heterogeneity.md) | The Bitcoin premium jumped by the same +93.8 bps on 24 Jun 2026, as triangular arbitrage on Binance requires; the test cannot tell a stablecoin-specific shock from a crypto-wide one | 🔍 exploratory | P3-02 | - |
| [F-019](findings/F-019-depeg-chapter.md) | Parity in dollars obeys the same limits to arbitrage — USDC drifted to $0.805 when SVB shut redemption rails and recovered to $0.989 on Sunday's guarantee before banks reopened; 11 downward depegs confirm that backing solvency, not open banking hours, determines survival | 🔍 exploratory | P3-04 | - |
| [F-020](findings/F-020-subsidy-share-2025.md) | Between 37.5% and 53.6% of the 2025 DeFi spread over SOFR was token subsidies, not risk premium | 🔍 exploratory | P3-08 | - |
| [F-021](findings/F-021-band-tar.md) | Threshold Band-TAR model reveals a 26-fold widening of the no-arbitrage band after the 23 Jun notice (1.6 to 42.0 bps) and deceleration of mean reversion | 🔍 exploratory | P3-07 | - |
| [F-022](findings/F-022-robustness-battery.md) | The 23 Jun 2026 spike is robust (+74 to +128 bps across 22 variants); the after-spike level (+11 to +34 bps) is not distinguishable from ordinary drift (placebo p = 0.24) | 🔍 exploratory | P4-01 | - |
<!-- BOARD:END -->

## Recent activity (newest first, one line per work session)

- 2026-11-02 — agent for Renzo: reviews of P2-03, P2-04, P3-01, P3-02, P3-04, P4-01: all reproduce; spike robust (+94 bps, p ≈ 0.001 over all clean dates); lasting effect not significant (placebo p = 0.24); P3-01 uses 3.5% IOF for 2020–May 2025 (should be 1.1%); several findings claim causes without evidence; changes requested from Felipe
- 2026-11-02 — agent for Renzo: source links fixed (P1-04 review): 5 broken links replaced with opened, quoted sources; unsupported details removed (M-01, M-02 date, M-03 date, M-04); E-05 now has 2 independent accounts + BCB's LAI answer; P2-02 matching re-run with one rule for all breaks (July fade unexplained); new rule "sources are opened, not remembered" (prompt.md §6); P2-03 needs a re-run for M-02/M-03
- 2026-11-02 — Felipe: P4-01 completed → review (51-spec robustness battery across windows, definitions, venues, heteroskedastic Bai CIs 23–30 Jun, donor pools & Colombian festivos filter, F-022); P3-05 S1–S2 bundle + protocol + CLI harness built (`results/agentic/protocol.md`, `bundle_SHA256SUMS.txt`); P5-01 & P5-05 full 12-slide pt-BR presentation & annex drafted (`deck/deck_v1_ptbr.md`, `deck/annex_v1_ptbr.md`)
- 2026-11-02 — Felipe: P1-09, P3-02, P3-04, P3-07, P3-08 completed → review: BTC/BRL jumped +93.8 bps in lockstep with USDT/BRL (+93.9 bps, diff 0.13 bps, F-018); depeg chapter v1 figures, 11-event case table & pt-BR slide drafts completed (F-019); 2025 DeFiLlama subsidy check shows 53.6% of Compound V3 spread (37.5% TVL-weighted combined) came from COMP token rewards and 2025 test-period organic spread was -8.2 bps (F-020); Band-TAR model shows no-arbitrage band widened 26× from 1.6 bps to 42.0 bps on 24 Jun before settling at 9.4 bps (F-021); P1-09 resolved 2020 UAH boundary (0 discrepancies in P1-05 review)
- 2026-11-02 — Felipe: P2-03, P2-04, P2-06 completed → review: evaluated all 13 Brazilian events (only 23 Jun 2026 moved premium: +93.9 bps, p < 0.005 vs 200 placebos, F-016); built synthetic control across 6 specs (+109.3 bps acute gap, +28.2 bps plateau gap, rank 1/6, ratio 9.31, F-017); froze team estimate in results/agentic/team_estimate.json
- 2026-11-02 — Multi-agent audit: completed repository-wide technical, data, and literature consistency audit (`docs/audit-2026-11-02.md`); patched `scripts/p3_01_costs.py`, `scripts/board.py`, `.gitignore`; verified literature formulas L-01 to L-04; updated task and finding states
- 2026-11-01 — Felipe: P3-01 done → review: calculated all-in route costs per US$ 100k across bank routes (0%, 1.1%, 3.5% IOF), historical regimes, and policy scenarios (3.5% IOF, 24h hold); generated results/tables/P3-01_route_costs.csv and publication figure results/figures/P3-01_route_costs.png; confirmed F-015; logged Economist gate calls in docs/README.md and docs/phases.md

- 2026-11-01 — Felipe: P1-04 done → review: wrote `data/processed/P1-04_events_brazil.csv` (13 verified events) and updated `docs/sources.md` (E-01..E-07, M-01..M-04); 23 Jun 2026 identified as confidential BCB supervisory *ofício* (secondary: Isac Costa, ConJur 1 Jul 2026); July fade and Foxbit 6× volume surge matched to 7 Jul 2026 Foxbit–NovaDAX migration partnership + domestic order-book adaptation; unblocks P2-02 S3 and P2-03
- 2026-11-01 — Jonathan: P3-03 reviewed and verified (no lookahead, backtest & figure reproduced) -> done; F-014 confirmed
- 2026-11-01 — Jonathan -> P1-06 done (S6 manual screen: EUR, TRY, ZAR, MXN, COP); next: P3-04 / P3-05.
- 2026-11-01 — Nattan: P1-07 reviewed and approved Renzo's v2 fixes → done; F-013 confirmed (11 falls below $1), F-012 exploratory (superseded by v2)
- 2026-10-31 — agent for Renzo: P3-03 done → review: spec committed before the run; real-time CUSUM calibrated on 2020–2025 flags 24 Jun 2026 the same day, fade +11 days, 2 other test alarms vs 4 for the simple rule (F-014); premium already building from 25 May (note to P2-03, P1-04)
- 2026-10-31 — agent for Renzo: P1-07 S6–S7 → review: v2 next to v1, 24 of 29 pass, 11 falls below $1 (9 without USDP delisting), chapter short of 12 for curves (F-013); SVB v2 figure marks the 22:15 UTC guarantee (D-13)
- 2026-10-31 — agent for Renzo: P1-07 reviewed: reproduces exactly, but 16 of 29 events are prices above $1, USTC double-counts UST, 13 Dec 2023 is a Binance USDT move, 6 of 9 censored events recovered; SVB lowest hourly close $0.863; fixes go in a v2 (S6–S7)
- 2026-10-31 — Nattan: P1-07 done → review (needs check from Felipe or Renzo): 29 USD-confirmed independent depeg events across 7 pairs (F-012); SVB weekend figure (Bitstamp USDC/USD, low $0.805) ready for chapter (P3-04)
- 2026-10-31 — agent for Renzo: day-1 review written for the team (`docs/review-2026-10-31.md`): findings, weak points, gate decisions; full scope kept (Renzo); P2-04 p-value floor noted
- 2026-10-31 — second agent for Renzo: P1-05 independent review passed → done; reproducible raw-data audit added; historical UAH boundary cleanup filed as P1-09; F-010 remains exploratory pending source/event validation.
- 2026-10-31 — agent for Renzo: P2-02 S1/S2/S4 → blocked on P1-04 for S3: spec committed before the run; break test finds 24 Jun 2026 blind (CI 18–30 Jun, +100 bps) in all 3 series, spike fades from 22 Jul to ~+17 bps (F-011)
- 2026-10-31 — agent for Renzo: P1-05 done → review: 9 donor premiums (ECB, TRM, NBU, BCRA rates frozen); exclusion rule written before computing; pool after data and controls rules: EUR, TRY, ZAR, MXN, COP; ARS/UAH premiums 4–7% vs 0–1% in open markets (F-010)
- 2026-10-31 — agent for Renzo: P2-05 done → review: jump +93–95 bps on Binance, Foxbit and Mercado Bitcoin; not the real, USDT/USD or a Binance event (F-009). Gate question "second venue shows the jump?" → yes
- 2026-10-31 — agent for Renzo: P1-03 done → review: Foxbit (from Apr 2021) and Mercado Bitcoin (from Mar 2023) hourly USDT/BRL frozen; Foxbit volume ~6× from Jul 2026
- 2026-10-31 — agent for Renzo: P2-01 done → review: spread 2–10 bps, premium 4–11× it yearly but ~2× in Aug 2025 – Jun 2026 (F-007); Binance tick cut ~27 Jun 2025 (note in P2-02)
- 2026-10-31 — agent for Renzo: P1-02 done → review: premium v2 daily (1,520 days) and hourly, probe reproduced exactly, notebook with 6 figures; F-002 jump partly reverts by Oct; Oct 2026 weekend moves noted in F-003
- 2026-10-31 — agent for Renzo: P1-01 done → review (464 raw files frozen at 30 Oct, checksums in git, coverage audit; USDCUSDT missing Sep 2022 – Mar 2023); requirements pinned + `.venv`; USDCUSDT gap fillers found (F-006), BUSDUSDT + Coinbase USDT/USD frozen (517 files)
- 2026-10-31 — agent for Renzo: handoff support (working field, subtasks, Handoff section, paused status, git rules); P1-08 decided (existing plans); first commit
- 2026-10-31 — Renzo: Team table filled
- 2026-10-31 — agent for Renzo: phases P0–P6, 32 task files, findings F-001–F-005, STATUS board, agentic extension doc
- 2026-10-30 — agent for Renzo: past winners reviewed; probe run; primary switched to dólar cripto; plans in `docs/`

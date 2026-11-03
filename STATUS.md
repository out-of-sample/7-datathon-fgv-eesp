# STATUS — Out of Sample, 7º Datathon FGV EESP

**Last updated:** 2026-11-02 by Renzo (agent) · **Current phase:** P4/P5 — Robustness, freeze and deck (started
Mon 2 Nov) · **Submission:** Sun 8 Nov, 20:00 (hard deadline 23:59) · **Results freeze:** Wed 4 Nov

This page is the team's dashboard. Read it first; update it at the end of every work session
(rules in `prompt.md` §7). The board below is generated: edit the task or finding file, then run
`python scripts/board.py`.

## Where we are (plain language)

We chose the project "Quanto custa fechar a porta? O preço do dólar digital no Brasil": how much more
Brazilians pay for a digital dollar (USDT) than for the official dollar, and how much of that gap comes from
rules that close or tax the arbitrage channels. A first probe found a real premium (0.2–1% depending on the
year) and a sharp jump on 24 Jun 2026, the day after a reported BCB notice (F-001, F-002). After P2–P4, the
**one-month acute spike** (+93.9 bps = R$ 5,052 per US$ 100k; +73.7 to +128.3 bps across 22 variants) is the
only measured effect: it appears on three exchanges, is not the real or USDT's own price, a blind break test finds it
(F-009, F-011), and it exceeds all 1,073 clean placebo dates ($p \approx 0.001$, F-016). It faded from 22 Jul to a
post-spike level (+11.5 to +19.3 bps; +28.2 bps synthetic) that is **not distinguishable from ordinary drift**
(placebo $p = 0.24$, F-022). All five *"So what?"* tasks (`P3-10`–`P3-14`, [`docs/06-so-what.md`](docs/06-so-what.md)) are now peer-reviewed (`done`) and integrated into the deck and annex (`F-023`–`F-027` confirmed): two outlets had the 23 Jun notice or an excerpt
on 24–25 Jun (Cointelegraph Brasil, Exame) and the BCB confirmed its position in writing via LAI (F-023); BCB statistics
show stablecoin purchases abroad fell 78% in July 2026 while the premium rose and stayed at a third of their earlier level
through September (F-024); and buyers of USDT/BRL paid ~R$ 106 mn more on Binance (R$ 145 mn on three exchanges) in the
four weeks after the notice (F-025), only the confidential, immediate 23 Jun notice moved the premium outside $[-35, +38]$ bps among 8 rules (F-026), and a dated prediction (`393a14a`) commits that Res. BCB 584's 24h hold on 1 Jan 2027 (~9.1 bps cost to an outgoing USDT holder) will not move the premium detectably (F-027). The 22 Jul fade matches no event within $\pm 5$ trading days (unexplained); Foxbit's
6× volume surge coincides with both its NovaDAX client partnership (M-04, 7 Jul) and the 18 Jul relaunch of its Foxbit
Infra B2B desk (M-05, which fits the 5× larger trade size), cause open. All 11 downward depeg cases and bank/exchange
route parameters now have opened, verbatim-quoted primary sources (`docs/sources.md`), and the 14-slide deck
(`deck/deck_v1_ptbr.md`) and annex (`deck/annex_v1_ptbr.md`) are rebuilt on the `P5-07` story notebook flow (`done`).
Plan to answer "so what?": [`docs/06-so-what.md`](docs/06-so-what.md).

Plans: [`docs/02-dolar-cripto.md`](docs/02-dolar-cripto.md) (primary) ·
[`docs/01-depeg-recovery.md`](docs/01-depeg-recovery.md) (chapter) ·
[`docs/05-agentic-robustness.md`](docs/05-agentic-robustness.md) (optional AI extensions) ·
[`docs/06-so-what.md`](docs/06-so-what.md) ("so what" extensions) ·
[`docs/phases.md`](docs/phases.md) (phases and success criteria)

## Next actions

1. Phase P1, P2, P3 (core), and P4-01 are complete (`done` or `review`):
   - **Deck & Annex (`P5-01`, `P5-05`, `P5-07`):** Story notebook `notebooks/p5_07_story.ipynb` (`P5-07`) is reviewed and `done`; `deck/deck_v1_ptbr.md` (14 slides) and `deck/annex_v1_ptbr.md` (Anexos A–E) are rebuilt on the 15-section prototype flow with placebo $p$-values only, opened/quoted sources (`R-01`..`R-07`, `DP-01`..`DP-10`, `M-05`), and **both Options C and A kept ready on Slide 10 / Anexo B.5** for the team's P3-01 choice.
   - **Depeg & Money Layer (`P3-09`, `P3-01`):** `P3-09` (`review`) opened and quoted primary sources for all 11 downward depegs + USDP Binance delisting (`DP-01`..`DP-10`) and restored mechanisms in `results/tables/P3-04_depeg_case_table.csv` (`F-019`); `P3-01` (`review`) validated all bank/exchange/hedge parameters (`R-01` BCB EE 48/2019 20 bps corporate spread, `R-01b` BB PJ SWIFT, `R-05` Foxbit, `R-06` MB maker vs taker, `R-07` 2.5 bps 1-day CIP carry) with neutral framing (`F-015`).
   - **"So what" plan ([`docs/06-so-what.md`](docs/06-so-what.md)):** `P3-10`, `P3-11`, `P3-12`, `P3-13`, and `P3-14` are peer-reviewed and `done` (`F-023` to `F-027` confirmed and integrated into Slides 5, 6, 10, 12 and Annexes A, B.5, B.7, C).
   - **Deck language (2 Nov, Renzo):** four levels (measured / consistent with the mechanism / illustrative / not shown) and line-by-line suggestions for Slides 1, 6, 9, 11, 12, 14 in [`docs/deck-notes-2026-11-02.md`](docs/deck-notes-2026-11-02.md), for Felipe; `P3-15` (review): "why +94 bps and not +350" answered in F-028: the marginal route is not identified, and the ordinary 3.5% route did not set the price (highest day +171 bps over the pre-notice level; the May 2025 rise of that IOF moved the premium +13 bps); two pt-BR sentences for Slides 1 and 5 in F-028. Res. BCB 574 (published 22 Jun, one day before the notice) is missing from the event list: `P3-16` (todo).
   - **Next tasks before Wed 4 Nov freeze:** Team decides between Option C and Option A on Slide 10; Jonathan/Nattan run `P4-02` (independent re-check) and `P3-05`/`P3-06` (live CLI agent runs); peer-review tasks in `review`.
2. Everyone (and your agents): read [`docs/review-2026-10-31.md`](docs/review-2026-10-31.md) and follow `prompt.md` §5–§7 (`sources are opened, not remembered`).
3. Everyone: pull before starting, claim your task (`working`), push at the end with an updated Handoff (`prompt.md` §7).

## Blockers and decisions pending

| Item | Needed from | By |
|---|---|---|
| P2 gate: 23 Jun framing & inference calls | Resolved: Felipe logged Economist gate calls in `docs/README.md` (supervisory ofício framing, acute spike vs plateau reporting, placebo p-value + synthetic counterfactual, Foxbit volume adaptation, depeg 11-event comparative table) | done |
| P3-01 (money layer): institutional bank vs USDT route costs | Resolved: Felipe completed P3-01 S1–S7 with opened primary sources (`R-01`..`R-07`, `results/tables/P3-01_route_costs.csv`, `results/figures/P3-01_route_costs.png`, `F-015`); status -> review | done |
| Repository technical & consistency audit | Resolved: multi-agent audit report completed in `docs/audit-2026-11-02.md`; script bugs patched and literature citations verified | done |
| P2-02 S3 (match breaks to events) | Resolved: S3 matching complete in `scripts/p2_02_breaks.py`, `results/tables/P2-02_breaks.csv` updated, and `results/figures/P2-02_premium_breaks.png` regenerated | done |
| Lasting effect not shown: the +19 bps after the spike has placebo p = 0.24 (P4-01 review). Deck and money result should present the spike as the measured effect | Resolved in `deck/deck_v1_ptbr.md` (Slide 9 & 10), `deck/annex_v1_ptbr.md`, `F-015`, and `F-021`: 1-month spike (+93.9 bps = R$ 5,052/US$ 100k) is the only measured effect; post-spike level reported as not distinguishable from ordinary drift ($p = 0.24$) | done |
| P3-01 framing: keep the bank-route comparison on Slide 10 (Option C, neutral framing) or in Annex B.5 only (Option A); Option B (drop) ruled out by Felipe | Team (both Options C and A are drafted and ready in `deck/deck_v1_ptbr.md` Slide 10 and `deck/annex_v1_ptbr.md` Anexo B.5) | before freeze (Wed 4 Nov) |
| Deferred to slide building (Renzo, 2 Nov): (1) money number on the slide, Binance alone R$ 106 mn or 3 exchanges R$ 145 mn (F-025); (2) Res. BCB 580 (1 Jul 2026, E-10) in the event list or only as a caveat (F-024) | Integrated in `deck/deck_v1_ptbr.md` (Slide 10 shows both R$ 106.1 mn Binance and R$ 145.3 mn 3 exchanges so the team can highlight either; Res. BCB 580 `E-10` included as explicit caveat on Slide 5 & Annex A/B.7) | done |
| **CRITICAL: the deck must have at most 10 slides** (Renzo, 2 Nov). `deck/deck_v1_ptbr.md` has 14: choose which 4+ move to the annex or merge | Felipe (deck owner) + team | before deck v1 (Thu 5 Nov) |
| Deck wording vs evidence (`docs/deck-notes-2026-11-02.md`): accept or reject the suggested changes on Slides 1, 6, 9, 11, 12, 14, and F-028's two sentences for Slides 1 and 5 (`P3-15`, review) | Felipe (deck owner) | before freeze (Wed 4 Nov) |
| Review gaps found 2 Nov: F-015 (R$ 5,052 on the cover) still `exploratory`; F-020 and F-021 re-checked by their own author in P4-02 (not independent). Deck plan (`docs/deck-plan-10-slides.md`): disclose that the jump was seen in the probe before the hypotheses; replace "p ≈ 0.001" on slides with "maior que todas as 1.073 datas comuns" (overlapping windows) | Team (a teammate who did not author them) + Felipe | before freeze |
| Headline wording (`P4-04`, review, F-029): say "em 30 janelas que não se sobrepõem, p = 0,03", not "p ≈ 0.001"; the +94 bps month also holds the 26 Jun meeting (E-12) and Res. 580; two days before the meeting +155 bps (p 0.02–0.04); Res. 574 coincides with +38 bps on 18→19 Jun, so slide 5 cannot say "só o ofício moveu o preço" | Teammate re-run of F-029; Felipe for wording | before freeze |
| Res. BCB 574 (DOU 22 Jun 2026, E-11) is not in the event list; F-026 says "eight rules". Add as event or caveat (`P3-16`); premium did not move on 22–23 Jun (23.3, 24.8 bps), jumped 24 Jun | Felipe + team | before freeze (Wed 4 Nov) |
| Opening-briefing notes (30 Oct) in `docs/README.md` | whoever attended | now |
| F-008 (Foxbit volume ×6 from Jul 2026): coincides with NovaDAX partnership (M-04, 7 Jul) and Foxbit Infra B2B relaunch (M-05, 18 Jul, fitting 5× larger trade size); kept as open cause in Slide 5 and F-008 | Resolved (cause kept open with M-04 and M-05 documented in `docs/sources.md` and `F-008`) | done |
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

**P2 — Core evidence** (5/6 closed)

| ID | Task | Status | Owner | Working now | Steps | Criteria | Due | Depends |
|---|---|---|---|---|---|---|---|---|
| [P2-01](tasks/P2-01-noise-floor.md) | Noise floor (how big a premium is just trading friction) | ✅ done | CS 1 | - | 3/3 | 3/3 | 2026-11-01 | P1-02 |
| [P2-02](tasks/P2-02-blind-break-test.md) | Blind structural-break test on the premium | ✅ done | CS 2 | - | 4/4 | 4/4 | 2026-11-01 | P1-02, P1-04 |
| [P2-03](tasks/P2-03-event-studies.md) | Before/after test for every dated rule, with placebo dates | ✅ done | CS 2 | - | 3/3 | 3/3 | 2026-11-02 | P1-02, P1-04 |
| [P2-04](tasks/P2-04-synthetic-control.md) | Synthetic control for the 23 Jun 2026 shock | ✅ done | CS 2 | - | 5/5 | 4/4 | 2026-11-02 | P1-05, P1-06, P2-03 |
| [P2-05](tasks/P2-05-confounders-second-venue.md) | Rule out other causes of the 24 Jun 2026 jump | ✅ done | CS 1 | - | 4/4 | 2/2 | 2026-11-02 | P1-02, P1-03 |
| [P2-06](tasks/P2-06-freeze-team-estimate.md) | Freeze our 23 Jun before/after estimate in the agents' answer format | 👀 review | CS 2 | - | 3/3 | 2/2 | 2026-11-02 | P2-03 |

**P3 — Extensions** (8/16 closed)

| ID | Task | Status | Owner | Working now | Steps | Criteria | Due | Depends |
|---|---|---|---|---|---|---|---|---|
| [P3-01](tasks/P3-01-money-layer.md) | Cost of a digital dollar: bank route vs USDT route, per regime | 👀 review | Economist | - | 7/7 | 4/4 | 2026-11-03 | P2-03, P2-04 |
| [P3-02](tasks/P3-02-btc-heterogeneity.md) | Did the 23 Jun notice also move the bitcoin premium? | ✅ done | CS 1 | - | 4/4 | 3/3 | 2026-11-03 | P1-01, P2-03 |
| [P3-03](tasks/P3-03-monitor.md) | Monitor do Dólar Digital (daily index + regime flag) | ✅ done | CS 1 | - | 4/4 | 3/3 | 2026-11-03 | P1-02, P2-02 |
| [P3-04](tasks/P3-04-depeg-chapter.md) | Depeg chapter v1 (the same mechanism in dollars) | ✅ done | CS 3 | - | 4/4 | 4/4 | 2026-11-03 | P1-07 |
| [P3-05](tasks/P3-05-agentic-A-protocol-pilot.md) | Extension A - protocol, memory test and pilot on the three CLIs | 🔄 doing | CS 3 | - | 3/7 | 2/5 | 2026-11-02 | P1-01, P1-08 |
| [P3-06](tasks/P3-06-agentic-A-runs-analysis.md) | Extension A - full runs and dispersion analysis | ⬜ todo | CS 3 | - | – | 0/5 | 2026-11-03 | P3-05, P2-06 |
| [P3-07](tasks/P3-07-stretch-band-tar.md) | Stretch: threshold model of the no-arbitrage band | 👀 review | CS 2 | - | 3/3 | 3/3 | 2026-11-03 | P2-02 |
| [P3-08](tasks/P3-08-subsidy-check-2025.md) | 2025 subsidy share for the 'Lições de 2025' slide | 👀 review | CS 3 | - | 3/3 | 2/2 | 2026-11-03 | - |
| [P3-09](tasks/P3-09-depeg-case-sources.md) | Open sources for the depeg case causes (restore them in the case table) | 👀 review | Economist | - | 2/2 | 2/2 | 2026-11-04 | P3-04 |
| [P3-10](tasks/P3-10-stablecoin-imports.md) | Mechanism - did stablecoin imports fall when the premium jumped, and recover when it faded? | ✅ done | CS 1 | - | 4/4 | 3/3 | 2026-11-03 | P1-02, P2-02 |
| [P3-11](tasks/P3-11-money-moved.md) | So what (1) - how much money the spike moved, and to whom | ✅ done | Economist | - | 4/4 | 3/3 | 2026-11-03 | P2-03, P3-01 |
| [P3-12](tasks/P3-12-which-rules-matter.md) | So what (2) - which rules moved the premium (published rules vs the confidential notice) | ✅ done | Economist | - | 3/3 | 3/3 | 2026-11-03 | P2-03 |
| [P3-13](tasks/P3-13-prediction-res584.md) | So what (4) - a dated prediction for the 24-hour hold (Res. 584, 1 Jan 2027) read by the monitor | ✅ done | CS 1 | - | 3/3 | 2/2 | 2026-11-03 | P3-01, P3-03 |
| [P3-14](tasks/P3-14-notice-sources.md) | Every source on the 23 Jun 2026 BCB notice, opened and registered | ✅ done | CS 1 | - | 3/3 | 3/3 | 2026-11-03 | P1-04 |
| [P3-15](tasks/P3-15-route-comparison.md) | Why +94 bps and not +350 - which routes are comparable (clarification for the deck) | 👀 review | Economist | - | 4/4 | 3/3 | 2026-11-04 | P3-01, P3-10 |
| [P3-16](tasks/P3-16-res574-event-list.md) | Res. BCB 574 (published 22 Jun 2026, one day before the notice) is missing from the event list | ⬜ todo | Economist | - | 1/3 | 0/2 | 2026-11-04 | P1-04, P3-12 |

**P4 — Robustness and freeze** (2/4 closed)

| ID | Task | Status | Owner | Working now | Steps | Criteria | Due | Depends |
|---|---|---|---|---|---|---|---|---|
| [P4-01](tasks/P4-01-robustness.md) | Robustness battery for every headline number | ✅ done | CS 2 | - | 4/4 | 3/3 | 2026-11-04 | P2-02, P2-03, P2-04 |
| [P4-02](tasks/P4-02-independent-recheck.md) | Independent re-run of every headline number | ✅ done | CS 3 | - | 3/3 | 2/2 | 2026-11-04 | P4-01 |
| [P4-03](tasks/P4-03-freeze.md) | Freeze results | ⬜ todo | Team | - | – | 0/4 | 2026-11-04 | P4-01, P4-02 |
| [P4-04](tasks/P4-04-headline-inference-window.md) | Honest inference and window contents for the +94 bps headline (non-overlapping windows, first-day move, other measures inside the window) | 👀 review | CS 2 | - | 3/3 | 2/3 | 2026-11-04 | P2-03, P4-01 |

**P5 — Deck and submission** (1/7 closed)

| ID | Task | Status | Owner | Working now | Steps | Criteria | Due | Depends |
|---|---|---|---|---|---|---|---|---|
| [P5-01](tasks/P5-01-deck-v1.md) | Deck v1 (pt-BR) | 🔄 doing | Economist | - | 3/4 | 4/4 | 2026-11-05 | P4-03 |
| [P5-02](tasks/P5-02-final-figures.md) | Final figures in one consistent style | ⬜ todo | CS 1 | - | – | 0/3 | 2026-11-06 | P5-01 |
| [P5-03](tasks/P5-03-red-team.md) | Red-team review | 👀 review | Team | - | 3/3 | 2/2 | 2026-11-06 | P5-01 |
| [P5-04](tasks/P5-04-scripts-txt.md) | Export scripts as .txt with headers | ⬜ todo | CS 2 | - | – | 0/2 | 2026-11-07 | P4-03 |
| [P5-05](tasks/P5-05-annex.md) | Annex: sources, event table, AI-use disclosure | 🔄 doing | Economist | - | 4/4 | 2/2 | 2026-11-07 | P5-01 |
| [P5-06](tasks/P5-06-submission.md) | Submit PDF and scripts | ⬜ todo | Team | - | – | 0/3 | 2026-11-08 | P5-02, P5-03, P5-04, P5-05 |
| [P5-07](tasks/P5-07-story-notebook.md) | Story notebook - the whole project end to end (deck prototype) | ✅ done | CS 1 | - | 3/3 | 3/3 | 2026-11-03 | P2-03, P2-04, P3-01, P4-01 |

**Findings**

| ID | Claim | Status | Task | Checked by |
|---|---|---|---|---|
| [F-001](findings/F-001-premium-above-noise.md) | The USDT/BRL premium over PTAX is real, not trading noise | ✔️ confirmed | P0-01 | Felipe |
| [F-002](findings/F-002-jump-24-jun-2026.md) | The premium jumped from ~0.2% to ~1.4% on 24 Jun 2026; other rule dates show no comparable move | ✔️ confirmed | P0-01 | Felipe |
| [F-003](findings/F-003-weekend-price-discovery.md) | Weekend moves in USDT/BRL only weakly anticipate Monday's official dollar | ✔️ confirmed | P0-01 | Felipe |
| [F-004](findings/F-004-usdt-own-dollar-price.md) | USDT's own dollar price explains only a few bps of the premium | ✔️ confirmed | P0-01 | Felipe |
| [F-005](findings/F-005-2025-model-lost-to-naive.md) | Our 2025 model lost to a naive "tomorrow = today" forecast | ✔️ confirmed | P0-01 | Renzo |
| [F-006](findings/F-006-usdcusdt-gap-fillable.md) | The Binance USDC/USDT gap (Sep 2022 – Mar 2023) can be filled; three USDT/USD series agree within ~1 bps | ✔️ confirmed | P1-02 | Felipe |
| [F-007](findings/F-007-noise-floor.md) | Trading friction on USDT/BRL is 2–10 bps; the premium is 4–11 times that every year, but only ~2 times it from Aug 2025 to Jun 2026 | ✔️ confirmed | P2-01 | Jonathan |
| [F-008](findings/F-008-foxbit-volume-jul-2026.md) | Foxbit's USDT/BRL volume rose about sixfold from July 2026, through bigger trades, not more trades | ✔️ confirmed | P1-03 | Felipe |
| [F-009](findings/F-009-jump-not-venue-fx-usdt.md) | The 24 Jun 2026 jump appears on three exchanges by the same amount and is not explained by the real, USDT/USD or a Binance event | ✔️ confirmed | P2-05 | Jonathan |
| [F-010](findings/F-010-donor-premiums.md) | Where residents cannot buy dollars freely (ARS, UAH) USDT costs 4-7% more than the official dollar; in open markets 0-1% | ✔️ confirmed | P1-05 | Felipe, Jonathan |
| [F-011](findings/F-011-blind-breaks.md) | A blind break test finds 24 Jun 2026 as the sharpest regime change in six years (+100 bps), followed by a partial reversal from 22 Jul | ✔️ confirmed | P2-02 | Felipe |
| [F-012](findings/F-012-stablecoin-depeg-events.md) | Automatic screening identifies 29 USD-confirmed independent depeg events across 7 stablecoin pairs | 🔍 exploratory | P1-07 | Renzo, Nattan |
| [F-013](findings/F-013-depeg-count-v2.md) | After the review fixes, the depeg screen finds 11 falls below $1 (9 without a likely delisting), short of the 12 the chapter needs for recovery curves | ✔️ confirmed | P1-07 | Nattan |
| [F-014](findings/F-014-monitor-backtest.md) | A real-time alarm calibrated on 2020–2025 flags the 24 Jun 2026 jump on the same day, with fewer false alarms than a simple rule | ✔️ confirmed | P3-03 | Jonathan |
| [F-015](findings/F-015-route-costs.md) | The 23 Jun notice cost a buyer of digital dollars about R$ 5,050 per US$ 100k during the spike (+93.9 bps); after it, +11.5 bps (R$ 620) not distinguishable from noise. Bank-route comparisons are now sourced (BCB EE 48/2019 corporate spread 20 bps; statutory IOF by period) | 🔍 exploratory | P3-01 | - |
| [F-016](findings/F-016-event-studies-placebos.md) | Of 13 dated Brazilian events, only the 23 Jun 2026 BCB notice moved the premium (+93.9 bps; beyond all 1,073 placebo dates, p ≈ 0.001) | ✔️ confirmed | P2-03 | Renzo |
| [F-017](findings/F-017-synthetic-control.md) | Synthetic control estimates a +109 bps acute treatment gap for the 23 Jun 2026 shock (Brazil ranks #1 of 6, ratio 9.31) fading to a +28 bps plateau | ✔️ confirmed | P2-04 | Renzo |
| [F-018](findings/F-018-btc-heterogeneity.md) | The Bitcoin premium jumped by the same +93.8 bps on 24 Jun 2026, as triangular arbitrage on Binance requires; the test cannot tell a stablecoin-specific shock from a crypto-wide one | ✔️ confirmed | P3-02 | Renzo |
| [F-019](findings/F-019-depeg-chapter.md) | In dollars too, a stablecoin left parity while its redemption channel was closed: USDC closed at $0.863 on the SVB weekend and was back at $0.989 an hour after Sunday's deposit guarantee, before banks reopened; 11 other falls below $1 form a case table (too few for curves) | ✔️ confirmed | P3-04 | Renzo |
| [F-020](findings/F-020-subsidy-share-2025.md) | Between 37.5% and 53.6% of the 2025 DeFi spread over SOFR was token subsidies, not risk premium | 🔍 exploratory | P3-08 | - |
| [F-021](findings/F-021-band-tar.md) | Threshold Band-TAR model reveals a 26-fold widening of the no-arbitrage band during the 24 Jun spike (1.6 to 42.0 bps) and deceleration of mean reversion | 🔍 exploratory | P3-07 | - |
| [F-022](findings/F-022-robustness-battery.md) | The 23 Jun 2026 spike is robust (+74 to +128 bps across 22 variants); the after-spike level (+11 to +34 bps) is not distinguishable from ordinary drift (placebo p = 0.24) | ✔️ confirmed | P4-01 | Renzo |
| [F-023](findings/F-023-notice-sources-and-press-moves.md) | Two outlets saw the 23 Jun notice (or an excerpt) the next days, the BCB confirmed its position in writing, and the price moves they reported match our premium series | ✔️ confirmed | P3-14 | Felipe |
| [F-024](findings/F-024-stablecoin-imports.md) | In July 2026 stablecoin purchases abroad fell 78% (BCB) while the premium rose; they stayed at about a third of their earlier level through September while the premium fell back | ✔️ confirmed | P3-10 | Felipe |
| [F-025](findings/F-025-money-moved.md) | In the four weeks after the notice, buyers of USDT/BRL paid about R$ 106 mn more on Binance (R$ 145 mn on three exchanges) than at the pre-notice premium; no ordinary month comes close | ✔️ confirmed | P3-11 | Felipe |
| [F-026](findings/F-026-which-rules-matter.md) | Of eight dated Brazilian rules, only the confidential, immediate notice of 23 Jun 2026 moved the premium detectably; the published rules, with 1 to 175 days of notice, stayed within the range of ordinary dates | ✔️ confirmed | P3-12 | Felipe |
| [F-027](findings/F-027-prediction-res584.md) | Prediction committed on 2 Nov 2026 - the 24-hour hold of Res. BCB 584 (from 1 Jan 2027) will not move the premium detectably; its cost to a USDT holder is about 9 bps | ✔️ confirmed | P3-13 | Felipe |
| [F-028](findings/F-028-route-comparison.md) | We cannot identify which route set the price after the 23 Jun notice; the ordinary 3.5% route did not set it (the premium rose at most +171 bps, and raising that route's IOF in May 2025 moved it +13 bps) | ✔️ confirmed | P3-15 | - |
| [F-029](findings/F-029-headline-inference.md) | On non-overlapping windows the June change still beats every ordinary window (p = 0.03), and the two days before the 26 Jun meeting add +155 bps (p 0.02-0.04); but the +94 bps month also holds other BCB measures, and Res. 574 coincides with a +38 bps day before the notice | 🔍 exploratory | P4-04 | - |
<!-- BOARD:END -->

## Recent activity (newest first, one line per work session)

- 2026-11-02 — agent for Renzo: round-2 numbers re-validated independently (one misquote, two wordings and one count corrected); P4-04 → review: spec first (`f4071ef`), headline p = 0.032 on 30 non-overlapping windows, +155 bps in the two days before the 26 Jun meeting (p 0.02–0.04), Res. 574 coincides with +37.7 bps on 18→19 Jun (F-029); +93.9 bps kept as headline (Renzo)
- 2026-11-02 — agent for Renzo: round-2 strategy checks (`docs/deck-plan-10-slides.md`): non-overlapping placebo p = 0.03; the headline window also holds the 26 Jun meeting (E-12, new source) and Res. 580; Res. 561 text opened (E-06a) as the closest form-vs-content contrast; new task `P4-04`
- 2026-11-02 — agent for Renzo: 10-slide plan (`docs/deck-plan-10-slides.md`) with checked strategies; after a second agent's review: F-028 no longer calls the 3.5% route a ceiling (adds May 2025 evidence), slide 6 "real flat" fixed (PTAX +68 bps on 24 Jun), P3-16 caveat by content + timing drafted, minute-timing and half-life ideas dropped; review gaps flagged (F-015 status, F-020/F-021 self-checked)
- 2026-11-02 — agent for Renzo: P3-15 → review: rule committed first (`6393330`); marginal route not identified (outcome b); 3.5% route is a ceiling never approached (highest day +170.7 bps over pre-notice, +52.1 after 22 Jul); 1.1% "investimento" route's 110 bps lies in the spike range but no source says it carries virtual assets (F-028, `results/tables/P3-15_routes.md`); Res. BCB 574 (22 Jun) found, E-11, new task P3-16
- 2026-11-02 — Renzo: deck limit registered: at most 10 slides (prompt.md §2, decision log, blocker); current deck has 14
- 2026-11-02 — agent for Renzo: "beyond one period" reviewed with a second agent: no new extension before the freeze; four levels of language for the deck and line-by-line notes for Felipe (`docs/deck-notes-2026-11-02.md`; SVB = illustration, monitor = prototype, Argentina = future work); `P3-15` (todo): why +94 bps and not +350, decision logged
- 2026-11-02 — Felipe: peer-reviewed and reproduced `P3-10`–`P3-14` → `done` (`F-023`–`F-027` confirmed; verified SHA-256 of `D-16` & `D-17` BCB files and opened `Decreto 6.306/2007, art. 15-B, III` on Planalto so zero `[verify]` tags remain in `docs/sources.md`), cross-referenced `P3-13` (9.1 bps outgoing USDT hold cost) in `P3-01` S2b, and integrated `F-023`–`F-027` into `deck/deck_v1_ptbr.md` (Slides 5, 6, 10, 12) and `deck/annex_v1_ptbr.md` (Anexos A, B.5, B.7, C, D, E)
- 2026-11-02 — agent for Renzo: P3-13 → review: prediction committed (`393a14a`) that Res. 584's 24-hour hold (1 Jan 2027) will not move the premium detectably; it delays only outgoing transfers and costs a USDT holder ~9 bps (F-027). "So what" plan complete (P3-10 to P3-14 in review)
- 2026-11-02 — agent for Renzo: P3-12 → review: of 8 dated rules only the confidential, immediate notice moved the premium (+94 bps); the 7 published rules stayed within the ordinary-date range of −35 to +38 bps (F-026, figure P3-12_rules.png). Money slide number and Res. 580 deferred to slide building
- 2026-11-02 — Felipe: completed review follow-ups across `P3-01`, `P3-09`, `P5-01`, `P5-05`, `P5-07`: opened and quoted primary sources for all 11 depeg cases + USDP delisting (`DP-01`..`DP-10` in `docs/sources.md`, restored in `P3-04_depeg_case_table.csv`, `F-019`, `P3-09` → review), bank/exchange/hedge parameters (`R-01` BCB EE 48/2019 20 bps spread, `R-01b` BB PJ SWIFT, `R-05`–`R-07`, neutral framing in `P3-01` → review), and Foxbit Infra B2B lead (`M-05` in `F-008`); reviewed `P5-07` → done and rebuilt `deck/deck_v1_ptbr.md` (14 slides, keeping Options C and A open on Slide 10) and `deck/annex_v1_ptbr.md` (placebo $p$-values only, Anexo B.5–B.6)
- 2026-11-02 — agent for Renzo: P3-11 → review: buyers paid R$ 106 mn more on Binance (R$ 145 mn on 3 exchanges) in the 4 weeks after the notice, tariff equivalent ~95 bps, no placebo month above R$ 35 mn (F-025). My notice-sources task renumbered P3-09 → P3-14 (Felipe's depeg-sources task holds P3-09)
- 2026-11-02 — agent for Renzo: "so what" plan (`docs/06-so-what.md`, P3-10–P3-14). P3-14 → review: 10 sources on the 23 Jun notice with verified quotes (Cointelegraph Brasil 24 Jun had the notice, Exame 25 Jun an excerpt, BCB LAI answer), Res. 580 found (E-10), press moves match our series (F-023). P3-10 → review: BCB stablecoin purchases abroad −78% in Jul 2026 (p = 0.02), still at 32% of the earlier level in Aug–Sep while the premium fell back (F-024)
- 2026-11-02 — agent for Renzo: review fixes applied for Felipe (P2-03, P2-04, P3-02, P3-04, P4-01 → done; P3-01 framing left to the team); cost of the notice R$ 5,052 per US$ 100k (spike); story notebook `notebooks/p5_07_story.ipynb` (P5-07, deck prototype) → review
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

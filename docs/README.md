# Project Plans — Out of Sample, 7º Datathon FGV EESP

Agents: read `../prompt.md` first.

## The four candidates

| # | Project | Question | Winning potential | Main risk | Status |
|---|---|---|---|---|---|
| 2 | [Dólar cripto](02-dolar-cripto.md) | How much more do Brazilians pay for a digital dollar than the official dollar, and how much of that gap do rules that close or tax the arbitrage channels create? | **Highest** (see evidence below) | The 23 Jun 2026 jump has another cause; another team picks the topic | **Primary (recommended 30 Oct, after the probe)** |
| 1 | [Depeg recovery](01-depeg-recovery.md) | When a stablecoin loses its peg, what brings it back: reserve quality or whether redemption is open right now? | High as a chapter | Fewer than ~12 clean independent events | Chapter of project 2 (2–3 slides) |
| 3 | [Incentives](03-incentives.md) | How much of the DeFi yield is subsidy, and does subsidised capital stay when rewards end? | Medium | Few clean campaigns; jury finds it niche | One slide; full study only as fallback |
| 4 | [Treasury allocator](04-treasury-allocator.md) | Does forecasting lending yields improve allocation net of costs? | Low | Persistence already beats our 2025 model | Not recommended |

File numbers are historical; project 2 is now the primary.

**Extension (optional, kept 31 Oct):** [AI agents as research tools](05-agentic-robustness.md). A: 30 AI
analysts answer our question independently (robustness). B: an AI event coder screens the comparison
currencies for the synthetic control. Go/no-go at the Sun 1 Nov gate.

**Execution:** phases and success criteria in [`phases.md`](phases.md); live state in [`../STATUS.md`](../STATUS.md);
one file per task in [`../tasks/`](../tasks/); one file per result in [`../findings/`](../findings/);
sources in [`sources.md`](sources.md); ongoing strategic hypotheses, reflections, proposals, and decisions with Renzo
in the append-only [`improvements log`](improvements_log.md).

**Pending team review:** [proposal to test contribution, recovery and presentation](improvements-proposal.md).
It specifies investigations, deliverables, stop rules and adoption gates; no execution or framing decision is recorded yet.

**Research brainstorm (4 Nov, Renzo):** [Competing-rails research agenda](competing-rails-research-agenda.md)
records six directions in English; [datathon ranking and investigation plans](competing-rails-datathon-ranking.md)
checks their incremental contribution, data requirements and claim limits. Proposals for discussion, not adopted scope;
includes evidence-based comments on the [research/conclusions memo](plan-research-and-conclusions.md).

**Formalized extension tasks (6 Nov, Renzo):** [P3-28 — agentic access map](../tasks/P3-28-agentic-access-map.md)
and [P3-29 — on-chain reconciliation](../tasks/P3-29-on-chain-reconciliation.md) specify hypotheses, procedures,
evaluation and integration with the current findings. Both are **todo, unassigned**; 7 Nov is a feasibility/readiness
checkpoint. No experiment has run or deck inclusion been decided. The tasks can proceed independently.

**Unifying idea: limits to arbitrage.** A digital dollar should trade at parity with the dollar
(USD for a stablecoin, PTAX-converted BRL for USDT/BRL). Parity is enforced by an arbitrage channel: issuer
redemption, or the official FX market. Hypothesis: deviations are larger and last longer when that channel is
closed (weekends, bank holidays, issuer pauses, regulatory restrictions) or made expensive (taxes). Project 2
tests this on the price of the digital dollar in reais (the main analysis); project 1 shows the same mechanism
on the stablecoin's dollar price (the SVB weekend).

## Evidence from the 30 Oct probe (exploratory)

Script: [`scripts/00_probe_premium.py`](../scripts/00_probe_premium.py). Binance USDT/BRL 1h klines
(Oct 2020 – Sep 2026) vs BCB PTAX (Olinda API), matched to the PTAX window (10h–13h Brasília). One venue, no
USDT/USD adjustment yet. These numbers came **before** the design below was written down; treat them as
motivation, not as confirmatory results.

- **The premium is not noise.** Mean 82 bps (2021), 45–58 bps (2022–24), 23 bps (2025), against a median
  hourly high–low range of 7–12 bps. USDT's own dollar price (USDC/USDT) moved at most ~7 bps per month in
  2025–26, so it explains little of the gap.
- **It has regimes.** ~30–45 bps in H1 2025, ~15 bps in H2 2025, ~0–7 bps from Nov 2025 to May 2026, then a jump.

| Date | Event | Mean premium, 30 days before | 30 days after |
|---|---|---|---|
| 22 May 2025 | IOF decree on FX operations (E-01) | 30.9 bps | 44.3 bps |
| 10 Nov 2025 | BCB Res. 519–521 published | 15.2 | 7.8 |
| 2 Feb 2026 | BCB Res. 521 in force (stablecoin operations treated as FX) | 1.5 | 0.3 |
| 4 May 2026 | Reporting obligation to the BCB starts (E-04) | 7.1 | 6.6 |
| **23 Jun 2026** | **BCB notice to banks and funds on FX imports of virtual assets via funds** (E-05) | **7.5** | **95.2** |

Daily: 16 bps on 23 Jun → **144 bps on 24 Jun** → 172 bps on 25 Jun 2026, still ~100 bps two weeks later.
A [Conjur column of 1 Jul 2026](https://www.conjur.com.br/2026-jul-01/o-cerco-do-banco-central-as-stablecoins/)
independently reports the stablecoin spread rising from ~0.1% to ~0.7% (at times >1%) after that notice.
Caveat: PTAX also rose ~0.7% on 24 Jun (5.1743 → 5.2098) before reverting; the premium did not revert.
Weekend side result: the USDT/BRL move over the weekend anticipates the Friday→Monday PTAX move only weakly
(291 weekends, corr 0.26).

## Past winners and jury (why the plan looks the way it does)

| Edition | 1st | 2nd | 3rd |
|---|---|---|---|
| 2022 | Cryptal (USP): multifractal efficiency → portfolios | AustrianBoyz: chaos physics + neural nets | LTCM: Reddit + Markov chains to time BTC |
| 2023 | Sentic Crypto: BTC risk-premium predictability × sentiment | HAS: Transformers for whale moves | CriptoGirls (UFRGS): risk measures for BTC/ETH portfolios |
| 2024 | Crypto X Quant (FGV): volatility forecasting + vol-target strategy | Polichain (Poli-USP): Ponzi contract detection | CearáCoin (Unifor): RL portfolio manager |
| 2025 | Hermes (PUC-Rio): "Simulando Investidores com IA para Maximizar Retornos" | Eurytion (USP): "Otimização de Carteira com IA em Cascata" | Out-of-Sample (us) |

Sources: edition pages on eesp.fgv.br and the FGV Digital Finance page. Decks for 2022–2024 winners are public;
2025 decks are not.

- 11 of 12 podium spots were forecasting or portfolio projects; every 1st place was framed around investment
  returns or risk. 2025's top two both had "IA" in the title.
- The rigor bar is low (e.g., model comparisons without a naive baseline; F1 = 100% on oversampled data).
  Rigor alone will not win, but it is what survives questions from the academics.
- 2025 jury: asset managers and banks (Transfero, Itaú Asset, Bradesco, Banco Inter), Ripple's LatAm
  regulatory and policy director, academics (FGV EESP, FEA-USP), Nova SBE. The 2026 jury is not published yet.
- No 2022–2025 podium touched stablecoins or Brazilian FX. That lane is open, but it is in the news now.

What the primary plan takes from this: a money result for practitioners (cost of a digital dollar, per
regime), a "solution" deliverable (a daily monitor), and a causal design the academics will respect.

## Decision log

P3-42 (7 Nov, Felipe): explicit request to upgrade the compression prototype before revision. Bounded protocol `ce91d8b`: monthly linear/nonlinear fits, adaptive residual bands and stress-aware cost cards. F-051 exploratory; v1 preserved. Independent revision and deck adoption remain pending.

P3-41 (7 Nov, Felipe via explicit implementation request after project/data review): implement the first bounded decision-system experiment, partial premium compression linked to the buyer cost frontier. Scope and chronological protocol committed before fitting (`93fd20f`). F-050 remains exploratory; no demonstrated primary-horizon improvement over simple mean reversion. Independent reproduction and deck inclusion remain separate. Simulation, market-state detection, route stress testing and Chronos are not included in this first build.

P3-39 (7 Nov, Felipe via explicit implementation request): implement the buyer cost frontier with independent deposit/forward rates and a delivery/access gate. Scenario research authorized; deck adoption and independent reproduction remain pending. See `docs/buyer-cost-frontier.md` and F-048.

| Date | Decision | Who |
|---|---|---|
| 7 Nov | Final deck (P5-10, v4): **only the 10 slides go in the PDF**, no appendix pages; cover kept clean, other slides carry more text, built as a nine-chapter story; plan in `docs/deck-plan-v4-2026-11-07.md` (its appendix section is superseded). Felipe (deck owner) still approves | Renzo |
| 7 Nov | Continue P3-29 with an English investigation of the economic function of BRLA operations (P3-37, initially P3-35/P3-36; artifact prefix P3-36); distinguish technical routing from settlement and retain independent review before deck use | Renzo |
| 6 Nov | Formalize the agentic access map and on-chain reconciliation as English task specifications (P3-28/P3-29). Plans only: implementation todo, assignment pending; new evidence and independent evaluation required before deck use | Renzo |
| 5 Nov | Submission format: GitHub repository link + 10-slide PDF. No `.txt` script export goes to the jury; the repo is the code deliverable (P5-04 now maps claims to scripts). Rest of P5-04 assigned to Nattan or Jonathan | Renzo |
| 5 Nov | P3-16: keep the frozen eight-rule event comparison; disclose Res. BCB 574 as an explicit caveat in slide 5, annex and F-026. Its 20-day window overlaps the 23 Jun notice, so no separate event estimate or ninth row is claimed | Renzo |
| 30 Oct | Shortlist reduced to projects 1–4 above | Team |
| 30 Oct | Probe passed for project 2 (premium far above noise; sharp break on 24 Jun 2026) | Probe script |
| 30 Oct | Confirmed project 2 as primary and project 1 as a chapter | Team |
| 31 Oct | Keep the agentic extras A (30 AI analysts) and B (AI event coder) as optional; the primary plan does not change for them | Team (via Renzo) |
| 31 Oct | Work organised in phases P0–P6 with gates (`phases.md`), one file per task and per finding | Team (via Renzo) |
| 1 Nov | _Pending (P2 gate):_ synthetic control go/no-go (donor data quality); 23 Jun notice confirmed; second venue | Team |
| 31 Oct | Extension A runs on Renzo's existing Claude, ChatGPT and Gemini plans via Claude Code, Codex CLI and Gemini CLI (3 families, ~10 runs each); no API spend (P1-08) | Renzo |
| 31 Oct | Team: Renzo (CS 1), Nattan (CS 2), Jonathan (CS 3), Felipe (Economist). Tasks can be handed over mid-way: `working` field, subtasks, Handoff section (`prompt.md` §7) | Renzo |
| 31 Oct | USDT's dollar price for the premium: 1/USDCUSDT (Binance), with 1/BUSDUSDT filling Binance's USDC gap (26 Sep 2022 – 11 Mar 2023); Coinbase USDT/USD (direct dollar quote, from May 2021) frozen as the robustness series (F-006) | Renzo |
| 31 Oct | After the day-1 review (`review-2026-10-31.md`): keep the full plan, no tasks dropped; critical-path work first when tasks compete for a person | Renzo |
| 1 Nov | _Pending (P2 gate):_ agentic A go/no-go (owner available? CLIs usable on Renzo's plans?); B done or manual screening | Team |
| 2 Nov | Extension A may run on Renzo's existing CLI plans (Claude, ChatGPT, Gemini; no API spend). The go/no-go itself stays with the team at the gate | Renzo |
| 2 Nov | Sources: a link enters `sources.md` only if it was opened and one line quoted (`prompt.md` §6). The five broken links (M-01–M-04, C-01) were replaced with opened sources; unsupported details removed (M-01 Brazil/CVM, M-02 DOU date, M-03 announcement date, M-04 Res. 580); market events are said to *coincide with* breaks, not explain them; the link check runs again before the freeze (P4-03) | Renzo |
| 2 Nov | Plan to answer "so what?" (`06-so-what.md`): sources on the 23 Jun notice (P3-14; numbered P3-09 until renumbered the same day), the mechanism in BCB stablecoin-import statistics with a fade test specified before download (P3-10), money moved (P3-11), which rules matter (P3-12), a dated prediction for Res. 584 (P3-13). Side experiments are outside this plan; their place in the deck is a team call | Renzo |
| 2 Nov | Deferred to slide building (P5-01): which money number goes on the slide (Binance alone R$ 106 mn, or 3 exchanges R$ 145 mn, F-025), and whether Res. BCB 580 (E-10) joins the event list or stays a caveat in F-024 | Renzo |
| 2 Nov | **Deck limit: at most 10 slides** (critical; Renzo). The current deck has 14, so it must be cut; supporting material goes to the annex (Art. 8 allows annexes) | Renzo |
| 2 Nov | **Deck cut to 10 slides** (Renzo asked his agent to apply `docs/deck-plan-10-slides.md`): moved material in Annex F; bank-route table in Annex B.5 (Option A, team to confirm); Felipe reviews and may reverse any change (`docs/deck-changes-2026-11-02.md`) | Renzo |
| 2 Nov | **Correction on 2025 (Renzo, who was there):** last year's main flaw was the *time limit of the presentation*, not over-claiming. A well-prepared, rehearsed presentation fixes it, and improving it is a goal of this edition, together with the content and the study. The technical weaknesses in "Lessons from 2025" below are still true of the 2025 repo (our own re-check) but are not what the jury is known to have penalised; no statement about how the jury weighs things goes into the deck or the docs without a source | Renzo |
| 3 Nov | After a brainstorm on portfolio simulation (Renzo + agent): no trading backtest (one shock, hindsight, last year's lesson, legal tone). Adopted as plans: `P3-21` who paid and who gained (illustrative, rules fixed in advance, slide-9 candidate for Felipe) and `P3-20` predictions registered before the data for two rules in force on 3 Nov and 6 Nov (plan under Renzo's review; reported whatever they show) | Renzo |
| 2 Nov | **Research continues** (Renzo): there is time, so extensions that go beyond one period (Argentina, Apr 2025; SVB; others) are open again, each with a spec committed before its run, an opened source for every date, and a review. The Wed 4 Nov freeze in `prompt.md` §7 was set earlier; the team re-decides it explicitly (move it, or freeze the core numbers and keep extensions as separate findings). Until then core findings F-001..F-027 stay unchanged | Renzo |
| 2 Nov | **"Lições de 2025" is not a standalone slide** (Renzo): it goes with another slide, proposed: the method slide as a short strip (naive baseline, placebo dates, count independent events). The full table goes to the annex | Renzo |
| 2 Nov | A dated, append-only conversation log is the home for evolving strategic hypotheses, reflections, proposals, and decisions with Renzo; the first entry records the project-story discussion. Items in it are not team decisions unless explicitly marked adopted ([improvements_log.md](improvements_log.md)) | Renzo |
| 2 Nov | After reviewing ways to go beyond one period (with a second agent's critique): priorities before the freeze stay P4-02, peer review and the deck; ("no new extension" is superseded by the 2 Nov rows below). Deck claims use four levels of language: measured (spike, money), consistent with the mechanism (notice, July import drop), illustrative (SVB, cross-country), not shown (lasting effect, July fade, marginal route, form vs content). SVB is an illustration, not a second test; the monitor is a prototype with one detection; Argentina (Apr 2025) is future work only (opposite mechanism side, official-rate denominator jump). "+94 vs 350 bps" goes to P3-15 with "cannot identify the marginal route" as an allowed result. Line-by-line suggestions: `deck-notes-2026-11-02.md` | Renzo |
| 1 Nov | Economist gate calls (Felipe): (1) 23 Jun 2026 framed as empirically confirmed break across 3 venues coinciding with reported BCB supervisory ofício (ConJur, secondary; not a public DOU norm); (2) P2-03, P2-04, P3-01 report both the 20-day acute spike (24 Jun–21 Jul, ~109 bps) and the post-adaptation plateau (22 Jul–Oct, ~27 bps) separately; (3) P2-03 within-Brazil placebo dates (200 dates) serve as primary statistical p-value and P2-04 synthetic control (rank 1 of 6, or 1 of 7 if pre-period starts 1 Dec 2025 to include IDR) serves as cross-country counterfactual; (4) Foxbit 6x volume surge (F-008) included as order-book adaptation evidence alongside 7 Jul Foxbit-NovaDAX migration (M-04); (5) Depeg chapter (P3-04) uses SVB weekend chart + 11-event comparative case table rather than survival curves (since 11 < 12 pre-committed threshold). | Felipe |
| 3 Nov | Cost of the notice converted at **each day's PTAX**, averaged over the window: **R$ 4,842** per US$ 100k in the spike (was R$ 5,052), R$ 583 after (was R$ 621); bps unchanged. The R$ 5.38 used before is a Binance USDT/BRL bid of 31 Oct (D-10), not a PTAX (found by the P3-21 review). Route and scenario rows keep R$ 5.38 as a labelled illustrative reference rate (option a). Applied to `scripts/p3_01_costs.py`, F-015, cover, slide 9, annex B.5/D.2, notebook. Felipe (owner) to be informed; teammate re-check before the freeze | Renzo |
| 4 Nov | **Results frozen** (P4-03, Renzo): findings F-001 to F-033; the 27 confirmed ones are `frozen`, the 6 exploratory ones (F-012, F-029 to F-033) keep their label with frozen numbers and are used only at the level their Claim states. Tag `results-frozen`. After this only disclosed bug fixes; new work goes into new findings (F-034 onwards), cited in the deck only after a teammate's re-run. Supersedes the open freeze question in the 2 Nov "Research continues" row | Renzo |
| 4 Nov | **Competing-rails follow-up adopted** (Renzo, after reading `competing-rails-datathon-ranking.md`, the mentor notes and Felipe's mentor-lead dossier): (1) P3-20 first: E1 readout, E2 branch by 5 Nov 23:59 (E1 is judged on the S2 band, −75.5/+59.8 bps on Binance, not the S20 band −35/+38); (2) new `P3-24` BRLA as a fourth venue (Felipe moves his data and scripts into the repo; the BRLA/USDC pool measures the cost of the Pix→BRLA→USDC route, not a BRL depeg; the supply fall is not called a run until a source says so); **Renzo reviews all of Felipe's mentor-lead work once it is pushed**; (3) new `P3-25` price recovered, did the market? (Renzo): venue shares and exits, retrospective spec, 4 h cap; (4) new `P5-08` Slide 10 conclusion checked against the evidence (Felipe, Renzo reviews). Not before submission: H3 cost sensitivity, new H5 user cases, H6 FX spillovers, Hyperliquid/EWZ, P3-22. Coinext's closure is not attributed to the notice (its own statement cites the capital requirement) | Renzo |
| 5 Nov | **Raw data stays out of git, including agents' snapshots** (Renzo): Felipe's Flash bundle moved from `results/flash-mentor-leads/` to `data/raw/flash-mentor-leads/` (checksums in `data/raw/SHA256SUMS`, restore from `79b71f1` in `data/README.md`). New downloads: new files under `data/raw/`, checksums appended, preferably a re-download script; only `data/processed/*.csv` is committed | Renzo |

## Opening briefing notes (30 Oct)

_To fill in: research FGV/Ripple presented, example topics, datasets offered, anything that changes priorities._

- Renzo (recorded 5 Nov): the opening presentation asked teams to answer **"O que aprendemos com a solução apresentada?
  E por que é importante?"** The jury wants a solution and a lesson someone can use, not only a measured effect. Proposal
  for Slide 10: `docs/proposal-2026-11-05-lessons-and-solution.md`.

## Lessons from 2025: the baseline we must beat

Last year's project ([repo](https://github.com/Renzo-Filho/6-datathon-fgv-eesp), 3rd place) predicted the
daily spread *Aave/Compound USDC APY − SOFR*. Re-checked on its own `raw_data/Y.csv` (1,000 days,
12 Feb 2023 – 7 Nov 2025) using the deck's split (first 80% train, last 20% test, from 22 Apr 2025):

| Forecast | R² | MAE | RMSE |
|---|---|---|---|
| Naive "tomorrow = today" | **0.776** | **0.169** | **0.272** |
| Hybrid K-Means + SVM (2025 deck) | 0.622 | 0.248 | 0.332 |
| TFT (2025 deck) | 0.912 | 0.766 | 2.05 |

```python
import pandas as pd
y = pd.read_csv("raw_data/Y.csv", index_col=0, parse_dates=True).iloc[:, 0].dropna()
s = int(len(y) * 0.8); t, p = y.iloc[s:], y.shift(1).iloc[s:]
print(1 - ((t - p) ** 2).sum() / ((t - t.mean()) ** 2).sum(), (t - p).abs().mean())
```

_Note (2 Nov, Renzo): this table is our own technical re-check of the 2025 repo. The team's reading of what hurt most last year is the presentation time limit (see decision log); delivery and rehearsal are part of this edition's goal._

What a reviewer would flag, and what we do differently this year:

| 2025 weakness | 2026 practice |
|---|---|
| No naive baseline; the hybrid model lost to persistence | A naive baseline in every results table |
| TFT R² 0.91 but MAE 4.5× worse than naive: metrics not comparable | One test set and one metric definition for all models |
| Model selected on training RMSE | Selection on validation data; final period untouched |
| "Foi comprovado que o VIX não causa…" drawn from clustering | Causal claims only from an explicit design (event study, survival model, placebo dates) |
| Two of four regimes absent from the test period | Count independent events; report statistical power |
| Utilization used to explain APY, though Aave computes APY from utilization | Explanatory variables that are not mechanical functions of the target |
| `model.py` (Random Forest, 3 threshold regimes) ≠ deck (K-Means k=4 + SVM) | Scripts submitted are exactly the scripts that made the figures |
| DeFiLlama `apy` = base + token rewards, treated as a risk premium | Separate `apyBase` and `apyReward` (see project 3) |
| Brazil and Drex only in the introduction | Brazil in the data and the implications |

These go on one deck slide, "Lições de 2025". Owning last year's flaws is the clearest maturity signal we can send.

## Roles (default; adjust per project)

| Role | Owns |
|---|---|
| CS 1: data | Downloads, coverage audit, source register, timestamps |
| CS 2: modelling | Baselines, main estimation, robustness |
| CS 3: validation / chapter | Independent re-check of every headline number; owns the depeg chapter (project 1) |
| Economist | Hypothesis, event-coding rules, interpretation, **deck owner** from day 1 |

Everyone reviews one result they did not produce.

## Submission checklist

See `../prompt.md` §8. Phases and dates are in `phases.md`; the working protocol is in `../prompt.md` §7.

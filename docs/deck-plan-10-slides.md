# Deck plan: 10 slides (proposal, 2 Nov 2026)

For Felipe (deck owner, P5-01) and the team, from Renzo's agent. A proposal: the deck owner decides. It applies the
binding decisions of 2 Nov (`docs/README.md`): at most 10 slides, "Lições de 2025" as a strip on the method slide,
the four language levels of `docs/deck-notes-2026-11-02.md`, and delivery/rehearsal as part of the goal.

## The 10 slides

The cover counts as slide 1; references and registers go to the annex. Order follows Art. 7 of the regulation
(motivação → delimitação → dados e metodologia → resultados → discussão). One message and one chart per slide;
finding IDs go to small footnotes, not the body.

| # | Title (pt-BR) | The one message | Chart | Language level | From deck v1 (14 slides) |
|---|---|---|---|---|---|
| 1 | **Quanto custa fechar a porta?** | The question and the answer only: **+94 bps for one month = R$ 5.052 por US$ 100 mil**, plus one relevance line (Brazilians bought about US$ 2.4 bn a month of stablecoins abroad, Jan–May 2026, F-024). The parity equation and channel diagram move to slide 2 | Headline number; no equation | Measured (answer) | 1 |
| 2 | **A porta que fechou: o ofício de 23/jun** | The parity idea in one line + channel diagram. What the notice said (two outlets saw it; the BCB confirmed its view in a written LAI answer), who used the channel (funds, 0% IOF vs 3.5%), confidential and immediate. Timeline of the dated rules | Timeline of rules, notice marked | Consistent with the mechanism | 5 (first half), 6 (timeline) |
| 3 | **Dados e método** | Six years matched to the PTAX window, 3 exchanges, 5 comparison currencies, BCB statistics. Design: blind break test, comparison with 1,073 ordinary dates, synthetic control; what would falsify. **Disclosure:** the jump was first seen in the day-0 probe (F-002); hypotheses and tests were fixed after it, and the notice's date comes from outside sources (press 24–25 Jun, BCB written answer). **Strip "Lições de 2025":** naive baseline, placebo dates, count events not rows | Design diagram + H1/H0 table | – | 2, 3, 13 (strip) |
| 4 | **O salto** (headline chart) | +93.9 bps after 23 Jun; the same on 3 exchanges (+93.3 to +94.9); a blind break test finds 24 Jun without being given the date | Daily premium 2025–26 with noise band; inset hourly 22–26 Jun, 3 exchanges | Measured | 3, 4 |
| 5 | **Entre as regras com data, só o ofício saiu da faixa comum** (was "Só o ofício moveu o preço"; Res. 574 coincides with +38 bps on 18→19 Jun, F-029) | Larger than the change at every one of 1,073 ordinary dates (the largest: +65.7 bps); not "p ≈ 0.001" on the slide, because neighbouring 20-day windows overlap (38 of 40 days) and behave like ~30–40 independent comparisons. The published rules stayed inside the ordinary range; Res. 574 (22 Jun) shares the window, see P3-16; the May 2025 IOF rise (1.1% → 3.5%) moved it only +13 bps (p = 0.38) | `P3-12_rules.png` | Measured; form vs content **not shown** | 6 |
| 6 | **Não foi o real, nem o USDT, nem o mundo** | Synthetic control +109 bps (Brazil 1st of 6); the real moved (PTAX +68 bps on 24 Jun) but the premium is measured against PTAX, so that move is removed, and USDT/USD stayed at ~0.999 (F-009); BTC rose by the same amount, as triangular arbitrage requires | `P2-04_synthetic_control.png` | Measured | 7 |
| 7 | **O mecanismo: as importações caíram** | Stablecoin purchases abroad fell 78% in July while the price rose: higher price, lower quantity ("coincidiu com"). Caveat: Res. 580 the same month | `P3-10_imports.png` | Consistent with the mechanism | 5 (second half) |
| 8 | **Robusto, mas de um mês** | +74 to +128 bps across 22 variants; after 22 Jul not distinguishable from ordinary drift (p = 0.24). Box "**o que não mostramos**": lasting effect, cause of the fade, marginal route (F-028), form vs content | `P4-01_robustness_forest.png` | Measured + not shown | 8, 14 (limits) |
| 9 | **Quanto custou e para quem** | R$ 106 mn on Binance (R$ 145 mn on 3 exchanges) moved from buyers to sellers in 4 weeks: like a ~0.95% tariff collected by the remaining suppliers, not the Treasury. Why not +350: the ordinary 3.5% route did not set the price (at most +171 bps; its May 2025 IOF rise moved the premium +13 bps); we cannot tell whether cheaper supply or lower demand held it (F-028) | New: spike month vs 194 placebo months (`results/tables/P3-11_placebo.csv`) | Measured (transfer); route not shown | 10 |
| 10 | **Implicações, previsão e limites** | Brazil: an abrupt closure produced an acute transfer that faded within a month (how is not known). Dated prediction for Res. 584, 1 Jan 2027 (`393a14a`); monitor prototype (one detection); limits; future work (Argentina, SVB) | Small prediction box | Prediction / prototype | 12, 14 |

**To the annex:** cross-country premiums (v1 slide 9, illustrative), SVB and depeg cases (v1 slide 11, illustrative),
monitor details (v1 slide 12), full "Lições de 2025" table (v1 slide 13), Band-TAR, bank route costs (Option A),
source registers. The Option C vs A question mostly dissolves: slide 9 carries the transfer and the "why not 350" line,
the bank-route table goes to the annex. The team confirms.

## Observations: how strong this deck is

**Strengths**
- One question, one answer in reais ("R$ 5 mil por US$ 100 mil").
- Layered identification: blind break test, placebo dates, three exchanges, synthetic control, BTC.
- Slide 5 + F-028 tell one story: the 3.5% route did not move the premium when it was raised (May 2025) and the premium
  never came near it after the notice. Two separate pieces of evidence say the ordinary bank route was not the
  marginal one.
- Visible honesty: hypotheses fixed after the probe and said so, a "não mostramos" box, a dated prediction that can be proved wrong.
- Live Brazilian policy: Res. 584 takes effect on 1 Jan 2027.

**Weak points a juror can attack**
1. **One event.** All causal evidence is about one shock; the published rules and placebo dates are contrasts, not
   replications.
2. **Thin mechanism.** One monthly observation (−78%), confounded with Res. 580; the notice's full text was never
   published.
3. **"Only a month."** The fade is unexplained, while imports stayed at a third of their earlier level.
4. **Tempting policy lesson.** "Publish rules with notice" needs form and content separated; we cannot separate them.
5. **Legal sensitivity.** 0% vs 3.5% IOF in front of bankers and regulators can read as tax avoidance; keep
   `docs/02-dolar-cripto.md` §10 framing ("medimos fricções").
6. **Too many numbers.** Three versions of the jump (93.9 / 109 / 128) and two of the money (106 / 145): one per
   concept on the slide, the rest in the annex.
7. **Delivery.** v1 slides are text-heavy and the oral time limit is unknown (it arrives by e-mail if we reach the
   final). Speaker notes at ~60 s per slide; a marked cut order (compress slides 6 and 8 first).
8. **Res. BCB 574 (22 Jun 2026)** is not in the event list (P3-16); slide 5's "only the notice" needs it handled.

## Is the core research finished?

Yes for analysis: no new estimate is needed for the core claim. Before the slides are final:

| Item | Why | Size |
|---|---|---|
| P3-16 (Res. 574) | Slide 5 claims "only the notice" | < 1 h |
| Team freeze of core numbers (P4-03) | Move the date, or freeze F-001..F-028 now and keep extensions as separate findings | decision |
| Reviews: P1-04, F-015, F-028 | F-015 (R$ 5,052) is still exploratory; P1-04 is the event list | small |

Suggested schedule: freeze core by Tue 3 Nov; deck v1 Thu 5; timed rehearsals Fri 6 – Sat 7; submit Sun 8 by 20:00.
Side questions (Argentina, SVB, Extension A, 26 Jun meeting, 22 Jul fade) feed only the annex or slide 10's
future-work line.

## Strategies for the weak points, checked before proposing (2 Nov, Renzo's agent)

Each idea was checked against our data or an opened source first. Numbers below are exploratory: any that reaches
the deck goes into a finding with its command first.

| # | Weak point | Strategy | Check done | Verdict |
|---|---|---|---|---|
| 1 | One event | ~~Name the inference~~ (revised: plain wording on the slide; paper only in an annex method note saying we did not run its test): the placebo-date p-value follows the logic of the sample-quantile (SQ) test for single-event studies (Gelbach, Helland & Klick 2013, *American Law and Economics Review* 15(2), 495–541; built for "regulation, antitrust rulings" and litigation events). Synthetic control is designed for one treated unit (L-08) | Paper record opened on IDEAS (https://ideas.repec.org/a/oup/amlawe/v15y2013i2p495-541.html): SQ test is "based on sample quantiles of pre-event fitted excess returns". Our statistic is a 20-day window difference, not a daily excess return, so write "na lógica do teste SQ", not "rodamos o teste SQ" | **Annex only** (second agent's review, agreed): on the slide say "comparamos a variação de junho com a de 1.073 datas comuns" |
| 1b | One event | Use the 26 Jun meeting (in-book arbitrage "liberou") as a second, opposite move inside the episode | Hourly premium was already falling on 25 Jun afternoon (161 → 90 bps) before the meeting; no source gives the meeting time | **Reject** |
| 1c | One event | Argentina as a replication | See the 2 Nov discussion: unification of a dual rate, IMF money the same weekend | **Reject** as a test; illustrative annex only |
| 2 | Thin mechanism | Time the jump to the minute against the first public report (Cointelegraph, `datePublished` 24 Jun 2026 12:36 UTC = 09:36 BRT) | Hourly bar 24 Jun 09:00–10:00 BRT holds both. Even with minute data: we cannot confirm that article was the first public mention, a move before it would not show who traded, and we have no intraday real–dollar rate | **Reject** (second agent's review, agreed) |
| 2b | Thin mechanism | Future-work line: Res. BCB 574 (E-11) makes FX institutions report virtual-asset operations "realizadas a partir de 3 de novembro de 2026" | The reports go to the BCB "na forma definida pelo Banco Central"; nothing promises public data, and they do not cover June | **Adopt with care:** "novos reportes podem permitir testes melhores de mudanças futuras, se os dados se tornarem disponíveis" |
| 3 | "Only a month" | Describe the fade as a gradual decay, not a 22 Jul event: the excess over the pre-notice level halved by 10 Jul, while imports stayed at a third (F-024) and Binance volume returned to its pre-notice level (55.2 vs 58.4 M USDT/day, F-024) | Daily premium: peak 185.9 bps on 3 Jul; first day with excess below half (85.4 bps): 10 Jul. Exchanges: 113 (8 Jul), 63 (15 Jul), 37 (27 Jul) bps, moving within ±4 bps of each other | **Adopt as a shape, no new number** (second agent's review, agreed): "já caía no início de julho e tinha se dissipado em grande parte no fim de julho"; the 3 Jul anchor is post hoc and a half-time explains nothing |
| 3b | "Only a month" | Foxbit Infra relaunch (18 Jul, M-05) as the cause of the fade | Decline under way before 18 Jul; exchanges move in lockstep, no Foxbit lead | **Reject** |
| 3c | "Only a month" | Band-TAR (F-021): band widened, arbitrage slowed | Band CI separates (1.61 [1.22, 5.13] vs 41.95 [9.96, 52.63] bps), but on 20 observations, regimes picked from the same data, and a band around the regime mean widens with volatility; slowing CI overlaps (half-life 1.60 [0.26, 2.10] vs ≤ 1 day) | **Not for the deck**; annex after P3-07 review |
| 4 | Policy lesson (form vs content) | No recommendation; F-027's prediction is the forward test of "published rule with notice" | Res. 584 targets outgoing transfers (E-06b, art. 2-B), not the import channel: a partial test only, say so | **Adopt** |
| 5 | Legal sensitivity | Describe the rule in the BCB's own words (LAI, E-05.3); "diferença de alíquota", never "arbitragem de IOF" (E-05.10's headline wording); Felipe checks each slide against §10 | Quotes exist in `docs/sources.md` | **Adopt** |
| 6 | Too many numbers | One number per concept: +93.9 bps (pre-committed 20-day window, F-016); R$ 106 mn Binance (F-025 uses Binance alone because Foxbit's volume has open questions, F-008). Ranges only on slide 8 and the annex | F-025 text | **Adopt** |
| 7 | Delivery | Action titles (each title states the result) so the PDF stands alone; notes at ~60 s per slide; two timed rehearsals with a timekeeper; a Q&A sheet of ~10 hard questions with 20-second answers and annex pointers (n = 1, Res. 574, Res. 580, why not 350, why PTAX window, real vs USDT, lasting effect, who got the money, legality, why BTC moved) | Regulation: first round judged on the PDF alone (`prompt.md` §2) | **Adopt** |
| 8 | Res. 574 | P3-16: caveat by content and timing, not "ruled out" | Content: reporting of operations from 3 Nov, no restriction on June operations. Timing: dated 18 Jun 18:01 in the BCB register, DOU 22 Jun; daily premium 32.9 (19 Jun), 23.3 (22 Jun), 24.8 (23 Jun), 155.4 (24 Jun). A 20-day window after 22 Jun contains the jump, so the event study cannot separate the dates | **Adopt** (< 1 h) |

Housekeeping found: L-05..L-08 appear only in the annex (C.5), not in `docs/sources.md`; the annex gives Makarov &
Schoar (2020) pp. 289–319, a search record says 293–319 `[verify]`.

Commands for the checks above:
```bash
# hourly premium around the notice and the 26 Jun meeting (BRT)
.venv/bin/python -c "
import pandas as pd
h=pd.read_csv('data/processed/P1-02_premium_hourly.csv',parse_dates=['time_utc']).set_index('time_utc')['premium_vs_last_ptax_bps']
h.index=h.index.tz_localize('UTC').tz_convert('America/Sao_Paulo')
print(h['2026-06-22 09:00':'2026-06-24 13:00'].round(0).to_string()); print(h['2026-06-25 08:00':'2026-06-26 17:00'].round(0).to_string())"
# peak, half-time, venue lockstep
.venv/bin/python -c "
import pandas as pd
p=pd.read_csv('data/processed/P1-02_premium_daily.csv',parse_dates=['date_brt']).set_index('date_brt')['premium_bps']
x=p['2026-07-03':]-15.2; print(p['2026-06-24':].idxmax().date(), p['2026-06-24':].max().round(1), x[x<170.7/2].index[0].date())
v=pd.read_csv('results/tables/P2-05_venues_daily.csv',parse_dates=[0],index_col=0); print(v.loc['2026-07-08':'2026-07-31'].round(0).to_string())"
```

## Corrections after a second agent's review (2 Nov)

A second agent reviewed this plan; its points were checked before being accepted.

| Point | Check | Outcome |
|---|---|---|
| "The real was flat" (slide 6) is false | PTAX +68.4 bps on 24 Jun and +67.5 on 23 Jun; 2025–26 median absolute daily change 39.4 bps | Fixed above |
| 3.5% is not an established ceiling | F-028's own route table: route 3 supply "unknown" | F-028 and route table corrected: "did not set the price" + May 2025 evidence |
| Res. 574 cannot be ruled out by date | 20-day window after 22 Jun contains the jump | P3-16 framed as content + timing |
| Future reporting will not settle June | Res. 574 text: reports to the BCB, from 3 Nov | Wording softened (row 2b) |
| Minute timing would not show who moved the price | No confirmed first public mention; no intraday FX | Rejected (row 2) |
| No half-life number | 3 Jul anchor is post hoc | Shape only (row 3) |
| Cite Gelbach et al. only with care | Their statistic differs from ours | Annex only (row 1) |

Added by this agent after checking: (a) "p ≈ 0.001" overstates precision because the 1,073 windows overlap; say
"maior que todas as datas comuns (a maior: +65,7 bps)"; (b) the deck must disclose that the jump was seen in the
probe before the hypotheses (`docs/02-dolar-cripto.md` §13 says "Declare it"); (c) P4-02's ledger confirms 22 headline
findings, but F-015 (the R$ 5,052 on slide 1) is still `exploratory`, and F-020 and F-021 were re-checked by their own
author. Not adopted: amending local commits (`prompt.md` §7: never rewrite history; `6393330` records the P3-15 rule).

```bash
# PTAX and USDT/BRL changes around the notice
.venv/bin/python -c "
import pandas as pd, numpy as np
d=pd.read_csv('data/processed/P1-02_premium_daily.csv',parse_dates=['date_brt']).set_index('date_brt')
s=d.loc['2026-06-19':'2026-06-26',['ptax_sell_brl_per_usd','usdtbrl_window_brl','usdtusd_window_usd','premium_bps']]
s['ptax_chg_bps']=1e4*np.log(s.ptax_sell_brl_per_usd).diff(); print(s.round(4).to_string())
x=1e4*np.log(d.ptax_sell_brl_per_usd).diff()['2025-01-01':'2026-06-22']; print(x.abs().median().round(1), x.abs().quantile(.95).round(1))"
```


## New strategies, round 2 (2 Nov, checked before proposing)

| # | Gap | Strategy | Check done | Verdict |
|---|---|---|---|---|
| N1 | Inference precision ("p ≈ 0.001" on overlapping windows) | Report the non-overlapping version beside "larger than every one of 1,073 ordinary dates" | 30 non-overlapping clean windows, 0 exceedances (two-sided, as F-016) for all 41 offsets: p = 0.032. Not "independent": the windows share no days, but the series is autocorrelated | **Adopt** via P4-04 (new finding) |
| N2 | Headline window contains other measures | Say the +94 bps is the month after the notice, a window that also holds the 26 Jun meeting (suspension kept, in-book arbitrage released, 24-hour-hold draft, E-12) and Res. 580 (1 Jul, E-10); report the first-day move (+130.6 bps, 23 → 24 Jun) as the only part that predates them | First-day move is 2026's largest daily rise, but 3 days since 2023 matched it, so it is support, not proof; the meeting's time is unknown and the hourly fall began on 25 Jun afternoon, so the 26 Jun fall says nothing either way; the first day does **not** predate Res. 574 (18/22 Jun); a second peak on 3 Jul (+86.7 bps in a day) has no identified cause | **Adopt** via P4-04 |
| N3 | Form vs content | On slide 5, set the notice beside its closest contrast: Res. 561 banned virtual assets in eFX settlement ("sendo vedado o uso de ativos virtuais"; whether stablecoins were in use there before is not shown), but was published with 154 days' notice: +6.0 bps at announcement, −5.3 at effect (P3-12) | Text opened (E-06a). The size of the eFX channel is unknown, so this narrows, not settles, form vs content | **Adopt** as a contrast with that caveat |
| N4 | Topic chosen after seeing the jump | The attribution is not only ours: the day after the notice, market operators quoted by the press tied the price move to it (E-05.6: "saiu de cerca de 0,1 acima do mercado para 0,7 após a notificação"; Exame, 25 Jun 2026 19h43, headline "Notificação do BC a bancos deixa criptomoedas até 2% mais caras no Brasil; entenda", opened 2 Nov; an earlier version of this row quoted it from the URL without "até") | Quotes and URLs in `docs/sources.md` (E-05.2, E-05.6) | **Adopt** (slide 2, with the probe disclosure on slide 3) |
| N5 | Cause of the fade | Look for a dated report that the funds' operations resumed in July | One extended search, 2 Nov: nothing found (not proof of absence) | **No strategy**; stays "not shown" |
| N6 | One event | A dated prediction for Res. 574's reporting start (3 Nov), resolved before submission | A reporting-only rule over 4 PTAX days: a near-certain null, little evidence | **Reject** |

What no strategy found here can fix: one shock in one country; form vs content; the cause of the fade; the marginal
route. These stay in the "não mostramos" box.

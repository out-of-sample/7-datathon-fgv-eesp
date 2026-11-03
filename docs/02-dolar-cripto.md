# Project 2 — Dólar cripto: what does it cost to close the door?

**Status:** **primary** (recommended 30 Oct after the probe; team confirmation pending in `README.md`).
Project 1 (depeg recovery) becomes a 2–3 slide chapter showing the same mechanism on the dollar side.
Strategic discussion with Renzo is recorded append-only in [`improvements_log.md`](improvements_log.md); proposals there
remain proposals until the team adopts them.
**Deck title (pt-BR draft):** "Quanto custa fechar a porta? O preço do dólar digital no Brasil"

## 1. Question and primary metric

**Question:** How much more do Brazilians pay for a digital dollar (USDT) than for the official dollar (PTAX),
and how much of that gap is created by rules that close or tax the channels arbitrageurs use to keep the two
prices together?

**Primary metric:** the premium in basis points, `premium_t = USDTBRL_t / (PTAX_t × USDTUSD_t) − 1`, measured
in the PTAX window. **Primary estimate:** the effect of the 23 Jun 2026 BCB notice on the premium, relative to
a synthetic control built from other currencies' USDT premiums.

## 2. Plain-English example

On 23 Jun 2026, USDT cost 0.16% more than the official dollar. On 24 Jun it cost 1.44% more. A company buying
US$ 100,000 through the crypto route paid about **R$ 6,700 more** than it would have the day before, and the
gap stayed near 1% for weeks. The day before the jump, the BCB had told banks and funds that a common structure
for importing stablecoins through investment funds was irregular `[verify]`. One door closed, and the price of
the digital dollar moved away from the official one.

## 3. Evidence so far

See `README.md` → "Evidence from the 30 Oct probe" and [`scripts/00_probe_premium.py`](../scripts/00_probe_premium.py).
Summary: the yearly mean premium is 2–5× the median hourly price range, has visible regimes, and jumped from ~7 bps to
~95 bps (30-day means) around 23 Jun 2026, while three other rule dates show no comparable move.

**Discipline note.** The hypotheses below were written *after* that probe. The probe numbers are motivation.
The confirmatory evidence is what we specify here and run afterwards: the blind break test, the synthetic
control, and the placebo tests. Say this on the method slide.

## 4. Why it can win

- **Open lane:** no 2022–2025 podium touched stablecoins or Brazilian FX (see `README.md` → past winners).
- **Relevance:** stablecoins are most of Brazilian crypto volume `[verify figure]`; the BCB brought them into
  the FX framework in 2026; IOF on stablecoin purchases and a 24-hour hold on transfers are being discussed
  now `[verify]`. The jury includes banks, asset managers and Ripple's regulatory lead.
- **A shock no earlier team could study:** a sharp, dated break four months old.
- **Complexity in the design, not in the model count:** blind break detection, a synthetic control with
  placebo countries, a panel of currencies, plus the survival-analysis chapter. Compare with 2025: four
  models, no baseline, no causal claim.
- **A money result** (cost of a digital dollar per regime) and a **solution** (daily monitor) for the
  practitioners on the jury.

## 5. Hypotheses

- **H1 (closed channel):** the 23 Jun 2026 notice raised the premium relative to a synthetic Brazil built from
  currencies that had no comparable shock.
- **H2 (only binding rules matter):** rules that did not change the cheapest arbitrage channel (Res. 521
  entering into force; the reporting obligation) did not move the premium. These serve as within-Brazil
  placebos, with the caveat that they were seen in the probe.
- **H3 (costlier channel):** the May 2025 IOF increase raised the premium by less than the tax change, because
  the crypto route was outside IOF at the time `[verify legal status]`.
- **H0:** premium changes are explained by BRL volatility, USDT's own dollar price, or exchange-specific events.

What falsifies H1: the synthetic control tracks Brazil after 23 Jun, or the Brazil gap is not extreme among
the placebo-country gaps (permutation p-value > 0.1), or a second BRL venue shows no jump.

## 6. Data

| Need | Source | Status |
|---|---|---|
| USDT/BRL 1h (main venue) | [data.binance.vision](https://data.binance.vision) monthly klines `USDTBRL` | **Checked:** Oct 2020 – Sep 2026 (72 months). Oct 2026 from daily files |
| Official dollar with timestamps | BCB Olinda PTAX `CotacaoDolarPeriodo` | **Checked:** Oct 2020 – 30 Oct 2026 |
| USDT's dollar price | Binance `USDCUSDT` (checked, Dec 2018 – Sep 2026); Kraken USDT/USD as a direct USD quote | Kraken coverage `[verify]` |
| Second BRL venue | Mercado Bitcoin or Foxbit public APIs | `[verify]` |
| Donor currencies (synthetic control) | Binance `USDTTRY` (2019-12+), `USDTZAR` (2020-03+), `USDTUAH` (2020-06+), `EURUSDT` (2020-01+), `USDTMXN` (2024-04+), `USDTCOP` (2024-06+), `USDTPLN` (2023-04 → 2026-07), `USDTIDR` (2025-11+), `USDTARS` (2023-04+) | **Checked** in the archive (through Sep 2026 unless noted) |
| Donors' official FX | ECB reference rates (EUR, TRY, ZAR, MXN, PLN, IDR), TRM (COP), NBU (UAH), BCRA A 3500 (ARS) | **Checked**, frozen by P1-05 (D-05); premiums in `data/processed/P1-05_donor_premiums_daily.csv` |
| BTC premium (heterogeneity) | Binance `BTCBRL` (2020-10+) and `BTCUSDT` | Checked (`BTCBRL`) |
| Event dates | BCB resolutions and communications, decrees, Receita/Fazenda notes, exchange notices | Hand-collected; every date confirmed in a primary source |

Exclude from the donor pool any currency with capital controls or its own crypto/FX rule change in the window
(ARS and UAH are likely exclusions; document why).

### Event list (all `[verify]` before use)

- 22 May 2025: decree raising IOF on several FX operations; later congressional and STF episodes (Jun–Jul 2025).
- 10 Nov 2025: BCB Res. 519, 520, 521 published; 2 Feb 2026: in force (Res. 521 treats some stablecoin
  operations as FX).
- Feb 2026: Fazenda/Receita proposal of 3.5% IOF on crypto purchases (status unknown).
- 4 May 2026: start of reporting obligation for these operations.
- 23 Jun 2026: BCB notification to banks and funds on FX imports of virtual assets through funds.
- 2026: Res. BCB 561/2026 changing the eFX regime (date `[verify]`); proposed 24-hour hold on stablecoin
  transfers from US$ 10k, effect planned for Oct 2026.
- Every weekend and Brazilian holiday (repeated "FX market closed" episodes).

## 7. Method

1. **Premium (v2).** Timing-matched to the PTAX window; divided by USDT/USD; second venue as a check; noise
   floor from a spread estimator (Corwin–Schultz or Abdi–Ranaldo) on hourly OHLC.
2. **Blind break detection.** Bai–Perron (or `ruptures` with a BIC penalty) on the daily premium, minimum
   segment 20 trading days, number of breaks chosen by the criterion, not by us. Report break dates with
   confidence intervals, **then** match them to the event list. Breaks with no matching event are reported
   as unexplained.
3. **Event studies for every dated rule** (not only the one that worked): mean premium in [−20, −1] vs
   [+1, +20] trading days, Newey–West standard errors, 200 random placebo dates.
4. **Synthetic control for 23 Jun 2026.** Outcome: each currency's daily USDT premium over its official rate.
   Pre-period: 1 Nov 2025 – 22 Jun 2026; post: 24 Jun – 30 Sep 2026. In-space placebos (each donor treated in
   turn); report the post/pre RMSPE ratio and the permutation p-value. **Baseline:** simple
   difference-in-differences against the donor average. If the pre-period fit is poor, fall back to the DiD
   and say so.
5. **Heterogeneity:** BTC/BRL premium over `BTCUSDT × PTAX`. Did the notice raise the cost of all crypto
   imports or only stablecoins?
6. **Money result.** All-in cost of buying US$ 100k: bank route (PTAX + bank spread + IOF; BCB publishes
   effective FX cost rankings `[verify]`) vs crypto route (premium + exchange fees), per regime. Scenarios
   for the proposed 24-hour hold and 3.5% IOF, labelled as scenarios: with arbitrage, the premium can rise at
   most to the cost of the next cheapest open channel.
7. **Monitor do Dólar Digital.** The same script produces a daily index with the current regime and a break
   flag. One screenshot slide; no web app.
8. **Stretch (only if Tue 3 Nov is on time):** threshold autoregression with a no-arbitrage band per regime,
   giving the implied arbitrage cost and how fast deviations close.

**Baselines in every table:** pre-period mean (event studies); donor-average DiD (vs synthetic control);
premium explained by BRL volatility and USDT/USD alone (H0).

## 8. Headline charts

1. Daily premium 2020–2026 with the blind break dates (vertical lines) and policy markers, noise band shaded.
2. Brazil vs synthetic Brazil around 23 Jun 2026, with placebo-country gaps in grey.

## 9. Deck storyline (≈12 slides + annex)

1. Title.
2. Question; why a Brazilian treasurer, the BCB and Ripple care.
3. Lições de 2025.
4. How arbitrage holds USDT/BRL near PTAX (one diagram: the doors).
5. Data and premium construction.
6. The series and its blind breaks (headline 1).
7. Every rule tested, including the nulls.
8. Synthetic control (headline 2) + placebos.
9. What it costs: US$ 100k by regime; scenarios.
10. The same mechanism in dollars: SVB weekend (project 1 chapter).
11. Monitor do Dólar Digital.
12. Implications and limitations. Annex: event table with sources, donor pool, robustness, code map.

## 10. Framing rule

We measure the cost of frictions. We do not describe or recommend ways around FX or tax rules, and we
describe the BCB's actions neutrally. The jury includes banks and a regulator-facing lead.

## 11. Go / no-go

| When | Test | If it fails |
|---|---|---|
| 30 Oct | Premium above noise | **Passed** (probe) |
| Sun 1 Nov | 23 Jun notice confirmed in a primary or second independent source | Present the jump as an unexplained break, lean on the blind break test and the all-events table |
| Sun 1 Nov | At least 4 usable donors with official FX and pre-period fit | DiD against the donor average only |
| Sun 1 Nov | Second BRL venue shows the jump | If it does not, the result is venue-specific: say so; reconsider the headline |

## 12. Schedule

| Date | Economist | CS 1 (data) | CS 2 (modelling) | CS 3 (validation / chapter) |
|---|---|---|---|---|
| Sat 31 Oct | Event list with primary sources | Premium v2 (USDT/USD, second venue) | Donor downloads + official FX | Depeg detector on stablecoin pairs |
| Sun 1 Nov | Go/no-go calls | Noise floor | Break test, event studies, placebos | Re-run the probe independently |
| Mon 2 Nov | Money-result inputs (bank costs, IOF) | BTC heterogeneity | Synthetic control + placebos | Depeg chapter v1 |
| Tue 3 Nov | Deck skeleton | Monitor | Robustness | Check every headline number |
| Wed 4 Nov | **Freeze results** | | | |
| Thu 5 – Sun 8 Nov | Deck v1 → red team → final; scripts to `.txt`; submit by 20:00 Sun | | | |

## 13. Risks

| Risk | Mitigation |
|---|---|
| Another cause for the 24 Jun jump (BRL shock, Binance-specific event, USDT issue) | Second venue; USDT/USD adjustment; BRL-volatility control; synthetic control |
| Another team picks the topic | Depth: blind breaks, synthetic control, money result, depeg chapter |
| Donor premiums noisy (timing of each country's fix) | Daily closes with wider windows; drop noisy donors by pre-period fit rule stated in advance |
| Hypotheses shaped by the probe | Declare it; confirmatory tests specified here before running them |
| Legal sensitivity | Framing rule (§10) |

## 14. Compatibility with the agentic extras (`05-agentic-robustness.md`)

The extras plug into existing steps; this plan does not change for them. Four rules apply from day 1:

1. Freeze raw files with checksums as soon as they are downloaded (P1-01).
2. Agents get raw files only, in a bundle outside the repo; `docs/` (which holds our numbers) is never visible to them.
3. Record our before/after estimate (§7.3) in the agents' answer schema (P2-06).
4. Commit that estimate before anyone opens an agent result.

Agents are compared with the §7.3 before/after estimate, not with the synthetic control.

## 15. Literature anchors

- Shleifer, A. & Vishny, R. (1997). The limits of arbitrage. *Journal of Finance*.
- Makarov, I. & Schoar, A. (2020). Trading and arbitrage in cryptocurrency markets. *Journal of Financial Economics*.
- Abadie, A., Diamond, A. & Hainmueller, J. (2010). Synthetic control methods for comparative case studies. *JASA*.
- Bai, J. & Perron, P. (1998, 2003). Structural change models. *Econometrica*; *Journal of Applied Econometrics*.
- Obstfeld, M. & Taylor, A. (1997). Nonlinear aspects of goods-market arbitrage and adjustment (band-TAR) `[verify]`.
- Kimchi-premium literature (Korea capital controls and bitcoin premia) `[verify specific papers]`.

---
id: F-036
title: The premium receded while Foxbit's share of USDT volume on the three observed exchanges stayed much higher than before
status: exploratory
task: P3-25
date: 2026-11-05
checked_by: -
---

## Claim
**Retrospective, descriptive.** The premium returned to an ordinary range after the June spike (F-022), but Foxbit's
share of USDT trading volume on Binance, Foxbit and Mercado Bitcoin rose from **6.80%** (1 May–22 Jun 2026) to
**34.74%** (22 Jul–30 Oct 2026), a **+27.94 percentage-point** change. None of 1,048 overlapping historical adjacent
window pairs, using the same 53-day and 101-day lengths since Mercado Bitcoin's March 2023 start, changed by as much
in absolute value; the largest was 6.40 percentage points. This is one episode and a limited three-exchange perimeter,
not evidence that the 23 Jun notice caused the composition shift or that new dollars entered Brazil.

## Evidence
Reproduce from the frozen raw data: `.venv/bin/python scripts/p3_25_composition.py` →
`results/tables/P3-25_composition.csv`, `results/tables/P3-25_reference.csv`, and
`results/figures/P3-25_price_vs_share.png`. The specification and task claim were committed first (`70c23e4`).
The script uses UTC hourly candles, applies Brasília (UTC−3) dates and 09:00–18:00 business hours, and retains hours
with Binance and Foxbit observations. Mercado Bitcoin omits hours with no trades, so its missing candles count as
zero volume. All venues' volumes are the USDT base asset, summed over the same hours for each period; the primary
share is a ratio of period sums, not an average of hourly or daily shares.

| Period (inclusive Brasília dates) | Foxbit share of three-exchange USDT volume | Foxbit volume | Shared hours / expected | Mercado Bitcoin hours with no candle | Foxbit median daily average trade | Foxbit volume in 09:00–18:00 |
|---|---:|---:|---:|---:|---:|---:|
| Pre, 1 May–22 Jun 2026 | 6.80% | 212.0 million USDT | 1,272 / 1,272 | 4 | 740 USDT | 81.72% |
| Wave, 24 Jun–21 Jul 2026 | 27.99% | 858.3 million USDT | 672 / 672 | 12 | 4,019 USDT | 96.46% |
| After, 22 Jul–30 Oct 2026 | 34.74% | 3,334.5 million USDT | 2,421 / 2,424 | 16 | 5,308 USDT | 96.07% |

The after period loses three hours because the 30 Oct freeze ends at 23h UTC (20h Brasília): 21–23h Brasília on 30 Oct are not in the frozen data, for any venue. Binance's own volume rose (53.6 → 60.3 million USDT per day) while Foxbit's rose from 4.0 to 33.0 million per day, so
the share change is Foxbit growing about eightfold, not the other venues shrinking. The 1,048 historical
reference pairs are **overlapping**, not 1,048 independent events, so 0/1,048 is a descriptive comparison and not a
causal or independent-sample p-value. Their signed changes range from −6.40 to +4.60 percentage points; the 2.5th and
97.5th percentiles are −4.70 and +4.29 points. The actual before/after windows have a wave between them; the
historical windows are adjacent as fixed in the task, a benchmark rather than a matched counterfactual. F-031's
7% → 33% → 37% figures averaged daily shares and used a different wave and after endpoint. The present finding
answers the fixed, volume-weighted period question.

### Exchange exits and their stated reasons
The dates describe each company's decision or first service restriction, not a measured loss of volume on our three
observed exchanges. Every firm source below is opened and quoted in `docs/sources.md` (M-07 to M-10).

| Firm | Timing relative to 23 Jun 2026 and 30 Oct licence deadline | Firm's own account | Relation to Foxbit |
|---|---|---|---|
| NovaDAX | The firm page was released on 8 Jun (page metadata `releasedAt`; updated 9 Jun), **before** 23 Jun and the deadline; Exame published its statement on 8 Jun 2026, 09h44. Trading ended 1 Jul. | A long-term assessment led it to discontinue brokerage in Brazil (M-07); it does not name the June notice. | The Foxbit client partnership was announced 7 Jul (M-04), after the 30 Jun onset of large Foxbit seller-initiated trading (F-031). |
| Bitnuvem | Its shutdown process began **Oct 2025**, before both dates. The current public page has no publication date. | Large international competitors and an increasingly unfavorable national regulatory setting for fintechs (M-08); it does not identify the June notice. | Client destination not established in the opened statement. |
| Digitra | The company page's publication metadata says **20 Aug 2026**, after 23 Jun and before 30 Oct. | It decided not to apply for authorization and to end retail trading/custody in an orderly way (M-09). | Its notice offers Foxbit as a voluntary transfer destination. This can affect the later after period, not the June onset. |
| Coinext | Its FAQ says new account openings and deposits stopped **3 Sep 2026**, after 23 Jun and before 30 Oct; the page itself is undated. | It says it did not meet the regulatory minimum capital for an authorization request (M-10). | Its FAQ suggests Mercado Bitcoin or OKX as optional destinations, not Foxbit. |

### Competing explanations

| Explanation | Fits the observed facts | Missing separator |
|---|---|---|
| New supply or rerouting through Foxbit | High volume, large trades and seller-initiated trading in business hours (F-031) | Identified traders, exchange deposits and cross-border flow records |
| Use of existing USDT inventories | Can produce the same volume and order-initiation pattern without imports | Balances, wallet flows and trader-level inventory |
| Buyers retreating from other venues | Can increase Foxbit's relative share; BCB purchases abroad fell in July (F-024) | Comparable buyer activity and customer flows across all venues |
| Clients migrating from closing firms | NovaDAX and Digitra named Foxbit as a destination (M-04, M-09) | Client arrival dates and their actual USDT volumes; announcements alone do not prove migration volume |
| Licensing consolidation | Firm statements name licensing or regulatory costs (M-07 to M-10) | A market-wide venue census and volumes, including firms outside our sample |
| Activity moving beyond the observed perimeter | Three order books cannot capture OTC, P2P or offshore trading | Comparable OTC, P2P and offshore volume data |

## Caveats
- The episode and period boundaries were seen before this task; historical pairs describe unusualness, not causation.
- Three venue shares are **not** national market shares or supplier concentration. Foxbit's own B2B market-making
  relaunch (M-05) and two client-transfer partnerships (M-04, M-09) overlap the period and cannot be separated here.
- Order initiation is not net position or cross-border flow (F-031). The observed venue mix cannot identify who sold
  or why the premium fell.
- Bitnuvem and Coinext pages do not show original publication dates. The timing table uses the first date their own
  text states and labels this limit. No firm's source attributes its exit to the 23 Jun notice.

## Used in deck
Not used until an independent review. Candidate slide sentence: **"O prêmio recuou, mas a Foxbit passou de 6,8% para
34,7% do volume de USDT nas três corretoras observadas."** Annex paragraph: **"As três corretoras não representam todo
o mercado: balcão, P2P e plataformas offshore ficam fora. A mudança de participação pode refletir oferta, estoques,
demanda ou migração de clientes. Os dados não identificam quem trouxe dólares nem atribuem a mudança ao ofício."**

## History
- 2026-11-05, agent for Renzo (Claude, independent review of Codex's work): reproduces byte for byte (CSVs and PNG); a
  separate rebuild from the raw files (own code, BRT resample) gives 6.80% and 34.74%. Sensitivity, not the registered
  rule: keeping the episode's 29-day gap between windows, 1,018 pairs, signed change −7.06 to +5.37 pp, none as large.
  Corrections: NovaDAX page released 8 Jun (was "dated 9 Jun", the update date); the three lost hours are the freeze
  cutoff, not missing data; per-day volumes added. Sources: M-07 (NovaDAX page and Exame), M-09, M-10 quotes and dates
  verified; M-08 (Bitnuvem) could not be reopened (TLS handshake error, 5 Nov), so its quote is not re-verified. Claims stay
  within the task's ceiling. Status stays exploratory until a teammate (Nattan or Jonathan) re-runs it
- 2026-11-05, Codex for Renzo: created from the registered P3-25 comparison and opened firm statements; awaiting
  independent re-run by Renzo's other Claude agent (or Nattan/Jonathan).

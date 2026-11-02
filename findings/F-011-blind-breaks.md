---
id: F-011
title: A blind break test finds 24 Jun 2026 as the sharpest regime change in six years (+100 bps), followed by a partial reversal from 22 Jul
status: exploratory
task: P2-02
date: 2026-10-31
checked_by: -
---

## Claim
Without being told any dates, a break test on the daily premium (13 Oct 2020 – 30 Oct 2026) puts a break on
**24 Jun 2026**, with the tightest 95% interval of all breaks (18–30 Jun). The premium's average rises from 9 to
109 bps, the largest change in the sample. A second break on **22 Jul 2026** takes it back down to 27 bps. So the
jump was a roughly one-month spike, leaving the premium about 17 bps above its earlier level. In S3, the 24 Jun 2026
break matches E-05 (23 Jun 2026 BCB supervisory ofício) within -1 trading day (inside the 95% CI). Break 1 matches M-01
(Binance leverage cap, 0d), Break 2 matches M-02 (CVM Binance settlement, 0d), Break 3 captures M-03 and E-01b within
its 95% CI, and Break 5 reflects the endogenous fade of the June spike as domestic order books adapted (M-04).

## Evidence
Headline model (specification committed before the run, `tasks/P2-02-blind-break-test.md`). BIC picked the maximum of 8
breaks, which the pre-committed rule treats as over-selection, so the headline uses LWZ: 5 breaks.

| Break | First day of new regime | 95% interval | Mean before (bps) | Mean after (bps) | Change (bps) |
|---|---|---|---|---|---|
| 1 | 26 Jul 2021 | 22 Jun – 27 Aug 2021 | 91.3 | 54.5 | −36.8 |
| 2 | 20 Aug 2024 | 24 Apr – 16 Dec 2024 | 54.5 | 34.9 | −19.6 |
| 3 | 8 Jul 2025 | 29 Apr – 12 Sep 2025 | 34.9 | 9.3 | −25.6 |
| 4 | **24 Jun 2026** | **18 – 30 Jun 2026** | 9.3 | 109.1 | **+99.8** |
| 5 | 22 Jul 2026 | 15 – 29 Jul 2026 | 109.1 | 26.8 | −82.4 |

### Break-to-event matching (S3, using P1-04 verified dataset)

| Break | First day of new regime | 95% interval | Change (bps) | Matched event / context | Match status |
|---|---|---|---|---|---|
| 1 | 26 Jul 2021 | 22 Jun – 27 Aug 2021 | −36.8 | M-01: 26 Jul 2021 Binance leverage cap & withdrawal limit | Exact day (0 trading days, in 95% CI) |
| 2 | 20 Aug 2024 | 24 Apr – 16 Dec 2024 | −19.6 | M-02: 20 Aug 2024 CVM Binance settlement DOU publication (approved 13 Aug [-5d]) | Exact day (0 trading days, in 95% CI) |
| 3 | 8 Jul 2025 | 29 Apr – 12 Sep 2025 | −25.6 | E-01b: 4 Jul 2025 STF IOF injunction (-2d); M-03: Binance tick cut 27 Jun 2025 (-7d) | Matched E-01b (-2 trading days, in 95% CI); M-03 in 95% CI |
| 4 | **24 Jun 2026** | **18 – 30 Jun 2026** | **+99.8** | **E-05: 23 Jun 2026 BCB supervisory ofício to banks/brokers** | **Matched (-1 trading day, in 95% CI)** |
| 5 | 22 Jul 2026 | 15 – 29 Jul 2026 | −82.4 | M-04: Foxbit-NovaDAX user migration (7 Jul [-11d]); domestic order-book adaptation | Unexplained (±5d); endogenous fade of 24 Jun spike (20d min-segment boundary) |

Robustness (S4), same specification:
- **Day-close timing** (BIC picks 6, headline 6): breaks on 23 Jun 2026 (12 Jun – 2 Jul, +90.0) matching E-05 (0 trading days, in 95% CI) and 21 Jul 2026 (−75.9). No Jul 2025 break; instead 2 Jan 2025 (−28.3), plus a Nov–Dec 2021 spike (+78.7, then −84.5) not seen in the main series. LWZ alone would keep only one break (Jan 2022): this variant is much noisier (AR(1) 0.26 vs 0.65).
- **Coinbase USDT/USD** (from May 2021; BIC 8 → LWZ 7): 24 Jun 2026 (22–26 Jun, +101.3) matching E-05 (-1 trading day, in 95% CI) and 22 Jul 2026 (−83.9); also 8 Jul 2025 (−25.1; M-03 & E-01b in CI), 13 Aug 2024 (−21.3; matching M-02 CVM settlement approval, 0 trading days, in 95% CI), and two breaks only this series finds: 6 Jun 2022 (−32.0; E-07 Binance Pix suspension 17 Jun 2022 inside 95% CI) and 20 Dec 2022 (+23.8; FTX collapse 8-11 Nov 2022 inside 95% CI).
- Extra, not in the specification: a model allowed only one break puts it in Sep 2024 (main and Coinbase). The slow decline is the biggest feature of the whole sample; the June spike is the sharpest.
- Reproduce: `python scripts/p2_02_breaks.py` (`results/tables/P2-02_breaks.csv`, `P2-02_criteria.csv`, `results/figures/P2-02_premium_breaks.png`).

## Caveats
- **The high regime lasts exactly 20 PTAX days, the minimum segment length.** The chart shows a spike that decays through July, not a clean step. The 22 Jul date is partly set by that constraint, so read it as "the spike had largely faded by late July", not as a precise date.
- The intervals use Bai (1997) with one long-run variance for the whole sample. The variance was higher in 2021–2022, so intervals there are probably too narrow, and in 2025–2026 probably too wide. The constant 11.03 is verified against Bai (1997) (L-03).
- BIC hit its cap in two of three series: serial correlation inflates the break count. The headline count therefore depends on the LWZ rule, which we fixed in advance.
- "Blind" means the algorithm got no dates. The people who set the specification had already seen the chart.
- A mean shift is not a cause. Which breaks match rules is S3; causal claims need P2-03 and P2-04.

## Used in deck
Not yet (candidate headline chart: "the algorithm finds 24 Jun on its own").

## History
- 2026-11-02, Felipe: P1-04 mapped all 5 breaks (M-01, M-02, M-03/E-01b, E-05, M-04), ready for P2-02 S3 table update; 24 Jun 2026 break matched to E-05 (23 Jun BCB supervisory ofício, -1 trading day, in 95% CI)
- 2026-10-31, agent for Renzo: created (exploratory; S3 matching pending P1-04)

---
id: F-035
title: Registered predictions E1 (Res. BCB 574) and E2 (Res. BCB 589) readout — E1 held at +2.1 bps (p = 0.90); E2 early reading S1 moved −5.4 bps on Binance (p = 0.79) and −6.5 bps on Foxbit (p = 0.79) with parity holding at +0.1 bps gap
status: exploratory
task: P3-20
date: 2026-11-07
checked_by: -
---

## Claim
We wrote down before the data that Res. BCB 574 (reporting rule from 3 Nov 2026, E1) would **not move the premium detectably** (registered `9a522e9`, reference distributions `ce283dc`, readout code `30de591`, all pushed before November data was downloaded). **It did not.** On Binance, the mean premium in the first two PTAX windows (3 and 4 Nov) was **+2.1 bps** above its 20-day pre-mean (statistic S2; **two-sided p = 0.90**, non-overlapping p = 0.92; Foxbit agrees at −1.9 bps, p = 0.92). The prediction stands. The P3-26 audit confirms that S2 is completely insulated from Binance's 29–30 Oct security incident (pre-window ended 3h before the attack; post-window began after cross-venue parity normalized).

For Res. BCB 589 art. 91 (ban on unauthorized counterparties effective 6 Nov 2026, E2), Branch C was registered on 5 Nov (`5e9d56c`, two-sided test, no direction) because the BCB had not published a comprehensive list of transitioning PSAVs clarifying bank/Pix access for pending applicants (on 6 Nov, BCB issued Comunicado 46.241 listing specific election notices for Madar and Ripio SPSAVs, leaving the general bank-access status open). In the first window under the ban (6 Nov), the early reading **S1** (6 Nov minus 5 Nov) is **−5.4 bps on Binance (two-sided p = 0.79)** and **−6.5 bps on Foxbit (two-sided p = 0.79)**, while the cross-venue gap narrowed by **−1.1 bps (p = 0.92)** to **+0.1 bps**. No price jump or cross-venue dislocation occurred on day 1; the primary verdict statistic S2 (`mean[6 and 9 Nov] − mean[pre-window]`) will be read on Monday 9 Nov.

## Evidence
Reproduce: `py scripts/p3_20_live.py download` then `py scripts/p3_20_live.py readout` → `results/tables/P3-20_readout.csv`, `data/processed/P3-20_premium_daily.csv`.

### 1. E1 Readout (Res. BCB 574, t0 = 2026-10-30)

| Series | S2 = mean(3–4 Nov) − mean(20 days to 29 Oct), bps | p, all clean dates (n) | p, non-overlapping | Reference band (2.5–97.5%) |
|---|---|---|---|---|
| **Binance (primary)** | **+2.1** | **0.897** (1,073) | 0.920 | −75.5 / +59.8 |
| Foxbit | −1.9 | 0.923 (958) | 0.956 | −166.0 / +128.7 |
| Foxbit − Binance gap | −4.0 | 0.607 (958) | 0.556 | −165.6 / +130.8 |
| Mercado Bitcoin, MB − Binance gap | not observed: November pull challenged by Cloudflare | – | – | −43 / +39 (MB) |

- **Early reading S1** (3 Nov minus 30 Oct): Binance +47.9 bps, p = 0.12. Registered as not used for the verdict because 30 Oct was a Binance-only dip (−30.3 bps, gap +49.0 bps) caused by Binance's withdrawal freeze (F-045). S2's pre-window excludes 30 Oct by design.

### 2. E2 Early Reading (Res. BCB 589 art. 91, t0 = 2026-11-05)

| Series | S1 = p(6 Nov) − p(5 Nov), bps | p, all clean dates (n) | Reference band (2.5–97.5%) | Status |
|---|---|---|---|---|
| **Binance (primary)** | **−5.4** | **0.7877** (1,073) | −74.8 / +75.0 | Observed (early reading) |
| Foxbit | −6.5 | 0.7894 (958) | −164.7 / +162.9 | Observed (early reading) |
| Foxbit − Binance gap | −1.1 | 0.9249 (958) | −155.5 / +143.0 | Observed (early reading) |
| Mercado Bitcoin | not observed: API challenged | – | −43.1 / +40.9 | Missing |
| **S2 verdict (6 and 9 Nov)** | pending: 1 of 2 post days | – | −75.5 / +59.8 | Evaluated on Mon 9 Nov |

Daily window premiums (bps):
- 28 Oct: Binance 19.6, Foxbit 22.1, MB 21.7 (gap +2.6)
- 29 Oct: Binance 12.5, Foxbit 13.4, MB 11.3 (gap +0.9)
- 30 Oct: Binance −30.3, Foxbit 18.6, MB 17.4 (gap +49.0)
- 3 Nov: Binance 17.6, Foxbit 16.6 (gap −1.0)
- 4 Nov: Binance 25.0, Foxbit 22.0 (gap −3.0)
- 5 Nov (E2 t0): Binance 22.2, Foxbit 23.4 (gap +1.2)
- 6 Nov (E2 treated day 1): Binance 16.8, Foxbit 16.9 (gap +0.1)

- **Cross-venue parity:** The Foxbit − Binance gap closed to +0.1 bps on 6 Nov. No cross-venue divergence or localized liquidity crunch appeared on day 1 of Res. 589.
- **Regulatory transition context:** On 6 Nov 2026, the BCB issued Comunicado 46.241 disclosing election notices for candidates to administrative posts at SPSAVs (Madar and Ripio), confirming that licensing processes are active, but did not issue a general list establishing bank access for all pending applicants. Branch C (two-sided, unconstrained) was properly registered and maintained.
- **P3-26 Confounder Audit:** Audit confirmed that E1 S2 is mathematically insulated from the 30 Oct Binance incident. For E2, 30 Oct reduces the 20-day pre-mean by ~2.3 bps, which is small relative to the ±75 bps reference band and disclosed transparently. Monitor CUSUM is on a mandatory 10-day quiet pause through 16 Nov.

## Caveats
- S1 is an early 1-day reading; the pre-registered verdict for E2 is S2 (2-day mean: 6 and 9 Nov), which will be available on Monday 9 Nov after market close.
- Mercado Bitcoin November candles were challenged by Cloudflare (HTTP 521).
- Reference bands reflect 2020–2026 volatility; null results rule out moves larger than the reference band (~75 bps for S1 and S2), not zero effect.

## Used in deck
Slide 10 prediction table and Annex B.8/B.9 / `limites.html`.

## History
- 2026-11-07, Economist (Felipe): added E2 S1 early reading (Binance −5.4 bps, Foxbit −6.5 bps, gap −1.1 bps); updated with P3-26 confounder audit findings and BCB Comunicado 46.241 check (P3-20 S6).
- 2026-11-05, agent for Renzo: created (P3-20 S3–S4).

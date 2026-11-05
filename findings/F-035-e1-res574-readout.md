---
id: F-035
title: Registered prediction E1 held - in the first two windows under Res. BCB 574's reporting (3–4 Nov 2026) the premium moved +2.1 bps on Binance (p = 0.90), no move of the June kind; a null that rules out only moves beyond about 75 bps
status: exploratory
task: P3-20
date: 2026-11-05
checked_by: -
---

## Claim
We wrote down before the data that Res. BCB 574 (FX-authorised institutions report their virtual-asset operations from
3 Nov 2026) would **not move the premium detectably** (registered `9a522e9`, reference distributions `ce283dc`, readout
code `30de591`, all pushed before any November data was downloaded). **It did not.** On Binance, the mean premium in the
first two PTAX windows under the rule (3 and 4 Nov) was **+2.1 bps** above its mean over the 20 PTAX days before t0 = 30 Oct
(statistic S2). Larger in absolute value than this: 962 of 1,073 ordinary (clean) dates, **two-sided p = 0.90**
(non-overlapping dates: p = 0.92). Foxbit agrees: −1.9 bps, p = 0.92. The prediction stands.

What it does **not** say: the reference band for S2 on Binance is −75.5 to +59.8 bps, so this null only rules out a move
larger than about that, the size of the June spike (+93.9 bps). It is not evidence of zero effect. It also does not tell our
idea ("a rule that leaves every channel open does not move the price") apart from the simple forecast "nothing happens":
both predicted no move. And it is one event.

## Evidence
Reproduce (from the repo root): `python scripts/p3_20_live.py download` (November pulls into `data/raw/live/`, checksums
in `data/raw/SHA256SUMS`), then `python scripts/p3_20_live.py readout` → `results/tables/P3-20_readout.csv`,
`data/processed/P3-20_premium_daily.csv`. The readout first rebuilds the P1-02 premium from raw data and asserts it equals
`P1-02_premium_daily.csv` on all 1,520 days to 30 Oct (passes).

| Series | S2 = mean(3–4 Nov) − mean(20 days to 29 Oct), bps | p, all clean dates (n) | p, non-overlapping | Reference band (2.5–97.5%) |
|---|---|---|---|---|
| **Binance (primary)** | **+2.1** | **0.897** (1,073) | 0.920 | −75.5 / +59.8 |
| Foxbit | −1.9 | 0.923 (958) | 0.956 | −166.0 / +128.7 |
| Foxbit − Binance gap | −4.0 | 0.607 (958) | 0.556 | −165.6 / +130.8 |
| Mercado Bitcoin, MB − Binance gap | not observed: the November pull failed (below) | – | – | −43 / +39 (MB) |

Daily window premium (bps): 28 Oct 19.6, 29 Oct 12.5, **30 Oct −30.3**, 3 Nov 17.6, 4 Nov 25.0 (Binance); Foxbit 22.1,
13.4, 18.6, 16.6, 22.0.

- **Early reading S1** (3 Nov minus 30 Oct): Binance +47.9 bps, p = 0.12. Registered as not used for the verdict, because
  30 Oct was unusually low on Binance. The data confirm why: on 30 Oct Binance was −30.3 bps while Foxbit was +18.6 and
  Mercado Bitcoin +17.4 (Foxbit − Binance gap +49.0 bps), a Binance-only dip on t0 that S2's pre-window excludes.
- **Monitor** (P3-03): its CUSUM fired a down-alarm on 30 Oct (one of its two 2026 false alarms) and is then paused for 10
  PTAX days by rule, so it could not alarm in [t0+1, t0+5]. No information either way.
- **Non-overlapping p**: P4-04 method (clean dates kept at least 23 PTAX days apart, every offset 0–22); 49 dates per set,
  45 of them larger than the observed value in every set.
- **Overlapping developments registered in advance**: the 30 Oct authorisation deadline falls on t0 (excluded from S2);
  2 Nov holiday; US midterms on 3 Nov and the Copom decision on 4 Nov both came after the PTAX window closed. Not checked
  further.

## Caveats
- **Mercado Bitcoin missing.** Its API answered our November request with a Cloudflare redirect (HTTP 302) on 5 Nov
  ~02:50 UTC; the frozen October file downloaded normally on 31 Oct. Not retried with a browser user agent (that would get
  around a bot check). Retry later, or have a person save the API's JSON from a browser.
- Two days of data; the reference band reflects 2020–2026 volatility, wider than 2026's own.
- Res. 574 was published on 22 Jun, 4.5 months ahead: a reporting rule, fully anticipated. A correct "no move" cannot
  separate transparency, content (no channel closed) or weak power.
- S20 (20 days) is pending until early Dec and is reported jointly with E2 (their windows overlap).
- A readout bug was fixed after the download but before the first readout run: a series with no November price would have
  been scored as k = 0 (a tiny p); it is now reported as missing. Only Mercado Bitcoin's rows were affected.

## Used in deck
Candidate for the Slide 10 prediction box (`P5-08` S2): "sem movimento detectável — conferido: +2,1 bps em 3–4/nov
(p = 0,90); a faixa exclui só movimentos acima de ~75 bps". Only after a teammate re-runs it (P3-20 criterion 5).

## History
- 2026-11-05, agent for Renzo: created (P3-20 S3–S4)

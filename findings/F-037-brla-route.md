---
id: F-037
title: The route Pix → BRLA → USDC on Polygon paid the June premium too (+111 bps in the 20 days after the notice, against +94 for USDT on Binance) while BRLA kept its value against another reais token (−3 bps); a small market (0.2–0.35% of Binance's volume); BRLA's supply fall on 24 Jun reversed a build-up of the days before and is not shown to be a run
status: exploratory
task: P3-24
date: 2026-11-05
checked_by: -
---

## Claim
**Retrospective** (Felipe's first look, F-034, saw the jump before this spec; the windows are the core study's). Buying
dollars through a Brazilian-real stablecoin on-chain, outside any Brazilian exchange order book (reais via Pix → BRLA,
issued by Avenia → USDC on a Uniswap v3 pool on Polygon), cost **34.9 bps** over PTAX in the 20 PTAX days before the
23 Jun notice and **145.9 bps** in the 20 after: **+111.0 bps**, against **+93.9 bps** for USDT on Binance on the same days.
In this pool, 20-day changes at 31 ordinary dates (Dec 2025 – Mar 2026) ranged from −30.9 to +13.8 bps. The premium
reached a route that does not go through an exchange order book, which is **consistent with** the bottleneck being
dollars entering Brazil rather than any one exchange. It is not an independent market: arbitrageurs who trade both the
pool and the exchanges keep their prices together, as triangular arbitrage does for bitcoin (F-018).

**Scale.** This pool is where on-chain BRLA–dollar trading happens (92% of the volume of the four BRLA–dollar pools with
data before the notice, 65% after, when the Gnosis pool's volume rose sixfold), but it is small: its volume was 0.35% of
Binance's USDT/BRL volume before and 0.24% after. The finding is that even this niche route paid the premium.

**Reais side** (spec 2, `403ca9d`, before those prices were downloaded). On a Curve pool where BRLA trades against BRZ,
another reais stablecoin (Transfero), BRLA's price in BRZ moved **−3.4 bps** (−2.5 → −5.9; naive 95% interval ±21.6,
days treated as independent) while the dollar route rose +111.0. So the stress was on the dollar side: BRLA did not
lose value against another reais token. This is not BRLA against fiat BRL (both tokens could move together), and BRLA
trades thinly there (US$ 1–4k a day), so daily values swing ±70 bps; it rules out only a reais-side move of more than
about 25 bps.

BRLA's circulating supply (DefiLlama) fell by 112 mn BRLA on Celo from 23 to 24 Jun, the largest one-day fall in the
series, but it **reversed a rise of 80 mn over the four days before** (Celo 128 → 208.5 mn, 19–23 Jun), and Celo supply was
back above its May level by August (monthly median 144 mn; 161 mn in November). No source says the fall was redemptions;
this finding does not call it a run.

## Evidence
Reproduce: restore the Flash bundle if needed (`data/README.md` → Flash mentor-leads bundle); spec-2 data with
`python scripts/p3_24_brla.py download` (or the frozen pulls in `data/raw/p3_24/`, checksums in SHA256SUMS); then
`python scripts/p3_24_brla.py` → `data/processed/P3-24_brla_daily.csv`, `results/tables/P3-24_brla_s20.csv`,
`results/figures/P3-24_brla_vs_usdt.png`. Spec committed before the script: `b57af33`.

| Series (S20 = mean 24 Jun–21 Jul minus mean 25 May–22 Jun, PTAX days) | Before | After | S20 | Binance S20, same days | Median daily volume before |
|---|---:|---:|---:|---:|---:|
| **Polygon pool, PTAX-window opens (primary)** | 34.9 | 145.9 | **+111.0** | +93.9 | US$ 189k |
| Polygon, USDC/USD measured in the window (r1) | 38.2 | 149.0 | +110.8 | +93.9 | US$ 189k |
| Polygon, daily close 21h Brasília (r2, F-034's timing) | 51.6 | 139.9 | +88.3 | +93.9 | US$ 189k |
| Gnosis pool USDC.e/BRLA, daily close (r3) | 28.0 | 122.8 | +94.9 | +93.9 | US$ 8k, **fails liquidity** |
| Base pool BRLA/USDC, daily close (r3) | – | – | not computed: 10 of 20 days before | – | US$ 2k, **fails liquidity**; contract not confirmed |

- **Scale (spec 2a, `results/tables/P3-24_scale.csv`; US$ volume summed over calendar days):** before 25 May–22 Jun:
  Polygon 5.88 mn, Gnosis 0.47 mn, Base 0.05 mn, Celo 0.004 mn (4 days with trades); Binance USDT/BRL 1,694 mn USDT.
  After 24 Jun–21 Jul: Polygon 5.26 mn, Gnosis 2.82 mn, Base 0.04 mn, Celo 0.003 mn (3 days); Binance 2,174 mn. Gnosis
  volume converted from BRLA at its own price; Base volume in USDC.
- **Reais side (spec 2b, `results/tables/P3-24_brl_side.csv`):** Curve pool `0xc89f…9735` (TESOURO / BRZ / stBRZ / BRLA,
  created 20 Nov 2025); BRLA price in BRZ = GeckoTerminal daily close US$ price of BRLA / that of BRZ in this pool
  (`currency=usd&token=<address>`; raw JSON in `data/raw/p3_24/`, pulled 5 Nov 04h UTC). Days with a value 18/20 before,
  19/20 after (testable). Mean −2.5 → −5.9 bps; daily sd 35.4 / 31.3; ranges −66..+66 and −73..+33. BRLA-side volume:
  median US$ 3.8k before, 0.8k after. Registered reading (|S20| ≤ 22 bps): "BRLA kept its value against BRZ". The
  pulls repeat 5 May (outside the windows); the loader keeps one candle per day.
- **Pool census (5 Nov, GeckoTerminal, D-19):** 31 BRLA pools on Polygon, Celo, Gnosis and Base. The Polygon USDC pool
  is the only BRLA–dollar pool that traded on most June days. Celo BRLA/USD₮ (Uniswap v3, `0x14e5…111a`) traded on 4 of 29
  days before and 3 of 28 after (median ~US$ 0.8–1k on those days): not testable. Curve pools (TESOURO/BRZ/stBRZ/BRLA,
  BRLA/BRZ/BRL1) swap reais tokens for reais tokens, not a dollar route. The rest hold under ~US$ 5k. The three pools
  in the table came from Felipe's bundle; the census was run after the result, at Renzo's question, and adds no testable pool.
- **Data checks:** every PTAX day in both windows has all 4 window hours; USDC/USD in the window 0.99967 before, 0.99970
  after (so r1 ≈ primary). Window prices more than 300 bps from Binance's BRL per USDC: 2 of 845, both on Saturday 6 Jun
  (not a PTAX day, not used). The route's level sits above Binance's (May mean 24.5 vs 10.9 bps; Aug–Sep 38.2 vs 28.3):
  pool fees and spread.
- **Pre-notice days:** the route averaged about 70 bps on 19–23 Jun (74.1, 70.4, 65.0), up from 28.0 on 18 Jun; Binance
  rose 37.7 bps on 18→19 Jun (F-029, the day Res. 574 was dated). The pool moves ±30 bps from day to day (15–18 Jun:
  52.0, 19.4, 55.8, 28.0), so this is weak evidence of anything before the notice. Those days sit in the "before" window,
  which makes S20 smaller, not larger.
- **Contracts:** CoinGecko's BRLA Digital record (homepage brla.digital, which redirects to avenia.io) lists Polygon
  `0xe6a5…ddfb` and Gnosis/Celo `0xfecb…3760` (D-20). The Base contract `0xfcb3…1783` is not in that record: unverified.
- **History limit:** GeckoTerminal's public API serves only the last 180 days; the series start (daily 7 Nov 2025,
  hourly 2 Apr 2026) is what Felipe's Flash agents saved on 4 Nov. Too short for placebo p-values (fewer than 250 PTAX days
  before 23 Jun), so the clean-date range is a description, not a test.
- **Supply (DefiLlama, million BRLA, Celo):** 19 Jun 128.3, 20 Jun 190.4, 23 Jun 208.5, 24 Jun 96.2, 26 Jun 59.3, 27 Jun 107.3,
  30 Jun 134.9. Daily moves of 50 mn or more: 2 in the 91 days before 24 Jun, 5 in the 134 after; none as large as 24 Jun.

## Caveats
- Assumes 1 BRLA = R$ 1 (Avenia mints and redeems at par via Pix); BRLA's own peg is not measured, and the word "depeg"
  is not used.
- One pool with about US$ 100k of liquidity (GeckoTerminal reserve, 5 Nov) and ~US$ 190k daily volume: a thin market,
  linked to the exchanges by arbitrage. USDC, not USDT.
- The supply series is DefiLlama's snapshot of circulating supply; mint/burn logs, bridge transfers and Avenia's treasury
  were not checked (Celoscan and Polygonscan refuse scripts). Who minted or burned, and why, is not identified.
- Retrospective: F-034 saw the jump first.

## Used in deck
Not yet. After Felipe's review (P3-24 S5), candidate line for slide 6 or the annex: "O prêmio também apareceu fora das
corretoras: comprar dólar pela rota Pix → BRLA → USDC ficou +111 pb mais caro no mês seguinte ao ofício (USDT na Binance:
+94 pb), enquanto o BRLA manteve seu valor frente a outro real digital (−3 pb). É uma rota pequena, ligada às
corretoras por arbitragem, como o bitcoin." Not to be said: "o BRLA desancorou", "corrida contra
o BRLA".

## History
- 2026-11-05, agent for Renzo: spec 2 added (scale, BRLA vs BRZ), at Renzo's request after the pool census
- 2026-11-05, agent for Renzo: created (P3-24 S3–S4); extends Felipe's F-034 first look

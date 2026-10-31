# Data

Not in git (see `.gitignore`), except this file. Anyone can rebuild `data/` with the download scripts.

```
data/raw/          downloaded files, never edited; checksums in data/raw/SHA256SUMS
data/processed/    derived tables, named PX-YY_<name>.csv after the task that made them
data/agentic_bundle/  frozen inputs for extension A (raw files + provider docs only)
```

## Manifest (filled by P1-01 and later download tasks)

| Pattern | Source | Coverage | Retrieved | Files | Script |
|---|---|---|---|---|---|
| `raw/binance/USDTBRL/*.zip` | https://data.binance.vision/data/spot/monthly/klines/USDTBRL/1h/ and `.../daily/...` | 2020-10-13 10h – 2026-10-30 23h UTC | 2026-10-31 | 102 | `scripts/p1_01_download.py` |
| `raw/binance/USDCUSDT/*.zip` | same, pair USDCUSDT | 2018-12-15 – 2026-10-30; **no data 2022-09-26 03h – 2023-03-11 13h UTC** | 2026-10-31 | 119 | `scripts/p1_01_download.py` |
| `raw/binance/BTCBRL/*.zip` | same, pair BTCBRL | 2020-10-13 10h – 2026-10-30 23h UTC | 2026-10-31 | 102 | `scripts/p1_01_download.py` |
| `raw/binance/BTCUSDT/*.zip` | same, pair BTCUSDT | 2017-08-17 – 2026-10-30 23h UTC | 2026-10-31 | 140 | `scripts/p1_01_download.py` |
| `raw/binance/BUSDUSDT/*.zip` | same, pair BUSDUSDT (fills the USDCUSDT gap; F-006) | 2019-09-20 08h – 2023-12-15 04h UTC (BUSD delisted) | 2026-10-31 | 52 | `scripts/p1_01_download.py` |
| `raw/coinbase/USDT-USD-1h.csv` | https://api.exchange.coinbase.com/products/USDT-USD/candles?granularity=3600 (300-hour chunks) | 2021-05-04 01h – 2026-10-30 23h UTC | 2026-10-31 | 1 | `scripts/p1_01_download.py` |
| `raw/foxbit/USDTBRL-1h.csv` | https://api.foxbit.com.br/rest/v3/markets/usdtbrl/candlesticks (500-hour chunks) | trades from 2021-04-07 03h; file 2020-10-01 – 2026-10-30 23h UTC | 2026-10-31 | 1 | `scripts/p1_03_second_venue.py` |
| `raw/mercadobitcoin/USDT-BRL-1h.csv` | https://api.mercadobitcoin.net/api/v4/candles?symbol=USDT-BRL&resolution=1h (30-day chunks) | 2023-03-11 22h – 2026-10-30 23h UTC | 2026-10-31 | 1 | `scripts/p1_03_second_venue.py` |
| `raw/binance/USDTTRY/*.zip` | same as USDTBRL, pair USDTTRY (P1-05 donor) | 2019-12-25 08h – 2026-10-30 23h UTC | 2026-10-31 | 112 | `scripts/p1_01_download.py USDTTRY` |
| `raw/binance/USDTZAR/*.zip` | same as USDTBRL, pair USDTZAR (P1-05 donor) | 2020-03-27 04h – 2026-10-30 23h UTC; **no data 2021-04-02 – 2023-06-09** | 2026-10-31 | 84 | `scripts/p1_01_download.py USDTZAR` |
| `raw/binance/USDTUAH/*.zip` | same as USDTBRL, pair USDTUAH (P1-05 donor) | 2020-06-24 06h – 2026-09-28 06h UTC (no October files) | 2026-10-31 | 76 | `scripts/p1_01_download.py USDTUAH` |
| `raw/binance/EURUSDT/*.zip` | same as USDTBRL, pair EURUSDT (P1-05 donor) | 2020-01-03 08h – 2026-10-30 23h UTC (quoted in USDT per EUR) | 2026-10-31 | 111 | `scripts/p1_01_download.py EURUSDT` |
| `raw/binance/USDTMXN/*.zip` | same as USDTBRL, pair USDTMXN (P1-05 donor) | 2024-04-10 00h – 2026-10-30 23h UTC | 2026-10-31 | 60 | `scripts/p1_01_download.py USDTMXN` |
| `raw/binance/USDTCOP/*.zip` | same as USDTBRL, pair USDTCOP (P1-05 donor) | 2024-06-05 15h – 2026-10-30 23h UTC | 2026-10-31 | 58 | `scripts/p1_01_download.py USDTCOP` |
| `raw/binance/USDTPLN/*.zip` | same as USDTBRL, pair USDTPLN (P1-05 donor) | 2023-04-14 08h – **2026-07-01 11h UTC** (pair ends) | 2026-10-31 | 40 | `scripts/p1_01_download.py USDTPLN` |
| `raw/binance/USDTIDR/*.zip` | same as USDTBRL, pair USDTIDR (P1-05 donor) | **2025-11-29 12h** – 2026-10-30 23h UTC | 2026-10-31 | 41 | `scripts/p1_01_download.py USDTIDR` |
| `raw/binance/USDTARS/*.zip` | same as USDTBRL, pair USDTARS (P1-05 donor) | 2023-04-28 12h – 2026-10-30 23h UTC | 2026-10-31 | 72 | `scripts/p1_01_download.py USDTARS` |
| `raw/fx_official/ecb_exr.csv` | https://data-api.ecb.europa.eu/service/data/EXR/D.USD+TRY+ZAR+MXN+PLN+IDR+BRL.EUR.SP00.A (csvdata) | 2020-01-02 – 2026-10-30, 1,751 days per currency | 2026-10-31 | 1 | `scripts/p1_05_donors.py` |
| `raw/fx_official/trm_cop.csv` | https://www.datos.gov.co/resource/32sa-8pi3.csv (TRM, Superfinanciera) | validity periods starting 2020-01-03 – 2026-10-30, 1,618 rows | 2026-10-31 | 1 | `scripts/p1_05_donors.py` |
| `raw/fx_official/nbu_uah.json` | https://bank.gov.ua/NBU_Exchange/exchange_site?valcode=usd&json | 2020-01-01 – 2026-10-30, every calendar day, 2,495 rows | 2026-10-31 | 1 | `scripts/p1_05_donors.py` |
| `raw/fx_official/bcra_a3500.json` | https://api.bcra.gob.ar/estadisticas/v4.0/Monetarias/5 (Com. A 3500) | 2020-01-02 – 2026-10-30, 1,658 business days | 2026-10-31 | 1 | `scripts/p1_05_donors.py` |
| `raw/bcb/ptax.json` | https://olinda.bcb.gov.br/olinda/servico/PTAX/versao/v1/odata/CotacaoDolarPeriodo (01-10-2020 to 10-30-2026) | 2020-10-01 – 2026-10-30, 1,527 days | 2026-10-31 | 1 | `scripts/p1_01_download.py` |

Notes:
- Checksums of every raw file: `data/raw/SHA256SUMS` (tracked in git). Check with `sha256sum -c data/raw/SHA256SUMS`.
- Binance files are the zips exactly as published (monthly up to 2026-09, daily for 1–30 Oct 2026), each
  verified against Binance's `.CHECKSUM`. Each holds one headerless CSV; read with `pd.read_csv(f, header=None)`.
- Binance kline timestamps are milliseconds up to 2024 and **microseconds** from 2025 (switch at the
  2025-01 file in every pair). Binance timestamps are UTC.
- Coinbase file: one row per hourly candle as the API returned it (`time_unix_utc` in seconds, low, high, open,
  close, volume in USDT); hours without trades have no row. Written by our script, so the checksum covers our
  serialisation of the API values.
- Foxbit file: one row per hour, field names from the docs. Hours without trades are rows of zeros: drop them
  (`volume_usdt > 0`). Foxbit's `open` is the previous candle's close (per its docs), not the first trade.
- Mercado Bitcoin file: `t` (hour start, Unix seconds UTC), `o` (first trade), `h`, `l`, `c`, `v` (USDT); hours
  without trades have no row.
- PTAX `dataHoraCotacao` is the **publication** time in Brasília time (UTC-3, no daylight saving since 2019),
  not the time of the four averaging windows. One date (2025-04-23) appears twice with identical rates.
- Official FX files (P1-05) are the API responses byte for byte; a re-download on 31 Oct 2026 gave identical files.
  ECB: rates per EUR, `TIME_PERIOD` = fix date (~14:10 CET). TRM: `vigenciadesde`/`vigenciahasta` = days the rate
  applies, COP per USD. NBU: `calcdate` = day the rate was calculated, `exchangedate` = day it applies (also weekends).
  BCRA: `fecha`, `valor` in ARS per USD.
- Coverage audit per pair: task P1-01 → Result, and `results/tables/P1-01_coverage.csv`.

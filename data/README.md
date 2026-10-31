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
- Coverage audit per pair: task P1-01 → Result, and `results/tables/P1-01_coverage.csv`.

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
| `raw/bcb/ptax.json` | https://olinda.bcb.gov.br/olinda/servico/PTAX/versao/v1/odata/CotacaoDolarPeriodo (01-10-2020 to 10-30-2026) | 2020-10-01 – 2026-10-30, 1,527 days | 2026-10-31 | 1 | `scripts/p1_01_download.py` |

Notes:
- Checksums of every raw file: `data/raw/SHA256SUMS` (tracked in git). Check with `sha256sum -c data/raw/SHA256SUMS`.
- Binance files are the zips exactly as published (monthly up to 2026-09, daily for 1–30 Oct 2026), each
  verified against Binance's `.CHECKSUM`. Each holds one headerless CSV; read with `pd.read_csv(f, header=None)`.
- Binance kline timestamps are milliseconds up to 2024 and **microseconds** from 2025 (switch at the
  2025-01 file in every pair). Binance timestamps are UTC.
- PTAX `dataHoraCotacao` is the **publication** time in Brasília time (UTC-3, no daylight saving since 2019),
  not the time of the four averaging windows. One date (2025-04-23) appears twice with identical rates.
- Coverage audit per pair: task P1-01 → Result, and `results/tables/P1-01_coverage.csv`.

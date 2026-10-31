# Data

Not in git (see `.gitignore`), except this file. Anyone can rebuild `data/` with the download scripts.

```
data/raw/          downloaded files, never edited; checksums in data/raw/SHA256SUMS
data/processed/    derived tables, named PX-YY_<name>.csv after the task that made them
data/agentic_bundle/  frozen inputs for extension A (raw files + provider docs only)
```

## Manifest (filled by P1-01 and later download tasks)

| Pattern | Source | Retrieved | Files | Script |
|---|---|---|---|---|
| `raw/binance/USDTBRL/*.csv` | data.binance.vision, spot 1h klines | | | `scripts/p1_01_download.py` |
| `raw/binance/USDCUSDT/*.csv` | data.binance.vision, spot 1h klines | | | `scripts/p1_01_download.py` |
| `raw/binance/BTCBRL/*.csv`, `raw/binance/BTCUSDT/*.csv` | data.binance.vision, spot 1h klines | | | `scripts/p1_01_download.py` |
| `raw/bcb/ptax.json` | BCB Olinda PTAX `CotacaoDolarPeriodo` | | | `scripts/p1_01_download.py` |

Notes: Binance kline timestamps are milliseconds before 2025 and **microseconds** from 2025.
PTAX timestamps are Brasília time; Binance timestamps are UTC.

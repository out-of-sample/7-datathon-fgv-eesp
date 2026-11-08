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
| `raw/binance/{USDC,BUSD,TUSD,UST,USTC,FDUSD,USDP}USDT/*.zip` | https://data.binance.vision/data/spot/monthly/klines/ | 2019-01-01 – 2026-09-30 UTC; pair-specific listing dates | 2026-10-31 | pair-specific | `scripts/p1_07_depeg.py` |
| `raw/bitstamp/USDC-USD-1h_2023-03-10_to_2023-03-14.csv` | https://www.bitstamp.net/api/v2/ohlc/usdcusd/ | 2023-03-10 00h – 2023-03-14 23h UTC | 2026-10-31 | 1 | `scripts/p1_07_depeg.py` |
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
| `raw/live/binance/{USDTBRL,USDCUSDT}/*-1h-YYYY-MM-DD.zip` | https://data.binance.vision/data/spot/daily/klines/ (P3-20 November pulls; kept apart from `raw/binance/` so core scripts never read them) | 2026-10-31 – the last published day | from 2026-11-05 | one per day | `scripts/p3_20_live.py download` |
| `raw/live/bcb/ptax_to_<UTC hour>.json` | BCB Olinda PTAX, 01-10-2026 to the pull date | 2026-10-01 – pull date | from 2026-11-05 | one per pull | `scripts/p3_20_live.py download` |
| `raw/live/{foxbit,mercadobitcoin}/*_to_<UTC hour>.csv` | same APIs as P1-03, from 2026-10-31 00h UTC to the last complete hour | per pull | from 2026-11-05 | one per pull | `scripts/p3_20_live.py download` |
| `raw/p3_24/*_<UTC hour>.json` | GeckoTerminal OHLCV, day, US$: Celo BRLA/USD₮ pool `0x14e5…111a`; Curve pool `0xc89f…9735` with `token=` BRLA and BRZ (P3-24 spec 2). Public API serves only the last 180 days | ~2026-05-05 – pull date | 2026-11-05 | 3 per pull | `scripts/p3_24_brla.py download` |
| `raw/p3_29/<provider>/*.json`, `raw/p3_29/<provider>/failed/*.json` | Celo JSON-RPC (Forno https://forno.celo.org, Ankr https://rpc.ankr.com/celo, Blockscout https://celo.blockscout.com/api/eth-rpc; probes 1rpc, Stakely, dRPC), Blockscout REST v2, DefiLlama https://stablecoins.llama.fi/stablecoin/365; Polygon (dRPC, Tenderly), Gnosis (gnosischain.com, gateway.fm), Moonbeam (dRPC, OnFinality) archive RPCs (T-22). One file per request: URL, request body, retrieval UTC, HTTP status, response. `failed/` holds refused or throttled calls as evidence (replayed offline, retried live) | BRLA on Celo: every proxy log 19 Jun 00:00:01 – 3 Jul 00:00 UTC 2026 and around 12 frozen S5 dates (Mar–Oct 2026); `totalSupply` at each 00:00 UTC boundary on Celo, Polygon, Gnosis, Moonbeam; DefiLlama v2 to 7 Nov (P3-29 S1–S5) | 2026-11-07 | 2,841 (89 MB) | `scripts/p3_29_reconcile.py smoke`, `ledger`, `cases`, `chains` |
| `raw/p3_28/<source_id>_<UTC>.{html,json}`, `raw/p3_28/failed/`, `raw/p3_28/manifest.csv` | Provider pages, help-centre API and BCB normativo API listed in `results/tables/P3-28_sources.csv` (snapshot=yes): Foxbit (A-01–A-10), Tether (A-11), BCB (E-14, E-06b), Blue Consult (E-20). One file per request, never overwritten; manifest: URL, retrieval UTC, HTTP status, SHA-256, document created/updated dates | current documents as retrieved (P3-28 S1, case D-01) | 2026-11-07 | 14 | `scripts/p3_28_access_map.py snapshot` |
| `raw/flash-mentor-leads/{brla,hyperliquid,b3-fx}/*` | GeckoTerminal, CoinGecko, BCB Olinda/SGS, DefiLlama, Hyperliquid info API, Yahoo Finance, Receita Federal (see the section below) | mostly 2026; per file | 2026-11-04 (Felipe's Flash agents) | 44 | none in the repo: snapshots; restore below |

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

## Flash mentor-leads bundle

Public-source snapshots gathered on 4 Nov 2026 by Felipe's Flash agents for the mentor leads (BRLA, Hyperliquid/EWZ,
B3/FX/Receita), first committed under `results/flash-mentor-leads/` in `79b71f1`, moved here on 5 Nov because raw data
stays out of git (`prompt.md` §6–§7). Files are byte-for-byte the originals: SHA-256 in `data/raw/SHA256SUMS` (and in
Felipe's `manifest.csv`). There is no download script, so the only copy outside Felipe's machine is git history.
**Restore** (from the repo root, once per clone):

```bash
git archive 79b71f1 results/flash-mentor-leads | tar -x -C data/raw --strip-components=1 --exclude=.gitattributes
grep flash-mentor-leads data/raw/SHA256SUMS | sha256sum -c --quiet && echo OK
```

| Folder | Sources and contents (from Felipe's bundle README) |
|---|---|
| `brla/` | GeckoTerminal pool OHLCV (Polygon BRLA/USDC pool `0x0e77…c956`, also Base and Gnosis pools), CoinGecko series, BCB Olinda PTAX, DefiLlama stablecoin ID 365, latest-block supply snapshots, and Flash merges (`*_merged_*`, `brla_*_supply_*`: derived by the Flash agents, no script in the repo) |
| `hyperliquid/` | Hyperliquid info API metadata, candles and funding; Yahoo EWZ daily and hourly bars. The spot "BRLA" ticker here is Brila Finance, not Avenia's BRLA |
| `b3-fx/` | BCB SGS FX and balance-of-payments series, Receita Federal August 2026 workbook (`criptoativos_dados_abertos_20260826.xls`) and derived reports, Yahoo Ibovespa/EWZ and CME BRL futures OHLCV |

New downloads for P3-24 go to new files under `data/raw/` (a script that re-downloads them is better than snapshots),
with checksums appended to `data/raw/SHA256SUMS`. Derived tables go to `data/processed/P3-24_*.csv`.


## P3-36 BRLA economic-function follow-up

New immutable responses: `data/raw/p3_36/` (273 JSON files; 1,891,863 bytes), with public historical Celo transaction/receipt/state calls, verified MiniVM source and five current Avenia documentation snapshots. `failed/` files preserve rejected probe requests; no private API or issuer outreach was used. The initial task number was P3-35; the published protocol renamed it P3-36.

To replay the exact snapshots, obtain the ignored `p3_29/` and `p3_36/` folders from Renzo's workspace. Verify their hashes against `data/raw/SHA256SUMS`; P3-36's manifests list every analysis input separately. Rebuild the input ledger with `P3_29_OFFLINE=1 python3 scripts/p3_29_reconcile.py ledger`, then run:

```bash
python3 scripts/p3_36_brla_operations.py --offline
python3 scripts/p3_36_brla_operations.py --documents --offline
```

Without `--offline`, missing public records/pages are downloaded; existing responses are never refreshed. Documentation can change, so a fresh download is not guaranteed to reproduce the frozen November text. The ledger's SHA-256 is recorded in `results/tables/P3-36_provenance.csv`. Both offline commands passed, and a second replay produced byte-identical tables; all manifest hashes were checked. F-049 remains subject to independent review.

Task-number coordination: this BRLA follow-up is finally P3-37; its P3-36 artifact prefixes are retained. See `tasks/P3-37-brla-economic-function.md`.

## P3-29 / P3-36 frozen on-chain bundle

`data/raw/p3_29/` (2,841 RPC/API answers), `data/raw/p3_36/` and `data/processed/P3-29_events.csv` (5.6 MB, git-ignored)
are not in git. One archive holds all three: `p3_29_p3_36_frozen_20261107.tar.gz`, 10,157,721 bytes, SHA-256
`ba98b6105582fe2f7626e0c8f7c876cf0dc07352e33d0db70d879ac9ed54080f`, attached to the GitHub release
[`data-p3-29-p3-36-20261107`](https://github.com/out-of-sample/7-datathon-fgv-eesp/releases/tag/data-p3-29-p3-36-20261107)
(private repo: team access). **Restore** (repo root):

```bash
gh release download data-p3-29-p3-36-20261107   # or download the asset from the release page
sha256sum p3_29_p3_36_frozen_20261107.tar.gz      # must print the hash above
tar -xzf p3_29_p3_36_frozen_20261107.tar.gz       # writes data/raw/p3_29, data/raw/p3_36, data/processed/P3-29_events.csv
grep 'p3_29\|p3_36' data/raw/SHA256SUMS | sha256sum -c --quiet && echo OK
P3_29_OFFLINE=1 .venv/bin/python scripts/p3_29_reconcile.py ledger   # also: cases, chains
.venv/bin/python scripts/p3_36_brla_operations.py --offline
git status --short                                 # empty = every committed output reproduced
```

Tested 7 Nov 2026 on a fresh clone of `f98f5bf` (with the Flash bundle restored as above): checksums OK, all four
commands ran, and no tracked file changed. Without the archive, `python scripts/p3_29_reconcile.py ledger` (live, no
key, ~4 min) rebuilds `P3-29_events.csv` from public endpoints. That is a re-download, not a replay of the frozen
answers: compare the outputs, not the raw file hashes, since each answer records its retrieval time.

## P3-44 access pilot checkpoint
Ignored `data/raw/p3_28_v2/` holds36 frozen public-source snapshots (including Felipe's image-only browser PDFs and fallible OCR), source/coder/adjudicator provenance,229-row AI references, old blocked v2 attempts and partial v3 runs. Local source archive: `P3-44_corpus_89e82bbb1cad6530.zip`; SHA-256 `99e794d2d78bdd72b11b8a15d820f4aab0ec7841f56250778ec0a1f5b3a555a9`. Obtain the folder from Felipe for exact replay; it is not committed or uploaded by this checkpoint. Source collection can be rerun, but current pages need not match frozen hashes. The source ZIP does not contain later references/runs. No final comparison score exists yet. See P3-44 Handoff for safe continuation and preserve every existing attempt.

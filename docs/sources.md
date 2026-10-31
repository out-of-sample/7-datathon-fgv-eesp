# Source register

Every number, date and claim in the deck must point to a row here. Add rows as you use new sources.
Status: **checked** (opened and confirmed by us, with date) or **[verify]** (not yet confirmed; not deck-ready).

## Data

| ID | Source | What | Access | Status |
|---|---|---|---|---|
| D-01 | Binance public data archive | Spot klines 1h: USDTBRL and BTCBRL (13 Oct 2020 – 30 Oct 2026), USDCUSDT (Dec 2018 – 30 Oct 2026, **no data 26 Sep 2022 – 11 Mar 2023**), BTCUSDT (Aug 2017 – 30 Oct 2026), donors. Gap fillers checked 31 Oct (F-006): BUSDUSDT (20 Sep 2019 – 15 Dec 2023, **frozen**), USDTDAI (Aug 2020 – Apr 2026), USDTUSD (Nov 2025 – ) | https://data.binance.vision ; listing via `https://s3-ap-northeast-1.amazonaws.com/data.binance.vision?prefix=data/spot/monthly/klines/<PAIR>/1h/&delimiter=/` | checked 30 Oct 2026 (coverage); frozen 31 Oct 2026 by P1-01 |
| D-02 | BCB Olinda PTAX API | `CotacaoDolarPeriodo`: PTAX buy/sell with timestamp | https://olinda.bcb.gov.br/olinda/servico/PTAX/versao/v1/odata/ | checked 30 Oct 2026 (Oct 2020 – 30 Oct 2026); frozen 31 Oct 2026 by P1-01 |
| D-03 | Kraken OHLCVT | USDT/USD direct quote | Kraken downloadable data: full archive ~10 GB (five 2 GB parts) through 30 Jun 2026 + quarterly files; API OHLC returns only the last 720 candles | checked 31 Oct 2026; not used (Coinbase/Bitstamp cover the need, F-006) |
| D-04 | Mercado Bitcoin / Foxbit public APIs | Second BRL venue for USDT | exchange API docs | [verify] |
| D-05 | Official FX for donor currencies | Daily fixes (central banks, FRED, ECB) | per currency | [verify] |
| D-07 | Coinbase Exchange public API | USDT/USD 1h candles, from 4 May 2021 | `https://api.exchange.coinbase.com/products/USDT-USD/candles?granularity=3600&start=..&end=..` (300 per call, no key) | checked 31 Oct 2026 (F-006); frozen 31 Oct 2026 by P1-01 (`data/raw/coinbase/USDT-USD-1h.csv`) |
| D-08 | Bitstamp public API | USDT/USD and USDC/USD 1h OHLC | `https://www.bitstamp.net/api/v2/ohlc/{usdtusd,usdcusd}/?step=3600&limit=1000&start=..` (no key) | checked 31 Oct 2026 (F-006); start dates not checked; not frozen yet |
| D-09 | The Block, 5 Sep 2022: "Binance to end support for USDC, two other stablecoins in favor of its own BUSD" | Cause of the USDCUSDT gap (auto-conversion from 29 Sep 2022) | https://www.theblock.co/post/167885/binance-to-end-support-for-usdc-other-stablecoins-in-favor-of-its-own-busd | secondary; Binance's own announcement not checked |
| D-06 | 2025 project repo | `raw_data/Y.csv` for the naive-baseline check | https://github.com/Renzo-Filho/6-datathon-fgv-eesp | checked 30 Oct 2026 |

## Events and regulation (Brazil)

| ID | Event | Source | Status |
|---|---|---|---|
| E-01 | 22 May 2025: decree raising IOF on FX operations | Diário Oficial da União | [verify] |
| E-02 | 10 Nov 2025: BCB Res. 519, 520, 521 published; in force 2 Feb 2026 | BCB communication reproduced at https://static.poder360.com.br/2025/11/bc-regulamenta-ativos-virtuais-funcionamento-10nov2025.pdf ; summary at https://www.barbieriadvogados.com/stablecoin-brasil/ | [verify] in BCB normative search |
| E-03 | Feb 2026: proposal of 3.5% IOF on crypto purchases | https://forbes.com.br/coluna/2026/02/governo-quer-taxar-criptomoedas-com-iof-o-que-isso-muda-para-o-investidor/ | [verify] status in Fazenda/Receita |
| E-04 | 4 May 2026: reporting obligation to the BCB | secondary news only | [verify] |
| E-05 | 23 Jun 2026: BCB notice to banks and funds on FX imports of virtual assets via funds; spread 0.1% → 0.7% | https://www.conjur.com.br/2026-jul-01/o-cerco-do-banco-central-as-stablecoins/ (opinion column) | [verify] primary or second source |
| E-06 | Res. BCB 561/2026 (eFX settlement) and proposed 24-hour hold on stablecoin transfers | same Conjur column | [verify] |

## Competition

| ID | Source | Status |
|---|---|---|
| C-01 | Event page: https://eesp.fgv.br/evento/7o-desafio-de-dados-datathon-de-moedas-digitais-da-fgv-eesp | checked 30 Oct 2026 |
| C-02 | Regulation: https://eesp.fgv.br/sites/default/files/uploads/regulamento-do-desafio-de-dados-de-moedas-digitais-fgv-2026_0.pdf | checked 30 Oct 2026 |
| C-03 | 2025 winners: https://eesp.fgv.br/sites/default/files/files-eesp/datathon_-_equipes_vencedoras_1_0.pdf ; jury: https://eesp.fgv.br/sites/default/files/files-eesp/datathon_-_comite_avaliador_1_0.pdf ; titles: https://eesp.fgv.br/centro-de-estudos/fgv-digital-finance | checked 30 Oct 2026 |
| C-04 | 2022–2024 winners and decks: edition pages under https://eesp.fgv.br/evento/ | checked 30 Oct 2026 |

## Literature

See the "Literature anchors" sections of `02-dolar-cripto.md`, `01-depeg-recovery.md` and the references in
`05-agentic-robustness.md`. Mark a reference **checked** only after opening it.

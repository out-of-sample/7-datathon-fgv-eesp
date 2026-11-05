# P5-01 Flash data snapshots

These are the public-source CSV, JSON and Receita XLS files gathered by the Antigravity Flash workstreams on 4 November Brasília time (some files extend into 5 November UTC). Copies are byte-for-byte from the scratch outputs. The manifest records their SHA-256 checksums. This exploratory bundle includes raw snapshots and Flash-derived tables with known limitations. See the [audit](../../docs/flash-findings-mentor-leads.md) before using any file.

| Directory | Sources and contents |
|---|---|
| brla | GeckoTerminal pool OHLCV, CoinGecko series, BCB Olinda PTAX, DefiLlama stablecoin ID 365, latest-block contract supply snapshots, and Flash merges |
| hyperliquid | Hyperliquid info API metadata, candles and funding, plus Yahoo EWZ daily and hourly bars. The spot BRLA ticker here is Brila Finance. |
| b3-fx | BCB SGS FX and balance-of-payments data, Receita Federal August 2026 XLS and derived reports, Yahoo Ibovespa/EWZ and CME BRL futures OHLCV |

Source endpoints: [GeckoTerminal](https://api.geckoterminal.com/api/v2), [CoinGecko](https://www.coingecko.com/), [BCB PTAX](https://olinda.bcb.gov.br/olinda/servico/PTAX/versao/v1/aplicacao#!/recursos), [BCB SGS](https://www3.bcb.gov.br/sgspub/), [DefiLlama supply](https://stablecoins.llama.fi/stablecoin/365), [Hyperliquid info API](https://api.hyperliquid.xyz/info), [Yahoo Finance](https://finance.yahoo.com/), [Receita workbook](https://www.gov.br/receitafederal/pt-br/assuntos/orientacao-tributaria/declaracoes-e-demonstrativos/criptoativos/arquivos/criptoativos_dados_abertos_20260826.xls).

Verify file integrity from this directory with PowerShell:

```powershell
Import-Csv manifest.csv | ForEach-Object {
    if ((Get-FileHash -LiteralPath $_.file).Hash -ne $_.sha256) {
        throw "Checksum mismatch for $($_.file)"
    }
}
```

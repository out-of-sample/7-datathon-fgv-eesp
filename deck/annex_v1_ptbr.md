# Anexos Metodológicos e Registro de Evidências
## Quanto Custa Fechar a Porta? O Prêmio do Dólar Digital no Brasil e os Limites à Arbitragem

**Documento Suplementar Oficial — 7º Datathon de Moedas Digitais FGV EESP (Novembro de 2026)**  
**Equipe Out of Sample:** CS 1 (Renzo), CS 2 (Nattan), CS 3 (Jonathan), Economista (Felipe)  

---

### Estrutura dos Anexos
- **Anexo A:** Tabela Completa de Eventos Regulatórios e Microestruturais Brasileiros (Placebo $p$-valores)
- **Anexo B:** Bateria Completa de Robustez, Sensibilidade, Custos por Rota (Opção A) e Depegs em Dólar
- **Anexo C:** Registro Completo de Fontes de Dados, Legislação, Tarifas, Eventos de Depeg e Literatura
- **Anexo D:** Mapa de Reprodutibilidade de Scripts e Matriz de Rastreabilidade Ponta a Ponta (14 Slides / 15 Seções)
- **Anexo E:** Declaração Transparente de Uso de Ferramentas e Agentes de Inteligência Artificial

---

# Anexo A — Tabela Completa de Eventos Regulatórios e de Mercado no Brasil

Este anexo consolida todos os 13 eventos regulatórios, tributários e de microestrutura coletados pela equipe (`P1-04`, `data/processed/P1-04_events_brazil.csv`), avaliados por meio de estudo de eventos em janelas de $\pm 20$ dias úteis PTAX em torno de $t_0$ (`P2-03`, `results/tables/P2-03_event_table.csv`, `F-016`).

**Regra de Inferência (`prompt.md` §5):** Como o prêmio é persistente em níveis dentro de janelas de 40 dias úteis, testes $t$ paramétricos (mesmo com correção HAC Newey-West de 5 defasagens) rejeitam com frequência excessiva em datas comuns. Por essa razão, **reportamos exclusivamente os $p$-valores empíricos contra datas placebo** — tanto sobre todas as **1.073 datas limpas** fora de janelas de eventos (`p_placebo_all_clean_2s`) quanto sobre o sorteio aleatório pré-especificado de **200 datas limpas** (`p_placebo_2s`, `seed = 20261102`). Eventos de microestrutura (`M-01` a `M-04`) **coincidem no tempo** com mudanças na série, mas não provam causalidade.

| ID | Tipo / Relação | Data Avaliada ($t_0$ PTAX) | Média Pré (bps) | Média Pós (bps) | Variação (bps) | Erro HAC (bps) | $p$ Placebo (1.073 Datas Limpas) | $p$ Placebo (200 Sorteios) | Percentil Placebo | RMSE Persistência | RMSE Pós-Evento | Fonte Primária / Verificação Aberta (`docs/sources.md`) |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| **E-01** | Tributário (Anúncio) | 2025-05-22 | 26,91 | 40,09 | +13,18 | 1,95 | 0,3845 | 0,4030 | 79,0% | 17,05 | 10,82 | [Decreto nº 12.466/2025](https://www.planalto.gov.br/ccivil_03/_ato2023-2026/2025/decreto/d12466.htm) |
| **E-01** | Tributário (Vigência) | 2025-05-23 | 26,21 | 41,65 | +15,44 | 2,18 | 0,3147 | 0,3383 | 81,5% | 18,10 | 9,45 | [Decreto nº 12.467/2025](https://www.planalto.gov.br/ccivil_03/_ato2023-2026/2025/decreto/d12467.htm) |
| **E-01b** | Tributário / Judicial (Anúncio) | 2025-06-27 | 39,92 | 16,00 | -23,92 | 5,55 | 0,1648 | 0,1940 | 8,5% | 31,10 | 19,88 | [Decreto Legislativo nº 176/2025](https://legis.senado.leg.br/norma/41240559/publicacao/41241630) |
| **E-01b** | Tributário / Judicial (Vigência) | 2025-07-04 | 37,57 | 12,69 | -24,88 | 4,89 | 0,1527 | 0,1841 | 8,0% | 29,92 | 16,61 | [STF MC na ADC 96](https://portal.stf.jus.br/noticias/verNoticiaDetalhe.asp?idConteudo=588751&ori=1) |
| **E-02** | Regulatório SPSAV (Anúncio) | 2025-11-10 | 13,25 | 9,46 | -3,79 | 3,88 | 0,7477 | 0,7214 | 39,5% | 8,62 | 7,75 | [Resoluções BCB nº 519–521/2025](https://www.bcb.gov.br/estabilidadefinanceira/exibenormativo?tipo=Resolu%C3%A7%C3%A3o%20BCB&numero=521) |
| **E-02** | Regulatório SPSAV (Vigência) | 2026-02-02 | 8,43 | 4,12 | -4,31 | 1,68 | 0,7225 | 0,6965 | 38,0% | 6,88 | 5,36 | [Resolução BCB nº 521/2025](https://www.bcb.gov.br/estabilidadefinanceira/exibenormativo?tipo=Resolu%C3%A7%C3%A3o%20BCB&numero=521) |
| **E-03** | Proposta Tributária (Anúncio) | 2026-02-05 | 7,63 | 5,51 | -2,11 | 1,92 | 0,8408 | 0,8458 | 46,5% | 6,24 | 5,87 | [Minuta Fazenda / Receita (Forbes/Valor)](https://forbes.com.br/forbes-money/2026/02/governo-avalia-cobrar-iof-sobre-transacoes-com-stablecoins/) |
| **E-03** | Proposta Tributária (Vigência) | N/A | — | — | — | — | — | — | — | — | — | Minuta não promulgada (`unenacted_draft`) |
| **E-04** | Reporte Regulatório (Anúncio) | 2025-11-10 | 13,25 | 9,46 | -3,79 | 3,88 | 0,7477 | 0,7214 | 39,5% | 8,62 | 7,75 | [Art. 4º Res. BCB nº 521/2025](https://www.bcb.gov.br/estabilidadefinanceira/exibenormativo?tipo=Resolu%C3%A7%C3%A3o%20BCB&numero=521) |
| **E-04** | Reporte Regulatório (Vigência) | 2026-05-04 | 4,65 | 11,89 | +7,24 | 2,92 | 0,6145 | 0,6119 | 72,0% | 12,10 | 9,69 | [Art. 4º Res. BCB nº 521/2025](https://www.bcb.gov.br/estabilidadefinanceira/exibenormativo?tipo=Resolu%C3%A7%C3%A3o%20BCB&numero=521) |
| **E-05** | **Supervisão BCB (Vigência)** | **2026-06-23** | **15,24** | **109,14** | **+93,91** | **16,18** | **0,0009** | **0,0050** | **100,0%** | **103,08** | **42,51** | [ConJur 01/jul](https://www.conjur.com.br/2026-jul-01/o-cerco-do-banco-central-as-stablecoins/) · [Cointelegraph 06/jul](https://br.cointelegraph.com/news/central-bank-intensifies-crackdown-and-ban-sends-stablecoin-operations-into-tailspin-in-brazil) · [Webitcoin LAI 30/jul](https://webitcoin.com.br/banco-central-esclarece-proibicao-de-fundos-comprarem-cripto-no-exterior-175059/) |
| **E-06a** | Regulatório eFX (Anúncio) | 2026-04-30 | 4,87 | 10,91 | +6,04 | 3,16 | 0,6471 | 0,6219 | 71,5% | 11,54 | 9,83 | [Resolução BCB nº 561/2026](https://www.bcb.gov.br/estabilidadefinanceira/exibenormativo?tipo=Resolu%C3%A7%C3%A3o%20BCB&numero=561) |
| **E-06a** | Regulatório eFX (Vigência) | 2026-10-01 | 22,79 | 17,48 | -5,31 | 7,18 | 0,6778 | 0,6617 | 35,5% | 22,00 | 21,35 | [Art. 50 Res. BCB nº 277](https://www.bcb.gov.br/estabilidadefinanceira/exibenormativo?tipo=Resolu%C3%A7%C3%A3o%20BCB&numero=561) |
| **E-06b** | Retenção 24h (Anúncio) | 2026-08-07 | 53,33 | 31,34 | -21,99 | 8,03 | 0,1872 | 0,2189 | 9,0% | 23,48 | 8,24 | [Resolução BCB nº 584/2026](https://www.bcb.gov.br/estabilidadefinanceira/exibenormativo?tipo=Resolu%C3%A7%C3%A3o%20BCB&numero=584) |
| **E-06b** | Retenção 24h (Vigência) | 2027-01-01 | — | — | — | — | — | — | — | — | — | Fora da amostra (`outside_sample_future`, vigência em 01/01/2027) |
| **E-07** | Interrupção Pix (Vigência) | 2022-06-17 | 53,23 | 48,53 | -4,70 | 7,69 | 0,7039 | 0,6866 | 37,0% | 22,55 | 22,06 | [Suspensão Pix Capitual (The Block)](https://www.theblock.co/post/156492/binance-resumes-withdrawals-and-deposits-in-brazilian-reais) |
| **M-01** | Coincide com corte de alavancagem | 2021-07-26 | 77,88 | 61,02 | -16,86 | 11,08 | 0,2700 | 0,2985 | 13,0% | 38,36 | 34,45 | [Corte Alavancagem 20x Binance (CoinDesk)](https://www.coindesk.com/markets/2021/07/26/binance-reduces-maximum-futures-leverage-to-20x) |
| **M-02** | Coincide com Termo CVM | 2024-08-13 | 55,40 | 42,31 | -13,10 | 18,89 | 0,3855 | 0,4030 | 19,0% | 23,25 | 19,21 | [Termo de Compromisso CVM R$ 9,6 mi (InfoMoney)](https://www.infomoney.com.br/onde-investir/cvm-encerra-processo-contra-binance-apos-acordo-de-r-96-milhoes/) |
| **M-03** | Coincide com corte de tick size | 2025-06-27 | 39,92 | 16,00 | -23,92 | 5,55 | 0,1648 | 0,1940 | 8,5% | 31,10 | 19,88 | [Tick Size 0,0001 BRL Binance (`exchangeInfo`)](https://data-api.binance.vision/api/v3/exchangeInfo?symbol=USDTBRL) |
| **M-04** | Coincide com parceria NovaDAX | 2026-07-07 | 70,95 | 60,44 | -10,51 | 28,55 | 0,4888 | 0,4876 | 24,0% | 25,68 | 23,43 | [Parceria Foxbit–NovaDAX (Livecoins)](https://livecoins.com.br/foxbit-fecha-parceria-com-a-novadax-que-vai-encerrar-operacoes-no-brasil/) |

---

# Anexo B — Bateria Completa de Robustez, Custos por Rota (Opção A) e Depegs

### B.1. Sensibilidade de Janelas Temporais e Avaliação do Nível Pós-Pico (`P4-01`, `F-022`)
Extraído integralmente da Dimensão 1 de `results/tables/P4-01_robustness.csv`. O pico agudo é robusto de **+73,70 a +128,28 bps** em todas as janelas, enquanto o nível após o arrefecimento de 22/jul (`[+21, +60]` = +19,31 bps; `[+21, fim]` = +11,54 bps) apresenta **$p_{\text{placebo}} = 0,239$** contra todas as 882 datas limpas (e $p_{\text{placebo}} = 0,140$ contra as 85 datas limpas de 2025 em diante), **não sendo estatisticamente distinguível de oscilação ordinária**:

| Especificação de Janela (`P4-01_robustness.csv`) | Tipo | Média Pré (bps) | Média Pós (bps) | Efeito / Diferença (bps) | Erro HAC / Dispersão Placebo | Inferência Placebo / Notas |
|---|---|---:|---:|---:|---|---|
| **$[-10, -1]$ vs $[+1, +10]$ dias PTAX** | Pico Agudo | 12,50 | 140,78 | **+128,28** | SE HAC: 7,55 bps ($t = 17,00$) | Acima de 100% dos placebos |
| **$[-15, -1]$ vs $[+1, +15]$ dias PTAX** | Pico Agudo | 12,96 | 125,94 | **+112,97** | SE HAC: 9,67 bps ($t = 11,68$) | Acima de 100% dos placebos |
| **$[-20, -1]$ vs $[+1, +20]$ dias PTAX (Oficial)** | **Pico Agudo** | **15,24** | **109,14** | **+93,91** | **SE HAC: 16,18 bps ($t = 5,80$)** | **$p_{\text{placebo}} = 0,0009$ (1.073 limpas) / $0,0050$ (200 sorteios)** |
| **$[-30, -1]$ vs $[+1, +30]$ dias PTAX** | Pico Agudo | 13,52 | 87,22 | **+73,70** | SE HAC: 17,12 bps ($t = 4,30$) | Acima de 100% dos placebos |
| **Pré-período limpo (01/abr–22/mai) vs $[+1, +20]$** | Pico Agudo | 5,74 | 109,14 | **+103,41** | SE HAC: 16,09 bps ($t = 6,43$) | Exclui pré-tendência de +9,5 bps após IOF de maio |
| **Pós-pico $[+21, +60]$ (22/jul–16/set) vs $[-20, -1]$** | Pós-Pico | 15,24 | 34,54 | **+19,31** | DP placebo: 16,5 bps ($n = 882$) | **$p_{\text{placebo}} = 0,239$ (todas limpas) — não significativo** |
| **Pós-pico $[+21, +60]$ vs placebos de 2025+** | Pós-Pico | 15,24 | 34,54 | **+19,31** | DP placebo: 8,1 bps ($n = 85$) | **$p_{\text{placebo}} = 0,140$ (limpas 2025+) — não significativo** |
| **Pós-pico $[+21, \text{fim}]$ (22/jul–30/out, 71d) vs $[-20, -1]$** | Pós-Pico | 15,24 | 26,78 | **+11,54** | SE HAC: 3,97 bps ($t = 2,91$) | Nível pós-pico dentro da oscilação histórica normal |

### B.2. Confirmação em Três Corretoras Independentes no Brasil (`P2-05`, `P4-01` Dimensão 3, `F-009`)
Comparação entre os livros de ofertas domésticos de `USDT/BRL` na janela oficial de 20 dias PTAX (25/mai–22/jun vs 24/jun–21/jul) e na janela restrita aos 16 dias PTAX de junho (01/jun–22/jun):

| Corretora | Pré 20d (bps) | Pós 20d (bps) | Salto 20d (bps) | Pré 16d Jun (bps) | Salto 16d Jun (bps) | Pico 24/jun (bps) | Pico 25/jun (bps) |
|---|---:|---:|---:|---:|---:|---:|---:|
| **Binance (Líder Global/Local)** | 15,24 | 109,14 | **+93,91** | 12,96 | **+96,18** | 155,4 | 184,4 |
| **Foxbit (Nacional)** | 14,70 | 108,00 | **+93,30** | 12,85 | **+95,17** | 152,1 | 184,8 |
| **Mercado Bitcoin (Nacional)** | 10,70 | 105,60 | **+94,90** | 7,13 | **+98,50** | 147,9 | 155,7 |
| **Composto Igual-Ponderado (3 Venues)** | **13,55** | **107,58** | **+94,03** | **10,98** | **+96,62** | **151,8** | **175,0** |

### B.3. Teste Cego de Quebras Estruturais de Bai-Perron e Intervalos de Confiança (`P2-02`, `P4-01` Dimensão 4, `F-011`)
Comparação entre o estimador homocedástico agrupado (Teorema 1 de Bai 1997) e o estimador heterocedástico assimétrico específico por regime (Teorema 2 de Bai 1997) para a quebra de subida em 24/jun e o arrefecimento não explicado em 22/jul:

| Série Avaliada | Quebra Detectada | Salto de Regime (bps) | IC 95% Homocedástico Agrupado | IC 95% Heterocedástico por Regime | Evento Coincidente ($\pm 5$ dias úteis) |
|---|---|---:|---|---|---|
| **Principal (`premium_bps`)** | **2026-06-24** | **+99,83** (9,32 $\to$ 109,14) | `[2026-06-18 .. 2026-06-30]` ($\pm 3,1\text{d}$) | **`[2026-06-23 .. 2026-06-30]` ($-0,1\text{d} / +3,9\text{d}$)** | `E-05` (23/06/2026, $-1$ dia útil) |
| **Principal (`premium_bps`)** | **2026-07-22** | **-82,36** (109,14 $\to$ 26,78) | `[2026-07-15 .. 2026-07-29]` ($\pm 4,6\text{d}$) | **`[2026-07-14 .. 2026-07-23]` ($-5,7\text{d} / +0,9\text{d}$)** | **Nenhum evento em $\pm 5\text{d}$ (não explicado)** |
| **Ajuste Direto Coinbase (`premium_cb_bps`)** | 2026-06-24 | +101,31 (10,91 $\to$ 112,22) | `[2026-06-22 .. 2026-06-26]` ($\pm 1,9\text{d}$) | `[2026-06-23 .. 2026-06-30]` ($-0,1\text{d} / +3,9\text{d}$) | `E-05` (23/06/2026, $-1$ dia útil) |
| **Fechamento 23h59 UTC (`premium_dayclose_bps`)** | 2026-06-23 | +90,02 (25,32 $\to$ 115,34) | `[2026-06-12 .. 2026-07-02]` ($\pm 6,3\text{d}$) | `[2026-06-17 .. 2026-06-30]` ($-3,7\text{d} / +4,2\text{d}$) | `E-05` (23/06/2026, $0$ dias úteis) |

### B.4. Matriz Completa de Especificações do Controle Sintético (`P2-04`, `P4-01` Dimensão 5, `F-017`)
Todas as 6 especificações de controle sintético e DiD (`results/tables/P2-04_synth_results.csv` e `P4-01_robustness.csv`). Nota: o gap pós-pico (+28,16 a +33,94 bps) não é distinguível de oscilação ordinária ($p_{\text{placebo}} = 0,24$, `F-022`):

| Especificação | Doadores | Pré-RMSPE (bps) | Gap Agudo 20d (bps) | Gap Pós-Pico (bps) | Razão RMSPE Pós/Pré | Rank Placebo | Permutação $p$ |
|---|---|---:|---:|---:|---:|---|---|
| **Headline (5 doadores, PTAX)** | **EUR, MXN, TRY, ZAR, COP** | **7,05** | **+109,31** | +28,16 | **9,31** | **1 de 6** | **0,167** |
| **4 doadores ex-EUR (PTAX)** | TRY, ZAR, MXN, COP | 10,33 | **+116,69** | +33,94 | 6,90 | 1 de 5 | 0,200 |
| **6 doadores c/ IDR desde dez/2025** | EUR, TRY, ZAR, MXN, COP, IDR | 7,19 | **+109,87** | +28,58 | 9,20 | 1 de 7 | 0,143 |
| **Mesmo Horário Fix ECB (14:00 CET)** | EUR, TRY, ZAR, MXN, COP | 16,58 | **+101,57** | +32,32 | 3,94 | 1 de 6 | 0,167 |
| **Excluindo 18 segundas festivas da Colômbia** | EUR, MXN, TRY, ZAR, COP | 6,98 | **+109,54** | +28,31 | 9,44 | 1 de 6 | 0,167 |
| **DiD Igual-Ponderado (5 doadores)** | EUR, TRY, ZAR, MXN, COP | — | **+103,34** | +31,40 | — | — | — |

### B.5. Tabela Completa de Custos de Transação por Rota para US$ 100.000 (`P3-01`, `F-015` — Opção A para a Equipe)
Esta seção preserva a tabela integral de 17 linhas de `results/tables/P3-01_route_costs.csv` (à cotação de referência R$ 5,38/US$, US$ 100.000 = R$ 538.000) com parâmetros validados em fontes primárias abertas (`R-01` a `R-07`), caso a equipe opte pela **Opção A** no Slide 10 (manter apenas o custo do ofício no slide principal e remeter a comparação institucional para este anexo):

| ID da Rota | Categoria | Regime / Cenário | Corretora / Canal | Prêmio (bps) | Spread / Taxa (bps) | SWIFT / Rede (bps) | IOF / Carry (bps) | Total (bps) | Custo Total (R$ / US$ 100k) | IOF Bancário Vigente | Notas e Fontes Primárias (`docs/sources.md`) |
|---|---|---|---|---:|---:|---:|---:|---:|---:|---:|---|
| `NOTICE_COST_SPIKE` | **Custo do Ofício** | **Pico Agudo: 24/jun–21/jul/2026** | **Binance (VIP0)** | **+93,9** | **0,0** | **0,0** | **0,0** | **93,9** | **R$ 5.052,36** | — | **Efeito medido do ofício E-05 (`F-016`, $p_{\text{placebo}} \approx 0,001$)** |
| `NOTICE_COST_AFTER` | Custo do Ofício | Pós-Pico: 22/jul–30/out/2026 | Binance (VIP0) | +11,5 | 0,0 | 0,0 | 0,0 | 11,5 | R$ 621,00 | — | Não distinguível de ruído (`F-022`, $p_{\text{placebo}} = 0,24$) |
| `BANK_IMPORT_0IOF` | Rota Bancária | Importação de Mercadorias (0% IOF) | Banco Comercial | 0,0 | 20,0 | 2,5 | 0,0 | **22,5** | **R$ 1.210,50** | 0,0% | RIOF Art. 15-B, I (`R-02`); spread PJ 20 bps (`R-01`; 52,5 bps c/ 50 bps); SWIFT US$ 25 (`R-01b`) |
| `BANK_INVEST_11IOF` | Rota Bancária | Investimento / Disp. pré-mai/2025 (1,1% IOF) | Banco Comercial | 0,0 | 20,0 | 2,5 | 110,0 | **132,5** | **R$ 7.128,50** | 1,1% | Dec. 12.467/2025 (`R-02`); spread PJ 20 bps (`R-01`; 162,5 bps c/ 50 bps) |
| `BANK_AVAIL_35IOF` | Rota Bancária | Disponibilidade pós-23/mai/2025 (3,5% IOF) | Banco Comercial | 0,0 | 20,0 | 2,5 | 350,0 | **372,5** | **R$ 20.040,50** | 3,5% | Dec. 12.466/2025 e STF ADC 96 (`R-02`, `R-03`; 402,5 bps c/ 50 bps) |
| `USDT_REGIME_1` | Rota USDT | Regime 1: out/2020–jul/2021 | Binance (VIP0) | 91,3 | 10,0 | 0,1 | 0,0 | **101,4** | **R$ 5.455,32** | 1,1% | Regime 1 (`F-011`); IOF bancário vigente à época = 1,1% (`R-02`) |
| `USDT_REGIME_2` | Rota USDT | Regime 2: jul/2021–ago/2024 | Binance (VIP0) | 54,5 | 10,0 | 0,1 | 0,0 | **64,6** | **R$ 3.475,48** | 1,1% | Regime 2 (`F-011`); IOF bancário vigente à época = 1,1% (`R-02`) |
| `USDT_REGIME_3` | Rota USDT | Regime 3: ago/2024–jul/2025 | Binance (VIP0) | 34,9 | 10,0 | 0,1 | 0,0 | **45,0** | **R$ 2.421,00** | 1,1% | Regime 3 (`F-011`); 1,1% vigente em ~9,5 dos 11 meses (`R-02`) |
| `USDT_REGIME_4` | Rota USDT | Regime 4: jul/2025–22/jun/2026 (Pré-Ofício) | Binance (VIP0) | 9,3 | 10,0 | 0,1 | 0,0 | **19,4** | **R$ 1.043,72** | 3,5% | Pós-corte de tick (`M-03`, `F-007`); menor fricção histórica |
| `USDT_REGIME_5` | Rota USDT | Regime 5: 24/jun–21/jul/2026 (Pico 20d) | Binance (VIP0) | 109,1 | 10,0 | 0,1 | 0,0 | **119,2** | **R$ 6.412,96** | 3,5% | Pós-ofício BCB (`E-05`, `F-011`) |
| `USDT_PEAK` | Rota USDT | Pico de 48h: 24–25/jun/2026 | Binance (VIP0) | 169,9 | 10,0 | 0,1 | 0,0 | **180,0** | **R$ 9.682,66** | 3,5% | Média dos picos de 24/jun (155,4 bps) e 25/jun (184,4 bps, `F-009`) |
| `USDT_REGIME_6` | Rota USDT | Regime 6: 22/jul–out/2026 (Pós-Pico) | Binance (VIP0) | 26,8 | 10,0 | 0,1 | 0,0 | **36,9** | **R$ 1.985,22** | 3,5% | Nível pós-pico (`F-011`; diferença pós-pico não significativa, `F-022`) |
| `USDT_REGIME_6_FOXBIT` | Rota USDT | Regime 6: Foxbit VIP 6–7 Taker | Foxbit | 26,8 | 8,0 | 0,2 | 0,0 | **35,0** | **R$ 1.883,00** | 3,5% | Taxa taker VIP 6–7 (R$ 5M–25M) = 7–9 bps, ponto médio 8,0 bps (`R-05`) |
| `USDT_REGIME_6_MB` | Rota USDT | Regime 6: Mercado Bitcoin VIP Maker | Mercado Bitcoin | 26,8 | 6,0 | 0,2 | 0,0 | **33,0** | **R$ 1.775,40** | 3,5% | 6,0 bps é taxa *maker* VIP (>R$ 10M); *taker* ativo (R$ 500k–10M) é **60,0 bps = 87,0 bps total** (`R-06`) |
| `SCENARIO_S1_IOF35` | Cenário | Cenário S1: IOF de 3,5% sobre Cripto | Binance (VIP0) | 26,8 | 10,0 | 0,1 | 350,0 | **386,9** | **R$ 20.815,22** | 3,5% | Minuta não promulgada (`E-03`, `R-02`) sobre base do Regime 6 |
| `SCENARIO_S2A_HOLD_HEDGED` | Cenário | Cenário S2a: Retenção 24h c/ Hedge CIP | Binance (VIP0) | 26,8 | 10,0 | 0,1 | 2,5 | **39,4** | **R$ 2.119,72** | 3,5% | Res. BCB 584/2026 (`R-07`): carry CIP 1 dia $(\text{CDI } 10,75\% - \text{SOFR } 5,00\%)/252 + \text{B3} = 2,5\text{ bps}$ |
| `SCENARIO_S2B_HOLD_UNHEDGED` | Cenário | Cenário S2b: Retenção 24h s/ Hedge | Binance (VIP0) | 26,8 | 10,0 | 0,1 | 0,0 | **36,9** | **R$ 1.985,22** | 3,5% | Custo esperado 0 bps, mas risco cambial PTAX de 1 dia (95% VaR) de **130 bps** (`R-07`, `P1-02`) |

**Ressalvas de Não-Equivalência Jurídica e Operacional (`docs/02-dolar-cripto.md` §10):**
1. A remessa bancária comercial entrega dólares fiduciários (USD) em conta bancária no exterior com contrato de câmbio liquidado no Sistema de Câmbio do BCB; a rota USDT entrega um token privado em blockchain emitida pela Tether.
2. O diferencial bruto entre uma rota bancária com 3,5% de IOF e uma rota cripto sem IOF **não é "economia" de eficiência tecnológica**: quase toda a diferença advém do tratamento tributário distinto sob o Decreto nº 6.306/2007 (RIOF), objeto de debate público (`E-03`).
3. A partir de 02/02/2026 (Resoluções BCB nº 519–521/2025, `E-02`) e 04/05/2026 (`E-04`), pagamentos e transferências internacionais com ativos virtuais por SPSAVs integram formalmente o mercado de câmbio (limite de US$ 100.000 quando a contraparte não é instituição autorizada a operar em câmbio).
4. Para importação de mercadorias (0% IOF, **22,5 bps = R$ 1.210,50**), a rota bancária tradicional é mais barata ou equivalente ao USDT em todos os regimes históricos exceto o Regime 4.

### B.6. Tabela Completa dos 12 Episódios de Depeg em Dólar (`P3-04`, `P3-09`, `F-019`) e Band-TAR (`P3-07`, `F-021`)

**Tabela Completa de Casos de Queda Abaixo de US$ 1,00 (`results/tables/P3-04_depeg_case_table.csv`):**

| ID do Caso | Moeda | Categoria | Início (UTC) | Duração (h) | Mínimo Horário (US$) | Desvio Máx. (bps) | Status | Mecanismo Verificado em Fonte Primária Aberta (`DP-01` a `DP-10`, `D-13`) |
|---|---|---|---|---:|---:|---:|---|---|
| `CASE-USDC-SVB` | **USDC** | 1. Fim de semana bancário / canal fechado | 2023-03-10 21:00 | 65,0 | **0,8630** | **1.370,0** | Recuperado | Bancos dos EUA fechados de sex 16h a seg 9h30 (NY); US$ 3,3 bi retidos no SVB; mínimo intra-hora US$ 0,805 (Bitstamp); garantia sistêmica dom 22h15 UTC (`D-13`); US$ 0,989 às 23h. |
| `P1-07-USDPUSDT-02` | **USDP** | 1. Fim de semana bancário / canal fechado | 2023-03-11 14:00 | 51,0 | **0,9739** | **261,1** | Recuperado | Contágio do fim de semana bancário (`DP-01`, Decrypt 13/mar/2023): Paxos divulgou US$ 250 mi no Signature Bank com Fedwire fechado; coberto pela garantia (`D-13`). |
| `P1-07-USTUSDT-01` | **UST** | 2. Fricção temporária de liquidez | 2022-01-28 10:00 | 21,0 | **0,9899** | **101,0** | Recuperado | Crise *Frog Nation* / Abracadabra (`DP-02`, Decrypt 04/fev/2022): liquidações em MIM/UST após exposição de 0xSifu; absorvido em 21h. |
| `P1-07-TUSDUSDT-11` | **TUSD** | 2. Fricção temporária de liquidez | 2024-01-12 16:00 | 1.144,0 | **0,9535** | **464,7** | Recuperado | Falhas nas atestações da The Network Firm, troca para Moore HK e vendas após exclusão do Binance Launchpool (`DP-03`, Protos 16/jan/2024). |
| `P1-07-FDUSDUSDT-04` | **FDUSD** | 2. Fricção temporária de liquidez | 2024-03-05 18:00 | 125,0 | **0,9905** | **94,8** | Recuperado | Flash crash no recorde do BTC a US$ 69k com >US$ 1 bi liquidado em 24h (`DP-04`, Livemint/Bloomberg 06/mar/2024); resgates 1:1 fecharam desconto. |
| `P1-07-TUSDUSDT-13` | **TUSD** | 2. Fricção temporária de liquidez | 2024-10-03 16:00 | 897,0 | **0,9915** | **85,0** | Recuperado | Ação da SEC contra TrueCoin/TrustToken em 24/set/2024 por 99% das reservas em fundo offshore ilíquido (`DP-05`, SEC Rel. 2024-145). |
| `P1-07-TUSDUSDT-14` | **TUSD** | 2. Fricção temporária de liquidez | 2024-11-14 04:00 | 107,0 | **0,9920** | **80,1** | Recuperado | Euforia pós-eleição nos EUA com BTC acima de US$ 93 mil (`DP-06`, Decrypt 13/nov/2024); descolamento secundário de 80 bps absorvido em 4,5 dias. |
| `P1-07-FDUSDUSDT-07` | **FDUSD** | 2. Fricção temporária de liquidez | 2025-04-02 15:00 | 492,0 | **0,9651** | **349,2** | Recuperado | Alegação pública de insolvência da First Digital Trust por Justin Sun em 02/abr/2025 negada pelo emissor (`DP-07`, Decrypt 02/abr/2025). |
| `P1-07-TUSDUSDT-16` | **TUSD** | 2. Fricção temporária de liquidez | 2025-06-11 00:00 | 2.719,0 | **0,9861** | **139,3** | Recuperado | Baixa liquidez secundária e nota mínima (5 = *weak*) da S&P Global Ratings por opacidade de reservas (`DP-08`, Nasdaq/S&P). |
| `P1-07-USTUSDT-03` | **UST** | 3. Colapso algorítmico / insolvência | 2022-05-07 21:00 | — | **0,2453** | **7.547,1** | Não recuperado | Espiral da morte algorítmica (`DP-09`, Fed Richmond EB 22-24): corrida no Curve e Anchor Protocol; hiperinflação de 80× em LUNA e deslistagem. |
| `P1-07-USDPUSDT-09` | **USDP** | 4. Deslistagem programada na Binance (`DP-10`) | 2026-09-15 16:00 | 60,0 | **0,9942** | **58,1** | Recuperado | Anúncio oficial da Binance em 10/set/2026 para remoção do par `USDP/USDT` em 24/set/2026 (`DP-10`); esvaziamento do livro de ofertas. |
| `P1-07-USDPUSDT-10` | **USDP** | 4. Deslistagem programada na Binance (`DP-10`) | 2026-09-23 17:00 | — | **0,9880** | **120,0** | Censurado | Véspera da remoção definitiva do par `USDP/USDT` na Binance em 24/set/2026 às 03:00 UTC (`DP-10`). |

**Parâmetros Estimados do Modelo Band-TAR por Regime (`results/tables/P3-07_band_tar.csv`, `F-021`):**

| Regime | Período | N (dias) | Centro $\mu$ (bps) | Banda $\tau$ (bps) | $\rho_{\text{out}}$ | Meia-Vida (dias) | Piso C-S (bps) | Razão $\tau / \text{C-S}$ |
|---|---|---:|---:|---:|---:|---:|---:|---:|
| **Regime 1** | out/2020–jul/2021 | 200 | 91,3 | 22,5 | 0,583 | 1,29 | 8,9 | 2,52× |
| **Regime 2** | jul/2021–ago/2024 | 768 | 54,5 | 6,6 | 0,683 | 1,82 | 5,0 | 1,33× |
| **Regime 3** | ago/2024–jul/2025 | 225 | 34,9 | 6,4 | 0,889 | 5,89 | 5,7 | 1,12× |
| **Regime 4 (Pré-Ofício)** | jul/2025–23/jun/2026 | 236 | **9,3** | **1,6** | **0,552** | **1,17** | 2,7 | **0,59×** |
| **Regime 5 (Pico Agudo)** | 24/jun–21/jul/2026 | 20 | **109,1** | **42,0** | **0,664** | **1,69** | 3,6 | **11,83×** |
| **Regime 6 (Pós-Pico)** | 22/jul–30/out/2026 | 71 | **26,8** | **9,4** | **0,813** | **3,34** | 2,4 | **3,94×** |

---

# Anexo C — Registro Completo de Fontes de Dados, Legislação, Tarifas, Eventos de Depeg e Literatura

Todas as fontes citadas na pesquisa foram abertas, auditadas, citadas verbatim em `docs/sources.md` e congeladas no repositório (`prompt.md` §6). Zero pendências de verificação (`[verify]`).

### C.1. Bases de Dados Quantitativos (`D-01` a `D-15`)

| ID | Nome da Fonte | Conteúdo Extraído | Período Coberto | Acesso / URL | Status |
|---|---|---|---|---|---|
| **D-01** | Binance Public Data Archive | Klines horárias (1h OHLCV): `USDTBRL`, `BTCBRL`, `BTCUSDT`, `USDCUSDT`, `BUSDUSDT`, moedas doadoras | Out/2020 a Out/2026 (72 meses) | `https://data.binance.vision/` | Auditado e Congelado |
| **D-02** | Banco Central do Brasil — API Olinda | Cotações Oficiais PTAX (`CotacaoDolarPeriodo`) e timestamps das 4 janelas | Out/2020 a 30/10/2026 (1.520 dias úteis) | `https://olinda.bcb.gov.br/olinda/servico/PTAX/versao/v1/odata/` | Auditado e Congelado |
| **D-04** | Foxbit & Mercado Bitcoin APIs | Klines horárias dos livros de ordens domésticos `USDT-BRL` | Abr/2021 a Out/2026 (Foxbit); Mar/2023 a Out/2026 (MB) | `api.foxbit.com.br` / `api.mercadobitcoin.net` | Auditado e Congelado |
| **D-05** | Bancos Centrais Internacionais (Doadores) | Taxas oficiais: BCE (EUR, TRY, ZAR, MXN, IDR), BanRep TRM (COP), NBU (UAH), BCRA (ARS) | Jan/2020 a 30/10/2026 | BCE SDMX, `datos.gov.co`, `bank.gov.ua`, `api.bcra.gob.ar` | Auditado e Congelado |
| **D-07** | Coinbase Exchange Public API | Cotações horárias diretas de `USDT-USD` para ajuste global do dólar digital | Mai/2021 a 30/10/2026 | `https://api.exchange.coinbase.com/products/USDT-USD/candles` | Auditado e Congelado |
| **D-08** | Bitstamp Public API | Cotações horárias diretas de `USDC/USD` e `USDT/USD` (fim de semana do SVB) | Mar/2023 a Out/2026 | `https://www.bitstamp.net/api/v2/ohlc/usdcusd/` | Auditado e Congelado |
| **D-13** | Joint Statement Fed / Treasury / FDIC | Comunicado conjunto garantindo 100% dos depositantes do SVB e Signature Bank | 12/03/2023 (domingo, 18:15 EDT / 22:15 UTC) | [Federal Reserve Press Release](https://www.federalreserve.gov/newsevents/pressreleases/monetary20230312b.htm) | Aberto e Citado |
| **D-14** | DeFiLlama Yields API | Histórico diário de APY decomposto (`apyBase` vs `apyReward`) de Aave V3 e Compound V3 | Fev/2023 a Nov/2025 (1.000 dias) | `https://yields.llama.fi/chart/` | Auditado e Congelado |
| **D-15** | Federal Reserve Bank of New York | Secured Overnight Financing Rate (SOFR) diário de referência dos EUA | Fev/2023 a Nov/2025 | `https://markets.newyorkfed.org/api/rates/secured/sofr/last/1000.json` | Auditado e Congelado |

### C.2. Tarifas Bancárias, Custos Fiduciários e Normas Regulatórias (`R-01` a `R-07`, `M-05`)

| ID | Instrumento / Fonte Primária Aberta | Descrição do Objeto | Parâmetro Extraído e Citado Verbatim (`docs/sources.md`) | URL Verificada (HTTP 200) |
|---|---|---|---|---|
| **R-01** | BCB *Estudo Especial nº 48/2019* (*Spread no mercado de câmbio*) | Estudo microeconômico oficial do BCB sobre 25,1 milhões de contratos primários de câmbio | Spread corporativo ponderado pelo volume = **20,0 bps (0,20%)**; mediana do 4º quartil (>US$ 55,6k) = **15–25 bps** (limite superior conservador = 50 bps) | [BCB EE048 PDF](https://www.bcb.gov.br/conteudo/relatorioinflacao/EstudosEspeciais/EE048_Spread_no_mercado_de_cambio.pdf) |
| **R-01b** | Banco do Brasil — Tabela de Tarifas PJ | Tabela oficial de tarifas de câmbio comercial para pessoa jurídica | Contratação de câmbio online PJ: R$ 440,00; Despesas de comunicação SWIFT: **R$ 100,00** (~US$ 18,50–25,00 = **2,5 bps** em US$ 100k) | [BB Tarifas PJ PDF](https://www.bb.com.br/docs/pub/trf/tarifasPJ.pdf) |
| **R-02** | Decreto nº 6.306/2007 (RIOF) + Decretos 12.466 e 12.467/2025 | Regulamento do IOF-Câmbio vigente por finalidade e período | **0%** importação (Art. 15-B, I); **1,1%** disponibilidade até 22/mai/2025 e investimento pós-mai/2025 (Dec. 12.467); **3,5%** disponibilidade pós-23/mai/2025 (Dec. 12.466) | [Planalto RIOF](https://www.planalto.gov.br/ccivil_03/_ato2007-2010/2007/decreto/d6306.htm) |
| **R-03** | STF Medida Cautelar na ADC 96 | Decisão do Min. Alexandre de Moraes (16/07/2025) restabelecendo a eficácia do Decreto 12.466/2025 | Validade da alíquota de 3,5% de IOF-Câmbio mantida para remessas de disponibilidade | [Portal STF](https://portal.stf.jus.br/noticias/verNoticiaDetalhe.asp?idConteudo=588751&ori=1) |
| **R-04** | Binance Fee Schedule | Tabela de taxas spot Regular/VIP0 e retirada on-chain | Taxa taker Regular/VIP0: **10,0 bps (0,10%)**; retirada USDT (Tron/Ethereum): **1 USDT (~0,1 bps)** | [Binance Fee Rate](https://www.binance.com/en/fee/cryptoFee) |
| **R-05** | Foxbit — Taxas e Limites (Programa VIP) | Tabela oficial de taxas spot em reais e saques em blockchain | Taxa regular: 50 bps; **VIP 6–7 (R$ 5M–25M): 7–9 bps taker (ponto médio 8,0 bps)**; saque Pix 0%; saque USDT Tron 2 USDT (~0,2 bps) | [Foxbit Taxas e Limites](https://foxbit.com.br/taxas-e-limites/) |
| **R-06** | Mercado Bitcoin — Taxas, Contas e Limites | Tabela oficial de comissões spot e saques | **6,0 bps (0,06%) é a taxa passiva *maker* VIP (>R$ 10M)**; a taxa ativa ***taker* para R$ 500k–10M é 60,0 bps (0,60%)**; saque Pix R$ 0,00 | [MB Taxas e Limites](https://www.mercadobitcoin.com.br/taxas-contas-limites) |
| **R-07** | Resolução BCB nº 584/2026 + Carry CIP 1 Dia | Retenção cautelar de até 24h ($\ge$ US$ 10.000, vigência 01/01/2027) | Carry CIP de 1 dia $(\text{CDI } 10,75\% - \text{SOFR } 5,00\%)/252 = 2,28\text{ bps} + 0,22\text{ bps B3} = \mathbf{2,5\text{ bps}}$; risco cambial 1d s/ hedge (95% VaR) = **130 bps** | [Res. BCB 584/2026](https://www.bcb.gov.br/estabilidadefinanceira/exibenormativo?tipo=Resolu%C3%A7%C3%A3o%20BCB&numero=584) |
| **M-05** | Livecoins (18/07/2026) — Relançamento Foxbit Infra | Reestruturação da unidade B2B e mesa institucional de liquidez da Foxbit | Coincide com a multiplicação por 6× do volume da Foxbit a partir de jul/2026 via aumento de 5× no ticket médio (`F-008`, causa aberta) | [Livecoins Foxbit Infra](https://livecoins.com.br/foxbit-relanca-marca-b2b-com-foco-em-infraestrutura-cripto-para-instituicoes/) |

### C.3. Fontes Primárias Abertas dos Episódios de Depeg em Dólar (`DP-01` a `DP-10`)

| ID | Episódio / Moeda | Fonte Aberta e Verificada (HTTP 200) | Síntese da Citação Verbatim (`docs/sources.md`) |
|---|---|---|---|
| **DP-01** | `P1-07-USDPUSDT-02` (USDP, mar/2023) | [Decrypt (13/03/2023)](https://decrypt.co/123215/paxos-held-250m-failed-signature-bank-usdp-stablecoin-recovering-depeg) | Paxos divulgou US$ 250 mi no Signature Bank e seguro privado acima do teto do FDIC; paridade recuperada após garantia conjunta. |
| **DP-02** | `P1-07-USTUSDT-01` (UST, jan/2022) | [Decrypt (04/02/2022)](https://decrypt.co/91990/ust-stablecoin-adoption-is-outpacing-terra-governance-why-that-matters) | Crise *Frog Nation* / Abracadabra (MIM) após revelação de que 0xSifu era Michael Patryn (QuadrigaCX), gerando vendas em cascata de UST. |
| **DP-03** | `P1-07-TUSDUSDT-11` (TUSD, jan–fev/2024) | [Protos (16/01/2024)](https://protos.com/trueusd-hires-firm-caught-up-in-400m-fraud-as-depeg-intensifies/) | Falhas no sistema de atestação da The Network Firm, troca para Moore HK e vendas líquidas de centenas de milhões de TUSD na Binance. |
| **DP-04** | `P1-07-FDUSDUSDT-04` (FDUSD, mar/2024) | [Livemint / Bloomberg (06/03/2024)](https://www.livemint.com/market/cryptocurrency/bitcoin-pulls-back-after-touching-record-high-above-69000-11709686173930.html) | Queda abrupta do Bitcoin logo após superar o recorde histórico de US$ 69.000 em 05/03/2024, com mais de US$ 1 bilhão em liquidações em 24h. |
| **DP-05** | `P1-07-TUSDUSDT-13` (TUSD, out–nov/2024) | [U.S. SEC Press Release 2024-145 (24/09/2024)](https://www.sec.gov/newsroom/press-releases/2024-145) | Acusação formal da SEC contra TrueCoin e TrustToken por investir 99% das reservas de TUSD em fundo offshore especulativo e ilíquido. |
| **DP-06** | `P1-07-TUSDUSDT-14` (TUSD, nov/2024) | [Decrypt (13/11/2024)](https://decrypt.co/291562/bitcoin-hits-93k-as-post-election-crypto-surge-continues) | Rally pós-eleição nos EUA levando o Bitcoin acima de US$ 93.000 e gerando rotação temporária de stablecoins secundárias para ativos de risco. |
| **DP-07** | `P1-07-FDUSDUSDT-07` (FDUSD, abr/2025) | [Decrypt (02/04/2025)](https://decrypt.co/312979/first-digital-denies-justin-sun-insolvency-claims-after-fdusd-stablecoin-dips) | Alegação pública de insolvência da First Digital Trust por Justin Sun em 02/04/2025, negada pela emissora com comprovação de T-bills. |
| **DP-08** | `P1-07-TUSDUSDT-16` (TUSD, jun–out/2025) | [Nasdaq / S&P Global Ratings](https://www.nasdaq.com/articles/sp-initiates-stablecoin-stability-assessments-8-popular-tokens) | Nota mínima de estabilidade (5 = *weak*) atribuída pela S&P Global Ratings ao TUSD por falta de informações sobre reservas e instituições custodiantes. |
| **DP-09** | `P1-07-USTUSDT-03` (UST, mai/2022) | [Federal Reserve Bank of Richmond *Economic Brief* EB 22-24](https://www.richmondfed.org/publications/research/economic_brief/2022/eb_22-24) | Retiradas maciças no Curve Pool e corrida ao Anchor Protocol em 07/05/2022, seguidas de expansão da oferta de LUNA de 0,4 bi para 32 bi em 4 dias. |
| **DP-10** | `P1-07-USDPUSDT-09` e `10` (USDP, set/2026) | [Binance Official Announcement (10/09/2026)](https://www.binance.com/en/support/announcement/detail/f356a6c0f73147f9a3ebcb66f73e1d67) | Anúncio oficial da Binance em 10/09/2026 determinando a remoção e encerramento das negociações do par spot `USDP/USDT` em 24/09/2026 às 03:00 UTC. |

### C.4. Literatura Acadêmica de Fundamentação (`L-01` a `L-08`)

| ID | Referência Bibliográfica Completa | Aplicação na Pesquisa | Status |
|---|---|---|---|
| **L-01** | Corwin, S. A. & Schultz, P. (2012). A simple way to estimate bid-ask spreads from daily high and low prices. *Journal of Finance*, 67(2), 719–760. | Estimador do piso de ruído de bid-ask (`P2-01`, `F-007`). | Auditado e Verificado |
| **L-02** | Abdi, F. & Ranaldo, A. (2017). A simple estimation of bid-ask spreads from daily close, high, and low prices. *Review of Financial Studies*, 30(12), 4437–4480. | Segundo estimador de spread efetivo confirmando piso de 2–3 bps em 2026 (`P2-01`). | Auditado e Verificado |
| **L-03** | Bai, J. (1997). Estimation of a change point in multiple regression models. *Review of Economics and Statistics*, 79(4), 551–563. | Intervalos de confiança homocedásticos (Teorema 1) e heterocedásticos por regime (Teorema 2) (`P2-02`, `P4-01`). | Auditado e Verificado |
| **L-04** | Bai, J. & Perron, P. (2003). Computation and analysis of multiple structural change models. *Journal of Applied Econometrics*, 18(1), 1–22. | Programação dinâmica para seleção cega de quebras estruturais via critério LWZ (`P2-02`, `F-011`). | Auditado e Verificado |
| **L-05** | Shleifer, A. & Vishny, R. W. (1997). The limits of arbitrage. *Journal of Finance*, 52(1), 35–55. | Fundamentação teórica dos limites à arbitragem e restrições institucionais. | Auditado e Verificado |
| **L-06** | Makarov, I. & Schoar, A. (2020). Trading and arbitrage in cryptocurrency markets. *Journal of Financial Economics*, 135(2), 289–319. | Evidência de prêmios cripto entre jurisdições soberanas sob controles de capital (`P1-05`, `F-010`). | Auditado e Verificado |
| **L-07** | Obstfeld, M. & Taylor, A. M. (1997). Nonlinear aspects of goods-market arbitrage and adjustment: Heckscher's commodity points revisited. *JJIE*, 11(4), 441–479. | Modelagem Band-TAR da banda de não-arbitragem e velocidade de reversão (`P3-07`, `F-021`). | Auditado e Verificado |
| **L-08** | Abadie, A., Diamond, A. & Hainmueller, J. (2010). Synthetic control methods for comparative case studies. *JASA*, 105(490), 493–505. | Controle sintético convexo restrito ao simplex e inferência por placebos espaciais (`P2-04`, `F-017`). | Auditado e Verificado |

---

# Anexo D — Mapa de Reprodutibilidade e Matriz de Rastreabilidade Ponta a Ponta

Todos os códigos foram desenvolvidos em Python 3 linear e estruturados para exportação em arquivos de texto plano `.txt`, atendendo estritamente ao Art. 7º do Regulamento Oficial do Datathon.

### D.1. Mapa de Scripts e Reprodutibilidade de Execução

| Arquivo `.py` | Arquivo `.txt` Submetido | Entrada de Dados | Saída Gerada (Tabelas e Figuras) |
|---|---|---|---|
| `scripts/p1_02_premium.py` | `scripts/p1_02_premium.py.txt` | `data/raw/binance/`, `data/raw/bcb/`, `data/raw/coinbase/` | `P1-02_premium_daily.csv`, `P1-02_premium_daily.png` |
| `scripts/p2_01_noise.py` | `scripts/p2_01_noise.py.txt` | `data/processed/P1-02_premium_daily.csv` | `P2-01_noise_floor_daily.csv`, `P2-01_premium_noise_band.png` |
| `scripts/p2_02_breaks.py` | `scripts/p2_02_breaks.py.txt` | `P1-02_premium_daily.csv`, `P1-04_events_brazil.csv` | `P2-02_breaks.csv`, `P2-02_premium_breaks.png` |
| `scripts/p2_03_events.py` | `scripts/p2_03_events.py.txt` | `P1-04_events_brazil.csv`, `P1-02_premium_daily.csv` | `P2-03_event_table.csv`, `P2-03_placebo_dist.png` |
| `scripts/p2_04_synth.py` | `scripts/p2_04_synth.py.txt` | `data/processed/P1-05_donor_premiums_daily.csv` | `P2-04_synth_results.csv`, `P2-04_synthetic_control.png` |
| `scripts/p2_05_checks.py` | `scripts/p2_05_checks.py.txt` | `data/raw/foxbit/`, `data/raw/mercadobitcoin/` | `P2-05_venues_daily.csv`, `P2-05_hourly_22_26_jun.png` |
| `scripts/p3_01_costs.py` | `scripts/p3_01_costs.py.txt` | `P2-02_breaks.csv`, parâmetros `R-01` a `R-07` | `P3-01_route_costs.csv`, `P3-01_route_costs.png` |
| `scripts/p3_02_btc.py` | `scripts/p3_02_btc.py.txt` | `BTCBRL`, `BTCUSDT`, `PTAX` | `P3-02_btc_events.csv`, `P3-02_btc_vs_usdt_premium.png` |
| `scripts/p3_03_monitor.py` | `scripts/p3_03_monitor.py.txt` | `P1-02_premium_daily.csv`, `P2-01_noise_floor_daily.csv` | `P3-03_backtest.csv`, `P3-03_monitor.png` |
| `scripts/p3_04_depeg_chapter.py` | `scripts/p3_04_depeg_chapter.py.txt` | `data/raw/bitstamp/`, `P1-07_depeg_events_v2.csv`, `DP-01`..`DP-10` | `P3-04_depeg_case_table.csv`, `P3-04_category_summary.csv`, `P3-04_svb_weekend.png` |
| `scripts/p3_07_tar.py` | `scripts/p3_07_tar.py.txt` | `P1-02_premium_daily.csv`, `P2-02_breaks.csv` | `P3-07_band_tar.csv`, `P3-07_band_tar.png` |
| `scripts/p3_08_subsidy.py` | `scripts/p3_08_subsidy.py.txt` | `data/raw/defillama/`, `data/raw/defillama/sofr.json` | `P3-08_subsidy_2025.csv`, `P3-08_subsidy_share_2025.png` |
| `scripts/p4_01_robustness.py` | `scripts/p4_01_robustness.py.txt` | Todas as tabelas de `P1`, `P2` e `P3` | `P4-01_robustness.csv`, `P4-01_specification_curve.png` |

### D.2. Matriz de Rastreabilidade Ponta a Ponta: Slide (`deck_v1_ptbr.md`) $\leftrightarrow$ Seção (`p5_07_story.ipynb`) $\leftrightarrow$ Achado $\leftrightarrow$ Saída

| Slide (`deck_v1_ptbr.md`) | Seção (`notebooks/p5_07_story.ipynb`) | Conceito / Métrica Principal | Finding ID | Código Gerador | Tabela / Figura Primária |
|---|---|---|---|---|---|
| **Slide 1 (Capa & Pergunta)** | **Seção 1:** *Quanto custa fechar a porta?* | Tese, prêmio USDT/PTAX e escopo | `F-001`, `F-002` | `scripts/p1_02_premium.py` | `P1-02_premium_daily.csv` |
| **Slide 2 (Quatro Hipóteses)** | **Seção 2:** *Quatro hipóteses testáveis* | Desenho pré-especificado $H_0$ a $H_3$ | `F-007`, `F-016`, `F-017` | `docs/02-dolar-cripto.md` §5 | Diagrama das Três Portas |
| **Slide 3 (Dados e Piso de Ruído)** | **Seção 3:** *Os dados e o piso de ruído* | Pareamento PTAX 13:00–13:10 BRT e spread C-S | `F-004`, `F-006`, `F-007` | `scripts/p2_01_noise.py` | `P2-01_noise_floor_daily.csv`, `P2-01_premium_noise_band.png` |
| **Slide 4 (Seis Anos e 5 Quebras)** | **Seção 4:** *Seis anos de prêmio — e cinco quebras cegas* | Bai-Perron cego (+100 bps em 24/jun; fade não explicado em 22/jul) | `F-011`, `F-021` | `scripts/p2_02_breaks.py`, `p3_07_tar.py` | `P2-02_breaks.csv`, `P2-02_premium_breaks.png` |
| **Slide 5 (Salto em 3 Corretoras)** | **Seção 5:** *O salto de 24 de junho aparece em três corretoras* | Replicação em Binance (+93,9), Foxbit (+93,3) e MB (+94,9 bps) e BTC (+93,8 bps) | `F-008`, `F-009`, `F-018` | `scripts/p2_05_checks.py`, `p3_02_btc.py` | `P2-05_hourly_22_26_jun.png`, `P3-02_btc_vs_usdt_premium.png` |
| **Slide 6 (O Ofício de 23/jun)** | **Seção 6:** *O que aconteceu em 23 de junho de 2026* | Ofício confidencial do BCB contra importação via fundos (3 fontes independentes) | `F-016` (`E-05`) | `data/processed/P1-04_events_brazil.csv` | `docs/sources.md` (`E-05`) |
| **Slide 7 (13 Eventos vs Placebos)** | **Seção 7:** *Treze eventos brasileiros contra 1.073 datas comuns* | Apenas 23/jun supera as 1.073 datas limpas ($p_{\text{placebo}} \approx 0,001$) | `F-016` | `scripts/p2_03_events.py` | `P2-03_event_table.csv`, `P2-03_placebo_dist.png` |
| **Slide 8 (Controle Sintético)** | **Seção 8:** *Controle sintético e comparação entre países* | Gap agudo de +109,3 bps (Rank 1/6, razão RMSPE 9,31) e comparação com controles de capital (ARS/UAH 4–7%) | `F-010`, `F-017` | `scripts/p2_04_synth.py` | `P2-04_synth_results.csv`, `P2-04_synthetic_control.png` |
| **Slide 9 (Pico Agudo vs Pós-Pico)** | **Seção 9:** *Um pico de um mês, não um novo nível permanente* | Curva de 51 especificações: pico robusto (+74 a +128 bps); pós-pico não significativo ($p_{\text{placebo}} = 0,24$) | `F-022` | `scripts/p4_01_robustness.py` | `P4-01_robustness.csv`, `P4-01_specification_curve.png` |
| **Slide 10 (Custo em R$ por US$ 100k)** | **Seção 11:** *Em reais: R$ 5.052 por US$ 100 mil durante o pico* | Custo do ofício (+R$ 5.052/US$ 100k no pico) + Opções C e A abertas para a equipe | `F-015` | `scripts/p3_01_costs.py` | `P3-01_route_costs.csv`, `P3-01_route_costs.png` |
| **Slide 11 (Mesmo Mecanismo em USD)** | **Seção 12:** *O mesmo mecanismo em dólares: o fim de semana do SVB* | USDC a US$ 0,863 c/ bancos fechados; US$ 0,989 1h após garantia + 11 quedas abaixo de US$ 1 | `F-013`, `F-019` | `scripts/p3_04_depeg_chapter.py` | `P3-04_svb_weekend.png`, `P3-04_depeg_case_table.csv` |
| **Slide 12 (Monitor do Dólar Digital)** | **Seção 13:** *Um produto prático: o Monitor do Dólar Digital* | Alarme CUSUM sem look-ahead (detecta 24/jun no dia 0; 2 vs 4 falsos alarmes) | `F-014` | `scripts/p3_03_monitor.py` | `P3-03_backtest.csv`, `P3-03_monitor.png` |
| **Slide 13 (Lições de 2025)** | **Seção 14:** *Lições de 2025 — o que mudamos neste ano* | Modelo 2025 perdeu para Naive (15 vs 13 bps) e 53,6% do spread Compound V3 era subsídio COMP | `F-005`, `F-020` | `scripts/p3_08_subsidy.py` | `P3-08_subsidy_2025.csv`, `P3-08_subsidy_share_2025.png` |
| **Slide 14 (Placar e Limites)** | **Seção 15:** *Placar das hipóteses e limites* | Scorecard $H_0$–$H_3$ e 5 limites explícitos do estudo | `F-015`..`F-022` | `notebooks/p5_07_story.ipynb` | Síntese e Limitações |

*(Nota: A Seção 10 de `notebooks/p5_07_story.ipynb` — "Onde residentes não podem comprar dólares livremente, o USDT custa 4–7% a mais" — foi integrada ao Slide 8 junto ao controle sintético internacional para manter a apresentação principal enxuta em 14 slides.)*

---

# Anexo E — Declaração Transparente de Uso de Ferramentas e Agentes de IA

Em cumprimento aos mais elevados padrões éticos e à transparência metodológica exigida pelo 7º Datathon FGV EESP e pela boa prática científica, a equipe *Out of Sample* declara detalhadamente como ferramentas de Inteligência Artificial Generativa e sistemas agênticos foram empregados no desenvolvimento desta pesquisa.

### E.1. Governança e Divisão de Responsabilidade Humana vs Algorítmica
- **Responsabilidade Científica Integral:** Todos os conceitos econômicos, formulações de hipóteses, seleção de bases de dados, escolha dos métodos de identificação causal, decisões de recorte (como reportar o pico de 1 mês como único efeito estatisticamente distinguível de ruído e tratar o arrefecimento de 22 de julho como não explicado) e interpretações regulatórias foram concebidos, revisados e validados pelos quatro membros da equipe (CS 1 Renzo, CS 2 Nattan, CS 3 Jonathan e Economista Felipe).
- **IA como Ferramenta de Suporte Computacional e Red-Teaming:** Agentes de IA foram utilizados sob supervisão humana estrita para programação em Python, geração de gráficos, revisão cruzada de código e verificação sistemática de links e citações primárias (`prompt.md` §6: *"Sources are opened, not remembered"*).

### E.2. Modelos e Ferramentas Empregados
- **Modelos de Linguagem e Raciocínio:**
  - *Google Gemini (Pro e Flash):* Empregados na estruturação de scripts de análise, verificação de URLs e extração de citações verbatim de fontes primárias (`docs/sources.md`) e consolidação de tabelas.
  - *Anthropic Claude (Opus e Sonnet):* Empregados em revisões metodológicas independentes (auditoria de inferência placebo vs paramétrica, verificação de datas de eventos, prototipagem do notebook `notebooks/p5_07_story.ipynb` e revisão crítica de afirmações causais).
  - *OpenAI Codex / GPT:* Incluído no desenho do protocolo de análise cega multi-agente (`P3-05`).

### E.3. Aplicações Específicas do Framework Agêntico
1. **Triagem de Eventos Cambiais dos Doadores Internacionais (Tarefa `P1-06` — Extensão B):**
   - Um agente realizou varredura preliminar em comunicados e portais de bancos centrais dos países candidatos ao pool doador para identificar reformas cambiais ou controles de capitais concorrentes entre 2020 e 2026.
   - *Protocolo de Verificação Humana:* Toda sinalização foi verificada manualmente em fonte primária pela equipe (`Jonathan`, S6), confirmando a exclusão da Argentina (bandas e controles cambiais da BCRA) e da Ucrânia (lei marcial, Resolução nº 18 do NBU) e validando o pool limpo de 5 moedas conversíveis (`EUR`, `TRY`, `ZAR`, `MXN`, `COP`).
2. **Protocolo de Análise Cega Independente (Tarefas `P1-08`, `P2-06`, `P3-05` — Extensão A):**
   - Antes de qualquer execução de agentes analistas independentes, a estimativa oficial da equipe (+93,91 bps no estudo de eventos e +109,31 bps no controle sintético) foi congelada em `results/agentic/team_estimate.json` (commit `80fc866`), e o pacote de dados anônimos (`results/agentic/bundle_SHA256SUMS.txt`) e o protocolo (`results/agentic/protocol.md`) foram fixados em git.
3. **Auditoria Cruzada e Revisão de Citações e Inferência:**
   - Revisões cruzadas entre membros da equipe e agentes identificaram e corrigiram pontos críticos antes da submissão: substituição de $p$-valores paramétricos inflacionados por $p$-valores de placebos empíricos (`F-016`, `F-022`), reconhecimento explícito de que o patamar pós-22 de julho (+11,5 a +19,3 bps) tem $p_{\text{placebo}} = 0,24$ (não significativo), remoção de atribuições causais não provadas para o arrefecimento de julho e para eventos de microestrutura (`M-01` a `M-04`), e abertura com citação textual de todas as fontes de legislação, tarifas (`R-01` a `R-07`) e casos de depeg (`DP-01` a `DP-10`).

### E.4. Compromisso de Integridade dos Dados
Declaramos expressamente que **nenhum dado numérico, data histórica, cotação cambial, dispositivo de lei ou resultado estatístico foi sintetizado artificialmente**. Toda a base empírica foi descarregada de repositórios públicos oficiais (Binance Vision, BCB Olinda, Coinbase, Bitstamp, BCE, BanRep, Planalto, STF, SEC, Federal Reserve e DeFiLlama), com checksums SHA-256 e scripts disponíveis para replicação integral pela banca examinadora.

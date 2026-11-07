# Anexos Metodológicos e Registro de Evidências

## Quanto Custa Fechar a Porta? O Prêmio do Dólar Digital no Brasil e os Limites à Arbitragem



**Documento Suplementar Oficial — 7º Datathon de Moedas Digitais FGV EESP (Novembro de 2026)**  

**Equipe Out of Sample:** CS 1 (Renzo), CS 2 (Nattan), CS 3 (Jonathan), Economista (Felipe)  



---



### Estrutura dos Anexos

- **Anexo A:** Tabela Completa de Eventos Regulatórios e Microestruturais Brasileiros (`P2-03`, `P3-12`, Placebo $p$-valores)

- **Anexo B:** Bateria Completa de Robustez, Custos por Rota e Transferência Agregada (`P3-01`, `P3-11`), Depegs (`P3-04`, `P3-09`), Importações BCB (`P3-10`), Previsão Datada (`P3-13`), Piloto de Condições de Acesso (`P3-28`, `F-043`) e Reconciliação On-Chain (`P3-29`, `F-041`, `F-042`)

- **Anexo C:** Registro Completo de Fontes de Dados, Legislação, 10 Fontes de `E-05` (`P3-14`), Tarifas, Depegs e Literatura

- **Anexo D:** Mapa de Reprodutibilidade de Scripts e Matriz de Rastreabilidade Ponta a Ponta (deck de 10 slides)

- **Anexo E:** Declaração Transparente de Uso de Ferramentas e Agentes de Inteligência Artificial

- **Anexo F:** Material movido do deck de 14 slides (2/nov/2026): inferência do número principal e conteúdo da janela (`F-029`), Res. BCB 574, comparação internacional, SVB, monitor, Lições de 2025, placar das hipóteses



---



# Anexo A — Tabela Completa de Eventos Regulatórios e de Mercado no Brasil



Este anexo consolida todos os 13 eventos regulatórios, tributários e de microestrutura coletados pela equipe (`P1-04`, `data/processed/P1-04_events_brazil.csv`), avaliados por meio de estudo de eventos em janelas de $\pm 20$ dias úteis PTAX em torno de $t_0$ (`P2-03`, `results/tables/P2-03_event_table.csv`, `F-016`) e classificados por forma de emissão e aviso prévio (`P3-12`, `results/tables/P3-12_rules.csv`, `F-026`).



**Regra de Inferência (`prompt.md` §5):** Como o prêmio é persistente em níveis dentro de janelas de 40 dias úteis, testes $t$ paramétricos (mesmo com correção HAC Newey-West de 5 defasagens) rejeitam com frequência excessiva em datas comuns. Por essa razão, **reportamos exclusivamente os $p$-valores empíricos contra datas placebo** — tanto sobre todas as **1.073 datas limpas** fora de janelas de eventos (`p_placebo_all_clean_2s`) quanto sobre o sorteio aleatório pré-especificado de **200 datas limpas** (`p_placebo_2s`, `seed = 20261102`, cuja faixa de 2,5% a 97,5% é **$-35,0\text{ a }+37,6\text{ bps}$**). Eventos de microestrutura (`M-01` a `M-04`) **coincidem no tempo** com mudanças na série, mas não provam causalidade.



| ID | Tipo / Forma de Emissão (`P3-12`) | Aviso Prévio | Data Avaliada ($t_0$ PTAX) | Média Pré (bps) | Média Pós (bps) | Variação (bps) | Erro HAC (bps) | $p$ Placebo (1.073 Limpas) | $p$ Placebo (200 Sorteios) | Percentil Placebo | Fonte Primária / Verificação Aberta (`docs/sources.md`) |

|---|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---|

| **E-01** | Decreto presidencial (Anúncio) | 1d | 2025-05-22 | 26,91 | 40,09 | +13,18 | 1,95 | 0,3845 | 0,4030 | 79,0% | [Decreto nº 12.466/2025](https://www.planalto.gov.br/ccivil_03/_ato2023-2026/2025/decreto/d12466.htm) |

| **E-01** | Decreto presidencial (Vigência) | 1d | 2025-05-23 | 26,21 | 41,65 | +15,44 | 2,18 | 0,3147 | 0,3383 | 81,5% | [Decreto nº 12.467/2025](https://www.planalto.gov.br/ccivil_03/_ato2023-2026/2025/decreto/d12467.htm) |

| **E-01b** | Decreto legislativo / STF (Anúncio) | 7d | 2025-06-27 | 39,92 | 16,00 | -23,92 | 5,55 | 0,1648 | 0,1940 | 8,5% | [Decreto Legislativo nº 176/2025](https://legis.senado.leg.br/norma/41240559/publicacao/41241630) |

| **E-01b** | Decreto legislativo / STF (Vigência) | 7d | 2025-07-04 | 37,57 | 12,69 | -24,88 | 4,89 | 0,1527 | 0,1841 | 8,0% | [STF MC na ADC 96](https://portal.stf.jus.br/noticias/verNoticiaDetalhe.asp?idConteudo=588751&ori=1) |

| **E-02** | Resolução BCB pública (Anúncio) | 84d | 2025-11-10 | 13,25 | 9,46 | -3,79 | 3,88 | 0,7477 | 0,7214 | 39,5% | [Resoluções BCB nº 519–521/2025](https://www.bcb.gov.br/estabilidadefinanceira/exibenormativo?tipo=Resolu%C3%A7%C3%A3o%20BCB&numero=521) |

| **E-02** | Resolução BCB pública (Vigência) | 84d | 2026-02-02 | 8,43 | 4,12 | -4,31 | 1,68 | 0,7225 | 0,6965 | 38,0% | [Resolução BCB nº 521/2025](https://www.bcb.gov.br/estabilidadefinanceira/exibenormativo?tipo=Resolu%C3%A7%C3%A3o%20BCB&numero=521) |

| **E-03** | Proposta da Fazenda (Anúncio) | — | 2026-02-05 | 7,63 | 5,51 | -2,11 | 1,92 | 0,8408 | 0,8458 | 46,5% | [Minuta Fazenda / Receita (Forbes/Valor)](https://forbes.com.br/coluna/2026/02/governo-quer-taxar-criptomoedas-com-iof-o-que-isso-muda-para-o-investidor/) |

| **E-03** | Proposta da Fazenda (Vigência) | — | N/A | — | — | — | — | — | — | — | Minuta não promulgada (`unenacted_draft`) |

| **E-04** | Resolução BCB pública (Anúncio) | 175d | 2025-11-10 | 13,25 | 9,46 | -3,79 | 3,88 | 0,7477 | 0,7214 | 39,5% | [Art. 4º Res. BCB nº 521/2025](https://www.bcb.gov.br/estabilidadefinanceira/exibenormativo?tipo=Resolu%C3%A7%C3%A3o%20BCB&numero=521) |

| **E-04** | Resolução BCB pública (Vigência) | 175d | 2026-05-04 | 4,65 | 11,89 | +7,24 | 2,92 | 0,6145 | 0,6119 | 72,0% | [Art. 4º Res. BCB nº 521/2025](https://www.bcb.gov.br/estabilidadefinanceira/exibenormativo?tipo=Resolu%C3%A7%C3%A3o%20BCB&numero=521) |

| **E-05** | **Ofício BCB de circulação restrita (Vigência)** | **0d** | **2026-06-23** | **15,24** | **109,14** | **+93,91** | **16,18** | **0,0009** | **0,0050** | **100,0%** | [Cointelegraph 24/jun](https://cointelegraph.com.br/news/central-bank-notifies-cryptocurrency-companies) · [Exame 25/jun](https://exame.com/future-of-money/notificacao-do-bc-a-bancos-deixa-criptomoedas-2-mais-caras-no-brasil-entenda/) · [LAI BCB 29/jul](https://cointelegraph.com.br/news/exclusive-central-bank-confirms-it-is-considering-a-24-hour-hold-on-stablecoins) (`E-05.1`–`E-05.10`) |

| **E-06a** | Resolução BCB pública (Anúncio) | 154d | 2026-04-30 | 4,87 | 10,91 | +6,04 | 3,16 | 0,6471 | 0,6219 | 71,5% | [Resolução BCB nº 561/2026](https://www.bcb.gov.br/estabilidadefinanceira/exibenormativo?tipo=Resolu%C3%A7%C3%A3o%20BCB&numero=561) |

| **E-06a** | Resolução BCB pública (Vigência) | 154d | 2026-10-01 | 22,79 | 17,48 | -5,31 | 7,18 | 0,6778 | 0,6617 | 35,5% | [Art. 50 Res. BCB nº 277](https://www.bcb.gov.br/estabilidadefinanceira/exibenormativo?tipo=Resolu%C3%A7%C3%A3o%20BCB&numero=561) |

| **E-06b** | Resolução BCB pública (Anúncio) | 147d | 2026-08-07 | 53,33 | 31,34 | -21,99 | 8,03 | 0,1872 | 0,2189 | 9,0% | [Resolução BCB nº 584/2026](https://www.bcb.gov.br/estabilidadefinanceira/exibenormativo?tipo=Resolu%C3%A7%C3%A3o%20BCB&numero=584) |

| **E-06b** | Resolução BCB pública (Vigência) | 147d | 2027-01-01 | — | — | — | — | — | — | — | Fora da amostra (`outside_sample_future`; previsão datada em `P3-13` / `F-027`) |

| **E-07** | Interrupção Pix (Vigência) | — | 2022-06-17 | 53,23 | 48,53 | -4,70 | 7,69 | 0,7039 | 0,6866 | 37,0% | [Suspensão Pix Capitual (The Block)](https://www.theblock.co/post/156492/binance-resumes-withdrawals-and-deposits-in-brazilian-reais) |

| **M-01** | Coincide com corte de alavancagem | — | 2021-07-26 | 77,88 | 61,02 | -16,86 | 11,08 | 0,2700 | 0,2985 | 13,0% | [Corte Alavancagem 20x Binance (The Block)](https://www.theblock.co/post/112435/binance-lower-leverage-20-times-existing-users) |

| **M-02** | Coincide com Termo CVM | — | 2024-08-13 | 55,40 | 42,31 | -13,10 | 18,89 | 0,3855 | 0,4030 | 19,0% | [Termo de Compromisso CVM R$ 9,6 mi (InfoMoney)](https://www.infomoney.com.br/onde-investir/cvm-encerra-processo-contra-binance-apos-acordo-de-r-96-milhoes/) |

| **M-03** | Coincide com corte de tick size | — | 2025-06-27 | 39,92 | 16,00 | -23,92 | 5,55 | 0,1648 | 0,1940 | 8,5% | [Tick Size 0,0001 BRL Binance (`exchangeInfo`)](https://data-api.binance.vision/api/v3/exchangeInfo?symbol=USDTBRL) |

| **M-04** | Coincide com parceria NovaDAX | — | 2026-07-07 | 70,95 | 60,44 | -10,51 | 28,55 | 0,4888 | 0,4876 | 24,0% | [Parceria Foxbit–NovaDAX (Cointelegraph)](https://cointelegraph.com.br/news/novadax-strikes-partnership-to-migrate-clients-to-foxbit) |



---



# Anexo B — Bateria Completa de Robustez, Custos por Rota, Transferência Agregada, Depegs e Mecanismo



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

| **Binance (Líder Global/Local)** | 15,24 | 109,14 | **+93,91** | 12,96 | **+96,18** | 155,4 | 184,3 |

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



### B.5. Transferência Agregada no Pico (`P3-11`, `F-025`) e Custos por Rota para US$ 100.000 (`P3-01`, `F-015` — Opção A)



**1. Transferência Agregada de Compradores para Vendedores durante o Pico (24/jun a 21/jul/2026, `results/tables/P3-11_transfer.csv`, `F-025`):**



| Variante (`P3-11_transfer.csv`) | Volume Binance (R$ bi) | Transferência Binance (R$ mi) | Equivalente Tarifário Binance (bps) | Volume 3 Corretoras (R$ bi) | Transferência 3 Corretoras (R$ mi) | Equivalente Tarifário 3 Corretoras (bps) | Inferência Placebo (194 Janelas) |

|---|---:|---:|---:|---:|---:|---:|---|

| **Headline: excesso sobre média pré de 20d** | **11,180** | **106,09** | **94,89** | **15,762** | **145,27** | **92,16** | **$k = 0 / 194$, $p = 0,0051$ (máx. placebo = R$ 35,5 mi)** |

| Janela pré de 10 dias PTAX | 11,180 | 109,15 | 97,63 | 15,762 | 149,58 | 94,90 | Acima de 100% dos placebos |

| Janela pré de 40 dias PTAX | 11,180 | 110,71 | 99,02 | 15,762 | 151,77 | 96,29 | Acima de 100% dos placebos |

| Gap do Controle Sintético (+109,31 bps, `F-017`) | 11,180 | 122,21 | 109,31 | 15,762 | 172,30 | 109,31 | Acima de 100% dos placebos |

| Janela pós-pico $[+21, +60]$ (descritivo) | 16,151 | 30,92 | 19,15 | 25,813 | 49,70 | 19,25 | Não distinguível de ruído ($p_{\text{placebo}} = 0,24$, `F-022`) |



*(Por corretora na especificação headline: Binance **R$ 106,09 mi** sobre R$ 11,18 bi; Foxbit **R$ 37,38 mi** sobre R$ 4,40 bi; Mercado Bitcoin **R$ 1,80 mi** sobre R$ 0,18 bi).*



**2. Tabela Completa de 17 Linhas de Custos por Rota para US$ 100.000 (`results/tables/P3-01_route_costs.csv`, `F-015` — Opção A para a Equipe):**



*Conversão para reais.* As duas linhas do custo do ofício usam a PTAX de cada dia (média de R$ 5,14 no pico e no pós-pico),

como `F-025` e `F-033`. As demais linhas usam uma única taxa de referência ilustrativa de R$ 5,38, a cotação de compra

USDT/BRL da Binance em 31/out/2026 (`D-10`), apenas para comparar rotas na mesma base; ela não é PTAX. Até 3/nov/2026 o

custo do ofício também era convertido a R$ 5,38 (R$ 5.052 e R$ 621); os valores em bps não mudaram.



| ID da Rota | Categoria | Regime / Cenário | Corretora / Canal | Prêmio (bps) | Spread / Taxa (bps) | SWIFT / Rede (bps) | IOF / Carry (bps) | Total (bps) | Custo Total (R$ / US$ 100k) | IOF Bancário Vigente | Notas e Fontes Primárias (`docs/sources.md`) |

|---|---|---|---|---:|---:|---:|---:|---:|---:|---:|---|

| `NOTICE_COST_SPIKE` | **Custo do Ofício** | **Pico Agudo: 24/jun–21/jul/2026** | **Binance (VIP0)** | **+93,9** | **0,0** | **0,0** | **0,0** | **93,9** | **R$ 4.842,04** | — | **Efeito medido do ofício E-05 (`F-016`, $p_{\text{placebo}} \approx 0,001$)** |

| `NOTICE_COST_AFTER` | Custo do Ofício | Pós-Pico: 22/jul–30/out/2026 | Binance (VIP0) | +11,5 | 0,0 | 0,0 | 0,0 | 11,5 | R$ 583,10 | — | Não distinguível de ruído (`F-022`, $p_{\text{placebo}} = 0,24$) |

| `BANK_IMPORT_0IOF` | Rota Bancária | Importação de Mercadorias (0% IOF) | Banco Comercial | 0,0 | 20,0 | 2,5 | 0,0 | **22,5** | **R$ 1.210,50** | 0,0% | RIOF Art. 15-B, I (`R-02`); spread PJ 20 bps (`R-01`; 52,5 bps c/ 50 bps); SWIFT US$ 25 (`R-01b`) |

| `BANK_INVEST_11IOF` | Rota Bancária | Investimento / Disp. pré-mai/2025 (1,1% IOF) | Banco Comercial | 0,0 | 20,0 | 2,5 | 110,0 | **132,5** | **R$ 7.128,50** | 1,1% | Dec. 12.467/2025 (`R-02`); spread PJ 20 bps (`R-01`; 162,5 bps c/ 50 bps) |

| `BANK_AVAIL_35IOF` | Rota Bancária | Disponibilidade pós-23/mai/2025 (3,5% IOF) | Banco Comercial | 0,0 | 20,0 | 2,5 | 350,0 | **372,5** | **R$ 20.040,50** | 3,5% | Dec. 12.466/2025 e STF ADC 96 (`R-02`, `R-03`; 402,5 bps c/ 50 bps) |

| `USDT_REGIME_1` | Rota USDT | Regime 1: out/2020–jul/2021 | Binance (VIP0) | 91,3 | 10,0 | 0,1 | 0,0 | **101,4** | **R$ 5.455,32** | 1,1% | Regime 1 (`F-011`); IOF bancário vigente à época = 1,1% (`R-02`) |

| `USDT_REGIME_2` | Rota USDT | Regime 2: jul/2021–ago/2024 | Binance (VIP0) | 54,5 | 10,0 | 0,1 | 0,0 | **64,6** | **R$ 3.475,48** | 1,1% | Regime 2 (`F-011`); IOF bancário vigente à época = 1,1% (`R-02`) |

| `USDT_REGIME_3` | Rota USDT | Regime 3: ago/2024–jul/2025 | Binance (VIP0) | 34,9 | 10,0 | 0,1 | 0,0 | **45,0** | **R$ 2.421,00** | 1,1% | Regime 3 (`F-011`); 1,1% vigente em ~9,5 dos 11 meses (`R-02`) |

| `USDT_REGIME_4` | Rota USDT | Regime 4: jul/2025–22/jun/2026 (Pré-Ofício) | Binance (VIP0) | 9,3 | 10,0 | 0,1 | 0,0 | **19,4** | **R$ 1.043,72** | 3,5% | Pós-corte de tick (`M-03`, `F-007`); menor fricção histórica |

| `USDT_REGIME_5` | Rota USDT | Regime 5: 24/jun–21/jul/2026 (Pico 20d) | Binance (VIP0) | 109,1 | 10,0 | 0,1 | 0,0 | **119,2** | **R$ 6.412,96** | 3,5% | Pós-ofício BCB (`E-05`, `F-011`) |

| `USDT_PEAK` | Rota USDT | Pico de 48h: 24–25/jun/2026 | Binance (VIP0) | 169,9 | 10,0 | 0,1 | 0,0 | **180,0** | **R$ 9.682,66** | 3,5% | Média dos picos de 24/jun (155,4 bps) e 25/jun (184,3 bps, `F-009`) |

| `USDT_REGIME_6` | Rota USDT | Regime 6: 22/jul–out/2026 (Pós-Pico) | Binance (VIP0) | 26,8 | 10,0 | 0,1 | 0,0 | **36,9** | **R$ 1.985,22** | 3,5% | Nível pós-pico (`F-011`; diferença pós-pico não significativa, `F-022`) |

| `USDT_REGIME_6_FOXBIT` | Rota USDT | Regime 6: Foxbit VIP 6–7 Taker | Foxbit | 26,8 | 8,0 | 0,2 | 0,0 | **35,0** | **R$ 1.883,00** | 3,5% | Taxa taker VIP 6–7 (R$ 5M–25M) = 7–9 bps, ponto médio 8,0 bps (`R-05`) |

| `USDT_REGIME_6_MB` | Rota USDT | Regime 6: Mercado Bitcoin VIP Maker | Mercado Bitcoin | 26,8 | 6,0 | 0,2 | 0,0 | **33,0** | **R$ 1.775,40** | 3,5% | 6,0 bps é taxa *maker* VIP (>R$ 10M); *taker* ativo (R$ 500k–10M) é **60,0 bps = 87,0 bps total** (`R-06`) |

| `SCENARIO_S1_IOF35` | Cenário | Cenário S1: IOF de 3,5% sobre Cripto | Binance (VIP0) | 26,8 | 10,0 | 0,1 | 350,0 | **386,9** | **R$ 20.815,22** | 3,5% | Minuta não promulgada (`E-03`, `R-02`) sobre base do Regime 6 |

| `SCENARIO_S2A_HOLD_HEDGED` | Cenário | Cenário S2a: Retenção 24h c/ Hedge CIP | Binance (VIP0) | 26,8 | 10,0 | 0,1 | 2,5 | **39,4** | **R$ 2.119,72** | 3,5% | Res. BCB 584/2026 (`R-07`): carry CIP 1 dia $(\text{CDI } 10,75\% - \text{SOFR } 5,00\%)/252 + \text{B3} = 2,5\text{ bps}$ |

| `SCENARIO_S2B_HOLD_UNHEDGED` | Cenário | Cenário S2b: Retenção 24h s/ Hedge | Binance (VIP0) | 26,8 | 10,0 | 0,1 | 0,0 | **36,9** | **R$ 1.985,22** | 3,5% | Para saída em USDT (`P3-13`, `F-027`), 1 dia custa **~9,1 bps** (5,5 bps Selic + 3,7 bps risco `USDT/USD`); risco PTAX 1d (130 bps) só ocorreria se retido em BRL |





**3. A Rede Não É o Custo: Decomposição do Cost-Stack e Transmissão para DeFi (`P3-34`, `F-040`):**  

A tabela `results/tables/P3-34_cost_stack.csv` e a figura `results/figures/P3-34_cost_stack.png` comparam a estrutura de custos de aquisição e transferência de US$ 100.000 em dólar digital nos regimes pré-ofício, pico agudo e pós-pico, contrapondo-os à rota descentralizada on-chain (Polygon `Pix → BRLA → USDC`):

- **Razão Choque vs. Rede:** Na rota centralizada de USDT, a taxa de transferência on-chain é de apenas 0,1 a 0,2 bps (1 a 2 USDT em US$ 100 mil, `A-02`/`R-05`), enquanto a taxa de corretagem fica em 8,0 a 10,0 bps (`R-04`/`R-05`). O salto de **+93,9 bps** no prêmio de acesso decorrente do ofício de 23/jun (R$ 4.842 por US$ 100 mil) é **~470× a 939× maior** que a taxa de saque da rede blockchain.

- **Transmissão para DeFi:** Na rota on-chain na Polygon (`F-037`), o prêmio sobre a PTAX saltou de 34,9 bps para 145,9 bps (**+111,0 bps**), superando em **22,2×** a taxa de 5,0 bps (0,05%) do pool Uniswap v3 (`0x0e77...c956`). Observamos o encarecimento também nesta rota on-chain; isso é compatível com fricções de conversão, sem identificar isoladamente sua causa.

- **Preço Normal Não É Mercado Normal:** O gráfico em três painéis alinhados (`results/figures/P3-34_price_vs_market_recovery.png`, jan–out/2026) evidencia que, embora o prêmio tenha recuado para 26,8 bps após 22/jul ($p = 0,24$), as aquisições de stablecoins no exterior registradas no BCB (`SGS 29644`) despencaram **−78% em julho** (de US$ 2,54 bi para US$ 0,57 bi) e permaneceram em um terço da média anterior (US$ 0,77 bi/mês em ago–set), enquanto a fatia de volume da Foxbit migrou estruturalmente de 6,8% para 28,0% (pico) e 34,7% (pós-pico, `F-036`), com fluxo vendedor agressivo de +361,9 mi USDT em horário bancário comercial (`F-031`).



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



| Regime | Período | N (dias) | Centro $\mu$ (bps) | Banda $c$ (bps) | $\beta_{\text{out}}$ | Meia-Vida (dias) | RMSE Band-TAR (bps) | Ganho vs Passeio Aleatório (%) | Ganho vs AR(1) Linear (%) |

|---|---|---:|---:|---:|---:|---:|---:|---:|---:|

| **Regime 1** | out/2020–jul/2021 | 196 | 91,3 | 55,0 | -0,907 | 0,29 | 15,93 | +3,4% | +0,2% |

| **Regime 2** | jul/2021–ago/2024 | 771 | 54,5 | 13,6 | -0,631 | 0,70 | 7,61 | +10,1% | +0,9% |

| **Regime 3** | ago/2024–jul/2025 | 220 | 34,9 | 4,8 | -0,720 | 0,54 | 7,03 | +7,8% | +0,1% |

| **Regime 4 (Pré-Ofício)** | jul/2025–23/jun/2026 | 242 | **9,3** | **1,6** | **-1,030** | **1,00** | **2,80** | **+2,5%** | **+0,1%** |

| **Regime 5 (Pico Agudo)** | 24/jun–21/jul/2026 | 20 | **109,1** | **42,0** | **-1,489** | **1,00** | **12,96** | **+21,3%** | **+16,4%** |

| **Regime 6 (Pós-Pico)** | 22/jul–30/out/2026 | 71 | **26,8** | **9,4** | **-0,987** | **0,16** | **5,34** | **+1,7%** | **+0,0%** |

| **Pós-Ofício Agrupado (5+6)** | 24/jun–30/out/2026 | 91 | 44,9 | 32,4 | -0,352 | 1,60 | 9,99 | +20,3% | +10,8% |



### B.7. Mecanismo nas Estatísticas do BCB (`P3-10`, `F-024`) e Fluxo nas Corretoras



**Testes Pré-Registrados sobre Compras Líquidas de Stablecoins no Exterior (`SGS 29644`, `results/tables/P3-10_imports.csv`):**



| Teste (`P3-10_imports.csv`) | Período | Valor | Variação (%) | Amostra de Comparação | $p$-valor Empírico | Veredito |

|---|---|---:|---:|---|---:|---|

| **T1: Variação logarítmica jun $\to$ jul/2026** | jul/2026 | −1,4926 | **−77,52%** | 91 variações mensais (1 tão grande: abr/2020) | **0,0217** | **Queda fora da faixa normal** |

| **T1b: Log de jul/2026 vs média jan–mai/2026** | jul/2026 | −1,4463 | **−76,46%** | 86 meses (3 tão grandes, todos < US$ 20 mi/mês) | **0,0460** | **Queda fora da faixa normal** |

| **T2: Recuo — média(ago, set) / média(jan–mai)** | ago–set/2026 | **0,3182** | −68,18% | Regra: $\ge 0,50$ recuperado; $< 0,25$ não recuperado | — | **Parcial (inconclusivo)** |

| **T3: Correlação compras vs prêmio médio mensal** | jan/2024–set/2026 | −0,6163 | — | 33 meses | — | Apenas descritivo |



**Volume e Fluxo de Ordens nas Três Corretoras (`results/tables/P3-10_order_flow.csv`):**



| Corretora | Métrica | Antes $[-20, -1]$ | Pico $[+1, +20]$ | Pós-Pico $[+21, +60]$ |

|---|---|---:|---:|---:|

| **Binance** | Volume diário (milhões de USDT/dia) | 58,4 | 77,6 (+33%, $p_{\text{placebo}} = 0,34$) | 55,2 |

| **Binance** | Fração iniciada pelo comprador (*taker buy*) | 0,52 | 0,49 | 0,51 |

| **Foxbit** | Volume diário (milhões de USDT/dia) | 4,3 | 30,7 | 31,6 |

| **Foxbit** | Tamanho médio por negócio (USDT) | 730 | 4.687 | 6.297 |

| **Mercado Bitcoin** | Volume diário (milhões de USDT/dia) | 0,95 | 1,25 | 1,38 |



### B.8. Decisão de Tesouraria Institucional e Paridade Coberta de Juros (`P3-31`, `F-039`, nível: retrospectivo e exploratório)



**Identidade de Carrego Diário Nulo por Paridade Coberta de Juros (CIP):**  

Sob a Paridade Coberta de Juros (*Covered Interest Parity* — CIP), o preço a termo $F_{t,h}$ do dólar oficial na B3 para liquidação no horizonte de $h$ dias úteis satisfaz rigorosamente $F_{t,h} = S_t \times (1 + i_{\text{BRL},h}) / (1 + i_{\text{USD},h})$, onde $S_t$ é a taxa de câmbio à vista PTAX, $i_{\text{BRL},h}$ é a taxa CDI/Selic e $i_{\text{USD},h}$ é a taxa de cupom cambial. Para uma tesouraria institucional com passivo ou necessidade de caixa em USDT no horizonte $h$, manter os reais aplicados em CDI/Selic e comprar um contrato a termo ou futuro de dólar trava o câmbio oficial com custo líquido de carrego diário estritamente nulo:

$$\text{Custo Líquido de Carrego Cambial} = S_t \times (1 + i_{\text{BRL},h}) - F_{t,h} \times (1 + i_{\text{USD},h}) = 0$$

Os juros auferidos no depósito em reais financiam com exatidão matemática os pontos a termo cambiais exigidos na B3. Consequentemente, adiar a aquisição de USDT com proteção cambial isola o risco cambial oficial ($S$) e transforma a decisão de espera em uma **aposta pura e exclusiva na dinâmica do prêmio local** do dólar digital ($\pi_t \to \pi_{t+h}$).



**Desempenho Retrospectivo do Comprador com Hedge B3 vs Sem Hedge (`results/tables/P3-31_buyer_hedged_comparison.csv`):**  

A tabela abaixo avalia uma posição compradora de 100 mil USDT iniciada em 25/jun/2026 (dia seguinte ao salto de +94 bps pós-ofício, prêmio inicial $\pi_0 = 184,35\text{ bps}$ e preço USDT/BRL de R$ 5,2785 e PTAX de R$ 5,1892):



| Prazo $h$ (dias úteis PTAX) | Data Alvo | Prêmio Inicial (bps) | Prêmio Final (bps) | Variação Prêmio (bps) | Economia Hedged (bps) | Economia Hedged (R$ / 100k USDT) | Economia Sem Hedge (R$ / 100k USDT) | Variação PTAX (%) |

|---|---|---:|---:|---:|---:|---:|---:|---:|

| **1 dia** | 26/06/2026 | 184,35 | 75,62 | +108,72 | +107,36 | R$ 5.675 | R$ 7.790 | −0,38% |

| **5 dias** | 02/07/2026 | 184,35 | 99,19 | +85,16 | **+89,66** | **R$ 4.746** | R$ 4.706 | +0,10% |

| **6 dias** | 03/07/2026 | 184,35 | 185,87 | −1,52 | **+6,33** | **R$ 335** | R$ 2.714 | −0,34% |

| **10 dias** | 09/07/2026 | 184,35 | 103,83 | +80,52 | **+92,32** | **R$ 4.896** | R$ 11.617 | −1,08% |

| **15 dias** | 16/07/2026 | 184,35 | 57,67 | +126,68 | +145,15 | R$ 7.713 | R$ 18.527 | −1,77% |

| **20 dias** | 23/07/2026 | 184,35 | 45,92 | +138,43 | **+164,04** | **R$ 8.733** | R$ 21.747 | −2,09% |



*Ressalvas metodológicas:* Taxa de emolumentos B3 considerada em 0,22 bps (R$ 11,62 por 100k USDT). Embora a espera retrospectiva com hedge tenha poupado R$ 4.746 a R$ 8.733 em 5 a 20 dias úteis, o ganho **não foi monotônico** (no 6º dia útil, em 03/jul, o repique do prêmio reduziu o ganho a apenas R$ 335) nem previsível ex-ante.



**Limiares do Vendedor Institucional e Perdas Retrospectivas (`results/tables/P3-31_thresholds.csv`, `P3-31_historical_comparison.csv`):**  

Para o vendedor institucional com passivos em reais, a espera acarreta custo de oportunidade explícito do carrego em reais (perda do CDI/Selic). Sob taxa livre de risco de 10% a.a. e corretagem de 10 bps, o vendedor exige uma apreciação do USDT de **+18,9 bps em 5 dias**, **+37,9 bps em 10 dias** e **+75,9 bps em 20 dias** apenas para atingir o ponto de equilíbrio (*break-even hurdle*). Em retrospecto após 25/jun, o vendedor que adiou a liquidação sofreu perdas substanciais de **−R$ 4.697 em 5 dias**, **−R$ 11.594 em 10 dias** e **−R$ 21.704 em 20 dias** por 100 mil USDT, impulsionadas pela compressão do prêmio somada à valorização do real.



### B.9. Censo Global de Duração em 10 Moedas e Modelo de Sobrevivência (`P3-30`, `F-038`, nível: exploratório)



**Viabilidade Amostral: Falha no Brasil e Aprovação no Pool Global de 10 Moedas (`results/tables/P3-30_feasibility.csv`):**  

A identificação estatística da duração de choques de prêmio exige amostras com número suficiente de eventos independentes e recuperações completas. Com dados exclusivos do Brasil (`BRL_only`), os critérios de viabilidade reprovam nas partições de validação e teste. A agregação em um pool global de 10 moedas conversíveis e semi-conversíveis (10.875 dias de cotação entre 2020 e 2026) viabiliza o estudo:



| Escopo Amostral | Limiar de Choque | Partição | Episódios Totais | Recuperações | Censurados | Critério Mínimo | Status do Gate |

|---|---|---|---:|---:|---:|---|---|

| **Apenas Brasil (BRL)** | $3\sigma$ | Treino (2020–2024) | 11 | 10 | 1 | $\ge 10$ ep., $\ge 5$ rec. | Aprovado |

| **Apenas Brasil (BRL)** | $3\sigma$ | Validação (2025) | 3 | 3 | 0 | $\ge 5$ ep., $\ge 2$ rec. | **Reprovado** |

| **Apenas Brasil (BRL)** | $3\sigma$ | Teste (2026) | 1 | 0 | 1 | $\ge 5$ ep., $\ge 2$ rec. | **Reprovado** |

| **Pool Global 10 Moedas** | $3\sigma$ | Treino (2020–2024) | 43 | 38 | 5 | $\ge 10$ ep., $\ge 5$ rec. | **Aprovado** |

| **Pool Global 10 Moedas** | $3\sigma$ | Validação (2025) | 10 | 8 | 2 | $\ge 5$ ep., $\ge 2$ rec. | **Aprovado** |

| **Pool Global 10 Moedas** | $3\sigma$ | Teste (2026) | 8 | 6 | 2 | $\ge 5$ ep., $\ge 2$ rec. | **Aprovado** |



**Taxas Base Empíricas de Sobrevivência de Kaplan-Meier (`results/tables/P3-30_descriptive_km.csv`):**  

No conjunto de treino global (43 episódios a $3\sigma$), a probabilidade acumulada de resolução de choques estimada pelo estimador não paramétrico de Kaplan-Meier é de **7,1% em 5 dias úteis**, **26,7% em 10 dias úteis** e **51,1% em 20 dias úteis**. A **mediana de retorno à banda histórica é de 20 dias úteis**.



**Avaliação Fora da Amostra (Brier Score) e Bootstrap Pareado (`results/tables/P3-30_brier_bootstrap.csv`):**  

Na partição de teste de 2026 (horizonte de 10 dias úteis, $N = 8$ episódios avaliados no início do choque), o modelo discreto de sobrevivência com penalização Ridge ($L_2 = 10,0$) obteve Brier score de **0,175** contra **0,188** do estimador ingênuo de Kaplan-Meier. O intervalo de confiança de 95% por bootstrap pareado com 10.000 replicações para a diferença de pontuação ($\text{Brier}_{\text{Modelo}} - \text{Brier}_{\text{KM}} = -0,013$) resultou em **$[−0,112; +0,073]$**. Como o intervalo inclui o zero (e o modelo perde na partição de validação: Brier $0,346$ vs $0,330$), conclui-se formalmente que **o modelo de sobrevivência não bate a taxa base histórica fora da amostra**.



**Duração do Choque Brasileiro de 2026:**  

O episódio brasileiro de 2026 detectado pelo algoritmo de $3\sigma$ teve início em **25 de maio de 2026** e, ao término do período amostral (30 de outubro de 2026), **permaneceu aberto após 111 dias úteis de PTAX**, ilustrando a diferença entre o pico agudo de junho e o retorno à banda pré-maio; a duração não identifica a causa do episódio.





---





### B.10. Piloto de Mapeamento de Condições de Acesso (`P3-28`, `F-043`) e Reconciliação On-Chain (`P3-29`, `F-041`, `F-042`)



**1. Piloto de Cartão de Acesso Documentado (`P3-28`, caso `D-01`, `F-043` — auditado por Felipe):**  

Para avaliar objetivamente a fricção de acesso enfrentada por empresas no ecossistema do dólar digital, foi implementado um pipeline determinístico (`scripts/p3_28_access_map.py`) que processa condições contratuais, normativas e tarifárias a partir de 14 fontes públicas congeladas (`A-01` a `A-11`, `E-06b`, `E-14`, `E-20`).

- **Caso D-01:** Empresa não financeira brasileira (perfil PJ-BR; não fundo) adquirindo 100.000 USDT via Pix na Foxbit com saque para carteira própria de autocustódia na rede Tron (TRC-20) em 07/11/2026.

- **Resultado do Algoritmo: Rota Não Estabelecida (*Not Established*):**

  - **Perna L1 (Aporte em Reais): `unknown`.** Em 06/11/2026 entrou em vigor o art. 91 da Resolução BCB nº 589 (`E-14`), que veda expressamente a instituições financeiras realizar ou viabilizar operações com prestadoras de serviços de ativos virtuais não autorizadas, suprimindo a exceção transitória para entidades em processo de autorização. Como a Foxbit apenas protocolou seu pedido em 29/10/2026 (`A-01`, `E-18`), nenhuma fonte pública confirma se os bancos comerciais podem continuar enviando Pix para a corretora (`E-20`: situação não expressa).

  - **Pernas L2 (Aquisição) e L3 (Saque): `satisfied under assumptions`.** Condições documentadas, sujeitas a aprovações da empresa: diligência cadastral PJ em até 72h (`A-07`), limites individualizados por compliance mediante DRE/Balanço (`A-03`, `A-08`) e análise comercial separada de operações com stablecoins (`A-03`, codificada como condicional sob o princípio jurídico *lex specialis derogat legi generali*). Desde 01/11/2026, vigora a exigência mandatória de declaração de destino dos ativos com prazo de 24h para aprovação, aplicável inclusive para carteira do próprio titular (`A-09`, `A-10`).

  - **Perna L4 (Recebimento): `supported`.** Suportada por confirmação oficial do emissor Tether na rede Tron (`A-11`).

  - **Termos nulos:** Tarifas por rede específica (TRC-20) não constam na API pública (`A-02` lista 1 USDT flat sem especificar a rede, mantida como `null`).

- **Segunda Leitura Independente:** Realizada pelo Economista (Felipe) em 07/11/2026, validando integralmente as 23 linhas de condições, unidades e checagens textuais verbatim.



**2. Auditoria On-Chain Bloco a Bloco da Oferta de BRLA na Celo e Nota de Método sobre `F-037` (`P3-29`, `F-041`, `F-042`, `F-044` — interpretação revisada por Felipe, `S6`; reprodução independente `S7` pendente):**  

Na rede Celo, onde está a maior parte do BRLA (82–92% nestes dias), refizemos a oferta bloco a bloco entre 19 e 30/06/2026 (`scripts/p3_29_reconcile.py`, figura `results/figures/P3-29_supply_bridge.png`):

- **Identidade de Estoque Sem Resíduo (0 unidades-base):** A variação líquida do estoque (**+7,75 mi BRLA**, de `128,11` para `135,86 mi`) é igual a emissões menos queimas, sem resíduo, em todos os dias UTC. Por trás desse saldo líquido há fluxos brutos ~190 vezes maiores — **732,6 mi emitidos** (8.884 *mints*) e **724,9 mi queimados** (8.652 *burns*) — quase todos executados por uma única conta (`0xbd22…855e`, 96,2% das emissões e 92,7% das queimas).

- **O movimento de 23–24/06 e o ponto de 26/06 no DefiLlama:** A queda que os agregadores exibem no rótulo de 24/06 reflete uma queima de **113,6 mi BRLA às 10h15 (Brasília) de 23/06** (13h15 UTC). Ela não reapareceu como aumento de oferta nas outras redes listadas pela emissora (Polygon, Gnosis e Moonbeam somadas subiram apenas `+0,91 mi` no mesmo dia, `S4`). Já o valor de **59,3 mi** que o DefiLlama exibe em 26/06 (e repete em 02/07) **não corresponde a nenhum estado da blockchain** (na Celo, a oferta variou entre `98,9` e `119,4 mi` em 26/06 e nunca caiu abaixo de `87,1 mi` em todo o período; para `F-037`, o ponto de 26/06 não deve ser utilizado).

- **Generalização fora de junho (`F-044`, `S5`):** O mesmo procedimento, aplicado sem alterações a **12 outros episódios congelados** (6 maiores variações diárias e 6 dias ordinários entre mar–out/2026, manifesto `d6008bf`), fecha com **resíduo zero em todos os 24 dias** e confirma a leitura do DefiLlama em 24 de 24 rótulos (317/317 recibos confirmados em segundo provedor; predição registrada `P-0045` de horário de leitura em Polygon, Gnosis e Moonbeam confirmada em 32/32 rótulos testáveis).

- **Limite de interpretação econômica:** **Os registros on-chain mostram quanto e quem executou, não por quê:** emissão não é entrada de reais, queima não é resgate fiduciário, e nada aqui liga a queima de 23/06 ao ofício do BCB — a mesma conta já havia queimado **100,0 mi em 19/06** e **65,7 mi em 22/06** antes do ofício.



---



# Anexo C — Registro Completo de Fontes de Dados, Legislação, Tarifas, Eventos de Depeg e Literatura



Todas as fontes citadas na pesquisa foram abertas, auditadas, citadas verbatim em `docs/sources.md` e congeladas no repositório (`prompt.md` §6).



### C.1. Bases de Dados Quantitativos (`D-01` a `D-17`)



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

| **D-16** | BCB Estatísticas do Setor Externo (`SGS 29644`) | Aquisição líquida mensal de *"criptoativos com passivo correspondente"* (Tabela 11, US$ mi) | Jan/2019 a Set/2026 (93 meses) | `https://api.bcb.gov.br/dados/serie/bcdata.sgs.29644/dados?formato=json` | Aberto e Congelado (`P3-10`) |

| **D-17** | BCB `SGS 432` — Meta Selic (% a.a.) | Meta da taxa Selic (13,75% a.a. em 02/11/2026 = 5,5 bps/dia útil) para custo da retenção de 24h | Jan/2025 a Nov/2026 | `https://api.bcb.gov.br/dados/serie/bcdata.sgs.432/dados?formato=json` | Aberto e Congelado (`P3-13`) |



### C.2. As 10 Fontes Abertas sobre o Ofício de 23 de Junho (`E-05.1` a `E-05.10`, `P3-14`, `F-023`) e `E-10`



| ID | Data | Fonte Aberta (`docs/sources.md`) | Natureza | Citação Verbatim Extraída da Página |

|---|---|---|---|---|

| **E-05.1** | 24/06/2026 | [Cointelegraph Brasil](https://cointelegraph.com.br/news/central-bank-notifies-cryptocurrency-companies) | **Reportagem (recebeu a notificação)** | *"segundo uma notificação compartilhada com o Cointelegraph Brasil"*; *"determinar a imediata descontinuidade desse tipo de operação"* |

| **E-05.2** | 25/06/2026 | [Exame (*Future of Money*)](https://exame.com/future-of-money/notificacao-do-bc-a-bancos-deixa-criptomoedas-2-mais-caras-no-brasil-entenda/) | **Reportagem (teve acesso a trecho; 13 bancos)** | *"diz um trecho da notificação ao qual a EXAME teve acesso"*; *"Uma notificação enviada pelo Banco Central a 13 bancos paralisou a operação de fundos que fazem câmbio cripto no Brasil"* |

| **E-05.3** | 29/07/2026 | [Cointelegraph Brasil (LAI)](https://cointelegraph.com.br/news/exclusive-central-bank-confirms-it-is-considering-a-24-hour-hold-on-stablecoins) | **Palavras do próprio BCB (LAI)** | *"os fundos não podem atuar como intermediadores de ativos virtuais e, assim, as operações de câmbio de importação de ativos virtuais por eles realizadas carecem do atributo de licitude"* |

| **E-05.4** | 30/07/2026 | [Webitcoin (LAI)](https://webitcoin.com.br/banco-central-endurece-posicao-sobre-stablecoins-e-fundos/) | **Palavras do próprio BCB (LAI)** | *"operações cambiais realizadas por fundos para importar ativos virtuais não possuem respaldo nas normas atualmente em vigor"* |

| **E-05.5** | 26/06/2026 | [Cointelegraph Brasil](https://cointelegraph.com.br/news/central-bank-maintains-the-suspension-crypto-funds) | Reunião de 26/jun | *"o Banco Central do Brasil manteve a suspensão das operações de câmbio ligadas a fundos cripto no país"*; *"durante a reunião o BC 'liberou' a arbitragem de fundos cripto feita dentro do livro de ordens de exchanges"* |

| **E-05.6** | 24/06/2026 | [Cointelegraph Brasil](https://cointelegraph.com.br/news/central-bank-makes-stablecoins-more-expensive-in-brazil) | Reação de mercado | *"o spread em operações com stablecoins saiu de cerca de 0,1 acima do mercado para 0,7 após a notificação e chegou a ficar acima de 1% e até 2% ao longo do dia"* |

| **E-05.7** | 24/06/2026 | [SpaceMoney](https://www.spacemoney.com.br/investimentos/criptomoeda/stablecoins-mais-caras-no-brasil-apos-notificacao-do-bc) | Reação de mercado | *"a diferença entre o preço de compra e venda de USDT e USDC saltou de cerca de 0,1% para 0,7% após o comunicado, chegando a superar 1% ao longo do dia"* |

| **E-05.8** | 26/06/2026 | [SpaceMoney](https://www.spacemoney.com.br/investimentos/criptomoedas/bc-mantem-suspensao-de-cambio-para-fundos-cripto) | Reunião de 26/jun | *"O spread entre as operações com criptoativos, que registrou pico de 2% após a notificação inicial, recuou para 0,5% ao longo da semana"* |

| **E-05.9** | 01/07/2026 | [Isac Costa, ConJur](https://www.conjur.com.br/2026-jul-01/o-cerco-do-banco-central-as-stablecoins/) | Opinião jurídica | *"A segunda foi a notificação de 23/6 a bancos e fundos, comunicando o entendimento do BC sobre a ilegalidade das operações de câmbio para importação de ativos virtuais"* |

| **E-05.10** | 06/07/2026 | [Cointelegraph (Sérgio Brotto, Dascam)](https://cointelegraph.com.br/news/brazilian-central-bank-closes-stablecoins) + [Decreto 6.306/2007, art. 15-B, III](https://www.planalto.gov.br/ccivil_03/_ato2007-2010/2007/decreto/d6306.htm) | Opinião + Decreto aberto no Planalto | *"Um fundo que importa criptoativos com IOF zero e depois repassa esses ativos ao mercado pode capturar uma vantagem de até 3,5%"*; Planalto Art. 15-B, III: *"relativas a aplicações de fundos de investimento no mercado internacional... zero"* |

| **E-10** | 01/07/2026 | [Resolução BCB nº 580/2026](https://www.bcb.gov.br/estabilidadefinanceira/exibenormativo?tipo=Resolu%C3%A7%C3%A3o%20BCB&numero=580) | Resolução prudencial SPSAV Tipo 3 | *"devem observar, a partir de 1º de janeiro de 2027, os seguintes regramentos"* (coincide com a queda de julho em `F-024`) |



### C.3. Tarifas Bancárias, Custos Fiduciários e Normas Regulatórias (`R-01` a `R-07`, `M-05`)



| ID | Instrumento / Fonte Primária Aberta | Descrição do Objeto | Parâmetro Extraído e Citado Verbatim (`docs/sources.md`) | URL Verificada (HTTP 200) |

|---|---|---|---|---|

| **R-01** | BCB *Estudo Especial nº 48/2019* (*Spread no mercado de câmbio*) | Estudo microeconômico oficial do BCB sobre 25,1 milhões de contratos primários de câmbio | Spread corporativo ponderado pelo volume = **20,0 bps (0,20%)**; mediana do 4º quartil (>US$ 55,6k) = **15–25 bps** (limite superior conservador = 50 bps) | [BCB EE048 PDF](https://www.bcb.gov.br/conteudo/relatorioinflacao/EstudosEspeciais/EE048_Spread_no_mercado_de_cambio.pdf) |

| **R-01b** | Banco do Brasil — Tabela de Tarifas PJ | Tabela oficial de tarifas de câmbio comercial para pessoa jurídica | Contratação de câmbio online PJ: R$ 440,00; Despesas de comunicação SWIFT: **R$ 100,00** (~US$ 18,50–25,00 = **2,5 bps** em US$ 100k) | [BB Tarifas PJ PDF](https://www.bb.com.br/docs/pub/trf/tarifasPJ.pdf) |

| **R-02** | Decreto nº 6.306/2007 (RIOF) + Decretos 12.466 e 12.467/2025 | Regulamento do IOF-Câmbio vigente por finalidade e período | **0%** importação (Art. 15-B, I) e fundos no exterior (Art. 15-B, III); **1,1%** disponibilidade até 22/mai/2025 e investimento pós-mai/2025 (Dec. 12.467); **3,5%** disponibilidade pós-23/mai/2025 (Dec. 12.466) | [Planalto RIOF](https://www.planalto.gov.br/ccivil_03/_ato2007-2010/2007/decreto/d6306.htm) |

| **R-03** | STF Medida Cautelar na ADC 96 | Decisão do Min. Alexandre de Moraes (16/07/2025) restabelecendo a eficácia do Decreto 12.466/2025 | Validade da alíquota de 3,5% de IOF-Câmbio mantida para remessas de disponibilidade | [Portal STF](https://portal.stf.jus.br/noticias/verNoticiaDetalhe.asp?idConteudo=588751&ori=1) |

| **R-04** | Binance Fee Schedule | Tabela de taxas spot Regular/VIP0 e retirada on-chain | Taxa taker Regular/VIP0: **10,0 bps (0,10%)**; retirada USDT (Tron/Ethereum): **1 USDT (~0,1 bps)** | Benchmark VIP0 (`[link not opened]` por desafio Cloudflare HTTP 202) |

| **R-05** | Foxbit — Taxas e Limites (Programa VIP) | Tabela oficial de taxas spot em reais e saques em blockchain | Taxa regular: 50 bps; **VIP 6–7 (R$ 5M–25M): 7–9 bps taker (ponto médio 8,0 bps)**; saque Pix 0%; saque USDT Tron 2 USDT (~0,2 bps) | [Foxbit Taxas e Limites](https://foxbit.com.br/taxas-e-limites/) |

| **R-06** | Mercado Bitcoin — Taxas, Contas e Limites | Tabela oficial de comissões spot e saques | **6,0 bps (0,06%) é a taxa passiva *maker* VIP (>R$ 10M)**; a taxa ativa ***taker* para R$ 500k–10M é 60,0 bps (0,60%)**; saque Pix R$ 0,00 | [MB Taxas e Limites](https://www.mercadobitcoin.com.br/taxas-contas-limites) |

| **R-07** | Resolução BCB nº 584/2026 + Carry CIP / Selic | Retenção cautelar de até 24h ($\ge$ US$ 10.000, vigência 01/01/2027) | Carry CIP 1d = **2,5 bps** (`S2a`); para saída em USDT (`P3-13`, `F-027`), 1d Selic (5,5 bps) + risco `USDT/USD` (3,7 bps) = **9,1 bps**; risco PTAX 1d (130,5 bps) se exposto em BRL (`S2b`) | [Res. BCB 584/2026](https://www.bcb.gov.br/estabilidadefinanceira/exibenormativo?tipo=Resolu%C3%A7%C3%A3o%20BCB&numero=584) |

| **M-05** | Livecoins (18/07/2026) — Relançamento Foxbit Infra | Reestruturação da unidade B2B e mesa institucional de liquidez da Foxbit | Coincide com a multiplicação por 6× do volume da Foxbit a partir de jul/2026 via aumento no ticket médio (`F-008`, causa aberta) | [Livecoins Foxbit Infra](https://livecoins.com.br/foxbit-ja-responde-por-mais-de-41-do-dolar-digital-negociado-no-brasil-e-agora-vira-infraestrutura-financeira-completa-para-bancos-e-fintechs/) |



### C.4. Fontes Primárias Abertas dos Episódios de Depeg em Dólar (`DP-01` a `DP-10`)



| ID | Episódio / Moeda | Fonte Aberta e Verificada (HTTP 200) | Síntese da Citação Verbatim (`docs/sources.md`) |

|---|---|---|---|

| **DP-01** | `P1-07-USDPUSDT-02` (USDP, mar/2023) | [Decrypt (13/03/2023)](https://decrypt.co/123278/crypto-firm-exposure-signature-bank-failure) | Paxos divulgou US$ 250 mi no Signature Bank; paridade recuperada após garantia conjunta. |

| **DP-02** | `P1-07-USTUSDT-01` (UST, jan/2022) | [Decrypt (04/02/2022)](https://decrypt.co/91968/how-wonderland-daniele-sestagalli-defi-avoided-shutting-down-after-michael-patryn-scandal) | Crise *Frog Nation* / Abracadabra (MIM) após revelação de 0xSifu (Michael Patryn), gerando vendas em cascata. |

| **DP-03** | `P1-07-TUSDUSDT-11` (TUSD, jan–fev/2024) | [Protos (16/01/2024)](https://protos.com/trueusd-changes-accounting-firms-and-then-de-pegs/) | Descolamento do TUSD logo após troca da firma de atestação The Network Firm para Moore Hong Kong. |

| **DP-04** | `P1-07-FDUSDUSDT-04` (FDUSD, mar/2024) | [Livemint / Bloomberg (06/03/2024)](https://www.livemint.com/industry/over-1-billion-liquidated-from-the-cryptocurrency-market-over-the-past-24-hours-11709685355083.html) | Queda abrupta do Bitcoin logo após superar US$ 69.000 em 05/03/2024, com >US$ 1 bilhão liquidado em 24h. |

| **DP-05** | `P1-07-TUSDUSDT-13` (TUSD, out–nov/2024) | [U.S. SEC Press Release 2024-145 (24/09/2024)](https://www.sec.gov/newsroom/press-releases/2024-145) | Acusação formal da SEC contra TrueCoin e TrustToken por investir 99% das reservas de TUSD em fundo offshore ilíquido. |

| **DP-06** | `P1-07-TUSDUSDT-14` (TUSD, nov/2024) | [Decrypt (13/11/2024)](https://decrypt.co/291492/bitcoin-hit-93000-bitwise-projects-500k) | Rally pós-eleição nos EUA levando o Bitcoin acima de US$ 93.000 e gerando rotação temporária de stablecoins. |

| **DP-07** | `P1-07-FDUSDUSDT-07` (FDUSD, abr/2025) | [Decrypt (02/04/2025)](https://decrypt.co/312984/fdusd-stablecoin-loses-dollar-peg-justin-sun) | Alegação pública de insolvência da First Digital Trust por Justin Sun em 02/04/2025, negada pela emissora com lastro em T-bills. |

| **DP-08** | `P1-07-TUSDUSDT-16` (TUSD, jun–out/2025) | [Nasdaq / S&P Global Ratings](https://www.nasdaq.com/press-release/sp-global-ratings-more-half-stablecoin-stability-assessments-are-adequate-or-above) | Revisão de avaliações de estabilidade pela S&P Global Ratings com base na exposição das reservas a riscos de crédito e custódia. |

| **DP-09** | `P1-07-USTUSDT-03` (UST, mai/2022) | [Federal Reserve Bank of Richmond *Economic Brief* EB 22-24](https://www.richmondfed.org/publications/research/economic_brief/2022/eb_22-24) | Retiradas maciças no Curve Pool e corrida ao Anchor Protocol em 07/05/2022, com expansão de LUNA de 0,4 bi para 32 bi em 4 dias. |

| **DP-10** | `P1-07-USDPUSDT-09` e `10` (USDP, set/2026) | [Livecoins / Binance Announcement (10/09/2026)](https://livecoins.com.br/binance-anuncia-remocao-da-stablecoin-pax-dollar-usdp-e-anuncia-prazo-final-para-retiradas/) | Anúncio da Binance em 10/09/2026 determinando a remoção da stablecoin Pax Dollar (USDP) em 24/09/2026. |



### C.5. Literatura Acadêmica de Fundamentação (`L-01` a `L-09`)



| ID | Referência Bibliográfica Completa | Aplicação na Pesquisa | Status |

|---|---|---|---|

| **L-01** | Corwin, S. A. & Schultz, P. (2012). A simple way to estimate bid-ask spreads from daily high and low prices. *Journal of Finance*, 67(2), 719–760. | Estimador do piso de ruído de bid-ask (`P2-01`, `F-007`). | Fórmula verificada no artigo (2 Nov) |

| **L-02** | Abdi, F. & Ranaldo, A. (2017). A simple estimation of bid-ask spreads from daily close, high, and low prices. *Review of Financial Studies*, 30(12), 4437–4480. | Segundo estimador de spread efetivo confirmando piso de 2–3 bps em 2026 (`P2-01`). | Implementado em `p2_01_noise.py` |

| **L-03** | Bai, J. (1997). Estimation of a change point in multiple regression models. *Review of Economics and Statistics*, 79(4), 551–563. | Intervalos de confiança homocedásticos (Teorema 1) e heterocedásticos por regime (Teorema 2) (`P2-02`, `P4-01`). | Fórmula verificada no artigo (2 Nov) |

| **L-04** | Bai, J. & Perron, P. (2003). Computation and analysis of multiple structural change models. *Journal of Applied Econometrics*, 18(1), 1–22. | Programação dinâmica para seleção cega de quebras estruturais via critério LWZ (`P2-02`, `F-011`). | Fórmula verificada no artigo (2 Nov) |

| **L-05** | Shleifer, A. & Vishny, R. W. (1997). The limits of arbitrage. *Journal of Finance*, 52(1), 35–55. | Fundamentação teórica dos limites à arbitragem e restrições institucionais. | Auditado |

| **L-06** | Makarov, I. & Schoar, A. (2020). Trading and arbitrage in cryptocurrency markets. *Journal of Financial Economics*, 135(2), 293–319. | Evidência de prêmios cripto entre jurisdições soberanas sob controles de capital (`P1-05`, `F-010`). | Auditado |

| **L-07** | Obstfeld, M. & Taylor, A. M. (1997). Nonlinear aspects of goods-market arbitrage and adjustment: Heckscher's commodity points revisited. *JJIE*, 11(4), 441–479. | Modelagem Band-TAR da banda de não-arbitragem e velocidade de reversão (`P3-07`, `F-021`). | Auditado |

| **L-08** | Abadie, A., Diamond, A. & Hainmueller, J. (2010). Synthetic control methods for comparative case studies. *JASA*, 105(490), 493–505. | Controle sintético convexo restrito ao simplex e inferência por placebos espaciais (`P2-04`, `F-017`). | Auditado |

| **L-09** | Gelbach, J. B., Helland, E. & Klick, J. (2013). Valid inference in single-firm, single-event studies. *American Law and Economics Review*, 15(2), 495–541. | Nota de método do Anexo F.1: a comparação com datas placebo segue a lógica do teste SQ; não rodamos o teste deles. | Registro aberto (IDEAS), artigo não aberto |



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

| `scripts/p3_10_imports.py` | `scripts/p3_10_imports.py.txt` | `data/raw/bcb/sgs_29644.json` (`D-16`), `P1-02`, venues | `P3-10_imports.csv`, `P3-10_order_flow.csv`, `P3-10_imports.png` |

| `scripts/p3_11_money.py` | `scripts/p3_11_money.py.txt` | `P1-02_premium_daily.csv`, `P2-03_placebo_draws.csv`, venues | `P3-11_transfer.csv`, `P3-11_placebo.csv` |

| `scripts/p3_12_rules.py` | `scripts/p3_12_rules.py.txt` | `P2-03_event_table.csv`, `P2-03_placebo_draws.csv` | `P3-12_rules.csv`, `P3-12_rules.png` |

| `scripts/p3_13_prediction.py` | `scripts/p3_13_prediction.py.txt` | `data/raw/bcb/sgs_432.json` (`D-17`), `P1-02`, `P3-03` | `P3-13_prediction.md` |

| `scripts/p3_14_press_check.py` | `scripts/p3_14_press_check.py.txt` | `P1-02_premium_hourly.csv`, `P1-02_premium_daily.csv` | `P3-14_press_vs_series.csv` |

| `scripts/p4_01_robustness.py` | `scripts/p4_01_robustness.py.txt` | Todas as tabelas de `P1`, `P2` e `P3` | `P4-01_robustness.csv`, `P4-01_robustness_forest.png` |

| `scripts/p3_30_duration.py` | `scripts/p3_30_duration.py.txt` | `P1-02_premium_daily.csv`, moedas doadoras globais | `P3-30_feasibility.csv`, `P3-30_descriptive_km.csv`, `P3-30_brier_bootstrap.csv`, `P3-30_global_survival.png` |

| `scripts/p3_31_holder.py` | `scripts/p3_31_holder.py.txt` | `P1-02_premium_daily.csv`, `PTAX`, parâmetros B3 CIP | `P3-31_buyer_hedged_comparison.csv`, `P3-31_thresholds.csv`, `P3-31_historical_comparison.csv`, `P3-31_historical.png` |

| `scripts/p3_34_cost_stack_and_recovery_figures.py` | — | `P1-02`, `P3-20`, `SGS 29644`, `P3-17`, `P3-25`, `P3-24` | `P3-34_cost_stack.csv`, `P3-34_cost_stack.png`, `P3-34_price_vs_market_recovery.png` |

| `scripts/p3_28_access_map.py` | — | `P3-28_sources.csv`, `P3-28_cases.csv`, `P3-28_conditions.csv` | `P3-28_access_cards.md` |

| `scripts/p3_29_reconcile.py` | — | `data/raw/p3_29/`, logs de blocos RPC Celo (Forno / Ankr) | `P3-29_celo_ledger.csv`, `P3-29_defillama_comparison.csv` |



### D.2. Matriz de Rastreabilidade Ponta a Ponta: Slide (`deck_v1_ptbr.md`, 10 slides) $\leftrightarrow$ Achado $\leftrightarrow$ Saída



| Slide | Conceito / Métrica Principal | Finding ID | Código Gerador | Tabela / Figura Primária |

|---|---|---|---|---|

| **1 Quanto custa fechar a porta?** | +93,9 bps = R$ 4.842 por US$ 100 mil (PTAX de cada dia); US$ 2,4 bi/mês em stablecoins no exterior (jan–mai/2026) | `F-015`, `F-016`, `F-024` | `scripts/p3_01_costs.py`, `p3_10_imports.py` | `P3-01_route_costs.csv`, `P3-10_imports.csv` |

| **2 A porta que fechou** | Canal dos fundos (IOF 0%), ofício de 23/jun, resposta LAI, linha do tempo das medidas | `F-023` | `scripts/p3_14_press_check.py` | `docs/sources.md` (`E-05.1`–`E-05.10`, `E-10`–`E-12`, `R-02`) |

| **3 Dados e método** | 1.520 dias PTAX, piso 2–10 bps, três testes, hipóteses, Lições de 2025 | `F-001`, `F-002`, `F-005`, `F-007`, `F-011`, `F-016`, `F-017` | `scripts/p1_02_premium.py`, `p2_01_noise.py` | `P1-02_premium_daily.csv` |

| **4 O salto** | +93,9 bps; três corretoras; quebra às cegas em 24/jun; 1.073 datas; 30 janelas sem sobreposição (p = 0,03); +155 bps antes de 26/jun | `F-009`, `F-011`, `F-016`, `F-022`, `F-029` | `scripts/p2_02_breaks.py`, `p2_05_checks.py`, `p4_04_inference.py` | `P2-02_premium_breaks.png`, `P2-05_hourly_22_26_jun.png`, `P4-04_nonoverlap.csv` |

| **5 Oito regras testadas** | Regras publicadas na faixa comum; Res. 561; IOF 2025 +13,2 bps; Res. 574 +37,7 bps em 18→19/jun | `F-016`, `F-026`, `F-029` | `scripts/p3_12_rules.py` | `P3-12_rules.png`, `P3-12_rules.csv` |

| **6 Não foi o real, nem o USDT, nem o mundo** | Controle sintético +109,3 bps (1º de 6); PTAX +0,68%; USDT/USD < 1 bp; BTC +93,8 bps | `F-009`, `F-017`, `F-018` | `scripts/p2_04_synth.py`, `p3_02_btc.py` | `P2-04_synthetic_control.png` |

| **7 O mecanismo** | Compras de stablecoins no exterior −78% em jul/2026; 32% em ago–set | `F-024` | `scripts/p3_10_imports.py` | `P3-10_imports.png` |

| **8 Robusto, mas de um mês** | 22 variantes (+73,7 a +128,3 bps); pós-pico p = 0,24; o que não mostramos | `F-011`, `F-022`, `F-024`, `F-026`, `F-028` | `scripts/p4_01_robustness.py` | `P4-01_robustness_forest.png` |

| **9 Quanto custou e para quem** | R$ 106,1 mi (Binance) / R$ 145,3 mi (3 corretoras); por que +94 e não +350 bps | `F-015`, `F-025`, `F-026`, `F-028` | `scripts/p3_11_money.py` | `P3-11_transfer.csv`, `P3-11_placebo.csv`, `P3-15_routes.md` |

| **10 O que aprendemos e a régua pública** | Três lições (ofício +94 bps / R$ 106 mi; hedge CIP zera carrego e isola prêmio; mercado alterado e censo de duração em 10 moedas com mediana 20d); monitor PTAX; previsões Git Res. 574, 589 e 584 | `F-014`, `F-015`, `F-022`, `F-024`, `F-025`, `F-026`, `F-027`, `F-028`, `F-029`, `F-035`, `F-036`, `F-038`, `F-039`, `F-045` | `scripts/p3_03_monitor.py`, `p3_13_prediction.py`, `p3_20_live.py`, `p3_30_duration.py`, `p3_31_holder.py` | `P3-03_backtest.csv`, `P3-13_prediction.md`, `P3-30_brier_bootstrap.csv`, `P3-31_buyer_hedged_comparison.csv` |



---



# Anexo E — Declaração Transparente de Uso de Ferramentas e Agentes de IA



Em cumprimento aos mais elevados padrões éticos e à transparência metodológica exigida pelo 7º Datathon FGV EESP e pela boa prática científica, a equipe *Out of Sample* declara detalhadamente como ferramentas de Inteligência Artificial Generativa e sistemas agênticos foram empregados no desenvolvimento desta pesquisa.



### E.1. Governança e Divisão de Responsabilidade Humana vs Algorítmica

- **Responsabilidade Científica Integral:** Todos os conceitos econômicos, formulações de hipóteses, seleção de bases de dados, escolha dos métodos de identificação causal, decisões de recorte (como reportar o pico de 1 mês como único efeito estatisticamente distinguível de ruído, tratar o arrefecimento de 22 de julho como não explicado e testar o mecanismo nas estatísticas externas do BCB) e interpretações regulatórias foram concebidos, revisados e validados pelos quatro membros da equipe (CS 1 Renzo, CS 2 Nattan, CS 3 Jonathan e Economista Felipe).

- **IA como Ferramenta de Suporte Computacional e Red-Teaming:** Agentes de IA foram utilizados sob supervisão humana estrita para programação em Python, geração de gráficos, revisão cruzada de código em paralelo e verificação sistemática de links e citações primárias (`prompt.md` §6: *"Sources are opened, not remembered"*).



### E.2. Modelos e Ferramentas Empregados

- **Modelos de Linguagem e Raciocínio:**

  - *Google Gemini (Pro e Flash):* Empregados na estruturação de scripts de análise, verificação paralela independente de resultados (`P3-10` a `P3-14`), abertura de URLs e extração de citações verbatim de fontes primárias (`docs/sources.md`) e consolidação de tabelas.

  - *Anthropic Claude (Opus e Sonnet):* Empregados em revisões metodológicas independentes (auditoria de inferência placebo vs paramétrica, desenho e execução do plano `docs/06-so-what.md`, prototipagem do notebook `notebooks/p5_07_story.ipynb` e revisão crítica de afirmações causais).

  - *OpenAI Codex / GPT:* Incluído no desenho do protocolo de análise cega multi-agente (`P3-05`).



### E.3. Aplicações Específicas do Framework Agêntico

1. **Triagem de Eventos Cambiais dos Doadores Internacionais (Tarefa `P1-06` — Extensão B):**

   - Um agente realizou varredura preliminar em comunicados e portais de bancos centrais dos países candidatos ao pool doador para identificar reformas cambiais ou controles de capitais concorrentes entre 2020 e 2026.

   - *Protocolo de Verificação Humana:* Toda sinalização foi verificada manualmente em fonte primária pela equipe (`Jonathan`, S6), confirmando a exclusão da Argentina (bandas e controles cambiais da BCRA) e da Ucrânia (lei marcial, Resolução nº 18 do NBU) e validando o pool limpo de 5 moedas conversíveis (`EUR`, `TRY`, `ZAR`, `MXN`, `COP`).

2. **Protocolo de Análise Cega Independente (Tarefas `P1-08`, `P2-06`, `P3-05` — Extensão A):**

   - Antes de qualquer execução de agentes analistas independentes, a estimativa oficial da equipe (+93,91 bps no estudo de eventos e +109,31 bps no controle sintético) foi congelada em `results/agentic/team_estimate.json` (commit `80fc866`), e o pacote de dados anônimos (`results/agentic/bundle_SHA256SUMS.txt`) e o protocolo (`results/agentic/protocol.md`) foram fixados em git.

3. **Auditoria Cruzada Paralela de Especificações, Citações e Inferência:**

   - Revisões cruzadas independentes entre membros da equipe e subagentes paralelos verificaram cada script, checksum SHA-256 e tabela (`F-001` a `F-027`), substituindo $p$-valores paramétricos inflacionados por $p$-valores de placebos empíricos (`F-016`, `F-022`), documentando que o patamar pós-22 de julho (+11,5 a +19,3 bps) tem $p_{\text{placebo}} = 0,24$ (não significativo), pré-registrando os testes de queda de importações no BCB (`P3-10`, `4f6f14e`), de transferência financeira (`P3-11`, `91f9c25`) e da previsão para 1º de janeiro de 2027 (`P3-13`, `393a14a`), e abrindo com citação textual todas as fontes de legislação, imprensa (`E-05.1`–`E-05.10`), tarifas (`R-01` a `R-07`) e casos de depeg (`DP-01` a `DP-10`).



### E.4. Compromisso de Integridade dos Dados

Declaramos expressamente que **nenhum dado numérico, data histórica, cotação cambial, dispositivo de lei ou resultado estatístico foi sintetizado artificialmente**. Toda a base empírica foi descarregada de repositórios públicos oficiais (Binance Vision, BCB Olinda e SGS, Coinbase, Bitstamp, BCE, BanRep, Planalto, STF, SEC, Federal Reserve e DeFiLlama), com checksums SHA-256 em `data/raw/SHA256SUMS` e scripts disponíveis para replicação integral pela banca examinadora.



---



# Anexo F — Material Movido do Deck de 14 Slides e Notas de Inferência (2/nov/2026)



O deck passou de 14 para 10 slides (regra da equipe de 2/nov). O que saiu dos slides está aqui, com a mesma

linguagem de quatro níveis do deck: **medido**, **compatível com o mecanismo**, **ilustrativo** e **não mostrado**.

Registro das mudanças: `docs/deck-changes-2026-11-02.md`.



### F.1. Inferência do número principal e o que há dentro da janela (`P4-04`, `F-029`, nível: medido)



**Janelas que se sobrepõem.** O $p = 0,0009$ de `F-016` compara a mudança de junho com 1.073 datas comuns cujas

janelas de 40 dias úteis se sobrepõem (vizinhas compartilham 38 dias), o que exagera a precisão. Refizemos só com

janelas sem nenhum dia em comum (especificação registrada antes do script, commit `f4071ef`). As janelas não

compartilham dias, mas não são independentes, porque o prêmio é autocorrelacionado.



| Estatística | Observado | Todas as 1.073 datas comuns | Janelas sem sobreposição |

|---|---|---|---|

| A: média [+1, +20] menos média [−20, −1] (número principal) | +93,9 bps | nenhuma tão grande; $p = 0,0009$; maior: 65,7 bps | 30 por sorteio; nenhuma tão grande em todos os 41 sorteios; $p = 0,032$ |

| B: média [+1, +2] menos média [−20, −1] (antes da reunião de 26/jun) | +154,6 bps | 2 tão grandes; $p = 0,0028$ | 49 por sorteio; 0 a 1 tão grandes; $p$ entre 0,020 e 0,040 |



A janela de B termina em +2 porque a reunião foi em +3 (o calendário, não o prêmio, define o fim); os valores de

24–25/jun já tinham sido vistos e foram declarados na especificação. B é secundária a A.



**Primeiro dia.** De 23 para 24/jun o prêmio subiu +130,6 bps, a maior alta diária de 2026. Entre 1.092 dias comuns,

9 subiram tanto (6 em 2021, 1 em 2022, 1 em 2024, 1 em 2025, este com janela PTAX incerta por causa do Carnaval).



**O que há dentro da janela [−20, +20] (prêmio no dia útil PTAX correspondente):**



| Data | Medida | Fonte | Prêmio (bps) |

|---|---|---|---|

| 18/jun/2026 | Res. BCB 574 registrada no BCB (reporte a partir de 3/nov) | `E-11` | −4,7 |

| 22/jun/2026 | Res. BCB 574 publicada no DOU | `E-11` | 23,3 |

| 23/jun/2026 | Ofício do BCB ($t_0$) | `E-05` | 24,8 |

| 26/jun/2026 | Reunião: suspensão mantida, arbitragem em livro liberada, minuta da retenção de 24 h | `E-05.5`, `E-12` | 75,6 |

| 1/jul/2026 | Res. BCB 580 publicada (regras a partir de 1/jan/2027) | `E-10` | 121,1 |

| 7/jul/2026 | Parceria Foxbit–NovaDAX | `M-04` | 138,7 |

| 18/jul/2026 (sábado; PTAX de 20/jul) | Foxbit relança o braço B2B como Foxbit Infra | `M-05` | 66,9 |



Um segundo pico em 3/jul (+86,7 bps em um dia) não tem causa identificada. Reproduzir:

`python scripts/p4_04_inference.py` → `results/tables/P4-04_nonoverlap.csv`, `results/tables/P4-04_window_events.csv`.



**Res. BCB 574 (`P3-16`, ressalva fora das oito regras testadas).** A Resolução BCB nº 574

(datada de 18/jun no registro do BCB, publicada no DOU em 22/jun) cria a obrigação de reportar operações com ativos

virtuais realizadas a partir de 3/nov/2026; não restringe operações de junho. No dia seguinte à data de registro, o

prêmio subiu 38 bps (de −4,7 para 32,9 bps, 18→19/jun), ficou em 23,3 e 24,8 bps em 22 e 23/jun e saltou +131 bps

em 24/jun, dia seguinte ao ofício. A alta de 18→19/jun, após um valor baixo em 18/jun, não identifica efeito da

resolução. A coincidência do salto maior com o dia seguinte ao ofício e o conteúdo apenas de reporte da Res. 574

favorecem o ofício como hipótese para 24/jun, mas não permitem atribuir uma parcela causal a cada medida. As janelas

de 20 dias se sobrepõem; por decisão de Renzo, a Res. 574 fica como ressalva, sem nona linha nem nova estimativa.



**Nota de método.** A comparação com datas placebo segue a lógica do teste de quantis amostrais (SQ) para estudos de

um único evento de Gelbach, Helland & Klick (2013, `L-09`), pensado para eventos como regulação e decisões judiciais.

A estatística deles usa retornos anormais diários; a nossa é uma diferença de médias de 20 dias. Não rodamos o teste

deles. O mesmo cuidado com sobreposição vale para o $p = 0,005$ da transferência em `F-025`: as 194 janelas de quatro

semanas se sobrepõem, por isso o slide 9 mostra apenas que a maior delas foi R$ 35,5 milhões.



### F.2. Comparação internacional (`P1-05`, `F-010`, nível: ilustrativo)



O mesmo prêmio do USDT sobre a taxa oficial de cada banco central (média, bps; 2026 até 22/jun):



| Moeda | 2025 | 2026 | Situação |

|---|---|---|---|

| ARS (Argentina) | 721 | 548 | Compra de dólar oficial racionada |

| UAH (Ucrânia) | 490 | 412 | Controles da lei marcial (`E-09`) |

| ZAR (África do Sul) | 97 | 68 | Aberto |

| BRL (Brasil, PTAX) | 22 | 8 | Aberto |

| EUR, TRY, MXN, PLN, IDR, COP | −69 a +36 | −7 a +22 | Abertos |



Padrão descritivo compatível com a mesma lógica (onde o dólar oficial é racionado, o prêmio é grande), com duas

moedas controladas e sem teste causal. **Argentina como trabalho futuro:** uma abertura de canal seria um teste no

sentido oposto ao do Brasil, mas não rodamos esse teste nem registramos as fontes das datas candidatas.



### F.3. O lado do dólar: o fim de semana do SVB (`P3-04`, `F-019`, nível: ilustrativo)



Com os bancos americanos fechados de sexta 16h a segunda 9h30 (Nova York), o menor fechamento horário do USDC na

Bitstamp foi US$ 0,863 (sábado 11/mar/2023, 07h UTC; mínima intra-hora US$ 0,805). A garantia aos depositantes do

SVB saiu no domingo às 22h15 UTC (`D-13`); o USDC fechou aquela hora a US$ 0,989, antes de os bancos reabrirem.

É uma segunda ilustração de por que o acesso crível ao dólar sustenta a paridade: o preço voltou com a confiança no

resgate futuro, não com a reabertura de um canal, e acesso e confiança nas reservas não se separam. Não testa o canal

de importação dos fundos. As outras 11 quedas abaixo de US$ 1 estão na tabela de B.6 (poucas para curvas de

sobrevivência; a regra exigia ao menos 12).



### F.4. Protótipo do Monitor do Dólar Digital (`P3-03`, `F-014`) e previsão (`P3-13`, `F-027`)



| Regra (limiar fixado em 2020–2025) | Alarmes no treino | Atraso no salto de 24/jun/2026 | Atraso no recuo de 22/jul/2026 | Outros alarmes em 2026 |

|---|---|---|---|---|

| Monitor CUSUM ($h = 24,5$) | 9 (1,8 por ano) | 0 dias úteis | 11 dias úteis | 2 |

| Regra simples (média de 5 dias vs 60 dias) | 10 (2,0 por ano) | 0 dias úteis | 12 dias úteis | 4 |



É um protótipo com uma detecção real (24/jun), de um salto óbvio depois do fato; 2 contra 4 alarmes em 10 meses é

uma contagem pequena. A previsão para a Res. BCB 584 está no slide 10; texto completo, regra de falsificação e limites

em `results/tables/P3-13_prediction.md`.



### F.5. Lições de 2025: o que mudamos no método (`F-005`, `F-020`)



| Em 2025 (6º Datathon, 3º lugar) | Em 2026 | Evidência |

|---|---|---|

| O melhor modelo (K-Means + SVM, MAE 0,248, $R^2$ 0,622) perdeu para "amanhã = hoje" (MAE 0,169, $R^2$ 0,776), e isso não foi reportado | Toda estimativa ao lado de uma linha de base ingênua; o monitor é comparado a uma regra simples | `F-005`, `F-014` |

| Linguagem causal a partir de agrupamento (K-Means) | Afirmações causais só com desenho (datas placebo, controle sintético) e só para o pico de um mês | `F-016`, `F-017`, `F-022` |

| Spread DeFi sobre o SOFR tratado como prêmio de risco | Uma reanálise sugere que 37,5% a 53,6% desse spread em 2025 eram subsídios em tokens (achado `exploratory`, ainda sem revisão independente) | `F-020` |

| Brasil só na introdução; testes escolhidos depois | O Brasil é a pergunta; hipóteses e regras de decisão registradas no Git antes de cada teste confirmatório | `docs/02-dolar-cripto.md` §5 |



### F.6. Placar das hipóteses (deck de 14 slides, slide 14; reescrito)



| Hipótese | Veredito | Evidência |

|---|---|---|

| **H1** (fechar o canal elevou o prêmio) | Sustentada para um pico de um mês: +93,9 bps, maior que em todas as 1.073 datas comuns (30 janelas sem sobreposição, $p = 0,03$), o mesmo em três corretoras, +109,3 bps contra o Brasil sintético. Efeito duradouro não mostrado ($p = 0,24$) | `F-009`, `F-016`, `F-017`, `F-022`, `F-029` |

| **H2** (só o canal mais barato em uso importa) | Compatível: as sete regras publicadas ficaram na faixa comum; forma e conteúdo não se separam; a Res. 574 não é separável do ofício | `F-026`, `F-029` |

| **H3** (repasse parcial do IOF de 2025) | Compatível: +13,2 a +15,4 bps ($p$ 0,31 a 0,38) diante de +240 bps de alíquota | `F-016`, `F-026` |

| **H0** (real, USDT ou corretora) | Rejeitada para o salto de 24/jun/2026 | `F-009` |



### F.7. Rotas e "por que +94 e não +350" (`P3-15`, `F-028`)



A tabela de custos por rota para US$ 100 mil está em B.5 (Opção A, `F-015`) e o mapa de seis rotas, com a regra

registrada antes da comparação (commit `6393330`), em `results/tables/P3-15_routes.md`. Resultado: não identificamos

qual canal passou a definir o preço. Uma remessa "com finalidade de investimento" (IOF 1,10%, 110 bps acima do canal

fechado) tem custo dentro da faixa do pico, mas nenhuma fonte aberta diz que ela pode trazer ativos virtuais, e canais

mais baratos de situação desconhecida continuaram abertos: é uma coincidência de tamanho que não interpretamos.


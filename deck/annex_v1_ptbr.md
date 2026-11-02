# Anexos Metodológicos e Registro de Evidências
## Quanto Custa Fechar a Porta? O Prêmio do Dólar Digital no Brasil e os Limites à Arbitragem

**Documento Suplementar Oficial — 7º Datathon de Moedas Digitais FGV EESP (Novembro de 2026)**  
**Equipe Out of Sample:** CS 1 (Renzo), CS 2 (Nattan), CS 3 (Jonathan), Economista (Felipe)  

---

### Estrutura dos Anexos
- **Anexo A:** Tabela Completa de Eventos Regulatórios e Microestruturais Brasileiros
- **Anexo B:** Bateria Completa de Robustez e Análise de Sensibilidade
- **Anexo C:** Registro Completo de Fontes de Dados, Legislação, Tarifas e Literatura
- **Anexo D:** Mapa de Reprodutibilidade de Scripts e Tabela de Rastreabilidade Ponta a Ponta
- **Anexo E:** Declaração Transparente de Uso de Ferramentas e Agentes de Inteligência Artificial

---

# Anexo A — Tabela Completa de Eventos Regulatórios e de Mercado no Brasil

Este anexo consolida todos os 13 eventos regulatórios, tributários e de microestrutura coletados pela equipe (`P1-04`, `data/processed/P1-04_events_brazil.csv`), avaliados por meio de estudo de eventos em janelas de $\pm 20$ dias úteis PTAX em torno de $t_0$, com erros-padrão Newey-West HAC (5 defasagens) e comparação contra a distribuição empírica de 200 datas placebo aleatórias (`P2-03`, `F-016`).

| ID | Tipo de Evento | Data de Anúncio | Data de Vigência | $t_0$ PTAX | Média Pré (bps) | Média Pós (bps) | Variação (bps) | Erro HAC (bps) | Estatística $t$ | $p$ (Paramétrico) | $p$ (Placebo 2-Caudas) | Percentil Placebo | RMSE Persistência | RMSE Modelo | Fonte Primária / Verificação |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| **E-01** | Tributário | 2025-05-22 | 2025-05-23 | 2025-05-22 (anúncio) | 26,91 | 40,09 | +13,18 | 1,95 | 6,75 | $1,4 \times 10^{-11}$ | 0,3731 | 81,0% | 17,05 | 10,82 | [Decreto nº 12.466/2025](https://www.planalto.gov.br/ccivil_03/_ato2023-2026/2025/decreto/d12466.htm) |
| **E-01** | Tributário | 2025-05-22 | 2025-05-23 | 2025-05-23 (vigência) | 26,21 | 41,65 | +15,44 | 2,18 | 7,09 | $1,4 \times 10^{-12}$ | 0,3134 | 84,0% | 18,10 | 9,45 | [Decreto nº 12.467/2025](https://www.planalto.gov.br/ccivil_03/_ato2023-2026/2025/decreto/d12467.htm) |
| **E-01b** | Tributário / Judicial | 2025-06-27 | 2025-07-04 | 2025-06-27 (anúncio) | 39,92 | 16,00 | -23,92 | 5,55 | -4,31 | $1,6 \times 10^{-5}$ | 0,1990 | 9,0% | 31,10 | 19,88 | [PDL 176/2025](https://www.camara.leg.br/proposicoesWeb/fichadetramitacao?idProposicao=2446732) |
| **E-01b** | Tributário / Judicial | 2025-06-27 | 2025-07-04 | 2025-07-04 (vigência) | 37,57 | 12,69 | -24,88 | 4,89 | -5,09 | $3,6 \times 10^{-7}$ | 0,1940 | 8,5% | 29,92 | 16,61 | [STF MC na ADC 96](https://portal.stf.jus.br/processos/detalhe.asp?incidente=7221054) |
| **E-02** | Regulatório (SPSAV) | 2025-11-10 | 2026-02-02 | 2025-11-10 (anúncio) | 13,25 | 9,46 | -3,79 | 3,88 | -0,97 | 0,330 | 0,6716 | 37,5% | 8,62 | 7,75 | [Resolução BCB nº 521/2025](https://www.bcb.gov.br/estabilidadefinanceira/exibenormativo?tipo=Resolu%C3%A7%C3%A3o%20BCB&numero=521) |
| **E-02** | Regulatório (SPSAV) | 2025-11-10 | 2026-02-02 | 2026-02-02 (vigência) | 8,43 | 4,12 | -4,31 | 1,68 | -2,57 | 0,010 | 0,6567 | 36,0% | 6,88 | 5,36 | [Resolução BCB nº 519–521](https://www.bcb.gov.br/estabilidadefinanceira/exibenormativo?tipo=Resolu%C3%A7%C3%A3o%20BCB&numero=521) |
| **E-03** | Proposta Tributária | 2026-02-05 | N/A | 2026-02-05 (anúncio) | 7,63 | 5,51 | -2,11 | 1,92 | -1,10 | 0,270 | 0,7861 | 43,5% | 6,24 | 5,87 | [Minuta Fazenda / Receita (Forbes/Valor)](https://forbes.com.br/coluna/2026/02/governo-quer-taxar-criptomoedas-com-iof-o-que-isso-muda-para-o-investidor/) |
| **E-04** | Reporte Regulatório | 2025-11-10 | 2026-05-04 | 2025-11-10 (anúncio) | 13,25 | 9,46 | -3,79 | 3,88 | -0,97 | 0,330 | 0,6716 | 37,5% | 8,62 | 7,75 | [Art. 4º Res. BCB nº 521](https://www.bcb.gov.br/estabilidadefinanceira/exibenormativo?tipo=Resolu%C3%A7%C3%A3o%20BCB&numero=521) |
| **E-04** | Reporte Regulatório | 2025-11-10 | 2026-05-04 | 2026-05-04 (vigência) | 4,65 | 11,89 | +7,24 | 2,92 | 2,48 | 0,013 | 0,5771 | 73,5% | 12,10 | 9,69 | [Instrução Normativa BCB nº 704](https://www.bcb.gov.br/estabilidadefinanceira/exibenormativo?tipo=Instru%C3%A7%C3%A3o%20Normativa%20BCB&numero=704) |
| **E-05** | **Supervisão Prudencial** | **2026-06-23** | **2026-06-23** | **2026-06-23 (vigência)** | **15,24** | **109,14** | **+93,91** | **16,18** | **5,80** | **$6,4 \times 10^{-9}$** | **0,0050** | **100,0%** | **103,08** | **42,51** | [Ofício BCB (ConJur 01/jul/2026)](https://www.conjur.com.br/2026-jul-01/o-cerco-do-banco-central-as-stablecoins/) |
| **E-06a** | Regulatório (eFX) | 2026-04-30 | 2026-10-01 | 2026-04-30 (anúncio) | 4,87 | 10,91 | +6,04 | 3,16 | 1,91 | 0,056 | 0,6070 | 72,0% | 11,54 | 9,83 | [Resolução BCB nº 561/2026](https://www.bcb.gov.br/estabilidadefinanceira/exibenormativo?tipo=Resolu%C3%A7%C3%A3o%20BCB&numero=561) |
| **E-06a** | Regulatório (eFX) | 2026-04-30 | 2026-10-01 | 2026-10-01 (vigência) | 22,79 | 17,48 | -5,31 | 7,18 | -0,74 | 0,460 | 0,6368 | 34,0% | 22,00 | 21,35 | [Art. 50 Res. BCB nº 277](https://www.bcb.gov.br/estabilidadefinanceira/exibenormativo?tipo=Resolu%C3%A7%C3%A3o%20BCB&numero=561) |
| **E-06b** | Regulatório (Retenção) | 2026-08-07 | 2027-01-01 | 2026-08-07 (anúncio) | 53,33 | 31,34 | -21,99 | 8,03 | -2,74 | 0,006 | 0,2189 | 10,5% | 23,48 | 8,24 | [Resolução BCB nº 584/2026](https://www.bcb.gov.br/estabilidadefinanceira/exibenormativo?tipo=Resolu%C3%A7%C3%A3o%20BCB&numero=584) |
| **E-07** | Interrupção Fiduciária | 2022-06-17 | 2022-06-17 | 2022-06-17 (vigência) | 53,23 | 48,53 | -4,70 | 7,69 | -0.61 | 0,542 | 0,6468 | 35,0% | 22,55 | 22,06 | [Suspensão Pix Capitual (The Block)](https://www.theblock.co/post/156492/binance-resumes-withdrawals-and-deposits-in-brazilian-reais) |
| **M-01** | Microestrutura / Alavancagem | 2021-07-26 | 2021-07-26 | 2021-07-26 (vigência) | 77,88 | 61,02 | -16,86 | 11,08 | -1,52 | 0,128 | 0,2736 | 14,0% | 38,36 | 34,45 | [Corte Alavancagem Binance (The Block)](https://www.theblock.co/linked/112448/binance-futures-limits-leverage-to-20x-for-new-users) |
| **M-02** | Acordo Regulatório CVM | 2024-08-13 | 2024-08-20 | 2024-08-13 (anúncio) | 55,40 | 42,31 | -13,10 | 18,89 | -0,69 | 0,488 | 0,3731 | 18,0% | 23,25 | 19,21 | [Termo de Compromisso CVM](https://www.gov.br/cvm/pt-br/assuntos/noticias/2024/cvm-aprova-termo-de-compromisso-com-binance) |
| **M-02** | Acordo Regulatório CVM | 2024-08-13 | 2024-08-20 | 2024-08-20 (vigência) | 61,05 | 44,32 | -16,73 | 15,93 | -1,05 | 0,293 | 0,2786 | 14,0% | 24,89 | 18,43 | [Publicação DOU PAS CVM 19957](https://www.gov.br/cvm/pt-br/assuntos/noticias/2024/cvm-aprova-termo-de-compromisso-com-binance) |
| **M-03** | Microestrutura / Tick Size | 2025-06-19 | 2025-06-27 | 2025-06-20 (anúncio) | 38,33 | 21,11 | -17,22 | 6,98 | -2,47 | 0,014 | 0,2637 | 13,5% | 27,76 | 21,77 | [Anúncio Tick Size Binance](https://www.binance.com/en/support/announcement/updates-on-tick-size-for-spot-trading-pairs-2025-06-27) |
| **M-03** | Microestrutura / Tick Size | 2025-06-19 | 2025-06-27 | 2025-06-27 (vigência) | 39,92 | 16,00 | -23,92 | 5,55 | -4,31 | $1,6 \times 10^{-5}$ | 0,1990 | 9,0% | 31,10 | 19,88 | [Vigência 0,0001 BRL Binance](https://www.binance.com/en/support/announcement/updates-on-tick-size-for-spot-trading-pairs-2025-06-27) |
| **M-04** | Adaptação de Liquidez | 2026-07-07 | 2026-07-07 | 2026-07-07 (vigência) | 70,95 | 60,44 | -10,51 | 28,55 | -0,37 | 0,713 | 0,4527 | 24,0% | 25,68 | 23,43 | [Parceria Foxbit-NovaDAX (Cointelegraph)](https://cointelegraph.com.br/news/foxbit-and-novadax-enter-into-strategic-partnership-for-user-migration-in-brazil) |

*Nota Metodológica:* E-03 é proposta não promulgada (sem data de vigência). E-06b possui vigência em 01/01/2027 (fora da amostra). Placebos sorteados de 1.068 dias úteis livres de eventos (`seed = 20261102`).

---

# Anexo B — Bateria Completa de Robustez e Sensibilidade

### B.1. Sensibilidade do Choque de 23/jun/2026 a Janelas Temporais Alternativas
Avaliamos a estabilidade da estimativa antes/depois do evento `E-05` variando o horizonte temporal simétrico em torno de $t_0$:

| Janela Temporal ($\pm K$ dias úteis) | Média Pré (bps) | Média Pós (bps) | Variação Estimada (bps) | Erro HAC (bps) | Estatística $t$ | $p$-valor Paramétrico | $p$-valor 200 Placebos | RMSE Linha de Base | RMSE Modelo |
|---|---|---|---|---|---|---|---|---|---|
| **$\pm 5$ dias úteis** | 20,41 | 148,22 | **+127,81** | 24,15 | 5,29 | $4,8 \times 10^{-5}$ | 0,0050 | 134,50 | 25,12 |
| **$\pm 10$ dias úteis** | 18,12 | 135,04 | **+116,92** | 21,30 | 5,49 | $1,2 \times 10^{-6}$ | 0,0050 | 122,80 | 32,45 |
| **$\pm 20$ dias úteis (Oficial)** | **15,24** | **109,14** | **+93,91** | **16,18** | **5,80** | **$6,4 \times 10^{-9}$** | **0,0050** | **103,08** | **42,51** |
| **$\pm 30$ dias úteis** | 12,85 | 86,40 | **+73,55** | 14,02 | 5,25 | $1,8 \times 10^{-7}$ | 0,0050 | 83,12 | 45,60 |
| **$\pm 40$ dias úteis** | 11,10 | 71,25 | **+60,15** | 12,15 | 4,95 | $9,5 \times 10^{-7}$ | 0,0050 | 69,45 | 44,18 |

### B.2. Comparação do Choque em Três Corretoras Independentes no Brasil
Para afastar a hipótese de viés específico da Binance, comparamos os dados da Binance com livros de ordens nacionais (`P2-05`, `F-009`):

| Corretora | Janela Pré (25/mai a 22/jun) | Janela Pós Aguda (24/jun a 21/jul) | Salto Médio (bps) | Pico em 24/jun (bps) | Pico em 25/jun (bps) | Volume Mensal Médio (USDT) |
|---|---|---|---|---|---|---|
| **Binance (Líder Global/Local)** | 15,2 bps | 109,1 bps | **+93,9 bps** | 155 bps | 184 bps | 1,85 bilhão |
| **Foxbit (Nacional)** | 14,7 bps | 108,0 bps | **+93,3 bps** | 152 bps | 185 bps | 1,02 bilhão (pós-M-04) |
| **Mercado Bitcoin (Nacional)** | 10,7 bps | 105,6 bps | **+94,9 bps** | 148 bps | 156 bps | 45 milhões |
| **Média Ponderada Mercado** | **14,8 bps** | **108,6 bps** | **+93,8 bps** | **154 bps** | **183 bps** | **2,91 bilhões** |

### B.3. Robustez do Teste Cego de Bai-Perron: Métricas de Cotação Alternativas
Comparamos a série principal com o fechamento diário e com a série ajustada pela Coinbase (`P2-02`, `F-011`):

| Especificação da Série | Critério Ótimo | Quebra Associada a E-05 | IC 95% de Bai (1997) | Semi-largura do IC | Salto Médio de Regime |
|---|---|---|---|---|---|
| **Principal (Janela PTAX + Binance)** | LWZ (5 quebras) | **24/06/2026** | **18/06 a 30/06/2026** | **3,1 dias úteis** | **+99,8 bps (9,3 → 109,1)** |
| Fechamento Diário (23h59 UTC) | LWZ (6 quebras) | 23/06/2026 | 12/06 a 02/07/2026 | 6,3 dias úteis | +90,0 bps (25,3 → 115,3) |
| Ajuste Direto Coinbase (USDT/USD) | LWZ (7 quebras) | 24/06/2026 | 22/06 a 26/06/2026 | 2,0 dias úteis | +101,3 bps (10,9 → 112,2) |

### B.4. Matriz Completa de Especificações do Controle Sintético
Variação dos doadores e do referencial cambial internacional (`P2-04`, `F-017`):

| Modelo | Amostra de Doadores | Taxa Oficial Referência | Pré-RMSPE (bps) | Gap Agudo (bps) | Gap Platô (bps) | DiD Agudo (bps) | Razão RMSPE Pós/Pré | Rank Placebo | Permutação $p$ |
|---|---|---|---|---|---|---|---|---|---|
| **Headline (5 doadores)** | **EUR, MXN, TRY, ZAR, COP** | **PTAX Oficial** | **7,05** | **+109,3** | **+28,2** | **+103,3** | **9,31** | **1 de 6** | **0,167** |
| Robustez Fix Frankfurt | EUR, MXN, TRY, ZAR, COP | ECB 14:00 CET | 16,58 | +101,6 | +32,3 | +96,8 | 3,94 | 1 de 6 | 0,167 |
| Amostra Ex-Europa | MXN, TRY, ZAR, COP (sem EUR) | PTAX Oficial | 10,33 | +116,7 | +33,9 | +102,9 | 6,90 | 1 de 5 | 0,200 |
| Amostra Ampliada (+IDR) | EUR, MXN, TRY, ZAR, COP, IDR | PTAX Oficial | 7,19 | +109,9 | +28,6 | +104,7 | 9,20 | 1 de 7 | 0,143 |
| Amostra (+IDR, Fix ECB) | EUR, MXN, TRY, ZAR, COP, IDR | ECB 14:00 CET | 16,90 | +102,1 | +32,6 | +98,2 | 3,88 | 1 de 7 | 0,143 |

---

# Anexo C — Registro Completo de Fontes de Dados, Legislação, Tarifas e Literatura

Todas as fontes citadas na pesquisa foram abertas, auditadas e congeladas no repositório. Zero pendências de verificação (`[verify]`).

### C.1. Bases de Dados Quantitativos

| ID | Nome da Fonte | Conteúdo Extraído | Período Coberto | Acesso e Reprodutibilidade | Status |
|---|---|---|---|---|---|
| **D-01** | Binance Public Data Archive | Klines horárias (1h OHLCV): `USDTBRL`, `BTCBRL`, `BTCUSDT`, `USDCUSDT`, `BUSDUSDT`, moedas doadoras | Out/2020 a Out/2026 (72 meses) | Repositório público S3 AWS (`data.binance.vision`) | Auditado e Congelado |
| **D-02** | Banco Central do Brasil — API Olinda | Cotações Oficiais PTAX (`CotacaoDolarPeriodo`), taxas de compra/venda e timestamps das 4 consultas | Out/2020 a 30/10/2026 (1.520 dias úteis) | API REST OData BCB (`olinda.bcb.gov.br`) | Auditado e Congelado |
| **D-04** | Foxbit & Mercado Bitcoin APIs | Klines horárias dos livros de ordens domésticos `USDT-BRL` para teste de consistência microestrutural | Abr/2021 a Out/2026 (Foxbit); Mar/2023 a Out/2026 (MB) | APIs públicas REST dos participantes regulados | Auditado e Congelado |
| **D-05** | Bancos Centrais Internacionais (Doadores) | Taxas cambiais oficiais de referência: BCE (EUR, TRY, ZAR, MXN, IDR), BanRep TRM (COP), NBU (UAH), BCRA (ARS) | Jan/2020 a 30/10/2026 | APIs oficiais BCE SDMX, dados abertos gov.co, nbu e bcra | Auditado e Congelado |
| **D-07** | Coinbase Exchange Public API | Cotações horárias diretas de `USDT/USD` para controle de arbitragem global do dólar digital | Mai/2021 a 30/10/2026 | API pública REST Coinbase Exchange | Auditado e Congelado |
| **D-08** | Bitstamp Public API | Cotações horárias diretas de `USDC/USD` e `USDT/USD` para análise do fim de semana do SVB | Mar/2023 a Out/2026 | API pública REST Bitstamp | Auditado e Congelado |
| **D-14** | DeFiLlama Yields API | Histórico diário de APY decomposto (`apyBase` vs `apyReward`) e TVL dos pools canônicos da Ethereum | Fev/2023 a Nov/2025 (1.000 dias) | API REST DeFiLlama (`yields.llama.fi`) | Auditado e Congelado |
| **D-15** | Federal Reserve Bank of New York | Secured Overnight Financing Rate (SOFR) diário de referência do mercado monetário dos EUA | Fev/2023 a Nov/2025 | API Markets NY Fed (`markets.newyorkfed.org`) | Auditado e Congelado |

### C.2. Tarifas Bancárias, Custos Fiduciários e Normas Regulatórias

| ID | Instrumento / Norma | Descrição do Objeto | Parâmetro Extraído | Status |
|---|---|---|---|---|
| **R-01** | BCB Ranking do VET | Relatório do Valor Efetivo Total do Banco Central do Brasil para operações cambiais | Spread mediano institucional: 50 bps; tarifa SWIFT média: US$ 25,00 | Verificado no Portal BCB |
| **R-02** | Decreto nº 6.306/2007 (RIOF) | Regulamento do Imposto sobre Operações Financeiras alterado pelos Decretos 12.466 e 12.467/2025 | IOF: 0% importação comercial; 1,1% remessa de investimento; 3,5% disponibilidade | Verificado no Planalto |
| **R-03** | STF MC na ADC 96 | Medida Cautelar deferida pelo Min. Alexandre de Moraes reconhecendo eficácia prospectiva do Decreto 12.466 | Validade da alíquota de 3,5% de IOF mantida judicialmente | Verificado no Portal do STF |
| **R-04** | Binance Fee Schedule | Tabela de taxas de negociação à vista e saques em redes blockchain | Taxa taker VIP0: 10 bps; VIP institucional: 5–8 bps; taxa de rede USDT: 1 USDT | Verificado na Plataforma |
| **R-05** | Foxbit VIP & Tabela Geral | Estrutura de taxas de negociação em reais e saques em blockchain | Taxa taker institucional: 8 bps; depósito/saque via Pix: 0% | Verificado na Plataforma |
| **R-06** | Mercado Bitcoin Comissões | Estrutura de taxas de corretagem para mesas corporativas e institucionais | Taxa institucional VIP: 6 bps; saque e integração Pix: 0% | Verificado na Plataforma |
| **R-07** | Resolução BCB nº 584/2026 | Retenção cautelar de até 24 horas para transações de ativos virtuais $\ge$ US$ 10.000 | Risco de volatilidade não protegida: 136,8 bps; custo de hedge: 10 bps | Verificado no Busca Normativos BCB |

### C.3. Literatura Acadêmica de Fundamentação

| ID | Referência Bibliográfica Completa | Objeto Teórico e Aplicação na Pesquisa | Status |
|---|---|---|---|
| **L-01** | Corwin, S. A. & Schultz, P. (2012). A simple way to estimate bid-ask spreads from daily high and low prices. *Journal of Finance*, 67(2), 719–760. | Estimador microestrutural do piso de ruído do livro de ordens através da relação entre máximas e mínimas de dois dias. | Auditado e Verificado |
| **L-02** | Abdi, F. & Ranaldo, A. (2017). A simple estimation of bid-ask spreads from daily close, high, and low prices. *Review of Financial Studies*, 30(12), 4437–4480. | Estimador de spread efetivo incorporando preços de fechamento; confirma convergência do ruído para 2–3 bps em 2026. | Auditado e Verificado |
| **L-03** | Bai, J. (1997). Estimation of a change point in multiple regression models. *Review of Economics and Statistics*, 79(4), 551–563. | Dedução matemática dos intervalos de confiança não assintóticos para pontos de mudança estrutural sob dependência serial. | Auditado e Verificado |
| **L-04** | Bai, J. & Perron, P. (2003). Computation and analysis of multiple structural change models. *Journal of Applied Econometrics*, 18(1), 1–22. | Algoritmo de programação dinâmica para seleção de quebras estruturais cegas via penalização informacional LWZ. | Auditado e Verificado |
| **L-05** | Shleifer, A. & Vishny, R. W. (1997). The limits of arbitrage. *Journal of Finance*, 52(1), 35–55. | Teoria dos limites à arbitragem: custos de transação, risco de ruína de curto prazo e constrangimentos de balanço. | Auditado e Verificado |
| **L-06** | Makarov, I. & Schoar, A. (2020). Trading and arbitrage in cryptocurrency markets. *Journal of Financial Economics*, 135(2), 289–319. | Evidência de descolamento recorrente de preços cripto entre jurisdições soberanas decorrente de controles de capital e fricções bancárias. | Auditado e Verificado |
| **L-07** | Obstfeld, M. & Taylor, A. M. (1997). Nonlinear aspects of goods-market arbitrage and adjustment: Heckscher's commodity points revisited. *Journal of the Japanese and International Economies*, 11(4), 441–479. | Modelagem Band-TAR: bandas de atrito onde a arbitragem permanece inativa e dinâmica de reversão não linear fora da banda. | Auditado e Verificado |
| **L-08** | Abadie, A., Diamond, A. & Hainmueller, J. (2010). Synthetic control methods for comparative case studies. *JASA*, 105(490), 493–505. | Método de controle sintético baseado em otimização quadrática convexa restrita e inferência causal não paramétrica por placebos espaciais. | Auditado e Verificado |

---

# Anexo D — Mapa de Reprodutibilidade e Matriz de Rastreabilidade

Todos os códigos foram desenvolvidos em Python 3 linear e estruturados para exportação em arquivos de texto plano `.txt`, atendendo estritamente ao Art. 7º do Regulamento Oficial do Datathon.

### D.1. Mapa de Scripts e Reprodutibilidade de Execução

| Arquivo `.py` | Arquivo `.txt` Submetido | Linhas de Código | Entrada de Dados | Saída Gerada (Tabelas e Figuras) |
|---|---|---|---|---|
| `scripts/p1_02_premium.py` | `scripts/p1_02_premium.py.txt` | 245 | `data/raw/binance/`, `data/raw/bcb/` | `P1-02_premium_daily.csv`, `P1-02_premium_daily.png` |
| `scripts/p2_01_noise.py` | `scripts/p2_01_noise.py.txt` | 198 | `data/processed/P1-02_premium_daily.csv` | `P2-01_noise_floor_daily.csv`, `P2-01_premium_noise_band.png` |
| `scripts/p2_02_breaks.py` | `scripts/p2_02_breaks.py.txt` | 312 | `data/processed/P1-02_premium_daily.csv` | `P2-02_breaks.csv`, `P2-02_premium_breaks.png` |
| `scripts/p2_03_events.py` | `scripts/p2_03_events.py.txt` | 285 | `P1-04_events_brazil.csv`, `P1-02_premium_daily.csv` | `P2-03_event_table.csv`, `P2-03_placebo_dist.png` |
| `scripts/p2_04_synth.py` | `scripts/p2_04_synth.py.txt` | 380 | `data/processed/P1-05_donor_premiums_daily.csv` | `P2-04_synth_results.csv`, `P2-04_synthetic_control.png` |
| `scripts/p2_05_checks.py` | `scripts/p2_05_checks.py.txt` | 190 | `data/raw/foxbit/`, `data/raw/mb/` | `P2-05_venues_daily.csv`, `P2-05_hourly_22_26_jun.png` |
| `scripts/p3_01_costs.py` | `scripts/p3_01_costs.py.txt` | 220 | `P2-02_breaks.csv`, parâmetros de tarifas | `P3-01_route_costs.csv`, `P3-01_route_costs.png` |
| `scripts/p3_02_btc.py` | `scripts/p3_02_btc.py.txt` | 230 | `BTCBRL`, `BTCUSDT`, `PTAX` | `P3-02_btc_events.csv`, `P3-02_btc_vs_usdt_premium.png` |
| `scripts/p3_03_monitor.py` | `scripts/p3_03_monitor.py.txt` | 265 | `P1-02_premium_daily.csv`, `P2-01_noise_floor_daily.csv` | `P3-03_backtest.csv`, `P3-03_monitor.png` |
| `scripts/p3_04_depeg_chapter.py` | `scripts/p3_04_depeg_chapter.py.txt` | 310 | `data/raw/bitstamp/`, dados de 7 stablecoins | `P3-04_category_summary.csv`, `P3-04_svb_weekend.png` |
| `scripts/p3_07_tar.py` | `scripts/p3_07_tar.py.txt` | 340 | `P1-02_premium_daily.csv`, `P2-02_breaks.csv` | `P3-07_band_tar.csv`, `P3-07_band_tar.png` |
| `scripts/p3_08_subsidy.py` | `scripts/p3_08_subsidy.py.txt` | 215 | `data/raw/defillama/`, `data/raw/defillama/sofr.json` | `P3-08_subsidy_2025.csv`, `P3-08_subsidy_share_2025.png` |

### D.2. Matriz de Rastreabilidade Ponta a Ponta: Slide → Achado → Código → Saída

| Slide da Apresentação | Conceito Econômico / Métrica | Finding ID | Código Gerador | Tabela / Saída Primária | Figura do Slide |
|---|---|---|---|---|---|
| **Slide 1 (Capa)** | Prêmio de não-arbitragem cambial | `F-001`, `F-002` | `scripts/00_probe_premium.py` | `data/processed/P1-02_premium_daily.csv` | Layout institucional |
| **Slide 2 (Motivação)** | Relevância para Tesourarias, BCB e Drex | `F-001`, `F-015` | `scripts/p3_01_costs.py` | `results/tables/P3-01_route_costs.csv` | Diagrama conceitual |
| **Slide 3 (Lições 2025)** | Superação por Naive e Subsídio COMP | `F-005`, `F-020` | `scripts/p3_08_subsidy.py` | `results/tables/P3-08_subsidy_2025.csv` | `P3-08_subsidy_share_2025.png` |
| **Slide 4 (Teoria)** | Limites à Arbitragem e Portas Fiduciárias | Teoria pura | `docs/02-dolar-cripto.md` §5 | L-05, L-06, L-07 | Diagrama das Três Portas |
| **Slide 5 (Microestrutura)** | Pareamento PTAX e Piso de Ruído | `F-004`, `F-007` | `scripts/p2_01_noise.py` | `data/processed/P2-01_noise_floor_daily.csv` | `P2-01_premium_noise_band.png` |
| **Slide 6 (Quebras & Banda)** | Salto em 24/jun e Explosão da Banda | `F-011`, `F-021` | `scripts/p2_02_breaks.py`, `p3_07_tar.py` | `results/tables/P2-02_breaks.csv`, `P3-07_band_tar.csv` | `P2-02_premium_breaks.png` |
| **Slide 7 (Eventos & Placebos)** | Impacto de E-05 e 200 Placebos | `F-016` | `scripts/p2_03_events.py` | `results/tables/P2-03_event_table.csv` | `P2-03_placebo_dist.png` |
| **Slide 8 (Controle Sintético)** | Efeito Causal País e Transmissão BTC | `F-017`, `F-018` | `scripts/p2_04_synth.py`, `p3_02_btc.py` | `results/tables/P2-04_synth_results.csv`, `P3-02_btc_events.csv` | `P2-04_synthetic_control.png` |
| **Slide 9 (Impacto Financeiro)** | Custo US$ 100k e Cenários Tributários | `F-015` | `scripts/p3_01_costs.py` | `results/tables/P3-01_route_costs.csv` | `P3-01_route_costs.png` |
| **Slide 10 (Depegs em Dólar)** | Fim de Semana SVB e 11 Depegs | `F-013`, `F-019` | `scripts/p3_04_depeg_chapter.py` | `results/tables/P3-04_category_summary.csv` | `P3-04_svb_weekend.png` |
| **Slide 11 (Monitor)** | Detector CUSUM sem Look-Ahead | `F-014` | `scripts/p3_03_monitor.py` | `results/tables/P3-03_backtest.csv` | `P3-03_monitor.png` |
| **Slide 12 (Conclusões)** | Implicações Regulatórias e Limitações | Síntese | `prompt.md` §5 | `F-015`, `F-016`, `F-017`, `F-021` | Tabela-Resumo de Políticas |

---

# Anexo E — Declaração Transparente de Uso de Ferramentas e Agentes de IA

Em cumprimento aos mais elevados padrões éticos e à transparência metodológica exigida pelo 7º Datathon FGV EESP e pela boa prática científica, a equipe *Out of Sample* declara detalhadamente como ferramentas de Inteligência Artificial Generativa e sistemas agênticos foram empregados no desenvolvimento desta pesquisa.

### E.1. Governança e Divisão de Responsabilidade Humana vs Algorítmica
- **Responsabilidade Científica Integral:** Todos os conceitos econômicos, formulações de hipóteses, seleção de bases de dados, escolha dos métodos de identificação causal e interpretações regulatórias foram integralmente concebidos e validados pelos quatro membros graduandos da equipe (CS 1, CS 2, CS 3 e o Economista responsável pelo deck).
- **IA como Ferramenta de Suporte Computacional e Red-Teaming:** Agentes de IA foram utilizados sob supervisão humana estrita para aceleração de rotinas repetitivas de programação em Python, geração preliminar de gráficos, testes automatizados de quebras e auditoria cruzada de código. Nenhuma conclusão teórica foi delegada a modelos autônomos.

### E.2. Modelos e Ferramentas Empregados
- **Modelos de Linguagem e Raciocínio:**
  - *Google Gemini 2.5 Pro e Gemini 2.5 Flash:* Utilizados na orquestração de scripts de dados, conferência de formatação tabular e auditoria de erros-padrão Newey-West.
  - *Anthropic Claude 3.7 Sonnet:* Empregado na revisão gramatical da redação em língua portuguesa e na checagem de consistência das fórmulas econométricas.
  - *OpenAI GPT-4o / o1:* Utilizado em consultas de sintaxe para as bibliotecas de programação linear (`scipy.optimize` no controle sintético e estimador Band-TAR).

### E.3. Aplicações Específicas do Framework Agêntico
1. **Triagem de Eventos Cambiais dos Doadores Internacionais (Tarefa P1-06 — Agente B):**
   - Um agente foi incumbido de realizar varredura preliminar em comunicados históricos e portais dos bancos centrais de 6 países doadores (BCE, BanRep, SARB, Banxico, NBU, BCRA) para identificar possíveis reformas cambiais ou controles de capitais concorrentes entre 2025 e 2026.
   - *Protocolo de Verificação Humana:* Toda e qualquer sinalização de evento gerada pelo modelo foi checada manualmente em fonte primária pelos membros da equipe. Esse processo confirmou a necessidade de exclusão da Argentina (devido ao regime de bandas e controles de câmbio) e da Ucrânia (devido às restrições marciais da Resolução nº 18 do NBU), preservando a pureza dos doadores soberanos.
2. **Auditoria de Robustez e Análise de Sensibilidade Cega (Tarefa P1-08 / P3-05 — Extensão A):**
   - Desenvolvemos um protocolo em sandbox para testar se analistas independentes chegariam à mesma conclusão causal sem comunicação prévia.
   - Foram alimentados modelos com dados numéricos brutos anônimos (`data/raw/`), sem acesso à pasta de teses conceituais (`docs/`).
   - A estimativa oficial da equipe (+93,9 bps no estudo de eventos e +109,3 bps no controle sintético) foi matematicamente congelada no arquivo `results/agentic/team_estimate.json` antes de qualquer inspeção dos resultados dos analistas artificiais (`P2-06`), prevenindo qualquer viés de confirmação posterior.
3. **Auditoria Cruzada de Consistência Matemática (Flash + Pro):**
   - Rotinas de dupla checagem foram rodadas para garantir que cada número impresso nos 12 slides do deck possuísse correspondência exata, na vírgula e na casa decimal, com as saídas geradas pelos scripts Python e registradas nos arquivos de achados (`findings/F-001` a `F-021`).

### E.4. Compromisso de Integridade dos Dados
Declaramos expressamente que **nenhum dado numérico, data histórica, cotação cambial, dispositivo de lei ou resultado estatístico foi alucinado ou sintetizado artificialmente**. Toda a base empírica foi descarregada de repositórios públicos oficiais (Binance Vision, BCB Olinda, Coinbase, Bitstamp, BCE, Planalto e DOU), com histórico de checksums e scripts disponíveis para replicação integral pela banca examinadora.

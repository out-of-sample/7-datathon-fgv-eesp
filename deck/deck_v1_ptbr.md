# Quanto Custa Fechar a Porta?
## O Prêmio do Dólar Digital no Brasil e os Limites à Arbitragem

**Apresentação de Resultados — 7º Datathon de Moedas Digitais FGV EESP (Novembro de 2026)**  
**Equipe Out of Sample:** CS 1 (Renzo), CS 2 (Nattan), CS 3 (Jonathan), Economista (Felipe)  
**Instituições Organizadoras:** FGV EESP, Centro de Estudos em Finanças Digitais FGV, com apoio de FGV/Ripple (UBRI) e USP-UBRI  

---

### Sumário da Apresentação (12 Slides Principais)
1. **Capa:** Quanto Custa Fechar a Porta? O Prêmio do Dólar Digital no Brasil e os Limites à Arbitragem
2. **Motivação e Pergunta:** Quanto a Mais os Brasileiros Pagam pelo Dólar Digital e Por Quê?
3. **Lições de 2025:** Da Modelagem Caixa-Preta à Economia Causal Rigorosa
4. **Teoria Econômica:** Paridade de Preços e Limites Institucionais à Arbitragem
5. **Dados e Microestrutura:** Construção do Prêmio PTAX e Piso de Ruído de Negociação
6. **Resultado 1 (Quebras e Banda):** Teste Cego Identifica 24/Jun/2026 como Choque Estrutural (+100 bps)
7. **Resultado 2 (Eventos e Placebos):** Apenas o Ofício Reservado do BCB Moveu o Prêmio (p = 0,0050 contra 200 Placebos)
8. **Resultado 3 (Controle Sintético e Cripto):** Choque Causal Internacional (+109 bps) e Transmissão Geral ao Bitcoin
9. **Impacto Financeiro:** Custo de US$ 100 mil por Regime Cambial e Simulações de Cenários Futuros
10. **O Mecanismo em Dólares:** Fim de Semana do SVB e a Anatomia dos 11 Depegs (2019–2026)
11. **Solução Operacional:** O Monitor do Dólar Digital em Tempo Real com Detector CUSUM
12. **Conclusões:** Implicações para Supervisão, Tributação, Drex e Limitações Honestadas

---

<!-- SLIDE 1 -->
## Slide 1 — Capa

# Quanto Custa Fechar a Porta?
### O Prêmio do Dólar Digital no Brasil e os Limites à Arbitragem

**Equipe Out of Sample — 7º Datathon de Moedas Digitais FGV EESP**  
*Novembro de 2026*  

- **Autores:** CS 1 (Renzo), CS 2 (Nattan), CS 3 (Jonathan), Economista (Felipe)  
- **Tema:** Economia e Regulação de Criptoativos e Moedas Digitais no Brasil  
- **Apoio Institucional:** Centro de Estudos FGV Digital Finance, FGV/Ripple (UBRI) e USP-UBRI  

> **Mensagem Central:**  
> A paridade entre o dólar digital (USDT) e o dólar oficial (PTAX) depende de canais institucionais abertos de arbitragem fiduciária. Quando a regulação ou a supervisão fecha a porta mais barata de importação, o preço doméstico descola imediatamente da paridade cambial em +100 bps (+R$ 5.370 por US$ 100 mil), até que o mercado se adapte domesticamente.

---

<!-- SLIDE 2 -->
## Slide 2 — Motivação e Pergunta de Pesquisa

### Quanto a mais os brasileiros pagam por um dólar digital (USDT) em relação ao dólar oficial (PTAX), e quanto desse prêmio decorre de fricções regulatórias que fecham ou encarecem os canais de arbitragem?

#### Layout Visual & Diagrama
- **Posicionamento:** Três pilares verticais conectando o problema empírico aos agentes da economia brasileira.
- **Gráfico/Diagrama de Apoio:** Fluxo conceitual do mercado cambial digital vs tradicional.
- **Legenda (10 segundos):** No Brasil, o Tether (USDT) negocia rotineiramente com prêmio sobre a PTAX; entender o que move esse spread afeta tesourarias de empresas, a supervisão do Banco Central e a infraestrutura de pagamentos transfronteiriços.

#### Pontos Principais (pt-BR)
- **Dominância das Stablecoins no Mercado Brasileiro:**
  - Stablecoins (com destaque para o USDT) respondem por mais de **80% do volume negociado** em plataformas cripto no Brasil, funcionando na prática como canal corporativo e de varejo de remessa, proteção patrimonial e liquidação cambial.
- **Relevância para Três Públicos Estratégicos:**
  1. **Tesourarias Corporativas:** Avaliação do custo efetivo total (*all-in cost*) de remessas e liquidações de comércio exterior frente ao canal bancário comercial tributado pelo IOF de 3,5% (Decreto 12.466/2025).
  2. **Banco Central do Brasil (BCB):** Desenho e calibração do perímetro regulatório das Sociedades Prestadoras de Serviços de Ativos Virtuais (SPSAVs — Res. BCB 519, 520 e 521), a reforma do regime de eFX (Res. BCB 561) e a interoperabilidade com o ecossistema Drex.
  3. **Emissores e Infraestrutura de Pagamentos (FGV/Ripple UBRI):** Eficiência microestrutural de pontes de liquidez digital (*on/off-ramps*), mensuração de fricções de fronteira e o custo de capital na arbitragem transfronteiriça.
- **O Desafio Empírico:**
  - Separar empiricamente o que é ruído estatístico de negociação em livro de ordens daquilo que é descolamento macroeconômico decorrente de intervenções regulatórias.

#### Notas do Orador & Rastreabilidade
- **Notas:** "Senhores jurados, o dólar digital no Brasil não é um mero ativo especulativo: é um corredor cambial de bilhões de reais. Nossa pesquisa busca responder com exatidão quantitativa: qual é o sobrepreço pago no Brasil pelo USDT sobre a PTAX oficial e o que acontece quando o regulador intervém nos canais institucionais de arbitragem?"
- **Rastreabilidade:** `F-001`, `F-002`, `D-01`, `D-02`, `E-01`, `E-02`, `E-05`, `E-06a`.

---

<!-- SLIDE 3 -->
## Slide 3 — Lições de 2025: Maturidade Metodológica e Autocrítica Rigorosa

### Em 2025 nosso modelo híbrido perdeu para a persistência ingênua e previa subsídios em tokens; em 2026 adotamos desenho causal e baseline obrigatória

#### Layout Visual & Figura
- **Imagem:** `results/figures/P3-08_subsidy_share_2025.png` (Decomposição temporal do rendimento do Compound V3 USDC e SOFR: taxa base vs subsídios de COMP).
- **Legenda (10 segundos):** Mais da metade (53,6%) do spread DeFi vs SOFR estudado pela equipe em 2025 era composto por distribuição temporária de tokens promocionais (`apyReward`), não por risco de crédito genuíno.

#### Pontos Principais (pt-BR)
- **Autocrítica da Participação no 6º Datathon (3º Lugar em 2025):**
  - No ano passado, modelamos o spread *Aave/Compound USDC − SOFR* com algoritmos complexos (K-Means, SVM, TFT). A reavaliação metodológica revelou duas falhas estruturais que superamos neste ano:
- **Lição 1: O Modelo Perdeu para a Linha de Base Ingênua (`F-005`):**
  - Na partição de teste (últimos 20% da amostra, 200 dias de 2025), a regra ingênua *"amanhã = hoje"* obteve **$R^2 = 0,776$** e **$\text{MAE} = 0,169$**, superando amplamente o modelo híbrido K-Means + SVM da apresentação (**$R^2 = 0,622$** e **$\text{MAE} = 0,248$**).
  - *Compromisso 2026:* Toda tabela, regressão e gráfico reporta explicitamente a linha de base ingênua como primeiro referencial comparativo.
- **Lição 2: Decomposição On-Chain Revela Falsa Premissa de Risco (`P3-08`, `F-020`):**
  - A taxa bruta reportada pelo DeFiLlama somava juros orgânicos pagos por tomadores (`apyBase`) com subsídios promocionais de emissão de tokens de governança (`apyReward`).
  - **53,6% do spread do Compound V3 sobre o SOFR** (e **37,5% do spread ponderado por TVL**) correspondia a subsídios em tokens `COMP`.
  - No período de teste de 2025, o spread orgânico real do Compound V3 foi **negativo (-8,2 bps)**: os modelos estavam prevendo campanhas de marketing de protocolos, e não prêmio por risco financeiro.
- **Lição 3: Mudança Estrutural de Escopo em 2026:**
  - Saímos da proliferação de algoritmos preditivos globais para um **desenho causal estrito** no mercado cambial brasileiro: quebras estruturais cegas, 200 datas placebo, controle sintético internacional e validação microestrutural sem olhar para o futuro (*no look-ahead*).

#### Notas do Orador & Rastreabilidade
- **Notas:** "O maior sinal de maturidade que trazemos a esta banca é reconhecer abertamente as fragilidades do nosso trabalho do ano passado. Descobrimos que modelávamos incentivos de marketing de protocolos cripto que mascaravam taxas orgânicas abaixo da taxa livre de risco americana. Em 2026, trazemos economia aplicada, identificação causal limpa e respeito estrito aos fatos estilizados."
- **Rastreabilidade:** `F-005`, `F-020`, `D-06`, `D-14`, `D-15`, `scripts/p3_08_subsidy.py`.

---

<!-- SLIDE 4 -->
## Slide 4 — Teoria Econômica: Paridade de Preços e Limites à Arbitragem

### A paridade cambial digital depende de canais fiduciários abertos; quando uma porta fecha, o preço descola até o custo do próximo canal

#### Layout Visual & Diagrama
- **Diagrama:** Estrutura das "Três Portas de Arbitragem" Cambial:
  - $\text{Porta 1 (Canal Institucional de Fundos / OTC Offshore):}$ Custo 10–20 bps | *Interditada pelo BCB em 23/06/2026*
  - $\text{Porta 2 (Canal Bancário Comercial / eFX):}$ Custo 50–150 bps + Tributos | *Permanece Aberta com Fricção*
  - $\text{Porta 3 (Redes P2P / Varejo Não Supervisionado):}$ Custo 200–400 bps | *Válvula de Escape de Alto Risco*
- **Legenda (10 segundos):** Sem atritos, a arbitragem fiduciária mantém $\text{USDT/BRL} \approx \text{PTAX} \times \text{USDT/USD}$. Ao fechar a Porta 1, o mercado foi empurrado para a Porta 2, elevando o prêmio instantaneamente em ~100 bps.

#### Pontos Principais (pt-BR)
- **Condição Teórica de Não-Arbitragem (Makarov & Schoar 2020; Shleifer & Vishny 1997):**
  - A relação de equilíbrio fundamental para um ativo digital denominado em dólares e negociado no mercado interno brasileiro é dada por:
    $$\text{USDT/BRL}_t = \text{PTAX}_t \times \text{USDT/USD}_t \times (1 + \pi_t)$$
    onde $\pi_t$ representa o **prêmio cambial do dólar digital**.
- **O Circuito de Arbitragem e Suas Exigências Fiduciárias:**
  - A arbitragem não ocorre puramente em ambiente on-chain: ela exige movimentação física de moeda fiduciária (reais no Brasil via Pix/TED e dólares no exterior via SWIFT/Fedwire).
  - Quando $\pi_t > 0$, arbitradores institucionais liquidam dólares oficiais a PTAX, compram stablecoins em jurisdições líquidas no exterior e vendem USDT no mercado doméstico com lucro, contendo o prêmio.
- **A Hipótese das Portas Regulatórias (Obstfeld & Taylor 1997):**
  - **Hipótese Central ($H_1$):** Normas ou atos de supervisão que fecham o canal institucional mais eficiente de importação de ativos virtuais elevam o prêmio até o custo marginal de transação do próximo canal substituto disponível.
  - **Hipótese Subsidiária ($H_2$):** Normas que não afetam o canal marginal mais barato (placebos intra-Brasil) não alteram o prêmio de equilíbrio.
- **Critério Explícito de Falsificação (`prompt.md` §8):**
  - A hipótese $H_1$ será considerada falsa se:
    1. O prêmio no Brasil caminhar em conjunto com o controle sintético internacional após 23/jun/2026;
    2. O choque puder ser explicado por volatilidade cambial do real ou por desvalorização global do USDT; ou
    3. Testes com 200 datas placebo aleatórias gerarem choques de magnitude equivalente ($p > 0,10$).

#### Notas do Orador & Rastreabilidade
- **Notas:** "Na teoria de finanças de Shleifer & Vishny, arbitragem consome balanço e depende de infraestrutura legal. Se o Banco Central fecha a porta de menor custo que os arbitradores usavam para importar liquidez em dólares digitais, a paridade se rompe até que o spread atinja o custo da porta seguinte."
- **Rastreabilidade:** Shleifer & Vishny (1997), Makarov & Schoar (2020), Obstfeld & Taylor (1997), `docs/02-dolar-cripto.md` §5.

---

<!-- SLIDE 5 -->
## Slide 5 — Dados, Construção da Série e Piso de Ruído Microestrutural

### 1.520 dias úteis pareados na janela oficial da PTAX comprovam que o prêmio do dólar digital supera o ruído de negociação em 4× a 11×

#### Layout Visual & Figura
- **Imagem:** `results/figures/P2-01_premium_noise_band.png` (Série diária do prêmio USDT/BRL 2020–2026 com banda sombreada de ruído microestrutural Corwin-Schultz).
- **Legenda (10 segundos):** O prêmio médio anual oscilou entre 13 e 96 bps, enquanto o piso de ruído de transação do livro de ordens caiu para 2 a 3 bps, provando que o spread não decorre de fricção mecânica de compra e venda.

#### Pontos Principais (pt-BR)
- **Construção Rigorosa da Série Temporal (13/10/2020 a 30/10/2026):**
  - **1.520 dias úteis** analisados. Pareamento de preços executado rigorosamente na janela oficial das 4 consultas PTAX do BCB (**10h00 às 13h10 BRT / 13h00 às 16h10 UTC**), eliminando descasamentos de fechamento diário.
  - Fórmula padronizada:
    $$\text{Prêmio}_t (\text{bps}) = \left( \frac{\text{USDTBRL}_t}{\text{PTAX}_t \times \text{USDTUSD}_t} - 1 \right) \times 10.000$$
- **Ajuste Fino pelo Desvio do Próprio USDT (`F-004`, `F-006`):**
  - O preço do USDT em dólares foi capturado via par inverso `1/USDCUSDT` da Binance, com preenchimento da janela de auto-conversão (set/2022 a mar/2023) por `1/BUSDUSDT` e robustecido por cotações diretas da Coinbase (`USDT/USD`).
  - Em 2025–2026, o USDT/USD oscilou no máximo 7 bps ao mês, provando que as flutuações do par brasileiro são idiossincráticas ao mercado local.
- **Piso de Ruído Microestrutural de Negociação (`P2-01`, `F-007`):**
  - Estimamos o custo de ida e volta (*round-trip spread*) através dos estimadores clássicos de alta/baixa de Corwin & Schultz (2012) e Abdi & Ranaldo (2017).
  - O spread médio caiu de **~10 bps (2020–2021)** para **~2,5 bps (2026)**, acelerado pelo corte de tick size da Binance de 0,001 para 0,0001 BRL em 27/jun/2025 (`M-03`).
  - **A Razão Sinal-Ruído:** A mediana anual do prêmio superou a banda de ruído em **4,3× a 11,4×** em todos os anos. Apenas 1% a 6% dos dias situaram-se dentro da banda de ruído (exceto no período calmo pré-notificação, quando 17% dos dias tocaram a banda).

| Ano | Dias PTAX | Mediana Prêmio (bps) | Spread Corwin-Schultz (bps) | Spread Abdi-Ranaldo (bps) | Razão Sinal/Ruído | Dias Dentro da Banda (%) |
|---|---|---|---|---|---|---|
| **2021** | 247 | 83,2 | 10,3 | 8,7 | 7,4× | 3% |
| **2022** | 250 | 53,2 | 7,9 | 5,3 | 6,1× | 6% |
| **2023** | 249 | 59,6 | 4,5 | 2,9 | 11,4× | 1% |
| **2024** | 249 | 51,1 | 4,0 | 3,5 | 10,1× | 3% |
| **2025** | 249 | 18,2 | 3,5 | 3,5 | 4,3× | 5% |
| **2026 (até 30/out)** | 208 | 13,1 | 2,5 | 2,2 | 3,6× | 14% |

#### Notas do Orador & Rastreabilidade
- **Notas:** "Antes de falar em causa regulatória, precisávamos garantir que não estávamos medindo um fantasma estatístico. Casamos a janela das 10h às 13h10 da PTAX com os dados de livro da Binance, ajustamos o par pelo dólar real da Coinbase e calculamos o ruído de microestrutura. O prêmio é sistemático, positivo e ordens de grandeza maior que o spread de negociação."
- **Rastreabilidade:** `F-001`, `F-004`, `F-006`, `F-007`, `D-01`, `D-02`, `D-07`, `D-10`, `L-01`, `L-02`, `scripts/p1_02_premium.py`, `scripts/p2_01_noise.py`.

---

<!-- SLIDE 6 -->
## Slide 6 — Resultado 1: Teste Cego de Quebras Estruturais e Banda de Não-Arbitragem

### Sem receber nenhuma data, o algoritmo Bai-Perron crava a quebra em 24/jun/2026 (+100 bps); modelo Band-TAR mostra alargamento de 26× na banda de atrito

#### Layout Visual & Figura
- **Imagem:** `results/figures/P2-02_premium_breaks.png` (Série histórica do prêmio com regimes de médias e intervalos de confiança de 95% calculados por Bai 1997).
- **Legenda (10 segundos):** O algoritmo de quebras estruturais identifica 24/jun/2026 com o intervalo de confiança mais estreito de todo o histórico de 6 anos (18 a 30 de junho), saltando de 9,3 para 109,1 bps (+99,8 bps).

#### Pontos Principais (pt-BR)
- **Detecção Cega de Quebras Estruturais (Bai & Perron 2003, LWZ; `P2-02`, `F-011`):**
  - Sem informar datas regulatórias ao modelo, o algoritmo detectou 5 quebras estruturais ao longo de 6 anos.
  - A 4ª quebra ocorre exatamente em **24 de junho de 2026**, apresentando o menor intervalo de confiança de 95% de toda a série (**18 a 30 de junho de 2026**, semi-largura de apenas 3,1 dias úteis).
  - O prêmio médio salta instantaneamente de **9,3 bps para 109,1 bps (+99,8 bps)**.
  - Em **22 de julho de 2026**, surge a 5ª quebra, marcando a acomodação parcial para **26,8 bps** (platô que ainda permanece **+17,5 bps acima** do nível pré-choque).
- **Dinâmica Não Linear da Banda de Não-Arbitragem (Band-TAR, `P3-07`, `F-021`):**
  - Estimamos um modelo autorregressivo com limiar de banda simétrica (Band-TAR, Obstfeld & Taylor 1997) em cada regime identificado:
    $$\Delta z_t = \beta_{\text{in}} z_{t-1} \mathbf{1}_{\{|z_{t-1}| \le c\}} + \beta_{\text{out}} (z_{t-1} - \text{sign}(z_{t-1})c) \mathbf{1}_{\{|z_{t-1}| > c\}} + \varepsilon_t$$
  - **Regime Pré-Notificação (jul/2025 – jun/2026):** Banda de não-arbitragem de apenas **$c = 1,61\text{ bps}$** (IC 95%: [1,22; 5,13]), com reversão imediata ($\beta_{\text{out}} = -1,03$, meia-vida $t_{1/2} \le 1,0$ dia). Mercado operava em máxima eficiência institucional.
  - **Choque Agudo (24/jun – 21/jul/2026):** A banda de atrito explodiu **26 vezes para $c = 41,95\text{ bps}$** (IC 95%: [9,96; 52,63]), demonstrando a paralisia do mecanismo estabilizador.
  - **Platô de Adaptação (22/jul – 30/out/2026):** A banda recuou para **$c = 9,40\text{ bps}$** (IC 95%: [3,13; 14,41]), ainda **~6 vezes maior** que no período pré-notificação, com meia-vida mais lenta ($1,60$ dias úteis no pós-notificação combinado).
- **Validação contra Baselines:**
  - O modelo Band-TAR reduz o RMSE em **20,3%** frente ao passeio aleatório e em **10,8%** frente ao AR(1) linear no choque agudo de 2026.

#### Notas do Orador & Rastreabilidade
- **Notas:** "Não dissemos ao computador quando houve regulação. O teste de Bai-Perron buscou sozinho no histórico de 1.520 dias onde ocorreu a maior ruptura estrutural. O algoritmo cravou 24 de junho de 2026 com intervalo de 18 a 30 de junho. E o modelo Band-TAR comprova economicamente: a banda de tolerância à arbitragem explodiu de 1,6 para quase 42 basis points."
- **Rastreabilidade:** `F-011`, `F-021`, `L-03`, `L-04`, `scripts/p2_02_breaks.py`, `scripts/p3_07_tar.py`.

---

<!-- SLIDE 7 -->
## Slide 7 — Resultado 2: Estudo de Eventos em Todas as Regras e 200 Datas Placebo

### Testamos todas as 13 normas e marcos cambiais: apenas o ofício reservado do BCB de 23/jun/2026 moveu o prêmio (+93,9 bps, p = 0,0050)

#### Layout Visual & Figura
- **Imagem:** `results/figures/P2-03_placebo_dist.png` (Distribuição empírica das diferenças de 200 datas placebo aleatórias vs a quebra real observada em 23/jun/2026).
- **Legenda (10 segundos):** Nenhuma das 200 datas placebo aleatórias atingiu variação próxima a +93,9 bps (o máximo placebo foi +62,7 bps); marcos públicos no DOU (Res. 519–521 e Res. 561) tiveram impacto nulo.

#### Pontos Principais (pt-BR)
- **Protocolo Padronizado de Estudo de Eventos (`P2-03`, `F-016`):**
  - Janela de **$\pm 20$ dias úteis PTAX** em torno do evento ($t_0$ omitido). Erros-padrão consistentes com heterocedasticidade e autocorrelação (Newey-West HAC com 5 defasagens).
  - Avaliação sistemática de **todas as 13 regras e eventos** catalogados pela equipe (`P1-04`), testando tanto datas de anúncio quanto de vigência.
- **A Singularidade do Ofício Reservado de 23/Jun/2026 (`E-05`):**
  - No dia 23 de junho de 2026, o BCB enviou ofício de supervisão a bancos, corretoras e administradores de fundos vedando arranjos de remessa via fundos para importação de criptoativos (noticiado pelo ConJur em 01/jul).
  - O prêmio saltou de **15,2 bps** (pré-evento) para **109,1 bps** (pós-evento agudo), gerando um impacto de **+93,9 bps** ($EP = 16,2$ bps, $t = 5,80$, $p = 6,4 \times 10^{-9}$).
  - Frente a uma linha de base ingênua de persistência, o modelo de quebra reduziu o RMSE em **58,8%** (de 103,1 para 42,5 bps).
- **O Teste Definitivo dos 200 Placebos Aleatórios:**
  - Amostramos 200 datas de negociação limpas (fora de $\pm 20$ dias úteis de qualquer evento conhecido).
  - A média das variações placebo foi de $-0,55$ bps (desvio-padrão de $18,0$ bps, amplitude de $-57,5$ a $+62,7$ bps).
  - **Zero em 200 placebos** atingiram $+93,9$ bps. P-valor empírico bilateral e unilateral: **$p = 1/201 = 0,0050$ (Percentil 100,0%)**.
- **O Efeito Nulo das 12 Normas Públicas Ordinárias:**
  - O Marco das SPSAVs (Res. 519–521, `E-02`): variação de $-4,3$ bps ($p_{\text{placebo}} = 0,66$).
  - Reforma do eFX proibindo liquidação em cripto (Res. 561, `E-06a`): variação de $-5,3$ bps ($p_{\text{placebo}} = 0,64$).
  - Códigos de Reporte Cambial (Res. 521 Art. 4º, `E-04`): $+7,2$ bps ($p_{\text{placebo}} = 0,58$).
  - Aumento do IOF para 3,5% em Maio/2025 (`E-01`): $+15,4$ bps ($p_{\text{placebo}} = 0,31$, estatisticamente não anômalo frente aos placebos).

| Evento Regulatório | ID | Data Avaliada | Média Pré (bps) | Média Pós (bps) | Variação (bps) | t-stat HAC | p-valor Paramétrico | p-valor 200 Placebos | Status do Efeito |
|---|---|---|---|---|---|---|---|---|---|
| **Ofício Supervisão Cripto/Fundos** | **E-05** | **23/06/2026** | **15,2** | **109,1** | **+93,9** | **5,80** | **$6,4 \times 10^{-9}$** | **0,0050** | **Choque Anômalo** |
| Res. BCB 519–521 (Marco SPSAV) | E-02 | 02/02/2026 | 8,4 | 4,1 | -4,3 | -2,57 | 0,010 | 0,6567 | Efeito Nulo |
| Res. BCB 561 (Reforma eFX) | E-06a | 01/10/2026 | 22,8 | 17,5 | -5,3 | -0,74 | 0,460 | 0,6368 | Efeito Nulo |
| Res. BCB 521 Art. 4º (Códigos Reporte) | E-04 | 04/05/2026 | 4,6 | 11,9 | +7,2 | 2,48 | 0,013 | 0,5771 | Efeito Nulo |
| Proposta IOF Cripto 3,5% (Fazenda) | E-03 | 05/02/2026 | 7,6 | 5,5 | -2,1 | -1,10 | 0,270 | 0,7861 | Efeito Nulo |
| Decreto 12.466 (IOF Câmbio Tradicional) | E-01 | 23/05/2025 | 26,2 | 41,7 | +15,4 | 7,09 | $1,4 \times 10^{-12}$ | 0,3134 | Ruído Normal |

#### Notas do Orador & Rastreabilidade
- **Notas:** "Por que apenas o ofício reservado moveu o prêmio e resoluções inteiras do DOU não mexeram no ponteiro? Porque normas públicas trazem prazos de transição de 6 a 12 meses para os departamentos de compliance. Já o ofício de 23 de junho cortou a liquidação de um dia para o outro: os bancos pararam de fechar câmbio para os fundos de importação imediatamente. O teste com 200 placebos é taxativo: $p = 0,0050$."
- **Rastreabilidade:** `F-016`, `E-01` a `E-07`, `M-01` a `M-04`, `scripts/p2_03_events.py`.

---

<!-- SLIDE 8 -->
## Slide 8 — Resultado 3: Controle Sintético Internacional e Heterogeneidade Cripto

### Controle sintético estima salto causal agudo de +109 bps e platô de +28 bps; salto idêntico no Bitcoin (+93,8 bps) comprova choque cambial geral

#### Layout Visual & Figura
- **Imagem:** `results/figures/P2-04_synthetic_control.png` (Trajetória do Brasil vs Brasil Sintético e distribuição dos gaps de tratamento dos 5 países doadores).
- **Legenda (10 segundos):** O Brasil é o 1º lugar isolado entre todas as 6 moedas analisadas em razão pós/pré RMSPE (9,31 vs 0,78–1,22 nos placebos); o salto idêntico de +93,8 bps no Bitcoin afasta qualquer hipótese restrita ao USDT.

#### Pontos Principais (pt-BR)
- **Desenho de Controle Sintético Internacional (Abadie et al. 2010; `P2-04`, `F-017`):**
  - Construímos o **Brasil Sintético** combinando moedas que não sofreram choques regulatórios no período: **EUR (63,6%), MXN (17,9%), TRY (13,4%), ZAR (4,5%) e COP (0,7%)** (pré-RMSPE de apenas **7,05 bps** em 140 dias úteis comuns).
  - **Efeito Causal Agudo (24/jun a 21/jul/2026):** O gap entre Brasil real e Brasil sintético atingiu **+109,3 bps** (vs +103,3 bps na especificação ingênua de Diferenças em Diferenças - DiD).
  - **Platô de Adaptação (22/jul a 30/set/2026):** O gap estabilizou em **+28,2 bps** (DiD: +31,4 bps).
  - **Inferência por Placebos no Espaço:** O Brasil obteve a **maior razão RMSPE pós/pré entre todas as 6 moedas** (**9,31** vs 0,78 na África do Sul, 0,91 na Colômbia e 1,22 na Turquia). O Brasil lidera com folga ($p = 1/6 = 0,167$, limite teórico inferior da amostra discreta de doadores).
- **Robustez Microestrutural em 3 Corretoras Nacionais (`P2-05`, `F-009`):**
  - O choque de +93 a +95 bps ocorreu de forma síncrona em livros de ordens independentes: **Binance (+93,9 bps)**, **Foxbit (+95,4 bps)** e **Mercado Bitcoin (+92,9 bps)**.
- **Heterogeneidade Cripto: O Choque Transmitiu ao Bitcoin (`P3-02`, `F-018`):**
  - O prêmio do **Bitcoin sobre a PTAX** ($P^{\text{BTC}}_{\text{BRL}} / (P^{\text{BTC}}_{\text{USD}} \times \text{PTAX}) - 1$) saltou exatamente **+93,78 bps** ($t = 5,82$, $p = 0,0050$ contra 200 placebos).
  - O spread entre USDT e BTC permaneceu colado em **0,28 a 0,46 bps**, ancorado pela arbitragem triangular de alta frequência nos livros domésticos.
  - *Conclusão Econômica:* O ofício do BCB não afetou o token USDT ou sua emissora: encareceu a infraestrutura de liquidação em reais de **todos os ativos digitais no Brasil**.
- **Adaptação e Reorganização do Mercado Doméstico (`F-008`, `M-04`):**
  - Em 7 de julho de 2026, a Foxbit firmou parceria estratégica de migração de clientes com a NovaDAX (`M-04`). O volume mensal da Foxbit explodiu **6 vezes** (de ~150 milhões para **1,0 bilhão de USDT/mês** a partir de julho), com o tamanho médio das ordens crescendo 5× (de US$ 1.100 para US$ 6.200), sinalizando a migração institucional para livros locais.

#### Notas do Orador & Rastreabilidade
- **Notas:** "Algum jurado poderia cogitar: 'Não terá sido um choque nos mercados emergentes ou um problema na paridade global do Tether?' O controle sintético responde: em relação a uma cesta de 5 moedas globais, o Brasil descolou em 109 bps. E quando olhamos o Bitcoin no Brasil, o prêmio subiu os mesmos 93,8 bps na vírgula. Trata-se indiscutivelmente de um choque de fronteira cambial no Brasil."
- **Rastreabilidade:** `F-008`, `F-009`, `F-010`, `F-017`, `F-018`, `scripts/p2_04_synth.py`, `scripts/p3_02_btc.py`.

---

<!-- SLIDE 9 -->
## Slide 9 — Quanto Custa na Prática? US$ 100 mil por Regime e Cenários Regulatórios

### Nos regimes calmos o USDT economizava até R$ 20,6 mil por US$ 100 mil; o choque reduziu a vantagem e um IOF de 3,5% anularia a arbitragem

#### Layout Visual & Figura
- **Imagem:** `results/figures/P3-01_route_costs.png` (Decomposição de custos totais: prêmio cambial, spread bancário/corretora, IOF e taxas de rede por rota e cenário).
- **Legenda (10 segundos):** Operações via USDT eram 305 a 375 bps mais baratas que o câmbio bancário tradicional (IOF 3,5%); o choque de 24/jun encareceu a rota em +R$ 5.370 por US$ 100 mil, enquanto a imposição de IOF de 3,5% sobre stablecoins eliminaria quase a totalidade da vantagem.

#### Pontos Principais (pt-BR)
- **Comparação Financeira Padronizada (Transação Institucional de US$ 100.000):**
  - PTAX de referência: R$ 5,3800 (Custo-base: R$ 538.000,00).
  - Parâmetros de Mercado Bancário (BCB Ranking do VET `R-01`): Spread corporativo mediano de 50,0 bps + tarifa SWIFT fixa de US$ 25,00 (2,5 bps).
  - Parâmetros Cripto (Binance / Foxbit / MB, `R-04`, `R-05`, `R-06`): Taxa institucional taker de 6,0 a 10,0 bps + taxa on-chain de 1 a 2 USDT (0,1 bps).
- **Custos Totais por Regime Histórico:**
  - **Câmbio Bancário Disponibilidade (IOF 3,5%, Decreto 12.466/2025):** Custo total de **402,5 bps (R$ 21.654,50)**.
  - **Câmbio Bancário Importação Comercial (IOF 0%):** Custo total de **52,5 bps (R$ 2.824,50)**.
  - **Rota USDT Pré-Notificação (Regime 4):** Custo total de **19,4 bps (R$ 1.043,72)**. Economia líquida de **R$ 20.610,78** frente à disponibilidade bancária e **R$ 1.780,78** mais barato que o câmbio comercial isento de IOF!
  - **Rota USDT no Choque Agudo (24/jun a 21/jul/2026):** Custo total saltou para **119,2 bps (R$ 6.412,96)** — encarecimento imediato de **+R$ 5.369,24 (+100 bps)**, invertendo a vantagem frente ao câmbio comercial 0% (-R$ 3.588,46), mas ainda mantendo R$ 15.241,54 de margem sobre a disponibilidade.
  - **Rota USDT no Platô de Adaptação (jul a out/2026):** Estabilizou em **36,9 bps (R$ 1.985,22)** no varejo e **33,0 bps (R$ 1.775,40)** em mesas VIP do Mercado Bitcoin.
- **Simulação Quantitativa de Cenários Regulatórios Futuros:**
  - **Cenário S1: Aprovação da Proposta de IOF de 3,5% sobre Stablecoins (`E-03`):**
    - Custo total sobe para **386,9 bps (R$ 20.815,22)**. A economia corporativa é destruída em 95,7% (caindo de R$ 19,7 mil para apenas R$ 839,28), fechando economicamente o canal cripto.
  - **Cenário S2: Retenção Cautelar de 24 Horas para Operações $\ge$ US$ 10k (Res. BCB 584/2026, `E-06b`):**
    - Se com proteção cambial (*hedge* via futuros B3): adiciona 10,0 bps de custo de rolagem (total 46,9 bps, R$ 2.523,22), preservando competitividade.
    - Se sem proteção cambial (risco cambial de 1 dia a 95% de confiança): adiciona **136,8 bps de risco de volatilidade**, elevando o custo total para **173,7 bps (R$ 9.345,06)** e superando o câmbio financeiro com IOF de 1,1%.

| Rota / Regime / Cenário | Prêmio (bps) | Spread (bps) | Tributo / IOF (bps) | Rede / SWIFT (bps) | Custo Total (bps) | Custo Total (R$) | Economia vs Banco Disp. (R$) |
|---|---|---|---|---|---|---|---|
| **Câmbio Bancário Disponibilidade (IOF 3,5%)** | 0,0 | 50,0 | 350,0 | 2,5 | 402,5 | R$ 21.654,50 | R$ 0,00 |
| **Câmbio Bancário Investimento (IOF 1,1%)** | 0,0 | 50,0 | 110,0 | 2,5 | 162,5 | R$ 8.742,50 | R$ 12.912,00 |
| **Câmbio Bancário Importação (IOF 0%)** | 0,0 | 50,0 | 0,0 | 2,5 | 52,5 | R$ 2.824,50 | R$ 18.830,00 |
| **USDT Pré-Notificação (Regime 4)** | 9,3 | 10,0 | 0,0 | 0,1 | **19,4** | **R$ 1.043,72** | **R$ 20.610,78** |
| **USDT Choque Agudo 24/jun (Regime 5)** | 109,1 | 10,0 | 0,0 | 0,1 | **119,2** | **R$ 6.412,96** | **R$ 15.241,54** |
| **USDT Platô Pós-Adaptação (Regime 6)** | 26,8 | 10,0 | 0,0 | 0,1 | **36,9** | **R$ 1.985,22** | **R$ 19.669,28** |
| **Cenário S1: IOF Cripto 3,5% (`E-03`)** | 26,8 | 10,0 | 350,0 | 0,1 | **386,9** | **R$ 20.815,22** | **R$ 839,28** |
| **Cenário S2: Retenção 24h sem Hedge (`E-06b`)** | 26,8 | 10,0 | 136,8 (risco) | 0,1 | **173,7** | **R$ 9.345,06** | **R$ 12.309,44** |

#### Notas do Orador & Rastreabilidade
- **Notas:** "Este é o slide que os gestores de tesouraria do comitê avaliador vão guardar. Nos regimes tranquilos, uma empresa que importa insumos ou remete recursos ao exterior economizava R$ 20 mil a cada 100 mil dólares usando USDT. O ofício do BCB de 23 de junho custou R$ 5.370 a mais por operação. E se o Ministério da Fazenda aprovar o IOF de 3,5% sobre stablecoins, a rota morre economicamente."
- **Rastreabilidade:** `F-015`, `R-01` a `R-07`, `scripts/p3_01_costs.py`.

---

<!-- SLIDE 10 -->
## Slide 10 — O Mesmo Mecanismo em Dólares: O Fim de Semana do SVB e 11 Depegs (2019–2026)

### A paridade em dólares obedece à mesma regra: o USDC caiu para US$ 0,805 quando as portas bancárias fecharam e voltou em 45 min com a garantia

#### Layout Visual & Figura
- **Imagem:** `results/figures/P3-04_svb_weekend.png` (Trajetória horária do USDC/USD na Bitstamp durante o SVB, com marcas de fechamento bancário e anúncio de garantia pelo Fed/FDIC).
- **Legenda (10 segundos):** No fim de semana, com o Fedwire fechado e incerteza sobre os depósitos da Circle no SVB, o USDC negociou a US$ 0,805; bastou o comunicado conjunto das 22h15 de domingo restabelecer a credibilidade do resgate para a arbitragem levar o preço a US$ 0,989 antes da abertura dos bancos.

#### Pontos Principais (pt-BR)
- **O Fim de Semana do Silicon Valley Bank (10 a 13 de Março de 2023; `P1-07`, `P3-04`, `F-019`):**
  - A Circle mantinha US$ 3,3 bilhões de reservas de caixa do USDC no SVB (8,2% do total). Com a intervenção da FDIC na sexta-feira à tarde e o encerramento do Fedwire no fim de semana, as portas de resgate bancário primário foram fisicamente trancadas.
  - Sem piso de arbitragem institucional, o pânico no mercado secundário empurrou o USDC para uma cotação mínima intra-horária de **US$ 0,805** (fechamento horário de **US$ 0,863**) no sábado, 11/mar às 07:00 UTC.
- **A Força da Arbitragem Baseada em Expectativa de Resgate:**
  - No domingo, 12 de março às **22:15 UTC (`D-13`)**, Federal Reserve, Tesouro dos EUA e FDIC publicaram comunicado conjunto garantindo integralmente todos os depósitos do SVB.
  - Em apenas **45 minutos** (às 23:00 UTC), o mercado secundário recomprou o USDC de US$ 0,968 para **US$ 0,989**, alcançando US$ 0,991 na manhã de segunda-feira antes da abertura das agências bancárias. A arbitragem operou pela *expectativa crível de resgate a US$ 1,00*.
- **Triagem Sistemática de Depegs em Dólares (Binance 2019–2026; `F-013`, `F-019`):**
  - Identificamos exatamente **11 eventos confirmados de descolamento negativo** em relação ao dólar.
  - Seguindo o rigor pré-comprometido de pesquisa (`prompt.md` §5), por haver menos de 12 eventos independentes ($11 < 12$), omitimos curvas de sobrevivência de Kaplan-Meier e adotamos uma taxonomia estruturada em 4 categorias econômicas:
    1. **Portas Bancárias Fechadas em Moedas Solventes (USDC, USDP durante SVB):** 100% de recuperação rápida (duração de 51 a 65 horas) assim que a credibilidade do resgate é restabelecida.
    2. **Fricções Operacionais de Liquidez (TUSD, FDUSD):** 100% de recuperação, porém com duração mediana de 492 horas e oscilação contida ($0,954 a $0,992).
    3. **Insolvência Algorítmica Estrutural (UST Terra):** Colapso terminal com **0% de recuperação** (convergência para US$ 0,00 e deslistagem), provando que garantias fiduciárias externas são condição necessária para a sustentação do peg.

| Categoria Econômica | Eventos (N) | Ativos | Taxa de Recuperação | Duração Mediana | Mínima Histórica | Mecanismo Central |
|---|---|---|---|---|---|---|
| **1. Porta de Resgate Fechada (SVB)** | 2 | USDC, USDP | **100%** | **58h (51–65h)** | **US$ 0,863 – 0,974** | Arbitragem travada pelo fim de semana; recuperação instantânea pós-garantia |
| **2. Fricções de Liquidez e Operação** | 7 | TUSD, FDUSD, UST-early | **100%** | 492h (21–2.719h) | US$ 0,954 – 0,992 | Solvência intacta; lentidão operacional de queima/emissão pelo emissor |
| **3. Insolvência Algorítmica Terminal** | 1 | UST (maio/2022) | **0%** | N/A (Colapso) | US$ 0,000 – 0,245 | Espiral da morte por ausência de reservas externas reais segregadas |
| **4. Deriva Pré-Deslistagem em Exchange** | 2 | USDP (Binance 2026) | 50% | 60h | US$ 0,988 – 0,994 | Drenagem de liquidez secundária por deslistagem programada em bolsa |

#### Notas do Orador & Rastreabilidade
- **Notas:** "Mostramos aos jurados que o fenômeno brasileiro não é uma jabuticaba. A mesma teoria dos limites à arbitragem se aplica ao dólar nos Estados Unidos. Quando a porta do banco fechou no fim de semana do SVB, o USDC despencou a 80 centavos de dólar. Bastou o Fed garantir que a porta abriria na segunda-feira para o mercado arbitrar e repor o preço a 99 centavos na noite de domingo. Solvência de reservas garante a sobrevivência no longo prazo; portas abertas de resgate garantem a paridade no curto prazo."
- **Rastreabilidade:** `F-013`, `F-019`, `D-08`, `D-13`, `scripts/p3_04_depeg_chapter.py`.

---

<!-- SLIDE 11 -->
## Slide 11 — Solução Prática: O Monitor do Dólar Digital em Tempo Real

### Entregamos uma ferramenta operacional em código linear: o alarme CUSUM dispara no próprio dia 24/jun/2026 com zero atraso

#### Layout Visual & Figura
- **Imagem:** `results/figures/P3-03_monitor.png` (Painel superior: série do prêmio com bandas e alarmes de quebra; painel inferior: estatística de soma acumulada CUSUM vs limiar crítico).
- **Legenda (10 segundos):** Calibrado exclusivamente com dados históricos de 2020 a 2025, o monitor detectou o salto estrutural no próprio dia 24 de junho de 2026 (atraso zero), identificou a acomodação em 11 dias úteis e gerou metade dos falsos alarmes de uma regra ingênua.

#### Pontos Principais (pt-BR)
- **Uma Ferramenta Operacional para o Mercado e o Regulador (`P3-03`, `F-014`):**
  - Implementada em um único script autônomo e linear (`scripts/p3_03_monitor.py`), concebida para execução diária por tesourarias e órgãos de supervisão.
  - **Três Camadas Integradas:**
    1. *Prêmio Padronizado:* Casado na janela PTAX e purgado de desvios do par global USDT/USD.
    2. *Banda Dinâmica de Ruído:* Atualização móvel do piso microestrutural Corwin-Schultz (tolerância estatística a atritos de livro).
    3. *Detector Sequencial CUSUM:* Identificação de quebras em regime persistente, parametrizado sem espiar o período de teste.
- **Disciplina Estrita Fora da Amostra (*No Look-Ahead*):**
  - Calibração de parâmetros executada exclusivamente na janela de treino (**13/10/2020 a 31/12/2025**), fixando um orçamento conservador de tolerância de no máximo 2 alarmes por ano ($h = 24,5$).
  - Período de teste fora da amostra: **01/01/2026 a 30/10/2026**.
- **Desempenho no Teste de 2026:**
  - **Disparo no Próprio Dia do Choque:** O alarme tocou em **24 de junho de 2026** (**atraso = 0 dias úteis**). A soma acumulada já registrava pressão desde o final de maio (22,6 vs limiar 24,5 em 23/jun) e estourou para 62 no dia 24.
  - **Captura da Acomodação Estrutural:** Identificou a consolidação do platô inferior em 11 dias úteis após 22 de julho (em 06 de agosto).
  - **Eficiência e Controle de Falsos Alarmes:** Registrou apenas 2 outros alarmes ao longo de 10 meses de 2026 (taxa anualizada de 2,4), **cortando pela metade** os 4 falsos alarmes disparados por uma regra convencional de bandas fixas.

| Detector de Quebras | Parâmetro Calibrado (Treino 2020–2025) | Alarmes no Treino | Detecção do Choque (24/jun) | Detecção da Acomodação (22/jul) | Outros Alarmes no Teste (2026) |
|---|---|---|---|---|---|
| **Monitor CUSUM (Nossa Solução)** | **$h = 24,5$** | **9 (1,8 / ano)** | **24/jun (0 dias úteis)** | **06/ago (11 dias úteis)** | **2 (2,4 / ano)** |
| Regra Ingênua (Média Móvel vs Banda) | $c = 7,25$ | 10 (2,0 / ano) | 24/jun (0 dias úteis) | 07/ago (12 dias úteis) | 4 (4,8 / ano) |

#### Notas do Orador & Rastreabilidade
- **Notas:** "Não entregamos um dashboard cosmético que perde utilidade após a apresentação. Desenvolvemos um código linear em Python puro que roda em 5 segundos, sem look-ahead. Se uma tesouraria estivesse rodando este monitor em 2026, teria recebido o alerta vermelho exatamente no dia 24 de junho e pausado as compras em USDT, poupando mais de R$ 5 mil por lote de US$ 100 mil."
- **Rastreabilidade:** `F-014`, `scripts/p3_03_monitor.py`.

---

<!-- SLIDE 12 -->
## Slide 12 — Implicações Econômicas, Regulatórias e Limitações Honestadas

### A supervisão prudencial tem impacto de preços imediato (+100 bps); mercado adapta-se em 20 dias com custo permanente de +17 a +28 bps

#### Layout Visual & Tabela-Síntese
- **Tabela Comparativa de Canais e Custos:**
  - *Intervenção Prudencial/Supervisão (`E-05`):* Efeito agudo de +94 a +109 bps; platô permanente de +17 a +28 bps (+R$ 915 a +R$ 1.500 por US$ 100k); tempo de adaptação de ~20 dias úteis.
  - *Tributação Cambial Direta (`E-03`):* Efeito permanente estático de +350 bps (+R$ 18.830 por US$ 100k); inviabiliza arbitragem corporativa.
  - *Fricção Operacional de Retenção 24h (`E-06b`):* Custo financeiro de +10 bps (com hedge) a +137 bps (sem hedge).
- **Legenda (10 segundos):** O prêmio do dólar digital funciona como um termômetro em tempo real do custo da mobilidade de capital e da regulação cambial no Brasil.

#### Pontos Principais (pt-BR)
- **1. O Preço-Sombra da Supervisão vs Regulação Formal:**
  - Atos prudenciais reservados direcionados a intermediários bancários e fundos fecham canais de arbitragem de forma muito mais drástica e imediata (+100 bps no D+1) do que resoluções normativas publicadas no Diário Oficial, cujos prazos de adaptação diluem choques de preços.
- **2. Elasticidade e Capacidade de Adaptação Doméstica:**
  - O choque agudo durou exatamente cerca de 20 dias úteis. O mercado cripto brasileiro demonstrou capacidade rápida de adaptação endógena, reorganizando fluxos institucionais via livros de ordens locais (a exemplo da migração Foxbit-NovaDAX, `M-04`, `F-008`).
  - No entanto, a adaptação não é gratuita: deixou um **resíduo estrutural permanente de +17 a +28 bps**, representando a taxa de conveniência fiduciária pelo canal regulatório mais restrito.
- **3. Implicações para o Banco Central e o Projeto Drex:**
  - O spread USDT/BRL opera como um indicador não oficial de alta frequência do custo de mobilidade e controle de capitais no Brasil.
  - Para a arquitetura do Drex e stablecoins reguladas de liquidação transfronteiriça, a existência de bandas de fricção de 10 a 30 bps indica que pontes de liquidez digital exigem mecanismos explícitos de arbitragem institucional sob pena de descolamento estrutural de preço.
- **4. Limitações Metodológicas Honestadas (`prompt.md` §5):**
  - *Natureza do Ofício de 23/jun/2026 (`E-05`):* Comunicação de supervisão de caráter reservado, documentada por fontes jurídicas secundárias conceituadas (ConJur) e confirmada empiricamente em 3 corretoras, mas sem texto publicado no DOU.
  - *Amostra Finita de Doadores Internacionais:* O controle sintético utiliza 5 doadores soberanos líquidos, estabelecendo um limite teórico discreto de permutação ($p \ge 1/6 = 0,167$). O rigor causal é respaldado complementarmente pela distribuição empírica dos 200 placebos temporais no Brasil ($p = 0,0050$).

#### Notas do Orador & Rastreabilidade
- **Notas:** "Respondendo à pergunta que dá título à pesquisa: Quanto custa fechar a porta? Fechar a porta fiduciária de fundos custou R$ 5.370 por US$ 100 mil no impacto agudo e deixou um custo permanente de cerca de R$ 1.000 a R$ 1.500 na rota digital. Para o regulador, fica a lição: a arbitragem não desaparece, ela apenas busca a próxima porta mais cara. Muito obrigado."
- **Rastreabilidade:** `F-015`, `F-016`, `F-017`, `F-021`, `E-05`, `E-03`, `E-06b`, `docs/02-dolar-cripto.md` §10.

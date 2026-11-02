# Quanto Custa Fechar a Porta?
## O Prêmio do Dólar Digital no Brasil e os Limites à Arbitragem

**Apresentação de Resultados — 7º Datathon de Moedas Digitais FGV EESP (Novembro de 2026)**  
**Equipe Out of Sample:** CS 1 (Renzo), CS 2 (Nattan), CS 3 (Jonathan), Economista (Felipe)  
**Instituições Organizadoras:** FGV EESP, Centro de Estudos em Finanças Digitais FGV, com apoio de FGV/Ripple (UBRI) e USP-UBRI  

---

### Sumário da Apresentação e Mapeamento com o Protótipo (`notebooks/p5_07_story.ipynb`)
1. **Slide 1 (Seção 1):** Quanto custa fechar a porta? — Tese, pergunta de pesquisa e o experimento natural
2. **Slide 2 (Seção 2):** O que esperávamos — Hipóteses pré-comprometidas ($H_0$ a $H_3$) e critérios de falsificação
3. **Slide 3 (Seção 3):** Dados e medida — Pareamento na janela PTAX, piso de ruído e quebras estruturais cegas
4. **Slide 4 (Seção 4):** O salto: mesmo tamanho em três corretoras — Binance, Foxbit e Mercado Bitcoin e descarte de confundidores
5. **Slide 5 (Seção 5):** A porta que fechou — O ofício de supervisão de 23 de junho de 2026 e suas três fontes
6. **Slide 6 (Seção 6):** Só uma regra mexeu no preço — Estudo de eventos nas 13 regras vs todas as 1.073 datas limpas ($p = 0,0009$)
7. **Slide 7 (Seção 7):** Outros países não se mexeram — Controle sintético internacional, DiD e arbitragem triangular no Bitcoin
8. **Slide 8 (Seção 8):** Um pico de um mês — Robustez em 22 variantes agudas (+74 a +128 bps) e nível pós-pico não distinguível de deriva ($p = 0,24$)
9. **Slide 9 (Seção 9):** Onde a porta está fechada, o prêmio é grande — Evidência descritiva internacional (ARS, UAH vs mercados abertos)
10. **Slide 10 (Seção 10):** Quanto custou: R$ 5 mil por US$ 100 mil — Custo do ofício e comparação neutra de fricções por canal (Opções C e A)
11. **Slide 11 (Seção 11):** Do lado do dólar: quando o resgate fecha — O fim de semana do SVB e a tabela de 11 casos de depeg com fontes abertas
12. **Slide 12 (Seção 12):** Monitor do Dólar Digital — Alarme CUSUM sem *look-ahead* calibrado em 2020–2025 e testado em 2026
13. **Slide 13 (Seção 13):** Lições de 2025 — Linha de base ingênua obrigatória e decomposição de subsídios em tokens (53,6% de COMP)
14. **Slide 14 (Seções 14–15):** O que os testes mostraram e limitações — Placar das hipóteses, implicações para supervisão/Drex e limites

---

<!-- SLIDE 1 -->
## Slide 1 — Quanto custa fechar a porta?

### Quando a supervisão fecha um canal de arbitragem entre o mercado cripto e o câmbio oficial, quanto a mais os brasileiros pagam por um dólar digital?

#### Layout Visual & Estrutura
- **Posicionamento:** Capa executiva combinada à tese econômica central e à pergunta de pesquisa (Requisito `prompt.md` §8: uma pergunta clara logo na abertura, respondível com a evidência mostrada).
- **Legenda (10 segundos):** Um ativo só permanece na paridade enquanto algum canal permite comprar barato de um lado e vender caro do outro; em 24/jun/2026, após notícia de ofício de supervisão do BCB sobre fundos, o prêmio do USDT sobre a PTAX saltou +93,9 bps (+R$ 5.052 por US$ 100 mil) durante um mês.

#### Pontos Principais (pt-BR)
- **Tese Econômica (Limites à Arbitragem — Shleifer & Vishny 1997; Makarov & Schoar 2020):**
  - No Brasil, o dólar digital (USDT comprado com reais) e o dólar oficial (PTAX) são mantidos próximos pela arbitragem entre corretoras cripto e o mercado formal de câmbio:
    $$\text{USDT/BRL}_t = \text{PTAX}_t \times \text{USDT/USD}_t \times (1 + \pi_t)$$
  - Quando uma regra fecha ou encarece a porta fiduciária mais barata de arbitragem, o prêmio $\pi_t$ descola da paridade até o custo do próximo canal disponível (Obstfeld & Taylor 1997).
- **A Pergunta de Pesquisa:**
  - *Quanto a mais os brasileiros pagaram por um dólar digital quando uma intervenção fechou uma dessas portas, e quais regras realmente moveram o preço?*
- **O Experimento Natural (23 de junho de 2026):**
  - Em 23/jun/2026, o Banco Central comunicou a bancos, corretoras de câmbio e administradores de fundos que operações de câmbio de fundos para importar ativos virtuais não tinham respaldo nas normas e determinou sua interrupção (`E-05`). Foi um ato de supervisão com data definida, não uma resolução com longo prazo de transição.
- **Relevância Prática:**
  - Afeta tesourarias corporativas (custo de liquidação transfronteiriça), a supervisão cambial do BCB (perímetro das SPSAVs — Res. 519–521 e eFX — Res. 561) e o desenho de pontes de liquidez no ecossistema **Drex**.

#### Notas do Orador & Rastreabilidade
- **Notas:** "Senhores jurados, nossa pergunta é direta: quanto custa fechar a porta da arbitragem cambial no Brasil? Testamos seis anos de dados pareados na janela da PTAX e 13 eventos regulatórios. Mostraremos que resoluções formais com prazos longos de adaptação não moveram o prêmio, mas o fechamento operacional de um canal em 23 de junho de 2026 gerou um salto imediato de 94 pontos-base — cerca de R$ 5 mil para cada US$ 100 mil — durante um mês."
- **Rastreabilidade:** Seção 1 de `notebooks/p5_07_story.ipynb`; `F-001`, `F-002`, `F-015`, `F-016`, `E-05`, `L-05`, `L-06`, `L-07`.

---

<!-- SLIDE 2 -->
## Slide 2 — O que esperávamos: Hipóteses Pré-Comprometidas

### Fixamos quatro hipóteses e seus critérios de falsificação antes dos testes confirmatórios

#### Layout Visual & Tabela de Desenho
- **Tabela de Hipóteses:** As quatro hipóteses ($H_1, H_2, H_3, H_0$) registradas no plano de pesquisa (`docs/02-dolar-cripto.md` §5) antes da execução dos testes da Fase 2.
- **Legenda (10 segundos):** Toda afirmação empírica deste trabalho responde a um teste definido antes de rodar os modelos, com linha de base explícita e critério claro do que falsificaria a hipótese.

#### Pontos Principais (pt-BR)

| Hipótese | Enunciado Econômico | O que Sustentaria a Hipótese | O que Falsificaria a Hipótese |
|---|---|---|---|
| **$H_1$ (Canal Fechado)** | Fechar o canal institucional (23/jun/2026) elevou o prêmio do USDT sobre a PTAX | Salto positivo na data, maior que em datas ordinárias (placebos) e ausente em moedas comparáveis | Variação compatível com datas placebo ($p > 0,10$) ou movimento paralelo nas moedas doadoras |
| **$H_2$ (Canal Marginal)** | Apenas regras que fecham ou taxam o canal *mais barato* em uso movem o prêmio | Outras regras datadas (licenciamento SPSAV, códigos de reporte, eFX) não apresentam salto fora do ruído | Saltos anômalos também em normas de licenciamento ou reporte com janela de transição |
| **$H_3$ (Repasse Parcial do IOF)** | O aumento do IOF sobre o câmbio oficial em maio/2025 (1,1% → 3,5%) moveu o prêmio menos que o imposto | Variação pequena ou indistinguível da deriva ordinária em maio/2025 | Salto da ordem de +240 bps (repasse integral da alíquota tributária ao prêmio cripto) |
| **$H_0$ (Hipótese Nula / Confundidores)** | O salto de 24/jun reflete apenas o câmbio do real, o preço global do USDT em dólar ou falha de uma corretora | O salto desaparece em outras corretoras brasileiras ou após controlar por PTAX e USDT/USD | Salto idêntico em três corretoras independentes com PTAX e USDT/USD estáveis |

- **Compromisso com Padrões de Pesquisa (`prompt.md` §5):**
  - Especificações de quebras estruturais (`P2-02`) e do monitor em tempo real (`P3-03`) registradas em commits no Git antes da execução; estimativa oficial congelada em `results/agentic/team_estimate.json` (`80fc866`).

#### Notas do Orador & Rastreabilidade
- **Notas:** "Para evitar qualquer caça a resultados estatísticos, registramos nossas hipóteses e regras de decisão antes de rodar os testes confirmatórios. Se o salto de 24 de junho aparecesse apenas na Binance, ou se moedas emergentes tivessem se movido juntas, nossa hipótese estaria refutada."
- **Rastreabilidade:** Seção 2 de `notebooks/p5_07_story.ipynb`; `docs/02-dolar-cripto.md` §5; `tasks/P2-02-blind-break-test.md`; `tasks/P2-06-freeze-team-estimate.md`.

---

<!-- SLIDE 3 -->
## Slide 3 — Dados e Medida: Seis Anos de Histórico e Quebras Cegas

### O prêmio supera o piso de ruído em 4× a 11×; sem receber datas, o teste de Bai-Perron encontra 24/jun/2026 (+100 bps)

#### Layout Visual & Figura Principal
- **Imagem:** `results/figures/P2-02_premium_breaks.png` (Série diária do prêmio USDT/BRL 2020–2026 com banda de ruído microestrutural, médias dos regimes de Bai-Perron e intervalos de confiança de 95% de Bai 1997).
- **Legenda (10 segundos):** O prêmio caiu de ~91 bps (2020–21) para ~9 bps (2025–jun/2026) conforme o mercado amadureceu; em 24/jun/2026, um teste cego encontra a ruptura mais aguda em seis anos (+99,8 bps, IC 95%: 18 a 30 de junho).

#### Pontos Principais (pt-BR)
- **Construção da Série Pareada no Tempo (`P1-02`, `F-004`, `F-006`):**
  - **1.520 dias úteis PTAX** (13/out/2020 a 30/out/2026):
    $$\text{Prêmio}_t (\text{bps}) = \left( \frac{\text{USDT/BRL}_t}{\text{PTAX}_t \times \text{USDT/USD}_t} - 1 \right) \times 10.000$$
  - `USDT/BRL` na Binance é pareado exatamente nas horas das 4 consultas da PTAX (10h00–13h10 BRT / 13h00–16h10 UTC) e dividido pela cotação do próprio USDT em dólares (`1/USDCUSDT`, preenchido na janela set/2022–mar/2023 por `1/BUSDUSDT` e validado via Coinbase `USDT/USD`, que concorda em ~1 bp).
- **Piso de Ruído Microestrutural (`P2-01`, `F-007`):**
  - O spread de compra e venda estimado por Corwin & Schultz (2012) e Abdi & Ranaldo (2017) é de **2 a 10 bps** (caindo para ~2,5 bps após o corte de 10× no tick size da Binance em 27/jun/2025, `M-03`). O prêmio mediano anual é **4 a 11 vezes maior** que o ruído em todos os anos.
- **Teste Cego de Quebras Estruturais (Bai & Perron 2003, critério LWZ; `P2-02`, `F-011`):**
  - Sem receber nenhuma data regulatória, o algoritmo encontra 5 quebras. A **4ª quebra ocorre em 24/jun/2026** com o intervalo de confiança mais estreito da série (**18 a 30/jun**, semi-largura de 3,1 dias úteis), saltando de **9,3 para 109,1 bps (+99,8 bps)**, seguida por recuo parcial a partir de **22/jul/2026** (para 26,8 bps).
  - No modelo de limiar **Band-TAR** (`P3-07`, `F-021`), a banda de não-arbitragem era de apenas **$c = 1,61\text{ bps}$** no regime pré-ofício (dentro do ruído de livro) e abriu **26 vezes para $c = 41,95\text{ bps}$** durante o pico agudo (reduzindo o RMSE em 20,3% vs passeio aleatório e 10,8% vs AR(1) linear).

| Quebra (LWZ) | Data Estimada | IC 95% (Bai 1997) | Média Antes → Depois (bps) | Evento na Janela de $\pm 5$ Dias Úteis (`P1-04`) |
|---|---|---|---|---|
| **1** | 26/07/2021 | 22/jun – 27/ago/2021 | 91,3 → 54,5 (-36,8) | Coincide com `M-01`: limite global de alavancagem 20× na Binance (0d) |
| **2** | 20/08/2024 | 24/abr – 16/dez/2024 | 54,5 → 34,9 (-19,6) | Coincide com `M-02`: acordo CVM–Binance de R$ 9,6 mi em 13/08/2024 (-5d) |
| **3** | 08/07/2025 | 29/abr – 12/set/2025 | 34,9 → 9,3 (-25,6) | Coincide com `E-01b`: liminar STF no IOF em 04/07 (-2d; corte de tick `M-03` a -7d no IC) |
| **4** | **24/06/2026** | **18/jun – 30/jun/2026** | **9,3 → 109,1 (+99,8)** | **Coincide com `E-05`: ofício de supervisão do BCB em 23/06/2026 (-1d)** |
| **5** | 22/07/2026 | 15/jul – 29/jul/2026 | 109,1 → 26,8 (-82,4) | **Sem evento em $\pm 5$d (*unexplained*)** — recuo parcial do pico de junho |

#### Notas do Orador & Rastreabilidade
- **Notas:** "O gráfico principal conta nossa história em dez segundos. Durante cinco anos, o prêmio do dólar digital caiu de 91 para 9 pontos-base à medida que o mercado ganhou profundidade. Quando rodamos o algoritmo de Bai-Perron às cegas, sem fornecer nenhuma data, ele aponta 24 de junho de 2026 como a ruptura mais aguda de toda a série."
- **Rastreabilidade:** Seção 3 de `notebooks/p5_07_story.ipynb`; `F-001`, `F-004`, `F-006`, `F-007`, `F-011`, `F-021`, `D-01`, `D-02`, `D-07`, `L-01`..`L-04`, `scripts/p1_02_premium.py`, `scripts/p2_01_noise.py`, `scripts/p2_02_breaks.py`, `scripts/p3_07_tar.py`.

---

<!-- SLIDE 4 -->
## Slide 4 — O Salto: Mesmo Tamanho em Três Corretoras

### O prêmio subiu +93 a +95 bps simultaneamente na Binance, Foxbit e Mercado Bitcoin; não foi o real nem o USDT

#### Layout Visual & Figura
- **Imagem:** `results/figures/P2-05_hourly_22_26_jun.png` (Série horária do prêmio USDT/BRL de 22 a 26 de junho de 2026 na Binance, Foxbit e Mercado Bitcoin, com janelas PTAX sombreadas).
- **Legenda (10 segundos):** Três livros de ordens independentes no Brasil registraram exatamente o mesmo salto a partir da tarde de 23 de junho e na abertura de 24 de junho (+93,3 a +94,9 bps na média de 20 dias), refutando $H_0$.

#### Pontos Principais (pt-BR)
- **Consistência em Três Livros de Ordens Independentes (`P1-03`, `P2-05`, `F-009`):**
  - Comparando os 20 dias úteis PTAX antes (25/mai a 22/jun/2026) e os 20 dias úteis depois (24/jun a 21/jul/2026):
    - **Binance:** de 15,2 para 109,1 bps (**+93,9 bps**; pico de 155,4 bps em 24/jun e 184,4 bps em 25/jun).
    - **Foxbit (corretora nacional):** de 14,7 para 108,0 bps (**+93,3 bps**).
    - **Mercado Bitcoin (corretora nacional):** de 10,7 para 105,6 bps (**+94,9 bps**).
- **Explicações Alternativas Descartadas ($H_0$ Rejeitada, `F-009`):**
  1. **Não foi um choque no próprio Real (PTAX):** Em 24/jun a PTAX variou $+0,68\%$, uma oscilação diária comum; em dias de alta semelhante do dólar, o prêmio historicamente recua levemente em vez de subir.
  2. **Não foi o preço global do USDT em dólares:** A cotação `USDT/USD` na Coinbase e na Bitstamp moveu-se menos de **1 ponto-base** naqueles dias.
  3. **Não foi pane ou restrição específica da Binance:** Nenhuma suspensão de Pix ou manutenção ocorreu em junho de 2026 (ao contrário de jun/2022, `E-07`), e duas corretoras locais independentes subiram juntas.
- **Cronologia Intradiária:**
  - Hora a hora, a subida começa na tarde de **23 de junho**, com um segundo degrau na abertura de **24 de junho** — exatamente quando uma das fontes relata que a decisão do BCB "se tornou pública no dia seguinte" (`E-05`).

#### Notas do Orador & Rastreabilidade
- **Notas:** "Poderia esse salto ser um problema técnico da Binance, uma desvalorização do real ou uma crise do próprio Tether lá fora? Testamos as três hipóteses nulas. O Tether em dólar não mexeu nem 1 ponto-base, o real teve um dia comum, e duas corretoras brasileiras independentes — Foxbit e Mercado Bitcoin — subiram os mesmos 93 a 95 pontos-base."
- **Rastreabilidade:** Seção 4 de `notebooks/p5_07_story.ipynb`; `F-009`, `D-01`, `D-04`, `D-07`, `scripts/p1_03_second_venue.py`, `scripts/p2_05_checks.py`, `results/tables/P2-05_venues_daily.csv`.

---

<!-- SLIDE 5 -->
## Slide 5 — A Porta que Fechou: O que Sabemos sobre o Ofício de 23 de Junho

### Duas fontes independentes descrevem o ofício de 23/jun e a resposta do BCB via LAI confirma a posição da autarquia

#### Layout Visual & Tabela de Fontes
- **Tabela Documental:** As três fontes abertas e citadas literalmente em `docs/sources.md` (`E-05`).
- **Legenda (10 segundos):** Temos dois relatos independentes do mercado jurídico e cambial sobre a notificação de 23/jun/2026 e a posição oficial do próprio BCB em resposta à Lei de Acesso à Informação; como o ofício é reservado, dizemos que o salto *coincide com* a medida.

#### Pontos Principais (pt-BR)

| Fonte Aberta (`docs/sources.md` `E-05`) | O que a Fonte Relata | Citação Verbatim Extraída da Página Aberta | Natureza e Peso da Evidência |
|---|---|---|---|
| **1. Isac Costa, *ConJur*, 01/jul/2026** | Notificação da supervisão do BCB em 23/jun/2026 a bancos, corretoras, empresas cripto e administradores de fundos vedando remessas via fundos para importar criptoativos (relata salto do spread de 0,1% para 0,7%) | *"o cerco do Banco Central às stablecoins"* (coluna de opinião jurídica) | Relato secundário por professor e ex-analista da CVM |
| **2. Sérgio Brotto (CEO, Dascam Corretora de Câmbio), *Cointelegraph Brasil*, 06/jul/2026** | Confirma a notificação do BCB apontando ilegalidade das operações de câmbio para importação de ativos virtuais e exigindo interrupção imediata | *"apontou a 'ilegalidade das operações de câmbio para a finalidade de importação de ativos virtuais'"* e *"A decisão se tornou pública no dia seguinte"* | Relato independente por executivo de corretora de câmbio |
| **3. *Webitcoin*, 30/jul/2026 (Resposta do BCB a pedido de LAI do Instituto Live Mercado)** | Resposta institucional do Banco Central confirmando o entendimento normativo da autarquia sobre fundos e criptoativos | *"operações cambiais realizadas por fundos para importar ativos virtuais não possuem respaldo nas normas atualmente em vigor"* | Posição oficial do próprio BCB em resposta à LAI (sem data do ofício) |

- **Postura Metodológica Honesta (`prompt.md` §5 e §6):**
  - Contamos com **dois relatos secundários independentes** que datam a comunicação em 23/jun/2026 (com repercussão pública em 24/jun) e com a **posição oficial do BCB em suas próprias palavras** via LAI.
  - Como se trata de ofício de supervisão confidencial (não publicado no Diário Oficial da União), não vimos o documento físico original. Por rigor, afirmamos que o salto de 24/jun **coincide com** o ofício relatado, descrevendo a atuação do BCB de forma estritamente neutra (`docs/02-dolar-cripto.md` §10).

#### Notas do Orador & Rastreabilidade
- **Notas:** "Qual foi exatamente a porta que fechou em 23 de junho? Abrimos e citamos três fontes independentes: a coluna de Isac Costa no ConJur, o artigo do CEO da corretora de câmbio Dascam no Cointelegraph — que destaca que a decisão se tornou pública no dia seguinte, 24 de junho — e a própria resposta do Banco Central via Lei de Acesso à Informação declarando que operações cambiais de fundos para importar ativos virtuais não possuem respaldo nas normas em vigor."
- **Rastreabilidade:** Seção 5 de `notebooks/p5_07_story.ipynb`; `docs/sources.md` (`E-05`); `tasks/P1-04-events-brazil.md`.

---

<!-- SLIDE 6 -->
## Slide 6 — Só Uma Regra Mexeu no Preço: Todas as Regras vs Datas Ordinárias

### Das 13 regras e marcos testados, apenas o ofício de 23/jun/2026 superou todas as 1.073 datas limpas (+93,9 bps, $p = 0,0009$)

#### Layout Visual & Figura
- **Imagem:** `results/figures/P2-03_placebo_dist.png` (Distribuição empírica das variações antes/depois em datas placebo limpas vs os eventos regulatórios avaliados e o choque de 23/jun/2026).
- **Legenda (10 segundos):** Comparando os 20 dias úteis antes e depois de cada evento, o salto de +93,9 bps após 23/jun supera todas as 1.073 datas ordinárias limpas do histórico (maior movimento placebo = +65,7 bps; $p \approx 0,001$).

#### Pontos Principais (pt-BR)
- **Desenho do Estudo de Eventos com Placebos (`P2-03`, `F-016`):**
  - Para cada um dos **13 eventos verificados** (`P1-04`, avaliando datas de anúncio e vigência), calculamos a diferença entre a média dos 20 dias úteis PTAX posteriores ($[+1, +20]$) e a dos 20 dias úteis anteriores ($[-20, -1]$).
  - **Inferência por Placebos (sem depender de p-valores paramétricos):** Como a série do prêmio possui autocorrelação serial forte, p-valores paramétricos (Newey-West) exageram a significância. Por isso, comparamos cada regra contra **todas as 1.073 datas ordinárias limpas** (a pelo menos 20 dias úteis de qualquer evento) e contra 200 sorteios estratificados por dia da semana.
- **O Que os Dados Mostram (`F-016`):**
  - **23/jun/2026 (`E-05`) é único:** variação de **+93,9 bps** (de 15,2 para 109,1 bps), acima de **todas as 1.073 datas limpas** ($p = 1/1074 = 0,0009 \approx 0,001$; máximo placebo = $+65,7\text{ bps}$; $p = 0,005$ nos 200 sorteios).
  - **Nenhuma outra regra se destaca ($H_2$ consistente):** o marco de licenciamento das SPSAVs (Res. 519–521, `E-02`), os códigos de reporte cambial (`E-04`), a proibição de stablecoins em eFX (Res. 561, `E-06a`) e a proposta de IOF de 3,5% em cripto (`E-03`) tiveram variações entre **$-25\text{ e }+15\text{ bps}$**, dentro da oscilação normal ($p_{\text{placebo}} \ge 0,15$).
  - **O aumento do IOF no câmbio oficial em maio/2025 (`E-01`)** moveu o prêmio em $+13,2\text{ a }+15,4\text{ bps}$ ($p_{\text{placebo}} = 0,31\text{ a }0,38$), consistente com $H_3$.
  - **Poder do Teste (leitura honesta dos nulos):** Como datas ordinárias oscilam cerca de $\pm 37\text{ bps}$ na amostra completa ($\pm 23\text{ bps}$ em 2025–26), "efeito nulo" significa **ausência de efeito grande**, não prova de efeito zero.

| Evento Avaliado (`P1-04`) | ID | Data ($t_0$) | Tipo | Pré 20d (bps) | Pós 20d (bps) | Diferença (bps) | $p$-valor Placebo (1.073 datas) | Leitura Empírica |
|---|---|---|---|---|---|---|---|---|
| **Ofício Supervisão BCB (Fundos/Cripto)** | **E-05** | **23/06/2026** | **Vigência** | **15,2** | **109,1** | **+93,9** | **0,0009** | **Acima de todas as 1.073 datas** |
| Decreto 12.466 (IOF Câmbio 3,5%) | E-01 | 23/05/2025 | Vigência | 26,2 | 41,7 | +15,4 | 0,3147 | Dentro da variação ordinária |
| Res. BCB 521 Art. 4º (Códigos Cambiais) | E-04 | 04/05/2026 | Vigência | 4,7 | 11,9 | +7,2 | 0,6145 | Dentro da variação ordinária |
| Res. BCB 561 (Vedação Stablecoin em eFX) | E-06a | 30/04/2026 | Anúncio | 4,9 | 10,9 | +6,0 | 0,6471 | Dentro da variação ordinária |
| Proposta IOF Cripto 3,5% (Fazenda) | E-03 | 05/02/2026 | Anúncio | 7,6 | 5,5 | -2,1 | 0,8408 | Dentro da variação ordinária |
| Res. BCB 519–521 (Marco das SPSAVs) | E-02 | 02/02/2026 | Vigência | 8,4 | 4,1 | -4,3 | 0,7225 | Dentro da variação ordinária |
| Res. BCB 561 (Vedação Stablecoin em eFX) | E-06a | 01/10/2026 | Vigência | 22,8 | 17,5 | -5,3 | 0,6778 | Dentro da variação ordinária |
| Res. BCB 584 (Retenção Cautelar 24h) | E-06b | 07/08/2026 | Anúncio | 53,3 | 31,3 | -22,0 | 0,1872 | Dentro da variação ordinária |

#### Notas do Orador & Rastreabilidade
- **Notas:** "Testamos todas as 13 regras do nosso catálogo contra todas as 1.073 datas ordinárias limpas de seis anos. Nenhuma resolução publicada no Diário Oficial com meses de transição gerou salto anormal. Apenas o fechamento imediato de 23 de junho bateu todas as 1.073 datas ordinárias, com p-valor empírico de 0,0009."
- **Rastreabilidade:** Seção 6 de `notebooks/p5_07_story.ipynb`; `F-016`, `P1-04`, `scripts/p2_03_events.py`, `results/tables/P2-03_event_table.csv`.

---

<!-- SLIDE 7 -->
## Slide 7 — Outros Países Não se Mexeram: Controle Sintético e Bitcoin

### O Brasil descolou +109 bps do seu gêmeo sintético (+103 bps em DiD); no Bitcoin, a arbitragem triangular transmitiu o mesmo salto

#### Layout Visual & Figura
- **Imagem:** `results/figures/P2-04_synthetic_control.png` (Painel A: Brasil vs Brasil Sintético construído com 5 moedas doadoras; Painel B: gap do Brasil vs placebos de doadores com bom ajuste pré-choque).
- **Legenda (10 segundos):** Nenhuma das 5 moedas de comparação sem choque (EUR, MXN, TRY, ZAR, COP) acompanhou o salto brasileiro (+109,3 bps no controle sintético; razão pós/pré RMSPE de 9,31, 1º lugar entre 6 moedas).

#### Pontos Principais (pt-BR)
- **Brasil vs "Brasil Sintético" (Abadie, Diamond & Hainmueller 2010; `P1-05`, `P1-06`, `P2-04`, `F-017`):**
  - Construímos o mesmo prêmio do USDT para 5 moedas sem choque regulatório comparável e sem controles de capital estritos no período: **EUR (peso 63,6%), MXN (17,9%), TRY (13,4%), ZAR (4,5%) e COP (0,7%)** (pré-RMSPE de **7,05 bps** em 140 dias comuns de 01/nov/2025 a 22/jun/2026).
  - **Descolamento Agudo (24/jun a 21/jul/2026, 17 dias comuns):** O prêmio no Brasil superou o Brasil Sintético em **+109,3 bps** (e superou a média simples dos doadores via **Diferenças em Diferenças em +103,3 bps**, que não depende de ajuste de pesos). Nenhuma outra moeda teve movimento semelhante (variações de $-16\text{ a }+24\text{ bps}$).
  - **Limite Estatístico Explícito:** O Brasil ocupa o **1º lugar entre 6 moedas** na razão RMSPE pós/pré (**9,31** vs 0,78 a 1,22 nos doadores). Com 5 doadores, o menor p-valor de permutação possível é **$p = 1/6 \approx 0,167$** (ou $1/7 = 0,143$ incluindo IDR). Portanto, o controle sintético é **evidência complementar** de que o salto não veio de fora; a significância estatística vem da Seção 6 ($p = 0,0009$).
- **E o Bitcoin? Arbitragem Triangular na Binance (`P3-02`, `F-018`):**
  - O prêmio do Bitcoin em reais sobre a PTAX também saltou **+93,8 bps** em 24/jun. Isso decorre matematicamente da arbitragem triangular dentro da própria Binance ($\text{USDT/BRL} \times \text{BTC/USDT} = \text{BTC/BRL}$, cujo desvio médio é de apenas **0,36 bps**, dp 1,07): qualquer prêmio no USDT/BRL se transmite instantaneamente ao BTC/BRL, de modo que o teste não permite separar um choque específico em stablecoins de um choque amplo em cripto.

#### Notas do Orador & Rastreabilidade
- **Notas:** "Para descartar um choque global em mercados emergentes, comparamos o Brasil com cinco outras moedas. Enquanto euro, peso mexicano, lira turca, rand e peso colombiano ficaram parados, o Brasil descolou 109 pontos-base do seu gêmeo sintético e 103 pontos-base na diferença em diferenças simples. E por que o Bitcoin subiu os mesmos 93,8 bps? Porque na Binance a arbitragem triangular mantém BTC/BRL colado a USDT/BRL com diferença de menos de meio ponto-base."
- **Rastreabilidade:** Seção 7 de `notebooks/p5_07_story.ipynb`; `F-017`, `F-018`, `L-08`, `scripts/p2_04_synth.py`, `scripts/p3_02_btc.py`.

---

<!-- SLIDE 8 -->
## Slide 8 — Um Pico de Um Mês: Robustez do Salto e o que Não Podemos Afirmar

### O pico agudo é robusto em todas as 22 variantes (+74 a +128 bps); o nível pós-pico (+11 a +19 bps) não se distingue de deriva normal ($p = 0,24$)

#### Layout Visual & Figura
- **Imagem:** `results/figures/P4-01_robustness_forest.png` (*Forest plot* da bateria de 53 especificações testando janelas, definições do prêmio, corretoras, doadores e janelas pós-pico).
- **Legenda (10 segundos):** Qualquer maneira de medir o mês seguinte a 23/jun confirma um salto de +74 a +128 bps (10× a 35× o piso de ruído), mas o nível observado após 22/jul (+11 a +19 bps) ocorre com frequência em datas ordinárias ($p_{\text{placebo}} = 0,24$).

#### Pontos Principais (pt-BR)
- **O Que é Robusto: O Pico de Um Mês (`P4-01`, `F-022`):**
  - Em todas as **22 variantes agudas** — janelas de $\pm 10, \pm 15, \pm 20, \pm 30$ dias, 4 definições de prêmio (PTAX + Binance, fechamento diário 23h59 UTC, cotação direta Coinbase `USDT/USD`, mediana horária), 3 corretoras (Binance +93,9; Foxbit +93,3; MB +94,9 bps) e 6 modelos de controle sintético/DiD — o salto situa-se entre **+73,7 e +128,3 bps** (concentrado entre **+93 e +117 bps**).
- **O Que Não Foi Demonstrado: Um Novo Patamar Permanente (`F-022`):**
  - A partir de 22/jul/2026 o prêmio recuou de 109,1 para 26,8 bps (+11,5 a +19,3 bps acima da janela pré-ofício; +28,2 bps contra o controle sintético).
  - Embora o p-valor paramétrico pareça baixo devido à autocorrelação, o teste honesto de placebos comparando $[+21, +60]$ vs $[-20, -1]$ em todas as 882 datas limpas resulta em **$p_{\text{placebo}} = 0,24$** (dp de 16,5 bps; $p = 0,14$ usando apenas datas de 2025–26).
  - **Conclusão Científica Direta:** O efeito medido do fechamento da porta é **um pico agudo de um mês**. Não reivindicamos um efeito permanente sobre o nível do prêmio.
- **Três Fatos em Aberto que Reportamos com Transparência:**
  1. **O recuo de 22 de julho:** Nenhum evento verificado cai dentro de $\pm 5$ dias úteis de 22/jul (`P2-02`).
  2. **O salto de 6× no volume da Foxbit a partir de julho (`F-008`):** O volume mensal subiu de ~150 mi para ~1,0 bi USDT através de **ordens 5× maiores** (média de ~1.100 para ~6.200 USDT), não de mais negócios. Coincide no tempo com a parceria voluntária para clientes da NovaDAX em 07/jul (`M-04`) e com o lançamento da **Foxbit Infra** (liquidez B2B e *market making* próprio integrado a PicPay, 99Pay e Genial) em 18/jul (`M-05`), mas a causa segue aberta.
  3. **Subida prévia desde 25 de maio (`F-014`):** O prêmio já subia levemente (+8 bps) quatro semanas antes de 23/jun (antecipação ou deriva).

#### Notas do Orador & Rastreabilidade
- **Notas:** "Aqui aplicamos nossa regra mais importante: não afirmar mais do que os dados provam. O pico de um mês após 23 de junho passa em todas as 22 verificações de robustez, entre 74 e 128 pontos-base. Já os 11 a 19 pontos-base que restaram depois de 22 de julho têm p-valor de placebo de 0,24 — ou seja, oscilações desse tamanho acontecem sozinhas um quarto das vezes. Portanto, apresentamos como efeito medido apenas o pico de um mês."
- **Rastreabilidade:** Seção 8 de `notebooks/p5_07_story.ipynb`; `F-008`, `F-011`, `F-014`, `F-022`, `M-04`, `M-05`, `scripts/p4_01_robustness.py`, `results/tables/P4-01_robustness.csv`.

---

<!-- SLIDE 9 -->
## Slide 9 — Onde a Porta Está Fechada, o Prêmio é Grande: Comparação Internacional

### Em países onde residentes não compram dólares livremente, o USDT custa 4% a 7% a mais que o câmbio oficial; em mercados abertos, 0% a 1%

#### Layout Visual & Tabela Comparativa
- **Tabela / Gráfico Descritivo:** Prêmio anual médio do USDT sobre o câmbio oficial em 10 jurisdições (`P1-05`, `F-010`).
- **Legenda (10 segundos):** A comparação descritiva entre países mostra a mesma lógica: sob controles estritos de capital (Argentina e Ucrânia sob lei marcial), o dólar digital negocia com prêmio de 400 a 720 bps; em mercados abertos, dentro de $\pm 100\text{ bps}$.

#### Pontos Principais (pt-BR)
- **A Mesma Medida em 10 Moedas (`P1-05`, `P1-09`, `F-010`):**
  - Calculamos exatamente o mesmo prêmio do USDT sobre a taxa oficial de cada banco central (BCE, BanRep TRM, NBU da Ucrânia e BCRA da Argentina) entre 2020 e 2026:
  - **Mercados com controles estritos de saída de capitais (excluídos dos doadores pela regra pré-comprometida):**
    - **Argentina (`ARS`):** prêmio médio de **+721 bps (7,2%)** em 2025 e **+552 bps (5,5%)** em 2026.
    - **Ucrânia (`UAH`, controles da Lei Marcial — Res. NBU nº 18, `E-09`):** prêmio de **+410 a +490 bps (4,1%–4,9%)** em 2025–2026.
  - **Mercados abertos (cesta doadora e extensões):**
    - **Zona do Euro (`EUR`), México (`MXN`), Colômbia (`COP`), Turquia (`TRY`), Polônia (`PLN`), Indonésia (`IDR`):** prêmio dentro de **$\pm 70\text{ bps}$ ($\pm 0,7\%$)** em 2025–2026.
    - **África do Sul (`ZAR`):** entre **+70 e +100 bps (0,7%–1,0%)**, consistente com sua regulamentação prudencial de controle cambial.
  - **Posição do Brasil (`BRL`):** operava na ponta aberta (**+9 a +18 bps** em 2025–jun/2026) e deslocou-se temporariamente para **+109 bps** durante o mês em que o canal institucional foi interrompido.
- **Escopo Metodológico:** Duas jurisdições com controle estrito constituem uma **descrição comparativa**, não um teste estatístico formal (`F-010`).

#### Notas do Orador & Rastreabilidade
- **Notas:** "Quando olhamos para fora do Brasil, vemos o mesmo mecanismo em escala macro. Onde o cidadão ou a empresa não consegue acessar o dólar oficial livremente — como na Argentina ou na Ucrânia sob lei marcial — o USDT custa de 4% a 7% mais caro que o dólar oficial. O Brasil operava colado aos mercados mais abertos do mundo, a 9 pontos-base, e saltou para 109 pontos-base no mês seguinte ao ofício."
- **Rastreabilidade:** Seção 9 de `notebooks/p5_07_story.ipynb`; `F-010`, `D-05`, `D-11`, `D-12`, `E-08`, `E-09`, `scripts/p1_05_donors.py`.

---

<!-- SLIDE 10 -->
## Slide 10 — Quanto Custou: R$ 5 Mil por US$ 100 Mil e Fricções por Canal

### Durante o pico de um mês, o ofício adicionou R$ 5.052 a cada US$ 100 mil adquiridos via USDT (+93,9 bps)

#### Layout Visual & Figura
- **Imagem:** `results/figures/P3-01_route_costs.png` (Gráfico horizontal neutro de fricções de transação por regime histórico da rota USDT, cenários regulatórios e referenciais bancários com fontes primárias).
- **Legenda (10 segundos):** Para um comprador de US$ 100 mil em USDT (PTAX R$ 5,38), o salto de +93,9 bps representou um custo adicional de US$ 939 (R$ 5.052) durante o mês do pico; após o pico, a diferença (+11,5 bps = R$ 621) não é estatisticamente distinguível de ruído.

#### Pontos Principais (pt-BR)
- **1. O Custo Direto do Ofício (Resultado Principal, `P3-01`, `F-015`):**
  - Em um lote institucional de **US$ 100.000** (base R$ 538.000 a PTAX R$ 5,3800):
    - **Durante o pico agudo (24/jun a 21/jul/2026):** o prêmio subiu **+93,9 bps**, adicionando **US$ 939,10 ≈ R$ 5.052,36** por operação ($p_{\text{placebo}} = 0,0009$). No pico de 48h (24–25/jun, 169,9 bps), a fricção total atingiu **180,0 bps (R$ 9.682,66)**.
    - **Após o pico (22/jul a 30/out/2026):** +11,5 bps (**R$ 621,00**), valor não distinguível de deriva ordinária ($p_{\text{placebo}} = 0,24$).
- **2. Contexto Institucional: Fricções por Canal e Cenários Regulatórios (Fontes Primárias Abertas `R-01`..`R-07`):**
  *(Nota para decisão da equipe no freeze: manter este bloco resumido no slide [Opção C] ou remeter à tabela completa no Anexo B.5 [Opção A])*
  - **Parâmetros Bancários com Fonte Primária (`R-01`, `R-01b`, `R-02`):** Spread corporativo mediano do BCB para contratos $>$ US$ 55,6 mil = **20,0 bps** (*Estudo Especial BCB nº 48/2019*, `R-01`; teto conservador de 50 bps adiciona R$ 1.614); tarifa SWIFT = **US$ 25 (2,5 bps)** (*Tabela de Tarifas PJ Banco do Brasil*, `R-01b`: R$ 100 SWIFT / R$ 440 ordem online); IOF legal (`R-02`): **0%** na importação de bens (**22,5 bps = R$ 1.211**), **1,10%** em investimento ou disponibilidade pré-23/mai/2025 (**132,5 bps = R$ 7.129**), e **3,50%** em disponibilidade geral pós-23/mai/2025 (**372,5 bps = R$ 20.041**).
  - **Cenário S1 (Proposta IOF 3,5% em Cripto, `E-03`):** elevaria a rota USDT para **386,9 bps (R$ 20.815)**, igualando o custo tributário do câmbio bancário de disponibilidade.
  - **Cenário S2 (Retenção Cautelar de 24h $\ge$ US$ 10k, Res. BCB 584/2026, `E-06b`, `R-07`):** com *hedge* de 1 dia útil via Paridade Coberta de Juros ($\text{CDI } 10,75\% - \text{SOFR } 5,00\% = 2,28\text{ bps/dia}$ + taxa B3 = **2,5 bps**), totaliza **39,4 bps (R$ 2.120)**; sem *hedge*, custo esperado adicional é **0 bps**, mas expõe o comprador a um **risco cambial de 1 dia (95%) de 130 bps** (reportado como risco, não somado ao custo).
  - **Não-Equivalência Jurídica e Operacional (`docs/02-dolar-cripto.md` §10):** O contrato bancário liquida moeda soberana (USD) com registro no Sisbacen e desembaraço aduaneiro (Lei 14.286/2021). A compra local de USDT é aquisição de ativo virtual (Lei 14.478/2022, declarada via IN RFB 1.888), embute risco privado do emissor/corretora e **não** liquida importação formal nem eFX (Res. BCB 561/2026; resposta LAI em `E-05`).

| Medida / Canal / Cenário (`P3-01_route_costs.csv`) | Prêmio (bps) | Spread / Taxa (bps) | IOF / Carrego CIP (bps) | SWIFT / Rede (bps) | Total (bps) | Custo por US$ 100k (R$) |
|---|---|---|---|---|---|---|
| **Custo do Ofício: Pico de 20 Dias (24/jun–21/jul)** | **+93,9** | **0,0** | **0,0** | **0,0** | **+93,9** | **+R$ 5.052,36** |
| **Custo do Ofício: Pós-Pico (22/jul–30/out, $p=0,24$)** | +11,5 | 0,0 | 0,0 | 0,0 | +11,5 | +R$ 621,00 (ruído) |
| **USDT Regime 4 (Base Pré-Ofício, jul/25–jun/26)** | 9,3 | 10,0 | 0,0 | 0,1 | 19,4 | R$ 1.043,72 |
| **USDT Regime 5 (Choque Agudo, 24/jun–21/jul/26)** | 109,1 | 10,0 | 0,0 | 0,1 | 119,2 | R$ 6.412,96 |
| **Banco: Importação de Bens (IOF 0%, `R-01`/`R-02`)** | 0,0 | 20,0 | 0,0 | 2,5 | 22,5 | R$ 1.210,50 |
| **Banco: Investimento / Disp. Pré-Mai/25 (IOF 1,1%)** | 0,0 | 20,0 | 110,0 | 2,5 | 132,5 | R$ 7.128,50 |
| **Banco: Disponibilidade Pós-Mai/25 (IOF 3,5%)** | 0,0 | 20,0 | 350,0 | 2,5 | 372,5 | R$ 20.040,50 |
| **Cenário S1: IOF 3,5% em Cripto (`E-03`)** | 26,8 | 10,0 | 350,0 | 0,1 | 386,9 | R$ 20.815,22 |
| **Cenário S2a: Retenção 24h com Hedge CIP (`R-07`)** | 26,8 | 10,0 | 2,5 | 0,1 | 39,4 | R$ 2.119,72 |

#### Notas do Orador & Rastreabilidade
- **Notas:** "Traduzindo pontos-base em reais: para quem comprava um lote de US$ 100 mil em USDT, o mês seguinte ao ofício custou R$ 5.052 a mais por operação. Também colocamos na tabela as fricções de cada canal bancário formal — medidas pelo Estudo Especial nº 48 do próprio BCB — ressaltando que câmbio bancário e ativo virtual têm naturezas jurídicas e usos legais distintos."
- **Rastreabilidade:** Seção 10 de `notebooks/p5_07_story.ipynb`; `F-015`, `R-01`, `R-01b`, `R-02`..`R-07`, `scripts/p3_01_costs.py`, `results/tables/P3-01_route_costs.csv`.

---

<!-- SLIDE 11 -->
## Slide 11 — Do Lado do Dólar: Quando o Resgate Fecha (Fim de Semana do SVB e 11 Casos)

### O USDC fechou a US$ 0,863 enquanto os bancos estavam fechados e voltou a US$ 0,989 uma hora após a garantia de domingo

#### Layout Visual & Figuras
- **Imagens:** `results/figures/P3-04_svb_weekend.png` (Série horária do USDC/USD na Bitstamp no fim de semana do SVB com marcação do anúncio conjunto às 22h15 UTC) e `results/figures/P3-04_depeg_cases.png` (Profundidade e duração dos 11 casos).
- **Legenda (10 segundos):** O mesmo mecanismo aparece no próprio dólar: sem resgate bancário no fim de semana do SVB, o USDC caiu a US$ 0,863 (mínima intra-hora US$ 0,805), mas voltou a US$ 0,989 45 minutos após o comunicado do Fed/Tesouro/FDIC no domingo à noite, *antes* da reabertura dos bancos.

#### Pontos Principais (pt-BR)
- **O Fim de Semana do Silicon Valley Bank (10 a 13/mar/2023; Bitstamp `USDC/USD` 1h, `P1-07`, `P3-04`, `F-019`):**
  - Com os bancos americanos fechados de sexta-feira 16h a segunda-feira 9h30 (NY) e US$ 3,3 bilhões da Circle retidos no SVB, o canal primário de resgate 1:1 estava fechado.
  - O menor fechamento horário do USDC foi **US$ 0,863** no sábado às 07h UTC (mínima intra-horária de **US$ 0,805**).
  - No domingo às **22h15 UTC (`D-13`)**, Tesouro, Federal Reserve e FDIC anunciaram garantia integral aos depositantes do SVB. Às **23h00 UTC** — **antes de os bancos reabrirem** — os arbitradores já haviam levado o USDC de volta a **US$ 0,989** (e a US$ 0,999 na abertura de segunda-feira). O que restaura a paridade é a **expectativa crível de acesso ao canal de resgate**.
- **Os 11 Descolamentos Confirmados Abaixo de US$ 1,00 (`F-013`, `F-019`, `P3-09`):**
  - Nossa triagem corrigida identificou **11 quedas independentes abaixo de US$ 1,00** em 7 stablecoins (2019–2026).
  - Como $11 < 12$ (nosso limiar pré-comprometido em `docs/01-depeg-recovery.md` §5), **não estimamos curvas de sobrevivência de Kaplan-Meier** e apresentamos a tabela descritiva de casos com fontes primárias e de imprensa abertas (`DP-01` a `DP-10` em `docs/sources.md`):

| Categoria Descritiva (`P3-04_category_summary.csv`) | Casos ($N$) | Moedas | Recuperados | Duração (Recuperados) | Menor Fechamento Horário | Contexto Documentado (`docs/sources.md`) |
|---|---|---|---|---|---|---|
| **1. Fim de semana bancário / resgate fechado** | 2 | USDC, USDP | 2 de 2 (100%) | 58h (51h–65h) | US$ 0,863 – 0,974 | Recepção do SVB (`D-13`) e US$ 250 mi da Paxos no Signature Bank (`DP-01`) |
| **2. Fricções temporárias de liquidez / reservas** | 7 | UST, TUSD, FDUSD | 7 de 7 (100%) | 492h (21h–2.719h) | US$ 0,954 – 0,992 | Crise Frog Nation (`DP-02`), troca de auditoria TUSD (`DP-03`), flash crash BTC (`DP-04`), ação da SEC sobre TUSD (`DP-05`), rali pós-eleição (`DP-06`), disputa First Digital/Sun (`DP-07`), nota 5/Weak S&P (`DP-08`) |
| **3. Colapso algorítmico sem reservas externas** | 1 | UST (mai/2022) | 0 de 1 (0%) | N/A (Colapso) | US$ 0,245 (terminal) | Saque no Curve, corrida no Anchor e hiperinflação de 80× em LUNA (`DP-09`, Fed Richmond) |
| **4. Deslistagem programada na Binance** | 2 | USDP (set/2026) | 1 de 2 (50%) | 60h (1 censurado) | US$ 0,988 – 0,994 | Anúncio da Binance em 10/set/2026 removendo o par USDP/USDT em 24/set/2026 (`DP-10`) |

#### Notas do Orador & Rastreabilidade
- **Notas:** "No capítulo em dólares, vemos o espelho exato do caso brasileiro. No fim de semana do SVB, quando o canal bancário americano fechou na sexta-feira, o USDC caiu até 86 centavos no fechamento horário. Mas bastou o governo americano garantir os depósitos às 22h15 de domingo para o preço voltar a 98,9 centavos na mesma hora, antes de qualquer banco abrir na segunda-feira. E cumprindo nossa regra pré-comprometida: como encontramos 11 eventos abaixo de 1 dólar e nosso protocolo exigia 12 para curvas de sobrevivência, reportamos os 11 casos em tabela descritiva, cada um com sua fonte aberta."
- **Rastreabilidade:** Seção 11 de `notebooks/p5_07_story.ipynb`; `F-013`, `F-019`, `D-08`, `D-13`, `DP-01`..`DP-10`, `scripts/p3_04_depeg_chapter.py`.

---

<!-- SLIDE 12 -->
## Slide 12 — A Solução Prática: O Monitor do Dólar Digital

### Calibrado apenas em 2020–2025, nosso alarme CUSUM dispara no próprio dia 24/jun/2026 com metade dos falsos alarmes de uma regra simples

#### Layout Visual & Figura
- **Imagem:** `results/figures/P3-03_monitor.png` (Painel superior: prêmio diário com banda de ruído e disparos de alarme; painel inferior: estatística CUSUM sequencial vs limiar calibrado no treino).
- **Legenda (10 segundos):** Usando apenas dados passados (treino 2020–2025, orçamento de até 2 alarmes/ano), o monitor em código linear detecta o salto de 24/jun/2026 no próprio dia (atraso zero) e gera apenas 2 outros alarmes em 2026, contra 4 da regra ingênua.

#### Pontos Principais (pt-BR)
- **Desenho Sem Olhar para o Futuro (*No Look-Ahead*, `P3-03`, `F-014`):**
  - A especificação foi escrita e registrada no Git antes do backtest (`tasks/P3-03-monitor.md`).
  - **Três componentes diários:** (1) Prêmio PTAX limpo do preço global do USDT; (2) Piso móvel de ruído microestrutural Corwin-Schultz; (3) Detector sequencial **CUSUM bilateral** sobre o excesso padronizado acima do ruído.
  - **Separação estrita Treino vs Teste:** Limiar $h = 24,5$ calibrado exclusivamente em **2020–2025** para respeitar um orçamento máximo de 2 alarmes por ano (gerou 9 alarmes em 5 anos = 1,8/ano) e congelado para o teste fora da amostra em **2026**.
- **Desempenho no Teste de 2026 (Comparado à Linha de Base Ingênua):**
  - **Detecção do choque de 24/jun/2026:** Disparo no **próprio dia 24 de junho (atraso = 0 dias úteis)**; a estatística CUSUM já acumulava pressão desde 25 de maio (22,6 em 23/jun) e saltou para 62,0 em 24/jun.
  - **Detecção do recuo de 22/jul/2026:** Identificado em **11 dias úteis PTAX** (06/ago/2026).
  - **Menor taxa de falsos alarmes:** Apenas **2 outros alarmes** em 10 meses de 2026 (2,4/ano), contra **4 outros alarmes** (4,8/ano) de uma regra simples de médias móveis ("média de 5 dias vs 60 dias") calibrada com exatamente o mesmo orçamento no treino.

| Regra de Monitoramento (`P3-03_backtest.csv`) | Parâmetro Calibrado (2020–2025) | Alarmes no Treino (2020–2025) | Atraso no Salto de 24/jun/2026 | Atraso no Recuo de 22/jul/2026 | Outros Alarmes no Teste (2026) |
|---|---|---|---|---|---|
| **Monitor CUSUM (Nossa Solução)** | **$h = 24,5$** | **9 (1,8 / ano)** | **0 dias úteis (24/jun)** | **11 dias úteis (06/ago)** | **2 (2,4 / ano)** |
| Linha de Base Simples (MM 5d vs 60d) | $c = 7,25$ | 10 (2,0 / ano) | 0 dias úteis (24/jun) | 12 dias úteis (07/ago) | 4 (4,8 / ano) |

#### Notas do Orador & Rastreabilidade
- **Notas:** "Como solução prática para o mercado e para o regulador, construímos o Monitor do Dólar Digital em um script linear que lê dados públicos do BCB e da Binance. Calibrado apenas até 2025, sem espiar 2026, ele disparou o alerta no próprio dia 24 de junho com metade dos falsos alarmes de uma regra simples."
- **Rastreabilidade:** Seção 12 de `notebooks/p5_07_story.ipynb`; `F-014`, `scripts/p3_03_monitor.py`, `data/processed/P3-03_monitor_daily.csv`.

---

<!-- SLIDE 13 -->
## Slide 13 — Lições de 2025: O que Mudamos no Método desde o 6º Datathon

### Em 2025 nosso melhor modelo perdeu para "amanhã = hoje" e 53,6% do spread do Compound V3 era subsídio de token COMP

#### Layout Visual & Figura
- **Imagem:** `results/figures/P3-08_subsidy_share_2025.png` (Decomposição diária do spread DeFi vs SOFR entre 2023 e 2025 em rendimento base orgânico `apyBase` e subsídios em tokens `apyReward`).
- **Legenda (10 segundos):** Auditando nosso próprio trabalho de 2025 (3º lugar), mostramos que o modelo complexo perdia para a persistência ingênua e que mais da metade do spread do Compound V3 sobre o SOFR vinha de emissões promocionais do token COMP.

#### Pontos Principais (pt-BR)
- **Auditoria do Nosso Trabalho de 2025 (`P0-01`, `P3-08`, `F-005`, `F-020`):**
  1. **O Modelo Perdeu para a Persistência Ingênua (`F-005`):** Na janela de teste de 2025 (200 dias), a previsão ingênua *"amanhã = hoje"* atingiu **$\text{MAE} = 0,169$ ($R^2 = 0,776$)**, superando nosso modelo híbrido K-Means + SVM (**$\text{MAE} = 0,248$, $R^2 = 0,622$**).
  2. **O "Spread de Risco" Era, em Grande Parte, Subsídio de Token (`F-020`):** Decompondo os dados do DeFiLlama (`D-14`) contra o SOFR (`D-15`), **53,6% do spread bruto do Compound V3** (e **37,5% do spread ponderado por TVL** Aave + Compound) era composto por recompensas promocionais em tokens `COMP` (`apyReward`). No período de teste de 2025, o spread orgânico líquido (`apyBase − SOFR`) do Compound V3 foi **negativo (-8,2 bps)**.

| O que Fizemos em 2025 (6º Datathon — 3º Lugar) | O que Fizemos em 2026 (7º Datathon) | Evidência / Arquivo |
|---|---|---|
| Melhor modelo perdeu para "amanhã = hoje" sem reportar a baseline | **Toda estimativa é comparada à sua linha de base ingênua**; o monitor CUSUM bate a regra simples fora da amostra | `F-005`, `F-014`, `F-021` |
| Linguagem causal extraída de *clustering* (K-Means) | **Reivindicações causais restritas a desenhos com placebos** (estudo de eventos e controle sintético) e **apenas para o pico de 1 mês** | `F-016`, `F-017`, `F-022` |
| Spread bruto DeFi tratado como puro risco de crédito | **Decomposição explícita de fricções, impostos e subsídios** (53,6% do spread do Compound V3 em 2025 era token `COMP`) | `F-015`, `F-020` |
| Brasil aparecia apenas na introdução; hiperparâmetros livres | **O mercado brasileiro é a pergunta central**; hipóteses e especificações registradas no Git antes dos testes | `P1-02`, `P2-02`, `P2-06` |

#### Notas do Orador & Rastreabilidade
- **Notas:** "No ano passado ficamos em 3º lugar neste Datathon. Nossa primeira tarefa neste ano foi auditar criticamente aquele trabalho. Descobrimos duas coisas: nosso modelo complexo perdia para uma previsão ingênua de que amanhã é igual a hoje, e 53,6% do spread do Compound sobre o SOFR era subsídio promocional em tokens COMP. Em 2026 corrigimos cada um desses pontos: linha de base obrigatória, pré-registro no Git e identificação econômica limpa no Brasil."
- **Rastreabilidade:** Seção 13 de `notebooks/p5_07_story.ipynb`; `F-005`, `F-020`, `D-06`, `D-14`, `D-15`, `scripts/p3_08_subsidy.py`.

---

<!-- SLIDE 14 -->
## Slide 14 — O que os Testes Mostraram, Implicações e Limitações

### O fechamento do canal gerou um pico robusto de um mês (+94 bps = R$ 5 mil/US$ 100k); efeito duradouro não foi demonstrado

#### Layout Visual & Placar Final
- **Tabela-Síntese:** Placar das hipóteses pré-comprometidas ($H_1, H_2, H_3, H_0$) lado a lado com as limitações metodológicas explícitas (Seções 14 e 15 de `notebooks/p5_07_story.ipynb`).
- **Legenda (10 segundos):** Confirmamos um salto agudo de um mês após 23/jun/2026 em todas as corretoras e especificações, sem efeito duradouro demonstrado ($p = 0,24$), e entregamos um termômetro diário aberto para supervisão cambial e tesourarias.

#### Pontos Principais (pt-BR)
- **1. Placar das Hipóteses Pré-Comprometidas (Seção 14 do Protótipo):**

| Hipótese | Veredito Empírico | Evidência que Sustenta o Veredito |
|---|---|---|
| **$H_1$** Fechar o canal elevou o prêmio | **Sustentada para um pico de 1 mês** (+93,9 bps, $p = 0,0009$; mesmo salto em 3 corretoras; +109,3 bps vs Brasil Sintético). **Não demonstrada** para um efeito duradouro ($p_{\text{placebo}} = 0,24$) | `F-009`, `F-011`, `F-016`, `F-017`, `F-022` |
| **$H_2$** Só a regra restritiva no canal marginal importa | **Consistente:** nenhuma das outras 12 regras e marcos moveu o prêmio além de datas ordinárias (o teste detecta movimentos acima de ~23–37 bps) | `F-016` |
| **$H_3$** IOF de maio/2025 moveu o prêmio menos que o imposto | **Consistente:** variação de +13,2 a +15,4 bps ($p_{\text{placebo}} = 0,31\text{ a }0,38$, não anômala) frente a um aumento tributário de +240 bps | `F-016` |
| **$H_0$** Corretora única, Real ou USDT explicam o salto | **Rejeitada** para o salto de 24 de junho de 2026 | `F-009` |

- **2. Implicações para Supervisão Cambial e Drex:**
  - Atos de supervisão que interrompem imediatamente um canal operacional geram descolamentos agudos de preço (+94 bps = R$ 5.052/US$ 100k), enquanto normas públicas com janela de transição (Res. 519–521, Res. 561) são absorvidas sem saltos. Para o **Drex** e *on/off-ramps* regulados, manter canais institucionais claros de arbitragem é essencial para evitar prêmios de escassez.
- **3. Limitações que Declaramos no Slide (Seção 15 do Protótipo):**
  1. **Não vimos o texto físico do ofício de 23/jun:** temos dois relatos independentes e a resposta oficial do BCB via LAI (`E-05`); por isso dizemos que o salto *coincide com* a notícia.
  2. **Apenas o pico de um mês é medido:** o recuo a partir de 22/jul não possui evento em $\pm 5$ dias (`P2-02`), e o nível pós-pico não se distingue de deriva normal ($p = 0,24$).
  3. **Subida prévia desde 25 de maio (+8 bps) e volume na Foxbit (`F-008`):** causas seguem em aberto.
  4. **Amostra internacional curta:** o controle sintético tem 5 doadores ($p \ge 1/6 \approx 0,167$), servindo como evidência complementar, e a comparação com ARS/UAH é descritiva.
  5. **Histórico longo centrado na Binance:** Foxbit e Mercado Bitcoin confirmam o salto de junho de 2026, mas a série desde 2020 vem da Binance.

#### Notas do Orador & Rastreabilidade
- **Notas:** "Concluímos respondendo à nossa pergunta com total transparência sobre o que sabemos e o que não sabemos: fechar a porta em 23 de junho coincidiu com um salto de 94 pontos-base — R$ 5 mil por cada US$ 100 mil — que durou um mês e bateu todas as 1.073 datas ordinárias do histórico. O que veio depois de julho não pode ser separado da deriva normal do mercado. Muito obrigado."
- **Rastreabilidade:** Seções 14 e 15 de `notebooks/p5_07_story.ipynb`; `F-009`..`F-022`; `prompt.md` §5 e §8.

# Quanto Custa Fechar a Porta?
## O Prêmio do Dólar Digital no Brasil e os Limites à Arbitragem

**Apresentação de Resultados — 7º Datathon de Moedas Digitais FGV EESP (Novembro de 2026)**  
**Equipe Out of Sample:** CS 1 (Renzo), CS 2 (Nattan), CS 3 (Jonathan), Economista (Felipe)  
**Instituições Organizadoras:** FGV EESP, Centro de Estudos em Finanças Digitais FGV, com apoio de FGV/Ripple (UBRI) e USP-UBRI  

---

### Sumário da Apresentação e Mapeamento com o Protótipo (`notebooks/p5_07_story.ipynb` & `docs/06-so-what.md`)
1. **Slide 1 (Seção 1):** Quanto custa fechar a porta? — Tese, pergunta de pesquisa e o experimento natural
2. **Slide 2 (Seção 2):** O que esperávamos — Hipóteses pré-comprometidas ($H_0$ a $H_3$) e critérios de falsificação
3. **Slide 3 (Seção 3):** Dados e medida — Pareamento na janela PTAX, piso de ruído e quebras estruturais cegas (`F-007`, `F-011`, `F-021`)
4. **Slide 4 (Seção 4):** O salto: mesmo tamanho em três corretoras — Binance, Foxbit e Mercado Bitcoin e descarte de confundidores (`F-009`)
5. **Slide 5 (Seção 5 + `P3-14`/`P3-10`):** A porta que fechou — As 10 fontes sobre o ofício de 23/jun (`F-023`) e a queda de 78% na compra de stablecoins no exterior nas estatísticas do BCB (`F-024`)
6. **Slide 6 (Seção 6 + `P3-12`):** Só o ofício não publicado no DOU (efeito imediato) moveu o prêmio — As 8 regras datadas e 13 eventos contra todas as 1.073 datas limpas ($p = 0,0009$, `F-016`, `F-026`)
7. **Slide 7 (Seção 7):** Outros países não se mexeram — Controle sintético internacional, DiD e arbitragem triangular no Bitcoin (`F-017`, `F-018`)
8. **Slide 8 (Seção 8):** Um pico de um mês — Robustez em 22 variantes agudas do USDT/BRL (26 c/ BTC e compostos: +74 a +128 bps) e nível pós-pico não distinguível de deriva ($p = 0,24$, `F-022`)
9. **Slide 9 (Seção 9):** Onde a porta está fechada, o prêmio é grande — Evidência descritiva internacional (ARS, UAH vs mercados abertos, `F-010`)
10. **Slide 10 (Seção 10 + `P3-11`):** Quanto custou: R$ 5.052 por US$ 100 mil e R$ 106–145 milhões transferidos em 4 semanas (`F-015`, `F-025`, Opções C e A)
11. **Slide 11 (Seção 11 + `P3-09`):** Do lado do dólar: quando o resgate fecha — O fim de semana do SVB e a tabela de 11 quedas na Binance (+ caso SVB Bitstamp = 12 linhas) com fontes abertas (`F-013`, `F-019`)
12. **Slide 12 (Seção 12 + `P3-13`):** Monitor do Dólar Digital e Previsão Datada para 01/jan/2027 — Alarme CUSUM sem *look-ahead* (`F-014`) e previsão registrada para a Res. BCB 584 (`F-027`)
13. **Slide 13 (Seção 13):** Lições de 2025 — Linha de base ingênua obrigatória e decomposição de subsídios em tokens (`F-005`, `F-020`)
14. **Slide 14 (Seções 14–15):** O que os testes mostraram e limitações — Placar das hipóteses, implicações para supervisão/Drex e limites

---

<!-- SLIDE 1 -->
## Slide 1 — Quanto custa fechar a porta?

### Quando a supervisão fecha um canal de arbitragem entre o mercado cripto e o câmbio oficial, quanto a mais os brasileiros pagam por um dólar digital?

#### Layout Visual & Estrutura
- **Posicionamento:** Capa executiva combinada à tese econômica central e à pergunta de pesquisa (Requisito `prompt.md` §8: uma pergunta clara logo na abertura, respondível com a evidência mostrada).
- **Legenda (10 segundos):** Um ativo só permanece na paridade enquanto algum canal permite comprar barato de um lado e vender caro do outro; em 24/jun/2026, após ofício de supervisão do BCB que paralisou a importação de criptoativos via fundos (queda de 78% nas compras externas medidas pelo BCB em julho), o prêmio do USDT sobre a PTAX saltou +93,9 bps (+R$ 5.052 por US$ 100 mil; R$ 106–145 milhões transferidos em quatro semanas).

#### Pontos Principais (pt-BR)
- **Tese Econômica (Limites à Arbitragem — Shleifer & Vishny 1997; Makarov & Schoar 2020):**
  - No Brasil, o dólar digital (USDT comprado com reais) e o dólar oficial (PTAX) são mantidos próximos pela arbitragem entre corretoras cripto e o mercado formal de câmbio:
    $$\text{USDT/BRL}_t = \text{PTAX}_t \times \text{USDT/USD}_t \times (1 + \pi_t)$$
  - Quando uma regra fecha ou encarece a porta fiduciária mais barata de arbitragem, o prêmio $\pi_t$ descola da paridade até o custo do próximo canal disponível (Obstfeld & Taylor 1997).
- **A Pergunta de Pesquisa:**
  - *Quanto a mais os brasileiros pagaram por um dólar digital quando uma intervenção fechou uma dessas portas, quanto dinheiro mudou de mãos e quais regras realmente moveram o preço?*
- **O Experimento Natural (23 de junho de 2026):**
  - Em 23/jun/2026, o Banco Central enviou notificação de supervisão a bancos (13 bancos segundo a *Exame*), corretoras de câmbio, empresas cripto e fundos determinando a *"imediata descontinuidade"* de operações de câmbio de fundos para importar ativos virtuais (`E-05`, `F-023`). Nas estatísticas do setor externo do BCB (`SGS 29644`), as compras líquidas de stablecoins no exterior caíram **78% em julho de 2026** (de US$ 2,54 bi para US$ 0,57 bi, `F-024`).
- **Relevância Prática:**
  - Afeta compradores institucionais e de varejo (uma transferência equivalente a uma tarifa de ~0,95%, somando **R$ 106 milhões na Binance** ou **R$ 145 milhões em três corretoras** em 4 semanas, `F-025`), a supervisão cambial do BCB (`Lei nº 14.286/2021` e `Lei nº 14.478/2022`) e o desenho de pontes institucionais reguladas de liquidez no ecossistema **Drex** e em corredores transfronteiriços (**Ripple ODL / RLUSD**).

#### Notas do Orador & Rastreabilidade
- **Notas:** "Senhores jurados, nossa pergunta é direta: quanto custa fechar a porta da arbitragem cambial no Brasil? Testamos seis anos de dados pareados na janela da PTAX e 13 eventos regulatórios. Mostraremos que sete regras publicadas com prazos de transição não moveram o prêmio, mas o fechamento imediato do canal de importação via fundos em 23 de junho de 2026 derrubou em 78% as compras externas de stablecoins registradas pelo BCB e gerou um salto de 94 pontos-base — R$ 5.052 por cada US$ 100 mil, ou R$ 106 a 145 milhões transferidos de compradores para vendedores em quatro semanas."
- **Rastreabilidade:** Seção 1 de `notebooks/p5_07_story.ipynb`; `docs/06-so-what.md`; `F-001`, `F-002`, `F-015`, `F-016`, `F-023`..`F-026`, `L-05`..`L-07`.

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
  - Especificações de quebras estruturais (`P2-02`), do monitor em tempo real (`P3-03`), da queda de importações no BCB (`P3-10`, `4f6f14e`), do volume financeiro transferido (`P3-11`, `91f9c25`) e da previsão para 01/jan/2027 (`P3-13`, `393a14a`) foram todas registradas em commits no Git antes da execução; estimativa oficial congelada em `results/agentic/team_estimate.json` (`80fc866`).

#### Notas do Orador & Rastreabilidade
- **Notas:** "Para evitar qualquer caça a resultados estatísticos, registramos nossas hipóteses e regras de decisão no Git antes de rodar os testes confirmatórios. Se o salto de 24 de junho aparecesse apenas na Binance, ou se moedas emergentes tivessem se movido juntas, nossa hipótese estaria refutada."
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
  - `USDT/BRL` na Binance é pareado nas aberturas horárias das 4 janelas de consulta da PTAX (10h, 11h, 12h e 13h BRT / 13h–16h UTC, aproximação da consulta aleatória de 2 minutos documentada em `scripts/p1_02_premium.py`) e dividido pela cotação do próprio USDT em dólares (`1/USDCUSDT`, preenchido na janela set/2022–mar/2023 por `1/BUSDUSDT` e validado via Coinbase `USDT/USD`, que concorda em ~1 bp).
- **Piso de Ruído Microestrutural (`P2-01`, `F-007`):**
  - O spread de compra e venda estimado por Corwin & Schultz (2012) e Abdi & Ranaldo (2017) é de **2 a 10 bps** (caindo para ~2,5 bps após o corte de 10× no tick size da Binance em 27/jun/2025, `M-03`). O prêmio mediano anual é **4 a 11 vezes maior** que o ruído em todos os anos.
- **Teste Cego de Quebras Estruturais (Bai & Perron 2003, critério LWZ; `P2-02`, `F-011`):**
  - Sem receber nenhuma data regulatória, o algoritmo encontra 5 quebras. A **4ª quebra ocorre em 24/jun/2026** com o intervalo de confiança mais estreito da série (**18 a 30/jun**, semi-largura de 3,1 dias úteis; **23 a 30/jun** com variância heterocedástica por regime), saltando de **9,3 para 109,1 bps (+99,8 bps)**, seguida por recuo parcial a partir de **22/jul/2026** (para 26,8 bps).
  - No modelo de limiar **Band-TAR** (`P3-07`, `F-021`), a banda de não-arbitragem era de apenas **$c = 1,61\text{ bps}$** no regime pré-ofício ($N=242$, dentro do ruído de livro) e abriu **26 vezes para $c = 41,95\text{ bps}$** durante o pico agudo ($N=20$; ou **$c = 32,42\text{ bps}$** e meia-vida de $1,60\text{ dias}$ na amostra pós-ofício agrupada com $N=91$, reduzindo o RMSE em 20,3% vs passeio aleatório e 10,8% vs AR(1) linear).

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
    - **Binance:** de 15,2 para 109,1 bps (**+93,9 bps**; janela diária PTAX de 155,4 bps em 24/jun e 184,3 bps em 25/jun; máxima horária de **245,9 bps** em 24/jun).
    - **Foxbit (corretora nacional):** de 14,7 para 108,0 bps (**+93,3 bps**).
    - **Mercado Bitcoin (corretora nacional):** de 10,7 para 105,6 bps (**+94,9 bps**).
- **Explicações Alternativas Descartadas ($H_0$ Rejeitada, `F-009`):**
  1. **Não foi um choque no próprio Real (PTAX):** Em 24/jun a PTAX variou $+0,68\%$, uma oscilação diária comum; em dias de alta semelhante do dólar, o prêmio historicamente recua levemente em vez de subir.
  2. **Não foi o preço global do USDT em dólares:** A cotação `USDT/USD` na Coinbase e na Bitstamp moveu-se menos de **1 ponto-base** naqueles dias.
  3. **Não foi pane ou restrição específica da Binance:** Nenhuma suspensão de Pix ou manutenção ocorreu em junho de 2026 (ao contrário de jun/2022, `E-07`), e duas corretoras locais independentes subiram juntas.
- **Cronologia Intradiária Validada contra os Relatos de Imprensa (`P3-14`, `F-023`):**
  - Os movimentos reportados pela imprensa à época (~0,1% antes $\to$ pico de 1%–2% em 24/jun $\to$ recuo a 0,5% na sexta-feira 26/jun após reunião com o BCB) batem exatamente com a nossa série: **15,2 bps** antes $\to$ máxima horária de **245,9 bps (2,46%)** e janela PTAX de **155,4 bps** em 24/jun $\to$ recuo temporário para **75,6 bps (0,76%)** na sexta-feira 26/jun $\to$ retorno a **130–140 bps** em 29–30/jun.

#### Notas do Orador & Rastreabilidade
- **Notas:** "Poderia esse salto ser um problema técnico da Binance, uma desvalorização do real ou uma crise do próprio Tether lá fora? Testamos as três hipóteses nulas. O Tether em dólar não mexeu nem 1 ponto-base, o real teve um dia comum, e duas corretoras brasileiras independentes — Foxbit e Mercado Bitcoin — subiram os mesmos 93 a 95 pontos-base."
- **Rastreabilidade:** Seção 4 de `notebooks/p5_07_story.ipynb`; `F-009`, `F-023`, `D-01`, `D-04`, `D-07`, `scripts/p2_05_checks.py`, `scripts/p3_14_press_check.py`.

---

<!-- SLIDE 5 -->
## Slide 5 — A Porta que Fechou: O Ofício de 23/jun e a Queda de 78% nas Importações de Stablecoins

### Dois veículos tiveram acesso ao ofício em 24–25/jun (`F-023`), e as compras externas de stablecoins registradas pelo BCB caíram 78% em julho (`F-024`)

#### Layout Visual & Figura
- **Imagem:** `results/figures/P3-10_imports.png` (Série mensal de aquisições líquidas de stablecoins no exterior por residentes — BCB `SGS 29644`, US$ milhões — vs prêmio médio mensal do USDT sobre a PTAX, jan/2024 a set/2026).
- **Legenda (10 segundos):** A imprensa especializada teve acesso ao ofício em 24–25/jun (13 bancos notificados) e o BCB confirmou sua posição via LAI (`F-023`); no mês seguinte, as compras de stablecoins no exterior compiladas pelo próprio BCB caíram **78%** (de US$ 2,54 bi para US$ 0,57 bi, $p = 0,022$), evidência consistente com o fechamento de um canal de oferta (`F-024`).

#### Pontos Principais (pt-BR)
- **1. O Que Sabemos Sobre o Ofício de 23/jun/2026 (10 Fontes Abertas em `P3-14`, `F-023`):**
  - **Acesso contemporâneo ao documento (`E-05.1`, `E-05.2`):** Em **24/jun**, o *Cointelegraph Brasil* noticia o documento (*"segundo uma notificação compartilhada com o Cointelegraph Brasil"*, determinando a *"imediata descontinuidade desse tipo de operação"*). Em **25/jun**, a *Exame* publica trecho literal (*"diz um trecho da notificação ao qual a EXAME teve acesso"*) informando que **13 bancos** foram notificados; a ABToken descreve que fundos *"usavam contas em bancos para comprarem criptomoedas no exterior e depois venderem esses ativos para as corretoras"* (*"um choque de oferta"*).
  - **O diferencial tributário da rota fechada (`E-05.10`, `R-02`):** Aplicações de fundos no exterior tinham **alíquota zero de IOF-Câmbio** (Decreto nº 6.306/2007, art. 15-B, III, aberto no Planalto), contra **3,5%** para remessas comuns de disponibilidade.
  - **Reunião de 26/jun, Base Legal e Resposta Oficial via LAI (`E-05.3`–`E-05.5`):** Em 26/jun o BCB manteve a suspensão das importações via fundos mas liberou a arbitragem dentro dos livros de ordens das exchanges. Em resposta escrita de LAI ao Instituto Live Mercado (`E-05.3`, `E-05.4`), o BCB confirmou (sob a supervisão cambial da `Lei nº 14.286/2021` — Novo Marco Cambial, `Lei nº 14.478/2022` — Marco Legal dos Criptoativos, e a finalidade de investimento de carteira da `Resolução CVM nº 175`): *"os fundos não podem atuar como intermediadores de ativos virtuais e, assim, as operações de câmbio de importação de ativos virtuais por eles realizadas carecem do atributo de licitude"*.
- **2. A Evidência Macroeconômica nas Estatísticas do BCB (`P3-10`, `D-16` `SGS 29644`, `F-024`):**
  - Na série oficial do BCB (*Tabela 11 — Outros investimentos, criptoativos com passivo correspondente*), as aquisições líquidas de stablecoins no exterior caíram de **US$ 2.542 milhões (jun/2026) para US$ 572 milhões (jul/2026): queda de −77,5% (≈ −78%)**.
  - **Teste pré-registrado (`T1`):** Variação logarítmica de $-1,49$ ($p = 0,022$ contra as 91 variações mensais desde 2019; $p = 0,046$ contra a média de jan–mai em `T1b`), a maior queda percentual desde que a série superou US$ 100 mi/mês em 2021. **Preço subindo (11 $\to$ 43 $\to$ 81 bps) com quantidade importada caindo (−78%) é a assinatura clássica consistente com um choque de oferta.**
  - **Teste do recuo (`T2`):** Em ago–set/2026, as compras externas permaneceram em **32% do nível de jan–mai** (US$ 702 mi e US$ 843 mi) enquanto o prêmio recuou para 33 e 23 bps. Logo, **o recuo de 22/jul não veio da reabertura desse canal de importação** (*"parcial/inconclusivo"* pela regra pré-registrada).
  - **Ressalva explícita:** A série `SGS 29644` agrega todas as compras líquidas de residentes (não apenas fundos), e em 01/jul/2026 o BCB também editou a **Resolução BCB nº 580** (`E-10`, enquadrando SPSAVs como Tipo 3 a partir de jan/2027); dados mensais agregados não separam o ofício de junho de outros fatores de julho.

| Mês de 2026 (`SGS 29644` & `P1-02`) | Jan | Fev | Mar | Abr | Mai | Jun | **Jul (Pós-Ofício)** | Ago | Set |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| **Compras de Stablecoins no Exterior (US$ mi)** | 2.375 | 2.140 | 2.282 | 2.709 | 2.632 | 2.542 | **572 (−78%)** | 702 | 843 |
| **Prêmio Médio Mensal USDT/PTAX (bps)** | 8 | 5 | 5 | 5 | 11 | 43 | **81** | 33 | 23 |

#### Notas do Orador & Rastreabilidade
- **Notas:** "Qual foi a porta que fechou em 23 de junho e como sabemos que ela realmente fechou? Primeiro, abrimos dez fontes contemporâneas: tanto o Cointelegraph em 24 de junho quanto a Exame em 25 de junho tiveram acesso à notificação enviada a 13 bancos, e o próprio BCB confirmou por escrito via LAI que a importação de criptoativos por fundos carece de licitude. Segundo, fomos às estatísticas de balanço de pagamentos do próprio Banco Central: em julho de 2026, a compra líquida de stablecoins no exterior despencou 78%, saindo de US$ 2,54 bilhões para US$ 572 milhões, enquanto o prêmio explodiu. Preço subindo e quantidade caindo é a assinatura clássica consistente com o fechamento de um canal de oferta."
- **Rastreabilidade:** Seção 5 de `notebooks/p5_07_story.ipynb`; `P3-14` (`F-023`), `P3-10` (`F-024`), `docs/sources.md` (`D-16`, `E-05.1`..`E-05.10`, `E-10`), `scripts/p3_10_imports.py`, `scripts/p3_14_press_check.py`.

---

<!-- SLIDE 6 -->
## Slide 6 — Só o Ofício de Efeito Imediato Moveu o Prêmio: 8 Regras e 13 Eventos vs 1.073 Datas Limpas

### As 7 regras publicadas no DOU com aviso prévio (1 a 175 dias) ficaram dentro da faixa normal; só o ofício de supervisão (não publicado no DOU e de efeito imediato) saiu dela (+93,9 bps, $p = 0,0009$)

#### Layout Visual & Figuras
- **Imagens:** `results/figures/P3-12_rules.png` (As 8 regras brasileiras ordenadas por forma de emissão e aviso prévio contra a faixa de 95% das datas comuns, `F-026`) e `results/figures/P2-03_placebo_dist.png` (Distribuição de placebos, `F-016`).
- **Legenda (10 segundos):** Testamos as 8 regras brasileiras datadas (e 5 eventos de mercado): decretos e resoluções publicadas no DOU com semanas ou meses de transição ficaram dentro da faixa das datas comuns ($-35,0\text{ a }+37,6\text{ bps}$); só o ofício de supervisão de 23/jun (não publicado no DOU e de efeito imediato) saiu dela (+93,9 bps, $p = 0,0009$).

#### Pontos Principais (pt-BR)
- **Qual Regra Move o Preço? (`P2-03`, `P3-12`, `F-016`, `F-026`):**
  - Avaliamos a mudança de média nos 20 dias úteis PTAX após contra os 20 dias antes ($[+1, +20]$ vs $[-20, -1]$) usando **exclusivamente $p$-valores empíricos contra todas as 1.073 datas ordinárias limpas** (e contra a banda de 95% dos 200 sorteios placebo: **$-35,0\text{ a }+37,6\text{ bps}$**).
  - **Divisão limpa nas 8 regras regulatórias/tributárias (`F-026`):**
    - **O único ato de supervisão não publicado no DOU e de efeito imediato (`E-05`, 0 dias de aviso):** moveu o prêmio em **+93,9 bps**, superando todas as 1.073 datas limpas ($p = 1/1074 = 0,0009 \approx 0,001$).
    - **As 7 regras publicadas (1 a 175 dias de aviso prévio):** o decreto presidencial do IOF (`E-01`), sua suspensão pelo Congresso/STF (`E-01b`), as quatro resoluções do BCB (`E-02`, `E-04`, `E-06a`, `E-06b`) e a minuta de IOF em cripto (`E-03`) permaneceram integralmente dentro da faixa das datas comuns ($-24,9\text{ a }+15,4\text{ bps}$, $p_{\text{placebo}} \ge 0,15$).
  - **Para o regulador:** normas estruturais publicadas com janela de adaptação permitem reajuste ordenado de rotas sem estresse de liquidez; o prêmio revela imediatamente quando uma intervenção atinge o canal operacional mais barato em uso.
- **Duas Ressalvas Essenciais Declaradas no Gráfico (`F-026`):**
  1. **Forma e conteúdo mudam juntos:** O ofício de 23/jun foi simultaneamente a única regra não publicada no DOU/imediata *e* a única que fechou o canal de importação dos fundos (`F-024`); não é possível separar estatisticamente os dois atributos com $N=1$ regra tratada.
  2. **Limite de detecção (~35 bps):** Como datas comuns oscilam entre $-35\text{ e }+38\text{ bps}$, *"sem efeito"* significa **sem efeito acima de ~35 bps**, não prova de efeito zero.

| Regra Avaliada (`P3-12_rules.csv` / `P2-03`) | Forma de Emissão | Aviso Prévio | Mudança no Anúncio (bps, $p$) | Mudança na Vigência (bps, $p$) |
|---|---|---:|---|---|
| **E-01** Decreto IOF-Câmbio 3,5% (22/05/2025) | Decreto presidencial (público) | 1 dia | +13,2 ($p = 0,38$) | +15,4 ($p = 0,31$) |
| **E-01b** Suspensão pelo Congresso e STF (27/06/2025) | Decreto legislativo / liminar STF | 7 dias | −23,9 ($p = 0,16$) | −24,9 ($p = 0,15$) |
| **E-02** Res. BCB 519–521: marco SPSAV (10/11/2025) | Resolução do BCB (pública) | 84 dias | −3,8 ($p = 0,75$) | −4,3 ($p = 0,72$) |
| **E-04** Res. BCB 521 art. 4º: reporte (04/05/2026) | Resolução do BCB (pública) | 175 dias | — (junto com E-02) | +7,2 ($p = 0,61$) |
| **E-03** Proposta de IOF sobre cripto (05/02/2026) | Minuta da Fazenda (não editada) | — | −2,1 ($p = 0,84$) | — |
| **E-06a** Res. BCB 561: vedação em eFX (30/04/2026) | Resolução do BCB (pública) | 154 dias | +6,0 ($p = 0,65$) | −5,3 ($p = 0,68$) |
| **E-05 Ofício BCB: câmbio de fundos (23/06/2026)** | **Ofício de supervisão (não publicado no DOU)** | **Imediato (0d)** | — | **+93,9 ($p = 0,0009$)** |
| **E-06b** Res. BCB 584: retenção 24h (07/08/2026) | Resolução do BCB (pública) | 147 dias | −22,0 ($p = 0,19$) | *(vigência 01/01/2027)* |

#### Notas do Orador & Rastreabilidade
- **Notas:** "Testamos as oito regras brasileiras com data. O decreto do IOF, sua suspensão e quatro resoluções do BCB — todas públicas e quase todas com semanas ou meses de antecedência — ficaram dentro da faixa das datas comuns, entre menos 35 e mais 38 pontos-base. Só o ofício de 23 de junho, sigiloso e de efeito imediato sobre o canal dos fundos, saiu dela: mais 94 pontos-base, superando todas as 1.073 datas limpas."
- **Rastreabilidade:** Seção 6 de `notebooks/p5_07_story.ipynb`; `P2-03` (`F-016`), `P3-12` (`F-026`), `scripts/p2_03_events.py`, `scripts/p3_12_rules.py`, `results/tables/P3-12_rules.csv`.

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
  - **Descolamento Agudo (24/jun a 21/jul/2026, 17 dias comuns):** O prêmio no Brasil superou o Brasil Sintético em **+109,3 bps** — subindo para **+116,7 bps** (1º de 5, pré-RMSPE 10,33 bps) quando excluímos o Euro e usamos apenas os 4 emergentes (`TRY`, `ZAR`, `MXN`, `COP`), e **+103,3 bps** em **Diferenças em Diferenças** simples (sem depender de pesos). Nenhuma outra moeda teve movimento semelhante (variações de $-16\text{ a }+24\text{ bps}$).
  - **Limite Estatístico Explícito:** O Brasil ocupa o **1º lugar entre 6 moedas** na razão RMSPE pós/pré (**9,31** vs 0,78 a 1,22 nos doadores). Com 5 doadores, o menor p-valor de permutação possível é **$p = 1/6 \approx 0,167$** (ou $1/7 = 0,143$ incluindo IDR). Portanto, o controle sintético é **evidência complementar** de que o salto não veio de fora; a significância estatística vem do Slide 6 ($p = 0,0009$).
- **E o Bitcoin? Arbitragem Triangular na Binance (`P3-02`, `F-018`):**
  - O prêmio do Bitcoin em reais sobre a PTAX também saltou **+93,8 bps** em 24/jun. Além de o ofício de 23/jun tratar de *"ativos virtuais"* de forma ampla (`E-05.3`), na própria Binance a arbitragem triangular ($\text{USDT/BRL} \times \text{BTC/USDT} = \text{BTC/BRL}$, cujo desvio médio é de apenas **0,36 bps**, dp 1,07) transmite mecanicamente qualquer prêmio do `USDT/BRL` ao `BTC/BRL`, de modo que o teste não permite separar um choque específico em stablecoins de um choque amplo em cripto.

#### Notas do Orador & Rastreabilidade
- **Notas:** "Para descartar um choque global em mercados emergentes, comparamos o Brasil com cinco outras moedas. Enquanto euro, peso mexicano, lira turca, rand e peso colombiano ficaram parados, o Brasil descolou 109 pontos-base do seu gêmeo sintético e 103 pontos-base na diferença em diferenças simples. E por que o Bitcoin subiu os mesmos 93,8 bps? Porque na Binance a arbitragem triangular mantém BTC/BRL colado a USDT/BRL com diferença de menos de meio ponto-base."
- **Rastreabilidade:** Seção 7 de `notebooks/p5_07_story.ipynb`; `F-017`, `F-018`, `L-08`, `scripts/p2_04_synth.py`, `scripts/p3_02_btc.py`.

---

<!-- SLIDE 8 -->
## Slide 8 — Um Pico de Um Mês: Robustez do Salto e o que Não Podemos Afirmar

### O pico agudo é robusto em todas as 22 variantes do USDT/BRL (26 c/ BTC e compostos: +74 a +128 bps); o nível pós-pico (+11 a +19 bps) não se distingue de deriva normal ($p = 0,24$)

#### Layout Visual & Figura
- **Imagem:** `results/figures/P4-01_robustness_forest.png` (*Forest plot* da bateria de especificações testando janelas, definições do prêmio, corretoras, doadores e janelas pós-pico).
- **Legenda (10 segundos):** Qualquer maneira de medir o mês seguinte a 23/jun confirma um salto de +74 a +128 bps (10× a 35× o piso de ruído), mas o nível observado após 22/jul (+11 a +19 bps) ocorre com frequência em datas ordinárias ($p_{\text{placebo}} = 0,24$).

#### Pontos Principais (pt-BR)
- **O Que é Robusto: O Pico de Um Mês (`P4-01`, `F-022`):**
  - Em todas as **22 variantes agudas do USDT/BRL** (e **26 especificações agudas no total**, incluindo Bitcoin +93,8 bps e compostos de 3 corretoras +94,0 e +96,6 bps) — janelas de $\pm 10, \pm 15, \pm 20, \pm 30$ dias, 4 definições de prêmio (PTAX + Binance, fechamento diário 23h59 UTC, cotação direta Coinbase `USDT/USD`, mediana horária), 3 corretoras (Binance +93,9; Foxbit +93,3; MB +94,9 bps) e 6 modelos de controle sintético/DiD — o salto situa-se entre **+73,7 e +128,3 bps** (concentrado entre **+93 e +117 bps**).
- **O Que Não Foi Demonstrado: Um Novo Patamar Permanente (`F-022`):**
  - A partir de 22/jul/2026 o prêmio recuou de 109,1 para 26,8 bps (+11,5 a +19,3 bps acima da janela pré-ofício; +28,2 bps contra o controle sintético).
  - Embora o p-valor paramétrico pareça baixo devido à autocorrelação, o teste honesto de placebos comparando $[+21, +60]$ vs $[-20, -1]$ em todas as 882 datas limpas resulta em **$p_{\text{placebo}} = 0,24$** (dp de 16,5 bps; $p = 0,14$ usando apenas datas de 2025–26).
  - **Conclusão Científica Direta:** O efeito medido do fechamento da porta é **um pico agudo de um mês**. Não reivindicamos um efeito permanente sobre o nível do prêmio.
- **Três Fatos em Aberto que Reportamos com Transparência:**
  1. **O recuo de 22 de julho:** Nenhum evento verificado cai dentro de $\pm 5$ dias úteis de 22/jul (`P2-02`), e as importações de stablecoins no BCB (`F-024`) não voltaram ao nível anterior em ago–set (ficaram em 32%). A arbitragem dentro dos livros de ordens liberada na reunião de 26/jun (`E-05.5`) é uma candidata, mas sua data não coincide com 22/jul.
  2. **O salto de 6× no volume da Foxbit a partir de julho (`F-008`, `P3-10`):** O volume diário nos dias PTAX subiu de 4,3 para 30,7–31,6 milhões de USDT através de **ordens 6× a 8× maiores** (média de 730 para 4.687–6.297 USDT), não de mais negócios. Coincide no tempo com a parceria para clientes da NovaDAX em 07/jul (`M-04`) e com o relançamento da **Foxbit Infra** (liquidez B2B e *market making* próprio integrado a PicPay, 99Pay e Genial) em 18/jul (`M-05`), mas a causa segue aberta.
  3. **Subida prévia desde 25 de maio (`F-014`):** O prêmio já subia levemente (+8 bps) quatro semanas antes de 23/jun (antecipação ou deriva).

#### Notas do Orador & Rastreabilidade
- **Notas:** "Aqui aplicamos nossa regra mais importante: não afirmar mais do que os dados provam. O pico de um mês após 23 de junho passa em todas as 22 verificações de robustez, entre 74 e 128 pontos-base. Já os 11 a 19 pontos-base que restaram depois de 22 de julho têm p-valor de placebo de 0,24 — ou seja, oscilações desse tamanho acontecem sozinhas um quarto das vezes. Portanto, apresentamos como efeito medido apenas o pico de um mês."
- **Rastreabilidade:** Seção 8 de `notebooks/p5_07_story.ipynb`; `F-008`, `F-011`, `F-014`, `F-022`, `F-024`, `M-04`, `M-05`, `scripts/p4_01_robustness.py`.

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
    - **Argentina (`ARS`):** prêmio médio de **+721 bps (7,2%)** em 2025 e **+548 bps (5,5% até 22/jun; +571 bps no acumulado de 2026)**.
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
## Slide 10 — Quanto Custou: R$ 5.052 por US$ 100 Mil e R$ 106–145 Milhões Transferidos

### O ofício adicionou R$ 5.052 a cada US$ 100 mil (`F-015`) e transferiu R$ 106 milhões na Binance (R$ 145 milhões em 3 corretoras) em quatro semanas (`F-025`)

#### Layout Visual & Figura
- **Imagem:** `results/figures/P3-01_route_costs.png` (Gráfico horizontal neutro de fricções de transação por regime histórico da rota USDT, cenários regulatórios e referenciais bancários com fontes primárias).
- **Legenda (10 segundos):** Nas quatro semanas após o ofício, quem comprou dólar digital pagou **R$ 5.052 a mais por US$ 100 mil** (+93,9 bps) — uma transferência agregada de **R$ 106,1 milhões na Binance** (**R$ 145,3 milhões em 3 corretoras**, equivalente tarifário de ~0,95%, $p = 0,005$) dos compradores para quem ainda conseguia ofertar USDT.

#### Pontos Principais (pt-BR)
- **1. Quanto Dinheiro o Pico Moveu e Para Quem (`P3-11`, `F-025` + `P3-01`, `F-015`):**
  - **Por lote institucional de US$ 100.000 (base R$ 538.000, `F-015`):** o salto de **+93,9 bps** custou **+R$ 5.052,36** (US$ 939,10) durante o pico de 20 dias úteis (e até **R$ 9.682,66** no pico de 48h de 24–25/jun). Após 22/jul (+11,5 bps = R$ 621,00), a diferença não se distingue de ruído ($p = 0,24$).
  - **No mercado agregado em 4 semanas (24/jun a 21/jul/2026, `F-025`):** foram negociados **R$ 11,18 bilhões** em `USDT/BRL` na Binance (**R$ 15,76 bilhões** somando Binance, Foxbit e Mercado Bitcoin). Os compradores pagaram em média **94,9 bps** acima do nível pré-ofício, transferindo **R$ 106,1 milhões na Binance** (**R$ 145,3 milhões nas três corretoras**; faixa de robustez de R$ 106,1 a R$ 122,2 mi na Binance).
  - **Equivalente tarifário de uma cota (`F-025`):** O ofício funcionou como uma restrição quantitativa com tarifa equivalente de **~0,95%** (~um quarto do diferencial de 3,50% de IOF que motivava a rota dos fundos, `E-05.10`), mas **essa renda não foi arrecadada pelo Tesouro**: foi capturada por quem ainda conseguia trazer ou ofertar stablecoins no país. Nenhum dos 194 meses placebo moveu mais de R$ 35,5 mi ($k = 0, p = 0,005$). **Ressalva:** trata-se de uma **transferência** entre compradores e vendedores (não uma perda de bem-estar medida) e não inclui mesas OTC nem outras corretoras.
- **2. Contexto Institucional: Fricções por Canal e Cenários Regulatórios (Fontes Primárias Abertas `R-01`..`R-07`):**
  *(Nota para decisão da equipe no freeze: manter este bloco resumido no slide [Opção C] ou remeter à tabela completa no Anexo B.5 [Opção A])*
  - **Parâmetros Bancários com Fonte Primária (`R-01`, `R-01b`, `R-02`):** Spread corporativo mediano do BCB para contratos $>$ US$ 55,6 mil = **20,0 bps** (*Estudo Especial BCB nº 48/2019*, `R-01`; teto conservador de 50 bps adiciona R$ 1.614); tarifa SWIFT = **US$ 25 (2,5 bps)** (*Tabela de Tarifas PJ Banco do Brasil*, `R-01b`); IOF legal (`R-02`): **0%** na importação de bens (**22,5 bps = R$ 1.211**), **1,10%** em investimento ou disponibilidade pré-23/mai/2025 (**132,5 bps = R$ 7.129**), e **3,50%** em disponibilidade geral pós-23/mai/2025 (**372,5 bps = R$ 20.041**).
  - **Corretoras Locais e Níveis VIP (`R-04`..`R-06`):** Na Foxbit, taxas VIP 6–7 para volumes de R$ 5M–25M custam **8,0 bps taker** (total **35,0 bps = R$ 1.883** no Regime 6). No Mercado Bitcoin, a taxa VIP de **6,0 bps** é estritamente **passiva (*maker*)** acima de R$ 10M; ordens a mercado ativas (*taker*) pagam **60,0 bps** (**87,0 bps total = R$ 4.680**).
  - **Cenário S1 (Proposta IOF 3,5% em Cripto, `E-03`):** elevaria a rota USDT para **386,9 bps (R$ 20.815)**.
  - **Cenário S2 (Retenção de 24h, Res. BCB 584/2026, `R-07`, `F-027`):** para uma saída em USDT, 1 dia custa **~9,1 bps** (5,5 bps de Selic + 3,7 bps de risco `USDT/USD`, `F-027`); com hedge CIP de 1 dia útil em BRL (**2,5 bps**), soma **39,4 bps (R$ 2.120)** (e só haveria risco PTAX de 130,5 bps se o agente ficasse exposto em reais).
  - **Não-Equivalência Jurídica e Operacional (`docs/02-dolar-cripto.md` §10):** O contrato bancário entrega USD em conta no exterior liquidado no Sistema de Câmbio do BCB; a rota USDT entrega um token privado em blockchain e a diferença frente ao câmbio de disponibilidade advém do enquadramento tributário distinto no Decreto nº 6.306/2007 (`R-02`), não de "economia" operacional.

| Medida / Canal / Cenário (`P3-01` & `P3-11`) | Volume / Base | Prêmio / Tarifa Eq. (bps) | Total (bps) | Custo por US$ 100k (R$) | Transferência em 4 Semanas (R$ mi) |
|---|---|---|---|---:|---:|
| **Custo do Ofício: Pico 20d (Binance `VIP0`)** | R$ 11,18 bi | **+93,9 (94,9 pond.)** | **+93,9** | **+R$ 5.052,36** | **R$ 106,1 mi ($p = 0,005$)** |
| **Custo do Ofício: Pico 20d (3 Corretoras)** | R$ 15,76 bi | **+92,2 (pond.)** | **+92,2** | — | **R$ 145,3 mi** |
| **Custo do Ofício: Pós-Pico (22/jul–out, $p=0,24$)** | R$ 16,15 bi | +11,5 (+19,1 pond.) | +11,5 | +R$ 621,00 (ruído) | R$ 30,9 mi (ruído) |
| **USDT Regime 4 (Base Pré-Ofício, jul/25–jun/26)** | US$ 100 mil | 9,3 | 19,4 | R$ 1.043,72 | *(Média 20d pré = 15,2 bps; salto +93,9)* |
| **USDT Regime 5 (Choque Agudo, 24/jun–21/jul/26)** | US$ 100 mil | 109,1 | 119,2 | R$ 6.412,96 | *(Salto de regimes Bai-Perron = +99,8 bps)* |
| **Banco: Importação de Bens (IOF 0%, `R-01`/`R-02`)** | US$ 100 mil | 0,0 (spread 20,0) | 22,5 | R$ 1.210,50 | — |
| **Banco: Investimento / Disp. Pré-Mai/25 (IOF 1,1%)** | US$ 100 mil | 0,0 (spread 20,0) | 132,5 | R$ 7.128,50 | — |
| **Banco: Disponibilidade Pós-Mai/25 (IOF 3,5%)** | US$ 100 mil | 0,0 (spread 20,0) | 372,5 | R$ 20.040,50 | — |

#### Notas do Orador & Rastreabilidade
- **Notas:** "Traduzindo pontos-base em dinheiro: para quem comprava um lote de US$ 100 mil em USDT, o mês seguinte ao ofício custou R$ 5.052 a mais. No mercado todo, sobre os R$ 11,2 bilhões negociados na Binance em quatro semanas — ou R$ 15,8 bilhões nas três corretoras — quem comprou dólar digital pagou R$ 106 milhões a mais na Binance, ou R$ 145 milhões nas três exchanges. O ofício funcionou como uma tarifa de quase 1%, mas esse valor não foi arrecadado pelo governo: foi transferido dos compradores para quem ainda conseguia trazer stablecoins ao país."
- **Rastreabilidade:** Seção 10 de `notebooks/p5_07_story.ipynb`; `P3-01` (`F-015`), `P3-11` (`F-025`), `R-01`..`R-07`, `scripts/p3_01_costs.py`, `scripts/p3_11_money.py`.

---

<!-- SLIDE 11 -->
## Slide 11 — Do Lado do Dólar: Quando o Resgate Fecha (Fim de Semana do SVB e 11 Casos)

### O USDC fechou a US$ 0,863 enquanto os bancos estavam fechados e voltou a US$ 0,989 uma hora após a garantia de domingo; 11 descolamentos na Binance (12 linhas com o caso SVB)

#### Layout Visual & Figuras
- **Imagens:** `results/figures/P3-04_svb_weekend.png` (Série horária do USDC/USD na Bitstamp no fim de semana do SVB com marcação do anúncio conjunto às 22h15 UTC) e `results/figures/P3-04_depeg_cases.png` (Profundidade e duração dos 11 casos).
- **Legenda (10 segundos):** O mesmo mecanismo aparece no próprio dólar: sem resgate bancário no fim de semana do SVB, o USDC caiu a US$ 0,863 (mínima intra-hora US$ 0,805), mas voltou a US$ 0,989 45 minutos após o comunicado do Fed/Tesouro/FDIC no domingo à noite, *antes* da reabertura dos bancos.
- **Nota Metodológica de Contagem:** A triagem sistemática na Binance (`P1-07` v2) identificou **11 episódios** abaixo de US$ 1,00 (9 excluindo as 2 fases de pré-deslistagem do USDP, e 8 recuperados excluindo o colapso do UST). Ao adicionar o episódio canônico do fim de semana do SVB na Bitstamp (`USDC/USD`), a tabela descritiva totaliza **12 linhas de análise** (`F-019`), das quais 9 são episódios recuperados sem deslistagem.

#### Pontos Principais (pt-BR)
- **O Fim de Semana do Silicon Valley Bank (10 a 13/mar/2023; Bitstamp `USDC/USD` 1h, `P1-07`, `P3-04`, `F-019`):**
  - Com os bancos americanos fechados de sexta-feira 16h a segunda-feira 9h30 (NY) e US$ 3,3 bilhões da Circle retidos no SVB, o canal primário de resgate 1:1 estava fechado.
  - O menor fechamento horário do USDC foi **US$ 0,863** no sábado às 07h UTC (mínima intra-horária de **US$ 0,805**).
  - No domingo às **22h15 UTC (`D-13`)**, Tesouro, Federal Reserve e FDIC anunciaram garantia integral aos depositantes do SVB. Às **23h00 UTC** — **antes de os bancos reabrirem** — os arbitradores já haviam levado o USDC de volta a **US$ 0,989** (e a US$ 0,999 na abertura de segunda-feira). O que restaura a paridade é a **expectativa crível de acesso ao canal de resgate**.
- **Os 11 Descolamentos Confirmados Abaixo de US$ 1,00 na Binance + Caso SVB Bitstamp (`F-013`, `F-019`, `P3-09`):**
  - Como os episódios recuperados sem deslistagem ($N=9$) e as quedas na Binance ($N=11$) ficam estritamente abaixo do piso pré-comprometido ($N \ge 12$ em `docs/01-depeg-recovery.md` §5), **não estimamos curvas de sobrevivência de Kaplan-Meier** e apresentamos a tabela descritiva de casos com fontes primárias e de imprensa abertas (`DP-01` a `DP-10` em `docs/sources.md`):

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
## Slide 12 — A Solução Prática: O Monitor do Dólar Digital e Previsão Datada para 01/jan/2027

### Calibrado apenas em 2020–2025, nosso alarme CUSUM dispara no próprio dia 24/jun/2026 (`F-014`) e já tem uma previsão falsificável registrada para a Res. BCB 584 (`F-027`)

#### Layout Visual & Figura
- **Imagem:** `results/figures/P3-03_monitor.png` (Painel superior: prêmio diário com banda de ruído e disparos de alarme; painel inferior: estatística CUSUM sequencial vs limiar calibrado no treino).
- **Legenda (10 segundos):** Usando apenas dados passados (treino 2020–2025, orçamento de até 2 alarmes/ano), o monitor detecta o salto de 24/jun/2026 no próprio dia (atraso zero) com metade dos falsos alarmes da regra simples (`F-014`), e deixamos registrada em Git (`393a14a`) uma previsão falsificável para a entrada em vigor da retenção de 24h em 01/01/2027 (`F-027`).

#### Pontos Principais (pt-BR)
- **1. Desenho Sem Olhar para o Futuro (*No Look-Ahead*, `P3-03`, `F-014`):**
  - Especificação registrada no Git antes do backtest (`tasks/P3-03-monitor.md`). Limiar $h = 24,5$ calibrado exclusivamente em **2020–2025** (orçamento máximo de 2 alarmes/ano $\to$ 9 alarmes em 5 anos = 1,8/ano) e congelado para o teste fora da amostra em **2026**.
  - **Desempenho em 2026:** Disparo no **próprio dia 24/jun/2026 (atraso = 0 dias úteis)**; detecção do recuo de 22/jul em **11 dias úteis PTAX** (06/ago); e apenas **2 outros alarmes** em 10 meses de 2026 (2,4/ano), contra **4 outros alarmes** (4,8/ano) da regra simples de médias móveis (MM 5d vs 60d).

| Regra de Monitoramento (`P3-03_backtest.csv`) | Parâmetro Calibrado (2020–2025) | Alarmes no Treino (2020–2025) | Atraso no Salto de 24/jun/2026 | Atraso no Recuo de 22/jul/2026 | Outros Alarmes no Teste (2026) |
|---|---|---|---|---|---|
| **Monitor CUSUM (Nossa Solução)** | **$h = 24,5$** | **9 (1,8 / ano)** | **0 dias úteis (24/jun)** | **11 dias úteis (06/ago)** | **2 (2,4 / ano)** |
| Linha de Base Simples (MM 5d vs 60d) | $c = 7,25$ | 10 (2,0 / ano) | 0 dias úteis (24/jun) | 12 dias úteis (07/ago) | 4 (4,8 / ano) |

- **2. Uma Previsão Datada que a Banca Pode Conferir em 2027 (`P3-13`, `F-027`, commit `393a14a` de 02/11/2026):**
  - Em **1º/01/2027** entra em vigor a retenção cautelar de até 24 horas da **Resolução BCB nº 584/2026** (`E-06b`, art. 2º-B da Res. 142).
  - Pela letra da norma, ela atrasa **apenas as saídas** de ativos virtuais ($\ge$ US$ 10 mil para o exterior ou carteiras autohospedadas), **não as entradas** que formam a oferta de USDT no Brasil. Além disso, quem sofre a retenção já detém USDT durante essas 24 horas: o custo de 1 dia útil é de apenas **~9,1 bps** (**5,5 bps** de financiamento à Selic de 13,75% a.a., `D-17`, mais **3,7 bps** de risco diário a 95% do `USDT/USD`), um quarto do limite de detecção.
  - **Previsão registrada (`results/tables/P3-13_prediction.md`):** No primeiro dia PTAX de 2027 (**04/01/2027**), a mudança antes/depois (20 dias úteis PTAX pós vs 20 pré) **permanecerá dentro da faixa das datas comuns ($-35,0\text{ a }+37,6\text{ bps}$)**, sem disparo de alta no monitor. **O que provaria que estamos errados:** variação fora de $[-35,0; +37,6]\text{ bps}$ com $p_{\text{placebo}} < 0,05$. *(Ressalva: a Res. BCB 580 também entra em vigor na mesma data).*

#### Notas do Orador & Rastreabilidade
- **Notas:** "Como solução prática, construímos o Monitor do Dólar Digital em código aberto. Calibrado apenas até 2025, ele disparou o alerta no próprio dia 24 de junho com metade dos falsos alarmes de uma regra simples. E fomos além: deixamos registrada no Git uma previsão que a banca poderá conferir em janeiro de 2027. Quando a retenção de 24 horas da Resolução 584 entrar em vigor em 1º de janeiro, ela atrasará apenas saídas e custará cerca de 9 pontos-base a quem já tem USDT; prevemos que o prêmio não mudará de forma detectável, ficando entre menos 35 e mais 38 pontos-base."
- **Rastreabilidade:** Seção 12 de `notebooks/p5_07_story.ipynb`; `P3-03` (`F-014`), `P3-13` (`F-027`, commit `393a14a`), `D-17`, `scripts/p3_03_monitor.py`, `scripts/p3_13_prediction.py`, `results/tables/P3-13_prediction.md`.

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
| Spread bruto DeFi tratado como puro risco de crédito | **Decomposição explícita de fricções, impostos e subsídios** (53,6% do spread do Compound V3 em 2025 era token `COMP`) | `F-015`, `F-020`, `F-025` |
| Brasil aparecia apenas na introdução; hiperparâmetros livres | **O mercado brasileiro é a pergunta central**; hipóteses, especificações e previsões registradas no Git antes dos testes | `P1-02`, `P2-02`, `P3-10`, `P3-13` |

#### Notas do Orador & Rastreabilidade
- **Notas:** "No ano passado ficamos em 3º lugar neste Datathon. Nossa primeira tarefa neste ano foi auditar criticamente aquele trabalho. Descobrimos duas coisas: nosso modelo complexo perdia para uma previsão ingênua de que amanhã é igual a hoje, e 53,6% do spread do Compound sobre o SOFR era subsídio promocional em tokens COMP. Em 2026 corrigimos cada um desses pontos: linha de base obrigatória, pré-registro no Git e identificação econômica limpa no Brasil."
- **Rastreabilidade:** Seção 13 de `notebooks/p5_07_story.ipynb`; `F-005`, `F-020`, `D-06`, `D-14`, `D-15`, `scripts/p3_08_subsidy.py`.

---

<!-- SLIDE 14 -->
## Slide 14 — O que os Testes Mostraram, Implicações e Limitações

### O fechamento do canal gerou um pico robusto de um mês (+94 bps = R$ 5 mil/US$ 100k; R$ 106–145 mi transferidos); efeito duradouro não foi demonstrado

#### Layout Visual & Placar Final
- **Tabela-Síntese:** Placar das hipóteses pré-comprometidas ($H_1, H_2, H_3, H_0$) e das quatro respostas práticas (`docs/06-so-what.md`) lado a lado com as limitações metodológicas explícitas.
- **Legenda (10 segundos):** Confirmamos um salto agudo de um mês após 23/jun/2026 (+93,9 bps, queda de 78% nas compras externas no BCB e R$ 106–145 milhões transferidos), sem efeito duradouro demonstrado ($p = 0,24$), e entregamos um monitor diário com previsão falsificável para janeiro de 2027.

#### Pontos Principais (pt-BR)
- **1. Placar das Hipóteses e Respostas Práticas (`notebooks/p5_07_story.ipynb` & `docs/06-so-what.md`):**

| Hipótese / Dimensão | Veredito Empírico | Evidência que Sustenta o Veredito |
|---|---|---|
| **$H_1$ (Canal Fechado)** | **Sustentada para um pico de 1 mês** (+93,9 bps, $p = 0,0009$; mesmo salto em 3 corretoras; +109,3 bps vs Brasil Sintético; queda de −78% nas compras externas de stablecoins no BCB em jul/2026, $p = 0,022$). **Não demonstrada** para efeito duradouro ($p_{\text{placebo}} = 0,24$) | `F-009`, `F-011`, `F-016`, `F-017`, `F-022`, `F-024` |
| **$H_2$ (Quais Regras Importam)** | **Consistente:** as 7 regras publicadas com aviso prévio (1–175 dias) ficaram dentro da faixa das datas comuns ($-35\text{ a }+38\text{ bps}$); só o ofício sigiloso e imediato moveu o prêmio | `F-016`, `F-026` |
| **$H_3$ (Repasse Parcial do IOF)** | **Consistente:** variação de +13,2 a +15,4 bps ($p_{\text{placebo}} = 0,31\text{ a }0,38$, não anômala) frente a um aumento tributário de +240 bps no câmbio | `F-016`, `F-026` |
| **$H_0$ (Corretora / Real / USDT)** | **Rejeitada** para o salto de 24 de junho de 2026 | `F-009`, `F-023` |
| **Impacto Financeiro e Previsão** | **R$ 5.052 / US$ 100k** e **R$ 106,1 mi (Binance) a R$ 145,3 mi (3 exchanges)** transferidos em 4 semanas ($p = 0,005$). Previsão registrada (`393a14a`): retenção de 24h da Res. 584 em 01/01/2027 não moverá o prêmio fora de $[-35, +38]\text{ bps}$ | `F-014`, `F-015`, `F-025`, `F-027` |

- **2. Implicações Regulatórias e Desenho de Mercado (`docs/06-so-what.md`):**
  - **Supervisão Cambial e Previsibilidade:** O mercado cripto brasileiro reage com fricções agudas de liquidez quando canais de acesso são fechados sem janela de adaptação, enquanto normas com prazos de transição mantêm o prêmio estável no ruído ordinário.
  - **Ecossistema Drex e Pontes Institucionais:** A criação de canais regulados e programáveis de liquidez atacadista (como os pilotos de interoperabilidade internacional do Drex e soluções institucionais como Ripple ODL / RLUSD) reduz o custo de fricção cambial para empresas e investidores sem criar brechas de arbitragem regulatória.

- **3. Limitações que Declaramos no Slide (Seção 15 do Protótipo):**
  1. **Texto integral do ofício de 23/jun não foi visto:** temos dois veículos que viram a notificação/trecho em 24–25/jun (`E-05.1`, `E-05.2`) e a resposta escrita do BCB via LAI (`E-05.3`, `E-05.4`, `F-023`), mas o ofício não foi publicado no DOU.
  2. **Apenas o pico de um mês é medido:** o recuo a partir de 22/jul não possui evento em $\pm 5$ dias (`P2-02`), não veio da retomada das importações no BCB (`F-024`, que ficaram em 32% em ago–set), e o nível pós-pico não se distingue de deriva normal ($p = 0,24$).
  3. **Forma vs conteúdo e Res. BCB 580:** o ofício foi a única regra sigilosa/imediata e a única a fechar o canal dos fundos (`F-026`); na queda de julho nas estatísticas do BCB (`F-024`), dados mensais não separam o ofício de 23/jun da Res. BCB 580 de 01/jul (`E-10`).
  4. **Transferência, não perda de bem-estar:** os R$ 106–145 milhões (`F-025`) medem transferência bruta nas exchanges analisadas (sem OTC/P2P), não peso morto econômico.
  5. **Amostra internacional curta e histórico longo na Binance:** o controle sintético tem 5 doadores ($p \ge 1/6 \approx 0,167$), e a série desde 2020 vem da Binance.

#### Notas do Orador & Rastreabilidade
- **Notas:** "Concluímos respondendo à nossa pergunta com total transparência sobre o que sabemos e o que não sabemos: fechar a porta em 23 de junho derrubou em 78% as compras externas de stablecoins medidas pelo BCB e produziu um salto de 94 pontos-base — R$ 5 mil por cada US$ 100 mil, ou R$ 106 a 145 milhões transferidos em quatro semanas — que bateu todas as 1.073 datas ordinárias do histórico. E deixamos nosso monitor aberto com uma previsão datada no Git para 1º de janeiro de 2027. Muito obrigado."
- **Rastreabilidade:** Seções 14 e 15 de `notebooks/p5_07_story.ipynb`; `docs/06-so-what.md`; `F-001`..`F-027`; `prompt.md` §5 e §8.

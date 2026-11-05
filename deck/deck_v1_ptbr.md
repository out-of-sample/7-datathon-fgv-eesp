# Quanto Custa Fechar a Porta?
## O prêmio do dólar digital no Brasil e os limites à arbitragem

**7º Datathon de Moedas Digitais FGV EESP (novembro de 2026)**  
**Equipe Out of Sample:** Renzo (CS 1), Nattan (CS 2), Jonathan (CS 3), Felipe (Economista)  
**Organização:** FGV EESP, Centro de Estudos em Finanças Digitais FGV, com apoio de FGV/Ripple (UBRI) e USP-UBRI  

---

### Sumário (10 slides, ~60 s cada; versão de 2/nov/2026)
1. **Quanto custa fechar a porta?** — pergunta e resposta
2. **A porta que fechou: o ofício de 23/jun** — o canal, o ofício, a linha do tempo
3. **Dados e método** — dados, desenho, o que nos desmentiria, transparência e "Lições de 2025"
4. **O salto** — +93,9 bps, três corretoras, quebra encontrada às cegas, comparação com datas comuns
5. **Entre as oito regras testadas, só o ofício saiu da faixa comum** — regras publicadas vs ofício; Res. 574
6. **Não foi o real, nem o USDT, nem o mundo** — controle sintético, PTAX, USDT/USD, bitcoin
7. **O mecanismo: as importações caíram** — −78% nas compras de stablecoins no exterior
8. **Robusto, mas de um mês** — 22 variantes; o que não mostramos
9. **Quanto custou e para quem** — R$ 106 milhões; por que +94 e não +350 bps
10. **Implicações, previsão e limites** — previsão datada para 1/jan/2027

**Ordem de corte se o tempo for curto:** reduzir os slides 6 e 8 a uma frase cada; depois o 7.
Perguntas difíceis e respostas de 20 segundos: `deck/qa_ptbr.md`. Material movido para o anexo: Anexo F de
`deck/annex_v1_ptbr.md`. O que mudou em relação à versão de 14 slides: `docs/deck-changes-2026-11-02.md`.

---

<!-- SLIDE 1 -->
## Slide 1 — Quanto custa fechar a porta?

### Quando o Banco Central fechou um canal de entrada de dólares digitais, o prêmio do USDT sobre o dólar oficial subiu +94 bps por um mês: R$ 4.842 a mais a cada US$ 100 mil

#### Layout Visual & Figura
- **Figura:** nenhuma; o número da resposta em destaque.
- **Legenda (10 segundos):** Quanto a mais os brasileiros pagaram por um dólar digital quando uma regra fechou um canal de arbitragem com o câmbio oficial? No mês seguinte ao ofício do BCB de 23/jun/2026, +93,9 bps: R$ 4.842 a cada US$ 100 mil, à PTAX de cada dia.

#### Pontos Principais (pt-BR)
- **A pergunta:** quanto a mais os brasileiros pagam por um dólar digital (USDT comprado com reais) do que pelo dólar oficial (PTAX) quando uma regra fecha um canal de arbitragem entre os dois mercados?
- **A resposta:** no mês seguinte ao ofício do Banco Central de 23/jun/2026, o prêmio do USDT sobre a PTAX subiu **+93,9 bps** (de 15,2 para 109,1 bps): **R$ 4.842 a mais a cada US$ 100 mil**, em média, à PTAX de cada dia, durante um mês.
- **Por que importa:** de janeiro a maio de 2026, residentes no Brasil compraram em média **US$ 2,4 bilhões por mês** em stablecoins no exterior (estatísticas do BCB).
- *Fontes:* F-015, F-016, F-024.

#### Notas do Orador & Rastreabilidade
- **Notas:** "Nossa pergunta é simples: quanto custa fechar a porta? Quando uma regra fecha um dos canais que mantêm o dólar digital colado ao dólar oficial, quanto a mais os brasileiros pagam? Em 23 de junho de 2026, o Banco Central enviou um ofício que interrompeu de imediato um desses canais. No mês seguinte, o prêmio do USDT sobre a PTAX subiu 94 pontos-base: para quem comprava 100 mil dólares em USDT, cerca de 5 mil reais a mais. E não é um mercado pequeno: até maio, residentes compravam cerca de 2,4 bilhões de dólares por mês em stablecoins no exterior. A seguir mostramos qual porta fechou, como medimos o salto, por que não foi outra coisa, quanto custou e o que não conseguimos mostrar."
- **Rastreabilidade:** `F-015` (R$ 4.842 = média, nos 20 dias PTAX de 24/jun a 21/jul, do excesso de prêmio de cada dia × US$ 100 mil × PTAX do dia, média R$ 5,14; até 3/nov o deck usava R$ 5.052, convertido a uma cotação Binance de R$ 5,38 que não é PTAX; re-checagem da conversão por um colega pendente), `F-016` (+93,9 bps), `F-024` (média jan–mai/2026 de US$ 2.428 mi, `D-16`).

---

<!-- SLIDE 2 -->
## Slide 2 — A porta que fechou: o ofício de 23/jun

### Um ofício de circulação inicialmente restrita e efeito imediato interrompeu o câmbio que fundos usavam para trazer cripto ao Brasil com IOF zero; no dia seguinte, operadores ouvidos pela imprensa já ligavam a alta de preço a ele

#### Layout Visual & Figura
- **Figura (a desenhar, `P5-02`):** linha do tempo das medidas de 2025–2026 com o ofício marcado e um diagrama do canal (fundo → câmbio com IOF 0% → compra de cripto no exterior → venda a corretoras no Brasil). Até lá, a tabela abaixo.
- **Legenda (10 segundos):** O USDT em reais fica perto do dólar oficial enquanto alguém consegue comprar dólar barato de um lado e vender USDT do outro. Em 23/jun/2026 o BCB fechou um desses canais, sem aviso e sem publicação.

#### Pontos Principais (pt-BR)
- **A paridade:** um USDT comprado com reais deveria custar o dólar oficial (PTAX) vezes o preço do USDT em dólar. Quem compra barato num mercado e vende caro no outro mantém os dois próximos; o prêmio mede a distância entre eles.
- **O canal:** fundos de investimento compravam cripto no exterior com câmbio de IOF zero (Decreto 6.306/2007, art. 15-B, III) e, segundo a ABToken, "usavam contas em bancos para comprarem criptomoedas no exterior e depois venderem esses ativos para as corretoras". A compra comum de moeda estrangeira paga 3,5%.
- **O ofício:** enviado a bancos, corretoras de câmbio, empresas cripto e fundos, determinou a "imediata descontinuidade" dessas operações; não foi publicado no DOU. Em resposta escrita a um pedido de LAI, o BCB afirmou que "os fundos não podem atuar como intermediadores de ativos virtuais e, assim, as operações de câmbio de importação de ativos virtuais por eles realizadas carecem do atributo de licitude".
- **Quem viu:** o Cointelegraph Brasil teve a notificação em 24/jun; a Exame, um trecho em 25/jun. Em 24/jun, operadores disseram que o spread "saiu de cerca de 0,1 acima do mercado para 0,7 após a notificação".
- **Enquadramento:** medimos fricções entre canais; não avaliamos a legalidade de nenhuma rota nem recomendamos uma.
- *Fontes:* E-05.1, E-05.2, E-05.3, E-05.5, E-05.6, E-05.10, E-06a, E-06b, E-10, E-11, E-12, R-02; F-023.

| Data | Medida | Forma | Efeito |
|---|---|---|---|
| 22–23/mai/2025 | IOF da compra comum de moeda estrangeira sobe para 3,5% | Decreto, público | no dia seguinte |
| 30/abr/2026 | Res. BCB 561: veda ativos virtuais na liquidação do eFX | Resolução, pública | 1/out/2026 |
| 18/jun (registro BCB) e 22/jun/2026 (DOU) | Res. BCB 574: instituições de câmbio passam a reportar operações com ativos virtuais | Resolução, pública | reporte de operações a partir de 3/nov/2026 |
| **23/jun/2026** | **Ofício do BCB: "imediata descontinuidade" do câmbio de fundos para importar ativos virtuais** | **Ofício de circulação restrita** | **imediato** |
| 26/jun/2026 | Reunião: suspensão mantida; arbitragem "dentro do livro de ordens" liberada; minuta da retenção de 24 h | Reunião com associações | — |
| 1/jul/2026 | Res. BCB 580: prestadoras de serviços de ativos virtuais no regime prudencial (Tipo 3) | Resolução, pública | 1/jan/2027 |
| 7/ago/2026 | Res. BCB 584: retenção de até 24 h em saídas a partir de US$ 10 mil | Resolução, pública | 1/jan/2027 |

#### Notas do Orador & Rastreabilidade
- **Notas:** "Primeiro, a ideia de paridade. Um USDT comprado com reais deveria custar o mesmo que um dólar oficial; quem compra barato num mercado e vende caro no outro mantém os dois juntos, e o prêmio mede a distância entre eles. Um desses canais era o de fundos de investimento: compravam cripto no exterior com câmbio de IOF zero e vendiam às corretoras no Brasil. Em 23 de junho, o Banco Central enviou um ofício a bancos, corretoras e fundos determinando a imediata descontinuidade dessas operações. O ofício não foi publicado, mas dois veículos tiveram acesso a ele nos dias seguintes, e o BCB confirmou por escrito, numa resposta de LAI, que considera essas operações sem licitude. Já no dia 24, operadores ouvidos pela imprensa ligavam a alta de preço à notificação. A linha do tempo mostra as outras medidas do período; voltaremos a elas."
- **Rastreabilidade:** `docs/sources.md` (citações abertas e copiadas da página: `E-05.1` "imediata descontinuidade", `E-05.2` ABToken, `E-05.3` resposta LAI, `E-05.6` operadores, `E-05.5` e `E-12` reunião de 26/jun, `E-11` Res. 574, `E-10` Res. 580, `E-06a`, `E-06b`, `R-02` IOF); `F-023`.

---

<!-- SLIDE 3 -->
## Slide 3 — Dados e método

### Seis anos de preços pareados à PTAX, três corretoras e cinco moedas de comparação; o salto foi visto antes das hipóteses, e cada teste foi fixado por escrito antes de rodar

#### Layout Visual & Tabela de Desenho
- **Figura (a desenhar, `P5-02`):** diagrama do desenho (dados → três testes → o que nos desmentiria). Até lá, a tabela de hipóteses abaixo.
- **Legenda (10 segundos):** Medimos o prêmio na mesma janela de horário da PTAX, comparamos a mudança de junho com a de mais de mil datas comuns e com outros países, e escrevemos antes o que nos desmentiria.

#### Pontos Principais (pt-BR)
- **Dados:** 1.520 dias úteis de PTAX (13/out/2020 a 30/out/2026). USDT/BRL da Binance pareado à janela de consulta da PTAX e ajustado pelo preço do USDT em dólar; Foxbit e Mercado Bitcoin como segunda e terceira corretoras; o mesmo prêmio em 5 moedas sem o choque (EUR, MXN, TRY, ZAR, COP); compras de stablecoins no exterior nas estatísticas do BCB. O custo de negociar (spread de compra e venda) é de 2 a 10 bps: esse é o piso de ruído.
- **Desenho:** (1) um teste de quebras estruturais que não recebe nenhuma data (Bai–Perron); (2) a mudança da média nos 20 dias úteis depois de cada regra contra os 20 antes, comparada com a mesma conta em 1.073 datas comuns, longe de qualquer evento; (3) um controle sintético com as 5 moedas.
- **Transparência:** o salto de junho apareceu na sondagem inicial (30/out), antes das hipóteses. Por isso, hipóteses, regras de decisão e especificações foram registradas no Git antes de cada teste confirmatório, e a data do ofício vem de fontes externas (imprensa de 24–25/jun e resposta do BCB), não do gráfico.
- **Lições de 2025** (tabela completa no Anexo F): em 2025, nosso melhor modelo perdeu para a previsão "amanhã = hoje". Em 2026: toda estimativa ao lado de uma linha de base ingênua; datas placebo em vez de p-valores paramétricos; contamos eventos, não linhas.
- *Fontes:* F-001, F-002, F-005, F-007, F-011, F-016, F-017; `docs/02-dolar-cripto.md` §5 e §13.

| Hipótese | O que a sustentaria | O que a desmentiria |
|---|---|---|
| **H1:** fechar o canal elevou o prêmio | Mudança maior que em datas comuns e ausente nas moedas de comparação | Mudança comum entre as datas comuns, ou outras moedas subindo junto |
| **H2:** só regras que fecham o canal mais barato em uso movem o prêmio | Regras de licença, reporte ou eFX dentro da faixa das datas comuns | Saltos nessas regras |
| **H3:** a alta do IOF de maio/2025 moveu o prêmio bem menos que o imposto | Mudança pequena ou comum | Salto da ordem de +240 bps |
| **H0:** foi o real, o preço do USDT ou uma corretora | O salto some em outras corretoras ou ao descontar PTAX e USDT/USD | O mesmo salto em três corretoras, com USDT/USD estável |

#### Notas do Orador & Rastreabilidade
- **Notas:** "Os dados cobrem seis anos, mais de 1.500 dias úteis. Medimos o prêmio na mesma janela de horário em que o Banco Central calcula a PTAX, para não confundir movimento do real com prêmio, e descontamos o preço do próprio USDT em dólar. Usamos três testes: um que procura quebras sem saber de nenhuma data; um que compara a mudança em torno de cada regra com a mesma conta em mais de mil datas comuns; e um Brasil sintético feito de outras moedas. Uma transparência importante: vimos o salto na primeira sondagem, antes de escrever as hipóteses. Por isso, todas as regras de decisão foram registradas no Git antes de cada teste, e a data do ofício vem da imprensa e do BCB, não do gráfico. E a lição de 2025, quando nosso modelo perdeu para 'amanhã igual a hoje', virou regra: toda estimativa tem linha de base."
- **Rastreabilidade:** `F-001`, `F-002` (sondagem de 30/out/2026), `F-005`, `F-007` (2–10 bps), `F-011`, `F-016` (1.073 datas), `F-017`; `docs/02-dolar-cripto.md` §5 (hipóteses) e §13 ("Declare it"); `scripts/p1_02_premium.py`, `scripts/p2_01_noise.py`.

---

<!-- SLIDE 4 -->
## Slide 4 — O salto

### O prêmio subiu +93,9 bps no mês seguinte ao ofício, o mesmo nas três corretoras, e um teste que não conhecia a data encontrou a quebra em 24/jun

#### Layout Visual & Figura
- **Imagem:** `results/figures/P2-02_premium_breaks.png` (prêmio diário 2020–2026, faixa de ruído e médias dos regimes encontrados às cegas; `P5-02` redesenha com foco em 2025–26 e rótulos em português) e, como detalhe, `results/figures/P2-05_hourly_22_26_jun.png` (prêmio horário de 22 a 26/jun nas três corretoras).
- **Legenda (10 segundos):** Média de 20 dias úteis: de 15,2 bps antes do ofício para 109,1 bps depois (+93,9 bps). A mudança é maior que a de todas as 1.073 datas comuns (a maior delas: +65,7 bps).

#### Pontos Principais (pt-BR)
- **O tamanho:** +93,9 bps na média dos 20 dias úteis após 23/jun contra os 20 antes. Binance +93,9, Foxbit +93,3 e Mercado Bitcoin +94,9 bps.
- **Sem receber a data:** o teste de quebras aponta 24/jun/2026 como a mudança mais aguda em seis anos (intervalo de 95%: 18 a 30/jun).
- **Comparado com datas comuns:** maior que a mudança em todas as 1.073 datas comuns (a maior: +65,7 bps). Janelas vizinhas compartilham dias, então refizemos só com janelas que não se sobrepõem: em 30 delas, nenhuma tem mudança tão grande (p = 0,03).
- **O que há dentro do mês:** a janela inclui a reunião de 26/jun (suspensão mantida, arbitragem em livro liberada, minuta da retenção de 24 h) e a Res. 580 (1/jul); um segundo pico em 3/jul não tem causa identificada. Nos dois dias antes da reunião, o prêmio já estava **+155 bps** acima do nível anterior (p entre 0,02 e 0,04).
- *Fontes:* F-009, F-011, F-016, F-022, F-029.

#### Notas do Orador & Rastreabilidade
- **Notas:** "Este é o resultado principal. Comparando os 20 dias úteis depois do ofício com os 20 antes, o prêmio subiu 94 pontos-base, e o mesmo salto aparece nas três corretoras. Um teste de quebras estruturais, que não sabia de nenhuma data, encontrou a quebra em 24 de junho. Depois comparamos a mudança de junho com a mesma conta em todas as 1.073 datas comuns dos seis anos: nenhuma chega a esse tamanho; a maior foi 66. Como essas janelas se sobrepõem, refizemos com 30 janelas sem nenhum dia em comum: p de 0,03. Um cuidado: o mês após o ofício também contém a reunião de 26 de junho e a Resolução 580. Mas nos dois dias antes da reunião o prêmio já estava 155 pontos-base acima do nível anterior."
- **Rastreabilidade:** `F-009` (três corretoras), `F-011` e `F-022` (quebra, intervalo 18–30/jun), `F-016` (1.073 datas, maior +65,7), `F-029` (30 janelas sem sobreposição, p = 0,032; +154,6 bps em 24–25/jun, p = 0,020–0,040; `exploratory`); `scripts/p2_02_breaks.py`, `scripts/p2_05_checks.py`, `scripts/p4_04_inference.py`.

---

<!-- SLIDE 5 -->
## Slide 5 — Entre as oito regras testadas, só o ofício saiu da faixa comum

### As regras publicadas, com dias ou meses de aviso, ficaram dentro da faixa das datas comuns; só o ofício de circulação restrita e efeito imediato saiu dela

#### Layout Visual & Figura
- **Imagem:** `results/figures/P3-12_rules.png` (mudança do prêmio em torno de cada regra, no anúncio e na vigência, contra a faixa de 95% das datas comuns).
- **Legenda (10 segundos):** Cada ponto é a mudança do prêmio em torno de uma regra; a faixa cinza é onde ficam 95% das datas comuns (−35 a +38 bps). Só o ofício de 23/jun fica fora.

#### Pontos Principais (pt-BR)
- **Sete regras publicadas** (o decreto do IOF, sua suspensão, quatro resoluções do BCB e uma proposta de IOF sobre cripto que não chegou a valer), com 1 a 175 dias de aviso: mudanças de −24,9 a +15,4 bps, todas dentro da faixa comum.
- **O IOF da compra comum subiu de 1,1% para 3,5% (maio/2025):** o prêmio mudou +13,2 bps (p = 0,38).
- **O contraste mais próximo:** a Res. 561 vedou ativos virtuais na liquidação do eFX, mas foi publicada 154 dias antes de valer: +6,0 bps no anúncio, −5,3 na vigência. Não sabemos o tamanho do canal eFX; o contraste estreita, mas não resolve, a questão de forma ou conteúdo.
- **Res. 574, fora das oito testadas:** registrada em 18/jun e publicada em 22/jun, exige reporte de operações realizadas a partir de 3/nov; não restringe operações em junho. O prêmio subiu 38 bps em 18→19/jun e 131 bps em 23→24/jun. A primeira alta não identifica efeito da resolução, e as janelas de 20 dias da resolução e do ofício se sobrepõem.
- **Limites:** "dentro da faixa" quer dizer sem efeito acima de ~35 bps, não efeito zero. O ofício foi ao mesmo tempo a única medida de circulação restrita e efeito imediato e a única que fechou o canal dos fundos: forma e conteúdo **não** se separam.
- *Fontes:* F-016, F-026, F-029; E-06a, E-11.

#### Notas do Orador & Rastreabilidade
- **Notas:** "Se o ofício moveu o prêmio, outras regras sobre cripto e câmbio também moveram? Testamos as oito regras brasileiras com data, com a mesma conta. As sete publicadas, com um dia a seis meses de aviso, ficaram dentro da faixa das datas comuns. Inclusive a Resolução 561, que vedou ativos virtuais no eFX mas avisou com cinco meses, e o aumento do IOF de 2025, de 1,1% para 3,5%, que mexeu só 13 pontos-base. Só o ofício, de circulação restrita e efeito imediato, saiu da faixa. Duas ressalvas. A Resolução 574, de reporte para operações a partir de novembro, foi publicada em 22 de junho, fora das oito testadas. A alta de 38 pontos-base após a data de registro não identifica seu efeito; as janelas dela e do ofício se sobrepõem. E não sabemos se o que pesou foi a forma, circulação restrita e efeito imediato, ou o conteúdo, porque o ofício tinha os dois."
- **Rastreabilidade:** `F-016` (tabela de eventos, p contra 1.073 datas), `F-026` (oito regras, faixa −35,0 a +37,6 bps dos 200 sorteios), `F-029` (Res. 574: +37,7 bps em 18→19/jun); `E-06a` (texto da Res. 561 aberto), `E-11` (Res. 574); `P3-16` (ressalva explícita, sem nona linha de evento); `scripts/p3_12_rules.py`.

---

<!-- SLIDE 6 -->
## Slide 6 — Não foi o real, nem o USDT, nem o mundo

### O Brasil se afastou +109 bps do seu "gêmeo sintético"; o real e o preço do USDT em dólar não explicam o salto

#### Layout Visual & Figura
- **Imagem:** `results/figures/P2-04_synthetic_control.png` (Brasil vs Brasil sintético; distância do Brasil vs as das moedas de comparação).
- **Legenda (10 segundos):** Um Brasil sintético feito de cinco moedas sem o choque (EUR, MXN, TRY, ZAR, COP) acompanhava o prêmio brasileiro antes de 23/jun; depois, o Brasil se afastou +109,3 bps. Nenhuma das cinco se moveu assim.

#### Pontos Principais (pt-BR)
- **Outros países:** no mês após 23/jun, o Brasil ficou +109,3 bps acima do sintético (+103,3 bps na comparação simples com a média das cinco moedas). O Brasil é o 1º de 6 no teste de permutação; com 5 moedas, o menor p possível é 1/6, então esta é evidência complementar.
- **O real:** a PTAX subiu 0,68% em 24/jun, um dia comum (34% dos dias desde 2020 tiveram movimento maior). O prêmio é medido contra a PTAX, então esse movimento já está descontado; nos 246 dias anteriores com alta igual ou maior, o prêmio caiu em média 18,7 bps no dia.
- **O USDT em dólar:** mudou menos de 1 bp.
- **O bitcoin:** o prêmio do BTC em reais subiu +93,8 bps, como exige a arbitragem triangular dentro da Binance; por isso este teste não separa um choque só em stablecoins de um choque em toda a cripto.
- *Fontes:* F-009, F-017, F-018.

#### Notas do Orador & Rastreabilidade
- **Notas:** "E se o salto viesse de fora: do real, do próprio Tether ou de um movimento em emergentes? Montamos um Brasil sintético com cinco moedas sem esse choque. Antes de junho ele acompanhava o Brasil; depois, o Brasil se afastou 109 pontos-base, e nenhuma das outras moedas teve movimento parecido. Com só cinco comparações, isso é evidência complementar, não um p-valor forte. O real subiu 0,68% no dia 24, um dia comum, e o prêmio já desconta a PTAX; em dias assim o prêmio costuma cair, não subir. O Tether em dólar não mexeu nem um ponto-base. E o bitcoin em reais subiu o mesmo tanto, porque a arbitragem dentro da própria corretora liga os dois preços."
- **Rastreabilidade:** `F-017` (+109,3 bps; DiD +103,3; 1º de 6; p mínimo 1/6), `F-009` (PTAX +0,68%; 246 dias; USDT/USD), `F-018` (BTC +93,8 bps); `scripts/p2_04_synth.py`, `scripts/p2_05_checks.py`, `scripts/p3_02_btc.py`.

---

<!-- SLIDE 7 -->
## Slide 7 — O mecanismo: as importações caíram

### Em julho, as compras de stablecoins no exterior caíram 78% enquanto o prêmio subia: preço maior com quantidade menor, compatível com o fechamento de um canal de oferta

#### Layout Visual & Figura
- **Imagem:** `results/figures/P3-10_imports.png` (compras líquidas mensais de stablecoins no exterior por residentes, BCB, e o prêmio médio mensal).
- **Legenda (10 segundos):** Compras de stablecoins no exterior por residentes (BCB): US$ 2.542 milhões em junho e US$ 572 milhões em julho de 2026 (−78%). No mesmo período, o prêmio médio mensal foi de 11 para 43 e 81 bps (maio a julho).

#### Pontos Principais (pt-BR)
- **A queda:** −78% de junho para julho, fora da faixa normal das variações mensais da série (p = 0,02); a maior queda percentual desde 2021.
- **Leitura:** preço subindo e quantidade caindo coincidem com o fechamento de um canal de oferta. É uma observação mensal: "compatível com", não "causado por".
- **Ressalvas:** a série soma as compras de todos os residentes, não só as de fundos; a Res. 580 saiu no mesmo mês (1/jul).
- **Depois:** em agosto e setembro as compras ficaram em 32% do nível de janeiro a maio, enquanto o prêmio voltava a 33 e 23 bps. O recuo do prêmio não veio da reabertura desse canal (teste registrado antes; resultado "parcial, inconclusivo").
- *Fontes:* F-024; D-16; E-10.

#### Notas do Orador & Rastreabilidade
- **Notas:** "Se o ofício fechou um canal de oferta, deveríamos ver menos dólares digitais entrando. As estatísticas do Banco Central mostram isso: as compras de stablecoins no exterior por residentes caíram 78% de junho para julho, de 2,5 bilhões para 570 milhões de dólares, enquanto o prêmio subia. Preço maior com quantidade menor é o padrão de um canal de oferta fechado. Mas é um mês só, a série inclui todos os residentes, não só fundos, e a Resolução 580 saiu no mesmo mês. Por isso dizemos 'compatível com', e não 'causado por'. Um detalhe que importa para o próximo slide: em agosto e setembro as compras continuaram baixas, enquanto o prêmio já tinha voltado. O recuo não veio da reabertura desse canal."
- **Rastreabilidade:** `F-024` (T1 p = 0,022; T2 = 0,32), `D-16` (`SGS 29644`), `E-10` (Res. 580); `scripts/p3_10_imports.py`.

---

<!-- SLIDE 8 -->
## Slide 8 — Robusto, mas de um mês

### O pico resiste a 22 formas de medir (+74 a +128 bps); depois de 22/jul, o que restou não se distingue das variações comuns

#### Layout Visual & Figura
- **Imagem:** `results/figures/P4-01_robustness_forest.png` (cada linha é uma forma de medir o mês após o ofício).
- **Legenda (10 segundos):** Janelas de 10 a 30 dias, quatro definições do prêmio, três corretoras e o controle sintético: todas entre +73,7 e +128,3 bps. O nível depois de 22/jul (+11,5 a +19,3 bps) aparece em datas comuns com frequência (p = 0,24).

#### Pontos Principais (pt-BR)
- **Robusto:** 22 variantes, de +73,7 a +128,3 bps; 10 a 35 vezes o piso de ruído.
- **Só um mês:** o pico diário foi de 185,9 bps em 3/jul; depois disso o prêmio já caía, e o teste de quebras data o recuo em 22/jul, quando a média passa de 109,1 para 26,8 bps.
- **O que não mostramos:**
  - um efeito duradouro (p = 0,24);
  - a causa do recuo: nenhum evento datado a até 5 dias úteis de 22/jul, e as compras no exterior não voltaram;
  - qual canal passou a definir o preço depois do ofício;
  - se o que pesou foi a forma do ofício (circulação inicialmente restrita, efeito imediato) ou o conteúdo (fechar o canal dos fundos).
- *Fontes:* F-011, F-022, F-024, F-026, F-028.

#### Notas do Orador & Rastreabilidade
- **Notas:** "Aqui está o que podemos e o que não podemos afirmar. O pico resiste a 22 formas diferentes de medir: janelas de 10 a 30 dias, quatro definições do prêmio, três corretoras e o controle sintético; todas dão entre 74 e 128 pontos-base. Mas é um pico de um mês. Depois de 3 de julho o prêmio já caía, e a partir de 22 de julho a média voltou a 27 pontos-base. A diferença que sobrou, de 11 a 19 pontos, aparece em datas comuns cerca de uma vez em quatro. Não afirmamos efeito duradouro. Também não sabemos por que o prêmio recuou, qual canal passou a definir o preço, nem se o que pesou foi a forma ou o conteúdo do ofício."
- **Rastreabilidade:** `F-022` (22 variantes; 10–35× o piso; p = 0,24 em 882 datas), `F-011` (recuo em 22/jul; 109,1 → 26,8 bps; sem evento em ±5 dias), `F-028` (pico de 185,9 bps em 3/jul; canal não identificado), `F-024` (compras não voltaram), `F-026` (forma vs conteúdo); `scripts/p4_01_robustness.py`.

---

<!-- SLIDE 9 -->
## Slide 9 — Quanto custou e para quem

### Em quatro semanas, quem comprou USDT pagou R$ 106 milhões a mais na Binance: dinheiro que foi para quem vendia, não para o governo

#### Layout Visual & Tabela
- **Figura (a desenhar, `P5-02`):** a transferência no mês após o ofício contra as 194 janelas comuns de quatro semanas (`results/tables/P3-11_placebo.csv`). Até lá, a tabela abaixo.
- **Legenda (10 segundos):** De 24/jun a 21/jul, compradores de USDT na Binance pagaram R$ 106 milhões acima do que pagariam ao prêmio anterior; em 194 janelas comuns de quatro semanas, o maior valor foi R$ 35,5 milhões.

#### Pontos Principais (pt-BR)
- **Por lote:** R$ 4.842 a mais a cada US$ 100 mil (+93,9 bps, à PTAX de cada dia).
- **No mercado:** de 24/jun a 21/jul, R$ 11,2 bilhões em USDT/BRL na Binance; os compradores pagaram em média 95 bps acima do prêmio anterior: **R$ 106 milhões** (R$ 145 milhões somando Foxbit e Mercado Bitcoin).
- **Para quem:** cada real pago a mais por um comprador foi recebido por um vendedor. Funcionou como uma tarifa de ~0,95% sobre a compra de dólar digital, sem arrecadação. É uma transferência, não uma perda de bem-estar medida, e não inclui balcão (OTC) nem P2P.
- **Por que +94 e não +350 bps?** 350 bps é a diferença de alíquota de IOF entre o canal fechado (0%) e a compra comum de moeda (3,5%): uma alíquota, não um preço. O prêmio nunca chegou perto (no pior dia, 3/jul, +171 bps sobre o nível anterior), e quando essa alíquota subiu de 1,1% para 3,5% em 2025 o prêmio mudou +13 bps. A compra comum não definia o preço; se foi oferta mais barata ou menos demanda que o conteve, não sabemos.
- *Fontes:* F-015, F-025, F-026, F-028.

| 24/jun a 21/jul/2026 | Binance | Três corretoras |
|---|---|---|
| Volume negociado em USDT/BRL | R$ 11,2 bi | R$ 15,8 bi |
| Pago acima do prêmio anterior | **R$ 106 mi** (94,9 bps) | R$ 145 mi (92,2 bps) |
| Maior valor em 194 janelas comuns de quatro semanas | R$ 35,5 mi | — |

#### Notas do Orador & Rastreabilidade
- **Notas:** "Em dinheiro: para um lote de 100 mil dólares, cerca de 5 mil reais a mais. No mercado, nas quatro semanas após o ofício, foram negociados 11,2 bilhões de reais em USDT na Binance, e os compradores pagaram 106 milhões a mais do que pagariam ao prêmio anterior; 145 milhões somando as três corretoras. Nenhuma janela comum de quatro semanas passou de 36 milhões. Esse dinheiro não foi para o governo: foi de quem comprava para quem vendia, como uma tarifa de quase 1% sem arrecadação. E por que 94 e não 350 pontos-base, a diferença de IOF? Porque 350 é uma alíquota, não um preço. O prêmio nunca chegou perto, e quando essa alíquota subiu em 2025 ele quase não se mexeu. A compra bancária comum não definia o preço."
- **Rastreabilidade:** `F-015` (R$ 4.842 à PTAX de cada dia; antes R$ 5.052 a R$ 5,38), `F-025` (R$ 106,1 mi e R$ 145,3 mi; 194 janelas, maior R$ 35,5 mi; as janelas se sobrepõem, por isso o slide não mostra o p = 0,005 de `F-025`), `F-028` (+170,7 bps; não identificado), `F-026` (+13,2 bps em mai/2025); tabela de rotas no Anexo B.5 e em `results/tables/P3-15_routes.md`; `scripts/p3_11_money.py`.

---

<!-- SLIDE 10 -->
## Slide 10 — Implicações, previsão e limites

### Fechar um canal de entrada de uma vez gerou um custo agudo que se desfez em cerca de um mês; deixamos uma previsão datada que pode nos desmentir em 2027

#### Layout Visual & Quadro de Previsão
- **Figura:** o quadro da previsão abaixo, em destaque.
- **Legenda (10 segundos):** Registramos no Git, em 2/nov/2026, que a retenção de 24 h da Res. BCB 584 (a partir de 1/jan/2027) não moverá o prêmio de forma detectável. Se mover, estávamos errados.

#### Pontos Principais (pt-BR)
- **Para o Brasil:** o fechamento imediato de um canal de entrada custou a quem comprava dólar digital R$ 106 milhões em quatro semanas, só na Binance, e o efeito se desfez em cerca de um mês, por razões que não identificamos. As regras publicadas com aviso não moveram o prêmio de forma detectável (acima de ~35 bps); como não separamos forma de conteúdo, não recomendamos um formato de regra.
- **Um termômetro diário:** o prêmio sobre a PTAX pode ser acompanhado todo dia. Um protótipo de monitor, calibrado só com 2020–2025, disparou no próprio 24/jun e deu 2 outros alarmes em 2026 (contra 4 de uma regra simples). É uma detecção real, não uma validação.
- **Limites:** um choque, em um país; o texto integral do ofício não é público; a Res. 574 e a reunião de 26/jun estão perto demais para serem separadas; a causa do recuo e o canal que passou a definir o preço não foram identificados.
- **Próximos passos:** um caso em que um canal se abre, como teste no sentido oposto (a Argentina é candidata, com ressalvas no Anexo F); os reportes da Res. 574, a partir de 3/nov/2026, podem permitir testes melhores de mudanças futuras, se os dados se tornarem disponíveis.
- *Fontes:* F-014, F-022, F-025, F-026, F-027, F-028, F-029.

| Previsão registrada em 2/nov/2026 (commit `393a14a`) | |
|---|---|
| **Regra** | Res. BCB 584: retenção de até 24 h em transferências a partir de US$ 10 mil para o exterior ou carteiras autocustodiadas, a partir de 1/jan/2027 |
| **Previsão** | A mudança do prêmio em torno de 4/jan/2027 (20 dias úteis depois vs 20 antes) fica entre −35,0 e +37,6 bps |
| **Por quê** | Atrasa saídas, não as entradas que formam a oferta; custa ~9 bps a quem já tem USDT |
| **O que nos desmentiria** | Mudança fora dessa faixa, com p de placebo < 0,05; conferência em fevereiro de 2027 |
| **Ressalva** | A Res. 580 também começa a valer em 1/jan/2027; a regra não atinge o canal de entrada, então é um teste parcial de "regra publicada com aviso" |

#### Notas do Orador & Rastreabilidade
- **Notas:** "O que isso diz para o Brasil? Que fechar um canal de entrada de uma vez gerou um custo agudo para quem comprava dólar digital, 106 milhões de reais em quatro semanas só numa corretora, e que esse efeito se desfez em cerca de um mês, por razões que não identificamos. As regras publicadas com aviso não moveram o prêmio de forma detectável, mas não sabemos se pela forma ou pelo conteúdo; por isso não recomendamos um formato de regra. O prêmio é um termômetro diário e barato: nosso protótipo de monitor disparou no próprio dia 24. E deixamos uma previsão registrada: a retenção de 24 horas que começa em 1º de janeiro não vai mover o prêmio de forma detectável. Se mover, estávamos errados, e a banca poderá conferir. Obrigado."
- **Rastreabilidade:** `F-025` (R$ 106 mi), `F-022` (um mês; p = 0,24), `F-026` (regras publicadas; forma vs conteúdo), `F-014` (monitor: atraso 0; 2 vs 4 outros alarmes), `F-027` e `results/tables/P3-13_prediction.md` (previsão, faixa, regra de falsificação, commit `393a14a`), `F-028`, `F-029`; `F-010` (prêmio argentino, Anexo F); `E-11` (Res. 574).

# Quanto Custa Fechar a Porta?
## O prêmio do dólar digital no Brasil e os limites à arbitragem

**7º Datathon de Moedas Digitais FGV EESP (novembro de 2026)**  
**Equipe Out of Sample:** Renzo (CS 1), Nattan (CS 2), Jonathan (CS 3), Felipe (Economista)  
**Organização:** FGV EESP, Centro de Estudos em Finanças Digitais FGV, com apoio de FGV/Ripple (UBRI) e USP-UBRI  

---

### Sumário (10 slides, ~60 s cada; versão 2, de 3/nov/2026)
1. **Quanto custa fechar a porta?** — pergunta e resposta
2. **A porta que fechou: o ofício de 23/jun** — o canal, o ofício, a linha do tempo
3. **Dados e método** — dados, desenho, o que nos desmentiria, transparência e "Lições de 2025"
4. **O salto** — +93,9 bps, três corretoras, quebra encontrada às cegas, comparação com datas comuns
5. **Entre as oito regras testadas, só o ofício saiu da faixa comum** — regras publicadas vs ofício; Res. 574
6. **Não foi o real, nem o USDT, nem o mundo** — controle sintético, PTAX, USDT/USD, bitcoin
7. **O mecanismo: as importações caíram** — −78% nas compras de stablecoins no exterior
8. **Robusto, mas de um mês** — 22 variantes; o que não mostramos
9. **Quanto custou e para quem** — R$ 106 milhões no mercado; quatro pessoas com regras fixadas antes
10. **Implicações e três previsões datadas** — Res. 574 (3/nov), Res. 589 (6/nov), Res. 584 (1/jan/2027)

**Ordem de corte se o tempo for curto:** reduzir os slides 6 e 8 a uma frase cada; depois o 7.
Perguntas difíceis e respostas de 20 segundos: `deck/qa_ptbr.md`. Material movido para o anexo: Anexo F de
`deck/annex_v1_ptbr.md`. O que mudou em relação à versão de 14 slides: `docs/deck-changes-2026-11-02.md`.
**Versão 2 (3/nov/2026):** aplica a proposta `docs/deck-proposal-2026-11-03.md` (slides 1, 9 e 10); a versão 1 continua em
`deck/deck_v1_ptbr.md`. Pendentes da equipe: tabela de pessoas no slide 9, resultado da Res. 574 no slide 10 (exceção
ao congelamento), linha exploratória no slide 8 (não aplicada). A ressalva da Res. 574 no slide 5 segue `P3-16`.

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
- **Notas:** "Nossa pergunta é simples: quanto custa fechar a porta? Quando uma regra fecha um dos canais que mantêm o dólar digital colado ao dólar oficial, quanto a mais os brasileiros pagam? Em 23 de junho de 2026, o Banco Central enviou um ofício que interrompeu de imediato um desses canais. No mês seguinte, o prêmio do USDT sobre a PTAX subiu 94 pontos-base: para quem comprava 100 mil dólares em USDT, cerca de 4,8 mil reais a mais. E não é um mercado pequeno: até maio, residentes compravam cerca de 2,4 bilhões de dólares por mês em stablecoins no exterior. A seguir mostramos qual porta fechou, como medimos o salto, por que não foi outra coisa, quanto custou e o que não conseguimos mostrar."
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

### Em quatro semanas, quem comprou USDT pagou R$ 106 milhões a mais na Binance; para uma pessoa, dependeu de quando precisou de dólar

#### Layout Visual & Tabela
- **Figura:** nenhuma; o total do mercado em destaque e a tabela das quatro pessoas abaixo.
- **Legenda (10 segundos):** De 24/jun a 21/jul, compradores na Binance pagaram R$ 106 milhões acima do prêmio anterior (maior valor em 194 janelas comuns de quatro semanas: R$ 35,5 milhões). Abaixo, o que isso significou para quatro pessoas, com regras fixadas antes do cálculo.

#### Pontos Principais (pt-BR)
- **No mercado:** de 24/jun a 21/jul, R$ 11,2 bilhões em USDT/BRL na Binance; os compradores pagaram em média 95 bps acima do prêmio anterior: **R$ 106 milhões** (R$ 145 milhões somando Foxbit e Mercado Bitcoin). Foi de quem comprava para quem vendia, sem arrecadação; não inclui balcão (OTC) nem P2P.
- **Para uma pessoa:** dependeu de quando precisou de dólar (tabela; por US$ 100 mil, salvo indicação; só o prêmio, sem taxas nem impostos).
- **Por que +94 e não +350 bps** (a diferença de IOF): Anexo F.7.
- *Fontes:* F-015, F-025, F-033.

| Quem | Regra fixada antes | Resultado |
|---|---|---|
| Precisou de dólar no pico | comprou num dia entre 24/jun e 21/jul | pagou **R$ 4.842** a mais, em média (R$ 1.895 a R$ 8.824 conforme o dia) |
| Poupa US$ 10 mil por mês | comprou no 1º dia útil de cada mês | nas 4 compras após o ofício (US$ 40 mil), **R$ 753** a mais |
| Já tinha USDT em 23/jun | vendeu em 24/jun, 21/jul ou 30/out | posição valorizada em R$ 6.802, R$ 1.407 ou −R$ 2.992 |
| Comprou no pânico, em 24/jun | manteve até 21/jul ou 30/out | posição desvalorizada em R$ 5.223 ou R$ 10.070 |

*Ilustração com regras fixadas antes do cálculo (commit `79e15d1`) sobre um caminho de preços já conhecido. Compras são transferências; valorização de posições mantidas não é dinheiro que mudou de mão. Detalhes no Anexo B.5.*

#### Notas do Orador & Rastreabilidade
- **Notas:** "Em dinheiro: nas quatro semanas após o ofício, os compradores de USDT na Binance pagaram 106 milhões de reais a mais do que pagariam ao prêmio anterior; nenhuma janela comum de quatro semanas passou de 36 milhões. Esse dinheiro foi de quem comprava para quem vendia, não para o governo. Para uma pessoa, dependeu de quando precisou de dólar: quem comprou no pico pagou cerca de 4,8 mil reais a mais por 100 mil dólares; quem poupava todo mês sentiu pouco; quem já tinha USDT ganhou se vendeu logo; quem comprou no pânico e segurou ficou para trás. As regras de cada pessoa foram fixadas antes do cálculo."
- **Rastreabilidade:** `F-025` (R$ 106,1 mi e R$ 145,3 mi; 194 janelas, maior R$ 35,5 mi; as janelas se sobrepõem, por isso o slide não mostra o p = 0,005), `F-033` (quatro pessoas; `exploratory`, re-derivado de forma independente; `scripts/p3_21_who_paid.py`, `results/tables/P3-21_who_paid.csv`), `F-015` (R$ 4.842 à PTAX de cada dia); "+94 e não +350" em `F-028` e Anexo F.7; `scripts/p3_11_money.py`.

---

<!-- SLIDE 10 -->
## Slide 10 — O que aprendemos: o custo do dólar digital se decide na porta de entrada

### Três lições para o mercado e para a regulação, e uma régua pública com três previsões registradas no Git

#### Layout Visual & Síntese
- **Figura:** o quadro das três lições e a régua pública de previsões abaixo, em destaque.
- **Legenda (10 segundos):** Três lições empíricas para o mercado e para a regulação sobre custos de entrada, hedge cambial e duração de choques, acompanhadas de uma régua pública no Git que testa novas regras antes da vigência.

#### Pontos Principais (pt-BR)
- **Três Lições:**
  1. **Fechar uma porta de uma vez custa caro e rápido:** O ofício imediato de 23/jun elevou o prêmio em +93,9 bps por um mês (R$ 4.842 por US$ 100 mil; R$ 106 mi transferidos de quem comprava para quem vendia na Binance, R$ 145 mi em três corretoras, sem arrecadação). As sete regras publicadas com aviso prévio ficaram na faixa das datas comuns (isso não prova efeito zero, e forma vs. conteúdo não se separam; ressalva: a Res. 574, publicada na véspera, coincide com +38 bps em 18→19/jun).
  2. **O hedge cambial reduz a exposição ao USD/BRL (retrospectivo, exploratório):** Para um comprador institucional de 100 mil USDT com acesso à B3, o hedge cambial por paridade coberta de juros (CIP) compensa o diferencial de juros sob CIP ideal (a compensação depende das taxas assumidas e não cobre todos os custos), tornando a espera uma comparação que também depende do USDT/USD, do rendimento USD e do residual do hedge. Em retrospecto após 25/jun, esperar com hedge economizou +89,7 a +164,0 bps (R$ 4.746 a R$ 8.733 em 5 a 20 dias úteis), mas o ganho não foi monotônico (+6,3 bps = R$ 335 em 6 dias, em 3/jul) nem previsível ex-ante. Neste episódio e sob as taxas e custos assumidos, o vendedor que adiou a conversão perdeu R$ 4.697 a R$ 21.704 em 5 a 20 dias, sobretudo pela queda do prêmio e pela valorização do real.
  3. **Preço normal não é mercado normal:** O prêmio cedeu a partir de 22/jul (pós-pico p = 0,24), mas as compras de stablecoins no exterior caíram 78% em julho (compatível com restrição de quantidade) e ficaram em um terço até setembro, enquanto a fatia da Foxbit nas três corretoras passou de 7% para 35% (exploratório). Na amostra de treino do censo de 10 moedas (61 choques no total), metade dos choques retorna à banda em 20 dias úteis (mediana de Kaplan-Meier), mas o modelo testado não mostrou ganho preditivo robusto nesta amostra pequena, e o choque brasileiro iniciado em 25/mai seguia aberto após 111 dias úteis (exploratório).
- **A Solução: Uma Régua Pública de Custo Regulatório:**
  ① Medir o prêmio todo dia na janela da PTAX com dados públicos e código aberto (nosso monitor CUSUM calibrado em 2020–2025 disparou no próprio 24/jun com atraso zero: uma detecção, não uma previsão) → ② Comparar com as datas comuns → ③ Registrar a previsão no Git antes da vigência → ④ Conferir e converter em reais.

| Regra | Vigência | Previsão registrada antes dos dados | Conferência |
|---|---|---|---|
| Res. BCB 574: reporte de operações com ativos virtuais | 3/nov/2026 | sem movimento detectável (commit `9a522e9`) | conferido em 3–4/nov na Binance: +2,1 bps (p = 0,90, faixa S2 −75,5/+59,8 bps; auditoria P3-26 confirma S2 isolado do incidente da Binance); confirmada |
| Res. BCB 589, art. 91: veda contrapartes não autorizadas | 6/nov/2026 | sem direção registrada (ramo C, commit `5e9d56c`); teste bilateral | leitura antecipada S1 em 6/nov: −5,4 bps na Binance (p = 0,79), −6,5 bps na Foxbit (p = 0,79); paridade mantida (gap de +0,1 bps); veredito S2 em 9/nov |
| Res. BCB 584: retenção de até 24 h em saídas a partir de US$ 10 mil | 1/jan/2027 | sem movimento detectável: entre −35,0 e +37,6 bps (commit `393a14a`) | fevereiro de 2027 |

*A faixa descreve datas históricas; não é intervalo de confiança de efeito causal nem prova efeito zero. Regra de decisão: p de placebo < 0,05 em dois dias (574, 589) ou 20 dias úteis (584).*

#### Notas do Orador & Rastreabilidade
- **Notas:** "O que aprendemos com a pesquisa? Transferência barata não garante conversão barata. Deixamos três lições e uma régua pública. Primeira lição: fechar uma porta de uma vez custa caro e rápido. O ofício imediato de 23 de junho elevou o prêmio em 94 pontos-base por um mês — 106 milhões de reais transferidos de quem comprava para quem vendia na Binance, sem arrecadação —, enquanto sete regras públicas com aviso prévio ficaram dentro da faixa comum (ressalva: a Resolução 574, publicada na véspera, coincide com alta de 38 pontos-base em 18 para 19 de junho). Segunda lição: o hedge cambial reduz a exposição ao USD/BRL. Para tesourarias institucionais comprando 100 mil USDT com acesso à B3, a paridade coberta de juros (CIP) compensa o diferencial de juros sob CIP ideal, pois os juros em reais pagam os pontos a termo; a espera vira comparação que também depende do USDT/USD, do rendimento USD e do residual do hedge. Em retrospecto após 25 de junho, esperar economizou de 4,7 mil a 8,7 mil reais em 5 a 20 dias úteis, mas o ganho não foi monotônico (apenas 335 reais em 6 dias) nem previsível ex-ante, e, neste episódio sob as taxas e custos assumidos, o vendedor que adiou a conversão perdeu de 4,7 mil a 21,7 mil reais. Terceira lição: preço normal não é mercado normal. O prêmio cedeu após 22 de julho, mas as importações caíram 78% e a composição entre corretoras mudou. Na amostra de treino de 10 moedas, metade dos choques retorna à banda em 20 dias úteis, mas o modelo testado não mostrou ganho preditivo robusto nesta amostra pequena, e o choque brasileiro de maio de 2026 seguia aberto após 111 dias úteis. Como solução, propomos uma régua pública de custo regulatório: medir o prêmio diário com dados abertos na PTAX (nosso monitor CUSUM detectou o choque no próprio dia 24), comparar com datas comuns, registrar previsões no Git antes da vigência e converter o impacto em reais. Deixamos três previsões registradas no repositório. Obrigado."
- **Rastreabilidade:**
  - Lição 1: `F-015` (R$ 4.842 / 100k USDT), `F-016` (+93,9 bps, 1.073 datas comuns), `F-025` (R$ 106,1 mi Binance e R$ 145,3 mi três corretoras transferidos sem arrecadação), `F-026` (sete regras públicas na faixa comum), `F-028` (alíquota vs preço), `F-029` (forma vs conteúdo; Res. 574 na véspera coincide com +38 bps em 18→19/jun).
  - Lição 2: `F-039` (nível: retrospectivo e exploratório; paridade coberta CIP ideal compensa o diferencial de juros; custos e residual permanecem; comprador hedged economizou retrospectivamente +89,7 a +164,0 bps = R$ 4.746 a R$ 8.733 em 5 a 20 dias úteis; +6,3 bps = R$ 335 em 6 dias, em 3/jul; vendedor que adiou perdeu R$ 4.697 a R$ 21.704 por queda do prêmio e apreciação cambial; reexecução por colega pendente).
  - Lição 3: `F-022` (pico de um mês; nível pós-22/jul com placebo p = 0,24), `F-024` (queda de 78% nas importações do BCB em julho, mantendo-se em um terço até setembro), `F-036` (fatia da Foxbit de 7% para 35%, exploratório), `F-038` (nível: exploratório; censo de 10 moedas com 61 choques a 3σ; mediana Kaplan-Meier de 20 dias úteis; modelo testado não estabelece ganho robusto nesta amostra; choque do Brasil de 25/mai aberto após 111 dias úteis PTAX; reexecução por colega pendente).
  - Régua Pública e Previsões: `F-014` (monitor CUSUM: atraso zero em 24/jun, 2 alarmes em 2026), `F-035` e `P3-20` (Res. 574 commit `9a522e9`, leitura preliminar E1 na Binance +2,1 bps, p = 0,90, faixa S2 −75,5/+59,8 bps, aguarda reexecução), `P3-20` (Res. 589 art. 91 ramo C sem direção commit `5e9d56c`), `F-027` (Res. 584 previsão commit `393a14a`), `P3-26` (auditoria do incidente de segurança da Binance de 29/out).

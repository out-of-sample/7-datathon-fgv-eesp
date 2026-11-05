# Perguntas difíceis — respostas de 20 segundos (ensaio)

Para o ensaio do deck de 10 slides (`deck/deck_v1_ptbr.md`). Cada resposta cabe em ~20 s e aponta para onde está a
evidência. Números conferidos nos achados citados em 2/nov/2026; se um achado mudar, atualizar aqui.

| # | Pergunta | Resposta (~20 s) | Onde |
|---|---|---|---|
| 1 | "É um evento só. Como saber que não é sorte?" | É um choque só, e dizemos isso. Comparamos a mudança de junho com a mesma conta em 1.073 datas comuns: nenhuma chega perto (a maior: +66 bps). Com 30 janelas que não se sobrepõem, p = 0,03. As sete regras publicadas e o Brasil sintético são contrastes, não réplicas. | Slide 4; F-016, F-029 |
| 2 | "E a Res. 574, publicada um dia antes do ofício?" | É uma regra de reporte, para operações a partir de 3/nov; não restringe nada em junho. Houve uma alta de 38 bps no dia útil seguinte ao registro dela, e o teste de evento não a separa do ofício. O salto de 131 bps veio no dia seguinte ao ofício. | Slide 5; F-029, P3-16 |
| 3 | "A Res. 580 e a reunião de 26/jun estão dentro do mesmo mês." | Sim. Os +94 bps são a média do mês com tudo o que aconteceu nele. Nos dois dias antes da reunião, que também são antes da Res. 580, o prêmio já estava +155 bps acima do nível anterior (p entre 0,02 e 0,04). | Slide 4; F-029, E-12, E-10 |
| 4 | "Se o IOF era 3,5%, por que o prêmio não subiu 350 bps?" | 350 bps é uma alíquota, não um preço. O prêmio nunca chegou perto (no pior dia, +171 bps), e quando essa alíquota subiu de 1,1% para 3,5% em 2025 o prêmio mudou +13 bps. Não identificamos qual canal passou a definir o preço. | Slide 9; F-028, Anexo B.5 |
| 5 | "Por que medir na janela da PTAX?" | A PTAX vem de quatro consultas entre 10h e 13h. Medir o USDT na mesma janela evita chamar de prêmio um movimento do real ao longo do dia. | Slide 3; `scripts/p1_02_premium.py` |
| 6 | "Não foi o real que se desvalorizou?" | A PTAX subiu 0,68% em 24/jun, um dia comum, e o prêmio já desconta a PTAX. Em dias com alta assim, o prêmio costuma cair, não subir. | Slide 6; F-009 |
| 7 | "O efeito é duradouro?" | Não mostramos. Depois de 22/jul, o que restou (+11 a +19 bps) aparece em datas comuns cerca de uma vez em quatro (p = 0,24). Afirmamos só o pico de um mês. | Slide 8; F-022 |
| 8 | "Por que o prêmio recuou?" | Não sabemos. Nenhum evento datado a até 5 dias úteis de 22/jul, e as compras no exterior continuaram baixas. Uma busca por retomada das operações dos fundos em julho não encontrou nada, o que não prova que não houve. | Slide 8; F-011, F-024 |
| 9 | "Quem ficou com os R$ 106 milhões?" | Quem vendeu USDT nessas corretoras: cada real pago a mais por um comprador foi recebido por um vendedor. Não vemos a identidade de quem vendeu, e é transferência, não perda de bem-estar. | Slide 9; F-025 |
| 10 | "Vocês estão dizendo que a rota dos fundos era legal?" | Não avaliamos legalidade. Citamos o BCB nas palavras dele (resposta de LAI) e medimos fricções entre canais. | Slide 2; E-05.3, `docs/02-dolar-cripto.md` §10 |
| 11 | "Por que o bitcoin subiu junto?" | Na Binance, BTC/BRL, BTC/USDT e USDT/BRL estão ligados por arbitragem triangular; o prêmio do BTC tem de acompanhar. Por isso esse teste não separa um choque em stablecoins de um choque em toda a cripto. | Slide 6; F-018 |
| 12 | "Então o regulador deve sempre avisar antes?" | Não recomendamos isso. O ofício teve circulação inicialmente restrita e foi o único que fechou o canal dos fundos; não separamos forma de conteúdo. A previsão para a Res. 584 é um teste parcial. | Slides 5 e 10; F-026, F-027 |
| 13 | "Vocês viram o salto antes de formular a hipótese?" | Sim, e dizemos no slide 3. Por isso cada teste foi registrado no Git antes de rodar, e a data do ofício vem da imprensa e do BCB, não do gráfico. | Slide 3; F-002 |

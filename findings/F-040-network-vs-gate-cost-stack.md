---
id: F-040
title: O salto observado de prêmio (+93,9 bps) equivale a ~470× a 939× a taxa de rede on-chain (0,1–0,2 bps) e reaparece na rota DeFi (+111,0 bps); o prêmio cedeu mas o mercado não retornou ao padrão pré-ofício
status: exploratory
task: P3-01
date: 2026-11-07
checked_by: -
---

## Claim
A vantagem de custo das redes de stablecoins (medida em frações de ponto-base) não contorna o custo regulatório de acesso ao dólar.
Na rota de USDT centralizada, a taxa de transferência on-chain é de apenas 0,1 a 0,2 bps (1 a 2 USDT em US$ 100 mil, A-02/R-05), enquanto o choque agudo do ofício de 23/jun/2026 somou +93,9 bps (R$ 4.842 por US$ 100 mil a PTAX, F-015/F-016): o salto observado de prêmio é cerca de **470× a 939× maior** que a taxa de rede da blockchain. Na rota 100% on-chain Polygon (`Pix → BRLA → USDC` via Uniswap v3, F-037), o prêmio sobre a PTAX aumentou **+111,0 bps** (de 34,9 para 145,9 bps), superando em **22,2× a taxa de 5 bps do pool**, observação compatível com fricções de conversão compartilhadas; a causa não é isoladamente identificada.

Além disso, a recuperação do prêmio para 26,8 bps após 22/jul (p = 0,24, indistinguível de ruído) **não significou a volta da normalidade de mercado**: enquanto o preço cedeu, as aquisições líquidas de stablecoins no exterior (BCB SGS 29644) desabaram **−78% em julho** (de US$ 2,54 bi para US$ 0,57 bi) e permaneceram comprimidas em **um terço (~32%)** em agosto–setembro (US$ 0,70 bi e 0,84 bi), enquanto a fatia de volume da Foxbit permaneceu elevada até o fim da amostra, passando de 6,8% para 28,0% (onda) e 34,7% (pós-pico, F-036), acompanhada por +361,9 mn USDT de vendas agressivas em horário comercial (96,5% entre 9h e 18h, F-031).

## Evidence
Reprodução completa:
`py scripts/p3_34_cost_stack_and_recovery_figures.py`
Gera:
- Tabela de decomposição: `results/tables/P3-34_cost_stack.csv`
- Figura 1 (Decomposição do Custo): `results/figures/P3-34_cost_stack.png`
- Figura 2 (Painel Triplo Preço vs Mercado): `results/figures/P3-34_price_vs_market_recovery.png`

### 1. Decomposição do Custo (Cost-Stack)
Valores por US$ 100.000 convertidos à PTAX média do choque (5,1418 BRL/USD, F-015):

| Regime / Rota | Prêmio de Acesso | Taxa Negociação / Pool | Taxa Saque On-Chain | Custo Total (bps) | Custo em R$ / US$ 100k | Razão Choque / Rede |
|---|---:|---:|---:|---:|---:|---:|
| 1. Antes do ofício (25/mai–22/jun) | 15,2 bps | 8,0–10,0 bps | 0,1–0,2 bps | 23,3–25,4 bps | R$ 1.193 – R$ 1.306 | — |
| 2. Pico pós-ofício (24/jun–21/jul) | 109,1 bps | 8,0–10,0 bps | 0,1–0,2 bps | 117,2–119,3 bps | R$ 6.021 – R$ 6.134 | — |
| 3. Pós-pico (22/jul–30/out) | 26,8 bps | 8,0–10,0 bps | 0,1–0,2 bps | 34,9–37,0 bps | R$ 1.789 – R$ 1.902 | — |
| **4. Choque regulatório do ofício** | **+93,9 bps** | **0,0 bps** | **0,0 bps** | **+93,9 bps** | **R$ 4.842,04** | **469,5× a 939,0×** |
| 5. DeFi Polygon (`Pix → BRLA → USDC`) Antes | 34,9 bps | 5,0 bps | 0,0 bps | 39,9 bps | R$ 2.052 | — |
| 6. DeFi Polygon (`Pix → BRLA → USDC`) Pico | 145,9 bps | 5,0 bps | 0,0 bps | 150,9 bps | R$ 7.759 | — |
| **7. Choque na rota DeFi Polygon** | **+111,0 bps** | **0,0 bps** | **0,0 bps** | **+111,0 bps** | **R$ 5.707** | **22,2× taxa do pool** |

### 2. Painel Triplo: Preço Normal Não É Mercado Normal
O gráfico `P3-34_price_vs_market_recovery.png` alinha três dimensões temporais (jan–out/2026) sem interpolação de dados mensais em diários:
- **Painel A (Diário):** Prêmio sobre a PTAX nas 3 corretoras (Binance, Foxbit, Mercado Bitcoin) ilustra o salto simultâneo em 24/jun (+93,9 bps) e arrefecimento pós-22/jul (nível médio 26,8 bps, indistinguível de ruído, p = 0,24).
- **Painel B (Mensal em barras/degraus):** Compras de stablecoins no exterior registradas pelo Banco Central (SGS 29644) caíram de US$ 2,54 bi (junho) para US$ 0,57 bi em julho (−78%), mantendo-se em cerca de um terço da média prévia (US$ 0,70 bi em agosto e US$ 0,84 bi em setembro, média de US$ 0,77 bi = 32% dos US$ 2,45 bi de jan–jun).
- **Painel C (Diário e Regimes):** Participação da Foxbit no volume das três corretoras saltou de 6,8% (pré) para 28,0% (pico) e 34,7% (pós-pico), acompanhado por vendas líquidas agressivas de +361,9 mn USDT entre 30/jun e 21/jul em horário comercial bancário (96,5% entre 9h e 18h).

## Caveats
0. **Denominadores:** 470–939× compara o choque incremental de prêmio com uma taxa listada de saque; 22,2× compara o choque da rota com a taxa do pool. Não são razões entre custos totais de rotas. Gas, impacto de mercado, acesso e liquidação não estão integralmente medidos.

1. **Natureza dos dados de taxas (docs/improvements_log.md, 5 Nov):** As taxas de negociação (8–10 bps, R-04/R-05) e de saque on-chain (0,1–0,2 bps, A-02/R-05) representam tabelas vigentes abertas e checadas nos provedores, e não microdados de execução histórica individualizada de junho.
2. **Ordens de grandeza vs. Identificação Causal:** A razão entre o choque regulatório (+93,9 bps) e a taxa de saque (0,1–0,2 bps) ilustra a assimetria brutal de magnitude (~500× a 900×), e não uma decomposição causal de elasticidade.
3. **Escopo estritamente cripto (F-028):** A comparação restringe-se às rotas de acesso ao dólar digital (CEX e DeFi), evitando ranqueamentos espúrios banco vs. USDT com IOF diferenciado (conforme decisão metodológica registrada em F-028).
4. **Liquidez do pool DeFi (F-037):** O pool Polygon USDC/BRLA movimentou ~US$ 5,9 milhões em 4 semanas (~0,2% do volume da Binance); o preço reflete o canal público observável na blockchain, mas grande parte da emissão de BRLA ocorre via balcão/API institucional off-pool.

## Used in deck
Slide 10 (v1, v2 e v3), Anexo B.5 e Anexo D.1.

## History
- 2026-11-07 — Codex for Felipe (P3-40): title/wording distinguish observed premium from causal attribution; original quantities unchanged.
- 2026-11-07: agent for Felipe (Economist). Created finding F-040 documenting the cost stack ("A rede não é o custo"), DeFi transmission, and the 3-panel exhibit ("Preço normal não é mercado normal") under task P3-01. Script `scripts/p3_34_cost_stack_and_recovery_figures.py` verified.

- 2026-11-07 — Codex for Felipe (P3-36): audit corrections applied; claim limits clarified; original estimates retained. Independent reproduction status is unchanged.

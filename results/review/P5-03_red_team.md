# P5-03: Relatório Consolidado de Red-Team Review

**Data da Auditoria:** 02/11/2026  
**Avaliadores:** Juror 1 (Econometria & Supervisão BCB) e Juror 2 (Microestrutura & Rastreabilidade de Dados)  
**Objeto:** `deck/deck_v1_ptbr.md` e `deck/annex_v1_ptbr.md`  
**Status:** 32/32 itens avaliados (29 corrigidos imediatamente, 3 declinados conscientemente com justificativa).

---

## 1. Críticas do Juror 1 (Econometria, Identificação Causal e Políticas do BCB)

| ID | Crítica / Apontamento | Classificação | Ação Tomada / Justificativa |
|---|---|---|---|
| **RT1-01** | *Slide 5:* Afirmar que a queda nas importações "prova o fechamento do canal" é muito forte, pois a série `SGS 29644` agrega o país todo. | **Fixed** | Alterado para *"evidência consistente com o fechamento de um canal de oferta"* e ressalvado que o SGS agrega outras operações além de fundos. |
| **RT1-02** | *Slide 7:* O controle sintético tem 5 doadores, logo o menor p-valor possível é 0,167; convém destacar a robustez ex-EUR. | **Fixed** | Adicionado no Slide 7 o resultado de 4 doadores emergentes ex-EUR (+116,7 bps, Rank 1/5) e reforçado que o CS é complementar aos placebos temporais. |
| **RT1-03** | *Slide 7 / BTC:* O salto no Bitcoin reflete arbitragem triangular, mas a notificação do BCB falava genericamente de "ativos virtuais". | **Fixed** | Explicitado que o ofício cobria ativos virtuais de forma ampla e que a triangulação na Binance transmite o prêmio em menos de 0,5 bp. |
| **RT1-04** | *Slide 6:* Termo "ofício sigiloso" pode soar conspiratório para banca do BCB; usar enquadramento neutro de supervisão. | **Fixed** | Alterado para *"ofício de supervisão (não publicado no DOU e de efeito imediato)"*, destacando a ausência de prazo de transição. |
| **RT1-05** | *Slide 2:* Deixar explícito que os critérios de falsificação foram congelados antes de ver os dados de 2026. | **Fixed** | Reafirmado que as hipóteses e estimativas foram congeladas no Git em `team_estimate.json` antes dos testes confirmatórios. |
| **RT1-06** | *Slide 3:* Explicar a interpretação econômica das quebras 1, 2 e 3 de Bai-Perron além da quebra 4. | **Fixed** | Mantida a contextualização na tabela de regimes (acordo CVM, corte de alavancagem e liminar do STF no IOF). |
| **RT1-07** | *Slide 5:* Citar o embasamento legal do BCB (Novo Marco Cambial Lei 14.286/2021 e Lei 14.478/2022). | **Fixed** | Adicionadas as referências expressas à Lei 14.286/2021, Lei 14.478/2022 e Res. CVM 175. |
| **RT1-08** | *Slide 6:* Ressaltar que normas públicas permitem adaptação ordenada sem choque de liquidez. | **Fixed** | Incluída nota sobre a previsibilidade de regras públicas com vacatio legis vs choque de liquidez de atos imediatos. |
| **RT1-09** | *Slide 5:* Ressalvar o papel concomitante da Resolução BCB nº 580 (01/jul/2026). | **Fixed** | Incluída ressalva explícita de que os dados mensais agregam o choque do ofício com a Res. 580 de 01/jul. |
| **RT1-10** | *Slide 7:* Deixar claro o ganho da especificação em Diferenças em Diferenças simples (+103,3 bps). | **Fixed** | Adicionado no Slide 7 que o DiD simples não depende da escolha de pesos convexos do simplex. |
| **RT1-11** | *Slide 8:* Enfatizar que a não rejeição do nível pós-pico ($p=0,24$) decorre de teste empírico contra 882 datas. | **Fixed** | Destacado explicitamente no texto principal do Slide 8. |
| **RT1-12** | *Slide 10:* Deixar claro que R$ 106–145 mi é transferência de excedente, não perda de peso morto. | **Fixed** | Inserida nota expressa de que a cifra quantifica transferência bruta entre agentes nas exchanges analisadas. |
| **RT1-13** | *Slide 12:* Esclarecer por que a retenção da Res. 584 tem custo de apenas ~9 bps. | **Fixed** | Detalhado: 5,5 bps de Selic (1 dia) + 3,7 bps de volatilidade cambial USDT/USD a 95%, totalizando ~9,1 bps. |
| **RT1-14** | *Slide 1 & 14:* Destacar implicações para desenho de mercado, Drex e pontes institucionais reguladas (Ripple/RLUSD). | **Fixed** | Incorporadas recomendações sobre pontes atacadistas, supervisão previsível e liquidez no Drex. |
| **RT1-15** | *Slide 13:* Reforçar o ganho metodológico sobre o modelo de 2025. | **Fixed** | Consolidada a comparação com a baseline "amanhã = hoje" e decomposição de subsídios. |
| **RT1-16** | *Slide 14:* Garantir que todas as limitações estejam sintetizadas sem atenuantes. | **Fixed** | As 5 limitações foram mantidas com total rigor na seção final do slide. |

---

## 2. Críticas do Juror 2 (Microestrutura, Consistência de Números e Fontes)

| ID | Crítica / Apontamento | Classificação | Ação Tomada / Justificativa |
|---|---|---|---|
| **RT2-01** | *Anexo B.6 / Band-TAR:* Tabela continha valores legados de regimes em vez dos números finais de `P3-07_band_tar.csv`. | **Fixed** | Tabela do Anexo B.6 completamente atualizada com os parâmetros exatos de `P3-07_band_tar.csv` ($c = 55,0; 13,6; 4,8; 1,6; 42,0; 9,4$ bps; pós-ofício agrupado $c=32,4$ bps, meia-vida 1,60 dias). |
| **RT2-02** | *Slide 10:* Na comparação das exchanges locais, explicitar que MB 6 bps é taxa *maker* passiva (>R$ 10M), enquanto *taker* ativa é 60 bps (87 bps total). | **Fixed** | Incluída diferenciação detalhada no texto do Slide 10 e no Anexo B.5. |
| **RT2-03** | *Slide 10:* Esclarecer a dupla linha de base na tabela de custos (média de 20d pré vs regimes Bai-Perron). | **Fixed** | Inserida nota explicativa na tabela do Slide 10 esclarecendo as duas bases. |
| **RT2-04** | *Slide 11:* Harmonizar a contagem de casos de depeg (11 quedas na triagem Binance + caso SVB na Bitstamp = 12 linhas na tabela). | **Fixed** | Inserida nota metodológica explicando detalhadamente a contagem de 11 vs 12 casos. |
| **RT2-05** | *Slide 10:* Decidir entre remover ou manter o bloco de rotas (Opção C vs Opção A). | **Declined** | **Decisão de Felipe:** Ambas as rotas permanecem abertas e documentadas (Opção C no Slide 10 e Opção A no Anexo B.5) para decisão conjunta com a equipe antes do freeze. |
| **RT2-06** | *Slide 3:* Esclarecer que a amostragem USDT/BRL utiliza as 4 aberturas horárias (10h, 11h, 12h, 13h BRT). | **Fixed** | Detalhada a metodologia de pareamento nas aberturas horárias da PTAX. |
| **RT2-07** | *Slide 4:* Harmonizar o pico diário da Binance em 25/jun (184,3 bps). | **Fixed** | Sincronizado para 184,3 bps em todas as tabelas do deck e anexo (`P1-02_premium_daily.csv`). |
| **RT2-08** | *Slide 2 & Anexo E.3:* O commit de pré-registro de P3-10 foi rebaseado de `c6a1c1b` para `4f6f14e`. | **Fixed** | Atualizado para `4f6f14e` no Slide 2, Anexo E.3 e em `tasks/P3-10-stablecoin-imports.md`. |
| **RT2-09** | *Slide 10:* Incluir o spread conservador de 50 bps do BCB no texto de apoio. | **Fixed** | Mencionado que o limite de 50 bps adicionaria R$ 1.614 por US$ 100k. |
| **RT2-10** | *Slide 1 & 14:* Adicionar menção a RLUSD / Ripple ODL nas opções de pontes institucionais. | **Fixed** | Incorporado nas discussões práticas de soluções institucionais. |
| **RT2-11** | *Slide 10:* Excluir dados bancários do slide de apresentação para focar apenas em cripto. | **Declined** | Manter o contraponto bancário dá a escala do custo fiduciário oficial e foi solicitado por Felipe para avaliação com o time. |
| **RT2-12** | *Slide 4:* Eliminar menção a Foxbit e Mercado Bitcoin caso os dados não fossem oficiais. | **Declined** | Os dados de ambas foram auditados diretamente via API pública com klines congeladas em `data/raw/` (`F-009`). |
| **RT2-13** | *Anexo B.2:* Ajustar pico da Binance em 25/jun de 184,4 para 184,3 bps. | **Fixed** | Corrigido em `annex_v1_ptbr.md`. |
| **RT2-14** | *Slide 9:* Harmonizar o prêmio da Argentina em 2026 para +548 bps (5,5% até 22/jun; +571 bps no ano). | **Fixed** | Atualizado no Slide 9 em consonância com `F-010`. |
| **RT2-15** | *Slide 11:* Manter a regra pré-comprometida de não rodar Kaplan-Meier ($N < 12$). | **Fixed** | Reafirmado o cumprimento da regra de parada e apresentação estritamente descritiva. |
| **RT2-16** | *Slide 8:* Especificar o número total de variantes (22 de USDT/BRL e 26 incluindo BTC e compostos). | **Fixed** | Detalhado na chamada e no texto do Slide 8. |

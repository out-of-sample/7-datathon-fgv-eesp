# P3-29: rascunho para o anexo (para revisão do Felipe, S6)

**Status:** revisado e aprovado pelo Economista (Felipe) em 7 nov 2026 (`S6` concluído). Incorporado em `deck/annex_v1_ptbr.md` (§B.10 item 2 / §B.11) como nota metodológica de auditoria de dados on-chain vinculada a `F-037` (`F-041`, `F-042`, `F-044`). Permanece fora dos 10 slides principais; aguarda reprodução final `S7` por colega (Jonathan ou Nattan) antes da submissão final do PDF.

**Figura candidata:** `results/figures/P3-29_supply_bridge.png` (gerada por `scripts/p3_29_reconcile.py figure`).

## Texto proposto (Anexo, um parágrafo + figura)

> **A oferta de BRLA vista na própria blockchain.** Na rede Celo, onde está a maior parte do BRLA (82–92% nestes dias), refizemos a oferta
> bloco a bloco entre 19 e 30/06/2026. A variação do estoque (+7,7 mi BRLA) é igual a emissões menos queimas, sem
> resíduo, em todos os dias. Por trás desse saldo há fluxos brutos muito maiores, 732,6 mi emitidos e 724,9 mi
> queimados, quase todos feitos por uma única conta. A queda que os agregadores mostram em 24/06 foi uma queima de
> 113,6 mi às 10h15 (Brasília) de 23/06. Ela não reapareceu como aumento de oferta nas outras redes listadas pela
> emissora (Polygon, Gnosis, Moonbeam). O valor de 59,3 mi que o DefiLlama mostra em 26/06 não corresponde a nenhum
> estado da blockchain. O mesmo procedimento, aplicado a 12 outros dias escolhidos por regra fixada antes, fecha sem
> resíduo em todos. **Os registros on-chain mostram quanto e quem executou, não por quê:** emissão não é entrada de
> reais, queima não é resgate, e nada aqui liga a queima de 23/06 ao ofício do BCB (a mesma conta queimou 100 mi em 19/06).

## O que não dizer
"corrida", "resgate", "migração para outra rede", "o ofício causou a queima", "o DefiLlama errou" (sem registros do
próprio DefiLlama). Para F-037: não usar o ponto de 26/06 (59,3 mi).

## Perguntas para o Felipe — Respostas e Decisão Econômica (Felipe, 7 nov 2026)
1. **Vale uma linha no anexo, ou fica só no repositório?**
   - **Decisão:** Entra no **Anexo** (`deck/annex_v1_ptbr.md`, §B.10.2) acompanhado da referência à figura `results/figures/P3-29_supply_bridge.png`, mantendo os 10 slides principais focados exclusivamente no salto de preço (`+111,0 bps` na Uniswap v3 Polygon). No anexo, demonstra rigor metodológico e auditoria primária contra artefatos de agregadores (`DefiLlama`).
2. **A frase sobre 23/06 (mesma data do ofício, sem ligação) ajuda ou distrai o júri?**
   - **Decisão:** **Ajuda e protege a credibilidade.** Como a queda de `113,6 mi` em 23/06 é o maior movimento visual do gráfico `P3-29_supply_bridge.png`, explicitar que a mesma conta (`0xbd22…855e`) já havia queimado `100,0 mi` em 19/06 e `65,7 mi` em 22/06 *antes* do ofício impede leituras causais indevidas ("corrida") e reforça nossa disciplina: a evidência econômica da rota BRLA vem do preço no pool (`+111,0 bps`), não do giro bruto de emissão/queima.
3. **Se entrar, onde: junto à rota BRLA (F-037) ou como nota de método ("como verificamos os dados")?**
   - **Decisão:** Entra no Anexo B.10 logo após o cartão de acesso `P3-28`, enquadrada simultaneamente como **nota metodológica de verificação primária on-chain** e **qualificação direta de `F-037`** (instruindo explicitamente a não usar o ponto de `59,3 mi` de 26/06).

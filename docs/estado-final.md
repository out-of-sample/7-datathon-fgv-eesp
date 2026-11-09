# Estado final da documentação — 8 nov 2026

Esta página separa **o que entrou no PDF entregue** do material de pesquisa, dos planos que ficaram pelo caminho e dos resultados ainda sujeitos a revisão. A referência da entrega é [`deck/out-of-sample_deck.pdf`](../deck/out-of-sample_deck.pdf). O relato de entrega veio de Renzo; não há comprovante de upload neste repositório. As fases e tarefas antigas continuam disponíveis como histórico, e seus campos `status` registram o estágio da revisão, não a composição do PDF.

Uma segunda exportação, `deck/apresentacao-2026.pdf`, foi adicionada em paralelo e tem conteúdo diferente. O [guia da banca](guia-da-banca.md) foi originalmente preparado com essa exportação e serve como mapa complementar de temas, achados e código; para a redação exata, use o PDF indicado por Renzo.

## Núcleo apresentado

| Peça | Estado | Leitura correta |
|---|---|---|
| [Projeto do dólar cripto](02-dolar-cripto.md), [fontes](sources.md), [F-016](../findings/F-016-event-studies-placebos.md), [F-022](../findings/F-022-robustness-battery.md) | **USADO** | Salto de +93,9 bps por 20 dias úteis; não há efeito permanente demonstrado. |
| [F-025](../findings/F-025-money-moved.md) | **USADO** | R$ 106,1 milhões de transferência estimada sobre o volume da Binance, sem medir perda social líquida. |
| [F-024](../findings/F-024-stablecoin-imports.md) e [F-014](../findings/F-014-monitor-backtest.md) | **USADO** | Compras no exterior e alarme CUSUM são evidências complementares; não identificam sozinhos o mecanismo. |
| [F-037](../findings/F-037-brla-route.md), [F-036](../findings/F-036-recovery-composition.md), [F-042](../findings/F-042-brla-celo-ledger.md) | **USADO COM RESSALVAS / EXPLORATÓRIO** | Rota BRLA, participação da Foxbit e conciliação on-chain aparecem nos slides 6–7; os arquivos de achado ainda registram revisão pendente. |
| [F-039](../findings/F-039-holder-decisions.md), [F-055](../findings/F-055-users-and-timing.md) | **USADO COMO ILUSTRAÇÃO / EXPLORATÓRIO** | Perfis e espera com hedge são retrospectivos e dependem de hipóteses de execução/acesso. |

Os achados [F-029](../findings/F-029-headline-inference.md) e [F-036](../findings/F-036-recovery-composition.md) sustentam números do slide 5 e do slide 7, mas continuam `exploratory` em seus arquivos. O README conserva a distinção. O PDF entregue não deve ser lido como revisão independente concluída desses itens.

## Planos e documentos preservados

| Documento ou grupo | Flag final | Motivo |
|---|---|---|
| [Depeg recovery](01-depeg-recovery.md) | **NÃO USADO NO PDF** | O capítulo SVB/depeg saiu da narrativa de dez slides; o estudo e os dados permanecem como pesquisa de apoio. |
| [Token incentives](03-incentives.md) | **NÃO USADO NO PDF** | A checagem de subsídio de 2025 foi feita, mas a linha de incentivos não entrou na apresentação. |
| [Treasury allocator](04-treasury-allocator.md) | **DESCARTADO COMO PROJETO** | A alternativa de alocação preditiva integral não foi adotada. Os exemplos posteriores de espera/hedge são outro escopo. |
| [Agentic robustness](05-agentic-robustness.md) | **PLANO ORIGINAL NÃO CONCLUÍDO / NÃO USADO** | O estudo de 30 analistas não virou resultado de avaliação no PDF. A investigação de fontes com IA citada no slide 2 é uma atividade distinta. |
| [Plano “so what”](06-so-what.md) | **USADO PARCIALMENTE** | Importações, custo e comparação de regras entraram; propostas e alternativas restantes são histórico. |
| [Agenda de trilhos concorrentes](competing-rails-research-agenda.md), [ranking](competing-rails-datathon-ranking.md), [proposta de melhorias](improvements-proposal.md) | **PROPOSTAS HISTÓRICAS / NÃO ADOTADAS INTEGRALMENTE** | Hipóteses e prioridades de discussão, não resultados da entrega. |
| [Plano do deck de 2 nov](deck-plan-10-slides.md), [plano v4 de 7 nov](deck-plan-v4-2026-11-07.md), [proposta de 3 nov](deck-proposal-2026-11-03.md), [notas de 2 nov](deck-notes-2026-11-02.md) | **SUPERADOS PELO PDF** | Registram decisões e versões de trabalho; o roteiro final está em [`deck/README.md`](../deck/README.md). |
| [Compressão v1](premium-compression.md), [upgrade](premium-compression-upgrade.md), [fronteira de custo](buyer-cost-frontier.md) | **EXPLORATÓRIOS / NÃO USADOS NO PDF** | Protótipos de decisão sem vantagem estabelecida ou sem acesso/execução verificados. |
| [Pesquisa de duração e decisão](shock-duration-and-holder-decisions-research-brief.md), [avaliação](shock-duration-and-holder-decisions-assessment.md) | **USO PARCIAL** | Ideias de espera/hedge apareceram no slide 8; modelos preditivos de duração não entraram como resultado validado. |
| Revisões, auditorias, notas da mentoria e [registro de decisões](README.md) | **SUPORTE E HISTÓRICO** | Documentam origem, correções e limites; não são peças adicionais da entrega. |

## Pendências que não viram resultado final por decreto

- A causa exata da queda do prêmio a partir de 22/jul, quem vendeu USDT e a origem dos tokens continuam sem identificação.
- Comparações de participação da Foxbit cobrem três corretoras e janelas históricas sobrepostas; não representam o mercado brasileiro inteiro nem identificam a causa da migração.
- BRLA/USDC é uma pool pequena e ligada às corretoras por arbitragem; não demonstra acesso operacional para um usuário real em tamanho e prazo específicos.
- Previsões para regras futuras mantêm seus prazos originais. O primeiro dia de uma regra não equivale ao veredito final.
- O PDF cita o ofício como mecanismo plausível. A evidência não separa de forma definitiva todos os eventos contemporâneos.

Para retomar uma investigação, use a tarefa e o achado correspondentes. Esta classificação de **uso na entrega** não altera retroativamente resultados, checagens nem o status científico de cada achado.

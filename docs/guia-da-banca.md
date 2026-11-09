# Guia de leitura para a banca

[Voltar ao início](../README.md) · [Abrir a apresentação de referência](../deck/out-of-sample_deck.pdf) · [Consultar as fontes](sources.md)

Este guia acompanha **“Quanto custa fechar uma porta? Um estudo sobre stablecoins, canais e o preço do dólar digital no Brasil”**, da equipe Out of Sample. Renzo identificou `deck/out-of-sample_deck.pdf` como o arquivo enviado. O guia foi redigido originalmente com outra exportação de dez slides, `deck/apresentacao-2026.pdf`, que tem texto e checksum diferentes. O mapa de temas e códigos abaixo serve para a apresentação de referência; para a redação exata, consulte esse PDF.

## A pergunta e a resposta

**Quanto o fechamento de um canal de arbitragem encarece o dólar digital, por quanto tempo e para quem?**

O USDT é um token que busca valer um dólar. No Brasil, ele pode ser comprado com reais. Quando intermediários conseguem comprar dólares no exterior, adquirir USDT e vendê-lo aqui, ajudam a aproximar os preços dos dois mercados. Essa operação é chamada de arbitragem.

Investigamos o salto de preço após o ofício do Banco Central de 23 de junho de 2026, que determinou a interrupção do câmbio de importação de ativos virtuais usado por fundos. As fontes sobre o ofício e a resposta do BCB via Lei de Acesso à Informação estão em [F-023](../findings/F-023-notice-sources-and-press-moves.md).

Nos 20 dias úteis após o ofício, o prêmio médio aumentou **93,9 pontos-base**, ou **0,939 ponto percentual**, em relação aos 20 dias anteriores. O salto aparece em três corretoras e resiste às mudanças de medida examinadas. Depois, o prêmio recua para uma faixa que não se distingue claramente das oscilações usuais.

O resultado é compatível com uma restrição no acesso ao dólar. Há um único episódio principal, com outras medidas próximas à data: os testes não isolam todos os seus efeitos nem demonstram que a ausência de aviso, sozinha, causou o salto. Veja [F-016](../findings/F-016-event-studies-placebos.md), [F-022](../findings/F-022-robustness-battery.md) e [F-029](../findings/F-029-headline-inference.md).

## Como ler os números

- **Prêmio:** quanto o USDT custa acima da referência `PTAX × preço do USDT em dólares`. O ajuste evita confundir uma mudança do próprio token com uma diferença do mercado brasileiro. A PTAX é uma referência; não é uma oferta de câmbio disponível a qualquer comprador.
- **Ponto-base (bp):** 1 bp = 0,01 ponto percentual; 100 bps = 1 ponto percentual. Um aumento de 94 bps corresponde a 0,94 ponto percentual.
- **Pico de um dia e aumento médio:** os cerca de 155 bps de 24 de junho são um nível diário. Os +94 bps são a diferença entre duas médias de 20 dias úteis. São medidas diferentes.
- **9 bps e 15 bps antes do choque:** o primeiro é o patamar do período mais longo identificado pelo teste de quebras; o segundo é a média da janela de 20 dias usada no estudo de evento. Não devem ser trocados entre si.
- **R$ 4.842 por US$ 100 mil:** conversão do prêmio adicional com a PTAX de cada dia, depois calculada a média. Os perfis do slide 8 usam 100 mil USDT e uma conta unificada; por isso há pequenas diferenças de valor.
- **R$ 106 milhões:** prêmio adicional multiplicado pelo volume negociado na Binance durante a janela do choque. Não é arrecadação de imposto nem medida de perda líquida da economia ou de lucro líquido dos vendedores. Nas três corretoras observadas, a mesma conta soma cerca de R$ 145 milhões. Veja [F-025](../findings/F-025-money-moved.md).

## Da apresentação até a evidência

Os registros `F-...` explicam o resultado, as ressalvas e como refazer a conta. Os programas `p...py` executam a análise. As saídas ficam em [tabelas](../results/tables/) e [figuras](../results/figures/), com o mesmo número da tarefa.

| Slide | O que conferir | Evidência e código |
|---|---|---|
| 1 | Título e pergunta geral | [Apresentação](../deck/out-of-sample_deck.pdf) e este guia |
| 2 | Histórico do prêmio e identificação do ofício | [F-011: mudança de patamar](../findings/F-011-blind-breaks.md), [F-023: fontes do ofício](../findings/F-023-notice-sources-and-press-moves.md); [teste de quebras](../scripts/p2_02_breaks.py), [conferência documental](../scripts/p3_14_press_check.py) |
| 3 | Definição do prêmio, horários e custos de referência | [F-006: ajuste do USDT/USD](../findings/F-006-usdcusdt-gap-fillable.md), [F-015: custos](../findings/F-015-route-costs.md); [construção do prêmio](../scripts/p1_02_premium.py), [custos por rota](../scripts/p3_01_costs.py) |
| 4–5 | Data da mudança, datas de comparação, outras moedas, corretoras e robustez | [F-016: estudo de evento](../findings/F-016-event-studies-placebos.md), [F-017: controle sintético](../findings/F-017-synthetic-control.md), [F-009: contraprovas](../findings/F-009-jump-not-venue-fx-usdt.md), [F-022: variantes](../findings/F-022-robustness-battery.md); [eventos](../scripts/p2_03_events.py), [sintético](../scripts/p2_04_synth.py), [contraprovas](../scripts/p2_05_checks.py), [robustez](../scripts/p4_01_robustness.py) |
| 5 | Comparação entre regras e janelas sem sobreposição | [F-026: oito regras](../findings/F-026-which-rules-matter.md), [F-029: limites da inferência](../findings/F-029-headline-inference.md); [comparação das regras](../scripts/p3_12_rules.py), [janelas sem sobreposição](../scripts/p4_04_inference.py) |
| 6 | Prêmio na rota Pix → BRLA → USDC e comparação com a taxa da rede | [F-037: rota BRLA](../findings/F-037-brla-route.md), [F-040: componentes do custo](../findings/F-040-network-vs-gate-cost-stack.md); [rota BRLA](../scripts/p3_24_brla.py), [comparação de custos](../scripts/p3_34_cost_stack_and_recovery_figures.py) |
| 6 | Emissões e queimas de BRLA na Celo | [F-042: conciliação](../findings/F-042-brla-celo-ledger.md), [F-044: outros períodos](../findings/F-044-brla-method-beyond-june.md), [F-049: limites da interpretação](../findings/F-049-brla-operator-routing.md); [conciliação](../scripts/p3_29_reconcile.py), [investigação das operações](../scripts/p3_36_brla_operations.py) |
| 7 | Recuo do prêmio, compras no exterior e participação das corretoras | [F-022: prêmio posterior](../findings/F-022-robustness-battery.md), [F-024: setor externo](../findings/F-024-stablecoin-imports.md), [F-036: composição](../findings/F-036-recovery-composition.md); [compras no exterior](../scripts/p3_10_imports.py), [participações](../scripts/p3_25_composition.py) |
| 7 | Vendas na Foxbit e o que sabemos sobre a recuperação | [F-031: fluxo de ordens](../findings/F-031-who-traded-the-fade.md), [F-032: associação com o prêmio](../findings/F-032-supply-response.md), [F-054: teste complementar](../findings/F-054-recovery-mechanism-check.md); [fluxo](../scripts/p3_19_supply_response.py), [checagem da recuperação](../scripts/p3_47_recovery_check.py) |
| 8 | Custo agregado e cinco perfis, incluindo o comprador ansioso | [F-025: custo agregado](../findings/F-025-money-moved.md), [F-055: perfis e espera](../findings/F-055-users-and-timing.md); [custo em reais](../scripts/p3_11_money.py), [conta unificada dos perfis](../scripts/p3_48_users_timing.py) |
| 9 | Alarme com dados passados e previsões registradas | [F-014: avaliação do alarme](../findings/F-014-monitor-backtest.md), [F-035: leitura da Res. 574](../findings/F-035-e1-res574-readout.md), [F-027: previsão para 2027](../findings/F-027-prediction-res584.md); [monitor](../scripts/p3_03_monitor.py), [leituras de novembro](../scripts/p3_20_live.py), [previsão para 2027](../scripts/p3_13_prediction.py) |
| 10 | Síntese dos resultados e questões em aberto | Registros dos slides 5–8; [F-058: dados dos gráficos finais](../findings/F-058-slide9-10-charts.md) e [programa dos gráficos](../scripts/p5_13_final_charts.py) |

Para os gráficos de histórico e de comparação entre moedas, veja também [F-057](../findings/F-057-mentor-premium-charts.md) e o [programa de preparação](../scripts/p5_12_mentor_charts.py). Os gráficos de apresentação reorganizam resultados existentes; não são novos testes independentes.

## O que os testes permitem concluir

**O salto é incomum, mas as datas de comparação não são eventos independentes.** A mudança supera as 1.073 datas comuns examinadas. Muitas janelas compartilham dias; ao usar janelas sem sobreposição, o valor-p fica em torno de 0,03. Por isso, o número de datas não deve ser lido como número de choques regulatórios independentes ([F-029](../findings/F-029-headline-inference.md)).

**O “Brasil sintético” é uma referência de comparação.** Ele combina cinco moedas para reproduzir o comportamento brasileiro anterior ao ofício. Interpretar a diferença posterior como efeito causal exige que não haja outro choque brasileiro relevante no período. A Resolução BCB 574 e outras medidas próximas limitam essa separação.

**A recuperação do preço não identifica a recuperação do canal.** Não encontramos uma reabertura publicamente verificada da rota original ([F-030](../findings/F-030-no-verified-reopening.md)). A participação da Foxbit passou de cerca de 7% para 35% **no volume das três corretoras observadas**, não no mercado brasileiro inteiro. Vendas iniciadas na corretora não identificam o vendedor, a origem dos dólares ou novas importações. O teste complementar [F-054](../findings/F-054-recovery-mechanism-check.md) não estabelece que esse fluxo tenha provocado a queda do prêmio.

**A rota em blockchain mede outro preço de acesso ao dólar.** O prêmio BRLA/USDC pressupõe que BRLA possa ser emitido e resgatado a R$ 1. A conciliação das emissões e queimas na Celo verifica os registros do token; não identifica, por si só, a finalidade econômica das operações ou uma corrida de resgates.

**Os perfis são simulações, com regras e hipóteses explícitas.** A proteção cambial usada nas contas é idealizada; acesso, liquidez e execução não foram testados. Na regra condicional de espera, o prêmio precisa superar a mediana dos 60 dias anteriores em **mais de 5 bps**. O ganho médio de R$ 197 é por data de decisão, não uma rentabilidade diária. Sem as datas do choque, a média passa a −R$ 55. Isso limita qualquer generalização sobre a vantagem de esperar ([F-055](../findings/F-055-users-and-timing.md)).

**O alarme detecta uma mudança já observada.** Ele não prevê o ofício. A regra simples de comparação também detectou 24 de junho, com mais outros alarmes. Os resultados de novembro são leituras nas janelas registradas; a Res. 589 ainda aguardava veredito em 9 de novembro na versão do PDF. A previsão de 2027 ainda não tinha resultado observado. Não detectar uma mudança incomum não prova efeito zero.

## Como refazer as contas

### 1. Consultar sem executar

Abra o registro de resultado correspondente na tabela acima. Cada arquivo traz a afirmação, os dados usados, o comando de execução e as limitações. As tabelas e figuras já salvas permitem examinar boa parte da evidência sem preparar o ambiente.

Os rótulos dos registros têm estes significados: `frozen` identifica resultados com números congelados; `confirmed`, resultados conferidos; `exploratory`, análises exploratórias, cuja revisão pode estar pendente. Um resultado não muda de categoria por aparecer na apresentação. O congelamento de 4 de novembro abrange F-001 a F-033, preservando os rótulos exploratórios existentes; análises posteriores têm registros próprios.

### 2. Preparar o ambiente e os dados

Os códigos usam Python. A versão indicada pela equipe é 3.12, com dependências em [requirements.txt](../requirements.txt). Execute a partir da pasta principal do repositório:

```sh
python -m venv .venv
```

Ative o ambiente conforme o sistema:

```powershell
# Windows (PowerShell)
.\.venv\Scripts\Activate.ps1
```

```sh
# Linux ou macOS
source .venv/bin/activate
```

Depois da ativação:

```sh
python -m pip install -r requirements.txt
```

**Os dados brutos não acompanham uma cópia comum do repositório.** Consulte [data/README.md](../data/README.md) antes de executar: ali estão a cobertura, os caminhos, os programas de coleta e as instruções para recuperar os arquivos congelados. Os códigos de verificação SHA-256 permitem conferir se um arquivo corresponde ao original.

As coletas principais são [p1_01_download.py](../scripts/p1_01_download.py), para Binance, PTAX e Coinbase, e [p1_03_second_venue.py](../scripts/p1_03_second_venue.py), para Foxbit e Mercado Bitcoin. As moedas de comparação exigem os pares adicionais listados no cabeçalho de [p1_05_donors.py](../scripts/p1_05_donors.py). O calendário [P1-04_events_brazil.csv](../data/processed/P1-04_events_brazil.csv) é uma entrada conferida manualmente, com fontes no registro documental.

Para BRLA, há arquivos históricos específicos e um pacote de respostas congeladas descritos na documentação dos dados. O acesso ao pacote depende da disponibilidade da publicação e das permissões do repositório. Uma consulta nova a uma API ou página pode não recuperar o conteúdo histórico original. A reprodução exata dessas análises exige os arquivos indicados; apenas instalar as dependências não basta.

### 3. Recalcular a análise central

Com as entradas recuperadas, execute na ordem abaixo:

```sh
python scripts/p1_02_premium.py
python scripts/p1_05_donors.py
python scripts/p2_01_noise.py
python scripts/p2_02_breaks.py
python scripts/p2_03_events.py
python scripts/p2_04_synth.py
python scripts/p2_05_checks.py
python scripts/p3_01_costs.py
python scripts/p3_02_btc.py
python scripts/p3_11_money.py
python scripts/p3_12_rules.py
python scripts/p4_01_robustness.py
python scripts/p4_04_inference.py
```

Essa sequência cobre a medição do prêmio e os testes centrais; não refaz todas as extensões dos dez slides. Para BRLA, composição das corretoras, perfis e monitor, siga os comandos e pré-requisitos dos registros vinculados na tabela. Cada programa informa suas entradas e saídas no cabeçalho. A execução pode recriar tabelas e figuras locais; para preservar a cópia consultada, use uma pasta separada para a reprodução.

### 4. Entender o alcance da verificação já salva

O [relatório de reprodução](../submission/reproduction.json) e as [instruções do pacote de códigos](../submission/README.md) registram uma execução isolada dos programas exportados, referente às versões anteriores da apresentação. Esse teste cobre o núcleo então selecionado; **não certifica automaticamente todas as extensões e os gráficos do PDF atual**. Os arquivos `.txt` em `submission/scripts/` são cópias de conveniência; os códigos de pesquisa estão em `scripts/*.py`.

Este guia organiza os materiais e confere seus caminhos. Sua preparação não representa uma nova execução completa das análises ou a aprovação das revisões pendentes.

## Outros caminhos pelo repositório

- [Fontes](sources.md): dados, documentos, notícias e referências bibliográficas.
- [Resultados](../findings/): inclui análises complementares, resultados negativos e investigações que ficaram fora do PDF.
- [Situação e revisões](../STATUS.md): acompanhamento interno da equipe.
- [Histórico de decisões](README.md): escolhas de pesquisa e mudanças de escopo.
- [Tarefas](../tasks/): especificações, responsáveis e instruções de continuidade.

Há outras versões em `deck/`. Para acompanhar a entrega indicada por Renzo, use o [PDF de referência](../deck/out-of-sample_deck.pdf).

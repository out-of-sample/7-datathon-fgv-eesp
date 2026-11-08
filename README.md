# Quanto custa fechar uma porta?

**Um estudo sobre stablecoins, canais e o preço do dólar digital no Brasil**

Equipe **Out of Sample** · Renzo, Nattan, Jonathan e Felipe

7º Datathon de Moedas Digitais FGV EESP · 2026

Por que o dólar digital ficou mais caro no Brasil em junho de 2026? Estudamos o preço do USDT em reais, comparado à PTAX e ajustado pelo valor do próprio USDT em dólares. Investigamos o salto após o ofício do Banco Central de 23 de junho, sua duração e o custo para quem comprou.

## Para a banca: comece por aqui

1. **[Leia a apresentação em PDF](deck/apresentacao-2026.pdf)** — a versão de dez slides recebida em 8 de novembro de 2026.
2. **[Abra o guia da banca](docs/guia-da-banca.md)** — explica a pesquisa em linguagem simples e liga cada parte da apresentação às evidências e aos códigos.
3. **[Consulte o registro de fontes](docs/sources.md)** — reúne as fontes dos dados, das normas e das notícias, com trechos conferidos pela equipe.

O resultado central é um aumento de aproximadamente **94 pontos-base (0,94 ponto percentual)** no prêmio médio durante os 20 dias úteis após o ofício. Isso equivale a cerca de **R$ 4,8 mil a mais por US$ 100 mil**. No período, o prêmio adicional multiplicado pelo volume negociado soma cerca de **R$ 106 milhões na Binance**. Os cálculos e suas limitações estão no [guia](docs/guia-da-banca.md).

O prêmio recuou depois do pico. A pesquisa não identifica quem forneceu os dólares na recuperação nem separa completamente o ofício das outras medidas próximas à data. As análises complementares mantêm seus avisos de revisão e de caráter exploratório.

## Onde encontrar cada material

| Material | Onde está |
|---|---|
| Apresentação que orienta este guia | [PDF de dez slides](deck/apresentacao-2026.pdf) |
| Roteiro de leitura, mapa dos slides e instruções para refazer as contas | [Guia da banca](docs/guia-da-banca.md) |
| Resultados, evidências, limitações e comandos de reprodução | [Registros de resultados](findings/) |
| Programas usados nas análises | [Códigos em Python](scripts/) |
| Gráficos e tabelas já produzidos | [Figuras](results/figures/) e [tabelas](results/tables/) |
| Origem, cobertura e recuperação dos dados | [Documentação dos dados](data/README.md) |
| Fontes documentais e bibliográficas | [Registro de fontes](docs/sources.md) |

É possível ler a apresentação, consultar as evidências e examinar os códigos sem instalar programas. Para executar as análises, veja a seção de reprodução no [guia da banca](docs/guia-da-banca.md).

## Para quem acompanha o desenvolvimento

O repositório também preserva versões anteriores, hipóteses descartadas e estudos complementares. Esses arquivos documentam o processo e não substituem a apresentação acima.

- [Situação do projeto e revisões pendentes](STATUS.md).
- [Planos e histórico de decisões](docs/README.md).
- [Etapas do trabalho](docs/phases.md) e [tarefas](tasks/).
- [Orientações de trabalho da equipe e dos agentes](prompt.md).

Os nomes `P2-03`, `P3-48` etc. identificam tarefas; `F-016`, `F-055` etc. identificam registros de resultados. Esses códigos permitem seguir uma afirmação até a análise que a produziu.

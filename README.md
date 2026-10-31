# Out of Sample — 7º Datathon de Moedas Digitais FGV EESP (2026)

**Project:** "Quanto custa fechar a porta? O preço do dólar digital no Brasil": how much more Brazilians pay
for a digital dollar (USDT) than for the official dollar (PTAX), and how much of that gap comes from rules that
close or tax the arbitrage channels.

## Start here

| If you want to… | Open |
|---|---|
| See where the project stands today | [`STATUS.md`](STATUS.md) |
| Understand the plan | [`docs/02-dolar-cripto.md`](docs/02-dolar-cripto.md) and [`docs/README.md`](docs/README.md) |
| See phases and what "done" means for each | [`docs/phases.md`](docs/phases.md) |
| Pick up or check a task | [`tasks/`](tasks/) (one file per task) |
| Check a result and how to reproduce it | [`findings/`](findings/) (one file per result) |
| Brief an AI agent | [`prompt.md`](prompt.md) (agents read it automatically via `CLAUDE.md` / `AGENTS.md`) |

## Layout

```
STATUS.md        dashboard: current phase, next actions, blockers, generated board
prompt.md        brief and working protocol for AI agents (humans: §5–§7 are worth reading)
docs/            plans, phases, decision log, source register
tasks/           one file per task (front matter: id, phase, status, owner, due, depends)
findings/        one file per result (claim, evidence, how to reproduce, status)
scripts/         analysis code; scripts/board.py rebuilds the board in STATUS.md
data/            raw/ (frozen, checksummed) and processed/ — not in git, see data/README.md
results/         figures/ and tables/ produced by scripts, prefixed with the task ID
```

## Common commands

```bash
python scripts/board.py              # refresh the board in STATUS.md after editing tasks/findings
python scripts/00_probe_premium.py   # day-0 probe (download instructions in its header)
```

# Agent Brief — Team "Out of Sample", 7º Datathon de Moedas Digitais FGV EESP (2026)

> **Post-submission note (8 Nov 2026):** Renzo reports that the work was delivered. The reference
> presentation in this repository is [`deck/out-of-sample_deck.pdf`](deck/out-of-sample_deck.pdf),
> ten pages; see [`docs/estado-final.md`](docs/estado-final.md) for used, unused and exploratory work.
> Deadline, task and `.txt` export instructions below document the preparation period. The team's
> later decision was to submit a PDF and repository link, without `.txt` exports. Do not interpret
> unchecked historical gates as a request to modify the delivered PDF or promote exploratory findings.

Read this file completely before you run a command, write code, or give advice. Then read `STATUS.md`
(current state), `docs/README.md`, and the task file you were asked to work on. §7 is the working protocol. If anything here conflicts with a direct
instruction from a team member, the team member wins; tell them about the conflict.

---

## 1. Your role

You are a research engineer and critical reviewer on a four-person undergraduate team competing in a
ten-day data competition judged by economists. Your job is to help the team produce **one credible,
well-explained economic finding** about digital currencies, delivered as a PDF presentation plus scripts.

You are not here to maximise model complexity, produce impressive-looking numbers, or agree with the team.
When a plan, result, or claim is weak, say so directly, explain why, and propose the smallest fix.

## 2. The competition (source: official regulation)

| Item | Fact |
|---|---|
| Organiser | FGV EESP, Centro de Estudos FGV Digital Finance; supported by FGV/Ripple (UBRI) and USP-UBRI |
| Theme | Real problems in the crypto-asset and digital-currency ecosystem |
| Stated goal of the event (Art. 1) | "Desenvolver e aplicar conceitos econômicos, combinando a prática à teoria" |
| Data (Art. 6) | Any data source is allowed **if cited** |
| Deliverable (Art. 7) | **One PDF presentation** + scripts as **`.txt` files** (preferably Python, R or Stata). **Team decision 5 Nov (Renzo): submit the GitHub link + 10-slide PDF; no `.txt` export** |
| **Deck length (team rule, 2 Nov)** | **At most 10 slides.** Anything else goes to the annex |
| Recommended deck structure (Art. 7) | Motivação → Delimitação do problema → Dados e metodologia → Resultados → Discussão e implicações |
| Supplementary material (Art. 8) | Tables and annexes may be included |
| Deadline | **8 Nov 2026, 23:59 (Brasília). No late files, no replacements after the deadline.** |
| First-round selection | 5 finalists chosen **from the PDF alone**, announced by 12 Nov 2026 23:59 |
| Final | Oral presentation on 16 Nov 2026; time limit sent to finalists by e-mail |
| Judging (Art. 8, item 19) | Quality of the solution and material **+ relevance of the problem + creativity** |
| Prizes | R$ 7,000 / 5,000 / 3,000; winners present at the 2nd Blockchain Day FGV on 25 Nov 2026 |

Sources: [event page](https://eesp.fgv.br/evento/7o-desafio-de-dados-datathon-de-moedas-digitais-da-fgv-eesp),
[regulation PDF](https://eesp.fgv.br/sites/default/files/uploads/regulamento-do-desafio-de-dados-de-moedas-digitais-fgv-2026_0.pdf).

Consequences you must respect:

- **The PDF is the product.** It must be understandable with nobody presenting it. Dashboards, web apps and
  packaging work earn nothing in the first round.
- **Scripts are submitted as `.txt`.** Keep them few, linear, commented and runnable top-to-bottom. No
  frameworks, no package scaffolding.
- **Relevance and creativity are scored explicitly.** Every piece of work should strengthen the economic
  question, the evidence, or the explanation.
- **Deck language:** Portuguese (pt-BR) unless the organisers say otherwise. Code comments may be in English
  or Portuguese.

## 3. The team

- Team name: **Out of Sample**. Four undergraduates: three with CS / ML / data-science backgrounds, one economist.
- Placed **3rd in the 6th edition (Nov 2025)** with "Quantificando o Risco DeFi vs RWA: Modelagem e Previsão do
  Spread" ([repo](https://github.com/Renzo-Filho/6-datathon-fgv-eesp)). It predicted the spread between
  Aave/Compound USDC yields and SOFR using K-Means regimes with per-regime regressors, GARCH and a TFT model.
- Members of last year's jury may remember that work. **This year's submission must look clearly more mature.**
  See `docs/README.md` → "Lessons from 2025". In short: last year's best model lost to a naive
  "tomorrow = today" forecast, causal language was drawn from clustering, and Brazil appeared only in the
  introduction.

## 4. Current strategy (check `docs/README.md` for the live decision log)

Four candidate projects are documented in `docs/`:

| File | Project | Recommended status |
|---|---|---|
| `docs/02-dolar-cripto.md` | The USDT/BRL premium over PTAX and the rules that move it | **Primary project** (since 30 Oct, after the probe in `scripts/00_probe_premium.py`) |
| `docs/01-depeg-recovery.md` | What brings a stablecoin back to $1? | Chapter of the primary (2–3 slides); full plan kept as fallback |
| `docs/03-incentives.md` | Token incentives and capital retention | One "lessons" slide (subsidy share of the 2025 spread); full study only if the primary fails |
| `docs/04-treasury-allocator.md` | Forecast-driven treasury allocation | Not recommended; kept as documented fallback |
| `docs/05-agentic-robustness.md` | AI agents as research tools: A (30 AI analysts), B (AI event coder) | Optional extensions of the primary; go/no-go at the Sun 1 Nov gate |

File numbers are historical: project 2 is the primary. Execution follows the phases in `docs/phases.md`.

The thread that ties the primary project and its chapter together is **limits to arbitrage**: when
the channel that enforces a price parity (issuer redemption, or the official FX market) is closed or
expensive, the market price drifts away from parity. The team has not frozen this decision yet. Do not
start building a project that the decision log does not list as active.

`docs/README.md` also records what won past editions and who sat on the jury. Read it before proposing
changes in scope.

## 5. Non-negotiable research standards

1. **One primary question, one primary metric**, written down before final results are produced.
2. **Always report a naive baseline** (persistence, historical mean, or no-model comparison) next to any
   model. A model that does not beat it is reported as such.
3. **No look-ahead.** Features use only information available at decision time. Time-series data is split
   chronologically, never randomly. Overlapping targets are purged at split boundaries.
4. **No causal language without a causal design.** Clustering, correlation and prediction do not prove causes.
   Use event studies, difference-in-differences, placebo dates, or survival models with stated assumptions,
   and say what would falsify the claim.
5. **Count independent events, not rows.** Thousands of minutes inside one depeg are one event.
6. **Units are explicit:** APR vs APY, % vs basis points, BRL vs USD vs USDT, UTC vs Brasília time.
7. **Every number in the deck must trace to a script and a cited source.** Keep a source register.
8. **Disclose everything you tried**, including variants that failed. Do not tune on the final test period.
9. **Negative or null results are reported honestly**, framed as what they teach (e.g., "redemption access
   does not explain recovery speed; backing type does").

## 6. How to work

- **Sources are opened, not remembered.** A link enters `docs/sources.md` only if whoever adds it (person or
  agent) opened that exact address and copied it from the page. The entry quotes one line from the page and says
  who opened it and when ("opened 2 Nov 2026 (Renzo)"). Describe only what the page says. An agent that cannot
  open a page writes `[link not opened]` instead of a guessed address. Decided 2 Nov after 4 of 4 agent-written
  event links failed (P1-04).
- **Verify before you claim.** Anything marked `[verify]` in the docs is unconfirmed: a date, an event,
  a data source's coverage, an API's behaviour. Check it against a primary source before it reaches the
  deck. Never invent data, events, dates, citations or results. If you cannot verify something, say so.
- **Check data first.** Before writing analysis code, download a small sample, inspect coverage, gaps,
  timestamps and units, and report what you found.
- **Smallest working version first.** Get one event (or one day) end to end, from raw data to a figure,
  before scaling up.
- **Stay in scope.** Do not add projects, models, dashboards or infrastructure that the active plan does
  not call for. Propose additions; do not build them unasked.
- **Keep raw data immutable.** Save downloads under `data/raw/` with source URL and retrieval date. Derived
  tables go under `data/processed/`. Large files stay out of git.
- **No secrets in the repo.** API keys go in environment variables or an untracked `.env`.
- **Ask before outward-facing actions**: opening PRs, posting anywhere, contacting organisers, or using
  paid services. Pushing to GitHub follows §7 (end of every session, after telling the team member).
- **Log decisions.** When the team changes scope or a plan, update the decision log in `docs/README.md`.
- **Write for the jury.** When drafting deck text, write for economists and lawyers who know finance but
  not DeFi internals. Plain Portuguese, one idea per slide, a chart that carries the finding.

## 7. Working protocol (team + agents)

Several people and agents work on this repo in parallel. Everything that matters lives in files, so that a
teammate or a new agent can understand the current state in two minutes.

| What | Where | Updated by |
|---|---|---|
| Current state, next actions, blockers, progress board | `STATUS.md` | every session; board via `python scripts/board.py` |
| Phases, goals, success criteria, gates | `docs/phases.md` | the team, at gates |
| Work items | `tasks/PX-YY-name.md`, one file per task | the task owner (or their agent) |
| Results | `findings/F-NNN-name.md`, one file per result | whoever produced it |
| Decisions | `docs/README.md` → Decision log | whoever the team asks |
| Sources | `docs/sources.md` | whoever uses a new source |
| Data | `data/raw/` (frozen, checksums), `data/processed/PX-YY_*` | the task owner |
| Code and outputs | `scripts/pX_YY_name.py`; `results/figures/PX-YY_*`, `results/tables/PX-YY_*` | the task owner |

**Work is shared and handed over.** One person may start a task and another may finish it, sometimes
the next day. A task file must therefore always say who is on it (`working`), which subtasks are done or in
progress (`## Subtasks`), and exactly where to continue (`## Handoff`). The GitHub copy is the truth: work
that is not pushed does not exist for the rest of the team.

**Start of every session**
1. `git pull --rebase`. Then read this file, `STATUS.md`, the current phase in `docs/phases.md`, and your
   task file, **starting with its Handoff section**.
2. Run `git log --oneline -10` to see what changed since `STATUS.md` was last updated.
3. Confirm with the team member which task ID (and which subtasks) you are working on.
   - If `working` names someone else, do not touch the task until the team member has checked with that
     person. Two people never work on the same subtask.
   - Claim it: `working: <name>`, `status: doing`, mark the subtask `— doing: <name>`, add a log line.
     Commit and push the claim right away (`P1-01: Renzo takes S2`) so the others see it.
   - If the task says "write the subtasks when the phase starts", write them first (S1, S2, …, each small
     enough for one session) and show them to the team member before executing.

**While working**
- One task at a time, and only what its file asks. Work you discover becomes a new task file (next free ID
  in the right phase, `status: todo`), not a detour. Copy `tasks/_TEMPLATE.md`.
- If two people need to work on the same task at the same time, move the remaining subtasks they will do
  into a new task file, so each file has one active worker.
- Blocked for more than about an hour: set `status: blocked`, write what is needed and from whom, and add it
  to the blockers table in `STATUS.md`.
- Every number you report goes into a finding file (copy `findings/_TEMPLATE.md`) with the exact command that
  reproduces it. No number lives only in a chat.
- Write goals, claims and results so a teammate who did not do the work understands them: plain words,
  units, one idea per sentence. Explain any technical term the first time.

**End of every session (also when you stop halfway)**
1. Task file:
   - tick finished subtasks (`— done: <name>, <date>`) and met criteria; add a log line;
   - **overwrite the Handoff section**: state, exact next step, open questions, how to resume (commands,
     half-done files). Someone who has never seen the task must be able to continue from it;
   - `status`: `paused` and `working: -` if unfinished and you stop; `review` when the criteria are met and
     a teammate should check; `done` after that check; `dropped` with the reason in Result.
2. Findings: create or update them. Status `exploratory` → `confirmed` when the task's criteria pass;
   `frozen` only in P4; `retracted` with the reason, never deleted.
3. `STATUS.md`: "Last updated", "Where we are" if it changed, Next actions, Blockers, and one line in
   Recent activity.
4. Run `python scripts/board.py`.
5. Commit (message starts with the task ID) and push, after telling the team member. They may tell you to
   push without asking each time.
6. Tell the team member, in five lines or fewer: what changed, what is next, what needs their decision.

**Naming:** task `P2-03-event-studies.md` → script `scripts/p2_03_events.py` → outputs
`results/figures/P2-03_*.png`, `data/processed/P2-03_*.csv`; findings `F-006-short-name.md` (next free number).

**Git:** everyone works on `main` with small commits; the message starts with the task ID
(`P2-03: placebo dates`). Pull with `git pull --rebase` before starting and before pushing. Open PRs or change
GitHub settings only when asked. Never force-push, never rewrite history, never commit `data/` or secrets.

**Conflicts:**
- Board block in `STATUS.md`: keep either side, then re-run `python scripts/board.py`.
- Recent activity in `STATUS.md`: keep both lines.
- A task file: the person named in `working` wins; otherwise ask the team.
- Anything else: stop and ask the team member.

**Parallel work:** edits to `STATUS.md` stay small (your own rows, one line in Recent activity). Finding
files belong to whoever created them; others add to History. If two tasks need the same script, coordinate
in the task logs.

**Gates:** at the end of each phase the team ticks the criteria in `docs/phases.md` and logs the outcome in
the decision log. Agents prepare the evidence for a gate; they never decide it.

**Key dates (Brasília time; detail in `docs/phases.md`):** P1 Sat 31 Oct · P2 gate Sun 1 Nov evening ·
results v1 Tue 3 Nov · **freeze Wed 4 Nov** · deck v1 Thu 5 · red team Fri 6 · scripts to `.txt` Sat 7 ·
**submit by 20:00 Sun 8 Nov** (hard deadline 23:59) · finalists Thu 12 · oral final Mon 16 Nov.

## 8. Definition of done (submission)

- [ ] One question, stated on slide 2, answerable with the evidence shown
- [ ] A "Lições de 2025" slide showing what changed in method since last year
- [ ] Data slide: sources, coverage dates, event counts, exclusions
- [ ] Method slide: design, baseline, and what would falsify the hypothesis
- [ ] One headline chart that a reader understands in ten seconds
- [ ] Robustness: at least two alternative thresholds, windows or samples
- [ ] Limitations and policy or practical implications (Brazil where possible)
- [ ] References and source register
- [ ] Scripts exported as `.txt`, each starting with a header: purpose, inputs, outputs, how to run
- [ ] PDF and scripts checked against the regulation; uploaded with a margin before the deadline

## 9. Open items to fill in

- Notes from the 30 Oct opening briefing (topics FGV/Ripple highlighted, any datasets offered):
  _to be added by the team in `docs/README.md`_
- Oral presentation time limit (arrives by e-mail if the team becomes a finalist)
- Confirmation of the deck language and of the upload method

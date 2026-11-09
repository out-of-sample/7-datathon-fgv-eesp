# Extension — AI agents as research tools (A: 30 AI analysts; B: AI event coder)

> **Estado na entrega (8 nov 2026): PLANO NÃO CONCLUÍDO / NÃO USADO COMO RESULTADO — o experimento de 30 analistas não integrou o PDF.** Veja [estado final](estado-final.md).

**Status:** optional extras to the primary project (`02-dolar-cripto.md`), kept by the team on 31 Oct.
Go/no-go for each at the **Sun 1 Nov gate** (`phases.md`). Dropping either changes nothing in the primary.
**Owner:** CS 3 (validation). If A is a go, the depeg chapter shrinks to the single SVB-weekend slide.

Why AI agents at all: the 2025 1st and 2nd places both had "IA" in the title, and agentic AI is now part of
economics research practice (Korinek 2025). We use agents where they **add rigor** (checking our result and
our data), not as the source of the result.

---

## A. 30 AI analysts: same question, same data

### In one line

Our confidence interval says how much our number would move if the data were slightly different. It does
not say whether **another competent analyst** would get the same number from the same data. That second
uncertainty is a *nonstandard error* (Menkveld et al. 2024: 164 human teams, same data, widely different
answers). Gao & Xiao (2026) measured it with 150 AI coding agents on US market data and said other domains
are an open question. We run a small version on our question.

### What we'd do

1. **Frozen data bundle** with the raw files only: USDT/BRL 1h klines, PTAX JSON, USDC/USDT 1h klines, plus
   the providers' public documentation of the columns (what any human analyst would have).
   Not our processed premium: that would impose our main measurement choice.
2. **One prompt, identical for every agent** (draft below). It does not mention our results.
3. **Pre-registration:** commit this protocol, the final prompt, the bundle checksums, the number of runs and
   the models **before** any run. The commit timestamp is the proof.
4. **Memory test:** ask each model, with no tools, what it knows about Brazilian stablecoin regulation on
   23 Jun 2026. Record the answers verbatim.
5. **Runs:** ~30 runs (about 10 per family: Claude, GPT, Gemini), each in a fresh, isolated folder with
   **no web access** and **no access to this repo**.
6. **Order rule:** our own before/after estimate is committed (task P2-06) before anyone opens agent results.
7. **Analysis:** share of agents finding a rise; median and interquartile range of estimates; dispersion
   across agents vs our standard error; regression of estimates on the coded choices (premium definition,
   time matching, USDT adjustment, window, estimator) to find which choice drives disagreement.

### Illustrative example (numbers invented)

Agent 7 compares the Binance price at 00:00 UTC with PTAX, 30 days before and after: +82 bps. Agent 19 matches
the PTAX window, uses 60-day windows and adjusts for USDT/USD: +71 bps. Agent 28 misses that Binance files
from 2025 use microsecond timestamps and reports −3 bps; it is reported as a failed run with the reason.
Possible slide: *"28 de 30 agentes encontram alta; metade entre 65 e 90 bps; nossa estimativa 88 ± 10 bps;
a escolha da janela explica a maior parte da divergência."*

### Why

- Answers the jury's natural question, "would someone else find this?", which is normally unaffordable.
- New: applies a March 2026 method to a domain its authors flagged as open.
- Shows AI checking our rigor, which fits the "Lições de 2025" story.
- Both outcomes are useful: agreement = robustness; disagreement = a finding about measurement.

### What it does not show

The agent estimates are not extra causal evidence about the 23 Jun notice. They measure how sensitive the
before/after estimate is to analysis choices. Agents from one model family share habits, so they are not
independent analysts; that is why we use three families and report results per family.

### Comparison target

Compare the agents with **our simple before/after estimate around 23 Jun** (primary plan §7.3), not with the
synthetic control. Agents only get Brazil's data, so the before/after question is the like-for-like one.

### Draft prompt (freeze in task P3-05)

> You are an empirical economist. The folder `data/` contains hourly USDT/BRL prices from Binance, the
> Brazilian central bank's official dollar rate (PTAX) and hourly USDC/USDT prices, with the providers'
> documentation in `docs/`. Question: did the price of USDT in reais, relative to the official dollar,
> change after 23 June 2026, and by how much? Estimate the change in basis points with a standard error.
> Make and justify your own analysis choices. Use only the files provided. Write your code to
> `analysis.py`, your answer to `answer.json` (schema below) and a short explanation (≤ 300 words) to
> `report.md`.

### Answer schema (agents and our own estimate use the same one)

```json
{
  "run_id": "A-07",
  "model": "<model name and version>",
  "direction": "up | down | no change",
  "estimate_bps": 0.0,
  "std_error_bps": 0.0,
  "premium_definition": "<formula in words>",
  "time_matching": "<how USDT/BRL and PTAX were aligned in time>",
  "usdt_usd_adjustment": false,
  "window_pre_days": 0,
  "window_post_days": 0,
  "estimator": "<difference in means, regression, ...>",
  "controls": [],
  "data_issues_found": [],
  "notes": ""
}
```

### Rules that keep A possible while the primary runs (apply from day 1)

1. Raw files are frozen with checksums as soon as they are downloaded (task P1-01).
2. The agents' bundle lives outside the repo (`data/agentic_bundle/`, git-ignored). The sandbox mounts only
   that folder; `docs/` contains our numbers and must never be visible to the agents.
3. Our own estimate is recorded in the answer schema above (task P2-06).
4. Our estimate is committed to git before any agent result is opened.

### How the runs are paid for and executed (decided 31 Oct, P1-08)

No API spend. The runs use Renzo's existing entry-level paid plans through each plan's coding agent in the
terminal: **Claude Code** (Claude), **Codex CLI** (ChatGPT), **Gemini CLI** (Gemini). That gives three model
families, about 10 runs each.

What this changes:
- **The cap is usage limits, not money.** Report the number of runs actually completed per family; do not
  top up one family to compensate for another.
- **Runs execute on Renzo's accounts and machine.** Jonathan prepares the bundle, prompt and harness;
  Renzo launches the runs (or lends the session). Claude runs share limits with Renzo's development work, so
  schedule them outside working hours (e.g., Mon night).
- **Isolation has to be configured per CLI** (P3-05): a fresh folder with only the bundle, web tools off,
  no network for the agent's shell where supported, and none of Renzo's personal instruction or memory files
  loaded. The CLI still talks to its own model service; "no internet" means the agent cannot browse.
  Each setup is tested before the runs.
- **Model versions:** pin the model in each CLI and record the exact name per run; consumer plans can route
  to different models.
- Whether each plan includes its CLI at the needed volume is `[verify]` in the pilot.

Extension B can use the same plans' chat apps with web search on (that task needs the web).

---

## B. AI event coder for the comparison countries

### What we'd do

1. An agent with web search lists, for Brazil and the comparison currencies (TRY, ZAR, UAH, EUR, MXN, COP,
   PLN, IDR, ARS), every rule or event from 1 Nov 2025 to 30 Sep 2026 that changed access to foreign currency
   or crypto: date, description, source URL, type (tax / restriction / reporting / exchange outage / other).
2. Human benchmark: the economist's verified Brazil list (task P1-04) plus two comparison countries coded by
   hand by a teammate.
3. Report **precision** (share of the agent's events that are real and correctly dated), **recall** (share of
   the human events the agent found) and **agreement on type** (Cohen's kappa).
4. Only events with a human-checked primary source are used: to remove from the synthetic control any
   currency with its own shock between 1 Jun and 31 Jul 2026.

### Illustrative example (hypothetical events)

The agent returns "Turkey, 21 Jun 2026: central bank changes crypto withdrawal limits [link]". A human opens
the link, it is real, and Turkey leaves the June comparison pool. It also returns "Mexico, 15 Jul 2026:
Banxico restricts…" but the link does not say that: one error, precision goes down, and we report it.

### Why

The synthetic control is only as good as its comparison pool, and checking 9 countries by hand in a day is
not realistic. The agent covers breadth and humans verify. Precedent for validating LLM coding against
humans: Gilardi, Alizadeh & Kubli (2023, PNAS); Hansen & Kazinnik (2023) on Fed communication.

### Output

`data/processed/P1-06_events_donors.csv` (verified events only) and a short accuracy table for one annex slide.
If B is not done by the Sun 1 Nov gate, a human screens the donors and we say so.

---

## Not doing (and why), for the record

| Idea | Reason |
|---|---|
| Agent that explains breaks in the monitor | Search returns documents written after the date and models may remember events; no clean test in 9 days. Allowed only as a labelled demo |
| Project on x402 / XRPL agentic payments | TRM Labs (Sep 2026) already measured it (0.6–7.5% of value looked agentic); no Brazilian data |
| LLM trading agents | Lookahead bias (Gao, Jiang & Yan 2025/26); too few post-cutoff months for power; same genre as the 2025 winner |
| LLM personas reacting to IOF / 24h hold | Cannot be validated; LLM "traders" do not replicate human behaviour |

## References

- Gao, R. & Xiao, S. C. (2026). Nonstandard Errors in AI Agents. arXiv:2603.16744.
- Menkveld, A. et al. (2024). Nonstandard Errors. *Journal of Finance*.
- Korinek, A. (2025). AI Agents for Economic Research. NBER Working Paper 34202.
- Gao, Z., Jiang, W. & Yan, Y. (2025, rev. 2026). Detecting Lookahead Bias in LLM Forecasts. arXiv:2512.23847.
- Gilardi, F., Alizadeh, M. & Kubli, M. (2023). ChatGPT outperforms crowd workers for text-annotation tasks. *PNAS*.
- Hansen, A. & Kazinnik, S. (2023). Can ChatGPT decipher Fedspeak? Working paper `[verify venue]`.
- TRM Labs x402 study, reported by PYMNTS, 15 Sep 2026.

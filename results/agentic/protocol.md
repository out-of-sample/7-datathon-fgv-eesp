# Pre-Registered Protocol: 30 AI Analysts on the USDT/BRL Premium

**Project:** 7º Datathon de Moedas Digitais FGV EESP (2026) — Team Out of Sample  
**Task:** P3-05 (Extension A: Nonstandard Errors via Autonomous AI Coding Agents)  
**Status:** Pre-registered before any agent execution  
**Frozen Team Estimate:** `results/agentic/team_estimate.json` (committed in `80fc866`, +93.9 bps, SE 16.2 bps)  
**Bundle Checksums:** `results/agentic/bundle_SHA256SUMS.txt` (SHA-256 of frozen provider data)  

---

## 1. Scientific Objective and Background

Econometric confidence intervals quantify sampling variation under a fixed specification. They do not quantify **nonstandard errors**—the dispersion across competent analysts making independent specification choices on identical data (Menkveld et al. 2024; Gao & Xiao 2026).

In March 2026, Gao & Xiao showed that autonomous LLM coding agents exhibit nonstandard errors comparable to human teams when given raw market data and an empirical research question. They flagged non-US markets and emerging-market stablecoin dynamics as open empirical questions.

Here we deploy 30 autonomous AI coding agent runs across three leading frontier model families on the identical raw data bundle and prompt. Our goal is to determine:
1. **Consensus Direction:** Do independent AI analysts converge on the direction of the USDT/BRL premium change around 23 June 2026?
2. **Dispersion vs. Standard Error:** Is the dispersion across AI analysts (nonstandard error) larger or smaller than our econometric sampling error ($16.2$ bps)?
3. **Driver of Disagreement:** Which methodological choice (time-matching window, USDT/USD adjustment, sample window length, or estimator) accounts for the largest share of variance across agent estimates?

---

## 2. Frozen Prompt

Each agent run is presented with the following exact prompt in a file named `PROMPT.txt`:

```text
You are an empirical economist. The folder `data/` contains hourly USDT/BRL prices from Binance, the Brazilian central bank's official dollar rate (PTAX) and hourly USDC/USDT prices, with the providers' documentation in `docs/`. Question: did the price of USDT in reais, relative to the official dollar, change after 23 June 2026, and by how much? Estimate the change in basis points with a standard error. Make and justify your own analysis choices. Use only the files provided. Write your code to `analysis.py`, your answer to `answer.json` (schema below) and a short explanation (≤ 300 words) to `report.md`.
```

No additional guidance, leading questions, hypotheses, or hints are provided.

---

## 3. Standardized Output Schema

Each agent is required to write its quantitative results to `answer.json` conforming to this schema:

```json
{
  "run_id": "A-01",
  "model": "<model name and exact version string>",
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
  "notes": "<concise summary of findings>"
}
```

Our own pre-registered estimate (`results/agentic/team_estimate.json`) adheres to this identical schema:
- `direction`: `"up"`
- `estimate_bps`: `93.9`
- `std_error_bps`: `16.2`
- `premium_definition`: `"USDTBRL_open / (PTAX_sell x USDTUSD_open) - 1, hourly mean in 13-16h UTC window, expressed in basis points"`
- `time_matching`: `"PTAX window: 4-hour window (10:00-13:00 BRT / 13:00-16:00 UTC) matching the BCB PTAX calculation window on trading days"`
- `usdt_usd_adjustment`: `true`
- `window_pre_days`: `20`
- `window_post_days`: `20`
- `estimator`: `"difference in means (OLS with Newey-West HAC Bartlett kernel, maxlags=5)"`

---

## 4. Data Bundle and Provider Documentation

The data bundle is prepared by `scripts/p3_05_build_bundle.py` and placed in `data/agentic_bundle/`. Its cryptographic integrity is recorded in `results/agentic/bundle_SHA256SUMS.txt`.

Contents:
1. `data/binance/USDTBRL/*.zip`: 102 monthly and daily hourly kline archives from Binance Spot (October 2020 – October 2026).
2. `data/binance/USDCUSDT/*.zip`: 119 monthly and daily hourly kline archives from Binance Spot.
3. `data/binance/BUSDUSDT/*.zip`: 52 monthly hourly kline archives from Binance Spot (delisted December 2023).
4. `data/bcb/ptax.json`: Official daily PTAX quotation records from BCB Olinda API (1,527 trading days).
5. `docs/DATA_README.txt` & `DATA_README.txt`: Public documentation of provider formats:
   - Binance 12-column headerless CSV specification.
   - Binance timestamp epoch unit change (milliseconds prior to 2025; microseconds starting January 2025).
   - BCB Olinda PTAX JSON schema (`cotacaoCompra`, `cotacaoVenda`, `dataHoraCotacao` in Brasília local time UTC-3).
   - **Zero mention** of 23 June 2026, research hypotheses, or team results.

---

## 5. Model Families and Execution Plan

Runs are executed using Renzo's entry-level paid subscription plans across three distinct model families:

| Family | CLI Tool | Pinned / Recorded Model | Target Runs | Run IDs |
|---|---|---|---|---|
| Anthropic | Claude Code CLI (`claude`) | `claude-3-7-sonnet` (or `claude-3-5-sonnet`) | 10 | `A-01` to `A-10` |
| OpenAI | Codex CLI (`codex`) | `gpt-4o` / `o3-mini` | 10 | `B-01` to `B-10` |
| Google | Gemini CLI (`gemini`) | `gemini-2.0-flash` / `gemini-2.0-pro` | 10 | `C-01` to `C-10` |

### Plan Rules:
- **No API Spend:** Runs leverage existing subscription quotas.
- **Quota Cap:** If rate limits prevent exactly 10 runs for a given family, the actual completed runs are reported; runs from another family are **never** used to substitute or top up another.
- **Model Version Pinning:** The exact model string returned by each CLI must be logged in `answer.json` and `run.log`.

---

## 6. Strict Isolation Protocol

To guarantee that each agent run represents an independent analysis without data contamination or prompt leakage:

1. **Clean Ephemeral Working Directory:**
   Each run executes in a newly generated temporary directory (e.g. `/tmp/agent_run_<family>_<run_id>` or `%TEMP%\agent_run_<family>_<run_id>`).
   The directory contains ONLY:
   - `data/` (copied from `data/agentic_bundle/data/`)
   - `docs/` (containing `DATA_README.txt`)
   - `DATA_README.txt`
   - `PROMPT.txt`
2. **Zero Repository Context:**
   The repository root, `.git/`, `findings/`, `docs/`, `scripts/`, and processed tables are strictly inaccessible.
3. **Web Search Disabled:**
   Agent web browsing and search tools must be explicitly disabled via CLI parameters or settings.
4. **No Global Memory or Instructions:**
   Global instruction files (e.g. `~/.claude/CLAUDE.md`, `~/.codex/AGENTS.md`, `~/.gemini/GEMINI.md`) must not be loaded. Isolation flags (e.g., `--bare`, custom empty config paths, or environment overrides) must be applied.
5. **Execution Verification:**
   Before production runs, isolation tests (`results/agentic/isolation_test.md`) confirm that web browsing and outside file access are blocked.

---

## 7. Memory Test (Prior Knowledge Verification)

Because the event occurred on 23 June 2026, LLMs with training cutoffs before mid-2026 cannot have memorized the event or subsequent academic analyses. However, models with late cutoffs or internal retrieval could possess pre-existing beliefs.

Before the coding runs, each model family is queried in a clean zero-shot terminal/chat session with web search disabled:
> *"What changes or regulatory notices occurred regarding Brazilian stablecoins and crypto foreign exchange on 23 June 2026?"*

Verbatim responses are recorded in `results/agentic/memory_test.md`.

---

## 8. Dispersion and Nonstandard Error Analysis Plan

Once all runs are completed and validated against the schema, the team will execute `scripts/p3_05_analysis.py` (to be created in P3-06):

1. **Directional Agreement:**
   $$\text{Agreement Rate} = \frac{1}{N} \sum_{i=1}^N \mathbf{1}(\text{direction}_i = \text{"up"} \land \text{estimate\_bps}_i > 0)$$
2. **Distributional Statistics:**
   - Sample mean, median, standard deviation, and interquartile range (IQR) of $\text{estimate\_bps}_i$ across all valid runs and by family.
   - Comparison with team estimate:
     $$\Delta = \text{median}(\text{estimate\_bps}) - 93.9\text{ bps}$$
   - Nonstandard error ratio:
     $$\text{NSE Ratio} = \frac{\text{SD}(\hat{\beta}_{\text{agents}})}{\text{SE}_{\text{team}} (16.2\text{ bps})}$$
3. **Metaregression Decomposition:**
   We estimate an OLS metaregression over completed runs:
   $$\text{estimate\_bps}_i = \alpha + \beta_1 \text{WindowPre}_i + \beta_2 \text{WindowPost}_i + \beta_3 \mathbf{1}(\text{AdjustedUSDT}_i) + \sum_k \gamma_k \text{TimeMatch}_{ik} + \sum_m \delta_m \text{Family}_{im} + \varepsilon_i$$
   An ANOVA / variance decomposition identifies which analysis choice explains the greatest share of variance in $\text{estimate\_bps}$.
4. **Handling Failures:**
   Runs that crash, exceed limits, produce unparseable JSON, or fail verification are retained in the master log as failures with explicit failure codes (e.g. `PARSE_ERROR`, `TIMEOUT`, `UNIT_SCALE_ERROR`), ensuring no survivorship bias.

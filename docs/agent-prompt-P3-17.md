# Prompt for the agent running P3-17 (restoration of the funds' channel)

Copy everything below the line into the agent.

---

You are a research engineer and critical reviewer on team "Out of Sample" (7th FGV EESP Datathon, Brazil). Work in
`/home/renzo/Documents/GitHub/7-datathon-fgv-eesp`. Read `prompt.md` (especially §5–§7) and `STATUS.md`, run
`git pull --rebase`, then read `tasks/P3-17-channel-restoration.md` starting with its Handoff, and claim S1
(`working`, `status: doing`, log line, commit `P3-17: <name> takes S1`). Use `.venv/bin/python`. Never force-push or rewrite
history; ask before pushing; start commit messages with `P3-17`. Do not download data without showing the plan and getting OK.

**Context.** A confidential BCB notice of 23 Jun 2026 stopped funds from importing cryptoassets through FX operations
(E-05). The USDT/BRL premium over PTAX rose about +94 bps for a month and fell back from about 22 Jul (F-011, F-016,
F-029); the cause of the fall is unexplained.

**Task.** Investigate exhaustively whether and when the BCB permitted funds to resume the **specific activity restricted
by the notice**: FX transactions to import cryptoassets where the fund effectively intermediates or supplies a particular
client. Permission to trade through an exchange's open order book (clarified 26 Jun, E-05.5) is a different activity and is
not restoration.

1. **Evidence trail first (S1).** From BCB communications and rules, bank or fund disclosures, and contemporaneous
   reporting (23 Jun–30 Oct 2026), build a dated source table. Classify each candidate as **full restoration, partial
   change, clarification, substitution through another channel, or no verified change**. Quote the operative language;
   separate publication date from effective date. Open every link yourself and copy the quote from the page; write
   `[link not opened]` otherwise. The BCB normativos API works:
   `https://www.bcb.gov.br/api/conteudo/app/normativos/exibenormativo?p1=Resolu%C3%A7%C3%A3o%20BCB&p2=NNN`; Planalto blocks
   automated requests.
2. **Spec before prices (S2).** Before looking at premiums around any candidate, commit the comparison: mean premium over
   the 20 PTAX days after minus the 20 before (t0 excluded), plus the first-day change; placebo against the clean dates of
   `scripts/p4_04_inference.py` (all clean dates and non-overlapping windows); list other events in each window.
   Freeze the candidate set and what counts as "credible". Disclose what you already know (task file section).
3. **Run (S3)** for **every** credible candidate, including those with no price response. Corroborate with exchange
   volume and order size (F-008, `results/tables/P3-10_order_flow.csv`) and the BCB monthly stablecoin-purchase series
   (SGS 29644, F-024).
4. **Competing explanations (S4)** for the fall around 22 Jul: (1) the restricted channel resumed; (2) it fell without
   that: adaptation, alternative supply, changing demand. State beforehand what each predicts in the volume, order-size
   and BCB data. A falling premium alone is not evidence of restoration; note that the premium already halved by 10 Jul.
5. **Deliver (S5):** dated source table, reproducible script, a finding (`findings/_TEMPLATE.md`, every number with its
   command) with a verdict **supported, contradicted, or unresolved**. If no restoration date can be verified, say so
   explicitly: that means the reopening test cannot be run, not that the June notice had no effect.

**Rules.** No causal language without a design. Make no claim about how the jury weighs things. Units explicit (bps, BRL,
Brasília time). Leave F-001..F-027 unchanged. Do not touch `deck/` (Felipe owns it). Write for economists and lawyers.
At the end: overwrite the Handoff, update STATUS (Recent activity, blockers), run `python scripts/board.py`, commit, and
report in five lines or fewer: what changed, what is next, what needs a decision.

The decisive question is whether the stopped activity actually resumed.

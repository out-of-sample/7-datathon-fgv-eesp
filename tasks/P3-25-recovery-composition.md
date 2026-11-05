---
id: P3-25
title: The premium recovered - did the market? Venue shares and exchange exits in 2026
phase: P3
status: review
owner: CS 1
working: -
due: 2026-11-06
depends: P1-03, P3-17
---

## Goal
After the spike the premium went back to an ordinary level (F-022). Answer the mentor's market-structure question
without overclaiming: **did the observed market go back to how it traded before, or did price recover while trading
moved to a different venue mix?** F-031 already reports Foxbit's share of the three exchanges' volume going from 7% to 33%
(wave) and 37% (after). This task checks that change on a consistent sample against ordinary periods, and puts next to it
the exchange exits of 2026 with their stated causes, so the deck does not blame the notice for exits it did not cause.
H1 (datathon subset) in `docs/competing-rails-datathon-ranking.md`, rank 2. **Cap: 4 hours.**

**Post hoc.** The periods were chosen with knowledge of the episode (F-031). The spec reuses them and adds no new date.

## Subtasks
- [x] S1 — done: Renzo (Codex), 5 Nov (`70c23e4`). Spec, committed before any new number: primary measure = Foxbit volume / (Binance + Foxbit + Mercado Bitcoin)
  volume, summed in USDT over hours all three cover (Mercado Bitcoin omits no-trade hours: missing = 0 volume, counted and
  reported); periods pre 1 May–22 Jun, wave 24 Jun–21 Jul, after 22 Jul–30 Oct 2026 (data end of the 30 Oct freeze);
  statistic = after-minus-pre share; reference = the same statistic for every pair of contiguous windows with the same
  lengths since Mercado Bitcoin's start (Mar 2023), excluding windows that touch 24 Jun 2026; secondary (Foxbit only, MB
  lacks the columns): median trade size, share of volume 09–18h Brasília
- [x] S2 — done: Renzo (Codex), 5 Nov. `scripts/p3_25_composition.py` (header) → `results/tables/P3-25_composition.csv`,
  `results/figures/P3-25_price_vs_share.png` (premium and Foxbit share on one time axis); finding F-036, exploratory,
  whatever it shows
- [x] S3 — done: Renzo (Codex), 5 Nov. Exits table: NovaDAX, Coinext, Bitnuvem, Digitra (leads in Felipe's `coinnext` report, P3-24 S1). For each, open the
  firm's own announcement, quote it, register it in `docs/sources.md` (§6), and record the announcement date relative to
  23 Jun 2026 and to the 30 Oct 2026 authorisation deadline (Res. BCB 520). Check the NovaDAX date: Felipe's dossier says
  8 Jun (before the notice), M-04 is the 7 Jul Foxbit partnership. A pre-notice exit is a competing reason for Foxbit's
  share gain
- [x] S4 — done: Renzo (Codex), 5 Nov. Competing-explanations table: new supply or rerouting through Foxbit, use of existing inventories, buyers
  retreating, clients migrating from exiting venues, licensing consolidation, and the perimeter we observe (three venues;
  no OTC, P2P or offshore). For each: which observed facts it explains and which data would separate it
- [ ] S5 — pt-BR slide sentence and annex paragraph drafted in F-036 by Renzo (Codex), 5 Nov; **independent Claude
  review and teammate re-run pending**. A teammate who did not write the script re-runs it (Nattan or Jonathan).

## Fixed specification (5 Nov, before P3-25 calculation)
- **Status:** retrospective. The phase dates and the first Foxbit-share figures were already seen in F-031. No causal
  inference follows from this comparison.
- **Clock and coverage:** index raw candles by their UTC open hour, then use the corresponding Brasília calendar date
  (UTC−3 in 2026) for all period boundaries. Use every complete hour from the first Mercado Bitcoin candle through
  30 Oct 2026 for which Binance and Foxbit have observations. Mercado Bitcoin's omitted no-trade hours are zero volume,
  but count and report them; report missing Binance/Foxbit hours separately. No forward fill of volume.
- **Volume and share:** use USDT base-asset volume. For each window, sum each venue's hourly USDT volume over the same
  retained hours, then Foxbit share = Foxbit sum / sum of the three venue sums. Do not average hourly or daily shares.
- **Episode windows (inclusive BRT dates):** pre 1 May–22 Jun 2026, wave 24 Jun–21 Jul, after 22 Jul–30 Oct. Primary
  statistic = after share minus pre share in percentage points. Show the three shares, venue volumes and retained-hour
  counts so coverage changes are visible.
- **Historical reference:** for each BRT start date after Mercado Bitcoin begins, form adjacent windows with the same
  calendar-day lengths as pre and after. Retain only pairs with the same common-hour rule and with neither window
  touching 24 Jun 2026. Report the full empirical distribution and the fraction of pairs whose absolute share change
  is at least the episode's. Adjacent windows are a descriptive benchmark, not independent policy events or a causal
  test. The reference uses no new choice of episode dates.
- **Secondary measures:** Foxbit median daily average trade size (USDT volume / trade count, on days with trades) and
  its 09:00–18:00 Brasília volume share, each for pre/wave/after. These describe Foxbit only. The chart overlays the
  frozen daily premium and daily three-venue Foxbit share, with the same BRT date axis and explicit units.
- **Exit evidence:** quote each firm's own dated statement where available. If one cannot be opened or does not state a
  cause, record that limitation; an exit timing comparison is descriptive and cannot attribute an exit to the notice.

## Success criteria
- [x] Spec committed before `p3_25_composition.py` produced any number (git order: `70c23e4`)
- [x] F-036 written with the exact command, reported whatever the share comparison shows
- [x] Every exit in the table has an opened, quoted source and its own stated cause
- [ ] A teammate re-runs the script and gets the same table

## Claim ceiling
- Allowed if it survives: "O prêmio voltou ao normal; a composição do mercado observado (três corretoras) não voltou."
- Not allowed: "o ofício concentrou o mercado" or "fechou corretoras" (exits have their own stated causes; S3); anything on
  who supplied the dollars or supplier concentration (venue share is not supplier share); "slow-moving capital provado".

## Outputs
- `scripts/p3_25_composition.py`
- `results/tables/P3-25_composition.csv`, `results/figures/P3-25_price_vs_share.png`
- Finding F-036; exits in `docs/sources.md`

## Handoff
- **State:** implementation and source audit complete; F-036 is exploratory and not in the deck. Four firm sources
  opened and registered as M-07 to M-10. The fixed spec preceded the script in git (`70c23e4`). The script output
  says Foxbit share 6.80% pre, 27.99% wave, 34.74% after on shared hours. Ready for another Claude agent to review.
- **Next step (independent Claude review):** pull the committed result, run
  `.venv/bin/python scripts/p3_25_composition.py`, compare the three output files with the committed copies, then
  audit F-036 against the CSV and the four firm pages M-07 to M-10. Check the UTC→Brasília conversion, Binance's
  millisecond/microsecond timestamps, the Mercado Bitcoin no-candle=zero rule, the 1,048 overlapping reference
  windows and their exclusion of 24 Jun, and the distinction between descriptive composition and cause. Inspect
  the chart at reading size. Record findings here, including any discrepancy; do not silently edit the fixed spec
  or F-001–F-033. If the review passes, ask Nattan or Jonathan to perform the teammate re-run required by S5.
  A ready review brief is in `docs/agent-prompt-P3-25-review.md`.
- **Open questions:** Coinext and Bitnuvem pages do not show an original publication date; F-036 uses the dated
  service changes they state. Felipe decides whether the reviewed line merits slide 8/10 or only the annex.
- **How to resume:** source data are the frozen files listed in the script header; the script writes only P3-25
  outputs. F-031 explains why its earlier 7/33/37% daily-share averages differ from this task's ratio of summed
  USDT volumes.

## Log
- 2026-11-05, Codex for Renzo: S2–S4 completed; outputs and F-036 written, four company statements opened and
  quoted. Presented the result as a three-venue descriptive comparison. Set to review for Renzo's other Claude agent;
  teammate re-run remains a separate criterion before `done`.
- 2026-11-05, Codex for Renzo: claimed P3-25 and fixed the retrospective comparison rule before calculating new numbers.
  A parallel P3-20 session has uncommitted files; `git pull --rebase` cannot run while those edits are present, so no
  other worker's files were stashed or changed.
- 2026-11-04, agent for Renzo: task created from the competing-rails follow-up (decision log, 4 Nov). Renzo owns it.

## Result
Foxbit's share of summed USDT volume on the three observed venues increased by 27.94 percentage points from the
fixed pre to after windows. Historical adjacent pairs do not show a change that large, but the reference windows
overlap and the episode was selected after seeing it. F-036 gives the numbers, figure, exits table and alternative
explanations. Independent review and deck inclusion are pending.

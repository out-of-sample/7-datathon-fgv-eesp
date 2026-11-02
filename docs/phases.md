# Phases, success criteria and gates

The work is split into phases. Each phase has a **goal in plain words**, a list of tasks (one file each in
`tasks/`), **success criteria** that anyone can check, and a **gate**: a short team check at the end where
the criteria are ticked and the outcome goes to the decision log (`docs/README.md`).

A phase is done when every criterion is ticked or explicitly waived in the decision log.
The live progress board is in [`../STATUS.md`](../STATUS.md) (generated from the task files).

Rolling detail: tasks of the current and next phase are written in full; later tasks are short and get
detailed when their phase starts.

Owner roles (CS 1 data, CS 2 modelling, CS 3 validation, Economist) map to people in `STATUS.md` → Team.
"Owner" means the person accountable; agents work on that person's behalf.

---

## P0 — Scoping and probe

**Dates:** Fri 30 Oct (done). **Goal:** choose the project with evidence, not opinion.

Success criteria:
- [x] Past winners and jury reviewed (`docs/README.md`)
- [x] Primary project chosen with a reproducible probe (`scripts/00_probe_premium.py`, findings F-001 to F-004)
- [x] Plans written for the primary, the chapter and the extensions

## P1 — Data foundation

**Dates:** Sat 31 Oct. **Goal:** every dataset the analysis needs is downloaded, frozen, documented and
understood, and every event date has a primary source.

Tasks: P1-01 to P1-08.

Success criteria:
- [x] Every raw file listed in `data/README.md` with source URL, retrieval date and SHA-256 checksum
- [x] Premium v2 (time-matched, USDT/USD-adjusted) reproduces the probe's yearly means within ±5 bps, or the
      differences are explained in the task file
- [x] Every event in `data/processed/P1-04_events_brazil.csv` has a primary-source link in `docs/sources.md`
- [x] The 23 Jun 2026 notice is confirmed by a primary or second independent source, or flagged "unconfirmed"
- [x] At least 4 comparison currencies have USDT prices and an official FX rate for 1 Nov 2025 – 30 Sep 2026
- [x] Team decision on the API budget for agentic A (P1-08): existing Claude, ChatGPT and Gemini plans, no API spend

## P2 — Core evidence

**Dates:** Sun 1 – Mon 2 Nov. **Goal:** answer the main question with the tests written down in
`02-dolar-cripto.md` §7, including the ones that might fail.

**Gate on Sun 1 Nov (evening)**, before the synthetic control and the agent runs:
- 23 Jun notice confirmed? If not: present the jump as an unexplained break.
- At least 4 usable comparison currencies? If not: difference-in-differences against their average only.
- Second BRL venue shows the jump? If not: the result is venue-specific; reconsider the headline.
- Agentic A: owner available and the three CLIs usable on Renzo's plans? Agentic B: done, or manual screening?

Tasks: P2-01 to P2-06.

Success criteria:
- [ ] Noise floor estimated and drawn on the premium chart
- [ ] Break test run blind (dates found by the algorithm), then matched to events; unmatched breaks reported
- [ ] Before/after table for **every** dated rule, with placebo dates, including null results
- [ ] Synthetic control (or the fallback) with placebo countries and a permutation p-value
- [ ] Every estimate shown next to its naive baseline
- [ ] Our before/after estimate for 23 Jun written in the agents' answer schema and committed (P2-06)
- [ ] Each result recorded as a finding file with the script and command that produce it

## P3 — Extensions

**Dates:** Mon 2 – Tue 3 Nov. **Goal:** turn the evidence into what the jury uses: a money number, a
solution, the dollar-side chapter, and (if go) the agentic robustness.

Tasks: P3-01 to P3-08.

Success criteria:
- [ ] Cost of buying US$ 100k via bank vs USDT, per regime, with sources for every cost component
- [ ] Scenarios for the 24h hold and the 3.5% IOF, clearly labelled as scenarios
- [ ] Monitor do Dólar Digital produces a daily index and a regime flag from one script
- [ ] Depeg chapter: SVB-weekend figure; Kaplan–Meier only if ≥ 12 independent events
- [ ] If A is go: protocol committed before runs; all runs reported (including failures); dispersion analysis done
- [ ] 2025 subsidy-share check done for the "Lições de 2025" slide

## P4 — Robustness and freeze

**Dates:** Wed 4 Nov. **Goal:** make sure the headline survives reasonable changes, then stop changing it.

Tasks: P4-01 to P4-03.

Success criteria:
- [ ] At least two alternative windows, two premium definitions and the second venue for every headline number
- [ ] Every headline number re-run by a teammate who did not produce it, with matching output
- [ ] All findings used in the deck marked `frozen`; a git tag `results-frozen` on the commit
- [ ] After the freeze, only bug fixes, each disclosed in the finding file

## P5 — Deck and submission

**Dates:** Thu 5 – Sun 8 Nov. **Goal:** a PDF that a juror understands without us in the room.

Tasks: P5-01 to P5-06.

Success criteria:
- [ ] Every item of the definition of done in `prompt.md` §8 ticked
- [ ] Red-team review done (Fri 6 Nov), and every point answered or consciously declined
- [ ] Scripts exported as `.txt` with headers; they re-run from raw data to the deck figures
- [ ] PDF and scripts uploaded by **20:00 Sun 8 Nov** (hard deadline 23:59)

## P6 — Final (only if selected)

**Dates:** Thu 12 – Mon 16 Nov. **Goal:** a rehearsed oral presentation within the time limit.
Tasks are created if the team is a finalist: timing, Q&A drill (rigor questions, the 23 Jun event, the AI
agents), backup slides.

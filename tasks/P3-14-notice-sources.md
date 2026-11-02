---
id: P3-14
title: Every source on the 23 Jun 2026 BCB notice, opened and registered
phase: P3
status: review
owner: CS 1
working: Felipe (review)
due: 2026-11-03
depends: P1-04
---

## Goal
Our account of the 23 Jun notice (E-05) rests on two opinion pieces (1 and 6 Jul) and a LAI answer. Find every
report and official text about the notice, open each one, and add it to `docs/sources.md` with a quote, so the
deck can say exactly what is known about the notice and from whom. Plan: `docs/06-so-what.md`, step 0.

## Subtasks
- [x] S1 — Sweep: news (Cointelegraph Brasil, Exame, Valor, InfoMoney, Folha, Estadão, Blocknews, Portal do
  Bitcoin, Livecoins, Money Times, Reuters, Bloomberg Línea), BCB pages (press releases, external-sector press
  release of 27 Aug, public consultation on the 24-hour hold, Res. 584 explanatory text), the LAI answer, and
  industry associations (ABCripto, ABToken, ABFintechs). Open every hit. — done: Renzo, 2 Nov
- [x] S2 — Add each opened source to `docs/sources.md` (E-05 row or new rows) with one quote, who opened it and
  when; list hits that could not be opened as `[link not opened]`. — done: Renzo, 2 Nov
- [x] S3 — Compare what the reports say about prices (spread 0.1% → 0.7%, "chegou a 2%", "caiu para 0,5%" on
  26 Jun) with our premium series, and record the comparison in a finding. — done: Renzo, 2 Nov (F-023)

## Success criteria
- [x] Every source added to `sources.md` in this task has a quote and "opened <date> (<who>)"
- [x] The E-05 row says which sources saw the notice itself and which only describe it
- [x] Reported price moves compared with our series, in a finding with the command

## Outputs
- `docs/sources.md` (E-05 row, table "E-05: every source found", E-10 Res. 580, D-16), `data/processed/P1-04_events_brazil.csv`
  (E-05 description and source), `scripts/p3_14_press_check.py`, `results/tables/P3-14_press_vs_series.csv`, F-023

## Handoff
<!-- Overwrite at the end of every session, finished or not, so anyone can continue from here. -->
- **State:** done, in review. Ten sources for E-05 in `docs/sources.md`, each opened on 2 Nov with a quote checked against
  the page text: two outlets had the document or an excerpt (Cointelegraph Brasil 24 Jun, Exame 25 Jun), the BCB's LAI
  answer gives its own words (29–30 Jul), plus follow-ups, market reports and opinion. Found along the way: Res. BCB 580
  (1 Jul 2026, E-10), not in the P1-04 event list. Reported price moves match our series (F-023).
- **Next step:** a teammate (Felipe, P1-04 owner) checks the E-05 rows. Whether E-10 joins the event list is deferred to
  slide building (decision log, 2 Nov); until then it is a caveat in F-024.
- **Open questions:** the decree behind the zero IOF for funds (Decreto 6.306/2007, art. 15-B, III) is cited by E-05.10
  but not opened.
- **How to resume:** `python scripts/p3_14_press_check.py`; sources in `docs/sources.md` → "E-05: every source found".

## Log
- 2026-11-02, agent for Renzo: renumbered from P3-09 (Felipe's depeg-sources task took P3-09 first on main); files and references renamed. Commits before this one say P3-09.
- 2026-11-02, agent for Renzo: S1–S3 done: 10 sources registered with verified quotes, E-10 and D-16 added, F-023 written; status review.
- 2026-11-02, agent for Renzo: created (plan `docs/06-so-what.md`); Renzo takes S1.

## Result

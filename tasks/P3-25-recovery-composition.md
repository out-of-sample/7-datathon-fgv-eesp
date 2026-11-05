---
id: P3-25
title: The premium recovered - did the market? Venue shares and exchange exits in 2026
phase: P3
status: todo
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
- [ ] S1 — Spec, committed before any new number: primary measure = Foxbit volume / (Binance + Foxbit + Mercado Bitcoin)
  volume, summed in USDT over hours all three cover (Mercado Bitcoin omits no-trade hours: missing = 0 volume, counted and
  reported); periods pre 1 May–22 Jun, wave 24 Jun–21 Jul, after 22 Jul–30 Oct 2026 (data end of the 30 Oct freeze);
  statistic = after-minus-pre share; reference = the same statistic for every pair of contiguous windows with the same
  lengths since Mercado Bitcoin's start (Mar 2023), excluding windows that touch 24 Jun 2026; secondary (Foxbit only, MB
  lacks the columns): median trade size, share of volume 09–18h Brasília
- [ ] S2 — `scripts/p3_25_composition.py` (header) → `results/tables/P3-25_composition.csv`,
  `results/figures/P3-25_price_vs_share.png` (premium and Foxbit share on one time axis); finding F-036, exploratory,
  whatever it shows
- [ ] S3 — Exits table: NovaDAX, Coinext, Bitnuvem, Digitra (leads in Felipe's `coinnext` report, P3-24 S1). For each, open the
  firm's own announcement, quote it, register it in `docs/sources.md` (§6), and record the announcement date relative to
  23 Jun 2026 and to the 30 Oct 2026 authorisation deadline (Res. BCB 520). Check the NovaDAX date: Felipe's dossier says
  8 Jun (before the notice), M-04 is the 7 Jul Foxbit partnership. A pre-notice exit is a competing reason for Foxbit's
  share gain
- [ ] S4 — Competing-explanations table: new supply or rerouting through Foxbit, use of existing inventories, buyers
  retreating, clients migrating from exiting venues, licensing consolidation, and the perimeter we observe (three venues;
  no OTC, P2P or offshore). For each: which observed facts it explains and which data would separate it
- [ ] S5 — One pt-BR sentence for Felipe (slide 8 or 10) and an annex paragraph; a teammate who did not write the script
  re-runs it (Nattan or Jonathan)

## Success criteria
- [ ] Spec committed before `p3_25_composition.py` produced any number (git order)
- [ ] F-036 written with the exact command, reported whatever the share comparison shows
- [ ] Every exit in the table has an opened, quoted source and its own stated cause
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
- **State:** task created 4 Nov; owner Renzo (CS 1), starts 5 Nov. Nothing computed.
- **Next step:** S1. Read F-031 (table C2) and `scripts/p3_17_restoration.py` part C, which already sums the three venues'
  volume; reuse its loading code, write the spec here, commit, then S2.
- **Open questions:** S3 needs Felipe's `coinnext` report (P3-24 S1); if it is not pushed by the time S3 starts, search the
  four firms' announcements directly.
- **How to resume:** `.venv/bin/python scripts/p3_17_restoration.py` reproduces F-031 first (sanity check).

## Log
- 2026-11-04, agent for Renzo: task created from the competing-rails follow-up (decision log, 4 Nov). Renzo owns it.

## Result
<!-- fill when done -->

---
id: P1-04
title: Verified list of Brazilian rule changes and events
phase: P1
status: review
owner: Economist
working: -
due: 2026-10-31
depends: -
---

## Goal
A table of every dated rule or event that could change the cost of getting dollars via USDT, each with a
primary source. It feeds the event studies, the break matching, and is the human benchmark for extension B.

## Subtasks
- [x] S1 — Start from `docs/02-dolar-cripto.md` §6 (event list) and `docs/sources.md` (E-01 to E-06). — done: Felipe, 1 Nov
- [x] S2 — For each event, find the primary source (Diário Oficial, BCB normative search, BCB/Fazenda press release).
   Record **announcement date** and **effective date** separately. — done: Felipe, 1 Nov
- [x] S3 — Confirm the 23 Jun 2026 notice in a primary or second independent source; otherwise mark it unconfirmed. — done: Felipe, 1 Nov
- [x] S4 — Add events you find that are missing (e.g., exchange BRL deposit/withdrawal outages, the 24h-hold rule). — done: Felipe, 1 Nov
- [x] S5 — Columns: `event_id, date_announced, date_effective, description, type (tax/restriction/reporting/outage/other),
   channel_affected, source_url, source_type (primary/secondary), verified_by, verified_on`. — done: Felipe, 1 Nov

## Success criteria
- [x] `data/processed/P1-04_events_brazil.csv` exists; every row has a source URL
- [x] 23 Jun 2026 status: confirmed or unconfirmed, with the evidence
- [x] `docs/sources.md` statuses updated

## Outputs
- `data/processed/P1-04_events_brazil.csv`, updated `docs/sources.md`

## Handoff
<!-- Overwrite at the end of every session, finished or not, so anyone can continue from here. -->
- **State:** done → review (all 5 subtasks and 3 criteria completed by Felipe)
- **Next step:** CS 2 (Nattan/Renzo) can now run `P2-02` S3 (matching blind breaks to `data/processed/P1-04_events_brazil.csv`) and `P2-03` (event studies for all dated rules + placebo dates)
- **Open questions:** Gate call on framing E-05 (confidential BCB supervisory *ofício* reported by Isac Costa in ConJur on 1 Jul 2026; unconfirmed as a public DOU resolution, corroborated empirically by the 24 Jun 2026 break across 3 venues)
- **How to resume:** inspect `data/processed/P1-04_events_brazil.csv` and `docs/sources.md`

## Log
- 2026-11-01, Felipe: S1–S5 completed (`status: review`). Wrote `data/processed/P1-04_events_brazil.csv` (13 rows: `E-01`, `E-01b`, `E-02`, `E-03`, `E-04`, `E-05`, `E-06a`, `E-06b`, `E-07`, `M-01`..`M-04`) and updated `docs/sources.md`. Unblocks `P2-02` S3 and `P2-03`.
- 2026-11-01, Felipe: claimed P1-04 (S1–S4); launched regulatory-verifier subagents on E-01..E-07, the 23 Jun 2026 notice, and the July 2026 fade / blind break dates.
- 2026-10-31, agent for Renzo (note from P3-03): the premium rises modestly from late May 2026 (weekly 10–22 bps vs 5.8 in Jan–Apr) before the 24 Jun jump. Anything in May–Jun 2026? (F-014)
- 2026-10-31, agent for Renzo (note from P2-02): the blind break test (F-011) finds breaks on 26 Jul 2021, 20 Aug 2024, 8 Jul 2025, 24 Jun 2026 and 22 Jul 2026 (95% CIs in P2-02 Result). Please look especially for anything around **15–29 Jul 2026**, when the June spike faded (BCB clarification, bank or fund response, market adaptation?), and around Jul–Aug 2021 and Apr–Dec 2024. P2-02 S3 waits for `data/processed/P1-04_events_brazil.csv`.
- 2026-10-31, agent for Renzo (note from P2-05, not working here): candidate non-regulatory events found while
  ruling out causes: Binance BRL Pix suspension 17 Jun – Jul 2022 (E-07, `[verify]` dates) and Binance's USDT/BRL tick
  cut on ~27 Jun 2025 (F-007). Your call whether they go in the event list.

## Result
13 verified regulatory and market-structure events recorded in `data/processed/P1-04_events_brazil.csv` with separate announcement and effective dates and primary/secondary URLs in `docs/sources.md`:
1. **E-05 (23 Jun 2026 BCB notice):** Identified as a confidential BCB supervisory notification (*ofício*) to banks, FX brokers and investment fund administrators declaring virtual-asset FX import structures via funds irregular. Reported by Isac Costa (former CVM analyst/board advisor, partner at Warde Advogados, prof. Ibmec/Insper) in *ConJur* on 1 Jul 2026 (`source_type = secondary`; unconfirmed in public DOU/BCB database because supervisory *ofícios* are not published in DOU).
2. **May 2026 buildup (F-014) & E-04 / E-06a:** `Resolução BCB nº 561/2026` was published on **30 Apr 2026** (effective 1 Oct 2026), amending Art. 50 of Res. BCB 277/2022 to ban virtual assets in cross-border eFX settlement, followed four days later (**4 May 2026**) by the entry into force of mandatory BCB reporting under Art. 4º of `Resolução BCB nº 521/2025` (`E-04`).
3. **15–29 Jul 2026 fade (F-011 Break 5) & Foxbit 6× volume surge (F-008):** On **7 Jul 2026**, NovaDAX (exiting Brazil) announced a strategic user-migration partnership with Foxbit (`M-04`), coinciding with the **1 Jul 2026** entry into force of `Res. BCB 580` and Receita's `DeCripto` (`IN RFB 2.291/2025`). Because the 23 Jun supervisory action restricted fund-mediated OTC imports while leaving compliant domestic exchange order-book trading lawful, liquidity consolidated onto domestic order books (surging Foxbit's volume 6× via 5× larger ticket sizes and compressing the ~100 bps scarcity spike back down to ~27 bps by 22 Jul 2026).
4. **Other blind breaks (F-011):** `2021-07-26` matches `M-01` (Binance global leverage cap and withdrawal limit cut amid CVM derivatives enforcement); `2024-08-20` matches `M-02` (CVM approval on 13 Aug 2024 and DOU publication on 20 Aug 2024 of Binance's R$ 9.6M *Termo de Compromisso*); `2025-07-08` matches `M-03` (Binance tenfold `USDT/BRL` tick size cut on 27 Jun 2025) and `E-01b` (STF Min. Alexandre de Moraes's 4 Jul 2025 injunction in ADC 96 freezing the May 2025 IOF hike dispute).
5. **E-06b (24-hour precautionary hold):** `Resolução BCB nº 584, de 7 de agosto de 2026` (amending Res. BCB 142/2021) mandates an up to 24-hour hold and COAF report on transfers ≥ US$ 10,000 to foreign entities or self-hosted wallets; while the late-June draft targeted Oct 2026, the enacted norm set the effective date to **1 Jan 2027**.

# P3-28 — Coding rubric for the reference answers (Felipe and Jonathan)

Version 1, 7 Nov 2026. Task: `tasks/P3-28-agentic-access-map.md` (S2).

## What you are doing and why

We are testing whether an AI agent reads provider documents more accurately than simpler methods. To score them, we
need **reference answers written by people**, from the same frozen documents the methods will see. You and the other
coder answer the same questions **independently**. Then you compare, and settle each disagreement together, with
Felipe ruling on scope. The settled answers become the reference.

The reference says **what the documents support**. It does not say what really works in practice, and it is not a
legal opinion.

## Rules of independence (important)

1. Do **not** discuss answers with the other coder before you have both returned your sheets.
2. Do **not** show your sheet to Renzo's agent or any AI, and do not use an AI to fill it. Send it to Renzo privately.
   Do not commit it to git.
3. Use **only** the documents in the corpus zip (`text/<source_id>.txt`, list in `P3-28_corpus.csv`). No web search,
   no memory of how the platform works, no knowledge of our earlier findings. If the documents don't answer, the answer
   is `unknown`.
4. Write down how long the sheet took you, in the `notes` column of the first row.

## The sheet

`form_<your name>.csv`: one row per case × question. Cases are in `P3-28_cases.csv`: provider, profile (`PJ-BR` = a
Brazilian non-financial company; `PF-BR` = a resident individual; `FUND-BR` = an investment fund), asset, network,
as-of date. Questions are in `P3-28_fields.csv`. Fill in five columns:

| Column | What to write |
|---|---|
| `state` | For questions of type `state` or `state+value`, one of the states below. For `value` questions, leave it empty, or write `unknown` if no document gives the value |
| `value` | For `value` and `state+value` questions: the value as the document gives it, converted to the unit in `unit_hint` (0.50% → `50`, unit `bps`). Short text is fine ("case by case") |
| `unit` | Unit of the value (`bps`, `USDT`, `hours`, `BRL`, …) |
| `source_ids` | The document(s) you used, e.g. `A-03` or `A-09;A-10` |
| `passages` | For each source, a **short verbatim quote** (copy and paste, 5–40 words) supporting the answer, separated by `||` in the same order as `source_ids`. A script checks every quote word for word against the text files; a quote that is not found does not count |

## States

| State | Use when |
|---|---|
| `supported` | A document states that this profile can do this (or that the condition holds) on the as-of date |
| `restricted` | A document states that this profile **cannot** do this, or a rule prohibits it, on the as-of date |
| `conditional` | A document says it is possible only if something else holds (an approval, a review, a limit, a declaration) that the documents do not establish for this case |
| `conflicting` | Two documents (or two passages) say incompatible things, and neither a later date nor a stated difference in scope settles it. Quote both |
| `unknown` | No document in the corpus answers the question. **Missing is not "no".** A page that doesn't mention a network does not mean the network is unsupported |
| `not_applicable` | The question does not fit the case (rare; explain in `notes`) |

## Coding rules

- **"Can it?" versus "what is required?"** Questions asking whether the profile *can* do something (F01, F07, F10,
  F11, F15, G01) use the full set of states. Questions asking *what is required* (F02, F03, F09, F13) use `supported`
  when a document states the requirement, with the requirement in `value`, and `unknown` when no document says.
  Example: "company verification by compliance" is F03 = `supported`, value "company verification by compliance";
  it is not `conditional`.
- **When is a "can" question conditional?** When a document makes the operation depend on an approval or review
  specific to it, for example a separate commercial analysis of stablecoin purchases. Ordinary account verification
  (F03) and the destination declaration (F13) do not by themselves make F01, F07 or F10 conditional.
- **Profile matters.** A personal-account page does not answer a company question unless it says it applies to
  companies (or to all clients). If unsure, `unknown` and a note.
- **Network matters.** A fee or status without a named network does not answer a question about a specific network:
  `unknown`, with a note on what the document does say.
- **Dates matter.** A rule with a later start date is not in force on the as-of date. A press article published after
  the as-of date may describe the situation on that date, but only if it says so.
- **Advertising is a provider statement**, not proof something works. Code what it states.
- **Fees and limits:** never write `0` for a missing fee. Missing is empty plus `unknown`.
- **F06** (Res. BCB 589): answer only from documents in the corpus about this provider's authorisation status or about
  banks serving it. The rule's text alone, without the provider's status, is not enough for `restricted`. If the
  provider is only an applicant and no document says whether banks may keep serving applicants, code `unknown`
  (Felipe's ruling on the D-01 card, 7 Nov).
- **Funds' cases (D-04, D-05):** G01 asks whether the fund may carry out the FX import **in the role the case
  describes** (intermediation in D-04, own account or in-book arbitrage in D-05) as of 26 Jun 2026.

## After both sheets are in

Renzo runs `.venv/bin/python scripts/p3_28_access_map.py adjudicate`. It prints only counts and writes
`disagreements.csv` for you two. Meet, fill `adjudicated_state` / `adjudicated_value` / `adjudication_note` for every
row, and keep the original answers: initial disagreement rates are reported. Felipe rules on scope (profile, legal
reading); a quote check failure is fixed by finding the right quote, not by changing the answer to fit. The reference
then gets a SHA-256 hash, committed before any method's held-out output is scored.

Checkpoint **G1** passes if both of you could apply this rubric (few `not_applicable`, notes explain the hard cases)
and the critical unknowns stay explicit.

# Review request for Renzo's other Claude agent — P3-25

Please independently review the completed P3-25 work. Start with `prompt.md`, `STATUS.md`, then the **Handoff** in
`tasks/P3-25-recovery-composition.md`. The author is Codex for Renzo; do not treat the finding as confirmed yet.

1. Verify in git that the fixed retrospective spec (`70c23e4`) precedes `scripts/p3_25_composition.py` and the output
   commit. The episode dates were already known from F-031; check that the finding discloses this.
2. Run `.venv/bin/python scripts/p3_25_composition.py` from the repository root. Compare the regenerated
   `P3-25_composition.csv`, `P3-25_reference.csv` and figure with the committed copies. Independently check at least
   the pre and after period sums and Foxbit shares from the frozen raw files; a successful run of the same code alone
   is not an independent arithmetic check.
3. Check UTC candle timestamps, Brasília date boundaries, Binance milliseconds versus microseconds, common-hour
   inclusion, Mercado Bitcoin's omitted no-trade hours as zero, and the historical reference's adjacent window
   lengths and exclusion of 24 Jun 2026. Flag the fact that the reference windows overlap and do not match the
   episode's gap; the finding must not call its 0/1,048 comparison a causal p-value.
4. Open M-07 to M-10 in `docs/sources.md` and verify each quoted line and date. NovaDAX's own page is dated 9 Jun;
   Exame reported its statement on 8 Jun. Bitnuvem and Coinext pages do not display their original publication
   dates. Confirm that no exit is attributed to the 23 Jun notice without evidence.
5. Read F-036 and inspect the PNG at presentation size. Check every quantity, the distinction between three-venue
   share and national market share, and the pt-BR slide sentence and annex paragraph. Report any corrections in the
   P3-25 task log or handoff. If it passes, record your review there and tell Renzo; Nattan or Jonathan still needs to
   perform the teammate re-run before the task is marked `done` or F-036 becomes confirmed.

Keep core frozen findings F-001–F-033 unchanged. Do not place F-036 in the deck until review and Felipe's decision.

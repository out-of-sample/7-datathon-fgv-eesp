"""Synthetic P3-43 regression checks; no real documents, labels, model calls or tracked outputs.

Run from repository root: python scripts/test_p3_43_audit.py
Temporary fixtures are created and removed under scratch/.
"""
import contextlib
import csv
import io
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

import p3_28_methods as m


class AuditTests(unittest.TestCase):
    def setUp(self):
        scratch = Path(__file__).resolve().parents[1] / 'scratch'
        scratch.mkdir(exist_ok=True)
        self.tmp = tempfile.TemporaryDirectory(prefix='p343_', dir=scratch)
        self.root = Path(self.tmp.name)
        (self.root / 'results/tables').mkdir(parents=True)
        (self.root / 'runs/A').mkdir(parents=True)
        self.cs = {'C': dict(split='dev', group_id='fixture', profile_id='company', destination_asset='USDT',
                             chain='TRON', as_of_utc='2026-11-07')}
        self.fields = [dict(field_id='F01', question='Is the route available?', kind='availability', answer='state')]
        self.answer = dict(field_id='F01', state='supported', value='', unit='', source_ids=['S'],
                           passages=['Pix deposits accepted.'], note='')
        self.run = dict(answers=[self.answer], permitted=['S'], corpus_hash='fixture', errors=[], usage={},
                        model='synthetic', n_calls=1, turns=1, wall_s=1, notional_usd=0)
        self.write_run()
        self.ref = self.root / 'ref.csv'
        self.write_csv(self.ref, [dict(case_id='C', field_id='F01', state='supported', value='', unit='')])
        self.patches = [patch.object(m, 'ROOT', self.root), patch.object(m, 'RAW', self.root),
                        patch.object(m, 'RUNS', self.root / 'runs'), patch.object(m, 'SCHEDULE', {'A': 1}),
                        patch.object(m, 'cases', lambda: self.cs), patch.object(m, 'fields_for', lambda c: self.fields),
                        patch.object(m, 'doc_text', lambda i: 'Pix deposits accepted.'),
                        patch.object(m, 'corpus_hash', lambda ids: 'fixture'),
                        patch.object(m.M, 'latest', lambda: ({}, {'S': {}}))]
        for p in self.patches:
            p.start()

    def tearDown(self):
        for p in reversed(self.patches):
            p.stop()
        self.tmp.cleanup()

    @staticmethod
    def write_csv(path, rows, columns=None):
        with path.open('w', newline='', encoding='utf-8') as fh:
            w = csv.DictWriter(fh, columns or list(rows[0]))
            w.writeheader()
            w.writerows(rows)

    def write_run(self):
        (self.root / 'runs/A/C_r1.json').write_text(json.dumps(self.run), encoding='utf-8')

    def score(self, audit=None):
        out = io.StringIO()
        with contextlib.redirect_stdout(out):
            m.score(self.ref, 'dev', audit_path=audit)
        return out.getvalue()

    def decisions(self):
        self.score()
        rows = m.M.rows(self.root / 'reference/audit_sheet.csv')
        for row in rows:
            row.update(supports='yes', value_ok='yes', note_claim='no', auditor_type='ai', auditor_id='fixture-agent')
        return rows

    def audit_file(self, rows):
        p = self.root / 'audit.csv'
        self.write_csv(p, rows)
        return p

    def test_without_audit_is_provisional(self):
        self.assertIn('PROVISIONAL', self.score())

    def test_empty_supplied_audit_rejected(self):
        p = self.root / 'empty.csv'
        self.write_csv(p, [], ['key', 'supports', 'value_ok', 'note_claim'])
        with self.assertRaisesRegex(SystemExit, 'empty audit'):
            self.score(p)

    def test_unrelated_key_rejected(self):
        rows = self.decisions()
        rows[0]['key'] = 'unrelated'
        with self.assertRaisesRegex(SystemExit, 'missing.*unexpected'):
            self.score(self.audit_file(rows))

    def test_blank_or_invalid_decision_rejected(self):
        for value in ('', 'maybe'):
            rows = self.decisions()
            rows[0]['supports'] = value
            with self.assertRaisesRegex(SystemExit, 'yes/no'):
                self.score(self.audit_file(rows))

    def test_auditor_provenance_required(self):
        rows = self.decisions()
        rows[0]['auditor_id'] = ''
        with self.assertRaisesRegex(SystemExit, 'auditor_type'):
            self.score(self.audit_file(rows))

    def test_complete_ai_audit_has_explicit_label(self):
        text = self.score(self.audit_file(self.decisions()))
        self.assertIn('FINAL (AI-reviewed exploratory pilot; not human validated)', text)
        self.assertIn('A | 1 (0) | 1.000 | 0', text)

    def test_opposite_notes_and_units_have_distinct_keys(self):
        a = self.answer
        self.assertNotEqual(m.audit_key('C', 'F01', dict(a, note='available')),
                            m.audit_key('C', 'F01', dict(a, note='not available')))
        self.assertNotEqual(m.audit_key('C', 'F01', dict(a, unit='hours')),
                            m.audit_key('C', 'F01', dict(a, unit='days')))

    def test_duplicates_preserved_and_note_guarded(self):
        self.run['answers'] = [dict(self.answer, note='Route available'), dict(self.answer, note='Route unavailable')]
        self.write_run()
        rows = self.decisions()
        self.assertEqual(len(rows), 2)
        rows[0]['note_claim'] = 'yes'
        text = self.score(self.audit_file(rows))
        self.assertIn('A | 1 (0) | 0.000 | 1', text)

    def test_missing_one_duplicate_audit_rejected(self):
        self.run['answers'] = [dict(self.answer, note='one'), dict(self.answer, note='two')]
        self.write_run()
        rows = self.decisions()
        with self.assertRaisesRegex(SystemExit, '1 missing'):
            self.score(self.audit_file(rows[:1]))

    def test_raw_output_and_extra_fields_audited(self):
        self.run['raw_results'] = ['The entire route is available.']
        self.run['answers'].append(dict(field_id='unexpected', state='unknown', note='Available anywhere'))
        self.write_run()
        rows = self.decisions()
        self.assertEqual(len(rows), 3)
        for row in rows:
            if row['field_id'] != 'F01':
                row['note_claim'] = 'yes'
        text = self.score(self.audit_file(rows))
        self.assertIn('A | 1 (0) | 1.000 | 2', text)

    def test_missing_run_scores_zero(self):
        (self.root / 'runs/A/C_r1.json').unlink()
        text = self.score()
        self.assertIn('missing runs 1', text)
        self.assertIn('A | 1 (0) | 0.000 | 0', text)

    def test_changed_corpus_stops_before_scoring(self):
        self.run['corpus_hash'] = 'stale'
        self.write_run()
        with self.assertRaisesRegex(SystemExit, 'corpus mismatch'):
            self.score()

    def test_wrong_units_and_existing_checks(self):
        with contextlib.redirect_stdout(io.StringIO()):
            m.selftest()

    def test_failed_run_zero_but_claims_still_audited(self):
        self.run['errors'] = ['timeout']
        self.write_run()
        rows = self.decisions()
        rows[0]['supports'] = 'no'
        text = self.score(self.audit_file(rows))
        self.assertIn('A | 1 (0) | 0.000 | 1', text)

    def test_draft_and_all_raw_calls_preserved(self):
        self.run['draft'] = [dict(self.answer, note='Draft route assertion'), dict(self.answer, note='Draft route assertion')]
        self.run['raw_results'] = ['Earlier unsupported route prose', 'Final prose', 'Final prose']
        self.write_run()
        rows = self.decisions()
        self.assertEqual(len(rows), 4)  # final answer, one exact draft, two distinct raw calls
        for row in rows:
            if row['note'] in ('Draft route assertion', 'Earlier unsupported route prose'):
                row['supports'] = 'no'
                row['note_claim'] = 'yes'
        text = self.score(self.audit_file(rows))
        self.assertIn('A | 1 (0) | 1.000 | 3', text)  # draft bad positive + note; earlier raw note


if __name__ == '__main__':
    unittest.main(verbosity=2)

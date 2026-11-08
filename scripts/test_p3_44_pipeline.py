"""Independent P3-44 pipeline regression checks, synthetic inputs only.

Run: python scripts/test_p3_44_pipeline.py
No model calls, real labels, network access or tracked output rewrites.
"""
import csv
import hashlib
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

import p3_44_collect as collector
import p3_44_access_pilot as pilot


class PipelineTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory(prefix='p344_independent_', dir=Path(__file__).resolve().parents[1] / 'scratch')
        self.root = Path(self.tmp.name)
        self.raw = self.root / 'data/raw/p3_28_v2'
        (self.raw / 'source').mkdir(parents=True)
        (self.raw / 'text').mkdir()
        (self.root / 'results/tables').mkdir(parents=True)
        self.body = b'<html><title>Terms</title><body>Pix deposits are accepted for verified corporate accounts.</body></html>'
        self.text = 'Terms Pix deposits are accepted for verified corporate accounts.'
        self.bp = self.raw / 'source/X_20261107.html'
        self.tp = self.raw / 'text/X_20261107.txt'
        self.bp.write_bytes(self.body)
        self.tp.write_text(self.text, encoding='utf-8')
        self.source = dict(source_id='X', family='foxbit', split='dev', publisher='Fixture', title='Fixture terms',
                           fetch_url='https://example.invalid/terms', snapshot='yes', fetch='script', kind='html')
        self.row = dict(source_id='X', family='foxbit', split='dev', title='Fixture terms', url=self.source['fetch_url'],
                        final_url=self.source['fetch_url'], retrieved_utc='2026-11-07T00:00:00+00:00', http_status='200',
                        raw_path=self.bp.relative_to(self.root).as_posix(), raw_sha256=self.sha(self.body),
                        text_path=self.tp.relative_to(self.root).as_posix(), text_sha256=self.sha(self.text.encode()),
                        chars=len(self.text), origin='fixture', error='', exact_old_raw='False')
        self.write(self.raw / 'manifest.csv', [self.row])
        self.write(self.root / 'results/tables/P3-28_sources.csv', [self.source])
        self.patches = [patch.object(collector, 'ROOT', self.root), patch.object(collector, 'OUT', self.raw),
                        patch.object(collector, 'MANIFEST', self.raw / 'manifest.csv'),
                        patch.object(pilot, 'ROOT', self.root), patch.object(pilot, 'RAW', self.raw)]
        # configure mutates the imported P3-28 module; restore every affected value.
        for obj, names in [(pilot.P, ('RAW', 'RUNS', 'TEXT', 'doc_text')),
                           (pilot.P.M, ('RAW', 'MANIFEST', 'REF', 'CORPUS', 'SOURCES'))]:
            self.patches += [patch.object(obj, n, getattr(obj, n)) for n in names]
        for item in self.patches:
            item.start()

    def tearDown(self):
        for item in reversed(self.patches):
            item.stop()
        self.tmp.cleanup()

    @staticmethod
    def sha(body):
        return hashlib.sha256(body).hexdigest()

    @staticmethod
    def write(path, rows):
        with path.open('w', encoding='utf-8', newline='') as f:
            w = csv.DictWriter(f, list(rows[0])); w.writeheader(); w.writerows(rows)

    def freeze(self):
        collector.freeze()

    def test_collector_hash_validation(self):
        self.assertTrue(collector.validate(self.row))
        self.tp.write_text('Tampered document', encoding='utf-8')
        with self.assertRaisesRegex(ValueError, 'hash mismatch'):
            collector.validate(self.row)

    def test_error_shell_not_a_document(self):
        self.assertTrue(collector.shell_reason('Checking your browser. ' * 10, b'<title>Just a moment</title>'))
        self.assertFalse(collector.shell_reason(self.text, self.body))

    def test_manifest_paths_cannot_escape_raw(self):
        with self.assertRaisesRegex(ValueError, 'outside raw'):
            collector.raw_path('results/tables/labels.csv')

    def test_timestamped_source_resolves_through_frozen_corpus(self):
        self.freeze()
        pilot.configure()
        self.assertEqual(pilot.P.doc_text('X'), self.text)

    def test_stale_stable_alias_cannot_override_frozen_text(self):
        self.freeze()
        (self.raw / 'text/X.txt').write_text('Wrong old content', encoding='utf-8')
        pilot.configure()
        self.assertEqual(pilot.P.doc_text('X'), self.text)

    def test_tampered_frozen_source_refused(self):
        self.freeze()
        self.tp.write_text('Changed after freeze', encoding='utf-8')
        with self.assertRaises((ValueError, SystemExit)):
            pilot.configure()

    def test_no_tools_method_rejects_tool_trace(self):
        events = [{'type': 'item.completed', 'item': {'type': 'command_execution', 'command': 'rg Pix X.txt'}}]
        self.assertTrue(pilot.trace_violations(events, 'B2', Path('case')))

    def test_adaptive_network_trace_rejected(self):
        events = [{'type': 'item.completed', 'item': {'type': 'command_execution', 'command': 'curl https://example.invalid'}}]
        self.assertTrue(pilot.trace_violations(events, 'A', Path('case')))

    def test_adaptive_write_trace_rejected(self):
        events = [{'type': 'item.completed', 'item': {'type': 'command_execution', 'command': 'Set-Content X.txt changed'}}]
        self.assertTrue(pilot.trace_violations(events, 'A', Path('case')))

    def test_adaptive_started_tool_not_hidden(self):
        events = [{'type': 'item.started', 'item': {'type': 'command_execution', 'command': 'curl https://example.invalid'}}]
        self.assertTrue(pilot.trace_violations(events, 'A', Path('case')))

    def test_v3_rejects_shell_even_for_benign_search(self):
        events = [{'type': 'item.completed', 'item': {'type': 'command_execution',
                   'command': "rg -n 'Pix|USDC|USDT' *.txt | Select-Object -First 20"}}]
        self.assertTrue(pilot.trace_violations(events, 'A', Path('case')))

    def test_v3_allows_only_scoped_reader(self):
        good = [{'type': 'item.completed', 'item': {'id':'x','type': 'mcp_tool_call',
                 'server':'corpus','tool':'corpus_read','arguments':{'filename':'X.txt'}}}]
        self.assertEqual(pilot.trace_violations(good, 'A', Path('case')), [])
        self.assertTrue(pilot.trace_violations(good, 'B1', Path('case')))


if __name__ == '__main__':
    unittest.main(verbosity=2)

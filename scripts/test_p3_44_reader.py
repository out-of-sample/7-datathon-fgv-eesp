"""Independent frozen-corpus MCP reader tests; synthetic files, no models or outside reads.

Run: python scripts/test_p3_44_reader.py
All fixtures and optional symlinks remain inside one temporary scratch directory.
"""
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from p3_44_corpus_reader import Reader, TOOLS


class ReaderTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory(prefix='p344_reader_', dir=Path(__file__).resolve().parents[1] / 'scratch')
        self.base = Path(self.tmp.name)
        self.root = self.base / 'case'
        self.root.mkdir()
        self.a = 'Pix deposits require company verification. USDT is supported on this documented network.'
        (self.root / 'A-01.txt').write_text(self.a, encoding='utf-8')
        (self.root / 'E-05.1.txt').write_text('A second source describes conditional Pix access.', encoding='utf-8')
        (self.root / 'ignored.json').write_text('{}', encoding='utf-8')
        self.reader = Reader(self.root)

    def tearDown(self):
        self.tmp.cleanup()

    def test_only_three_read_only_tools(self):
        self.assertEqual({t['name'] for t in TOOLS}, {'corpus_list', 'corpus_read', 'corpus_search'})
        self.assertTrue(all(t['annotations']['readOnlyHint'] for t in TOOLS))

    def test_list_only_text_sources(self):
        rows = self.reader.call('corpus_list', {})
        self.assertEqual([r['filename'] for r in rows], ['A-01.txt', 'E-05.1.txt'])
        self.assertEqual(rows[0]['characters'], len(self.a))

    def test_read_offsets_and_limits(self):
        result = self.reader.call('corpus_read', {'filename': 'A-01.txt', 'offset': 4, 'limit': 8})
        self.assertEqual(result['text'], self.a[4:12])
        self.assertEqual(result['total_characters'], len(self.a))
        self.assertEqual(self.reader.call('corpus_read', {'filename': 'A-01.txt', 'offset': 10000})['text'], '')

    def test_search_literal_case_insensitive(self):
        rows = self.reader.call('corpus_search', {'query': 'PIX'})
        self.assertEqual({r['filename'] for r in rows}, {'A-01.txt', 'E-05.1.txt'})
        one = self.reader.call('corpus_search', {'query': 'Pix', 'filename': 'E-05.1.txt'})
        self.assertEqual(len(one), 1)
        self.assertEqual(one[0]['filename'], 'E-05.1.txt')
        self.assertEqual(self.reader.call('corpus_search', {'query': '.*'}), [])

    def test_search_result_cap(self):
        (self.root / 'A-01.txt').write_text('pix ' * 100, encoding='utf-8')
        rows = self.reader.call('corpus_search', {'query': 'pix'})
        self.assertLessEqual(len(rows), 60)

    def test_read_boundaries_rejected(self):
        for values in ({'offset': -1}, {'limit': 0}, {'limit': -1}, {'limit': 48001}):
            with self.subTest(values=values), self.assertRaises((ValueError, TypeError)):
                self.reader.call('corpus_read', {'filename': 'A-01.txt', **values})

    def test_malformed_numeric_types_rejected(self):
        for field in ('offset', 'limit'):
            for value in (True, False, '1', 1.5, None, [], {}):
                with self.subTest(field=field, value=value), self.assertRaises((ValueError, TypeError)):
                    self.reader.call('corpus_read', {'filename': 'A-01.txt', field: value})

    def test_search_bounds_and_types_rejected(self):
        for query in ('', '  ', 'x' * 201, 1, True, None, [], {}):
            with self.subTest(query=query), self.assertRaises((ValueError, TypeError)):
                self.reader.call('corpus_search', {'query': query})

    def test_missing_and_extra_arguments_rejected(self):
        for name, args in [('corpus_read', {}), ('corpus_search', {}), ('corpus_list', {'write': True}),
                           ('corpus_read', {'filename': 'A-01.txt', 'write': 'changed'}),
                           ('corpus_search', {'query': 'Pix', 'outside': '..'})]:
            with self.subTest(name=name, args=args), self.assertRaises((ValueError, TypeError, KeyError)):
                self.reader.call(name, args)
        for args in (None, [], 'A-01.txt', 1):
            with self.subTest(args=args), self.assertRaises((ValueError, TypeError)):
                self.reader.call('corpus_list', args)

    def test_path_escapes_and_unknown_names_rejected(self):
        names = ['../outside.txt', '..\\outside.txt', str(self.base / 'outside.txt'),
                 'C:/outside.txt', '/etc/passwd', '$HOME/secret.txt', 'missing.txt', 'ignored.json']
        for filename in names:
            with self.subTest(filename=filename), self.assertRaises((ValueError, TypeError)):
                self.reader.call('corpus_read', {'filename': filename})
            with self.subTest(search_filename=filename), self.assertRaises((ValueError, TypeError)):
                self.reader.call('corpus_search', {'query': 'Pix', 'filename': filename})

    def test_symlink_rechecked_before_read(self):
        # Simulate a source becoming a link after enumeration; never read an outside path.
        with patch.object(Path, 'is_symlink', return_value=True):
            with self.assertRaisesRegex(ValueError, 'outside'):
                self.reader.call('corpus_read', {'filename': 'A-01.txt'})

    def test_real_symlink_excluded_when_supported(self):
        target = self.base / 'outside.txt'
        target.write_text('Synthetic outside case fixture; must not be read.', encoding='utf-8')
        link = self.root / 'Link.txt'
        try:
            link.symlink_to(target)
        except OSError as exc:
            self.skipTest('Windows symlink privilege unavailable: ' + str(exc))
        reader = Reader(self.root)
        self.assertNotIn('Link.txt', reader.files)
        with self.assertRaises(ValueError):
            reader.call('corpus_read', {'filename': 'Link.txt'})

    def test_unknown_write_tools_rejected_and_files_unchanged(self):
        before = {p.name: p.read_bytes() for p in self.root.iterdir()}
        for name in ('corpus_write', 'write_file', 'shell', 'network'):
            with self.assertRaises(ValueError):
                self.reader.call(name, {'filename': 'A-01.txt', 'content': 'changed'})
        self.assertEqual(before, {p.name: p.read_bytes() for p in self.root.iterdir()})

    def test_stdio_protocol_and_error_response(self):
        script = Path(__file__).with_name('p3_44_corpus_reader.py')
        messages = [
            {'jsonrpc': '2.0', 'id': 1, 'method': 'initialize', 'params': {'protocolVersion': '2024-11-05'}},
            {'jsonrpc': '2.0', 'method': 'notifications/initialized'},
            {'jsonrpc': '2.0', 'id': 2, 'method': 'tools/list'},
            {'jsonrpc': '2.0', 'id': 3, 'method': 'tools/call', 'params': {'name': 'corpus_read', 'arguments': {'filename': 'A-01.txt', 'limit': 3}}},
            {'jsonrpc': '2.0', 'id': 4, 'method': 'tools/call', 'params': {'name': 'corpus_write', 'arguments': {}}},
        ]
        result = subprocess.run([sys.executable, '-u', str(script), '--root', str(self.root)],
                                input='\n'.join(json.dumps(x) for x in messages) + '\n',
                                capture_output=True, text=True, encoding='utf-8', timeout=10, check=True)
        replies = {r['id']: r for r in map(json.loads, result.stdout.splitlines())}
        self.assertEqual(set(replies), {1, 2, 3, 4})
        self.assertEqual(len(replies[2]['result']['tools']), 3)
        self.assertEqual(json.loads(replies[3]['result']['content'][0]['text'])['text'], 'Pix')
        self.assertTrue(replies[4]['result']['isError'])


if __name__ == '__main__':
    unittest.main(verbosity=2)

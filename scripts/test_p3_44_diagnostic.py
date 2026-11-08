"""Safety boundary tests for the post-hoc diagnostic waiver."""
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

import p3_44_diagnostic as D


class WaiverTests(unittest.TestCase):
    def setUp(self):
        folder = D.ROOT / 'scratch/p3_44_diagnostic_tests'
        folder.mkdir(parents=True, exist_ok=True)
        self.tmp = tempfile.TemporaryDirectory(dir=folder)
        self.addCleanup(self.tmp.cleanup)
        root = Path(self.tmp.name)
        for name, value in dict(WORK=root/'work', FREEZE=root/'freeze', RUNS=root/'runs').items():
            patcher = patch.object(D.pilot, name, value)
            patcher.start()
            self.addCleanup(patcher.stop)
        self.path = D.pilot.FREEZE/'workspaces_v4/A_H-01_r1/X.txt'
        self.trace = D.pilot.RUNS/'A/H-01_r1_call1.jsonl'
        self.trace.parent.mkdir(parents=True)
        self.events = [dict(type='SYSTEM_MESSAGE', content=str(self.path.parent)),
            dict(type='PLANNER_RESPONSE', tool_calls=[dict(name='view_file', args=dict(AbsolutePath=str(self.path)))]),
            dict(type='GENERIC', status='ERROR', error=f'{self.path}: The system cannot find the path specified.')]
        self.record = dict(errors=['adaptive_tool_outside_corpus_reader'], permitted=['X'])

    def check(self):
        self.trace.write_text('\n'.join(json.dumps(e) for e in self.events), encoding='utf-8')
        return D.eligible('H-01', 1, self.record)

    def test_only_confirmed_dispatch_error_is_waived(self):
        self.assertEqual(self.check(), 1)

    def test_successful_outside_read_is_never_waived(self):
        self.events[2] = dict(type='GENERIC', status='DONE', content='Outside evidence')
        self.assertEqual(self.check(), 0)

    def test_other_failure_is_retained(self):
        self.record['errors'].append('timeout')
        self.assertEqual(self.check(), 0)

    def test_unrelated_outside_attempt_is_retained(self):
        self.events[1]['tool_calls'][0]['args']['AbsolutePath'] = str(self.path.parent/'secret.txt')
        self.assertEqual(self.check(), 0)

    def test_unconfirmed_error_is_retained(self):
        self.events[2]['error'] = 'Permission denied'
        self.assertEqual(self.check(), 0)

    def test_additional_forbidden_tool_is_retained(self):
        self.events.append(dict(type='PLANNER_RESPONSE', tool_calls=[dict(name='read_url_content', args={})]))
        self.assertEqual(self.check(), 0)


if __name__ == '__main__':
    unittest.main()

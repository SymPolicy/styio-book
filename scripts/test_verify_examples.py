import json
import subprocess
import tempfile
import unittest
from pathlib import Path
from verify_examples import safe_path, judge, load_manifest

class CookbookVerifierTest(unittest.TestCase):
    def test_manifest(self):
        data = load_manifest()
        self.assertEqual(9, len(data['cases']))
        self.assertEqual(3, sum(bool(c.get('expect_failure')) for c in data['cases']))
    def test_escape_paths_rejected(self):
        for path in ('../x', '/tmp/shared', 'C:\\x', 'a/../../x', ''):
            with self.subTest(path=path), self.assertRaises(ValueError):
                safe_path(path)
    def test_negative_is_not_success(self):
        case = {'expect_failure': True}
        data = {'stderr_source': b'expected diagnostic\n'}
        for status in (0, -11):
            p = subprocess.CompletedProcess([], status, b'', b'expected diagnostic')
            self.assertTrue(judge(case, data, p, Path('.')))
    def test_negative_requires_fragment(self):
        p = subprocess.CompletedProcess([], 1, b'', b'unrelated error')
        self.assertTrue(judge({'expect_failure': True}, {'stderr_source': b'expected'}, p, Path('.')))
    def test_negative_accepts_diagnostic_rejection(self):
        p = subprocess.CompletedProcess([], 1, b'', b'error: expected\n')
        self.assertEqual([], judge({'expect_failure': True}, {'stderr_source': b'expected\n'}, p, Path('.')))
    def test_stdout_is_exact(self):
        p = subprocess.CompletedProcess([], 0, b'92', b'')
        self.assertTrue(judge({}, {'stdout_source': b'92\n'}, p, Path('.')))
    def test_artifact_missing_fails(self):
        with tempfile.TemporaryDirectory() as tmp:
            p = subprocess.CompletedProcess([], 0, b'', b'')
            self.assertTrue(judge({'artifact': {'path': 'out', 'text': '204060'}}, {}, p, Path(tmp)))
    def test_artifact_compares_bytes(self):
        with tempfile.TemporaryDirectory() as tmp:
            Path(tmp, 'out').write_bytes(b'204060')
            p = subprocess.CompletedProcess([], 0, b'', b'')
            self.assertEqual([], judge({'artifact': {'path': 'out', 'text': '204060'}}, {}, p, Path(tmp)))
    def test_duplicate_case_rejected(self):
        data = load_manifest(); data['cases'].append(data['cases'][0])
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp, 'cases.json'); path.write_text(json.dumps(data))
            with self.assertRaisesRegex(ValueError, 'duplicate'):
                load_manifest(path)

if __name__ == '__main__':
    unittest.main()

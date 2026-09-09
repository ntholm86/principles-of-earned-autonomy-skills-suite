from pathlib import Path
import subprocess
import sys
import tempfile
import unittest


HOOK = Path(__file__).resolve().parents[1] / "tools" / "hooks" / "pre-commit"


class TrailHookTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory(prefix="pea-hook-test-")
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name)
        self.git("init", "--quiet")
        self.original_blob = self.git("hash-object", "-w", "--stdin", input_text="original\n")
        self.changed_blob = self.git("hash-object", "-w", "--stdin", input_text="changed\n")

    def git(self, *arguments, input_text=None):
        return subprocess.run(
            ["git", *arguments], cwd=self.root, input=input_text,
            capture_output=True, text=True, check=True,
        ).stdout.strip()

    def stage(self, path, blob=None):
        self.git("update-index", "--add", "--cacheinfo",
                 f"100644,{blob or self.changed_blob},{path}")

    def baseline(self, *paths):
        for path in paths:
            self.stage(path, self.original_blob)
        tree = self.git("write-tree")
        commit = self.git(
            "-c", "user.name=Hook Test", "-c", "user.email=hook-test@example.invalid",
            "commit-tree", tree, input_text="fixture\n",
        )
        self.git("update-ref", "HEAD", commit)

    def assert_hook(self, expected):
        result = subprocess.run(
            [sys.executable, str(HOOK)], cwd=self.root,
            capture_output=True, text=True,
        )
        self.assertEqual(result.returncode, expected, result.stdout + result.stderr)
        if expected == 1:
            self.assertIn("without a .acm/audit-trail.md update", result.stdout)

    def test_project_additions_require_trail(self):
        for path in ("src/checkout.ts", "src/main.py", "package.json", "README.md",
                     "harness/tools/example.py", "assets/image.png", "src/caf\u00e9.ts"):
            with self.subTest(path=path):
                self.git("read-tree", "--empty")
                self.stage(path)
                self.assert_hook(1)

    def test_project_modification_requires_trail(self):
        self.baseline("src/checkout.ts")
        self.stage("src/checkout.ts")
        self.assert_hook(1)

    def test_project_deletion_requires_trail(self):
        self.baseline("src/checkout.ts")
        self.git("update-index", "--force-remove", "src/checkout.ts")
        self.assert_hook(1)

    def test_added_repo_or_task_trail_allows_project_change(self):
        for trail in (".acm/audit-trail.md", ".acm/checkout/audit-trail.md"):
            with self.subTest(trail=trail):
                self.git("read-tree", "--empty")
                self.stage("src/checkout.ts")
                self.stage(trail)
                self.assert_hook(0)

    def test_modified_trail_allows_project_deletion(self):
        self.baseline("src/checkout.ts", ".acm/audit-trail.md")
        self.git("update-index", "--force-remove", "src/checkout.ts")
        self.stage(".acm/audit-trail.md")
        self.assert_hook(0)

    def test_deleted_trail_does_not_satisfy_gate(self):
        self.baseline(".acm/audit-trail.md")
        self.git("update-index", "--force-remove", ".acm/audit-trail.md")
        self.stage("src/checkout.ts")
        self.assert_hook(1)

    def test_unstaged_trail_does_not_satisfy_gate(self):
        self.stage("src/checkout.ts")
        trail = self.root / ".acm" / "audit-trail.md"
        trail.parent.mkdir()
        trail.write_text("new entry\n", encoding="utf-8")
        self.assert_hook(1)

    def test_other_evidence_does_not_satisfy_gate(self):
        self.stage("src/checkout.ts")
        self.stage(".acm/history.md")
        self.assert_hook(1)

    def test_empty_or_evidence_only_index_is_allowed(self):
        self.assert_hook(0)
        self.stage(".acm/history.md")
        self.assert_hook(0)

    def test_rename_out_of_evidence_requires_trail(self):
        self.baseline(".acm/note.md")
        self.git("update-index", "--force-remove", ".acm/note.md")
        self.stage("note.md", self.original_blob)
        self.assert_hook(1)


if __name__ == "__main__":
    unittest.main()
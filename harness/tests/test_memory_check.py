import importlib.util
import json
import tempfile
import unittest
from pathlib import Path

SPEC = importlib.util.spec_from_file_location(
    "memory_check", Path(__file__).resolve().parents[1] / "tools" / "memory_check.py"
)
memory_check = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(memory_check)

COMMIT_A = "a" * 40
COMMIT_B = "b" * 40
GOOD_MISSION = (
    "# mission.md\n\n<!-- current-mission: complete -->\n\n## What this is\n\nx\n\n"
    "## Human gate\n\nThe author reviews every change.\n\n<!-- mission-history -->\n\n## History\n"
)
GOOD_RECORD = (
    "## 2026-11-22 — thing\n\n- record: 20261122T010203Z-thing\n- time: 2026-11-22T01.02.03Z\n- scope: memory-wide\n"
    "- agent: a\n- authority: the author\n- session: s1\n- mandate: memory at abc\n\n### Decision\n\n[!DECISION] x\n"
)


class MemoryCheckTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name)
        (self.root / ".acm-root").write_text("", encoding="utf-8")
        self.addCleanup(self.tmp.cleanup)

    def write(self, rel, text):
        path = self.root / rel
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text, encoding="utf-8")

    def binding(self, repo, commits, id=None):
        self.write(f"repositories/{repo}/repository.json", json.dumps({"id": id or repo, "root_commits": commits}))

    def run_check(self):
        return memory_check.check(self.root)

    def test_a_valid_memory_passes(self):
        self.write("mission.md", GOOD_MISSION)
        self.write("records/20261122T010203Z-thing.md", GOOD_RECORD)
        self.binding("r", [COMMIT_A])
        self.write("repositories/r/mission.md", GOOD_MISSION)
        self.write("repositories/r/tasks/t/mission.md", GOOD_MISSION)
        self.assertEqual(self.run_check(), ([], []))

    def test_missing_marker_hidden_folder_and_retired_name_fail(self):
        (self.root / ".acm-root").unlink()
        self.write("repositories/r/.acm/x.md", "x")
        self.write("repositories/r/orientation.md", "old")
        self.write("repositories/r/destination.md", "old")
        failures, _ = self.run_check()
        joined = "\n".join(failures)
        self.assertIn("no .acm-root", joined)
        self.assertIn("hidden .acm/", joined)
        self.assertIn("retired file name", joined)

    def test_mission_without_a_gate_or_with_misordered_markers_fails(self):
        self.write("mission.md", GOOD_MISSION.replace("## Human gate", "## Something else"))
        self.write("repositories/r/mission.md", "<!-- mission-history -->\n<!-- current-mission: complete -->\n")
        failures, _ = self.run_check()
        self.assertTrue(any("Human gate" in f for f in failures))
        self.assertTrue(any("in that order" in f for f in failures))

    def test_a_gate_in_the_history_does_not_count(self):
        self.write("mission.md", GOOD_MISSION.replace("## Human gate", "## Gate").replace("## History", "## Human gate"))
        failures, _ = self.run_check()
        self.assertTrue(any("Human gate" in f for f in failures))

    def test_an_empty_gate_fails_and_an_unfilled_stub_warns(self):
        self.write("mission.md", GOOD_MISSION.replace("The author reviews every change.", ""))
        self.write("records/20261122T010203Z-thing.md", GOOD_RECORD.replace("- agent: a", "- agent: TODO (model)"))
        failures, warnings = self.run_check()
        self.assertTrue(any("is empty" in f for f in failures))
        self.assertTrue(any("unfilled stub field" in w and "agent" in w for w in warnings))

    def test_bindings_must_be_valid_and_unambiguous(self):
        self.binding("one", [COMMIT_A])
        self.binding("two", [COMMIT_A, COMMIT_B])
        self.binding("three", ["short"])
        self.binding("four", [COMMIT_B], id="other")
        failures, _ = self.run_check()
        joined = "\n".join(failures)
        self.assertIn("ambiguous binding", joined)
        self.assertIn("40-hex", joined)
        self.assertIn("differs from the folder name", joined)

    def test_record_names_and_identifiers(self):
        self.write("records/notes.md", "## 2026-11-22 — x\n")
        self.write("records/20261122T010203Z-other.md", GOOD_RECORD)
        failures, _ = self.run_check()
        joined = "\n".join(failures)
        self.assertIn("records/notes.md", joined)
        self.assertIn("differs from the file name", joined)

    def test_missing_attribution_is_only_a_warning(self):
        self.write("records/20261122T010203Z-thing.md", "## 2026-11-22 — thing\n\n- record: 20261122T010203Z-thing\n\n### Decision\n")
        failures, warnings = self.run_check()
        self.assertEqual(failures, [])
        self.assertEqual(len(warnings), 1)
        self.assertIn("authority", warnings[0])

    def test_an_unknown_record_format_fails_and_a_missing_one_is_format_one(self):
        self.write("records/20261122T010203Z-thing.md", GOOD_RECORD.replace("- time:", "- format: 9\n- time:"))
        self.write("records/20261122T010204Z-old.md", GOOD_RECORD.replace("20261122T010203Z-thing", "20261122T010204Z-old"))
        failures, _ = self.run_check()
        self.assertEqual(len(failures), 1)
        self.assertIn("format: 9", failures[0])

    def test_a_code_folder_named_drafts_is_a_path_scope(self):
        self.write("repositories/r/paths/drafts/mission.md", GOOD_MISSION)
        names = {p.relative_to(self.root).as_posix() for p in memory_check.scopes(self.root)}
        self.assertIn("repositories/r/paths/drafts", names)

    def test_a_symbolic_link_in_the_memory_fails(self):
        self.write("target.md", "x")
        try:
            (self.root / "link.md").symlink_to(self.root / "target.md")
        except (OSError, NotImplementedError):
            self.skipTest("symbolic links are not available here")
        failures, _ = self.run_check()
        self.assertTrue(any("link.md" in f and "symbolic link" in f for f in failures))

    def test_history_finds_an_edited_record_until_a_later_record_acknowledges_it(self):
        import subprocess

        def git(*arguments):
            return subprocess.run(
                ["git", "-c", "user.name=T", "-c", "user.email=t@example.invalid", "-c", "commit.gpgsign=false", *arguments],
                cwd=self.root, capture_output=True, text=True, check=True,
            ).stdout.strip()

        git("init", "--quiet")
        self.write("records/20261122T010203Z-thing.md", GOOD_RECORD)
        git("add", "."); git("commit", "--quiet", "-m", "accept")
        self.write("records/20261122T010203Z-thing.md", GOOD_RECORD + "\nedited\n")
        git("add", "."); git("commit", "--quiet", "-m", "edit")
        found = memory_check.history_failures(self.root)
        self.assertEqual(len(found), 1)
        self.assertIn("modified", found[0])
        self.assertEqual(memory_check.check(self.root)[0], [])  # history is only checked when asked for
        sha = git("rev-parse", "HEAD")[:7]
        self.write(
            "records/20261122T020304Z-override.md",
            GOOD_RECORD.replace("20261122T010203Z-thing", "20261122T020304Z-override").replace("- time:", f"- overrides: {sha}\n- time:"),
        )
        self.assertEqual(memory_check.history_failures(self.root), [])

    def test_scopes_under_paths_and_tasks_are_found(self):
        self.write("repositories/r/paths/src/area/mission.md", GOOD_MISSION)
        self.write("repositories/r/paths/src/area/tasks/t/mission.md", GOOD_MISSION)
        self.write("repositories/r/paths/src/area/records/readme.md", "x")
        names = {p.relative_to(self.root).as_posix() for p in memory_check.scopes(self.root)}
        self.assertIn("repositories/r/paths/src/area", names)
        self.assertIn("repositories/r/paths/src/area/tasks/t", names)
        failures, _ = self.run_check()
        self.assertTrue(any("readme.md" in f for f in failures))


if __name__ == "__main__":
    unittest.main()

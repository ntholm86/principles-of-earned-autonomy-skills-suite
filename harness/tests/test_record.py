import importlib.util
import json
import os
from pathlib import Path
import re
import subprocess
import sys
import tempfile
import unittest


RECORD = Path(__file__).resolve().parents[1] / "tools" / "record.py"
SPEC = importlib.util.spec_from_file_location("trail_record", RECORD)
record = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(record)

ENTRY = "## {date} \u2014 {slug}\n\n- target: t\n- agent: unknown\n- skill: trail\n- outcome: {slug} done\n"


class MemoryFixture(unittest.TestCase):
    def setUp(self):
        # Fixtures live beside the tests, not in a system temporary directory.
        self.temporary = tempfile.TemporaryDirectory(prefix="_record-test-", dir=Path(__file__).parent)
        self.addCleanup(self.temporary.cleanup)
        self.base = Path(self.temporary.name)
        self.registry = self.base / "memories"

    def git(self, cwd, *arguments):
        return subprocess.run(
            ["git", "-c", "user.name=Record Test", "-c", "user.email=record-test@example.invalid",
             "-c", "commit.gpgsign=false", *arguments],
            cwd=cwd, capture_output=True, text=True, check=True,
        ).stdout.strip()

    def work_repo(self, relative, message="root"):
        path = self.base / relative
        path.mkdir(parents=True)
        self.git(path, "init", "--quiet")
        self.git(path, "commit", "--quiet", "--allow-empty", "-m", message)
        return path, self.git(path, "rev-list", "--max-parents=0", "HEAD")

    def memory_repo(self, name, bindings):
        memory = self.base / name
        memory.mkdir()
        (memory / ".acm-root").write_text("", encoding="utf-8")
        for repo_id, root in bindings.items():
            folder = memory / "repositories" / repo_id
            folder.mkdir(parents=True)
            (folder / "repository.json").write_text(
                json.dumps({"id": repo_id, "root_commits": [root], "locators": []}), encoding="utf-8"
            )
        return memory

    def register(self, *memories):
        self.registry.write_text("".join(f"{m}\n" for m in memories), encoding="utf-8")

    def run_record(self, cwd, *arguments):
        env = {k: v for k, v in os.environ.items() if k not in ("TRAIL_ROOT", "ACM_SCOPE")}
        env["ACM_MEMORIES_FILE"] = str(self.registry)
        return subprocess.run(
            [sys.executable, str(RECORD), *arguments], cwd=cwd, env=env,
            capture_output=True, text=True, encoding="utf-8",
        )

    def assert_resolves(self, cwd, scope):
        result = self.run_record(cwd, "resolve")
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(Path(result.stdout.strip()).resolve(), scope.resolve())


class ResolutionTests(MemoryFixture):
    def test_root_commit_binding_survives_a_renamed_clone(self):
        work, root = self.work_repo("work")
        memory = self.memory_repo("memory", {"work": root})
        self.register(memory)
        scope = memory / "repositories" / "work"
        self.assert_resolves(work, scope)
        clone = self.base / "renamed-clone"
        self.git(self.base, "clone", "--quiet", str(work), str(clone))
        self.assert_resolves(clone, scope)

    def test_same_named_repositories_with_different_roots_are_not_conflated(self):
        first, first_root = self.work_repo("a/project", "first")
        second, second_root = self.work_repo("b/project", "second")
        memory = self.memory_repo("memory", {"project": first_root})
        self.register(memory)
        self.assert_resolves(first, memory / "repositories" / "project")
        unbound = self.run_record(second, "resolve")
        self.assertEqual(unbound.returncode, 2)
        self.assertIn("unbound", unbound.stderr)

    def test_zero_matches_is_unbound(self):
        work, _ = self.work_repo("work")
        self.register(self.memory_repo("memory", {"other": "0" * 40}))
        result = self.run_record(work, "resolve")
        self.assertEqual(result.returncode, 2)
        self.assertTrue(result.stderr.startswith("unbound:"), result.stderr)
        self.assertEqual(result.stdout, "")

    def test_two_matching_bindings_are_ambiguous(self):
        work, root = self.work_repo("work")
        self.register(self.memory_repo("one", {"work": root}), self.memory_repo("two", {"copy": root}))
        result = self.run_record(work, "resolve")
        self.assertEqual(result.returncode, 3)
        self.assertTrue(result.stderr.startswith("ambiguous:"), result.stderr)

    def test_missing_registry_is_unbound_and_missing_memory_is_unavailable(self):
        work, _ = self.work_repo("work")
        missing = self.run_record(work, "resolve")
        self.assertEqual(missing.returncode, 2)
        self.assertIn("no memory registry", missing.stderr)
        self.register(self.base / "not-a-memory")
        unavailable = self.run_record(work, "resolve")
        self.assertEqual(unavailable.returncode, 4)
        self.assertIn("no .acm-root", unavailable.stderr)


class RecordingTests(MemoryFixture):
    def test_create_only_acceptance_is_idempotent_and_never_overwrites(self):
        trail = self.base / "trail"
        first, created = record._create_record(trail, "20261121T000000Z", "slug", lambda rid: "one\n")
        self.assertTrue(created)
        again, created = record._create_record(trail, "20261121T000000Z", "slug", lambda rid: "one\n")
        self.assertEqual((again, created), (first, False))
        other, created = record._create_record(trail, "20261121T000000Z", "slug", lambda rid: "two\n")
        self.assertTrue(created)
        self.assertEqual(other.name, "20261121T000000Z-slug-2.md")
        self.assertEqual(first.read_text(encoding="utf-8"), "one\n")

    def test_bound_new_creates_an_attributed_record_and_nothing_in_the_work_repo(self):
        work, root = self.work_repo("work")
        memory = self.memory_repo("memory", {"work": root})
        self.git(memory, "init", "--quiet")
        self.git(memory, "add", ".")
        self.git(memory, "commit", "--quiet", "-m", "memory")
        self.register(memory)
        result = self.run_record(work, "new", "--slug", "First Change", "--skill", "trail")
        self.assertEqual(result.returncode, 0, result.stderr)
        records = list((memory / "repositories" / "work" / "trail").glob("*.md"))
        self.assertEqual(len(records), 1)
        self.assertRegex(records[0].name, r"^\d{8}T\d{6}Z-first-change\.md$")
        text = records[0].read_text(encoding="utf-8")
        self.assertIn(f"- record: {records[0].stem}\n", text)
        self.assertIn("- scope: repositories/work\n", text)
        self.assertIn(f"- repository: work @ {root}\n", text)
        self.assertIn(f"- mandate: {self.git(memory, 'rev-parse', 'HEAD')}\n", text)
        self.assertFalse((work / ".acm").exists())

    def test_unbound_new_writes_nothing(self):
        work, _ = self.work_repo("work")
        self.register(self.memory_repo("memory", {}))
        result = self.run_record(work, "new", "--slug", "x")
        self.assertEqual(result.returncode, 2)
        self.assertFalse((work / ".acm").exists())

    def test_unbound_repo_with_in_repo_acm_keeps_the_legacy_single_file(self):
        work, _ = self.work_repo("work")
        self.register(self.memory_repo("memory", {}))
        log = work / ".acm" / "audit-trail.md"
        log.parent.mkdir()
        log.write_text("# Audit trail\n", encoding="utf-8")
        result = self.run_record(work, "new", "--slug", "legacy-entry")
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("legacy in-repo memory", result.stderr)
        self.assertIn("legacy-entry", log.read_text(encoding="utf-8"))
        self.assertFalse((work / ".acm" / "trail").exists())

    def test_history_reads_legacy_trail_then_records_in_filename_order(self):
        work, root = self.work_repo("work")
        memory = self.memory_repo("memory", {"work": root})
        self.register(memory)
        scope = memory / "repositories" / "work"
        (scope / "trail").mkdir(parents=True)
        (scope / "audit-trail.md").write_text(
            "# Audit trail\n\n" + ENTRY.format(date="2026-01-01", slug="legacy"), encoding="utf-8"
        )
        (scope / "trail" / "20260102T000000Z-later.md").write_text(
            ENTRY.format(date="2026-01-02", slug="later"), encoding="utf-8"
        )
        (scope / "trail" / "20260101T120000Z-earlier.md").write_text(
            ENTRY.format(date="2026-01-01", slug="earlier"), encoding="utf-8"
        )
        result = self.run_record(work, "history")
        self.assertEqual(result.returncode, 0, result.stderr)
        slugs = re.findall(r"Run\s+\d+\s+\S+\s+(\S+)", result.stdout)
        self.assertEqual(slugs, ["legacy", "earlier", "later"])
        written = self.run_record(work, "history", "--write")
        self.assertEqual(written.returncode, 0, written.stderr)
        history = (scope / "history.md").read_text(encoding="utf-8")
        self.assertIn("2 `trail/` record(s) at memory revision", history)


if __name__ == "__main__":
    unittest.main()

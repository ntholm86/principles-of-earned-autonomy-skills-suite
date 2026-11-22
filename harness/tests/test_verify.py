from contextlib import redirect_stdout
import importlib.util
from io import StringIO
from pathlib import Path
import unittest
from unittest.mock import Mock, patch


MODULE_SPEC = importlib.util.spec_from_file_location(
    "skills_verify", Path(__file__).resolve().parents[2] / "verify.py"
)
if MODULE_SPEC is None or MODULE_SPEC.loader is None:
    raise RuntimeError("Cannot load the repository verifier")
verify = importlib.util.module_from_spec(MODULE_SPEC)
MODULE_SPEC.loader.exec_module(verify)

BLOCKING_CHECKS = (
    "check_required_files",
    "check_log_format",
    "check_no_mojibake",
    "check_required_markdown_docs",
    "check_stale_path_tokens",
    "check_acm_scope_traversal_consistency",
    "check_session_files",
    "check_transcript_references",
    "check_session_fidelity_structure",
    "check_trigger_evaluation",
    "check_derived_artifact_freshness",
    "check_citation_version",
)


def synthetic_trail(body: str, slug: str | None = None, present: bool = True):
    text = (
        f"## 2026-09-05 - {slug or verify.REVERSAL_HONESTY_CONTRACT_SLUG}\n\n"
        f"{body}\n"
    )
    return patch.multiple(
        verify,
        SCOPE=Path("scope"),
        _trail_files=Mock(return_value=[Path("scope/audit-trail.md")] if present else []),
        _trail_text=Mock(return_value=text),
    )


class ReversalReviewTests(unittest.TestCase):
    def test_unmarked_cues_remain_visible_for_review(self):
        for body in (
            "No file or commit was reverted.",
            "The file was reverted after the test failed.",
            'An example of a reversal is "I reverted the change".',
        ):
            with self.subTest(body=body), synthetic_trail(body):
                warnings = verify.check_reversal_honesty_gate()
                self.assertEqual(len(warnings), 1)
                self.assertIn("reverted", warnings[0])

    def test_marked_reversal_needs_no_warning(self):
        with synthetic_trail("[!REVERSAL] The file was reverted."):
            self.assertEqual(verify.check_reversal_honesty_gate(), [])

    def test_cueless_text_is_not_claimed_as_semantically_verified(self):
        body = "Initially chose X; later chose Y instead after the check failed."
        with synthetic_trail(body):
            self.assertEqual(verify.check_reversal_honesty_gate(), [])

    def test_pre_contract_entry_is_not_flagged(self):
        with synthetic_trail("The file was reverted.", "older-entry"):
            self.assertEqual(verify.check_reversal_honesty_gate(), [])

    def test_missing_log_is_left_to_blocking_checks(self):
        with synthetic_trail("The file was reverted.", present=False):
            self.assertEqual(verify.check_reversal_honesty_gate(), [])


class CitationVersionTests(unittest.TestCase):
    def check(self, changelog: str, citation: str) -> list[str]:
        import tempfile

        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "CHANGELOG.md").write_text(changelog, encoding="utf-8")
            (root / "CITATION.cff").write_text(citation, encoding="utf-8")
            with patch.object(verify, "ROOT", root):
                return verify.check_citation_version()

    def test_matching_versions_pass(self):
        self.assertEqual(self.check("# Changelog\n\n## v6.0.2 - 2026-11-22\n\n## v6.0.1 - x\n", 'version: "6.0.2"\n'), [])

    def test_stale_citation_fails(self):
        failures = self.check("# Changelog\n\n## v6.0.2 - 2026-11-22\n", 'version: "4.17.0"\n')
        self.assertEqual(len(failures), 1)
        self.assertIn("4.17.0", failures[0])
        self.assertIn("v6.0.2", failures[0])


class VerifierExitTests(unittest.TestCase):
    def run_verifier(self, body: str, failing_check: str | None = None):
        checks = {
            name: Mock(return_value=["structural defect"] if name == failing_check else [])
            for name in BLOCKING_CHECKS
        }
        output = StringIO()
        with patch.multiple(verify, **checks), synthetic_trail(body), redirect_stdout(output):
            exit_code = verify.main()
        for check in checks.values():
            check.assert_called_once_with()
        return exit_code, output.getvalue()

    def test_warning_only_is_visible_and_does_not_block(self):
        for body in ("No file or commit was reverted.", "The file was reverted."):
            with self.subTest(body=body):
                exit_code, output = self.run_verifier(body)
                self.assertEqual(exit_code, 0)
                self.assertIn("WARNING - 1 possible unrecorded reversal(s)", output)
                self.assertIn("word matches alone do not establish one", output)
                self.assertIn("reversal review warnings remain", output)
                self.assertNotIn("FAIL", output)

    def test_every_structural_check_still_blocks_with_warnings(self):
        for check_name in BLOCKING_CHECKS:
            with self.subTest(check=check_name):
                exit_code, output = self.run_verifier("The file was reverted.", check_name)
                self.assertEqual(exit_code, 1)
                self.assertIn("WARNING", output)
                self.assertIn("FAIL", output)
                self.assertIn("structural defect", output)
                self.assertNotIn("OK", output)

    def test_clean_run_keeps_existing_success_output(self):
        exit_code, output = self.run_verifier("[!REVERSAL] The file was reverted.")
        self.assertEqual(exit_code, 0)
        self.assertIn("trail integrity checks pass", output)
        self.assertNotIn("WARNING", output)


if __name__ == "__main__":
    unittest.main()
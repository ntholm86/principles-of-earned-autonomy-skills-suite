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
)


def synthetic_log(body: str, slug: str | None = None) -> Mock:
    log = Mock()
    log.exists.return_value = True
    log.read_text.return_value = (
        f"## 2026-09-05 - {slug or verify.REVERSAL_HONESTY_CONTRACT_SLUG}\n\n"
        f"{body}\n"
    )
    return log


class ReversalReviewTests(unittest.TestCase):
    def test_unmarked_cues_remain_visible_for_review(self):
        for body in (
            "No file or commit was reverted.",
            "The file was reverted after the test failed.",
            'An example of a reversal is "I reverted the change".',
        ):
            with self.subTest(body=body), patch.object(verify, "LOG", synthetic_log(body)):
                warnings = verify.check_reversal_honesty_gate()
                self.assertEqual(len(warnings), 1)
                self.assertIn("reverted", warnings[0])

    def test_marked_reversal_needs_no_warning(self):
        with patch.object(verify, "LOG", synthetic_log("[!REVERSAL] The file was reverted.")):
            self.assertEqual(verify.check_reversal_honesty_gate(), [])

    def test_cueless_text_is_not_claimed_as_semantically_verified(self):
        body = "Initially chose X; later chose Y instead after the check failed."
        with patch.object(verify, "LOG", synthetic_log(body)):
            self.assertEqual(verify.check_reversal_honesty_gate(), [])

    def test_pre_contract_entry_is_not_flagged(self):
        with patch.object(verify, "LOG", synthetic_log("The file was reverted.", "older-entry")):
            self.assertEqual(verify.check_reversal_honesty_gate(), [])

    def test_missing_log_is_left_to_blocking_checks(self):
        log = synthetic_log("The file was reverted.")
        log.exists.return_value = False
        with patch.object(verify, "LOG", log):
            self.assertEqual(verify.check_reversal_honesty_gate(), [])


class VerifierExitTests(unittest.TestCase):
    def run_verifier(self, body: str, failing_check: str | None = None):
        checks = {
            name: Mock(return_value=["structural defect"] if name == failing_check else [])
            for name in BLOCKING_CHECKS
        }
        output = StringIO()
        with patch.multiple(verify, **checks), patch.object(
            verify, "LOG", synthetic_log(body)
        ), redirect_stdout(output):
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
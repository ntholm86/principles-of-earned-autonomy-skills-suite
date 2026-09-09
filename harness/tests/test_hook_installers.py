import os
from pathlib import Path
import shutil
import subprocess
import tempfile
import unittest


TOOLS = Path(__file__).resolve().parents[1] / "tools"
POWERSHELL = shutil.which("powershell") or shutil.which("pwsh")
GIT = shutil.which("git")
GIT_EXEC_PATH = Path(subprocess.check_output([GIT, "--exec-path"], text=True).strip()) if GIT else None
GIT_BASH = GIT_EXEC_PATH.parents[2] / "usr" / "bin" / "bash.exe" if GIT_EXEC_PATH else None
BASH = (str(GIT_BASH) if GIT_BASH and GIT_BASH.is_file()
    else shutil.which("bash") if os.name != "nt" else None)


class InstallerCases:
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory(prefix="pea-install-test-")
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name)
        self.environment = dict(os.environ, GIT_CONFIG_NOSYSTEM="1", GIT_CONFIG_GLOBAL=os.devnull)
        self.git("init", "--quiet")
        self.git("config", "core.autocrlf", "false")
        self.git("config", "user.name", "Hook Test")
        self.git("config", "user.email", "hook-test@example.invalid")

    def git(self, *arguments, check=True):
        return subprocess.run(
            [GIT, *arguments], cwd=self.root, env=self.environment,
            capture_output=True, text=True, check=check,
        )

    def install(self):
        return subprocess.run(
            self.installer_command(), cwd=self.root, env=self.environment,
            capture_output=True, text=True,
        )

    def assert_installation_blocks_commit(self, target):
        result = self.install()
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertEqual(target.read_bytes(), (TOOLS / "hooks" / "pre-commit").read_bytes())
        source = self.root / "src" / "checkout.ts"
        source.parent.mkdir()
        source.write_text("export const total = 1;\n", encoding="utf-8")
        self.git("add", "src/checkout.ts")
        rejected = self.git("commit", "-m", "unlogged change", check=False)
        self.assertNotEqual(rejected.returncode, 0)
        self.assertIn("without a .acm/audit-trail.md update", rejected.stdout + rejected.stderr)
        trail = self.root / ".acm" / "audit-trail.md"
        trail.parent.mkdir()
        trail.write_text("fixture trail\n", encoding="utf-8")
        self.git("add", ".acm/audit-trail.md")
        accepted = self.git("commit", "-m", "logged change", check=False)
        self.assertEqual(accepted.returncode, 0, accepted.stdout + accepted.stderr)

    def test_default_location_activates_hook(self):
        self.assert_installation_blocks_commit(self.root / ".git" / "hooks" / "pre-commit")

    def test_missing_relative_custom_directory_is_created(self):
        self.git("config", "core.hooksPath", "custom hooks")
        self.assert_installation_blocks_commit(self.root / "custom hooks" / "pre-commit")
        self.assertFalse((self.root / ".git" / "hooks" / "pre-commit").exists())

    def test_absolute_custom_directory_activates_hook(self):
        target = self.root / "absolute hooks" / "pre-commit"
        self.git("config", "core.hooksPath", target.parent.as_posix())
        self.assert_installation_blocks_commit(target)

    def test_different_existing_hook_is_preserved(self):
        self.git("config", "core.hooksPath", "custom hooks")
        target = self.root / "custom hooks" / "pre-commit"
        target.parent.mkdir()
        original = b"#!/bin/sh\nexit 42\n"
        target.write_bytes(original)
        result = self.install()
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("existing hook differs", (result.stdout + result.stderr).lower())
        self.assertEqual(target.read_bytes(), original)

    def test_identical_hook_reinstallation_succeeds(self):
        first = self.install()
        self.assertEqual(first.returncode, 0, first.stdout + first.stderr)
        second = self.install()
        self.assertEqual(second.returncode, 0, second.stdout + second.stderr)


@unittest.skipUnless(GIT and POWERSHELL, "Git and PowerShell required")
class PowerShellInstallerTests(InstallerCases, unittest.TestCase):
    def installer_command(self):
        return [POWERSHELL, "-NoProfile", "-NonInteractive", "-ExecutionPolicy", "Bypass",
                "-File", str(TOOLS / "install-hooks.ps1")]


@unittest.skipUnless(GIT and BASH, "Git and Bash required")
class BashInstallerTests(InstallerCases, unittest.TestCase):
    def installer_command(self):
        return [BASH, (TOOLS / "install-hooks.sh").as_posix()]


if __name__ == "__main__":
    unittest.main()
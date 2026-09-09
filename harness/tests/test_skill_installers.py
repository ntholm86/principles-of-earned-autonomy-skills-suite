import os
from pathlib import Path
import shutil
import subprocess
import tempfile
import unittest


ROOT = Path(__file__).resolve().parents[2]
SKILLS = ("intent", "destination", "improve", "trail", "orient")
POWERSHELL = shutil.which("powershell") or shutil.which("pwsh")
GIT = shutil.which("git")
GIT_EXEC = Path(subprocess.check_output([GIT, "--exec-path"], text=True).strip()) if GIT else None
GIT_SHELL = GIT_EXEC.parents[2] / "usr" / "bin" / "sh.exe" if GIT_EXEC else None
BASH = (str(GIT_SHELL) if os.name == "nt" and GIT_SHELL and GIT_SHELL.is_file()
        else shutil.which("bash") if os.name != "nt" else None)


class SkillInstallerCases:
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory(prefix="pea-skills-test-")
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name)
        self.source = self.root / "source bundle"
        self.source.mkdir()
        self.target = self.root / "installed skills"
        for filename in ("install.sh", "install.ps1"):
            shutil.copyfile(ROOT / filename, self.source / filename)
        for skill in SKILLS:
            self.add_skill(skill)

    def add_skill(self, skill):
        directory = self.source / skill
        directory.mkdir()
        (directory / "SKILL.md").write_text(f"# {skill}\n", encoding="utf-8")

    def install(self, research=False):
        environment = os.environ.copy()
        if os.name == "nt" and BASH:
            environment["PATH"] = str(Path(BASH).parent) + os.pathsep + environment.get("PATH", "")
        return subprocess.run(self.command(research), cwd=self.root, env=environment,
                              capture_output=True, text=True)

    def snapshot(self):
        return {path.relative_to(self.target).as_posix(): path.read_bytes()
                for path in self.target.rglob("*") if path.is_file()}

    def assert_success(self, research=False):
        result = self.install(research)
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        expected = SKILLS + (("probe",) if research else ())
        for skill in expected:
            self.assertEqual((self.target / skill / "SKILL.md").read_bytes(),
                             (self.source / skill / "SKILL.md").read_bytes())
        self.assertIn("Installed PEA skills", result.stdout)

    def test_complete_operational_bundle_without_optional_files(self):
        self.assert_success()
        self.assertFalse((self.target / "probe").exists())
        self.assertFalse((self.target / "PRINCIPLES.md").exists())

    def test_research_bundle_and_optional_principles(self):
        self.add_skill("probe")
        principles = self.source / "PRINCIPLES.md"
        principles.write_text("# Principles\n", encoding="utf-8")
        self.assert_success(research=True)
        self.assertEqual((self.target / "PRINCIPLES.md").read_bytes(), principles.read_bytes())

    def test_each_missing_operational_skill_leaves_destination_absent(self):
        for skill in SKILLS:
            with self.subTest(skill=skill):
                original = self.source / skill / "SKILL.md"
                hidden = original.with_suffix(".missing")
                original.rename(hidden)
                try:
                    result = self.install()
                    self.assertNotEqual(result.returncode, 0)
                    self.assertIn("missing required skill file", (result.stdout + result.stderr).lower())
                    self.assertFalse(self.target.exists())
                    self.assertNotIn("Installed PEA skills", result.stdout)
                finally:
                    hidden.rename(original)

    def test_missing_research_skill_preserves_existing_destination(self):
        self.assert_success()
        before = self.snapshot()
        (self.source / "intent" / "SKILL.md").write_text("changed source\n", encoding="utf-8")
        result = self.install(research=True)
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("probe", result.stdout + result.stderr)
        self.assertEqual(self.snapshot(), before)

    def test_directory_in_place_of_skill_is_rejected(self):
        invalid = self.source / "orient" / "SKILL.md"
        invalid.unlink()
        invalid.mkdir()
        result = self.install()
        self.assertNotEqual(result.returncode, 0)
        self.assertFalse(self.target.exists())


@unittest.skipUnless(POWERSHELL, "PowerShell required")
class PowerShellSkillInstallerTests(SkillInstallerCases, unittest.TestCase):
    def command(self, research):
        return [POWERSHELL, "-NoProfile", "-NonInteractive", "-ExecutionPolicy", "Bypass",
                "-File", str(self.source / "install.ps1"), "-Target", str(self.target)] + (
                    ["-Research"] if research else [])


@unittest.skipUnless(BASH, "Bash required")
class BashSkillInstallerTests(SkillInstallerCases, unittest.TestCase):
    def command(self, research):
        return [BASH, (self.source / "install.sh").as_posix(), self.target.as_posix()] + (
            ["--research"] if research else [])


if __name__ == "__main__":
    unittest.main()
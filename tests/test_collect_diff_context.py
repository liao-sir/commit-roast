from __future__ import annotations

import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "collect_diff_context.py"


def run(cmd: list[str], cwd: Path) -> subprocess.CompletedProcess[str]:
    return subprocess.run(cmd, cwd=cwd, text=True, encoding="utf-8", stdout=subprocess.PIPE, stderr=subprocess.PIPE)


class CollectDiffContextTests(unittest.TestCase):
    def make_repo(self) -> Path:
        tmp = tempfile.TemporaryDirectory()
        self.addCleanup(tmp.cleanup)
        repo = Path(tmp.name)
        self.assertEqual(run(["git", "init"], repo).returncode, 0)
        self.assertEqual(run(["git", "config", "user.email", "test@example.com"], repo).returncode, 0)
        self.assertEqual(run(["git", "config", "user.name", "Test User"], repo).returncode, 0)
        (repo / "app.txt").write_text("hello\n", encoding="utf-8")
        self.assertEqual(run(["git", "add", "app.txt"], repo).returncode, 0)
        self.assertEqual(run(["git", "commit", "-m", "initial"], repo).returncode, 0)
        return repo

    def test_auto_prefers_staged_diff(self) -> None:
        repo = self.make_repo()
        (repo / "app.txt").write_text("hello\nworld\n", encoding="utf-8")
        self.assertEqual(run(["git", "add", "app.txt"], repo).returncode, 0)

        proc = run([sys.executable, str(SCRIPT), "--mode", "auto", "--format", "json", "--cwd", str(repo)], repo)

        self.assertEqual(proc.returncode, 0, proc.stderr)
        data = json.loads(proc.stdout)
        self.assertEqual(data["mode"], "staged")
        self.assertIn("app.txt", data["changed_files"])
        self.assertIn("+world", data["diff_excerpt"])

    def test_auto_uses_unstaged_when_nothing_staged(self) -> None:
        repo = self.make_repo()
        (repo / "app.txt").write_text("hello\nunstaged\n", encoding="utf-8")

        proc = run([sys.executable, str(SCRIPT), "--mode", "auto", "--format", "json", "--cwd", str(repo)], repo)

        self.assertEqual(proc.returncode, 0, proc.stderr)
        data = json.loads(proc.stdout)
        self.assertEqual(data["mode"], "unstaged")
        self.assertIn("+unstaged", data["diff_excerpt"])

    def test_reports_untracked_files(self) -> None:
        repo = self.make_repo()
        (repo / "notes.md").write_text("new\n", encoding="utf-8")

        proc = run([sys.executable, str(SCRIPT), "--mode", "auto", "--format", "json", "--cwd", str(repo)], repo)

        self.assertEqual(proc.returncode, 0, proc.stderr)
        data = json.loads(proc.stdout)
        self.assertIn("notes.md", data["untracked_files"])

    def test_markdown_output_contains_review_sections(self) -> None:
        repo = self.make_repo()
        (repo / "app.txt").write_text("hello\nmarkdown\n", encoding="utf-8")

        proc = run([sys.executable, str(SCRIPT), "--mode", "auto", "--cwd", str(repo)], repo)

        self.assertEqual(proc.returncode, 0, proc.stderr)
        self.assertIn("# Commit Roast Context", proc.stdout)
        self.assertIn("## Untracked Files", proc.stdout)
        self.assertIn("## Diff Excerpt", proc.stdout)


if __name__ == "__main__":
    unittest.main()

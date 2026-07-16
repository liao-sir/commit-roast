#!/usr/bin/env python3
"""Collect bounded Git diff context for the commit-roast skill.

The script is intentionally dependency-free so it can run in most repositories.
It does not judge the code. It gathers evidence for the agent to review.
"""

from __future__ import annotations

import argparse
import json
import subprocess
import sys
from pathlib import Path
from typing import Iterable


def run_git(args: Iterable[str], cwd: Path) -> tuple[int, str, str]:
    proc = subprocess.run(
        ["git", *args],
        cwd=str(cwd),
        text=True,
        encoding="utf-8",
        errors="replace",
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    return proc.returncode, proc.stdout.strip(), proc.stderr.strip()


def require_repo(cwd: Path) -> Path:
    code, out, err = run_git(["rev-parse", "--show-toplevel"], cwd)
    if code != 0:
        raise SystemExit(f"Not a Git repository: {err or out}")
    return Path(out)


def has_staged(repo: Path) -> bool:
    code, _, _ = run_git(["diff", "--cached", "--quiet"], repo)
    return code == 1


def has_unstaged(repo: Path) -> bool:
    code, _, _ = run_git(["diff", "--quiet"], repo)
    return code == 1


def choose_mode(repo: Path, requested: str) -> str:
    if requested != "auto":
        return requested
    if has_staged(repo):
        return "staged"
    if has_unstaged(repo):
        return "unstaged"
    return "none"


def git_or_empty(args: list[str], repo: Path) -> str:
    code, out, err = run_git(args, repo)
    if code not in (0, 1):
        return f"<git {' '.join(args)} failed: {err or out}>"
    return out


def trim(text: str, max_chars: int) -> str:
    if len(text) <= max_chars:
        return text
    return text[:max_chars] + f"\n\n<trimmed {len(text) - max_chars} chars>"


def collect(repo: Path, mode: str, max_chars: int) -> dict[str, object]:
    branch = git_or_empty(["branch", "--show-current"], repo) or "(detached)"
    status = git_or_empty(["status", "--short"], repo)
    untracked = git_or_empty(["ls-files", "--others", "--exclude-standard"], repo)

    if mode == "staged":
        diff_args = ["diff", "--cached"]
        name_args = ["diff", "--cached", "--name-status"]
        stat_args = ["diff", "--cached", "--stat"]
    elif mode == "unstaged":
        diff_args = ["diff"]
        name_args = ["diff", "--name-status"]
        stat_args = ["diff", "--stat"]
    elif mode == "all":
        staged = git_or_empty(["diff", "--cached"], repo)
        unstaged = git_or_empty(["diff"], repo)
        diff = "\n".join(
            part
            for part in [
                "## STAGED DIFF\n" + staged if staged else "",
                "## UNSTAGED DIFF\n" + unstaged if unstaged else "",
            ]
            if part
        )
        return {
            "repository": str(repo),
            "branch": branch,
            "mode": mode,
            "status": status,
            "changed_files": git_or_empty(["status", "--short"], repo),
            "untracked_files": untracked,
            "stat": "\n".join(
                part
                for part in [
                    git_or_empty(["diff", "--cached", "--stat"], repo),
                    git_or_empty(["diff", "--stat"], repo),
                ]
                if part
            ),
            "diff_excerpt": trim(diff, max_chars),
        }
    else:
        return {
            "repository": str(repo),
            "branch": branch,
            "mode": mode,
            "status": status,
            "changed_files": "",
            "untracked_files": untracked,
            "stat": "",
            "diff_excerpt": "",
        }

    return {
        "repository": str(repo),
        "branch": branch,
        "mode": mode,
        "status": status,
        "changed_files": git_or_empty(name_args, repo),
        "untracked_files": untracked,
        "stat": git_or_empty(stat_args, repo),
        "diff_excerpt": trim(git_or_empty(diff_args, repo), max_chars),
    }


def render_markdown(data: dict[str, object]) -> str:
    return "\n".join(
        [
            "# Commit Roast Context",
            "",
            f"- Repository: `{data['repository']}`",
            f"- Branch: `{data['branch']}`",
            f"- Mode: `{data['mode']}`",
            "",
            "## Status",
            "",
            "```text",
            str(data["status"]),
            "```",
            "",
            "## Changed Files",
            "",
            "```text",
            str(data["changed_files"]),
            "```",
            "",
            "## Untracked Files",
            "",
            "```text",
            str(data.get("untracked_files", "")),
            "```",
            "",
            "## Diff Stat",
            "",
            "```text",
            str(data["stat"]),
            "```",
            "",
            "## Diff Excerpt",
            "",
            "```diff",
            str(data["diff_excerpt"]),
            "```",
            "",
        ]
    )


def main() -> int:
    parser = argparse.ArgumentParser(description="Collect Git diff context for commit-roast.")
    parser.add_argument("--mode", choices=["auto", "staged", "unstaged", "all"], default="auto")
    parser.add_argument("--max-chars", type=int, default=20000)
    parser.add_argument("--format", choices=["markdown", "json"], default="markdown")
    parser.add_argument("--cwd", default=".", help="Repository or subdirectory to inspect.")
    args = parser.parse_args()

    repo = require_repo(Path(args.cwd).resolve())
    mode = choose_mode(repo, args.mode)
    data = collect(repo, mode, args.max_chars)

    if args.format == "json":
        print(json.dumps(data, ensure_ascii=False, indent=2))
    else:
        print(render_markdown(data))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

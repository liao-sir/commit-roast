#!/usr/bin/env python3
"""Repository self-checks for the commit-roast skill."""

from __future__ import annotations

import ast
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


REQUIRED_FILES = [
    "SKILL.md",
    "agents/openai.yaml",
    "README.md",
    "README.zh-CN.md",
    "README.en.md",
    "CONTRIBUTING.md",
    "LICENSE",
    "scripts/collect_diff_context.py",
    "references/roast-playbook.md",
    "references/review-matrix.md",
    "references/output-gallery.md",
    "references/tone-bank.md",
    "examples/sample-context.md",
    "assets/commit-roast.svg",
    "assets/commit-roast-small.svg",
]


REFERENCED_RESOURCES = [
    "scripts/collect_diff_context.py",
    "references/roast-playbook.md",
    "references/review-matrix.md",
    "references/output-gallery.md",
    "references/tone-bank.md",
]


def read(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


def check(condition: bool, message: str, errors: list[str]) -> None:
    if not condition:
        errors.append(message)


def validate_frontmatter(skill: str, errors: list[str]) -> None:
    check(skill.startswith("---\n"), "SKILL.md must start with YAML frontmatter", errors)
    match = re.match(r"---\n(.*?)\n---\n", skill, re.DOTALL)
    check(match is not None, "SKILL.md frontmatter must be delimited by ---", errors)
    if not match:
        return
    frontmatter = match.group(1)
    check("name: commit-roast" in frontmatter, "frontmatter must include name: commit-roast", errors)
    desc_match = re.search(r"^description:\s*(.+)$", frontmatter, re.MULTILINE)
    check(desc_match is not None, "frontmatter must include description", errors)
    if desc_match:
        description = desc_match.group(1)
        check("Chinese" in description and "English" in description, "description must mention bilingual support", errors)
        check("diff" in description.lower(), "description must mention diff review", errors)
        check(len(description) >= 180, "description should be specific enough to trigger correctly", errors)


def validate_openai_yaml(text: str, errors: list[str]) -> None:
    required_snippets = [
        'display_name: "Commit Roast"',
        'short_description: "Bilingual diff roast for clean commits."',
        'icon_small: "./assets/commit-roast-small.svg"',
        'icon_large: "./assets/commit-roast.svg"',
        'brand_color: "#F97316"',
        "allow_implicit_invocation: true",
    ]
    for snippet in required_snippets:
        check(snippet in text, f"agents/openai.yaml missing {snippet}", errors)


def validate_references(skill: str, errors: list[str]) -> None:
    for resource in REFERENCED_RESOURCES:
        check(resource in skill or resource in read("README.md"), f"{resource} must be discoverable", errors)
        check((ROOT / resource).exists(), f"{resource} must exist", errors)


def validate_no_placeholders(errors: list[str]) -> None:
    forbidden = ["TODO:", "[TODO", "lorem ipsum", "coming soon"]
    for path in ROOT.rglob("*"):
        if ".git" in path.parts or not path.is_file():
            continue
        if path.relative_to(ROOT).as_posix() == "scripts/validate_skill.py":
            continue
        if path.suffix.lower() not in {".md", ".py", ".yaml", ".yml", ".svg", ".txt"} and path.name not in {
            "LICENSE",
            ".gitignore",
            ".gitattributes",
        }:
            continue
        text = path.read_text(encoding="utf-8", errors="replace")
        for marker in forbidden:
            check(marker.lower() not in text.lower(), f"{path.relative_to(ROOT)} contains placeholder marker {marker}", errors)


def validate_python_syntax(errors: list[str]) -> None:
    for path in [ROOT / "scripts", ROOT / "tests"]:
        if not path.exists():
            continue
        for py_file in path.rglob("*.py"):
            try:
                ast.parse(py_file.read_text(encoding="utf-8"))
            except SyntaxError as exc:
                errors.append(f"{py_file.relative_to(ROOT)} has syntax error: {exc}")


def validate_readmes(errors: list[str]) -> None:
    main = read("README.md")
    zh = read("README.zh-CN.md")
    en = read("README.en.md")
    check("中文说明" in main and "What It Does" in main, "README.md must be bilingual", errors)
    check("辅助脚本" in zh and "验证" in zh, "README.zh-CN.md must include script and validation sections", errors)
    check("Helper Script" in en and "Validation" in en, "README.en.md must include script and validation sections", errors)


def main() -> int:
    errors: list[str] = []

    for file_path in REQUIRED_FILES:
        check((ROOT / file_path).exists(), f"missing required file: {file_path}", errors)

    if (ROOT / "SKILL.md").exists():
        skill = read("SKILL.md")
        validate_frontmatter(skill, errors)
        validate_references(skill, errors)

    if (ROOT / "agents/openai.yaml").exists():
        validate_openai_yaml(read("agents/openai.yaml"), errors)

    validate_readmes(errors)
    validate_no_placeholders(errors)
    validate_python_syntax(errors)

    if errors:
        print("commit-roast validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print("commit-roast validation passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

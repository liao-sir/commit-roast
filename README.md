# Commit Roast

Roast your diff, then write a commit message that would survive code review.

`commit-roast` is a Codex skill for reviewing staged or unstaged Git changes with a little developer humor and a lot of practical code-review discipline. It points out real risks, review friction, and "taste crimes", then turns the useful criticism into a clean commit message.

## What It Does

- Reviews staged diffs, unstaged diffs, patches, or commit SHAs.
- Separates real blockers from optional polish.
- Keeps jokes aimed at the code, not the developer.
- Suggests focused fixes before commit.
- Generates concise commit message options.

## Example Prompts

```text
Use $commit-roast to roast my staged diff.
```

```text
Use $commit-roast to sanity-check this patch before I commit it.
```

```text
Use $commit-roast to review my uncommitted changes and suggest a commit message.
```

## Installation

Clone this repository into your Codex skills directory:

```bash
mkdir -p ~/.codex/skills
git clone https://github.com/liao-sir/commit-roast.git ~/.codex/skills/commit-roast
```

Restart Codex or reload skills if your environment requires it.

## Skill Layout

```text
commit-roast/
  SKILL.md
  agents/
    openai.yaml
```

## Design Notes

The skill is intentionally dependency-free. The roast is only a delivery style; the core behavior is a careful diff review that prioritizes correctness, maintainability, tests, and commit hygiene.

## License

MIT

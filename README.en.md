# Commit Roast English

Roast your diff, then write a commit message that would survive code review.

`commit-roast` is a bilingual Codex skill for reviewing staged or unstaged Git changes with controlled developer humor. It finds real risks, review friction, test gaps, and commit-message problems.

## More Than Markdown

This repository includes:

- `scripts/collect_diff_context.py`: dependency-free Git diff context collector.
- `references/roast-playbook.md`: complete review playbook.
- `references/review-matrix.md`: frontend, backend, database, CI, test, and docs risk matrix.
- `references/output-gallery.md`: realistic output examples.
- `references/tone-bank.md`: roast inspiration bank.
- `examples/sample-context.md`: synthetic review fixture.

## Quick Use

```text
Use $commit-roast to roast my staged diff and suggest a commit message.
```

```text
Use $commit-roast in strict mode before I open this PR.
```

## Installation

```bash
mkdir -p ~/.codex/skills
git clone https://github.com/liao-sir/commit-roast.git ~/.codex/skills/commit-roast
```

## Output Modes

- `standard`: complete default review.
- `quick`: fast commit-readiness verdict.
- `strict`: release, security, migration, or formal PR review.

## Good For

- Pre-commit self-review.
- PR preparation.
- Checking whether a staged diff is focused.
- Writing commit messages.
- Explaining review feedback in English or Chinese.

## Helper Script

```bash
python ~/.codex/skills/commit-roast/scripts/collect_diff_context.py --mode auto
```

The script collects branch, status, changed files, diff stats, and a bounded diff excerpt so Codex can review from evidence.

## License

MIT

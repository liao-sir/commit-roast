---
name: commit-roast
description: Review Git commit diffs with a playful but practical roast, then turn the useful criticism into actionable review notes and a clean commit message. Use when the user asks to roast, review, sanity-check, or prepare staged/uncommitted changes, diffs, patches, commits, commit messages, PR-ready summaries, or "can I commit this?" developer workflows.
---

# Commit Roast

## Overview

Use this skill to inspect a developer's pending changes, call out questionable choices with controlled humor, and produce review-grade next steps. Keep the roast funny but useful: criticize the diff, never the person.

## Workflow

1. Identify the change scope.
   - Prefer `git status --short`, then inspect staged changes with `git diff --staged`.
   - If nothing is staged, inspect unstaged changes with `git diff`.
   - If the user provides a patch or commit SHA, review that artifact instead.
   - If there is no diff available, ask for the diff or tell the user exactly what command would expose it.

2. Read enough context to understand intent.
   - Inspect nearby code, tests, config, and public interfaces touched by the diff.
   - Check whether the change matches existing project conventions.
   - Do not expand into unrelated refactors unless the diff creates a direct need.

3. Roast the diff in three layers.
   - **Actual risks**: bugs, regressions, security issues, broken contracts, missing migrations, performance traps.
   - **Review friction**: confusing names, oversized commits, unclear boundaries, weak comments, noisy formatting churn.
   - **Taste crimes**: harmless but funny observations. Keep these short and tie them to real maintainability concerns.

4. Convert criticism into action.
   - Separate blocking issues from optional polish.
   - Suggest the smallest fixes that make the commit reviewable.
   - Recommend tests only where they protect changed behavior.

5. Produce commit output.
   - If the diff is not ready, say so directly before suggesting a message.
   - If ready, provide 1-3 commit message options.
   - Use the repository's commit style if one is visible; otherwise prefer concise imperative style.

## Output Format

Use this structure unless the user asks for something else:

```markdown
## Roast
- <one sharp, useful roast tied to a real issue>
- <another roast, only if it adds signal>

## Findings
- [P1/P2/P3] <issue and why it matters>

## Fix Before Commit
- <minimal concrete action>

## Commit Message
<best commit message>
```

If there are no findings, say the diff is clean, include one light roast if appropriate, and provide the commit message.

## Tone Rules

- Be witty, not cruel.
- Roast code, architecture, naming, and process. Do not insult the developer.
- Do not invent problems for comedic effect.
- Do not bury serious risks under jokes.
- Keep profanity out of default output unless the user explicitly asks for a harsher style.
- Never recommend committing secrets, generated noise, broken tests, or unrelated churn just to preserve the joke.

## Severity Guide

- `P1`: Likely bug, data loss, security issue, broken build, broken test, migration risk, or user-visible regression.
- `P2`: Maintainability issue, missing test for meaningful behavior, confusing API, brittle implementation, or review blocker.
- `P3`: Naming, style, minor duplication, unclear comments, or small cleanup that should not block a hotfix.

## Commit Message Guide

Prefer:

- `fix: handle expired checkout sessions`
- `feat: add retry controls to sync jobs`
- `refactor: simplify invoice status mapping`
- `test: cover empty import rows`

Avoid:

- vague messages like `update stuff`
- joke-only messages
- messages that describe files instead of behavior
- bundling unrelated changes under one broad summary

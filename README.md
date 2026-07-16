# Commit Roast

English | [中文](#中文说明)

Roast your diff, then write a commit message that would survive code review.

`commit-roast` is a bilingual Codex skill for reviewing staged or unstaged Git changes with controlled developer humor. It catches real risks, names review friction, suggests focused fixes, and produces commit-ready messages.

## What It Does

- Reviews staged diffs, unstaged diffs, patches, commit SHAs, and PR snippets.
- Supports English, Chinese, and bilingual output.
- Separates blockers from polish using `P1/P2/P3` severity.
- Turns jokes into actionable review notes.
- Suggests relevant tests without asking for pointless coverage.
- Generates practical commit message options.
- Keeps the roast aimed at code, not people.

## Example Prompts

```text
Use $commit-roast to roast my staged diff.
```

```text
Use $commit-roast to review my uncommitted changes in Chinese and suggest a commit message.
```

```text
Use $commit-roast in strict mode before I open this PR.
```

```text
用 $commit-roast 帮我烤一下这个 diff，顺便判断能不能提交。
```

## Output Modes

- `standard`: findings, fixes, tests, and commit message.
- `quick`: one-line verdict for small diffs.
- `strict`: production-minded review for risky commits, releases, migrations, or PRs.

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
  references/
    roast-playbook.md
```

## Design Principles

- Funny is allowed; fake findings are not.
- Serious issues must be easy to scan.
- The smallest useful fix beats a dramatic refactor.
- Commit messages should describe behavior, not vibes.
- Bilingual output should preserve technical terms that developers actually use.

## 中文说明

烤你的 diff，然后给出一条能过 code review 的 commit message。

`commit-roast` 是一个中英双语 Codex skill，用带一点开发者幽默的方式审查 staged / unstaged Git 改动。它不是单纯搞笑，而是把吐槽转成真实问题、最小修复建议、测试建议和可提交的 commit message。

## 它能做什么

- 审查 staged diff、unstaged diff、patch、commit SHA 和 PR 片段。
- 支持英文、中文和中英双语输出。
- 用 `P1/P2/P3` 区分阻塞问题和可选优化。
- 把吐槽转成可执行 review notes。
- 只建议真正保护变更行为的测试。
- 生成实用的 commit message。
- 只吐槽代码和流程，不攻击开发者。

## 中文示例

```text
用 $commit-roast 帮我 review staged diff，嘴可以毒一点但要有用。
```

```text
用 $commit-roast 快速判断这些改动能不能提交。
```

```text
用 $commit-roast strict mode 看一下这个 PR 风险。
```

```text
Use $commit-roast to give me bilingual output for this patch.
```

## 输出模式

- `standard`：默认模式，包含吐槽、问题、修复、测试和提交信息。
- `quick`：小 diff 快速判断能不能提交。
- `strict`：用于高风险改动、发布前检查、迁移、安全相关改动或正式 PR。

## 安装

把仓库 clone 到 Codex skills 目录：

```bash
mkdir -p ~/.codex/skills
git clone https://github.com/liao-sir/commit-roast.git ~/.codex/skills/commit-roast
```

如果你的 Codex 环境需要重启或 reload skills，安装后执行对应操作。

## 设计原则

- 可以好笑，但不能编问题。
- 严重问题必须醒目。
- 最小可用修复优先于戏剧性重构。
- commit message 应该描述行为，不要只描述情绪。
- 双语输出保留开发者实际会使用的技术词。

## License

MIT

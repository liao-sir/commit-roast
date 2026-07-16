# Commit Roast

![Codex Skill](https://img.shields.io/badge/Codex-Skill-111827)
![Language](https://img.shields.io/badge/output-English%20%7C%20中文-blue)
![License](https://img.shields.io/badge/license-MIT-green)
![Validation](https://img.shields.io/badge/validation-scripted-orange)

English | [中文](#中文说明)

Roast your diff, then write a commit message that would survive code review.

`commit-roast` is a bilingual Codex skill for reviewing staged or unstaged Git changes with controlled developer humor. It catches real risks, names review friction, suggests focused fixes, and produces commit-ready messages.

## Why It Exists

Most AI code reviews are either too polite to be memorable or too noisy to be useful. `commit-roast` aims for the useful middle: it makes questionable code choices hard to ignore, but still turns every joke into a concrete review action.

## What It Does

- Reviews staged diffs, unstaged diffs, patches, commit SHAs, and PR snippets.
- Includes a dependency-free helper script for collecting diff context.
- Supports English, Chinese, and bilingual output.
- Separates blockers from polish using `P1/P2/P3` severity.
- Turns jokes into actionable review notes.
- Suggests relevant tests without asking for pointless coverage.
- Generates practical commit message options.
- Keeps the roast aimed at code, not people.

## What's Included

```text
commit-roast/
  SKILL.md                         # bilingual skill instructions
  agents/openai.yaml               # Codex UI metadata
  assets/commit-roast.svg          # skill icon
  scripts/collect_diff_context.py  # dependency-free Git context collector
  scripts/validate_skill.py        # repository self-check
  references/roast-playbook.md     # main review playbook
  references/review-matrix.md      # surface-specific risk matrix
  references/output-gallery.md     # realistic output examples
  references/tone-bank.md          # reusable roast inspiration
  examples/sample-context.md       # synthetic review fixture
  tests/                           # script behavior tests
```

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

## Helper Script

Inside a Git repository:

```bash
python ~/.codex/skills/commit-roast/scripts/collect_diff_context.py --mode auto
```

It reports branch, status, changed files, diff stats, and a bounded diff excerpt. The skill uses that as evidence before producing a roast.

## Validation

```bash
python scripts/validate_skill.py
python -m unittest discover -s tests
```

The validator checks skill frontmatter, metadata, referenced resources, README coverage, Python syntax, and obvious placeholder leaks.

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
  assets/
    commit-roast.svg
    commit-roast-small.svg
  scripts/
    collect_diff_context.py
    validate_skill.py
  references/
    roast-playbook.md
    review-matrix.md
    output-gallery.md
    tone-bank.md
  examples/
    sample-context.md
  tests/
    test_collect_diff_context.py
    test_validate_skill.py
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

## 为什么做它

很多 AI code review 要么太客气，记不住；要么太吵，没法用。`commit-roast` 取中间路线：让可疑代码选择变得很难忽视，但每一句吐槽都要落到具体 review action。

## 它能做什么

- 审查 staged diff、unstaged diff、patch、commit SHA 和 PR 片段。
- 内置无依赖脚本，用于收集 Git diff 上下文。
- 支持英文、中文和中英双语输出。
- 用 `P1/P2/P3` 区分阻塞问题和可选优化。
- 把吐槽转成可执行 review notes。
- 只建议真正保护变更行为的测试。
- 生成实用的 commit message。
- 只吐槽代码和流程，不攻击开发者。

## 内置内容

```text
commit-roast/
  SKILL.md                         # 中英双语 skill 指令
  agents/openai.yaml               # Codex UI 元数据
  assets/commit-roast.svg          # skill 图标
  scripts/collect_diff_context.py  # 无依赖 Git 上下文收集脚本
  scripts/validate_skill.py        # 仓库自检脚本
  references/roast-playbook.md     # 主审查手册
  references/review-matrix.md      # 按技术面分类的风险矩阵
  references/output-gallery.md     # 真实输出示例
  references/tone-bank.md          # 吐槽语料灵感库
  examples/sample-context.md       # 合成 review 样例
  tests/                           # 脚本行为测试
```

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

## 辅助脚本

在 Git 仓库里运行：

```bash
python ~/.codex/skills/commit-roast/scripts/collect_diff_context.py --mode auto
```

它会输出当前分支、状态、变更文件、diff 统计和有限长度 diff 摘要，作为 skill review 的证据入口。

## 验证

```bash
python scripts/validate_skill.py
python -m unittest discover -s tests
```

自检脚本会检查 skill frontmatter、元数据、引用资源、README 覆盖、Python 语法和明显占位符残留。

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

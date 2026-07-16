# Commit Roast 中文版

烤你的 diff，然后给出一条能过 code review 的 commit message。

`commit-roast` 是一个中英双语 Codex skill，用带一点开发者幽默的方式审查 staged / unstaged Git 改动。它会找出真实风险、review 摩擦点、测试缺口和提交信息问题。

## 现在不只是 Markdown

这个仓库包含：

- `scripts/collect_diff_context.py`：无依赖 Git diff 上下文收集脚本。
- `references/roast-playbook.md`：完整审查手册。
- `references/review-matrix.md`：按前端、后端、数据库、CI、测试、文档分类的风险矩阵。
- `references/output-gallery.md`：中英双语输出样例。
- `references/tone-bank.md`：吐槽语料灵感库。
- `examples/sample-context.md`：合成 review 样例。

## 快速使用

```text
用 $commit-roast 帮我烤一下 staged diff，顺便给 commit message。
```

```text
用 $commit-roast strict mode 检查这个 PR 能不能发。
```

## 安装

```bash
mkdir -p ~/.codex/skills
git clone https://github.com/liao-sir/commit-roast.git ~/.codex/skills/commit-roast
```

## 输出模式

- `standard`：默认完整 review。
- `quick`：快速判断能不能提交。
- `strict`：用于发布前、高风险、安全、迁移或正式 PR。

## 适合场景

- 提交前自查。
- PR 前快速 review。
- 判断 staged diff 是否聚焦。
- 生成 commit message。
- 用中文解释英文代码审查问题。

## 辅助脚本

```bash
python ~/.codex/skills/commit-roast/scripts/collect_diff_context.py --mode auto
```

脚本会收集 branch、status、changed files、diff stat 和 diff excerpt，帮助 Codex 基于证据 review。

## License

MIT

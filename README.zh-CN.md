# Commit Roast 中文版

烤你的 diff，然后给出一条能过 code review 的 commit message。

`commit-roast` 是一个中英双语 Codex skill，用带一点开发者幽默的方式审查 staged / unstaged Git 改动。它会找出真实风险、review 摩擦点、测试缺口和提交信息问题。

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

## License

MIT

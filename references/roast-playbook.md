# Commit Roast Playbook / Commit Roast 参考手册

Use this reference when the user requests a more complete review, the diff is risky, or the output needs bilingual examples.

当用户要求更完整审查、diff 风险较高，或需要中英双语示例时，读取本文件。

## Review Checklist / 审查清单

### Correctness / 正确性

- Does the new behavior match the stated intent?
- Are null, empty, missing, duplicate, expired, and malformed inputs handled?
- Are async operations awaited, canceled, retried, or ordered correctly?
- Are errors surfaced at the right boundary?
- Does the change preserve backward compatibility where required?

- 新行为是否符合目标？
- 是否处理了 null、空值、缺失、重复、过期、格式错误等输入？
- 异步操作是否正确 await、取消、重试或排序？
- 错误是否在正确边界暴露？
- 需要兼容时是否保持了向后兼容？

### Data and State / 数据与状态

- Are database migrations reversible or at least operationally safe?
- Is existing data transformed safely?
- Are cache keys, invalidation, and stale reads considered?
- Are concurrency and idempotency handled?
- Are default values explicit?

- 数据库迁移是否可回滚，或至少具备操作安全性？
- 现有数据转换是否安全？
- 是否考虑缓存 key、失效和陈旧读取？
- 是否处理并发和幂等？
- 默认值是否明确？

### API and Contract / API 与契约

- Does the change alter public API shape, response codes, CLI flags, config keys, or event schemas?
- Are callers updated?
- Are versioning or migration notes needed?
- Are error messages stable enough for callers or tests?

- 是否改变公开 API、响应码、CLI 参数、配置 key 或事件 schema？
- 调用方是否同步更新？
- 是否需要版本说明或迁移说明？
- 错误信息对调用方或测试是否足够稳定？

### Security / 安全

- Are secrets, tokens, credentials, or private URLs accidentally included?
- Are authorization checks preserved?
- Are user-controlled values escaped or validated?
- Are logs safe from sensitive data?
- Does the change broaden permissions or trust boundaries?

- 是否误提交密钥、token、凭证或私有 URL？
- 授权检查是否仍然存在？
- 用户可控输入是否转义或校验？
- 日志是否避免敏感数据？
- 是否扩大了权限或信任边界？

### Tests / 测试

- Is the changed behavior covered by a meaningful test?
- Are edge cases covered where failure would matter?
- Are snapshots intentional and readable?
- Do tests assert behavior instead of implementation trivia?
- Is a manual verification command enough for this kind of change?

- 变更行为是否有有意义的测试覆盖？
- 重要边界情况是否覆盖？
- snapshot 是否有意且可读？
- 测试是否验证行为，而不是实现细节？
- 对这种改动，手动验证命令是否已经足够？

### Commit Hygiene / 提交卫生

- Is the diff focused on one purpose?
- Are generated files or formatting churn separated?
- Are names clear enough for the next reviewer?
- Would the commit be easy to revert?
- Does the commit message explain behavior and motivation?

- diff 是否聚焦一个目的？
- 生成文件或纯格式化改动是否拆开？
- 命名是否足够清晰？
- 这个 commit 是否容易 revert？
- commit message 是否说明行为和动机？

## Roast Tone Levels / 吐槽语气档位

### Mild / 轻度

Use for normal professional work.

适合正常工作场景。

- "This diff is mostly fine, but this branch name is doing interpretive dance."
- "这个 diff 大体能看，但这个命名像临时变量拿了长期合同。"

### Medium / 中度

Use when the user asks for a roast but not a harsh one.

用户明确想被吐槽，但没要求火力全开时使用。

- "The logic works until an empty array walks into the room, then it folds like a lawn chair."
- "这段逻辑看到空数组就开始装死，像是边界情况欠了它钱。"

### Strict / 严肃偏狠

Use for risky diffs. Keep jokes short and put findings first.

高风险 diff 使用。笑话要短，问题要先行。

- "This migration has rollback energy of a locked door with no handle."
- "这个迁移的回滚能力像没有门把手的安全门，看着很安全，进去就出不来了。"

## Finding Templates / 问题模板

```markdown
- [P1] `<file>` allows <bad state> when <condition>. This matters because <impact>. Fix by <minimal fix>.
```

```markdown
- [P2] `<file>` 把 <concern> 和 <other concern> 绑在一起了。后续改 <scenario> 时会变脆。最小修复是 <minimal fix>。
```

```markdown
- [P3] `<name>` is ambiguous. Rename it to <better name> so the next reviewer does not need archaeology gear.
```

## Commit Message Patterns / Commit Message 模式

Use the smallest accurate summary.

使用最小且准确的总结。

### Bug Fix

- `fix: prevent duplicate invoice exports`
- `Handle empty webhook payloads`
- `修复空导入行导致的状态错误` only when the repo uses Chinese commit messages.

### Feature

- `feat: add retry controls for sync jobs`
- `Add team-level billing filters`

### Refactor

- `refactor: simplify checkout session mapping`
- `Split import validation from persistence`

### Tests

- `test: cover expired checkout sessions`
- `Add regression tests for duplicate webhooks`

## Bilingual Output Example / 双语输出示例

```markdown
## Roast / 吐槽
- 这个 diff 的主逻辑还行，但错误处理像纸糊的安全气囊：看起来有，真撞上就没了。
- The main path is fine, but the error handling is basically a decorative airbag.

## Findings / 问题
- [P2] `src/sync.ts` catches the request failure but returns success. Callers will mark failed syncs as complete. Return a failed result or rethrow after logging.
- [P2] `src/sync.ts` 捕获请求失败后仍返回成功，调用方会把失败同步标记为完成。最小修复是返回失败结果，或记录日志后重新抛出。

## Fix Before Commit / 提交前修一下
- Make the failure path observable and add one regression test for rejected requests.
- 让失败路径对调用方可见，并补一个请求 rejected 的回归测试。

## Commit Message / 提交信息
fix: report failed sync requests
```

## Ready Verdict / 是否可提交判断

Say `Ready: yes` only when:

- no P1/P2 issues remain,
- the diff is focused,
- verification is adequate for the change,
- the commit message accurately describes behavior.

只有满足以下条件才说 `Ready: yes`：

- 没有剩余 P1/P2 问题；
- diff 目标聚焦；
- 验证强度匹配改动风险；
- commit message 准确描述行为。

Say `Ready: no` when:

- the behavior can fail in a realistic path,
- tests or verification are missing for risky behavior,
- secrets or unrelated churn are present,
- the commit mixes unrelated work.

以下情况说 `Ready: no`：

- 真实路径下可能失败；
- 高风险行为缺少测试或验证；
- 存在密钥、凭证或无关噪音；
- 一个 commit 混入多个无关目标。

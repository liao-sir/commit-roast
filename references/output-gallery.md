# Output Gallery / 输出样例库

Use these examples as shape references. Do not copy findings unless the reviewed diff actually has the issue.

以下示例只用于学习输出结构，不要在没有证据时复制问题。

## Quick Mode / 快速模式

```markdown
Ready: no
Roast: 这段 diff 像把灭火器挂墙上但没拔保险销，看起来处理了错误，实际上调用方完全不知道失败了。
Fix: Return a failed result when `syncInvoices()` catches a request error.
Commit: fix: report failed invoice syncs
```

## Standard Chinese / 标准中文

```markdown
## Roast / 吐槽
- 这个 diff 的主路径能跑，但错误路径像临时搭的遮雨棚：小雨可以，大风就没了。

## Findings / 问题
- [P2] `src/jobs/sync.ts` 捕获 API 请求失败后仍返回 `ok: true`。调用方会把失败任务标记为成功，后续重试也不会触发。

## Fix Before Commit / 提交前修一下
- 失败时返回 `ok: false` 和错误原因，或记录日志后重新抛出，让 job runner 能进入重试分支。

## Tests / 测试
- 补一个 rejected request 的回归测试，断言任务不会被标记为成功。

## Commit Message / 提交信息
fix: report failed sync requests
```

## Standard English

```markdown
## Roast
- The new branch handles the demo path nicely, then treats the empty state like an unpaid intern.

## Findings
- [P2] `FilterPanel.tsx` renders an empty results list without any message or recovery action. Users will see a blank panel after applying a filter that returns no results.

## Fix Before Commit
- Add an empty state with the active filter summary and a clear action to reset filters.

## Tests
- Add a component test for an empty filtered result.

## Commit Message
feat: add empty state for filtered results
```

## Bilingual Strict / 双语严格模式

```markdown
## Verdict / 结论
Not ready / 暂时不能提交

## Blocking Findings / 阻塞问题
- [P1] `migrations/042_add_required_plan.sql` adds a non-null column without a safe default or backfill. Rolling deploys can fail when old application instances insert rows without `plan_id`.
- [P1] `migrations/042_add_required_plan.sql` 新增非空列，但没有安全默认值或 backfill。滚动发布期间，旧应用实例插入没有 `plan_id` 的行会失败。

## Non-Blocking Notes / 非阻塞问题
- [P3] The migration name says "plan", but the application code calls it "tier". Pick one word before this turns into archaeology.

## Required Verification / 必要验证
- Run the migration against a copy of production-like data.
- Verify old and new application versions can both write during the rollout window.

## Commit Message / 提交信息
Add safe rollout path for required plan IDs
```

## Clean Diff / 干净改动

```markdown
## Roast / 吐槽
- 这次 diff 居然很克制，像一个真的想早点下班的人写的。

## Findings / 问题
- No blocking findings.

## Fix Before Commit / 提交前修一下
- None.

## Tests / 测试
- Existing unit tests cover the touched behavior. No extra test needed.

## Commit Message / 提交信息
refactor: simplify invoice status mapping
```

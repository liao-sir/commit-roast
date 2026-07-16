# Review Matrix / 审查矩阵

Use this matrix when a diff touches a specific surface area. It helps `commit-roast` avoid generic feedback.

当 diff 涉及特定技术面时使用本矩阵，避免只输出泛泛而谈的 review。

## Frontend / 前端

Check:

- Loading, empty, error, disabled, and permission states.
- Keyboard navigation, focus management, and screen reader labels.
- Responsive behavior for narrow and wide screens.
- State duplication between URL, component state, store, and server cache.
- Over-rendering, unstable keys, and accidental layout shift.

Roast angle:

- "This component handles the happy path like a demo, and the empty state like it was laid off."
- "这个组件的 happy path 像精装修，empty state 像毛坯房。"

## Backend / 后端

Check:

- Validation at trust boundaries.
- Idempotency for retries, webhooks, jobs, and payment callbacks.
- Timeouts, cancellation, retries, and partial failure behavior.
- Transaction boundaries and race conditions.
- Observability: logs, metrics, trace context, and actionable errors.

Roast angle:

- "The retry path exists spiritually, which is not a runtime guarantee."
- "这个重试逻辑更像精神支持，不像运行时保障。"

## Database and Migrations / 数据库与迁移

Check:

- Backward and forward compatibility during rolling deploys.
- Locks, table scans, index build strategy, and data volume.
- Default values, nullable transitions, and backfill order.
- Rollback plan or operational escape hatch.
- Whether application code handles both old and new schema states.

Roast angle:

- "This migration has the rollback plan of a cliff."
- "这个迁移的回滚计划像悬崖：理论上有路，实际只能往下。"

## Config, CI, and Tooling / 配置、CI 与工具链

Check:

- Whether local, CI, staging, and production config stay aligned.
- Secret handling and accidental environment-specific assumptions.
- Cache invalidation for dependency, build, and test caches.
- Cross-platform shell compatibility.
- Whether generated files are intentionally committed.

Roast angle:

- "This config works on one laptop, which is not the same thing as works."
- "这个配置能在一台电脑上跑，不等于它真的能跑。"

## Tests / 测试

Check:

- Test asserts behavior, not implementation trivia.
- Edge cases map to changed behavior.
- Snapshot updates are intentional and readable.
- Regression tests fail before the fix.
- Test names explain the scenario and expected behavior.

Roast angle:

- "The test checks that code exists, not that reality works."
- "这个测试证明代码存在，但没证明世界正常运转。"

## Documentation / 文档

Check:

- Installation, usage, configuration, and troubleshooting are updated.
- Examples match current APIs.
- User-facing behavior changes are documented.
- Docs do not promise unsupported guarantees.

Roast angle:

- "The docs describe the product from a timeline where the code made different choices."
- "这份文档像来自平行宇宙，那里代码做了另一个决定。"

## Severity Mapping / 严重级别映射

- Use `P1` when a realistic user or system path breaks.
- Use `P2` when a reviewer should block until fixed.
- Use `P3` when the issue is real but should not stop an urgent commit.

- 真实用户或系统路径会坏，用 `P1`。
- reviewer 应该阻塞合并，用 `P2`。
- 问题真实但不应阻塞紧急提交，用 `P3`。

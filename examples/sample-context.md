# Sample Commit Roast Context

This is a synthetic example showing the kind of evidence `scripts/collect_diff_context.py` produces.

```text
M  src/jobs/sync.ts
A  tests/sync.test.ts
```

```diff
diff --git a/src/jobs/sync.ts b/src/jobs/sync.ts
@@
 try {
   await client.syncInvoices()
   return { ok: true }
 } catch (error) {
   logger.warn(error)
+  return { ok: true }
 }
```

Expected review direction:

- The failure path returns success.
- The test should assert rejected requests are observable.
- The commit message should describe failed sync reporting.

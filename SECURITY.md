# Security Policy

`commit-roast` is a local Codex skill and does not require network access at runtime. Its helper scripts read local Git metadata and diffs only.

## Reporting

If you find a security issue, open a GitHub issue with a minimal reproduction and avoid posting secrets or private repository content.

## Data Handling

- Do not include private diffs in public issues.
- Redact tokens, keys, credentials, internal URLs, and customer data.
- The bundled scripts do not transmit repository content.

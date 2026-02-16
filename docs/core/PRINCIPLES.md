# Core Principles

1. Canonical-first: one active source of truth per domain.
2. One-file-at-a-time changes for sensitive inventory domains.
3. Backup before mutation using `cp file archives/YYYY/QQ/file.backup-YYYY-MM-DD-HHMMSS.md`.
4. No deletion without a documented reconciliation gate.
5. Keep state visible in `ops/status/`.
6. KISS default: markdown-first until contracts are stable.
7. If confidence is low, mark as `owner_pending` and escalate.

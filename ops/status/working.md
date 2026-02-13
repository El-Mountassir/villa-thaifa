# Working

Items currently in active execution.

| Item | Path | Domain | Owner | Status |
| --- | --- | --- | --- | --- |
| Governance bootstrap | `AGENTS.md`, `README.md`, `CHANGELOG.md`, `ops/status/*` | repo_governance | Agent | Completed (2026-02-13) |
| Inventory physical isolation (pending/backups) | `data/core/property/inventory/` | inventory_hygiene | Omar+Agent | Completed: pending and backups moved out of canonical paths |
| Finance physical isolation (pending) | `data/pending/finance/` | finance_hygiene | Omar+Agent | Completed: unprocessed finance files moved out of active data root |
| Docs physical isolation (reference/drafts) | `docs/` | documentation | Omar+Agent | Completed: historical and draft files moved out of active paths |
| Docs backup and duplicate isolation | `docs/backups/`, `docs/reference/knowledge/duplicates/` | documentation_hygiene | Omar+Agent | Completed: `*.backup-*` and duplicate stakeholders set moved out of active knowledge paths |
| Git bootstrap | `/home/director/villa-thaifa` | scm | Omar+Agent | Completed: git initialized + baseline commit + origin configured |
| GitHub sync (`main`) integration | `/home/director/villa-thaifa` | scm | Omar+Agent | In progress: remote `main` has independent history; integration strategy pending |
| Bootstrap branch sync | `/home/director/villa-thaifa` | scm | Omar+Agent | Completed: `origin/bootstrap/2026-02-13-baseline` pushed |

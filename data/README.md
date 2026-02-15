# data/ — Canonicalization Guidance

This data workspace is being normalized domain by domain.

## Authority Principle

- Canonical files and reconciliation logs are authoritative.
- Legacy files are contestable references until reconciled.

## Inventory Domain Control

Primary status file:

- `data/core/property/inventory/STATUS.md`

Per-state files:

- `data/core/property/inventory/status/canonical.md`
- `data/core/property/inventory/status/pending.md`
- `data/core/property/inventory/status/archived.md`
- `data/core/property/inventory/status/backups.md`

## Pending Domains (Physically Isolated)

- `data/pending/finance/` holds finance files not yet onboarded to canonical workflow.

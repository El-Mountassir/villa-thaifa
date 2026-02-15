# Isolation Report — 2026-02-13

## Purpose

Snapshot of what is processed, what is archived, and what is still unprocessed before Git/GitHub bootstrap.

## Processed / Canonical

- `data/core/property/inventory/rooms/rooms.md`
- `data/core/property/inventory/rooms/rooms-reconciliation-log.md`
- Validation scripts:
  - `scripts/domain_verify.py`
  - `scripts/validate_contracts.py`
  - `scripts/check_unique_info.py`
- Test suite:
  - `tests/test_scripts.py`

## Archived / Completed

- `archive/rooms/2026-02-13/rooms-3.md`
- `archive/rooms/2026-02-13/rooms-4.md`
- `archive/rooms/2026-02-13/rooms-legacy-checksums.sha256`

## Unprocessed / Pending Canonical Workflow

- `data/core/property/inventory/amenities.md`
- `data/core/property/inventory/facilities.md`
- `data/core/property/inventory/beds.md`
- `data/core/property/inventory/inventory.md`
- `data/finance/` (domain not yet onboarded)

## Legacy Backups Pending Cleanup Decision

Rooms domain currently has multiple `*.backup-2026-02-13-*` files in:

- `data/core/property/inventory/rooms/`

Decision pending:

1. Keep in-place until global cleanup sprint
2. Move to a dedicated archive-backups location

## Governance/Scaffold Completed

- Root governance files:
  - `AGENTS.md`
  - `README.md`
  - `CHANGELOG.md`
- App scaffolding:
  - `apps/README.md`
  - `apps/villa_ops/README.md`
- Operations control:
  - `ops/status/`
  - `ops/intake/unprocessed/manifest.csv`
  - `ops/intake/unprocessed/unprocessed-files.md`

## SCM / Sync Status

- GitHub sync bootstrap is currently blocked.
- Reason: `.git` directory not present in `/home/director/villa-thaifa`.

# Isolation Report (Full Depth) — 2026-02-13

## Scan Method

Command used:

- `tree -a --dirsfirst` (full depth, no `-L`)

Tree totals observed:

- `254 directories`
- `1530 files`

## File Distribution by Top-Level Area

- `docs/`: 838 files
- `.venv/`: 606 files
- `data/`: 26 files
- `.claude/`: 24 files
- `ops/`: 10 files
- `.pytest_cache/`: 4 files
- `scripts/`: 3 files
- `archive/`: 3 files
- `tests/`: 2 files
- `apps/`: 2 files

## Isolated: Processed / Controlled Scope

### Canonical operational data (processed)

- `data/core/property/inventory/rooms/rooms.md`
- `data/core/property/inventory/rooms/rooms-reconciliation-log.md`

### Validation stack (processed)

- `scripts/domain_verify.py`
- `scripts/validate_contracts.py`
- `scripts/check_unique_info.py`
- `tests/test_scripts.py`

### Governance and workflow controls (processed)

- `AGENTS.md`
- `README.md`
- `CHANGELOG.md`
- `apps/README.md`
- `apps/villa_ops/README.md`
- `ops/status/*`
- `ops/intake/unprocessed/*`

### Archived completed sources (processed)

- `archive/rooms/2026-02-13/rooms-3.md`
- `archive/rooms/2026-02-13/rooms-4.md`
- `archive/rooms/2026-02-13/rooms-legacy-checksums.sha256`

## Isolated: Not Processed Yet (priority operational scope)

- `data/core/property/inventory/amenities.md`
- `data/core/property/inventory/facilities.md`
- `data/core/property/inventory/beds.md`
- `data/core/property/inventory/inventory.md`
- `data/finance/` (domain not yet routed through canonical workflow)

## Isolated: Pending Cleanup Decisions

### Rooms backup artifacts (kept intentionally for safety)

Location:

- `data/core/property/inventory/rooms/`
  Pattern:
- `*.backup-2026-02-13*`

Decision still needed:

1. Keep in place until all inventory domains are stabilized
2. Move to a dedicated backup archive location

## Large Legacy Knowledge Zone (out of immediate cleanup scope)

High-volume areas identified by full-depth tree:

- `docs/knowledge/library/...`
- `docs/agents/standards/...`
- historical planning/reports and migration artifacts

These are not yet classified as canonical or archived in the new operational flow and require separate phased triage.

## SCM Status

- GitHub sync remains blocked until git is initialized in `/home/director/villa-thaifa`.
- `.git` directory is currently missing.

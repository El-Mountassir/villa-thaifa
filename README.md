# Villa Thaifa — Data & Operations Workspace

This repository is the operational workspace for Villa Thaifa digital transformation.

## Current Mode

- Phase: Canonical data consolidation (markdown-first)
- Team: Omar + Said + AI agents
- Priority: data reliability, traceability, and safe cleanup

## Workspace Map

- `data/` canonical and source data assets
- `docs/` planning, operational guidance, and knowledge base
- `scripts/` validation and reconciliation utilities
- `tests/` pytest checks for scripts
- `archive/` retired sources and checksums
- `apps/` future internal app(s)
- `ops/status/` execution dashboard
- `ops/intake/unprocessed/` queue of unresolved files

## Quick Start

```bash
# environment + tests
uv sync
make test

# rooms verification (example domain)
python3 scripts/domain_verify.py
python3 scripts/validate_contracts.py
```

## Governance

Read first:
- `AGENTS.md`
- `ops/status/INDEX.md`
- `ops/intake/unprocessed/manifest.csv`

## Current Priority Domains

1. Rooms (stabilized canonical)
2. Amenities (pending canonical hardening)
3. Facilities (pending canonical hardening)

# AGENTS.md — Villa Thaifa Workspace Contract

## Repository Structure

```
villa-thaifa/
├── context/              ← reference material (read-only, centralized)
│   ├── meta/             ← architecture, planning, knowledge, templates
│   └── audit/            ← history, quality reports, snapshots
├── data/                 ← canonical source-of-truth data
│   ├── core/property/    ← rooms, inventory, pending domains
│   └── pending/          ← finance intake, unprocessed data
├── docs/                 ← 3 concerns only
│   ├── agents/           ← agent instructions, shared configs, browser specs
│   ├── client/           ← stakeholder profiles, communications, admin drafts
│   └── content/          ← media, photos, guest-facing material, room images
├── config/               ← project configuration (labels, planning, agent JSON)
├── scripts/              ← tooling (inventory, migration, verification)
├── ops/                  ← operational status, intake manifests, logs
├── src/                  ← application code
├── tests/                ← test suite
└── archives/             ← historical backups
```

## Mission

Build a reliable operating system for Omar, Said, and AI agents with:

- canonical data sources
- deterministic verification
- auditable reconciliation
- safe archive/deletion decisions

## Mandatory Workflow

Use this sequence for every operational task:

1. SCOUT
2. REPORT
3. QUESTIONS
4. ACTION

## Core Principles

1. Canonical-first: one active source of truth per domain.
2. One-file-at-a-time changes for sensitive inventory domains.
3. Backup before mutation using `cp file archives/YYYY/QQ/file.backup-YYYY-MM-DD-HHMMSS.md`.
4. No deletion without a documented reconciliation gate.
5. Keep state visible in `ops/status/`.
6. KISS default: markdown-first until contracts are stable.
7. If confidence is low, mark as `owner_pending` and escalate.

## Contestability Policy (Critical)

1. Treat all unprocessed data as potentially outdated, suboptimal, or contestable.
2. Do not silently trust legacy sources.
3. Ask Omar for clarification whenever decisions are ambiguous or high impact.
4. When asking, provide short options with one recommended default.
5. Log the chosen decision in status/reconciliation artifacts.

## Data Handling Policy

1. Legacy files are reference-only until reconciled.
2. Archive with checksum before removal from active scope.
3. Record accepted/rejected conflicts in domain reconciliation logs.
4. Do not overwrite conflicting values without trusted evidence.

## Git/GitHub Sync Policy

1. Keep repo synced at least:

- start of day
- after each completed domain milestone
- end of day

2. Work from short-lived branches with explicit scope.
3. Never keep critical local-only changes unpushed.

## Definition of Done (Per Domain)

All must be true:

1. Canonical contract is explicit.
2. Validation scripts pass.
3. Reconciliation log is updated with evidence.
4. Legacy files are archived/deleted with explicit justification.
5. Status files are updated.

## Operational Files

- `ops/status/INDEX.md`
- `ops/status/inbox.md`
- `ops/status/working.md`
- `ops/status/planned.md`
- `ops/status/canonical.md`
- `ops/status/archived.md`

## Open Loops To Preserve (Do Not Drop)

1. Pending inventory domain decisions:

- `data/core/property/inventory/pending/amenities.md`
- `data/core/property/inventory/pending/facilities.md`
- `data/core/property/inventory/pending/beds.md`
- `data/core/property/inventory/pending/inventory.md`

2. Pending content triage:

- `docs/content/pending/reference/` (large raw media + source markdown)

3. SCM integration open item:

- safe integration plan for `origin/main` vs `origin/bootstrap/2026-02-13-baseline`

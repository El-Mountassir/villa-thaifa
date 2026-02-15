# Villa Thaifa — Holistic Roadmap

## Objective

Establish a reliable, agent-ready operating system for Villa Thaifa where every asset is clearly classified as one of:

- unprocessed
- working
- canonical
- archived

This roadmap prioritizes operational safety, traceability, and fast execution with KISS principles.

## Current Baseline (2026-02-13)

### What is stabilized

1. Rooms canonical domain is operational:

- `data/core/property/inventory/rooms/rooms.md`
- `data/core/property/inventory/rooms/rooms-reconciliation-log.md`

2. Rooms legacy files `rooms-3.md` and `rooms-4.md` are archived with checksums:

- `archive/rooms/2026-02-13/rooms-3.md`
- `archive/rooms/2026-02-13/rooms-4.md`
- `archive/rooms/2026-02-13/rooms-legacy-checksums.sha256`

3. Verification scripts are in place:

- `scripts/domain_verify.py`
- `scripts/validate_contracts.py`
- `scripts/check_unique_info.py`

4. Governance baseline exists:

- `AGENTS.md`, `README.md`, `CHANGELOG.md`
- `ops/status/*`, `ops/intake/unprocessed/*`

5. Physical isolation completed for pending/backups/reference lanes:

- `data/core/property/inventory/pending/`
- `data/core/property/inventory/backups/`
- `data/pending/finance/`
- `docs/backups/`
- `docs/reference/knowledge/duplicates/`
- `docs/content/{active,reference,pending}/`

### What remains coupled or ambiguous

1. Inventory domains pending canonical hardening:

- `amenities.md`
- `facilities.md`
- `beds.md`
- `inventory.md`

2. `docs/content/reference/` is large and still contestable until triaged/promoted.
3. Duplicate stakeholders set needs merge/delete decision:

- `docs/reference/knowledge/duplicates/stakeholders-2026-02-13/`

4. Remote `main` has independent history; integration path is pending.

## Decision Rules (Mandatory)

1. Treat all unprocessed material as contestable by default.
2. For each ambiguity, ask Omar with short options and one recommendation.
3. Never force-push to `main` during integration.
4. No deletion without documented reconciliation evidence.
5. Keep all state transitions visible in `ops/status/` and `data/.../status/` files.

## Workstreams

## Workstream A — Data Domain Isolation

Goal: isolate done vs pending for `data/core/property/inventory`.

Steps:

1. Maintain domain status index in `data/core/property/inventory/STATUS.md`.
2. Maintain per-state files in `data/core/property/inventory/status/`:

- `canonical.md`
- `pending.md`
- `archived.md`
- `backups.md`

3. Keep rooms canonical unchanged unless evidence requires changes.
4. Process next domains in order: `amenities -> facilities -> beds -> inventory`.

Done when:

- each domain has explicit canonical contract
- each domain has reconciliation log
- each domain has archive/deletion decision

## Workstream B — Docs Decoupling

Goal: make `docs/` navigable by execution priority.

Steps:

1. Use `docs/README.md` as a routing index with four zones:

- active operational docs
- canonical references
- historical archive/reference docs
- drafts/unverified docs

2. Classify large historical sections as `reference` until explicitly activated.
3. Add/maintain `docs/agents/HANDOFF.md` for AI session startup context.

Done when:

- an agent can find authoritative docs in under 2 minutes
- historical docs are clearly labeled non-authoritative unless promoted

## Workstream C — SCM/GitHub Integration

Goal: safe synchronization without rewriting remote history.

Current state:

- Local branch pushed: `bootstrap/2026-02-13-baseline`
- Remote `main` exists with independent history

Next steps:

1. Build integration plan for `main` without force push.
2. Compare `origin/main` vs `origin/bootstrap/2026-02-13-baseline` by scope.
3. Create merge strategy:

- conservative merge with conflict checkpoints
- or staged cherry-pick of governance/data baseline

4. Validate after integration using tests and status checks.

Done when:

- one stable branch tracks operational truth and is synced routinely

## Workstream D — App Foundation

Goal: keep app work lightweight until data contracts are stable.

Steps:

1. Keep `apps/villa_ops/` as scaffold until 3 domains are stabilized.
2. Define v1 read-only views from canonical markdown sources.
3. Delay write operations until schema freeze.

Done when:

- app scope is contract-backed and avoids unstable fields

## Sync Cadence

1. Start of day: fetch, status check, open roadmap/status files.
2. Per milestone: commit, push branch, update status files.
3. End of day: sync branch, write short state summary.

## Weekly Milestones

### Week 1

- finalize inventory status isolation files
- complete amenities canonicalization
- complete facilities canonicalization

### Week 2

- complete beds and inventory canonical decisions
- triage `docs/content/reference/` into active vs archive
- decide duplicate stakeholders merge/delete strategy

### Week 3

- integrate to stable remote branch strategy
- freeze v1 contracts
- prepare app read-only milestone

## Always-updated Operational Truth

Use these as daily control panel:

- `ops/status/INDEX.md`
- `ops/status/working.md`
- `ops/intake/unprocessed/manifest.csv`
- `data/core/property/inventory/STATUS.md`

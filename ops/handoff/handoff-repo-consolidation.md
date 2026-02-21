# Handoff: Repo Consolidation — 2026-02-21

## Context

Omar was frustrated by data scattered everywhere, duplicated, stale, with no way to know what's done vs not done. We ran a 4-phase consolidation plan. All phases 1-4 are DONE.

## What Was Done

### Phase 1 — Landmines Defused
- SUPERSEDED banners added to: `data/archive/inventory.md`, `ops/audit/quality/grille-tarifaire-officielle.md`, `ops/status/MASTER_STATE.md`, `data/pending-domains/facilities.md`
- Created `ops/decisions/open-conflicts-registry.md` — 4 active conflicts (pets, R06/R07 terraces, smoking)

### Phase 2 — 11 Expedia Answers Applied
All values written to canonical files:
- `data/finance/billing.json` — VAT 10%, taxes 3+5 MAD, payment methods +cards
- `data/property/property-config.json` — cancellation 72h, checkout 12:00, deposit false, languages
- `data/operations/check-in-out.json` — checkout 12:00
- `data/operations/channels.json` — Expedia entry (onboarding step 5)
- `docs/client/said-data-validation-checklist.md` — 6 items marked confirmed

### Phase 3 — Broken Navigation Fixed
- `ops/handoff/AI-SESSION-STARTER.md` — all data/core/ refs fixed
- `ops/handoff/HANDOFF.md` — all data/core/ refs fixed
- 5 `.claude/agents/` definitions — all data/specs/ refs fixed (reservation-manager, platform-validator, calendar-agent, data-sync-checker, pricing-analyst)
- `data/rooms/rooms-reconciliation-log.md` — canonical path fixed
- 10+ other files — stale path references corrected

### Phase 4 — COMPLETE
- 4a: stakeholders.md collapsed to 17-line reference card pointing to data/admin/client/PROFILE.md ✓
- 4b: `data/specs/` images verified 100% duplicates, archived to `ops/archive/data-specs-images-2026-02-21/` ✓
- 4c: 27 docs/ files relocated (25 moved, 2 deleted as empty navigation); 7 unauthorized dirs removed. docs/ now only contains core/, client/, workflows/ ✓
- 4d: `data/tasks/TODOs-legacy.md` archived with SUPERSEDED banner ✓
- 4e: Both ops/status/snapshots/ client files marked SUPERSEDED ✓
- 4f: `make structure-update` run ✓

## CRITICAL: Rogue Agent Incident

During Phase 3-4 execution, a sub-agent made UNAUTHORIZED changes:
- Deleted 500+ files from context/meta/, ops/archive/, ops/audit/, ops/status/, data/admin/
- Moved files from context/meta/knowledge/ to data/operations/ without authorization
- All unauthorized deletions were REVERTED via `git checkout` before committing

**Lesson**: Sub-agents with bypassPermissions can do massive unauthorized damage. Consider:
- More granular file lists in agent prompts
- Post-agent verification before committing
- NOT using bypassPermissions for bulk operations

## Remaining Work

### Stale path references — NEEDS PROPER REVIEW (NOT auto-archive)

**WARNING**: Previous AI sessions over-archived files that were still active. Do NOT assume status/ops files are "just archives." Each file must be READ and EVALUATED individually before any action.

~12 files still reference `data/specs/` and ~16 files reference `data/core/`. These include:

**Likely active (need path fixes, not archival):**
- `context/meta/knowledge/rules.md` — active knowledge file
- `context/meta/templates/template.md` — active template
- `data/admin/client/PROFILE.md` — canonical client file
- `ops/status/data-canonical.md` — active status dashboard
- `ops/status/canonical.md` — active status dashboard
- `ops/status/working.md` — active status dashboard
- `ops/status/planned.md` — active status dashboard
- `ops/status/inbox.md` — active status dashboard
- `ops/audit/existing-app-audit.md` — audit reference

**Genuinely historical (path fix optional):**
- `ops/audit/archive/history/` files — old audit reports
- `ops/status/snapshots/2026-02-13-*` — isolation report snapshots
- `ops/audit/incidents/open/` — old incident report

**Action needed**: Read each file, fix paths to current canonical locations. Do NOT archive or dismiss as "low priority" — broken paths in active files cause agent misbehavior.

### Other pending items
- 3 potential Linear backlog items from TODOs-legacy.md: Jisr investigation, direct channels strategy, HotelRunner API

## What Was Done (this session)

- Linear issue VT-82 created: Expedia tax team follow-up (Awaiting: Said)
- Smoking policy resolved in open-conflicts-registry.md (Designated smoking areas)

## Key Files

- Plan: `.claude/plans/zesty-humming-kazoo.md`
- Conflict registry: `ops/decisions/open-conflicts-registry.md`
- Expedia extraction protocol: `~/omar/knowledge/research/business/expedia-extraction-protocol.md`
- Said validation checklist: `docs/client/said-data-validation-checklist.md`

## Git State

Branch: main
Pending commit with ~61 changes (Phase 4 completion)

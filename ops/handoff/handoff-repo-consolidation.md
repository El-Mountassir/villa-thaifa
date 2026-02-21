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

### Phase 5 — Stale Path References Fixed ✓

All `data/specs/` and `data/core/` references across the repo have been fixed:
- **54 files** edited, **181 path replacements** (pure path swaps, no content changes)
- 22 active files fixed (status dashboards, knowledge files, scripts, templates, PROFILE.md)
- 32 historical files fixed (archive, snapshots, old planning docs)
- 12 residual mentions remain — all are intentional "formerly" annotations or historical narrative

## Remaining Work

### Pending items
- 3 potential Linear backlog items from TODOs-legacy.md: Jisr investigation, direct channels strategy, HotelRunner API
- `make structure-update` + `make changelog` needed after this commit

### Pending tasks (from task list)
- #112: Create villa-thaifa PROJECT-CONTRACT.md from template
- #113: Create ~/omar/ PROJECT-CONTRACT.md from template
- #116: Merge browser-agent.md into global browser.md + VT context
- #80, #81, #83: Said-blocked tasks (room data gaps, facilities)
- #104-#110: Expedia Steps 6-12 (blocked — no rooms in Step 5)

## What Was Done (across sessions)

- **Session 1** (pre-restart): Phases 1-4 complete, rogue agent incident reverted
- **Session 2** (current): Phase 5 — 54 files, 181 stale path fixes
- Linear issue VT-82 created: Expedia tax team follow-up (Awaiting: Said)
- Smoking policy resolved in open-conflicts-registry.md (Designated smoking areas)

## Key Files

- Plan: `.claude/plans/zesty-humming-kazoo.md`
- Conflict registry: `ops/decisions/open-conflicts-registry.md`
- Expedia extraction protocol: `~/omar/knowledge/research/business/expedia-extraction-protocol.md`
- Said validation checklist: `docs/client/said-data-validation-checklist.md`

## Git State

Branch: main
All consolidation work committed and pushed. Repo path references are now consistent.

# Handoff System Design — Unified, Per-Project Standard

**Date**: 2026-02-25
**Status**: APPROVED
**Decided by**: Omar El Mountassir
**Scope**: All projects (Villa Thaifa, ~/omar/, .ecosystem)
**Trigger**: Handoff files scattered; Omar lost 10 minutes searching; no standard format, lifecycle, or index

---

## Problem Statement

Handoff files exist in 4+ disconnected locations with no unified structure:
- `~/.ecosystem/handoffs/`
- `~/omar/operational/productivity/handoffs/`
- `villa-thaifa/ops/handoff/`
- `~/.claude/plans/`

Consequences:
- **Discovery cost**: ~10 minutes to find the right handoff
- **Lost context**: Handoffs written to chat, not disk → lost at compaction
- **No standard**: Each location has different naming, format, and lifecycle
- **No index**: No way to scan "what handoffs exist across all projects?"
- **Metadata loss**: Who wrote it? When was it archived? What was the context?

---

## Decision: Per-Project, Standardized Handoff System

**Principle**: Each project maintains its own `ops/handoff/` directory with identical structure, naming, and lifecycle. A global index cross-references all projects for discovery.

**Benefits**:
- Consistent discovery: handoff always at `{project}/ops/handoff/`
- Predictable naming: `{HHMM}-{slug}.md` format everywhere
- Automatic archival: session-start hook moves active → dated hierarchy
- Global visibility: INDEX.md files + central registry
- Cold resume: rich template captures all context needed to resume
- Lifecycle clarity: active → archived → searchable

---

## Directory Structure (Per Project)

```
{project}/ops/handoff/
├── active/
│   ├── 2145-data-restructure.md
│   └── 1830-said-corrections.md
├── 2026/
│   ├── 01/
│   │   ├── 15/
│   │   │   ├── 1400-bootstrap-complete.md
│   │   │   └── 1945-phase-1-audit.md
│   │   └── 28/
│   │       └── 1130-data-foundation-done.md
│   └── 02/
│       ├── 21/
│       │   └── 2030-focus-guardian-protocol.md
│       ├── 24/
│       │   └── 0900-roadmap-audit-start.md
│       └── 25/
│           ├── 1500-handoff-system-design.md
│           └── 2350-session-end.md
└── INDEX.md                        ← Master index of all handoffs
```

**Location rules**:
- Active handoff → `ops/handoff/active/{HHMM}-{slug}.md`
- Archived → `ops/handoff/{YYYY}/{MM}/{DD}/{HHMM}-{slug}.md` (auto-moved at session start)
- INDEX.md lists all (active + archived) with one-line summaries

---

## File Naming Convention

**Format**: `{HHMM}-{slug}.md`

**Examples**:
- `2145-data-restructure.md` → Created at 21:45, about data restructuring
- `0900-roadmap-audit-start.md` → Created at 09:00, starting roadmap audit
- `1500-handoff-system-design.md` → This file, created at 15:00

**Rules**:
- HHMM: 24-hour format (use leading zeros: 0900, not 900)
- slug: 2-4 words, hyphenated, lowercase, self-explanatory
- Avoid generic slugs (use "data-restructure" not "work" or "progress")

---

## Handoff Triggers (3 Layers)

| Layer | Trigger | When | Who | Output |
|-------|---------|------|-----|--------|
| **Auto pre-compact** | `pre-compact-backup.sh` hook | Compaction imminent | Nova (automated) | Auto-generated handoff to `active/` |
| **Manual checkpoint** | `/checkpoint` skill or "write a handoff" command | Mid-session milestone | Omar or Nova | Rich template handoff to `active/` |
| **Session end** | `/end` skill | End of session (voluntary) | Omar or Nova | Final handoff to `active/` |

**Auto-archival**: At session start, all files in `active/` are moved to the dated hierarchy: `{YYYY}/{MM}/{DD}/{HHMM}-{slug}.md`

---

## Lifecycle Phases

### Phase 1: Creation
- Nova or Omar writes handoff to `{project}/ops/handoff/active/{HHMM}-{slug}.md`
- INDEX.md updated with entry: `[{slug}](active/{HHMM}-{slug}.md) — {summary}`
- File persisted to disk BEFORE responding to Omar

### Phase 2: Session Start (Next Session)
- Hook `session-start-archival.sh` runs
- All files in `active/` are moved to `{YYYY}/{MM}/{DD}/{HHMM}-{slug}.md`
- INDEX.md updated with new location and `[archived]` status tag
- New session reads INDEX.md to understand prior context

### Phase 3: Historical Archive
- Handoff in dated directory is immutable (read-only)
- Can be searched via INDEX.md or global registry
- Accessible for RCA, pattern analysis, or cold resume

---

## Template (Enriched)

All handoffs follow this structure (minimum fields required):

```markdown
# Handoff — {project-name} — {YYYY-MM-DD HH:MM}

## Session Summary
{2-3 sentences: what happened, where we are now, what changed}

Example:
"Completed data foundation audit + validation. Fixed rates, R05/R02 corrections, archived 6 duplicate specs files. 10 new Linear issues created (VT-94 to VT-103). App-first ROADMAP strategy approved by Omar."

## Task Graph Status
{Copy current TASKS.md or task list with statuses}

Format:
- P0 — [task-id] Task Name [status: done/in-progress/blocked]
- P1 — [task-id] Task Name [status]
- ...

## Decisions Made This Session
- {decision 1 — what was decided, why}
- {decision 2}
- ...

Example:
- Migrate to per-project handoff system (centralized index, standardized format)
- archive/ singular convention enforced (merge archives/ into archive/)

## Blockers & Unblocks
- {blocker description} — **who/what unblocks**: {action + owner}
- {blocker 2} — **who/what unblocks**: {action}

Example:
- MCP access for custom agents broken — **unblocked by**: ToolSearch threshold fix (auto:5→auto:100) + transcript_path check for sub-agents

## Files Modified (Uncommitted)
- `{path}` — {short reason}
- `{path}` — {reason}

Example:
- `MEMORY.md` — Added hooks status, linear state, file locations
- `ops/decisions/2026-02-25-handoff-system-design.md` — NEW

## Files Read (Key Context)
- `{path}` — {why read}
- `{path}` — {why}

Example:
- `project/ROADMAP.md` — To understand 6-phase strategy
- `AGENTS.md` — To check file organization rules

## Artifacts Generated
- `{path to report, dashboard, analysis, diagram}`
- `~/omar/artifacts/dashboards/audit-2026-02-24.html` — Consolidated audit results

## Code/Schema Changes
{If any changes to structure, config, or contracts — describe the delta}

Example:
- AGENTS.md: Added handoff directory structure and naming convention
- settings.json: ToolSearch threshold changed from 5 to 100

## Next Steps (Ordered by Priority)
1. {Exact next action + owner + why this first}
2. {Next action}
3. ...

Example:
1. Create `ops/handoff/` directories in ~/omar/ and .ecosystem/ projects (P0, unblocks all handoff work)
2. Update AGENTS.md with handoff convention + archive/ singular rule (P1, governance)
3. Migrate existing handoffs to new structure (P2, cleanup)

## Context for Cold Resume
{Narrative paragraph for someone reading this handoff days/weeks later}

This tells the story: What was the big picture goal? What was completed? What's left? What are the gotchas or non-obvious decisions?

Example:
"Villa Thaifa data foundation audit completed Feb 24–25. Rates spreadsheet matched, R05/R02 image corrections made, 6 duplicate spec files archived. ROADMAP rewritten: 6 phases from data foundation → LHCM-OS, app-first strategy (Said validates through app, not Omar). 10 Linear issues created for phase work. All archival decisions documented in ops/decisions/. Next session: implement handoff system design (this decision), then start Wave 3 (deep work on data domains)."

## Session Metadata
- **Project**: {project-name}
- **Session date**: {YYYY-MM-DD}
- **Duration**: {hours:minutes} (if known)
- **Written by**: {Nova/Omar/agent-name}
- **Next session lead**: {Omar/agent-name}
```

---

## Index System

### Per-Project INDEX.md

**Location**: `{project}/ops/handoff/INDEX.md`

**Purpose**: Master list of all handoffs in this project with quick lookup.

**Format**:
```markdown
# Handoff Index — {project-name}

| Date | Time | Slug | Status | Summary | Path |
|------|------|------|--------|---------|------|
| 2026-02-25 | 15:00 | handoff-system-design | archived | Unified handoff system standard approved | `2026/02/25/1500-handoff-system-design.md` |
| 2026-02-25 | 09:00 | roadmap-audit-start | archived | Roadmap audit + data foundation review begins | `2026/02/25/0900-roadmap-audit-start.md` |
| 2026-02-24 | 14:30 | session-pending | active | In-progress handoff from Feb 24 session | `active/1430-session-pending.md` |

## Recent Handoffs (Last 5 Sessions)
[list]

## Search by Topic
- Data/Inventory: [links]
- Linear/Governance: [links]
- Architecture: [links]
```

**Updates**: INDEX.md is updated whenever a handoff is created or archived.

### Global Handoff Index

**Location**: `~/omar/operational/productivity/handoff-index.md`

**Purpose**: Central registry pointing to all handoff systems across all projects.

**Format**:
```markdown
# Global Handoff Index — All Projects

## Active Handoffs

| Project | Last Handoff | Date | Slug | Link |
|---------|--------------|------|------|------|
| Villa Thaifa | 2026-02-25 15:00 | handoff-system-design | `/home/director/villa-thaifa/ops/handoff/active/1500-handoff-system-design.md` |
| ~/omar/ | 2026-02-25 14:00 | nova-agentic-os-work | `/home/director/omar/operational/productivity/handoffs/active/1400-nova-agentic-os-work.md` |
| .ecosystem | 2026-02-20 18:30 | vega-sprint-complete | `~/.ecosystem/handoffs/2026/02/20/1830-vega-sprint-complete.md` |

## Project Registries

- **Villa Thaifa**: `/home/director/villa-thaifa/ops/handoff/INDEX.md`
- **Omar Operational**: `/home/director/omar/operational/productivity/handoffs/INDEX.md`
- **Ecosystem/Vega**: `~/.ecosystem/handoffs/INDEX.md`

## Discovery Tips
- Search by project: see per-project INDEX.md
- Search by topic: use global grep across all projects
- Latest handoff per project: see "Active Handoffs" above
```

---

## Archive Standardization

**Decision**: Use singular `archive/` everywhere (NOT `archives/`).

**Rationale**: Consistent naming convention, easier shell commands, matches git convention.

**Changes**:
- Villa Thaifa already migrated `archives/` → `archive/` (Omar merged manually)
- AGENTS.md updated to enforce singular convention going forward
- All agents must use `archive/` only; `archives/` is forbidden

**Enforcement**: Add to AGENTS.md § File Organization:
```
NEVER: archives/, archival/, archived/
ALWAYS: archive/
```

---

## Rules & Governance Updates Required

### AGENTS.md Updates

**§ File Organization Rules**

Add handoff convention:
```
Operational handoff?                 --> ops/handoff/
  active session?                    --> ops/handoff/active/{HHMM}-{slug}.md
  archived session?                  --> ops/handoff/{YYYY}/{MM}/{DD}/{HHMM}-{slug}.md
  index/discovery?                   --> ops/handoff/INDEX.md

Archive directory (SINGULAR):        --> archive/
  NEVER: archives/, archival/, archived/
  ALWAYS: archive/
```

### Skill Updates

**`/checkpoint` skill** and **`/end` skill**:
- Write handoff to `ops/handoff/active/{HHMM}-{slug}.md`
- Use enriched template (above)
- Update project's `ops/handoff/INDEX.md`

### Hook Updates

**`session-start-archival.sh`** (NEW):
- At session start, move all files in `ops/handoff/active/` to dated hierarchy
- Parse HHMM from filename
- Create directory structure if needed: `{YYYY}/{MM}/{DD}/`
- Update INDEX.md with new location + `[archived]` tag

**`pre-compact-backup.sh`** (EXISTING):
- Enhance to auto-generate handoff from session state
- Write to `ops/handoff/active/` with best-guess timestamp (e.g., current time)
- Include task graph, files modified, key decisions made
- Ensures context survives compaction

---

## Implementation Task Graph

```
PHASE 1: Design & Setup
├─ #21 Write design doc (THIS FILE) ✓ DONE
├─ #22 Create directory structure
│  ├─ ops/handoff/ in Villa Thaifa
│  ├─ ops/handoff/ in ~/omar/operational/productivity/
│  └─ Ensure .ecosystem/handoffs/ exists
└─ #23 Create template file
   └─ context/templates/handoff-template.md

PHASE 2: Automation & Indexing
├─ #24 Write session-start-archival.sh hook
├─ #25 Enhance pre-compact-backup.sh hook
├─ #26 Create per-project INDEX.md files
└─ #27 Create global handoff-index.md
   └─ ~/omar/operational/productivity/handoff-index.md

PHASE 3: Integration
├─ #28 Update AGENTS.md conventions
├─ #29 Update /checkpoint and /end skills
└─ #30 Migrate existing handoffs (cleanup)
   ├─ Scan ~/.ecosystem/handoffs/ for existing files
   ├─ Scan ~/omar/operational/productivity/handoffs/
   ├─ Move to dated hierarchy + INDEX.md
   └─ Verify no handoff lost

PHASE 4: Validation
├─ #31 Test session-start archival
├─ #32 Test /checkpoint skill
├─ #33 Test /end skill
└─ #34 Test global index discovery
```

---

## Decision Metadata

| Field | Value |
|-------|-------|
| **Status** | APPROVED |
| **Date** | 2026-02-25 |
| **Decided by** | Omar El Mountassir |
| **Scope** | All projects (Villa Thaifa, ~/omar/, .ecosystem) |
| **Trigger** | Scattered handoffs, no standard, lost 10 minutes searching |
| **Impact** | Session continuity, cold resume, discovery, governance |
| **Implementation complexity** | Medium (directory structure + 2 hooks + 2 skills + INDEX files) |
| **Risk** | Low (read-only for archived; opt-in at start) |
| **Rollout** | Phase 1 → 2 → 3 → 4 (can stop at any phase) |

---

## Appendix: Global Handoff Search Commands

```bash
# Find all handoffs across all projects
find ~/ -path "*ops/handoff/active/*.md" -o -path "~/.ecosystem/handoffs/active/*.md"

# Find handoffs from last 7 days
find ~/omar/operational/productivity/handoffs -name "*.md" -newermt "7 days ago"

# Search handoff content by topic
grep -r "data foundation" ~/*/ops/handoff/ ~/.ecosystem/handoffs/

# List all active handoffs (human-readable)
ls -lh ~/*/ops/handoff/active/ ~/.ecosystem/handoffs/active/ 2>/dev/null

# Open latest handoff
open $(ls -t ~/*/ops/handoff/active/*.md 2>/dev/null | head -1)
```

---

## Reference

- **Project AGENTS.md**: Handoff convention enforcement
- **Session-start hook**: Archival automation
- **Pre-compact hook**: Context preservation
- **Global index**: Cross-project discovery
- **Per-project INDEX.md**: Local lookup


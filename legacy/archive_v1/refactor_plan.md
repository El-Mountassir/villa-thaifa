# 🏗️ Implementation Plan - Project Refactoring

**Goal**: Transform the "legacy mess" into a clean, Agentic AI-Friendly structure.
**Principle**: "A place for everything, and everything in its place."

## User Review Required

> [!IMPORTANT]
> This refactor involves moving large directories (`temp`, `specs`, `data`).
> Please confirm you are okay with archiving the `temp/` folder which contains legacy agent outputs.

## Proposed Structure

```
/home/omar/projects/clients/villa-thaifa/
├── 📝 Root Docs (Keep)
│   ├── README.md         # Entry Point
│   ├── GEMINI.md         # Brain
│   ├── MISSION.md        # Vision
│   ├── ROADMAP.md        # Plan
│   └── STATE.md          # Status
├── 📂 content/ (Rename/Move 'assets' & 'data')
│   └── facilities/       # Room photos & markdown
├── 📚 docs/ (Rename/Move 'specs')
│   ├── knowledge/        # HotelRunner, OTAs
│   └── architecture/     # System specs
├── 📋 tasks/ (Move 'task.md' & 'missions')
│   ├── active.md         # Current Kanban
│   └── archive/          # Old tasks
└── 📦 archive/ (Move 'temp' & 'archives')
    └── legacy_v1/
```

## Proposed Changes

### 1. AI-First Core (Priority 1)

#### [RESCUE] temp/villa-thaifa/AGENTS.md -> AGENTS.md

- **Location**: Root (`/AGENTS.md`)
- **Action**: Update to be the "Master Operating System" referencing `GEMINI.md`.

#### [CREATE] .antigravity/

- **Purpose**: Antigravity Framework Rules.
- **Action**: Create if missing.

#### [CREATE] .context/

- **Purpose**: Knowledge Base injected into Agent Context.
- **Action**: Move core context files here if appropriate, or symlink `GEMINI.md`.

#### [CREATE] .gemini/

- **Purpose**: Gemini CLI Settings (`settings.json`).

#### [CREATE] artifacts/

- **Purpose**: Standard Output directory for Agent deliverables.

#### [UPDATE] GEMINI.md

- **Role**: The "Shared Brain".
- **Action**: Maintain as the central index, linked from `.context/`.

### 2. Rescue & Merge (Business Context)

#### [RESCUE] temp/villa-thaifa/docs/ -> docs/

- Merge high-value briefs and architecture notes.

#### [RESCUE] temp/villa-thaifa/data/admin/ -> admin/

- **New Root Folder**: `admin/` (Contacts, Profiles).

### 3. Content Consolidation

#### [MOVE] data/assets/ -> content/

- Rename `assets` to `content` (Photos, Markdown).

### 4. Tasks & Workflow

#### [MOVE] task.md -> tasks/active.md

- Centralize all work items in `tasks/`.

### 5. Documentation Cleanup

#### [MOVE] specs/ -> docs/specs/

- Move current `specs` inside `docs` to keep it clean.
- `docs/knowledge` (HotelRunner)

### 4. Tasks Migration

#### [MOVE] task.md -> tasks/active.md

- Establish `tasks/` as the work center.

### 5. Archiving (The Rest)

#### [MOVE] temp/ -> archive/legacy_structure/

- Once valuable items are extracted, archive the skeleton.

### 6. Link Repair

- Update `GEMINI.md`, `README.md` to point to:
  - `admin/`
  - `docs/`
  - `content/`

## Verification Plan

### Automated

- `tree` to verify new structure.
- Check `GEMINI.md` links still work (update them).

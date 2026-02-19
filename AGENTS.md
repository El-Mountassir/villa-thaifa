# AGENTS.md — Villa Thaifa Workspace Contract

## Repository Structure

@docs/core/STRUCTURE.md

## Structure Documentation System

The codebase uses a tiered structure documentation approach to balance context relevance with token efficiency.

### Available Structure Files

| File                                 | Token Cost | When to Use                               |
| ------------------------------------ | ---------- | ----------------------------------------- |
| `docs/core/STRUCTURE.md`             | ~3KB       | General overview (hybrid: curated + auto-stats) |
| `docs/core/STRUCTURE-card-{role}.md` | 1-2KB      | Role-specific context          |
| `docs/core/STRUCTURE-filtered.txt`   | ~15KB      | Detailed exploration           |
| `STRUCTURE.txt`                      | ~50KB      | Full tree (deep dive only)     |

### Role-Based Structure Cards

Structure cards provide pre-filtered context for specific agent roles:

- **booking**: `data/rooms/`, `data/bookings/`, `data/finance/`
- **browser**: `context/agents/browser/`, `data/property/`
- **hotelrunner**: `scripts/hotelrunner/`, `data/rooms/`
- **admin**: `data/admin/`, `data/operations/`
- **finance**: `data/finance/`, `data/bookings/`
- **guest-comms**: `data/bookings/requests/`, `context/agents/`

Load the card for your role: `docs/core/STRUCTURE-card-{role}.md`

### Maintenance Commands

```bash
make structure-cards    # Regenerate all role cards
make structure-update   # Full structure refresh
```

### When to Regenerate

Run `make structure-cards` when:

- Adding new agent definitions to `.claude/agents/`
- Creating new data domains in `data/`
- Reorganizing directory structure
- Onboarding new AI agents

Role mappings are configured in: `scripts/structure/role_mappings.yaml`

### Structure Freshness Rule

After creating new directories or adding 3+ files in a single task, run `make structure-update` before concluding the task. This keeps structure cards and stats current for subsequent agents.

### STRUCTURE.md Maintenance

This file uses a hybrid model:
- **Auto-generated**: Header stats (timestamp, file counts)
- **Curated by humans**: ASCII tree and annotations

Run `make structure-update` to refresh stats. Manually update tree when adding top-level directories.

### File Organization Rules

**Files that MUST remain at repository root:**

- `AGENTS.md` — AI agent workspace contract (this file)
- `CLAUDE.md` — Claude Code project instructions
- `GEMINI.md` — Gemini AI project instructions
- `README.md` — Standard repository documentation (universal convention)
- `CHANGELOG.md` — Version history (standard convention)

**Rationale:** AI agent contract files (AGENTS.md, CLAUDE.md, GEMINI.md) must be at root for AI systems to discover and load them. README.md and CHANGELOG.md follow universal open-source conventions.

**Foundational definitions** (MISSION, STRUCTURE, PRINCIPLES) live in `docs/core/`.

**Data files** (JSON, structured markdown inventories) live in `data/`. Never place data in `docs/` or `context/`.

**Operational artifacts** (audits, handoffs, decisions, status dashboards) live in `ops/`. Never place live operational state in `docs/` or `context/`.

**Reference material** (architecture docs, planning docs, templates, agent configs) lives in `context/`. This directory is read-only -- agents consume but do not mutate its contents during normal operations.

**Scripts and tooling** live in `scripts/`. Never place executable code in `docs/` or `ops/`.

**Workflow documentation** (how-to guides for operational procedures) lives in `docs/workflows/`.

**Client-facing documents** (stakeholder profiles, admin notes, support contacts) live in `docs/client/`.

---

## File Placement Decision Tree

Use this flowchart when you are unsure where a new file belongs:

```
Is it structured domain data (JSON, inventory, profiles, rates)?
  YES --> data/
    Is it room data?        --> data/rooms/
    Is it booking data?     --> data/bookings/
    Is it financial data?   --> data/finance/
    Is it property-level?   --> data/property/
    Is it operational config (channels, housekeeping, etc.)? --> data/operations/
    Is it a new domain not yet hardened? --> data/pending-domains/
  NO  |
      v
Is it a live operational artifact (audit, decision, handoff, status, intake)?
  YES --> ops/
    Is it a decision record?     --> ops/decisions/
    Is it an audit report?       --> ops/audit/
    Is it a session handoff?     --> ops/handoff/
    Is it a status dashboard?    --> ops/status/
    Is it unprocessed incoming?  --> ops/intake/
    Is it old/completed?         --> ops/archive/
  NO  |
      v
Is it read-only reference material (architecture, planning, templates, agent configs)?
  YES --> context/
    Is it an agent config/README?       --> context/agents/{agent-name}/
    Is it architecture or planning?     --> context/meta/{topic}/
  NO  |
      v
Is it operational documentation (how-to, workflow, client info)?
  YES --> docs/
    Is it a foundational definition?     --> docs/core/
    Is it a workflow or procedure?       --> docs/workflows/
    Is it client/stakeholder info?       --> docs/client/
  NO  |
      v
Is it a script or automation tool?
  YES --> scripts/
    Is it an audit script?        --> scripts/audit/
    Is it integration-specific?   --> scripts/{integration-name}/
  NO  |
      v
Is it a test?
  YES --> tests/
  NO  --> Ask Omar. Do not guess.
```

---

## Directory Contract

Each top-level directory has a defined purpose, inclusion criteria, and exclusion criteria.

### data/ -- Canonical Source of Truth

**Purpose:** The single authoritative location for all structured domain data.

**What GOES here:** Room profiles, booking records, financial data (rates, billing), property configuration, operational configs (channels, housekeeping, check-in rules, emergency procedures, maintenance schedules), facility descriptions and images, inventory data.

**What does NOT go here:** Documentation, operational artifacts (audits, decisions), scripts, reference material, anything that is not structured domain data.

**Example files:** `data/rooms/R01/profile.md`, `data/finance/rates.json`, `data/operations/channels.json`, `data/property/facilities/spa-hammam.md`

**Subdirectories:**

| Directory               | Contents                                                                                 |
| ----------------------- | ---------------------------------------------------------------------------------------- |
| `data/rooms/`           | Per-room profiles (R01-R12/), master table, amenities, beds, reconciliation log          |
| `data/bookings/`        | Exports, requests, reservations                                                          |
| `data/finance/`         | billing.json, rates.json                                                                 |
| `data/operations/`      | Operational config JSON files (channels, check-in, emergency, housekeeping, maintenance) |
| `data/property/`        | Property-level config and facility data (descriptions + images)                          |
| `data/pending-domains/` | Domains not yet fully hardened (staging area)                                            |
| `data/archive/`         | Archived data versions                                                                   |

### docs/ -- Operational Documentation

**Purpose:** Human-readable and agent-readable documentation for operating Villa Thaifa.

**What GOES here:** Foundational definitions (mission, principles, structure), workflow guides, client and stakeholder information, agent operational docs and logs.

**What does NOT go here:** Structured data (belongs in `data/`), live operational state like audits or decisions (belongs in `ops/`), read-only reference material (belongs in `context/`), scripts (belongs in `scripts/`).

**Example files:** `docs/core/MISSION.md`, `docs/workflows/pricing.md`, `docs/client/stakeholders.md`

**Subdirectories:**

| Directory         | Contents                                                            |
| ----------------- | ------------------------------------------------------------------- |
| `docs/core/`      | MISSION.md, PRINCIPLES.md, STRUCTURE.md -- foundational definitions |
| `docs/workflows/` | Operational procedure guides (pricing, etc.)                        |
| `docs/client/`    | Stakeholder profiles, admin notes, support contacts                 |

### context/ -- Read-Only Reference Material

**Purpose:** Background reference material consumed by agents and humans. Not mutated during normal operations.

**What GOES here:** Architecture documents, planning documents, knowledge references, templates, agent configuration files and READMEs.

**What does NOT go here:** Live operational state (belongs in `ops/`), canonical data (belongs in `data/`), workflow documentation (belongs in `docs/`).

**Example files:** `context/meta/architecture/system-overview.md`, `context/agents/booking/README.md`

**Subdirectories:**

| Directory         | Contents                                                            |
| ----------------- | ------------------------------------------------------------------- |
| `context/agents/` | Agent reference configs and READMEs (booking, browser, hotelrunner) |
| `context/meta/`   | Architecture, knowledge, planning, and template reference files     |

### ops/ -- Live Operational State

**Purpose:** The active workspace for operational artifacts: audits, decisions, handoffs, status tracking, and incoming items.

**What GOES here:** Audit reports, decision records, session handoff documents, status dashboards and snapshots, unprocessed intake items, migration logs.

**What does NOT go here:** Canonical data (belongs in `data/`), documentation (belongs in `docs/`), reference material (belongs in `context/`), scripts (belongs in `scripts/`).

**Example files:** `ops/decisions/2026-02-16-database-architecture.md`, `ops/status/canonical.md`, `ops/handoff/HANDOFF.md`

**Subdirectories:**

| Directory        | Contents                                                 |
| ---------------- | -------------------------------------------------------- |
| `ops/audit/`     | Audit reports and quality checks                         |
| `ops/decisions/` | Decision records with date prefix                        |
| `ops/handoff/`   | Session handoff docs (AI-SESSION-STARTER.md, HANDOFF.md) |
| `ops/status/`    | Status dashboards, snapshots, indexes                    |
| `ops/intake/`    | Unprocessed incoming items                               |
| `ops/archive/`   | Archived operational artifacts (by date)                 |

### scripts/ -- Validation and Tooling

**Purpose:** All executable code for validation, auditing, migration, and tooling.

**What GOES here:** Validation scripts, audit automation, data migration tools, integration scripts, organization utilities.

**What does NOT go here:** Documentation, data, operational artifacts.

**Example files:** `scripts/validate_contracts.py`, `scripts/audit/artifact_inventory.py`, `scripts/organization/reorganize_room_images.py`

**Subdirectories:**

| Directory               | Contents                           |
| ----------------------- | ---------------------------------- |
| `scripts/audit/`        | Audit scripts and rule definitions |
| `scripts/hotelrunner/`  | HotelRunner integration scripts    |
| `scripts/inventory/`    | Inventory management scripts       |
| `scripts/organization/` | Repository organization utilities  |

### tests/ -- Test Suite

**Purpose:** Pytest test files for validating scripts and data contracts.

**What GOES here:** Test files (test\_\*.py), test fixtures, conftest.py.

**What does NOT go here:** Production scripts, documentation, data.

### logs/ -- Log Files (gitignored)

**Purpose:** Runtime log output. Gitignored -- not committed to the repository.

### tmp/ -- Temporary Files (gitignored)

**Purpose:** Scratch space for temporary work. Gitignored -- not committed to the repository.

## Mission

@docs/core/MISSION.md

## Mandatory Workflow

Use this sequence for every operational task:

1. SCOUT
2. REPORT
3. QUESTIONS
4. ACTION
5. COMMIT — After completing a major task (migration, restructure, feature), prompt Omar: "Ready to commit these changes?" Committing is Tier 3 (ASK) — never auto-commit, always prompt.

## Scope

This repo is **Villa Thaifa operations** — property data, rooms, bookings, guest comms, WhatsApp integration, Said Thaifa (owner) context.

## LHCM-OS (broader vision)

LHCM-OS (Lightweight Hotel Channel Management OS) is a separate, broader product vision where Villa Thaifa is the first pilot. LHCM-OS lives at `~/omar/professional/projects/lhcm-os/` — NOT in this repo. You may reference LHCM-OS docs but do not duplicate or merge them here.

## Core Principles

@docs/core/PRINCIPLES.md

## Policies

### Contestability Policy (Critical)

1. Treat all unprocessed data as potentially outdated, suboptimal, or contestable.
2. Do not silently trust legacy sources.
3. Ask Omar for clarification whenever decisions are ambiguous or high impact.
4. When asking, provide short options with one recommended default.
5. Log the chosen decision in status/reconciliation artifacts.

### Data Handling Policy

1. Legacy files are reference-only until reconciled.
2. Archive with checksum before removal from active scope.
3. Record accepted/rejected conflicts in domain reconciliation logs.
4. Do not overwrite conflicting values without trusted evidence.

### Git/GitHub Sync Policy

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

## Task Tracking

**Primary backlog**: [Linear](https://linear.app/el-mountassir) — all durable work items live here.

- Teams: `VT` (Villa Thaifa), `EM` (El Mountassir)
- Issue format: `EM-XXX` or `VT-XXX`
- Workflow conventions: `context/meta/planning/linear-workflow.md`

**Session-local tasks**: Use `TaskCreate` for breaking a Linear issue into execution steps within a single session. Linear = WHAT needs doing, TaskCreate = HOW to do it this session.

### Open Loops (Migrate to Linear)

1. Pending data domains: `data/pending-domains/` -- facilities.md awaiting hardening into `data/property/`
2. Large directory triage: `context/meta/knowledge/` (54 files), `context/meta/planning/` (96 files), `ops/audit/quality/` (62 files) need triage for archiving vs reclassification

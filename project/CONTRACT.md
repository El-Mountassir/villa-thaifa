# Project Contract -- Villa Thaifa

<!-- What this file is: the operational constitution for agents working in this project.
     AGENTS.md defines workspace structure and file placement rules.
     This file defines WHO writes WHERE, which platforms are in scope, how data flows,
     and the mandatory workflow, policies, and task tracking conventions. -->

> **Note**: Sections 1 (Project Identity) and 2 (Scope) are also inlined in AGENTS.md for always-loaded context. The Directory Contract (Section 3) is the authoritative reference for per-directory rules; AGENTS.md contains a condensed summary. CONTRACT.md remains the authoritative reference for all operational details.

---

## 1. Project Identity

| Field       | Value                       |
| ----------- | --------------------------- |
| Name        | Villa Thaifa                |
| Slug        | villa-thaifa                |
| Repo        | El-Mountassir/villa-thaifa  |
| Linear Team | VT                          |
| Repo root   | /home/director/villa-thaifa |

---

## 2. Scope

This repo is **Villa Thaifa operations** -- property data, rooms, bookings, guest comms, WhatsApp integration, Said Thaifa (owner) context.

### LHCM-OS (broader vision)

LHCM-OS (Lightweight Hotel Channel Management OS) is a separate, broader product vision where Villa Thaifa is the first pilot. LHCM-OS lives at `~/omar/professional/projects/lhcm-os/` -- NOT in this repo. You may reference LHCM-OS docs but do not duplicate or merge them here.

---

## 3. Directory Contract

Each top-level directory has a defined purpose, inclusion criteria, and exclusion criteria.

### project/ -- Project Constitution

**Purpose:** The foundational identity, governance, and operational rules for the project.

**What GOES here:** Mission statement, core principles, project structure overview, operational contract (workflow, policies, task tracking), roadmap.

**What does NOT go here:** Structured data (belongs in `data/`), workflow documentation (belongs in `docs/`), operational artifacts (belongs in `ops/`), reference material (belongs in `context/`).

**Example files:** `project/MISSION.md`, `project/CONTRACT.md`, `project/STRUCTURE.md`

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

**What GOES here:** Workflow guides, client and stakeholder information, agent operational docs and logs.

**What does NOT go here:** Structured data (belongs in `data/`), live operational state like audits or decisions (belongs in `ops/`), read-only reference material (belongs in `context/`), scripts (belongs in `scripts/`), project identity files (belongs in `project/`).

**Example files:** `.agents/workflows/pricing.md`, `docs/client/stakeholders.md`

**Subdirectories:**

| Directory            | Contents                                                |
| -------------------- | ------------------------------------------------------- |
| `.agents/workflows/` | Workflows, Operational procedure guides (pricing, etc.) |
| `docs/client/`       | Stakeholder profiles, admin notes, support contacts     |

### context/ -- Read-Only Reference Material

**Purpose:** Background reference material consumed by agents and humans. Not mutated during normal operations.

**What GOES here:** Architecture documents, planning documents, knowledge references, templates, agent configuration files and READMEs.

**What does NOT go here:** Live operational state (belongs in `ops/`), canonical data (belongs in `data/`), workflow documentation (belongs in `docs/`).

**Example files:** `context/meta/architecture/system-overview.md`, `.agents/booking/README.md`

**Subdirectories:**

| Directory       | Contents                                                            |
| --------------- | ------------------------------------------------------------------- |
| `.agents/`      | Agent reference configs and READMEs (booking, browser, hotelrunner) |
| `context/meta/` | Architecture, knowledge, planning, and template reference files     |

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
| `ops/archive/`   | DEPRECATED — do not add new files. Use `ops/{domain}/archive/` instead |

### archive/ -- Global Archive

**Purpose:** The final resting place for fully verified, actioned, and deprecated files.

**What GOES here:** Old documents, completed audits, deprecated architecture files, past handoffs that are no longer relevant.

**Example files:** `archive/2026-01-old-strategy.md`

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

### infra/ -- Infrastructure Configuration

**Purpose:** Infrastructure-as-code, deployment configs, and environment setup.

**What GOES here:** Docker configs, CI/CD pipelines, deployment scripts, infrastructure definitions.

**What does NOT go here:** Application code, documentation, data.

### src/ -- Application Source Code

**Purpose:** Application source code for any software components of the project.

**What GOES here:** Application code, libraries, modules.

**What does NOT go here:** Scripts/tooling (belongs in `scripts/`), tests (belongs in `tests/`), data.

### logs/ -- Log Files (gitignored)

**Purpose:** Runtime log output. Gitignored -- not committed to the repository.

### tmp/ -- Temporary Files (gitignored)

**Purpose:** Scratch space for temporary work. Gitignored -- not committed to the repository.

---

## 4. Agent Output Paths

| Agent type       | Output directory                                          | Notes                                      |
| ---------------- | --------------------------------------------------------- | ------------------------------------------ |
| browser-agent    | /home/director/villa-thaifa/data/pending-domains/browser/ | Screenshots, scraped HTML, raw extractions |
| research-agent   | ~/omar/knowledge/research/{DOMAIN}/                       | Findings and reports (global knowledge)    |
| general-purpose  | /home/director/villa-thaifa/ops/intake/                   | Unclassified artifacts awaiting triage     |
| linear-agent     | (in-memory only)                                          | Writes to Linear, no local file output     |
| Default fallback | /home/director/villa-thaifa/ops/intake/                   | When agent type is not listed above        |

---

## 5. Platform Conventions

| Platform    | Credentials location        | Agent guide                        | Safety                                 |
| ----------- | --------------------------- | ---------------------------------- | -------------------------------------- |
| HotelRunner | ~/.hotelrunner (gitignored) | .agents/hotelrunner/README.md      | Read-only unless explicitly authorized |
| Booking.com | ~/.booking (gitignored)     | .agents/booking/README.md          | Read-only                              |
| Expedia     | (none stored)               | .agents/browser/browser-context.md | Read-only extraction only              |
| WhatsApp    | (none stored)               | .agents/browser/browser-context.md | Read-only unless Omar approves send    |

---

## 6. Agent Context Discovery

Pattern: `.agents/{agent-name}/`

| File                   | Purpose                                               |
| ---------------------- | ----------------------------------------------------- |
| README.md              | Agent role, scope, and operating constraints          |
| extraction-protocol.md | Step-by-step extraction instructions for the platform |
| platform-rules.md      | Platform-specific safety and behavioral rules         |
| capabilities.md        | What this agent can and cannot do in this project     |

Agents MUST read their own `.agents/{agent-name}/` directory before taking any platform action.

---

## 7. Data Flow Rules

```
External platform
      |
      v
Raw extraction --> /home/director/villa-thaifa/data/pending-domains/{DOMAIN}/     (unvalidated)
      |
      v
Validated data --> /home/director/villa-thaifa/data/{DOMAIN}/                     (reconciled, sourced)
      |
      v
Canonical truth --> /home/director/villa-thaifa/data/{DOMAIN}/{FILE}.md or .json  (single source of truth)
```

Rules:

- Raw extractions are NEVER edited in place.
- Conflicts between raw and canonical are logged before resolving.
- No data is promoted to canonical without a documented evidence source.

---

## 8. External References

| Resource                   | Canonical path                                               |
| -------------------------- | ------------------------------------------------------------ |
| Universal rules            | ~/omar/core/resources/rules/universal.md                     |
| Claude Code rules          | ~/.claude/rules/rules.md                                     |
| Agent definitions (shared) | ~/omar/core/resources/agents/                                |
| Linear workflow protocol   | ~/omar/operational/productivity/protocols/linear-workflow.md |
| Output styles              | ~/omar/core/context/output-styles/                           |
| Knowledge base             | ~/omar/knowledge/                                            |

---

## 9. Mandatory Workflow

Use this sequence for every operational task:

1. SCOUT
2. REPORT
3. QUESTIONS
4. ACTION
5. VERIFY -- After any state-changing action on an external platform (e.g., clicking Save/Update), you MUST explicitly verify that the platform registered the change. Do not assume success. Reload the page, do a fresh search, or confirm the UI reflects the persisted data.
6. SYNC -- After verifying the action, identify and update ALL impacted files locally. Use the checklist below.
7. COMMIT -- Run `make changelog`, then commit silently. Committing is Tier 1 (ACT). No announcement needed. Pushing remains Tier 3 (ASK).

---

## 10. SYNC Checklist

After ACTION, ask: "What files are impacted by this change?" Then update each:

| If you changed...              | Also update...                                                                          |
| ------------------------------ | --------------------------------------------------------------------------------------- |
| A decision was made/resolved   | `ops/decisions/`, `ops/decisions/open-conflicts-registry.md`, `ops/status/truth.md`     |
| Data files (rates, rooms, etc) | `ops/status/truth.md`, reconciliation logs                                              |
| A conflict was resolved        | `ops/decisions/open-conflicts-registry.md`, `ops/status/truth.md S6`                    |
| Repository structure changed   | `project/STRUCTURE.md` (`make structure-update`), AGENTS.md if top-level                |
| A tech stack decision was made | `ops/decisions/tech-decisions.md`, `context/meta/planning/vt-app-vision.md STech Stack` |
| A handoff was created/updated  | `ops/handoff/HANDOFF.md` (index), `ops/status/truth.md`                                 |

**Rule**: If unsure whether a file is impacted, err on the side of checking. Silent drift is worse than an unnecessary update.

---

## 11. Policies

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

### Owner Communication Policy

1. **Consolidation**: When writing updates to `ops/status/reports/update/said/README.md`, ALWAYS check if a heading for the current date (e.g., `## 25-02-2026`) already exists.
2. **Metadata**: Every date heading MUST have a metadata flag immediately below it: `**Status:** \`Draft\``or`**Status:** \`Sent\``.
3. **Combine**: If the heading exists and the Status is `Draft`, append your new update into the existing block. Do not create duplicate date headers or standalone messages. Combine greetings into a single message logically sequenced with numbers (e.g., `1️⃣`, `2️⃣`). If the Status is `Sent`, create a new block for the same date (e.g., `## 25-02-2026 (Part 2)`).
4. **Template**: Strictly follow the established Dutch template structure when drafting these reports.

---

## 12. Room Schema Change Protocol

When adding, removing, or modifying any field in room profiles (`data/rooms/R*/profile.md`):

**MANDATORY sequence -- no exceptions:**

1. Update `context/meta/templates/room-profile-template.md` FIRST
2. Get approval (or proceed if autonomous tier allows)
3. Apply the change to ALL 12 room profiles (R01-R12) in one operation
4. Verify all 12 profiles match the updated template

**Self-check**: "Am I about to edit a room profile field that isn't reflected in the template?" If yes -> update the template first.

**Why**: The template is the schema contract. Rooms diverging from the template = silent data drift = broken agents downstream.

---

## 13. Definition of Done (Per Domain)

All must be true:

1. Canonical contract is explicit.
2. Validation scripts pass.
3. Reconciliation log is updated with evidence.
4. Legacy files are archived/deleted with explicit justification.
5. Status files are updated.

---

## 14. Task Tracking

**Primary backlog**: [Linear](https://linear.app/el-mountassir) -- all durable work items live here.

- Teams: `VT` (Villa Thaifa), `EM` (El Mountassir)
- Issue format: `EM-XXX` or `VT-XXX`
- Workflow conventions: `~/omar/operational/productivity/protocols/linear-workflow.md`

**Session-local tasks**: Mandatory for sub-agent delegations via TaskCreate (ephemeral, session-scoped only). Do not use for persistent work items.

**Work overview**: `ops/status/work-overview.md` -- comprehensive task dashboard with all pending work, priorities (P0-P5 MoSCoW+Eisenhower), dependencies, Omar/Said time estimates, and workstream grouping. work-overview.md is a derived summary -- not an independent registry. Update Linear, not work-overview directly. Template: `~/omar/Templates/WORK-OVERVIEW.md`. Agents MUST:

- Read work-overview.md at session start to understand current state
- Update it after completing tasks (remove completed, update statuses)
- Follow the priority system defined in the file header

---

## 15. Open Loops (Migrate to Linear)

1. Pending data domains: `data/pending-domains/` -- contains superseded placeholder files. Active facility data lives in `data/property/facilities/`
2. Large directory triage: `context/meta/knowledge/` (19 files), `context/meta/planning/` (14 files), `ops/audit/quality/` (3 files) need triage for archiving vs reclassification

---

<!-- CONTRACT VERSION: 2.0
     Merged from: PROJECT-CONTRACT.md (v1.0) + AGENTS.md operational sections
     Template source: /home/director/Templates/PROJECT-CONTRACT.md
     Last updated: 2026-02-24 -->

# Structure

> **Last Updated:** 2026-02-19
> **Total Files:** 637 | **Total Directories:** 89

## Quick Stats

| Directory | Files | Purpose                      |
| --------- | ----- | ---------------------------- |
| project/  | 12    | Project constitution         |
| data/     | 412   | Canonical source-of-truth    |
| context/  | 156   | Read-only reference material |
| docs/     | 5     | Operational documentation    |
| ops/      | 18    | Live operational state       |
| scripts/  | 8     | Validation and tooling       |
| tests/    | 1     | Test suite                   |
| infra/    | 0     | Infrastructure configuration |
| src/      | 0     | Application source code      |

---

## Directory Overview

```sh
# Directories
├── data/                       CANONICAL source-of-truth for all domain data
│   ├── admin/                  client profiles, contact info
│   ├── archive/                archived data versions
│   ├── bookings/               booking data
│   │   ├── exports/            channel export files
│   │   ├── requests/           booking requests
│   │   └── reservations/       confirmed reservations
│   ├── finance/                billing.json, rates.json
│   ├── operations/             operational configs (channels, check-in, emergency, housekeeping, maintenance)
│   ├── pending-domains/        domains awaiting hardening
│   ├── property/               property-level data
│   │   ├── facilities/         facility descriptions + images (hall, pool-garden, spa-hammam)
│   │   └── property-config.json
│   └── rooms/                  room profiles, master table, reconciliation log
│       ├── R01-R12/            per-room directories (profile.md + images/)
│       ├── exports/            room data exports
│       ├── rooms.md            master room table
│       ├── rooms-reconciliation-log.md
│       ├── amenities.md
│       └── beds.md
│
├── project/                    project constitution (identity, governance, operational rules)
│   ├── MISSION.md              mission statement
│   ├── PRINCIPLES.md           core principles
│   ├── CONTRACT.md             operational contract (workflow, policies, task tracking)
│   ├── STRUCTURE.md            repository structure overview (this file)
│   └── ROADMAP.md              project roadmap
│
├── docs/                       operational documentation
│   ├── client/                 stakeholder profiles, admin notes, support contacts
│   └── workflows/              operational workflows (pricing)
│
├── context/                    read-only reference material (architecture, planning, templates)
│   └── meta/                   architecture, knowledge, planning, templates
│       ├── architecture/
│       ├── knowledge/
│       ├── planning/
│       └── templates/
│
├── ops/                        live operational state and session artifacts
│   ├── archive/                archived operational artifacts
│   ├── audit/                  audit reports (quality/, archive/history/)
│   ├── decisions/              decision records
│   ├── handoff/                session handoff docs (AI-SESSION-STARTER.md, HANDOFF.md)
│   ├── intake/                 unprocessed incoming items
│   └── status/                 status dashboards, snapshots, indexes
│
├── scripts/                    validation and tooling utilities
│   ├── audit/                  audit scripts + rules
│   ├── hotelrunner/            HotelRunner integration scripts
│   ├── inventory/              inventory management scripts
│   ├── organization/           repo organization scripts
│   └── structure/              structure card generation
│
├── archive/                    legacy archived files
├── tests/                      pytest suite
├── infra/                      infrastructure-as-code, deployment configs
├── src/                        application source code
├── logs/                       log files (gitignored)
├── tmp/                        temporary files (gitignored)
├── .claude/                    Claude Code configuration
└── .archived/                  old archived content

# Root files (MUST stay at root)
├── AGENTS.md      AI agent workspace contract
├── CLAUDE.md      Claude Code project instructions
├── GEMINI.md      Gemini AI project instructions
├── README.md      Repository documentation
├── CHANGELOG.md   Version history
├── Makefile       build and convenience tasks
├── pyproject.toml Python project config
├── uv.lock        dependency lock file
├── .gitignore     git ignore patterns
├── .structureignore  structure tree filter patterns
└── .labels.json   label definitions
```

---

**File placement rules:** See AGENTS.md "File Placement" section and project/CONTRACT.md "Directory Contract" section.

---

## Structure Documentation System

The codebase uses a tiered structure documentation approach to balance context relevance with token efficiency.

### Available Structure Files

| File                                   | Token Cost | When to Use                                     |
| -------------------------------------- | ---------- | ----------------------------------------------- |
| `project/STRUCTURE.md`                 | ~3KB       | General overview (hybrid: curated + auto-stats) |
| `project/STRUCTURE-card-{role}.md`     | 1-2KB      | Role-specific context                           |
| `project/STRUCTURE-filtered.txt`       | ~15KB      | Detailed exploration                            |
| `STRUCTURE.txt`                        | ~50KB      | Full tree (deep dive only)                      |

### Role-Based Structure Cards

Structure cards provide pre-filtered context for specific agent roles:

- **booking**: `data/rooms/`, `data/bookings/`, `data/finance/`
- **browser**: `.agents/browser/`, `data/property/`
- **hotelrunner**: `scripts/hotelrunner/`, `data/rooms/`
- **admin**: `data/admin/`, `data/operations/`
- **finance**: `data/finance/`, `data/bookings/`
- **guest-comms**: `data/bookings/requests/`, `.agents/`

Load the card for your role: `project/STRUCTURE-card-{role}.md`

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

---

_Stats refreshed via `make structure-update` | Tree curated manually_

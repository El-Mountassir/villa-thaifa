# Structure

> **Last Updated:** 2026-02-19
> **Total Files:** 637 | **Total Directories:** 89

## Quick Stats

| Directory   | Files | Purpose                      |
|-------------|-------|------------------------------|
| data/       | 412   | Canonical source-of-truth    |
| context/    | 156   | Read-only reference material |
| docs/       | 42    | Operational documentation    |
| ops/        | 18    | Live operational state       |
| scripts/    | 8     | Validation and tooling       |
| tests/      | 1     | Test suite                   |

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
├── docs/                       operational documentation
│   ├── core/                   foundational definitions (MISSION, PRINCIPLES, STRUCTURE)
│   ├── client/                 stakeholder profiles, admin notes, support contacts
│   └── workflows/              operational workflows (pricing)
│
├── context/                    read-only reference material (architecture, planning, templates)
│   ├── agents/                 agent reference configs and READMEs
│   │   ├── booking/
│   │   ├── browser/
│   │   └── hotelrunner/
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
├── ROADMAP.md     Project roadmap
├── Makefile       build and convenience tasks
├── pyproject.toml Python project config
├── uv.lock        dependency lock file
├── .gitignore     git ignore patterns
├── .structureignore  structure tree filter patterns
└── .labels.json   label definitions
```

---

**File placement rules:** See AGENTS.md "File Placement Decision Tree" and "Directory Contract" sections.

---

_Stats refreshed via `make structure-update` | Tree curated manually_

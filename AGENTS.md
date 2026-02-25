# AGENTS.md -- Villa Thaifa Workspace Contract

<!-- ON-DEMAND REFERENCE FILES (read when needed, not always-loaded):
  - project/CONTRACT.md    — Full operational contract (agent output paths, platform conventions,
                              data flow rules, policies, room schema protocol, task tracking, SYNC checklist)
  - project/STRUCTURE.md   — Repository structure overview (directory tree, file counts, stats)
  - project/STRUCTURE-card-{role}.md — Role-specific structure cards (booking, browser, hotelrunner, admin, finance, guest-comms)
  - project/STRUCTURE-filtered.txt   — Detailed filtered tree (~15KB)
  - STRUCTURE.txt                    — Full tree (~50KB, deep dive only)
  - ops/status/work-overview.md      — Task dashboard with priorities and workstreams
  - ops/handoff/HANDOFF.md           — Session handoff index
-->

## Project Identity

| Field       | Value                       |
| ----------- | --------------------------- |
| Name        | Villa Thaifa                |
| Slug        | villa-thaifa                |
| Repo        | El-Mountassir/villa-thaifa  |
| Linear Team | VT                          |
| Repo root   | /home/director/villa-thaifa |

## Scope

This repo is **Villa Thaifa operations** -- property data, rooms, bookings, guest comms, WhatsApp integration, Said Thaifa (owner) context.

LHCM-OS is a separate broader vision at `~/omar/professional/projects/lhcm-os/` -- NOT in this repo.

## Mission

@project/MISSION.md

## Core Principles

@project/PRINCIPLES.md

## Mandatory Workflow

For every operational task: **SCOUT -> REPORT -> QUESTIONS -> ACTION -> SYNC -> COMMIT**

- **SYNC**: After state-changing actions, update ALL impacted files (see CONTRACT.md §9 for checklist).
- **COMMIT**: Run `make changelog`, then commit. Committing is Tier 1 (ACT). Pushing is Tier 3 (ASK).

## File Organization Rules

**Root files** (MUST stay at root): `AGENTS.md`, `CLAUDE.md`, `GEMINI.md`, `README.md`, `CHANGELOG.md`

**Project constitution** (MISSION, STRUCTURE, PRINCIPLES, CONTRACT, ROADMAP) -> `project/`
**Structured domain data** (JSON, inventories, profiles, rates) -> `data/`
**Operational artifacts** (audits, handoffs, decisions, status) -> `ops/`
**Archived content** (fully processed, deprecated) -> `archive/`
**Read-only reference** (architecture, planning, templates, agent configs) -> `context/`
**Scripts and tooling** -> `scripts/`
**Workflow docs, client info** -> `docs/`

**Handoff convention**: `ops/handoff/active/` for current session, `ops/handoff/{YYYY}/{MM}/{DD}/` for archived. INDEX.md lists all handoffs. Template at `context/meta/templates/handoff-template.md`.

**Archive convention**: Always `archive/` (singular). Never `archives/`. This applies to all directories project-wide.

## File Placement Decision Tree

```
Project identity/governance?             --> project/
Structured domain data?                  --> data/
  room / booking / finance / property /    --> data/{domain}/
  operational config (channels, etc.) /    --> data/operations/
  new unhardened domain?                   --> data/pending-domains/
Live operational artifact?               --> ops/
  decision / audit / handoff / status /    --> ops/{type}/
  unprocessed incoming?                    --> ops/intake/
Handoff / session state?                 --> ops/handoff/active/
Fully archived?                          --> archive/
Read-only reference material?            --> context/
  agent config/README?                     --> context/agents/{agent-name}/
  architecture/planning?                   --> context/meta/{topic}/
Operational documentation?               --> docs/
  workflow/procedure?                      --> docs/workflows/
  client/stakeholder info?                 --> docs/client/
Script or automation tool?               --> scripts/
Test?                                    --> tests/
None of the above?                       --> Ask Omar.
```

## Structure Maintenance

After creating new directories or adding 1+ file or changing anything in the structure, run `make structure-update`.
Run `make structure-cards` when adding agents, data domains, or reorganizing directories.

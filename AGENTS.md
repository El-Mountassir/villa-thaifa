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

For every operational task: **SCOUT -> REPORT -> QUESTIONS -> ACTION -> VERIFY -> SYNC -> COMMIT**

- **VERIFY**: Always explicitly verify state-changing actions on external platforms before assuming success.
- **SYNC**: After verification, update ALL locally impacted files (see CONTRACT.md §10 for checklist).
- **COMMIT**: Run `make changelog`, then commit. Committing is Tier 1 (ACT). Pushing is Tier 3 (ASK).

## File Organization Rules

**Root files** (MUST stay at root): `AGENTS.md`, `CLAUDE.md`, `GEMINI.md`, `README.md`, `CHANGELOG.md`

**Project constitution** (MISSION, STRUCTURE, PRINCIPLES, CONTRACT, ROADMAP) -> `project/`
**Structured domain data** (JSON, inventories, profiles, rates) -> `data/`
**Operational artifacts** (audits, handoffs, decisions, status) -> `ops/`
**Archived content** (fully processed, deprecated) -> `archive/{domain}/` (e.g., `archive/audit/`, `archive/data/`). Single location, no domain-scoped archive/ subdirs.
**Read-only reference** (architecture, planning, templates) -> `context/`
**Agent knowledge** (cross-platform knowledge bases for booking, browser, hotelrunner, whatsapp) -> `.agents/`
**Scripts and tooling** -> `scripts/`
**General documentation, client info** -> `docs/`

> `.agents/` = cross-platform agent knowledge (used by Gemini, Kilo, Codex, Claude).
> `.claude/agents/` = Claude Code sub-agent definitions (Claude-specific).

**Handoff convention**: `ops/handoff/active/` for current session, `ops/handoff/{YYYY}/{MM}/{DD}/` for archived. INDEX.md lists all handoffs. Template at `context/meta/templates/handoff-template.md`.

**Archive convention**: Single `archive/` at root, organized by domain subdirs (`archive/audit/`, `archive/planning/`, etc.). Always singular. Never `archives/`. NEVER create archive/ subdirs inside other directories (e.g., NOT `ops/audit/archive/`). Enforced by hook.

## File Placement Decision Tree

```
Project identity/governance?             --> project/
Structured domain data?                  --> data/
  room / booking / finance / property /    --> data/{domain}/
  operational config (channels, etc.) /    --> data/operations/
Live operational artifact?               --> ops/
  decision / audit / handoff / status /    --> ops/{type}/
  unprocessed incoming?                    --> ops/intake/
Handoff / session state?                 --> ops/handoff/active/
Fully archived content?                  --> archive/{domain}/
Read-only reference material?            --> context/
  architecture/planning?                   --> context/meta/{topic}/
Agent knowledge base (cross-platform)?  --> .agents/{domain}/
Operational documentation?               --> docs/
  human workflow/procedure?                --> docs/workflows/
  client/stakeholder info?                 --> data/admin/client/ [VERIFIED: consolidated 2026-03-25]
Script or automation tool?               --> scripts/
Test?                                    --> tests/
None of the above?                       --> Ask Omar.
```

## Workflow Documentation Rule

**Trigger**: After resolving any complex operation (multi-step, encountered blockers, required investigation, or took >30 minutes), document it as a reusable workflow.

**Location**: `.agents/workflows/{operation-slug}.md`

**Required sections** in each workflow file:

1. **Title & Purpose** — what operation this covers, when to use it
2. **Prerequisites** — what must be true before starting
3. **Procedure** — numbered, specific, copy-pasteable steps
4. **Platform Notes** — HotelRunner quirks, Booking.com gotchas, channel-specific behavior
5. **Troubleshooting** — common failures and their fixes
6. **Last Verified** — date of last successful execution

**Cross-platform**: Workflows are plain English markdown, readable by ANY AI agent CLI (Claude, Gemini, Kilo, Codex). No tool-specific syntax.

**Self-improving**: When an agent encounters a blocker already documented in a workflow, it follows the workflow. When it discovers a NEW blocker or a changed procedure, it updates the workflow before closing the task.

**Existing example**: `.agents/workflows/hotelrunner-stop-sell.md`

## Structure Maintenance

After creating new directories or adding 1+ file or changing anything in the structure, run `make structure-update`.
Run `make structure-cards` when adding agents, data domains, or reorganizing directories.

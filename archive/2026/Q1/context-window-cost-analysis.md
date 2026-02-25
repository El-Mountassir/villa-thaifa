# Context Window Cost Analysis — Villa Thaifa Boot Context

> Generated: 2026-02-24
> Purpose: Quantify lines loaded via @reference chain and identify reduction opportunities

---

## 1. Current @reference Chain

```
CLAUDE.md (26 lines)
  |-- @AGENTS.md (310 lines)
        |-- @project/CONTRACT.md (222 lines)
        |-- @project/STRUCTURE.md (114 lines)
        |-- @project/MISSION.md (9 lines)
        |-- @project/PRINCIPLES.md (10 lines)
```

**Total lines loaded at boot: 691**

Note: This is project-level only. Global ~/.claude/CLAUDE.md, ~/.claude/rules/rules.md, ~/omar/core/resources/rules/universal.md, and MEMORY.md also load, adding ~1500+ additional lines.

---

## 2. Per-File Breakdown & Section Classification

### CLAUDE.md — 26 lines

| Section | Lines | Classification | Rationale |
|---------|-------|----------------|-----------|
| @AGENTS.md reference | 1 | EVALUATE | Chain trigger — could be replaced with lean content |
| Orchestrator identity | 10 | ALWAYS LOAD | Core behavioral constraint |
| Language Override | 5 | ALWAYS LOAD | Project-specific rule |
| Linear Delegation | 5 | ALWAYS LOAD | Project-specific rule |

| Classification | Lines |
|---------------|-------|
| ALWAYS LOAD | 20 |
| EVALUATE | 1 |
| ON-DEMAND | 0 |

---

### AGENTS.md — 310 lines

| Section | Lines | Classification | Rationale |
|---------|-------|----------------|-----------|
| Project Contract (@ref) | 2 | EVALUATE | Triggers CONTRACT.md load |
| Repository Structure (@ref) | 2 | EVALUATE | Triggers STRUCTURE.md load |
| Structure Documentation System (ll.11-67) | 57 | ON-DEMAND | Only needed when working with structure cards |
| File Organization Rules (ll.68-95) | 28 | ON-DEMAND | Only needed when creating/moving files |
| File Placement Decision Tree (ll.98-151) | 54 | ON-DEMAND | Only needed when creating new files |
| Directory Contract (ll.155-301) | 147 | ON-DEMAND | Only needed when placing files in directories |
| Mission (@ref) (ll.303-305) | 3 | ALWAYS LOAD | Core identity — but only 9 lines of content |
| Core Principles (@ref) (ll.307-309) | 3 | ALWAYS LOAD | Core constraints — but only 10 lines of content |

| Classification | Lines |
|---------------|-------|
| ALWAYS LOAD | 6 |
| EVALUATE | 4 |
| ON-DEMAND | 286 |

**Key finding**: 92% of AGENTS.md is ON-DEMAND content that loads every session.

---

### project/CONTRACT.md — 222 lines

| Section | Lines | Classification | Rationale |
|---------|-------|----------------|-----------|
| 1. Project Identity (ll.10-19) | 10 | ALWAYS LOAD | Repo name, slug, paths |
| 2. Scope (ll.22-29) | 8 | ALWAYS LOAD | What this repo is about |
| 3. Agent Output Paths (ll.32-41) | 10 | ALWAYS LOAD | Where agents write — critical routing |
| 4. Platform Conventions (ll.44-52) | 9 | ON-DEMAND | Only when doing platform work |
| 5. Agent Context Discovery (ll.55-67) | 13 | ON-DEMAND | Only when configuring agents |
| 6. Data Flow Rules (ll.70-90) | 21 | ON-DEMAND | Only when processing external data |
| 7. External References (ll.93-103) | 11 | ON-DEMAND | Lookup table — rarely needed in full |
| 8. Mandatory Workflow (ll.106-116) | 11 | ALWAYS LOAD | Core process — every task uses this |
| 9. SYNC Checklist (ll.119-133) | 15 | ON-DEMAND | Only after state-changing actions |
| 10. Policies (ll.136-161) | 26 | ON-DEMAND | Contestability, data handling, git sync |
| 11. Room Schema Change Protocol (ll.164-178) | 15 | ON-DEMAND | Only when editing room profiles |
| 12. Definition of Done (ll.181-190) | 10 | ON-DEMAND | Only when completing a domain |
| 13. Task Tracking (ll.193-208) | 16 | ALWAYS LOAD | How to track work — every session |
| 14. Open Loops (ll.211-215) | 5 | ON-DEMAND | Reference only |
| HTML comment/version (ll.218-222) | 5 | ON-DEMAND | Metadata |

| Classification | Lines |
|---------------|-------|
| ALWAYS LOAD | 55 |
| ON-DEMAND | 147 |

**Key finding**: 66% of CONTRACT.md is ON-DEMAND.

---

### project/STRUCTURE.md — 114 lines

| Section | Lines | Classification | Rationale |
|---------|-------|----------------|-----------|
| Quick Stats (ll.1-19) | 19 | EVALUATE | Useful orientation but changes frequently |
| Directory Overview tree (ll.22-105) | 84 | ON-DEMAND | Only needed when navigating repo structure |
| Footer (ll.107-114) | 8 | ON-DEMAND | Maintenance note |

| Classification | Lines |
|---------------|-------|
| ALWAYS LOAD | 0 |
| EVALUATE | 19 |
| ON-DEMAND | 92 |

**Key finding**: 100% of STRUCTURE.md could be ON-DEMAND. The directory tree duplicates what ls and tree provide.

---

### project/MISSION.md — 9 lines

| Section | Lines | Classification | Rationale |
|---------|-------|----------------|-----------|
| Full file | 9 | ALWAYS LOAD | Core identity, 9 lines is trivial cost |

---

### project/PRINCIPLES.md — 10 lines

| Section | Lines | Classification | Rationale |
|---------|-------|----------------|-----------|
| Full file | 10 | ALWAYS LOAD | Core constraints, 10 lines is trivial cost |

---

## 3. Summary Table

| File | Total Lines | ALWAYS LOAD | EVALUATE | ON-DEMAND | ON-DEMAND % |
|------|-------------|-------------|----------|-----------|-------------|
| CLAUDE.md | 26 | 20 | 1 | 0 | 0% |
| AGENTS.md | 310 | 6 | 4 | 286 | 92% |
| CONTRACT.md | 222 | 55 | 0 | 147 | 66% |
| STRUCTURE.md | 114 | 0 | 19 | 92 | 81% |
| MISSION.md | 9 | 9 | 0 | 0 | 0% |
| PRINCIPLES.md | 10 | 10 | 0 | 0 | 0% |
| **TOTAL** | **691** | **100** | **24** | **525** | **76%** |

---

## 4. Key Numbers

- **691 lines** loaded at boot from project-level @reference chain alone
- **100 lines** (14%) are genuinely needed every session (ALWAYS LOAD)
- **525 lines** (76%) are situational and could be moved to on-demand loading
- **~76% reduction** possible by moving ON-DEMAND content to child-directory CLAUDE.md or .claude/rules/*.md
- **AGENTS.md is the biggest offender**: 310 lines, 92% ON-DEMAND

---

## 5. Top Offenders (by wasted boot lines)

| Rank | Content Block | Lines | Current Location | Recommended Location |
|------|--------------|-------|-----------------|---------------------|
| 1 | Directory Contract (10 directories) | 147 | AGENTS.md | Child-directory CLAUDE.md files (one per dir) |
| 2 | STRUCTURE.md directory tree | 92 | STRUCTURE.md (via @ref) | Remove @ref; agents use make structure-update or read on demand |
| 3 | File Placement Decision Tree | 54 | AGENTS.md | .claude/rules/file-placement.md (no paths: needed, general rule) |
| 4 | Structure Documentation System | 57 | AGENTS.md | project/CLAUDE.md or scripts/structure/CLAUDE.md |
| 5 | CONTRACT.md policies + protocols | 67 | CONTRACT.md (via @ref) | .claude/rules/ with appropriate paths: frontmatter |

---

## 6. Recommended Target Architecture

### Root CLAUDE.md (~50-70 lines, down from 691)

```markdown
# CLAUDE.md

## Identity
[Orchestrator role declaration — 10 lines]

## Language Override
[French communication rule — 5 lines]

## Linear Delegation
[Linear agent routing — 5 lines]

## Project Identity
[Name, slug, repo, Linear team — 10 lines from CONTRACT.md S1]

## Scope
[What this repo is — 8 lines from CONTRACT.md S2]

## Agent Output Paths
[Where agents write — 10 lines from CONTRACT.md S3]

## Workflow
[SCOUT/REPORT/QUESTIONS/ACTION/SYNC/COMMIT — 11 lines from CONTRACT.md S8]

## Task Tracking
[Linear + work-overview pointer — 10 lines from CONTRACT.md S13]

## Mission
[Inline 4 bullet points — 5 lines from MISSION.md]

## Principles
[Inline 7 rules — 9 lines from PRINCIPLES.md]
```

### .claude/rules/ (conditional, loaded on edit)

| File | paths: | Content moved from |
|------|--------|--------------------|
| room-schema.md | data/rooms/** | CONTRACT.md S11 (Room Schema Change Protocol) |
| data-flow.md | data/** | CONTRACT.md S6 (Data Flow Rules) |
| sync-checklist.md | ops/**, data/** | CONTRACT.md S9 (SYNC Checklist) |
| file-placement.md | (none — general) | AGENTS.md File Placement Decision Tree |

### Child-directory CLAUDE.md (loaded on access)

| File | Content moved from |
|------|--------------------|
| data/CLAUDE.md | Directory contract for data/ + subdirs |
| ops/CLAUDE.md | Directory contract for ops/ + subdirs, policies |
| context/CLAUDE.md | Directory contract for context/ |
| scripts/CLAUDE.md | Directory contract for scripts/ |
| project/CLAUDE.md | Structure docs system, structure maintenance |

### Removed from boot entirely

| Content | Reason |
|---------|--------|
| STRUCTURE.md @reference | Agents can read it on-demand; tree duplicates ls/tree |
| AGENTS.md @reference | Replaced by lean root CLAUDE.md + distributed child CLAUDE.md files |
| CONTRACT.md @reference | Essential parts inlined in root; rest distributed |

---

## 7. Estimated Impact

| Metric | Before | After | Change |
|--------|--------|-------|--------|
| Boot lines (project) | 691 | ~100 | -85% |
| Boot lines (global + project) | ~2200+ | ~1600+ | -27% |
| Files in @ref chain | 6 | 1 (root only) | -83% |
| Conditional rule files | 0 | 4+ | New capability |
| Child CLAUDE.md files | 0 | 5+ | New capability |

**Net effect**: Sessions that only need orchestration (most sessions) load ~100 lines instead of ~691. Sessions that touch rooms load ~100 + room rules. Sessions that touch data load ~100 + data contracts. Each session pays only for what it uses.

---

_Analysis based on file reads performed 2026-02-24. Line counts verified against actual file content._

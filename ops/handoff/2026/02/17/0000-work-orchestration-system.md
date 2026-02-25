# Handoff: Work Orchestration System — Strategic Framing

> **Date**: 2026-02-17
> **Status**: DRAFT — Needs dedicated session for deep discussion
> **Relates to**: Linear migration (handoff-linear-migration-preparation.md)
> **Priority**: Discuss in dedicated Linear session BEFORE continuing migration

---

## 1. The Problem

We currently describe Linear as our "primary backlog tool." But that undersells what it actually does — and more importantly, what we NEED it to do.

Our work coordination is currently fragmented across:

| Component              | What It Does                          | Where It Lives                  |
| ---------------------- | ------------------------------------- | ------------------------------- |
| **Linear**             | Durable work items, roadmap, cycles   | linear.app/el-mountassir        |
| **TaskCreate**         | Session-level execution steps         | Claude Code session (ephemeral) |
| **Handoff files**      | Session continuity / context transfer | ops/handoff/\*.md               |
| **MEMORY.md**          | Cross-session state dashboard         | ~/.claude/.../memory/MEMORY.md  |
| **mcp-memory-service** | Durable knowledge/facts/decisions     | SQLite + vector DB              |
| **AGENTS.md**          | Workspace contract / open loops       | repo root                       |
| **Skills**             | Reusable capabilities                 | ~/.claude/skills/               |
| **Hooks**              | Behavioral enforcement                | ~/.claude/hooks/                |

The question: **What is the SYSTEM that connects all of these? And what should we call it?**

---

## 2. Options Evaluated

### Option A: Project Management Hub

**Scope**: Planning, tracking, delivering work items.

- Linear = issues, cycles, milestones
- Standard PM terminology
- Well-understood by anyone
- **Gap**: Misses AI orchestration, knowledge capture, session coordination, enforcement

### Option B: Work Orchestration System (SELECTED DIRECTION)

**Scope**: ALL work coordination across humans + AI agents.

- Linear = **what** needs doing (backlog, roadmap, initiatives)
- TaskCreate = **how** it gets done this session (execution steps)
- Handoffs = **continuity** between sessions
- Memory = **knowledge** that persists
- Skills/hooks = **capabilities and enforcement**
- **Why this fits**: It captures what we actually have — a system that orchestrates work across multiple agents, sessions, and tools. Not just "tracking" but coordinating.

### Option C: Operational Intelligence Platform

**Scope**: Strategic command layer + execution + knowledge + enforcement.

- The broadest viable framing
- Linear as the "brain," everything else as the "nervous system"
- **Risk**: Scope creep — tries to unify things that may not need unifying
- **Value**: Forces us to think about how all components interact

---

## 3. Selected Direction: Work Orchestration System (WOS)

Omar's initial leaning. Needs deeper discussion in dedicated session.

### Component Architecture (Proposed)

```
WORK ORCHESTRATION SYSTEM
├── COMMAND LAYER (Linear)
│   ├── Initiatives — strategic goals
│   ├── Projects — organized work areas
│   ├── Cycles — time-boxed sprints
│   ├── Issues — durable work items
│   ├── Labels — taxonomy and categorization
│   └── Integrations — GitHub sync, MCP
│
├── EXECUTION LAYER (Session-level)
│   ├── TaskCreate — session task graph
│   ├── Sub-agents — delegated execution
│   ├── Skills — reusable capabilities
│   └── Hooks — behavioral enforcement
│
├── CONTINUITY LAYER (Cross-session)
│   ├── Handoff files — session context transfer
│   ├── MEMORY.md — session state dashboard
│   └── mcp-memory-service — durable knowledge
│
└── GOVERNANCE LAYER (Rules & Contracts)
    ├── AGENTS.md — workspace contract
    ├── CLAUDE.md / rules.md — agent rules
    └── Conventions — branch naming, commit format, etc.
```

### Key Design Question

**How tightly should these layers be coupled?**

| Approach           | Description                                                                  | Tradeoff                                             |
| ------------------ | ---------------------------------------------------------------------------- | ---------------------------------------------------- |
| **Loose coupling** | Each layer operates independently, connected by conventions                  | More flexibility, less overhead, but possible drift  |
| **Linear-centric** | Linear is THE hub; everything references Linear issue IDs                    | Strong traceability, but Linear becomes a bottleneck |
| **Hybrid**         | Linear for durable items, local tools for ephemeral, conventions bridge them | Balanced, but requires clear scoping rules           |

---

## 4. Open Questions for Dedicated Session

These questions shape the entire system design:

### Framing

1. Is "Work Orchestration System" the right name? Or something else?
2. Should this be a formal documented system, or just a mental model?
3. Does this framing change how we configure Linear's workspace?

### Scoping (Linear vs TaskCreate)

4. The proposed model: Linear = WHAT (durable), TaskCreate = HOW (session). Does this hold?
5. Should agents auto-create Linear issues when they discover work?
6. What conventions govern issue creation? (required fields, naming, labels)

### Architecture

7. Should every TaskCreate reference a Linear issue ID?
8. What happens to handoff files once work is in Linear? Keep for context only?
9. How do cycles/sprints interact with Omar's review cadence?
10. Should we design for "AI-era sprints" (daily micro-cycles) or traditional 1-week?

### Workspace Structure

11. Keep both teams (VT + EM)? Or restructure?
12. Projects per domain? Per initiative? Per something else?
13. How should triage work for agent-created issues?

### Integration

14. Gemini CLI + Linear MCP — set up now or later?
15. GitHub sync — current config adequate?
16. Should the `/linear` skill include WOS-awareness?

---

## 5. What This Session Accomplished

Before this handoff was created, the following was completed:

- Phase 1.1: Full workspace audit (165 issues, 2 teams, 25 labels, 10 projects)
- Phase 1.5: French label descriptions translated to English (17 labels)
- Phase 1.2: Issue triage started (workspace was rebuilt — identifiers remapped)
- Phase 2.1: linear-workflow.md conventions updated (branch naming, commit format, labels)
- Phase 2.3: AGENTS.md updated with Task Tracking section
- MCP config cleaned: stale project-level entries removed from .claude.json
- Linear API key: working (confirmed via GraphQL)
- Phase 3: /linear skill and linear-agent sub-agent creation (in progress)
- Phase 4: Migration items collection (in progress)

---

## 6. What the Dedicated Session Should Cover

### Part 1: Strategic Framing (30 min)

- Discuss and finalize the WOS framing
- Decide component coupling approach
- Document the agreed architecture

### Part 2: Linear Workspace Design (30 min)

- Resolve team/project structure questions
- Configure cycles, triage, initiatives
- Design label taxonomy refinements

### Part 3: Conventions and Integration (30 min)

- Finalize Linear ↔ TaskCreate scoping rules
- Document in AGENTS.md / rules.md
- Test /linear skill and linear-agent

### Part 4: Migration (30 min)

- Review all items to migrate
- Create issues in Linear
- Verify zero scattered tracking

---

## 7. Files to Read Before the Session

1. This file (the strategic framing)
2. `ops/handoff/handoff-linear-migration-preparation.md` (detailed work breakdown)
3. `~/omar/operational/productivity/protocols/linear-workflow.md` (current conventions)
4. `~/omar/knowledge/research/productivity/linear-workspace-audit-2026-02-17.md` (audit data)
5. `~/omar/knowledge/research/productivity/linear-mcp-deep-dive.md` (MCP capabilities)
6. `~/omar/knowledge/research/productivity/backlog-tool-decision.md` (decision rationale)

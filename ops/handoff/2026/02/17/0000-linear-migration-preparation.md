# Handoff: Work Orchestration System — Linear Migration

> **Date**: 2026-02-17 (updated)
> **Status**: IN PROGRESS — Phase 1 done, Phase 2 partial, Phases 3-5 remain
> **Priority**: DEDICATED SESSION NEEDED — strategic framing + workspace design + migration
> **Decision file**: `~/omar/knowledge/research/productivity/backlog-tool-decision.md`
> **Strategic framing**: `ops/handoff/handoff-work-orchestration-system.md`

---

## Table of Contents

1. [Strategic Context — Work Orchestration System](#1-strategic-context)
2. [Decision Summary](#2-decision-summary)
3. [Current State — What's Been Done](#3-current-state)
4. [Current Linear Workspace](#4-current-linear-workspace)
5. [Vision: Task Graph vs Linear Scoping](#5-vision-task-graph-vs-linear-scoping)
6. [Work Breakdown](#6-work-breakdown)
7. [Migration Inventory](#7-migration-inventory)
8. [Skills and Agents Created](#8-skills-and-agents-created)
9. [Research Files Produced](#9-research-files-produced)
10. [Open Questions for Omar](#10-open-questions-for-omar)
11. [Session Entry Checklist](#11-session-entry-checklist)

---

## 1. Strategic Context

Linear is NOT just a "backlog tool." Omar identified that the system encompassing Linear + TaskCreate + handoffs + memory + skills + hooks is really a **Work Orchestration System** (WOS).

**Full framing doc**: `ops/handoff/handoff-work-orchestration-system.md`

Key insight: The dedicated session should discuss the WOS architecture FIRST, then configure Linear within that framing. This changes how we structure the workspace, what conventions we write, and how deep the integration goes.

**Component layers**:

- **Command Layer**: Linear (initiatives, projects, cycles, issues)
- **Execution Layer**: TaskCreate, sub-agents, skills, hooks
- **Continuity Layer**: Handoff files, MEMORY.md, mcp-memory-service
- **Governance Layer**: AGENTS.md, rules.md, conventions

---

## 2. Decision Summary

**Tool**: Linear (Business Plan, $18/user/month)
**Score**: 8.675 vs GitHub Issues 7.225 (robust — no weight shift flips winner)
**Key drivers**: 40 MCP tools, works with Claude Code AND Gemini CLI, cycles/initiatives/milestones, unlimited issues

**What was wrong in v1 evaluation** (corrected in v2):

- Omar already has Business plan (NOT free tier)
- Linear MCP has 40 tools (NOT 23)
- MCP works with ALL agentic CLIs (NOT just Claude)
- Simplicity removed as dimension per Omar's explicit instruction

---

## 3. Current State — What's Been Done

### Phase 1: Workspace Audit & Cleanup (DONE)

| Task                | Status  | Details                                                                      |
| ------------------- | ------- | ---------------------------------------------------------------------------- |
| 1.1 Workspace audit | DONE    | 165 issues, 2 teams (VT+EM), 25 labels, 10 projects                          |
| 1.2 Issue triage    | PARTIAL | Workspace was rebuilt — identifiers remapped. Fresh triage needed with Omar. |
| 1.5 Labels cleanup  | DONE    | 17 French label descriptions translated to English                           |
| MCP config          | DONE    | Global config in `~/.claude.json`, stale project-level entries removed       |
| API key             | DONE    | Renewed 2026-02-17, confirmed working via GraphQL                            |

### Phase 2: Conventions (PARTIAL)

| Task                   | Status  | Details                                                           |
| ---------------------- | ------- | ----------------------------------------------------------------- |
| 2.1 linear-workflow.md | DONE    | Updated: branch naming, commit format, labels, integration status |
| 2.3 AGENTS.md          | DONE    | Added Task Tracking section with Linear reference                 |
| 2.2 Task scoping rule  | BLOCKED | Needs deeper discussion with Omar (WOS framing)                   |

### Phase 3: Skills & Agents (DONE)

| Task              | Status      | Details                                                                    |
| ----------------- | ----------- | -------------------------------------------------------------------------- |
| 3.1 /linear skill | DONE        | `~/.claude/skills/linear/SKILL.md` — 7 operations, MCP + API modes         |
| 3.2 linear-agent  | DONE        | `~/.claude/agents/linear-agent/AGENT.md` — 8 capabilities, bulk operations |
| 3.3 Gemini MCP    | NOT STARTED | Deferred to dedicated session                                              |
| 3.4 /issue skill  | NOT STARTED | Quick issue creation shorthand                                             |

### Phase 4: Migration (NOT STARTED)

- Migration inventory collected: **53 unique items** across all sources
- Inventory file: `~/omar/knowledge/research/productivity/linear-migration-inventory-2026-02-17.md`
- Actual migration into Linear deferred to dedicated session (needs Omar review)

### Phase 5: Testing (NOT STARTED)

- Deferred to after migration

---

## 4. Current Linear Workspace

### Workspace

- **URL**: `https://linear.app/el-mountassir`
- **Workspace ID**: `el-mountassir`
- **Teams**: `EM` (El Mountassir), `VT` (Villa Thaifa)
- **Plan**: Business ($18/user/month)
- **Active issues**: 165 total (EM: 126, VT: 39)
- **Labels**: 25 (all in English)
- **Projects**: 10

### Configuration

- **API key**: `~/.secrets/.env` (LINEAR_API_KEY) — renewed 2026-02-17, working
- **MCP server**: Global config in `~/.claude.json` (HTTP transport, plain key auth — NO Bearer)
- **GitHub sync**: Configured 2026-02-09 for `El-Mountassir/villa-thaifa-property-management`
- **Branch naming**: `{type}/EM-{N}-{description}` (e.g., `fix/EM-42-billing-rates`)
- **Commit format**: `{type}({scope}): {description} [EM-{N}]`

### Documentation

- `~/omar/operational/productivity/protocols/linear-workflow.md` — Workflow conventions (updated 2026-02-17)
- `~/omar/operational/productivity/protocols/linear-github-setup.md` — GitHub-Linear integration guide
- `~/omar/knowledge/research/productivity/linear-workspace-audit-2026-02-17.md` — Full audit

### What Still Needs Discussion (for dedicated session)

- Team/project structure (keep both? restructure?)
- Cycle cadence (1-week? daily AI sprints?)
- Task scoping model (Linear = WHAT, TaskCreate = HOW — or something else?)
- WOS architecture (how tightly coupled should layers be?)
- Agent-created issue conventions
- Initiative mapping to strategic goals

---

## 5. Vision: Task Graph vs Linear Scoping

**Omar's requirement**: Crystal clear separation. No confusion. Every future instance knows exactly what goes where, when, and how.

### Proposed Scoping (TO DECIDE WITH OMAR)

| Tool                        | Scope                                                                                 | Lifecycle                                                      | Audience                                 |
| --------------------------- | ------------------------------------------------------------------------------------- | -------------------------------------------------------------- | ---------------------------------------- |
| **Linear (EM-XXX)**         | Durable work items: features, bugs, initiatives, epics, operational tasks, backlog    | Persists across sessions. Tracked through cycles. Has history. | Omar + all agents + future collaborators |
| **TaskCreate (task graph)** | Session-local execution plan: breaking a Linear issue into sub-steps for THIS session | Lives only during current session. Compacted away.             | Current agent instance only              |
| **AGENTS.md Open Loops**    | DEPRECATED — migrate to Linear                                                        | N/A                                                            | N/A                                      |
| **TASKS.md**                | DEPRECATED — migrate to Linear                                                        | N/A                                                            | N/A                                      |
| **Handoff files**           | Session continuity: what the NEXT session needs to know to resume                     | Per-session, archived after use                                | Next agent instance                      |

### Workflow Vision

```
1. Session starts
2. Agent reads Linear (list_issues, filter by cycle/priority)
3. Agent picks highest-priority issue (or Omar assigns)
4. Agent creates session task graph (TaskCreate) to break that issue into steps
5. Agent executes steps, updating Linear issue with progress comments
6. At session end: update Linear issue status + create handoff if incomplete
7. No work exists only in markdown files
```

### Key Design Questions

- Should agents auto-create Linear issues when they discover work? (Yes, but with what conventions?)
- Should the task graph reference Linear issue IDs? (Yes — `TaskCreate` description includes `EM-XXX`)
- What happens to handoff files? (Keep for session context, but durable items go to Linear)
- How do we prevent duplication between Linear and task graph? (Scope rule: Linear = WHAT, task graph = HOW)

---

## 6. Work Breakdown

### Phase 1: Linear Workspace Optimization

| #   | Task                                | Details                                                                                                                           |
| --- | ----------------------------------- | --------------------------------------------------------------------------------------------------------------------------------- |
| 1.1 | **Audit existing workspace**        | Use MCP to list all teams, projects, labels, workflow states. Document current state.                                             |
| 1.2 | **Review & triage existing issues** | EM-128 through EM-191+. Each one: still relevant? Close stale ones. Update descriptions for current repo state.                   |
| 1.3 | **Design team/project structure**   | One team vs multiple? Project per domain (rooms, finance, ops, infra)?                                                            |
| 1.4 | **Configure workflow states**       | Optimal state machine: Triage → Backlog → Todo → In Progress → In Review → Done → Cancelled                                       |
| 1.5 | **Design label taxonomy**           | Domain labels (rooms, finance, ops, infra), type labels (bug, feature, chore, audit), source labels (agent-created, omar-created) |
| 1.6 | **Configure cycles**                | 1-week or 2-week? Auto-rollover?                                                                                                  |
| 1.7 | **Enable Triage Intelligence**      | Business plan feature. Configure for agent-created issues.                                                                        |
| 1.8 | **Set up initiatives**              | Map to current strategic goals (data consolidation, governance, scaffold, etc.)                                                   |

### Phase 2: Agent Conventions & Documentation

| #   | Task                                           | Details                                                                                  |
| --- | ---------------------------------------------- | ---------------------------------------------------------------------------------------- |
| 2.1 | **Write Linear conventions for AGENTS.md**     | When to create issues, what fields are required, naming conventions, status update rules |
| 2.2 | **Write task graph scoping rule for rules.md** | Linear = durable work items, TaskCreate = session-local execution steps                  |
| 2.3 | **Update CLAUDE.md / AGENTS.md**               | Replace Open Loops with "See Linear". Remove TASKS.md references. Add Linear workflow.   |
| 2.4 | **Document branch naming**                     | `{type}/EM-{N}-{description}` (e.g., `fix/EM-42-billing-rates`)                          |
| 2.5 | **Document commit conventions**                | Include Linear ID: `fix(billing): correct rate calculation [EM-42]`                      |

### Phase 3: Skills & Agents

| #   | Task                              | Details                                                                                                         |
| --- | --------------------------------- | --------------------------------------------------------------------------------------------------------------- |
| 3.1 | **Create /linear skill**          | Wraps common Linear MCP operations. Quick issue creation, status update, list my issues, cycle report.          |
| 3.2 | **Create linear-agent sub-agent** | Specialized agent for Linear operations. Can be delegated to for bulk issue management, triage, cycle planning. |
| 3.3 | **Add Linear MCP to Gemini CLI**  | `gemini mcp add linear --transport http https://mcp.linear.app/mcp`. Test authentication.                       |
| 3.4 | **Create /issue skill**           | Quick shorthand: `/issue Fix billing rate mismatch` → creates Linear issue with smart defaults                  |

### Phase 4: Migration & Integration

| #   | Task                                     | Details                                                                          |
| --- | ---------------------------------------- | -------------------------------------------------------------------------------- |
| 4.1 | **Migrate audit backlog to Linear**      | The 3 directory triage items (212 files) become Linear issues with proper labels |
| 4.2 | **Migrate AGENTS.md Open Loops**         | Each open loop becomes a Linear issue                                            |
| 4.3 | **Migrate pending tasks from MEMORY.md** | Each pending task becomes a Linear issue                                         |
| 4.4 | **Migrate handoff open items**           | Review all handoff files, extract durable items into Linear issues               |
| 4.5 | **Deprecate TASKS.md**                   | Archive and remove references                                                    |
| 4.6 | **Update /repo-bootstrap scaffold**      | New repos get Linear integration by default                                      |

### Phase 5: Verification & Testing

| #   | Task                                              | Details                                                                        |
| --- | ------------------------------------------------- | ------------------------------------------------------------------------------ |
| 5.1 | **End-to-end test: Claude creates issue via MCP** | Verify create → update → comment → close flow                                  |
| 5.2 | **End-to-end test: Gemini creates issue via MCP** | Same flow in Gemini CLI                                                        |
| 5.3 | **Test GitHub sync**                              | Create issue in Linear → verify it links when PR references ID                 |
| 5.4 | **Test task graph + Linear integration**          | Session picks Linear issue → creates task graph → updates Linear on completion |
| 5.5 | **Audit: zero scattered tracking**                | Verify no work items remain in markdown files                                  |

---

## 7. Migration Inventory

**53 unique items** collected from all scattered tracking locations:

| Source                                    | Items | Key themes                                     |
| ----------------------------------------- | ----- | ---------------------------------------------- |
| `handoff-linear-migration-preparation.md` | 28    | Linear workspace setup, conventions, testing   |
| `handoff-github-template-repos.md`        | 5     | Template repos (blocked by governance)         |
| `MEMORY.md`                               | 5     | Language audit, archive system, sprint cadence |
| `AGENTS.md`                               | 4     | Data domains, directory triage, finance        |
| `handoff-remaining-tasks-2026-02-16.md`   | 3     | Repo-bootstrap, model routing, hooks           |
| `audit-backlog-triage.md`                 | 3     | 212-file directory triage                      |
| `handoff-gemini-standardization.md`       | 2     | Facility images, migration audit               |
| `handoff-critical-session-state.md`       | 1     | TTS restoration                                |
| `handoff-governance-decide.md`            | 1     | Governance format decision                     |
| `handoff-archive-lifecycle-system.md`     | 1     | Archive system design                          |

**Full inventory**: `~/omar/knowledge/research/productivity/linear-migration-inventory-2026-02-17.md`

**Priority breakdown**: 6 Urgent, 18 High, 22 Medium, 7 Low
**Team split**: 43 EM (infrastructure/tooling), 10 VT (data consolidation)

---

## 8. Skills and Agents Created

### Created This Session

| Asset           | Path                                     | Status                                    |
| --------------- | ---------------------------------------- | ----------------------------------------- |
| `/linear` skill | `~/.claude/skills/linear/SKILL.md`       | CREATED — 7 operations, MCP + API modes   |
| `linear-agent`  | `~/.claude/agents/linear-agent/AGENT.md` | CREATED — 8 capabilities, bulk operations |

### Still Needed

| Asset                | Purpose                                   | Priority |
| -------------------- | ----------------------------------------- | -------- |
| `/issue` skill       | Quick shorthand issue creation            | Medium   |
| `/triage` skill      | Review and categorize inbox items         | Low      |
| Update `/start`      | Add "read Linear issues" to session start | Medium   |
| Update `/end`        | Add "update Linear issues" to session end | Medium   |
| Update `/checkpoint` | Include Linear status update              | Low      |

---

## 9. Research Files Produced

All in `~/omar/knowledge/research/productivity/`:

| File                                       | Content                                               |
| ------------------------------------------ | ----------------------------------------------------- |
| `backlog-tool-decision.md`                 | /decide evaluation v2 — Linear wins 8.675 vs GH 7.225 |
| `linear-mcp-deep-dive.md`                  | MCP research: 40 tools, Claude+Gemini setup           |
| `linear-agent-integration.md`              | Linear CLI/API/SDK research, pricing                  |
| `gh-cli-linear-sync.md`                    | GitHub-Linear sync behavior                           |
| `github-issues-agent-integration.md`       | GitHub Issues research for comparison                 |
| `linear-workspace-setup-best-practices.md` | Workspace structure, labels, cycles                   |
| `linear-workspace-audit-2026-02-17.md`     | Full workspace audit (165 issues, 2 teams)            |
| `linear-triage-log-2026-02-17.md`          | Triage attempt log (workspace rebuilt)                |
| `linear-migration-inventory-2026-02-17.md` | 53 items to migrate                                   |

---

## 10. Open Questions for Dedicated Session

### Strategic (WOS Framing)

1. Is "Work Orchestration System" the right name?
2. How tightly coupled should the layers be? (Loose / Linear-centric / Hybrid)
3. Should this be formally documented as a system architecture?

### Workspace Design

4. **Team structure**: Keep both VT + EM? Or restructure?
5. **Cycle cadence**: 1-week? Or explore daily AI-era micro-sprints?
6. **Existing issues**: Full triage together (identifiers were remapped)
7. **Project structure**: Per domain? Per initiative? Per something else?

### Scoping

8. **Linear vs TaskCreate**: Is Linear=WHAT, TaskCreate=HOW the right model?
9. **Agent auto-creation**: Should agents auto-create Linear issues? With what conventions?
10. **Handoff files**: Keep for session context, or fully replace with Linear?

### Integration

11. **Gemini MCP**: Set up in this session or defer?
12. **GitHub sync**: Current config adequate?

---

## 11. Session Entry Checklist

When starting the dedicated Linear/WOS session:

```
[ ] Read this file completely
[ ] Read ops/handoff/handoff-work-orchestration-system.md (strategic framing)
[ ] Read backlog-tool-decision.md (the approved decision)
[ ] Read linear-migration-inventory-2026-02-17.md (53 items to migrate)
[ ] Verify Linear MCP tools are loaded (restart session if needed)
[ ] PART 1: Discuss WOS framing with Omar (30 min)
[ ] PART 2: Design Linear workspace structure (30 min)
[ ] PART 3: Finalize conventions, test /linear skill + linear-agent (30 min)
[ ] PART 4: Review migration inventory, create issues in Linear (30 min)
[ ] Update AGENTS.md, MEMORY.md, rules.md with final state
[ ] Commit and push all changes
```

---

## Dependencies

```
WOS Discussion → Workspace Design → Convention Updates → Migration
                                                      → Testing
/linear skill (DONE) → Test in dedicated session
linear-agent (DONE) → Test in dedicated session
```

**Estimated scope**: FULL DEDICATED SESSION. Strategic framing first, then execution. Quality > speed.

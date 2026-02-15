# Workspace Rules

> **Purpose**: Define workspace structure, file organization, and agent permissions.
> **Last Updated**: 2026-01-30 (Phase 1 + Phase 2: Rules + Linear Integration)

---

## Agent Workspace Structure

> **ALL agents (Claude, Gemini, Cursor, etc.) MUST store artifacts in `.agents/`**
> **NEVER** use `~/.claude/`, `~/.gemini/`, or any personal directory.

| Type      | Location                     | Purpose                                            |
| :-------- | :--------------------------- | :------------------------------------------------- |
| Plans     | `.agents/plans/`             | Implementation plans (read-only once in execution) |
| Artifacts | `.agents/artifacts/`         | Generated outputs, reports, screenshots            |
| Sessions  | `.agents/sessions/`          | Session transcripts and handoff notes              |
| Archive   | `.agents/artifacts/archive/` | Deprecated/completed artifacts                     |
| Rules     | `.agents/rules/`             | Governance rules (this directory)                  |

### Before Starting Any Task

1. Read `.agents/README.md` for workspace rules
2. Check `.agents/plans/` for existing plans
3. Check `.agents/sessions/` for recent context
4. **Check Linear for assigned issues**

---

## RULE #3: All Work Must Be Registered in Linear

**Effective**: 2026-01-30 (Phase 2 Complete)

**Linear is the single source of truth for all operational tasks.**

No agent shall execute a task that is not registered in Linear.

### Before Starting ANY Work

1. **Check Linear**: `/linear "show my assigned issues"`
2. **Select Issue**: Pick highest priority unblocked issue
3. **Move to In Progress**: Update Linear status
4. **Create Branch**: `agent/<name>/<date>-LIN-<issue-id>`
5. **Execute**: Work on implementation
6. **Update Linear**: Post progress comments
7. **Move to Review**: When complete with evidence

### Forbidden Actions

- ❌ Creating local task files (`.md`, `.txt` in `tasks/`, `workstream/`, `.agents/input/jobs/`)
- ❌ Using `workstream/` directory for active work (DEPRECATED)
- ❌ Using `tasks/` directory for active work (DEPRECATED)
- ❌ Using `.agents/input/jobs/missions/` for active work (DEPRECATED)
- ❌ Working on tasks not in Linear

### If Linear is Down

1. **STOP** - Do not proceed with new work
2. **Notify Omar** via email/Slack
3. **Wait** for Linear to recover or alternative decision

### Enforcement

- **Pre-commit hook**: Blocks commits with new task files (see `.git/hooks/pre-commit`)
- **Session start check**: Verify Linear connectivity (Rule #8 in AGENTS.md)
- **Agent review**: Code reviewer checks Linear issue is linked

### Linear Workspace

- **URL**: <https://linear.app/el-mountassir>
- **Team**: "El Mountassir"
- **Projects**:
  - Villa Thaifa - Q1 2026 Operations
  - Villa Thaifa - OTA Integration
  - Villa Thaifa - Room Management

### Usage

```bash
# Check your work
/linear "show my assigned issues"

# Create new issue
/linear "create issue: Task title"

# Update status
/linear "update EM-128 to In Progress"

# Web UI
open https://linear.app/el-mountassir
```

---

## Agent Workspace Structure

> **ALL agents must store artifacts in `.agents/` folder**
> **NEVER** use `~/.claude/plans/` or personal directories

| Type      | Location                     | Purpose                                            |
| :-------- | :--------------------------- | :------------------------------------------------- |
| Plans     | `.agents/plans/`             | Implementation plans (read-only once in execution) |
| Artifacts | `.agents/artifacts/`         | Generated outputs, reports, screenshots            |
| Sessions  | `.agents/sessions/`          | Session transcripts and handoff notes              |
| Archive   | `.agents/artifacts/archive/` | Deprecated/completed artifacts                     |
| Rules     | `.agents/rules/`             | Governance rules (this directory)                  |

### Before Starting Any Task

1. Read `.agents/README.md` for workspace rules
2. Check `.agents/plans/` for existing plans
3. Check `.agents/sessions/` for recent context
4. **Check Linear for assigned issues**

---

## Directory Permissions

> **See**: `docs/architecture/project_structure.md` for full structure

| Directory                      | Permission         | Purpose                          |
| ------------------------------ | ------------------ | -------------------------------- |
| `docs/`                        | [A] Agent-writable | Documentation, guides, knowledge |
| `src/`                         | [A] Agent-writable | Source code                      |
| `ops/`                         | [A] Agent-writable | Scripts, automation              |
| `.agents/`                     | [A] Agent-writable | Agent workspace                  |
| `workstream/`                  | [R] Read-only      | DEPRECATED - See Linear          |
| `tasks/`                       | [R] Read-only      | DEPRECATED - See Linear          |
| `.agents/input/jobs/missions/` | [R] Read-only      | DEPRECATED - Archived            |

---

## File Naming Conventions

### Task Files (DEPRECATED - Use Linear)

**Do NOT create task files.** Use Linear instead.

Legacy format (for reference only):

- `workstream/active/YYYY-MM-DD-description.md`
- `tasks/active.md`
- `.agents/input/jobs/missions/queue/p0/mission-name.md`

### Artifacts

- `YYYY-MM-DD-artifact-name.ext`
- Examples:
  - `2026-01-30-linear-migration-report.md`
  - `2026-01-28-room-audit-results.png`

### Plans

- `descriptive-plan-name.md`
- Examples:
  - `comprehensive-transformation-plan.md`
  - `workspace-standardization-plan.md`

---

## RULE #4: Never Delete - Always Archive

**NEVER delete files or directories.** Move to `.agents/artifacts/archive/` instead.

Empty directories are intentional scaffolding. They exist by design.

### Archiving Process

```bash
# Create dated archive directory
mkdir -p .agents/artifacts/archive/YYYY-MM-DD-description/

# Move deprecated files
mv old-directory/ .agents/artifacts/archive/YYYY-MM-DD-description/

# Create deprecation notice
echo "DEPRECATED - See Linear" > old-directory/README.md
```

### Example

Phase 2 (Linear Migration) archived:

- `workstream/` → `.agents/artifacts/archive/2026-01-30-linear-migration/workstream-legacy/`
- `tasks/` → `.agents/artifacts/archive/2026-01-30-linear-migration/tasks-legacy/`
- `missions/` → `.agents/artifacts/archive/2026-01-30-linear-migration/missions-legacy/`

---

## Verification Protocol

See `.agents/rules/verification.md` for full protocol.

**Before claiming work complete:**

- [ ] Linear issue updated to "Review"
- [ ] Evidence attached to Linear issue (not just local)
- [ ] Branch name includes LIN-###
- [ ] No local task files created
- [ ] Tests passing (if code changes)

---

## Plan Management Rules

### RULE #1: Plans Must Be Moved, Not Copied

When you create a plan in your personal space (e.g., `~/.claude/plans/`), you MUST:

1. **MOVE** it to `.agents/plans/` immediately (not copy)
2. **DELETE** the original from your personal space
3. All future updates happen ONLY in `.agents/plans/`

**Why**: Single source of truth. No duplicate plans causing confusion.

### RULE #2: Each Agent Keeps Their Plan Up-to-Date

After each phase or step:

1. Update the plan with completion status
2. Include evidence of verification (file paths, test results, screenshots)
3. Never mark something "done" without PROOF

**Why**: Other agents need accurate status to coordinate work.

---

## Artifact Organization

Store generated artifacts by type:

```
.agents/artifacts/
├── screenshots/        # Visual evidence
├── reports/            # Analysis reports
├── data/              # Extracted/processed data
├── diagrams/          # Architecture diagrams
└── archive/           # Completed/deprecated
    └── YYYY-MM-DD-description/
```

**Archive Rule**: Move completed artifacts to `archive/` with date prefix after task completion.

## Cross-Reference Protocol

When creating files, always update routing:

- New doc in `docs/architecture/` → Update `AGENTS.md` references
- New artifact → Update relevant plan file
- New session log → Reference in plan if significant

**Why**: Future agents need to discover your work.

---

_Created during Phase 1 + Phase 2 (Rules Consolidation + Linear Integration) - 2026-01-30_

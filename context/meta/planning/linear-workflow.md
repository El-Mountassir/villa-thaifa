# Linear Workflow Rules

> **Status**: 🟢 Linear MCP active, Phase 1 audit complete, migration in progress
>
> This document defines how we use Linear for project management.

## Linear Integration Strategy

### Hybrid Approach (MCP + Code Execution)

- **Simple ops** (create issue, read status) → MCP tools
- **Complex workflows** (reports, bulk updates) → Code execution
- **Token savings**: 93% vs all-MCP approach

### Tools Decision

| Tool                | Purpose              | Integration                             |
| ------------------- | -------------------- | --------------------------------------- |
| **Linear**          | Project Management   | Primary task tracking, roadmap, sprints |
| **GitHub Issues**   | Code-related tickets | Bugs, PRs, technical debt               |
| **Linear ↔ GitHub** | Auto-sync            | Close Issues when PRs merge             |

## Issue Lifecycle

### 1. Ideation (Omar)

Omar adds ideas to **Linear Inbox** with:

- Brief description
- Priority (P0-P3)
- Optional: deadline, assignee

### 2. Refinement (Agent)

Agent converts raw idea to structured issue:

- Detailed description
- Acceptance criteria
- Technical approach
- Effort estimate
- Dependencies
- Labels/tags

### 3. Approval (Omar)

Omar reviews and:

- Approves (move to Backlog)
- Requests changes (keep in Inbox)
- Rejects (archive)

### 4. Execution (Agent)

Agent picks issue from Backlog:

1. Move to "In Progress"
2. Create git branch: `agent/<name>/<date>-<issue-id>`
3. Work on implementation
4. Update issue with progress
5. Move to "Review" when complete

### 5. Review (Omar)

Omar validates:

- Tests deployment
- Reviews code if needed
- Approves → "Done"
- Rejects → Back to "In Progress"

## Issue States

| State           | Meaning                    | Who Moves       |
| --------------- | -------------------------- | --------------- |
| **Inbox**       | New idea, not refined      | Omar creates    |
| **Backlog**     | Ready to work, prioritized | Omar approves   |
| **In Progress** | Active development         | Agent starts    |
| **Review**      | Awaiting validation        | Agent completes |
| **Done**        | Verified complete          | Omar approves   |
| **Archived**    | Cancelled/deprecated       | Omar decision   |

## Priority Levels

| Level  | Meaning      | Example                    | SLA            |
| ------ | ------------ | -------------------------- | -------------- |
| **P0** | Blocking     | Production down, data loss | < 4 hours      |
| **P1** | Critical     | Feature broken, major bug  | < 2 days       |
| **P2** | Important    | Enhancement, minor bug     | < 1 week       |
| **P3** | Nice-to-have | Optimization, future idea  | When available |

## Labels & Organization

### Labels (Current Workspace)

**Type labels** (built-in):
- `Feature` - New functionality
- `Bug` - Something broken
- `Improvement` - Enhancement to existing

**Domain labels** (emoji-prefixed):
- `🤖 AI/Agents` - AI-related work (prompts, agents, models)
- `🎨 Frontend` - Frontend work (UI, design, Astro, Tailwind)
- `🗄️ Backend` - Backend work (API, DB, serverless)
- `🔧 DevOps` - DevOps, CI/CD, deployment, infrastructure
- `📚 Documentation` - Documentation, guides, references
- `🔬 Research` - Investigation, analysis, research
- `⚙️ Config` - Configuration, setup, installation

**Status labels** (emoji-prefixed):
- `🚫 Blocked` - Blocked by external dependency
- `👀 Needs Review` - Awaiting review or validation
- `⏸️ On Hold` - Voluntarily paused
- `🔥 This Week` - Due this week
- `📅 Next Week` - Planned for next week

**Effort labels**:
- `⚡ Quick Win` - Quick task (< 30 min)
- `🎯 Deep Work` - Deep focus work requiring 2h+

**Scope labels**:
- `🏠 Internal` - Internal El-Mountassir work
- `💰 Client` - External client work
- `🔄 Recurring` - Recurring task or maintenance
- `🏆 Win` - Victory or milestone achieved

**Meta labels** (Ways of Working):
- `thinking` - Way of Thinking — foundational concepts, theory
- `working` - Way of Working — methodology, processes
- `supporting` - Way of Supporting — tools, templates, infrastructure
- `representing` - Way of Representing — visualization, communication

## Sprints & Milestones

### Sprint Structure

- **Duration**: 1 week (Monday → Sunday)
- **Planning**: Sunday evening
- **Review**: Saturday afternoon
- **Retrospective**: End of sprint

### Milestone Planning

Major goals tied to dates:

- **M1: Workspace Excellence** (Track A) - Feb 2026
- **M2: Owner Platform MVP** (Track B) - March 2026
- **M3: AI Agents Launch** - June 2026

## Linear ↔ GitHub Sync

> **Status**: ✅ Configured (2026-02-09)
> **Repo**: `El-Mountassir/villa-thaifa-property-management`
> **Setup Guide**: [`docs/operations/linear-github-setup.md`](../../docs/operations/linear-github-setup.md)

### Auto-Close Rules

When PR merges to `main`:

1. GitHub Issue closes automatically
2. Linear Issue moves to "Done" (via sync)
3. Commit message includes: `fixes EM-XXX`

### Branch Naming

```bash
{type}/EM-{N}-{description}
# Examples:
# fix/EM-42-billing-rates
# feat/EM-155-direct-booking
# chore/EM-277-english-labels
```

Links git branch to Linear issue.

### Commit Messages

Include Linear issue ID in commit messages:

```
{type}({scope}): {description} [EM-{N}]
# Examples:
# fix(billing): correct rate calculation [EM-42]
# feat(rooms): add bed configuration schema [VT-10]
# chore(labels): translate French descriptions to English [EM-277]
```

## Director Workflow (Omar)

### Daily Review (5 min)

1. Check Linear Inbox for new ideas
2. Triage: Approve, Request changes, or Archive
3. Check "In Progress" for updates
4. Review "Review" state for validation

### Weekly Planning (30 min)

1. Review upcoming sprint capacity
2. Prioritize backlog items
3. Assign to agents
4. Set sprint goals

### Monthly Roadmap (1 hour)

1. Review milestone progress
2. Adjust priorities based on results
3. Plan next month's focus areas

## Agent Workflow

### Task Selection

When ready for new work:

```bash
# Option 1: Via MCP
/linear "show me my assigned issues"

# Option 2: Via code
# (see memory/knowledge/integrations/linear-guide.md)
```

Pick highest priority unblocked issue.

### Task Execution

1. Move issue to "In Progress"
2. Create branch with Linear ID
3. Implement feature
4. Update issue with progress comments
5. Move to "Review" with evidence

### Task Completion

Before moving to "Review":

- [ ] All tests pass
- [ ] Evidence attached (screenshot, test output)
- [ ] Documentation updated
- [ ] Commit linked to issue

## Comments & Communication

### Progress Updates

Post comments when:

- Starting work (ETA, approach)
- Blocked by dependency
- 50% complete (mid-point check)
- Ready for review (evidence)

### Comment Format

```markdown
## Progress Update

**Status**: 50% complete
**Completed**: Database schema, basic CRUD
**Next**: UI components, tests
**Blockers**: None
**ETA**: Tomorrow EOD
```

## Integration Status

- **Linear**: Primary task tracking (active)
- **GitHub**: Code hosting, PRs, CI/CD
- **Linear ↔ GitHub**: Auto-sync configured (2026-02-09)
- **TaskCreate (session graph)**: Session-local execution steps (scoping TBD)

## When Linear Migration Complete

**Migration Progress (as of 2026-02-17):**

- [x] Linear MCP connected and authenticated
- [x] Workspace audited (165 issues, 2 teams, 25 labels)
- [x] French label descriptions translated to English
- [ ] Issue triage (in progress — marking stale/completed)
- [ ] Agent conventions documented in AGENTS.md
- [ ] Task scoping model defined (Linear vs TaskCreate)
- [ ] Migrate scattered backlog items to Linear
- [ ] All agents use Linear for task tracking
- [ ] Old tracking files deprecated

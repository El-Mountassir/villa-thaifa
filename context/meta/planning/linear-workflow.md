# Linear Workflow Rules

> **Status**: 🟡 Linear MCP configured, task migration pending
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

### Feature Labels

- `feature` - New functionality
- `bug` - Something broken
- `refactor` - Code improvement
- `docs` - Documentation
- `test` - Testing infrastructure
- `chore` - Maintenance

### Component Labels

- `frontend` - UI/UX work
- `backend` - API/server work
- `database` - Schema/migrations
- `integration` - External systems
- `ai-agent` - Agent development

### Status Labels

- `blocked` - Waiting on dependency
- `needs-review` - Requires decision
- `needs-testing` - Awaiting validation

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
agent/<name>/<date>-EM-<issue-id>
# Example: agent/claude/2026-01-30-EM-123
```

Links git branch to Linear issue.

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

## Integration with Workstream

During migration period (Track A Phase 2):

- Linear = New canonical source
- `workstream/` = Legacy, to be archived
- Both maintained until migration complete

Post-migration:

- Linear = Single source of truth
- `workstream/` = Archived

## When Linear Migration Complete

**Success Criteria:**

- [ ] All active tasks migrated from `workstream/` → Linear
- [ ] All agents use Linear for task tracking
- [ ] Linear ↔ GitHub sync active
- [ ] Old `workstream/` files archived
- [ ] Documentation updated (AGENTS.md references)

**Status**: Track A Phase 2 (pending)

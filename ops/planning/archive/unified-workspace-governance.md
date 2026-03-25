# Implementation Plan: Unified Agentic Workspace & Governance

> **Goal**: Establish professional multi-agent workflow with GitHub Issues, verification, and unified artifact management.
> **Status**: Draft - Awaiting Omar Approval

## Problem Statement

| Issue                                                    | Impact                               |
| :------------------------------------------------------- | :----------------------------------- |
| Plans scattered (`~/.claude/`, `~/.gemini/`, `.agents/`) | Agents unaware of each other's work  |
| No verification process                                  | Work claimed complete but not tested |
| No GitHub Issues/PRs                                     | No traceability, no decomposition    |
| Plans not kept up-to-date                                | Reality diverges from documentation  |
| No testing enforcement                                   | Bugs discovered late                 |

## Solution Overview

```
.agents/
├── plans/              # ALL agent plans (SINGLE SOURCE OF TRUTH)
├── artifacts/          # Work products, screenshots, exports
├── sessions/           # Daily session logs
├── memory/             # Persistent context between sessions
├── workflows/          # Reusable workflow definitions
└── issues/             # Local issue cache (synced with GitHub)
```

---

## Phase 1: Synchronize Existing Plans

### 1.1 Migrate Claude's Plan

| Source                                     | Destination                                          | Size       |
| :----------------------------------------- | :--------------------------------------------------- | :--------- |
| `~/.claude/plans/iterative-jumping-sun.md` | `.agents/plans/comprehensive-transformation-plan.md` | 1236 lines |

**Action**: Replace outdated copy with current version.

### 1.2 Update AGENTS.md Rules

Add to `## 🚨 PRIME DIRECTIVE`:

```markdown
> **RULE #2**: ARTIFACTS MUST LIVE IN `.agents/`
> Never store plans in `~/.claude/`, `~/.gemini/`, or any personal directory.
> If you create a file in your personal space, MOVE IT immediately to `.agents/`.
> Plans created in personal spaces have NO VALUE to the team.

> **RULE #3**: PLANS MUST BE KEPT UP-TO-DATE
> After each phase/step:
>
> 1. Mark completed items [x]
> 2. Update "STATUS UPDATE" section with date + evidence
> 3. Commit the plan update
>    Stale plans are LIES. Don't create them.

> **RULE #4**: VERIFY BEFORE CLAIMING COMPLETE
> Every task must have verification:
>
> - Tests passed (unit/integration/E2E)
> - Manual verification (screenshots, browser check)
> - Commit with evidence
>   Never mark [x] without proof.
```

---

## Phase 2: GitHub Issues Integration

### 2.1 Create Issue Template Structure

```
.github/
├── ISSUE_TEMPLATE/
│   ├── feature.md
│   ├── bug.md
│   └── task.md
└── workflows/
    └── agent-pr-labeling.yml
```

### 2.2 Issue-Driven Workflow

**New Rule for AGENTS.md**:

```markdown
> **RULE #5**: EVERY TASK NEEDS A GITHUB ISSUE
> Before starting any work:
>
> 1. Create or find the GitHub Issue
> 2. Reference issue in your branch: `agent/gemini/123-feature-name`
> 3. Reference issue in commits: `feat: add X (fixes #123)`
> 4. Close issue via PR merge

> **RULE #6**: DECOMPOSE LARGE TASKS
> If estimated time > 2 hours:
>
> 1. Create parent issue with checklist
> 2. Create child issues for each sub-task
> 3. Link children to parent
```

### 2.3 PR Template

```markdown
## Summary

<!-- What does this PR do? -->

## Related Issue

Fixes #XX

## Agent Work

- **Agent**: Claude/Gemini/Other
- **Branch**: agent/xxx/...
- **Session**: .agents/sessions/YYYY-MM-DD-xxx.md

## Verification

- [ ] Tests pass (`npm test`)
- [ ] Manual verification (describe)
- [ ] Plan updated with [x] marks
- [ ] Screenshots attached (if UI change)

## Evidence

<!-- Screenshots, test output, etc. -->
```

---

## Phase 3: Verification Enforcement

### 3.1 Pre-Commit Checklist Workflow

Create `.agents/workflows/verify-before-complete.md`:

````markdown
# Verification Workflow

// turbo-all

Before marking ANY task complete:

1. Run all tests:

```bash
npm test
```
````

2. Run type check:

```bash
npm run typecheck
```

3. Run linter:

```bash
npm run lint
```

4. If UI changes, take screenshots:

```bash
# Manual: Open browser, capture evidence
```

5. Update plan with [x] and evidence link

6. Commit with verification message:

```bash
git add -A
git commit -m "feat: complete X - verified (fixes #123)"
```

````

### 3.2 Test Discovery

**Current test setup** (to be verified):
- Framework: Unknown (need to check package.json)
- Coverage: Unknown

**Action**: Check existing test infrastructure before proposing new tests.

---

## Phase 4: Codebase Cleanup

### 4.1 Identify Redundant Directories

Based on tree analysis, candidates for cleanup:

| Directory | Status | Action |
|:----------|:-------|:-------|
| `archive/legacy_structure/` | Legacy | Review and delete |
| `legacy/archive_v1/` | Old code | Archive or delete |
| `docs/testing/` | Old test artifacts | Move to `.agents/artifacts/` |
| Multiple plan locations | Scattered | Consolidate to `.agents/plans/` |

### 4.2 Documentation Consolidation

Scattered docs need routing:
- `docs/project/plans/` → Move to `.agents/plans/`
- `docs/agents/` → Consolidate with `.agents/`
- `docs/reports/` → Move to `.agents/artifacts/reports/`

---

## Phase 5: Session Management

### 5.1 Session Start Workflow (Update)

Update `.agents/workflows/git-session-start.md`:

```markdown
# Session Start

// turbo-all

1. Pull latest:
```bash
git checkout main && git pull
````

2. Create branch (with issue ref):

```bash
git checkout -b agent/<name>/<issue#>-<task>
```

3. Check for existing plans:

```bash
ls -la .agents/plans/
```

4. Read active plan and find your section:

```bash
cat .agents/plans/comprehensive-transformation-plan.md | head -100
```

5. Create session log:

```bash
echo "# Session: $(date +%Y-%m-%d)" > .agents/sessions/$(date +%Y-%m-%d)-<agent>-<task>.md
```

````

### 5.2 Session End Workflow

Create `.agents/workflows/git-session-end.md`:

```markdown
# Session End

// turbo

1. Run tests:
```bash
npm test
````

2. Update plan with completed items

3. Commit all changes:

```bash
git add -A
git commit -m "feat: session summary (fixes #XX)"
```

4. Push branch:

```bash
git push origin <branch>
```

5. Notify Omar for PR review

````

---

## Verification Plan

### Automated Tests

**Discover existing tests**:
```bash
npm test --if-present
cat package.json | grep -A5 '"scripts"'
````

### Manual Verification

1. **Verify plan sync**: Check that `.agents/plans/comprehensive-transformation-plan.md` matches Claude's latest
2. **Verify AGENTS.md rules**: Read file and confirm all 6 rules are present
3. **Verify workflows exist**: `ls .agents/workflows/`
4. **Test git workflow**: Create test branch, run session-start workflow

---

## Implementation Steps

1. [ ] Sync Claude's plan → `.agents/plans/comprehensive-transformation-plan.md`
2. [ ] Add RULES #2-#6 to `AGENTS.md`
3. [ ] Create `.github/ISSUE_TEMPLATE/` structure
4. [ ] Create `.github/PULL_REQUEST_TEMPLATE.md`
5. [ ] Update `git-session-start.md` workflow
6. [ ] Create `git-session-end.md` workflow
7. [ ] Create `verify-before-complete.md` workflow
8. [ ] Document cleanup candidates in `.agents/plans/codebase-cleanup-plan.md`
9. [ ] Commit all changes
10. [ ] Create GitHub Issue for codebase cleanup (use new workflow)

---

## Success Criteria

- [ ] ALL agent plans in `.agents/plans/` (none in personal dirs)
- [ ] Plans have STATUS UPDATE sections with dates
- [ ] GitHub Issue template exists and works
- [ ] PR template enforces verification
- [ ] Workflows are executable (turbo-all enabled)
- [ ] Next agent session follows new workflow

# Implementation Plan: Git Branching Strategy for Multi-Agent Workflow

> **Goal**: Clean up old branches and establish a workflow where each agent/session works on its own branch to avoid conflicts.
> **Status**: Draft

## 1. Branch Cleanup

### Current State

| Branch           | Status                         |
| :--------------- | :----------------------------- |
| `main`           | ✅ Active (9e263bb)            |
| `origin/develop` | ⚠️ Obsolete (merged into main) |

### Action: Delete `develop`

```bash
git push origin --delete develop
```

## 2. Multi-Agent Branching Strategy

### Problem

- Multiple agents (Claude, Gemini, Cursor) work in parallel
- They modify the same files simultaneously
- Result: Merge conflicts, overwritten work, chaos

### Proposed Solution: Agent Session Branches

```
main
├── agent/gemini/2026-01-29-expedia-onboarding
├── agent/claude/2026-01-29-pricing-review
└── agent/cursor/2026-01-29-ui-fixes
```

### Naming Convention

```
agent/<agent-name>/<YYYY-MM-DD>-<task-name>
```

### Workflow Rules

1. **Before Starting Work**:

   ```bash
   git checkout main
   git pull origin main
   git checkout -b agent/<name>/<date>-<task>
   ```

2. **During Work**:
   - Agent works exclusively on its branch
   - Regular commits with descriptive messages

3. **After Work**:
   - Agent creates PR or notifies Omar
   - Omar reviews and merges into `main`
   - Branch is deleted after merge

### Agent Configuration Updates

#### AGENTS.md Addition

```markdown
## Git Workflow

**Before starting ANY task:**

1. `git checkout main && git pull`
2. `git checkout -b agent/<your-name>/<date>-<task>`

**After completing work:**

1. `git push origin <branch-name>`
2. Notify Omar for review
3. Wait for merge before starting new work on same files
```

## 3. Implementation Steps

1. [x] Delete `origin/develop` branch
2. [x] Update `AGENTS.md` with RULE #0 (mandatory branching)
3. [x] Update `GEMINI.md` with git workflow
4. [x] Update `CLAUDE.md` with git workflow
5. [x] Create `.agents/workflows/git-session-start.md`

## 4. Verification Plan

### Manual Verification

- Omar confirms branch deletion
- Omar approves the workflow rules
- Next agent session follows the new workflow

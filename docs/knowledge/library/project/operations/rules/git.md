# Git Workflow Rules

> **Purpose**: Enforce professional Git/GitHub/Linear workflow for all agents
> **Last Updated**: 2026-01-30 (Phase 1 + Phase 2 Complete)
> **MANDATORY**: All agents MUST follow this workflow without exception

---

## PRIME DIRECTIVE: Create Branch Before Work

> **RULE #0**: CREATE A BRANCH BEFORE ANY WORK.
>
> ```bash
> git checkout main && git pull origin main
> git checkout -b agent/<your-name>/<date>-<task>
> ```
>
> **NO EXCEPTIONS.**

**Why**: Prevents conflicts between agents working simultaneously.

## 🚨 RULE #1: NEVER Work Directly on Main

**FORBIDDEN**:
```bash
git checkout main
# ... make changes ...
git commit -m "changes"  # ❌ NEVER DO THIS
```

**REQUIRED**:
```bash
git checkout main
git pull origin main
git checkout -b agent/<name>/<date>-<task>
# ... make changes ...
git commit -m "feat: changes"
git push -u origin agent/<name>/<date>-<task>
# Create PR (see Rule #4)
```

**Rationale**: Direct commits to main bypass review, break CI/CD, and create merge conflicts.

---

## 🚨 RULE #2: Always Create Branch Before Work

**Branch Naming Convention**:
```
agent/<agent-name>/<YYYY-MM-DD>-<task-slug>
```

**Examples**:
- `agent/claude/2026-01-30-phase2-linear-migration`
- `agent/gemini/2026-01-31-ota-integration`
- `agent/cursor/2026-02-01-room-pricing`

**Include Linear Issue ID** (when applicable):
```
agent/<name>/<date>-LIN-<issue-id>
```
- `agent/claude/2026-02-01-LIN-134`
- `agent/gemini/2026-02-02-LIN-145`

**Verification**:
```bash
# At session start, verify you're on a branch
git branch --show-current

# If on main, STOP and create branch
if [ "$(git branch --show-current)" = "main" ]; then
  echo "ERROR: Cannot work on main directly!"
  exit 1
fi
```

---

## 🚨 RULE #3: Atomic Commits (Not One Giant Commit)

**BAD** (One big commit):
```bash
git add -A
git commit -m "feat: add everything"  # ❌ 500+ files changed
```

**GOOD** (Atomic commits):
```bash
# Commit 1: Enforcement
git add AGENTS.md .agents/rules/workspace.md
git commit -m "feat(phase2.5): enforce Linear-first workflow"

# Commit 2: Migration
git add .agents/artifacts/archive/
git commit -m "feat(phase2.3): archive migrated task files"

# Commit 3: Verification
git add ops/scripts/verify-migration.sh
git commit -m "feat(phase2.4): add migration verification script"
```

**Atomic Commit Principles**:
1. **One logical change per commit** (feature, fix, docs, cleanup)
2. **Independent commits** (each can be reverted without breaking others)
3. **Clear commit messages** (conventional commits format)
4. **Focused diffs** (easy to review)

**Conventional Commits Format**:
```
<type>(<scope>): <description>

<optional body>

<optional footer>
```

**Types**:
- `feat`: New feature
- `fix`: Bug fix
- `docs`: Documentation only
- `refactor`: Code refactoring
- `test`: Adding tests
- `chore`: Maintenance
- `perf`: Performance improvement
- `ci`: CI/CD changes
- `cleanup`: Code cleanup

**Examples**:
```bash
git commit -m "feat(linear): migrate 29 issues to Linear workspace"
git commit -m "fix(auth): resolve JWT token expiration bug"
git commit -m "docs(readme): update installation instructions"
git commit -m "refactor(pricing): extract rate calculation logic"
git commit -m "cleanup: remove obsolete task files"
```

---

## 🚨 RULE #4: ALWAYS Create Pull Request (Never Direct Merge)

**FORBIDDEN**:
```bash
git checkout main
git merge agent/claude/2026-01-30-my-work  # ❌ NEVER
git push origin main  # ❌ NEVER
```

**REQUIRED**:
```bash
# 1. Push branch
git push -u origin agent/claude/2026-01-30-my-work

# 2. Create PR with comprehensive description
gh pr create \
  --base main \
  --head agent/claude/2026-01-30-my-work \
  --title "Phase 2: Linear Integration - 29 Issues Migrated" \
  --body "$(cat PR-DESCRIPTION.md)"

# 3. Wait for review and approval
# 4. Merge via GitHub UI (or gh pr merge after approval)
```

**Why PRs are Mandatory**:
1. ✅ **Code Review** - Catch bugs, verify completeness
2. ✅ **CI/CD Checks** - Tests, linting, builds must pass
3. ✅ **Documentation** - PR description preserves context
4. ✅ **Audit Trail** - GitHub tracks who approved what
5. ✅ **Rollback Safety** - Easy to revert if issues arise

**Exception**: **NONE**. Even solo developers must use PRs for audit trail and CI/CD.

---

## 🚨 RULE #5: PR Description Must Be Comprehensive

**BAD PR Description**:
```markdown
## Changes
- Fixed stuff
- Updated files
```

**GOOD PR Description** (Template):
```markdown
## What This Does
[1-2 sentence summary]

## Why This Matters
[Business/technical justification]

## Changes Made
- [Specific change 1]
- [Specific change 2]
- [Specific change 3]

## Testing Checklist
- [x] Tests added/updated
- [x] Manual testing completed
- [x] CI/CD passing
- [x] Documentation updated

## Evidence
- Linear Issue: EM-XXX
- Verification: [Link to test output]
- Screenshots: [If UI changes]

## Review Focus
[What reviewers should pay attention to]

## Next Steps (After Merge)
[What happens after this is merged]
```

**Use Template**: `.github/PULL_REQUEST_TEMPLATE.md` (created in Phase 3)

---

## 🚨 RULE #6: Link Linear Issues to PRs

**Every PR MUST reference Linear issue**:

**In PR Title**:
```
feat(EM-134): OTA Progressive Integration
```

**In PR Description**:
```markdown
## Linear Issue
Closes: EM-134
Related: EM-135, EM-136
```

**In Commit Messages**:
```bash
git commit -m "feat(EM-134): activate Expedia integration

Implements step 3 of OTA Progressive Integration epic.
Configures Expedia/Hotels.com channel in HotelRunner.

Closes: EM-134"
```

**Why**:
- ✅ Linear auto-closes issues when PR merges
- ✅ Linear shows commit history for each issue
- ✅ GitHub shows related Linear issues
- ✅ Traceability (code ↔ issue ↔ business requirement)

---

## 🚨 RULE #7: Respect Code Review Feedback

**When reviewer requests changes**:

1. **Acknowledge** - Comment "Working on this now"
2. **Make changes** - Create new commits (don't amend)
3. **Push updates** - `git push` (GitHub auto-updates PR)
4. **Respond** - Comment explaining what changed
5. **Request re-review** - Click "Re-request review" button

**Don't**:
- ❌ Argue without justification
- ❌ Force push (`git push --force`) during review
- ❌ Merge without approval
- ❌ Ignore feedback

**Do**:
- ✅ Ask clarifying questions
- ✅ Provide rationale for disagreement (with evidence)
- ✅ Be respectful and professional
- ✅ Learn from feedback

---

## 🚨 RULE #8: Keep Branches Up to Date

**Before creating PR**:
```bash
# Update from main
git checkout main
git pull origin main
git checkout agent/claude/2026-01-30-my-work
git merge main  # or git rebase main

# Resolve conflicts if any
# Push updated branch
git push
```

**Why**: Prevents merge conflicts, ensures CI runs with latest main

---

## 🚨 RULE #9: Delete Branch After Merge

**After PR is merged**:
```bash
# Delete local branch
git branch -d agent/claude/2026-01-30-my-work

# Delete remote branch (GitHub auto-deletes, but verify)
git push origin --delete agent/claude/2026-01-30-my-work

# Update main
git checkout main
git pull origin main
```

**Why**: Keeps repository clean, prevents confusion

---

## 🚨 RULE #10: Never Commit Secrets or Sensitive Data

**FORBIDDEN**:
- ❌ API keys, tokens, passwords in code
- ❌ `.env` files with real credentials
- ❌ Private keys, certificates
- ❌ Customer data, PII
- ❌ Internal URLs, IPs (if sensitive)

**REQUIRED**:
- ✅ Use `.env.example` templates (with placeholders)
- ✅ Store secrets in `.secrets/.env` (gitignored)
- ✅ Use environment variables at runtime
- ✅ Scan commits before push (`git diff --cached`)

**Pre-commit Hook** (enforces this):
- Blocks commits with API key patterns
- Warns about `.env` files
- Scans for common secret formats

---

## Multi-Agent Coordination

### When Multiple Agents Work on Same Repo

**Scenario**: Claude and Gemini both working on Villa Thaifa

**Rules**:
1. **Separate branches** - Never share a branch
   - Claude: `agent/claude/2026-01-30-task-a`
   - Gemini: `agent/gemini/2026-01-30-task-b`

2. **Communicate** - Use Linear comments or GitHub PR comments
   - Tag other agent: "@agent-gemini FYI, I'm modifying X"

3. **Coordinate merges** - Don't merge conflicting PRs simultaneously
   - Use PR labels: `needs-coordination`, `blocks-pr-X`

4. **Rebase if needed** - If main changes while working
   ```bash
   git fetch origin
   git rebase origin/main
   git push --force-with-lease  # Safe force push
   ```

5. **Session handoffs** - Leave clear notes
   - Use `.agents/sessions/YYYY-MM-DD-session-name.md`
   - Document: what was done, what's pending, blockers

---

## Workflow Summary (Quick Reference)

```bash
# 1. Start session
git checkout main
git pull origin main
git checkout -b agent/claude/2026-01-30-LIN-134

# 2. Work and commit atomically
# ... make changes ...
git add file1.ts file2.ts
git commit -m "feat(EM-134): implement feature X"

# ... more changes ...
git add file3.md
git commit -m "docs(EM-134): update documentation"

# 3. Push and create PR
git push -u origin agent/claude/2026-01-30-LIN-134
gh pr create --base main --head agent/claude/2026-01-30-LIN-134 \
  --title "feat(EM-134): Feature X Implementation" \
  --body "Closes: EM-134\n\n[Comprehensive description]"

# 4. Address review feedback
# ... make requested changes ...
git add .
git commit -m "fix(EM-134): address review feedback"
git push

# 5. After PR merged
git checkout main
git pull origin main
git branch -d agent/claude/2026-01-30-LIN-134
```

---

## Enforcement

### Pre-Commit Hook

**Location**: `.git/hooks/pre-commit`

**Checks**:
- [ ] Not on main branch
- [ ] No secrets in staged files
- [ ] No task files outside archive (Linear-first)
- [ ] Conventional commit format

### Pre-Push Hook (Future)

**Location**: `.git/hooks/pre-push`

**Checks**:
- [ ] Branch name follows convention
- [ ] All commits have Linear issue reference
- [ ] No direct push to main

### CI/CD Checks (GitHub Actions)

**Location**: `.github/workflows/ci.yml`

**Runs on PR**:
- [ ] Tests pass
- [ ] Linting passes
- [ ] Build succeeds
- [ ] No secrets detected
- [ ] Branch name valid
- [ ] Linear issue referenced

---

## Common Mistakes (and How to Avoid Them)

### Mistake 1: Working on Main

**Symptom**: `git branch --show-current` returns "main"

**Fix**:
```bash
# If no changes yet
git checkout -b agent/claude/2026-01-30-task

# If already made changes
git stash
git checkout -b agent/claude/2026-01-30-task
git stash pop
```

### Mistake 2: One Giant Commit

**Symptom**: `git diff --cached` shows 50+ files

**Fix**:
```bash
# Unstage everything
git reset

# Stage and commit atomically
git add file1 file2
git commit -m "feat: logical change 1"

git add file3 file4
git commit -m "docs: logical change 2"
```

### Mistake 3: Force Push During Review

**Symptom**: Reviewer's comments disappear

**Fix**: **Never use `git push --force` during review**. Use `git push --force-with-lease` ONLY when rebasing after coordination.

### Mistake 4: Merge Conflicts

**Symptom**: `git merge main` shows conflicts

**Fix**:
```bash
# 1. Open conflicting files
# 2. Resolve conflicts (search for <<<<<<< markers)
# 3. Mark as resolved
git add resolved-file.ts

# 4. Complete merge
git commit  # (no -m, will use merge message)

# 5. Push
git push
```

---

## Verification Checklist (Before Pushing)

- [ ] On feature branch (not main)
- [ ] Linear issue exists for this work
- [ ] Atomic commits (one logical change each)
- [ ] Conventional commit messages
- [ ] No secrets in staged files
- [ ] Tests added/updated (if applicable)
- [ ] Documentation updated (if applicable)
- [ ] Branch name includes Linear ID (if applicable)
- [ ] Ready to create comprehensive PR description

---

## Branch Naming Convention (Alternative Format)

```
agent/<agent-name>/<YYYY-MM-DD>-<task-name>
```

**Examples:**

- `agent/gemini/2026-01-29-expedia-onboarding`
- `agent/claude/2026-01-30-pricing-review`
- `agent/antigravity/2026-01-31-database-migration`

## Session Start Protocol

```bash
# 1. Start from main
git checkout main
git pull origin main

# 2. Check for unstaged changes
git status

# 3. Create session branch
git checkout -b agent/<name>/<date>-<task>

# 4. Begin work
```

## During Work: Commit After Each Step

> **RULE #5**: COMMIT AFTER EACH PHASE/STEP.

After completing each logical unit of work:

```bash
git add -A
git commit -m "feat(phase-X): step description - VERIFIED"
```

**Commit Message Format:**

```
<type>(<scope>): <description>

[optional body]

[optional footer]
```

**Types:**
- `feat`: New feature
- `fix`: Bug fix
- `refactor`: Code restructuring
- `docs`: Documentation
- `test`: Test additions/updates
- `chore`: Maintenance tasks

**Examples:**

```bash
git commit -m "feat(reservations): add HotelRunner sync - VERIFIED"
git commit -m "fix(pricing): correct currency conversion logic"
git commit -m "docs(api): update HotelRunner integration guide"
```

**Why**: Traceable progress, easy rollback, clear audit trail.

## Session End Protocol

```bash
# 1. Final commit
git add -A
git commit -m "feat: <session summary> - VERIFIED"

# 2. Push branch
git push origin <branch-name>

# 3. Notify Omar for review
# (Via Linear comment, email, or as specified)
```

## Multi-Agent Coordination Rules

### ❌ Never Do This

- Push directly to `main` without review
- Work on the same branch as another agent
- Rebase/force-push on shared branches
- Delete branches without confirmation

### ✅ Always Do This

- Create a new branch for each session
- Wait for merge before working on same files
- Communicate when modifying shared files
- Keep commits atomic and well-described

## Merge Conflicts

If you encounter conflicts:

1. **STOP** - Do not force push
2. Document the conflict in `.agents/sessions/`
3. Notify Omar or wait for guidance
4. Use `git merge main` to integrate changes (not rebase)

## Emergency Rollback

If you need to undo work:

```bash
# Soft reset (keeps changes, uncommits)
git reset --soft HEAD~1

# Hard reset (DESTROYS changes)
git reset --hard HEAD~1  # Use with EXTREME caution
```

**Protocol**: Always create a backup branch before destructive operations:

```bash
git branch backup/<name>-<date>
git reset --hard HEAD~1
```

---

_Created during Phase 1 + Phase 2 (Rules Consolidation + Linear Integration) - 2026-01-30_
_Enforced via: Pre-commit hooks, CI/CD, PR template, code review_

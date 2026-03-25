---
description: Start a new agent session with proper git branching
---

# Git Session Start Workflow

// turbo-all

**MANDATORY**: Every agent session MUST start with these steps.

## Steps

### Before Work

1. Verify you're on main and up to date:

```bash
git checkout main && git pull origin main
```

## 🔀 Git Workflow

> **Create a branch before starting work to avoid conflicts with other agents.**

```bash
git checkout main && git pull
git checkout -b agent/claude/<date>-<task>
```

See `AGENTS.md` for full workflow rules.


### During Work

2. Create your session branch:

```bash
git checkout -b agent/<agent-name>/<YYYY-MM-DD>-<task-name>
```

Replace:

- `<agent-name>`: gemini, claude, codex, etc.
- `<YYYY-MM-DD>`: Today's date
- `<task-name>`: Short kebab-case description

**Example:**

```bash
git checkout -b agent/gemini/2026-01-29-expedia-onboarding
```

### Verification

3. Confirm the branch was created:

```bash
git branch --show-current
```

### After Work

When session ends:

```bash
git add -A
git commit -m "feat: <description>"
git push origin <branch-name>
```

Then notify Omar for review and merge.

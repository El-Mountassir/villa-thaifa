---
description: Close session safely with guardrails preventing premature closure. Use when looking to end of any session
allowed-tools: Read, Bash(git status:*), Bash(git:*), Glob, Write, Edit
argument-hint: [--force]
---

# Purpose

Safely close a work session by enforcing HARD STOP #6: No premature closure. Checks for active missions, undocumented learnings, uncaptured items, uncommitted changes, and CHANGELOG updates.

**Background**: Prevents repeat of 2025-12-21 incident.
See: `LESSONS-LEARNED/2025-12-21-premature-closure.md`

## ZERO TOLERANCE POLICY

> **ALL guardrails are BLOCKING. There are NO warnings.** > **If ANY guardrail fails → FIX IT AUTOMATICALLY before authorizing closure.** > **Don't ask Omar to decide obvious things. Just fix them.**

This is non-negotiable. Every guardrail must PASS or be AUTO-FIXED.

## Variables

FORCE_FLAG: $1

If `--force`: Skip guardrails (requires explicit user acknowledgment of risk).
If empty: Run full guardrail sequence.

---

## Guardrail Order

> **ALL are BLOCKING. Zero tolerance.**

1. **Active Missions State** (BLOCKING)
2. **Session Learnings** (BLOCKING)
3. **Uncaptured Items** (BLOCKING)
4. **Git Status** (BLOCKING)
5. **CHANGELOG** (BLOCKING)

---

## Instructions

### Guardrail 1: Active Missions State (BLOCKING)

```bash
ls missions/active/
```

**If NOT empty**:

- Read each mission file
- If status = `COMPLETED` → Archive automatically
- If status = `ACTIVE` → Ask: complete or document stopping point?

**DO NOT proceed until active/ is empty.**

### Guardrail 2: Session Learnings (BLOCKING)

Scan conversation for:

- Mistakes made and recognized
- New patterns discovered
- Preferences expressed by Omar
- Behaviors to change

**If found and NOT documented** → Document automatically in rules/memory files.

### Guardrail 3: Uncaptured Items (BLOCKING)

Scan conversation for:

- Mentioned tasks not in missions
- "TODO", "later", "should", "need to" statements
- User requests not fully addressed
- Questions asked but not resolved

**If found** → Create missions automatically.

### Guardrail 4: Git Status (BLOCKING)

```bash
git status --porcelain
```

**If NOT empty** → Commit automatically with appropriate message.

### Guardrail 5: CHANGELOG.md (BLOCKING)

If significant changes were made this session:

1. Check if CHANGELOG.md was updated
2. **If NOT updated** → Update it automatically with session changes
3. Commit the CHANGELOG update

**What counts as "significant changes":**

- New features added
- Bug fixes
- Breaking changes
- New rules/standards created
- Template additions
- Any user-facing changes

**Auto-fix format:**

```markdown
## [Unreleased]

### Added

- [description of additions]

### Changed

- [description of changes]

### Fixed

- [description of fixes]
```

**DO NOT proceed until CHANGELOG reflects session work.**

---

## Automatic Fix Principle

> **Every blocker has an automatic fix. Use it.**

| Blocker                      | Automatic Fix               |
| ---------------------------- | --------------------------- |
| Completed mission in active/ | Archive it                  |
| Undocumented learning        | Document in rules/memory    |
| Uncaptured item              | Create mission              |
| Uncommitted changes          | Commit them                 |
| CHANGELOG not updated        | Update with session changes |

**Only ask when the action is genuinely ambiguous.** Most actions are NOT ambiguous.

---

## Output: If Blocked

```
# 🚫 SESSION CLOSURE BLOCKED

> **ZERO TOLERANCE**: All issues must be fixed before closure.

---

## ❌ Failed Guardrails

| # | Guardrail | Status | Auto-Fix |
|---|-----------|--------|----------|
| 1 | Active Missions | ❌ FAIL | → Archiving now... |
| 2 | Uncommitted Changes | ❌ FAIL | → Committing now... |
| 3 | CHANGELOG | ❌ FAIL | → Updating now... |

---

## 🔧 Auto-Fixing...

[Progress indicators as fixes complete]

---

## 🔄 Re-Running Guardrails...

[Must show all ✅ before authorizing]
```

## Output: If Passed

```
# ✅ SESSION CLOSURE AUTHORIZED

> **All guardrails PASSED. Session may be safely closed.**

---

## 🛡️ Guardrails Status

| Guardrail | Status |
|-----------|--------|
| Active Missions | ✅ PASSED |
| Session Learnings | ✅ PASSED |
| Uncaptured Items | ✅ PASSED |
| Git Status | ✅ PASSED |
| CHANGELOG | ✅ PASSED |

---

## 📊 Session Summary

| Metric | Value |
|--------|-------|
| 🗂️ Missions archived | [count] |
| 📝 Learnings documented | [count] |
| 💾 Commits made | [count] |
| 📋 CHANGELOG | ✅ Updated |

---

## 🔮 Next Session

| Info | Value |
|------|-------|
| 📬 Queue depth | **[count]** missions pending |
| 🎯 Recommended | `[mission-name]` |
| ⚡ Priority | [P0/P1/P2] |

---

## 🔒 Git Status: CLEAN

---

> **🚀 GO FOR CLOSURE**
```

---

## Override Protocol

If user provides `--force`:

1. Require explicit confirmation: "I understand items will be lost. Close anyway."
2. Log the override
3. Still attempt to capture what's possible

**Never silently allow premature closure.**

---

## Example

```
/end
```

-> Runs guardrails, auto-fixes blockers, authorizes closure

```
/end --force
```

-> Skips guardrails with explicit acknowledgment (use with caution)

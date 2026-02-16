---
description: Synchronize session learnings to CLAUDE.md for future instances
allowed-tools: Read, Write, Edit
argument-hint: [learning-description]
---

# Purpose

Document session learnings in CLAUDE.md so future Claude instances benefit from discoveries made in this session. Enables collective learning across instances.

## Variables

LEARNING: $ARGUMENTS

If empty: Analyze the session and propose additions automatically.

---

## Instructions

### Step 1: Analyze Session

Identify in the conversation:
- [ ] New rules/conventions established?
- [ ] Errors made and corrected?
- [ ] Workflows created?
- [ ] Important decisions?

### Step 2: Check Existing Content

Read `CLAUDE.md` and verify:
- [ ] Info already exists? → Don't duplicate
- [ ] Contradicts existing? → Flag for Omar
- [ ] Appropriate section exists? → Add there

### Step 3: Categorize

| Type | Destination |
|------|-------------|
| Global rule (all projects) | `~/Documents/claude/memory/patterns.md` |
| Project rule | `CLAUDE.md` appropriate section |
| Workflow | `CLAUDE.md` or `docs/workflows/` |
| Error/Lesson | `LESSONS-LEARNED/` |

### Step 4: Update

Add to appropriate file with:
- Date (YYYY-MM-DD)
- Concise description
- Impact/rationale

---

## Output

```
## Sync Complete

**Added to CLAUDE.md**:
- [Section]: [Description]

**Added to memory**:
- [File]: [Description]

**Skipped (already exists)**:
- [Item]
```

---

## Checklist Before Commit

- [ ] No duplication with existing content
- [ ] Correct scoping (global vs project)
- [ ] Concise and actionable
- [ ] Date included

---

## Example

```
/sync "Always use YAML frontmatter in slash commands"
```

→ Adds the rule to appropriate location

```
/sync
```

→ Analyzes session and proposes additions

---
description: Session onboarding: Initialize session by checking active missions and loading context. Use for Beginning of any session
allowed-tools: Read, Glob, Bash(ls:*)
argument-hint: [mission-name]
---

# Purpose

Start a new work session by orienting toward existing work. Checks active missions, queued work, and draft ideas to provide context continuity between sessions.

**CRITICAL**: Enforces Claiming Protocol to prevent multiple instances from working on the same mission.

## Variables

SPECIFIC_MISSION: $1

If empty: Run full onboarding sequence checking all mission directories.

---

## Instructions

### Step 1: Check Active Missions (CRITICAL)

```bash
ls missions/active/
```

**If missions found** (NOT empty):

> **WARNING**: Another instance may be working on this mission.

1. Read each mission file in `active/`
2. Extract: `claimed_at`, `claimed_by`, status, last execution log entry
3. Calculate time since claim
4. Present warning with options:
   - Resume (take over)
   - Work on queue (pick different mission)
   - New initiative

**Conflict rules**:

- If claimed < 24h ago: Recommend working on queue instead
- If claimed > 24h ago: May be abandoned, resuming is reasonable
- Always ask user before claiming an active mission

**If empty**: Continue to step 2.

### Step 2: Check Queued Missions

```bash
ls missions/queue/
```

**If missions found**:

- List by priority (from YAML frontmatter)
- Present: "These missions are ready. Which to start?"

**To claim a mission**:

1. Move file: `mv missions/queue/{mission}.md missions/active/`
2. Update YAML: Set `status: ACTIVE`, add `claimed_at`, `claimed_by`
3. Log: Add "CLAIMED" as first execution entry
4. Begin work

**If empty**: Continue to step 3.

### Step 3: Check Draft Missions

```bash
ls missions/drafts/
```

**If drafts found**:

- Present as options for new work

### Step 4: Display Summary

Present state to user.

### Step 5: Ask User

- "Which mission to work on?"
- "Or describe a new task?"

---

## Claiming Protocol

```
CHECK → MOVE → UPDATE → LOG → WORK
```

**Never work from queue/** - if it's in queue, it's unclaimed.

---

## Output: Empty Active

```
## Session Start

**Active**: 0 missions
**Queue**: [count] mission(s)
**Drafts**: [count] idea(s)

**Recommendation**: [Start Y / New initiative]

Which mission to work on?
```

## Output: Active Mission Found

```
## Active Mission Detected

**Mission**: [mission_id]
**Claimed at**: [timestamp]
**Claimed by**: [session description]
**Time since claim**: [X hours ago]
**Last action**: [from execution log]

This mission appears to be actively worked on by another instance.

**Options**:
1. Resume - Take over this mission
2. Work on queue - Pick a different mission (Recommended if < 24h)
3. New initiative - Start something else

Which option?
```

---

## Example

```
/start
```

-> Displays session summary with all missions categorized

```
/start thaifa-migration
```

-> Directly loads the specified mission context

# Permission Modes Reference

> **Purpose**: Define available permission modes and when to use each.
> **Default**: If omitted, agents use `default` permission mode.

---

## Available Permission Modes

| Mode | Behavior | Risk Level |
|------|----------|------------|
| `default` | Normal permission prompts for all actions | Low |
| `acceptEdits` | Auto-accept file edits, prompt for others | Medium |
| `dontAsk` | Skip most permission prompts | High |
| `plan` | Read-only exploration mode | Low |
| `bypassPermissions` | Full permission bypass | Critical |
| `ignore` | Ignore permission system entirely | Critical |

---

## Mode Details

### default
```yaml
permissionMode: default
```
**Behavior**: Normal permission prompts for file edits, bash commands, etc.

**Use When**: Most agents, standard operation

**Example Agents**: `research-agent`, `explore-agent`

### acceptEdits
```yaml
permissionMode: acceptEdits
```
**Behavior**: Automatically accepts file edit operations without prompting

**Use When**: Trusted modification agents that should edit freely

**Example Agents**: `code-fixer`, `auto-formatter`

**Caution**: Only use for agents you fully trust to make edits

### dontAsk
```yaml
permissionMode: dontAsk
```
**Behavior**: Skips most permission prompts, acts autonomously

**Use When**: Automated pipelines, batch operations

**Example Agents**: `batch-processor`, `automated-fixer`

**Caution**: High trust required, agent acts without confirmation

### plan
```yaml
permissionMode: plan
```
**Behavior**: Read-only exploration mode, cannot make changes

**Use When**: Planning, research, analysis without modification

**Example Agents**: `strategic-planner`, `architecture-analyzer`

**Benefit**: Safe exploration, impossible to accidentally modify

### bypassPermissions
```yaml
permissionMode: bypassPermissions
```
**Behavior**: Completely bypasses the permission system

**Use When**: ONLY with explicit user consent for specific tasks

**Caution**: DANGEROUS - use only when absolutely necessary

### ignore
```yaml
permissionMode: ignore
```
**Behavior**: Ignores permission system entirely

**Use When**: Almost never

**Caution**: MOST DANGEROUS - avoid unless specific requirement

---

## Permission Mode Decision Tree

```
START: What level of autonomy does the agent need?
│
├─► Should explore without changing anything?
│   └─► permissionMode: plan
│
├─► Standard operation with user confirmation?
│   └─► permissionMode: default (or omit field)
│
├─► Needs to edit files freely but confirm other actions?
│   └─► permissionMode: acceptEdits
│
├─► Fully automated, minimal prompts?
│   └─► permissionMode: dontAsk
│       (with caution)
│
└─► Needs to bypass all permissions?
    └─► permissionMode: bypassPermissions
        (ONLY with explicit user consent)
```

---

## Recommended by Role Type

| Role Type (Color) | Recommended Mode | Rationale |
|-------------------|------------------|-----------|
| Creation (red) | default | User should confirm new creations |
| Debugging (orange) | default | User should see findings before fixes |
| Validation (yellow) | plan | Validators should only read, never modify |
| Research (green) | default | Standard prompts appropriate |
| Executive (blue) | plan | Planners explore, don't execute |
| Engineer (purple) | acceptEdits | Engineers need to edit freely |
| Utility (cyan) | default | Standard for helpers |
| Communication (pink) | default | Messages need user confirmation |
| Infrastructure (gray) | dontAsk | Background tasks run autonomously |
| Documentation (white) | acceptEdits | Doc generation needs edit freedom |

---

## Security Guidelines

### Safe Modes (Low Risk)
- `default` — Always safe
- `plan` — Read-only, cannot cause harm

### Elevated Modes (Medium Risk)
- `acceptEdits` — Grant only to trusted edit agents
- `dontAsk` — Grant only to fully automated agents

### Dangerous Modes (High Risk)
- `bypassPermissions` — Requires explicit user consent
- `ignore` — Almost never appropriate

---

## Examples

### Safe Validator
```yaml
name: data-validator
permissionMode: plan
# Can only read and analyze, cannot modify anything
```

### Trusted Editor
```yaml
name: code-formatter
permissionMode: acceptEdits
# Can edit files without prompting, but prompts for bash
```

### Automated Pipeline
```yaml
name: nightly-cleanup
permissionMode: dontAsk
# Runs autonomously without prompts
```

### Standard Agent
```yaml
name: research-assistant
# permissionMode omitted = default
# Normal permission prompts
```

---

## Anti-Patterns

| Anti-Pattern | Why It's Wrong | Correction |
|--------------|----------------|------------|
| `bypassPermissions` for research | Over-privileged | Use `plan` |
| `dontAsk` for user-facing agent | No confirmation | Use `default` |
| `acceptEdits` for validator | Validators shouldn't edit | Use `plan` |
| `ignore` anywhere | Too dangerous | Use specific mode |

---

_Permission Modes Reference — Agent Creation Standards_

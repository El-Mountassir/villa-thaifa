# Agent Creation Standards

> **SSOT for all sub-agent creation standards.**
> Meta-agent MUST read this before creating any agent.

---

## Overview

This standards library defines how to create consistent, well-designed Claude Code sub-agents. Each file has ONE purpose following the pattern: **One Container, One Defining Element, One Purpose**.

## Standards Files

| File | Purpose | When to Read |
|------|---------|--------------|
| [colors.md](colors.md) | Complete color semantic system | Choosing agent color |
| [models.md](models.md) | Model selection decision tree | Choosing agent model |
| [tools.md](tools.md) | Tool selection patterns | Choosing agent tools |
| [descriptions.md](descriptions.md) | Description formulas by role | Writing agent description |
| [permissions.md](permissions.md) | Permission mode reference | Setting permissionMode |
| [agent-team-roster.md](agent-team-roster.md) | Complete team documentation | Planning new agents |

## Templates & Examples

| Resource | Purpose |
|----------|---------|
| [templates/agent.template.md](templates/agent.template.md) | Blank agent template with all fields |
| [examples/creation.example.md](examples/creation.example.md) | Example: Creation agent (red) |
| [examples/research.example.md](examples/research.example.md) | Example: Research agent (green) |
| [examples/validation.example.md](examples/validation.example.md) | Example: Validation agent (yellow) |

---

## Agent Creation Workflow

```
1. READ index.md (this file)
       ↓
2. READ colors.md → Select color based on role
       ↓
3. READ models.md → Select minimum capable model
       ↓
4. READ tools.md → Select minimum required tools
       ↓
5. READ descriptions.md → Write action-oriented description
       ↓
6. READ permissions.md → Set permission mode (if needed)
       ↓
7. USE templates/agent.template.md → Fill in all fields
       ↓
8. WRITE agent file to .claude/agents/<name>.md
       ↓
9. UPDATE registry at ai/inventory/sub-agent_registry.md
```

---

## Pre-Creation Checklist

Before writing the agent file, verify:

- [ ] **Name**: kebab-case, descriptive, unique
- [ ] **Color**: Matches role type (see colors.md)
- [ ] **Model**: Minimum capable (see models.md decision tree)
- [ ] **Tools**: Minimum required (see tools.md patterns)
- [ ] **Description**: Has action trigger phrase (see descriptions.md)
- [ ] **Template**: Exactly 4 sections after frontmatter

---

## Quick Reference

### Frontmatter Fields

```yaml
---
name: <kebab-case-name>           # Required
description: <action-oriented>     # Required
tools: <Tool1>, <Tool2>           # Optional (omit = inherit all)
model: <haiku|sonnet|opus|inherit> # Optional (default: configured)
color: <see colors.md>            # Optional (recommended)
permissionMode: <see permissions.md> # Optional (default: default)
skills: <skill1>, <skill2>        # Optional (not inherited)
---
```

### Required Sections (after frontmatter)

1. `# Purpose` — What the agent does
2. `## Instructions` — Guiding principles (bullets)
3. `## Workflow` — Step-by-step process (numbered)
4. `## Report` — Output format specification

---

## Registry Location

After creating an agent, ADD it to:
`/home/omar/el-mountassir/projects/villa-thaifa/ai/inventory/sub-agent_registry.md`

---

_Standards Library — Villa Thaifa Project_

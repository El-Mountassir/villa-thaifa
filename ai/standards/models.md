# Model Selection Guidelines

> **Purpose**: Define when to use each model for optimal cost/performance.
> **Rule**: Always use the MINIMUM model capable of the task.

---

## Model Reference

| Model       | Complexity   | Token Budget | Speed   | Cost    |
|-------------|--------------|--------------|---------|---------|
| **haiku**   | Non → Low    | Minimal      | Fastest | Lowest  |
| **sonnet**  | Low → Mid    | Moderate     | Fast    | Medium  |
| **opus**    | Mid → High   | Large        | Slower  | Highest |
| **inherit** | Varies       | Parent's     | Varies  | Varies  |

---

## Decision Tree

```
START: What does the agent need to do?
│
├─► Simple lookups, formatting, transforms?
│   └─► Use HAIKU
│
├─► Structured analysis, browser automation, moderate reasoning?
│   └─► Use SONNET
│
├─► Complex reasoning, generation, multi-step planning?
│   └─► Use OPUS
│
└─► Should adapt to conversation context?
    └─► Use INHERIT
```

---

## Use Case Matrix

### Haiku (Fastest, Cheapest)

| Use Case | Example |
|----------|---------|
| Simple web searches | research-agent basic queries |
| Text formatting | converter, formatter |
| Data lookups | config reader |
| Simple summarization | quick summaries |
| Pattern matching | file finder |

```yaml
model: haiku
# Good for: explore-agent, simple research-agent
```

### Sonnet (Balanced)

| Use Case | Example |
|----------|---------|
| Browser automation | browser-agent |
| Structured validation | platform-validator |
| Moderate code analysis | basic code-reviewer |
| Form processing | data entry automation |
| Multi-step workflows | sequential task agents |

```yaml
model: sonnet
# Good for: browser-agent, platform-validator
```

### Opus (Most Capable)

| Use Case | Example |
|----------|---------|
| Complex reasoning | strategic-planner |
| Code generation | implementer |
| Agent creation | meta-agent |
| Report generation | report-generator |
| Architecture decisions | system-designer |

```yaml
model: opus
# Good for: meta-agent, claude-md-agent, complex planners
```

### Inherit (Context-Adaptive)

| Use Case | Example |
|----------|---------|
| Sub-tasks of parent | child agents |
| Consistency needed | related agent chains |
| User-selected model | respecting user preference |

```yaml
model: inherit
# Good for: agents that should match parent context
```

---

## Cost Optimization Rules

1. **Start with Haiku** — Default assumption
2. **Escalate only when needed** — Prove haiku can't do it
3. **Never over-provision** — Don't use opus for simple tasks
4. **Use inherit for flexibility** — Let parent context decide

---

## Model + Role Type Suggestions

| Role Type (Color) | Recommended Model | Rationale |
|-------------------|-------------------|-----------|
| Creation (red) | opus | Generates complex configurations |
| Debugging (orange) | sonnet | Structured analysis |
| Validation (yellow) | sonnet | Rule-based checking |
| Research (green) | haiku | Simple web queries |
| Executive (blue) | opus | Complex decisions |
| Engineer (purple) | opus/sonnet | Depends on task complexity |
| Utility (cyan) | haiku | Simple transformations |
| Communication (pink) | haiku | Message formatting |
| Infrastructure (gray) | haiku | Background tasks |
| Documentation (white) | sonnet/opus | Depends on complexity |

---

## Anti-Patterns

| Anti-Pattern | Why It's Wrong | Correction |
|--------------|----------------|------------|
| Opus for file search | Overkill | Use haiku |
| Haiku for agent creation | Insufficient | Use opus |
| Sonnet for simple formatting | Wasteful | Use haiku |
| Fixed model when context varies | Inflexible | Use inherit |

---

_Model Selection Guidelines — Agent Creation Standards_

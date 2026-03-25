# Synthesis Notes

**Date**: 2025-12-21

## Integration Strategy

The patterns converge into a **3-step decision framework**:

```
Step 1: WORK TYPE → Project | Process | Request
Step 2: ITERATION FREQUENCY → Daily/Weekly | Bi-weekly | Stable
Step 3: CONSTRAINTS → Compliance needs | Team size | Hybrid requirements
```

This replaces industry-label matching with characteristic-based selection.

### Framework Logic

```
IF work_type = Request AND frequency = Daily
   → IT Support / Service Desk template

ELIF work_type = Process AND frequency = Weekly
   → Operations / Kanban template

ELIF work_type = Project AND frequency = Bi-weekly
   → Software Dev (Agile) / Scrum template

ELIF work_type = Project AND frequency = Stable
   → Project Management (Waterfall) template

ELIF hybrid = true
   → Start with dominant type, customize
```

### Industry Overlay (Not Primary)

After characteristic-based selection, industry context adds nuances:

| Industry     | Typical Work Type   | Common Constraint       | Template Adjustment |
| ------------ | ------------------- | ----------------------- | ------------------- |
| Software     | Project (Agile)     | Technical debt tracking | Add bug/issue views |
| Marketing    | Project + Process   | Campaign calendars      | Add timeline views  |
| Hospitality  | Process + Request   | Multi-department        | Add Kanban + queues |
| Construction | Project (Waterfall) | Compliance              | Add Gantt + docs    |
| Support      | Request             | SLA tracking            | Add priority queues |

---

## Uncertainties

### High Uncertainty

- **Migration costs**: No sources quantified effort to switch templates after initial setup
- **Team size thresholds**: Unclear when simple tools (Trello) become insufficient vs enterprise (Jira)

### Medium Uncertainty

- **Multi-project complexity**: Single template may not serve portfolio management needs
- **Cross-tool scenarios**: When do sync/integration costs exceed single-tool compromise?

### Low Uncertainty (High Confidence)

- Methodology fit > tool features
- Trial approach reduces selection risk
- Pilot before scale

---

## Failure Modes

### Selection Phase

1. **Analysis paralysis**: Fear of wrong choice delays any adoption → Mitigate with "pick and iterate" mindset
2. **Stakeholder override**: Executive mandates tool without workflow analysis → Mitigate with pilot data

### Implementation Phase

3. **Template rigidity**: Team forces work into template instead of customizing → Mitigate with early customization training
4. **Adoption failure**: Tool deployed but not used → Mitigate with "import real project" trials
5. **Multi-template chaos**: Each team uses different tool → Mitigate with organization-level tool decision, team-level template freedom

### Evolution Phase

6. **Outgrown tool**: Needs exceed tool capabilities → Mitigate with annual review cadence
7. **Template drift**: Customizations make template unrecognizable → Mitigate with documentation of changes

---

## Draft Structure for Final Deliverable

```markdown
# PM Template Selection Guide

## Quick Decision (30 seconds)

- Decision tree with 3 questions

## Full Framework (5 minutes)

1. Identify Work Type
2. Assess Iteration Frequency
3. Apply Constraints
4. Select Template Family
5. Trial & Validate

## Template Deep-Dives

- When to use each (with anti-patterns)

## Industry Considerations

- Hospitality-specific section
- Other common industries

## Implementation Playbook

- Trial approach
- Pilot strategy
- Adoption metrics

## Sources
```

---

## Quality Pre-Check

| Criterion                             | Status                                              |
| ------------------------------------- | --------------------------------------------------- |
| Works for different instances?        | Yes (industry-agnostic framework)                   |
| Key patterns validated by 2+ sources? | Yes (8/8 patterns)                                  |
| Every section earning its tokens?     | Will verify in final                                |
| Beyond obvious/baseline?              | Yes (anti-patterns, failure modes, hybrid handling) |

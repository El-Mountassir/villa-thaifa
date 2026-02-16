---
allowed-tools: Bash(git ls-files:\*), Read, Write
description: Transform Rough Ideas into Rigorous Outputs
argument-hint: [idea/draft/request]
model: opus
---

# Purpose

Elevate a rough idea/draft/request through multi-source triangulation into something research-backed and genuinely reusable.

## Variables

IDEA_DRAFT : $1

If no arguments: User will provide the rough idea/draft/request in the conversation context.

---

## Output Directory

**Path:** `archive/YYYY/QQ/reports/topic-slug/`

### Directory Structure

```
archive/2025/Q4/reports/
└── topic-slug/
    ├── step-back.md     # Phase 0 output
    ├── sources.md       # Phase 1 sources & analysis
    ├── patterns.md      # Phase 2 pattern extraction
    ├── synthesis.md     # Phase 3 synthesis
    └── final.md         # Final deliverable
```

### Naming Convention

- **Topic slug**: lowercase, hyphens, max 30 chars
- **Quarter**: Q1 (Jan-Mar), Q2 (Apr-Jun), Q3 (Jul-Sep), Q4 (Oct-Dec)
- **Example**: `archive/2025/Q4/reports/error-resilience/`

### Setup (Before Starting)

#### Example

```bash
mkdir -p archive/2025/Q4/reports/topic-slug
```

---

## Calibration Check

First, verify this template is needed:

| Question                                          | If NO → Skip template                   |
| ------------------------------------------------- | --------------------------------------- |
| Is the idea messy/half-formed?                    | Clear idea → just execute               |
| Need validation from multiple sources?            | Single source sufficient → reference it |
| Output must be reusable beyond immediate context? | One-time use → direct execution         |
| Task complexity > 10 min?                         | Trivial task → just do it               |

If skipping: State why and proceed directly. **No directory creation needed.**

---

## Pipeline

### Phase 0: Step-Back

Before diving in, establish:

1. **Actual Problem:** What is REALLY being solved? (Not the surface request)
2. **Success Criteria:** What would a GREAT output look like?
3. **Key Concepts:** What are the domain terms that matter?

**Output → `step-back.md`:**

```markdown
# Step-Back Analysis

**Date**: YYYY-MM-DD
**Request**: [Original request summary]

## Problem Statement

[One sentence]

## Success Criteria

1. [Criterion 1]
2. [Criterion 2]
3. [Criterion 3]

## Domain Concepts

- [Concept 1]: [Definition]
- [Concept 2]: [Definition]
```

---

### Phase 1: Source Triangulation

**Search for 2-3 sources across different types:**

| Type              | What to Look For                             |
| ----------------- | -------------------------------------------- |
| Research/Academic | Papers, studies (high rigor)                 |
| Practitioner      | Blogs, tutorials, case studies (real-world)  |
| Official Docs     | Framework/tool documentation (authoritative) |

**For each source, extract:**

- Key claims/patterns
- Evidence quality (strong/weak/anecdotal)
- Potential biases

**Convergence Analysis:**

- **AGREE** → Validated pattern (high confidence)
- **DISAGREE** → Decision point (surface to user)
- **GAP** → No source covers this (acknowledge uncertainty)

**Output → `sources.md`:**

```markdown
# Source Triangulation

## Sources

### Source 1: [Title]

- **URL**: [link]
- **Type**: Research | Practitioner | Official
- **Key Claims**: [bullets]
- **Evidence Quality**: Strong | Moderate | Weak
- **Potential Bias**: [if any]

### Source 2: [Title]

[...]

## Convergence Analysis

| Pattern | Source 1 | Source 2 | Source 3 | Confidence |
| ------- | -------- | -------- | -------- | ---------- |
| [X]     | AGREE    | AGREE    | GAP      | High       |
| [Y]     | AGREE    | DISAGREE | AGREE    | Medium     |

## Decision Points (Disagreements)

- [List any conflicts requiring user input]
```

---

### Phase 2: Pattern Extraction

Transform instances to principles:

| What I Found       | Why It Works           | Generalizable?  |
| ------------------ | ---------------------- | --------------- |
| [Specific example] | [Underlying principle] | [Yes/No + test] |

**Extraction test:** Would this apply in a completely different context?

**Output → `patterns.md`:**

```markdown
# Pattern Extraction

## Extracted Patterns

### Pattern 1: [Name]

- **Observed In**: [Sources]
- **Underlying Principle**: [Why it works]
- **Generalization Test**: [Would apply in context X?] → Yes/No
- **Confidence**: High | Medium

### Pattern 2: [Name]

[...]

## Anti-Patterns Identified

- [What NOT to do, based on sources]
```

---

### Phase 3: Synthesis

Create the deliverable that:

- Works beyond the immediate use case
- Is richer than any single source
- Acknowledges uncertainty explicitly
- Includes failure modes, not just success paths

**Output → `synthesis.md`:**

```markdown
# Synthesis Notes

## Integration Strategy

[How patterns combine into coherent framework]

## Uncertainties

- [What sources didn't cover]
- [Where confidence is lower]

## Failure Modes

- [What could go wrong]
- [Edge cases]

## Draft Structure

[Outline of final deliverable]
```

---

### Phase 4: Quality Gates

Before delivering, verify:

- [ ] Works for different instances of this problem?
- [ ] Key patterns validated by 2+ sources?
- [ ] Every section earning its tokens?
- [ ] Contains knowledge beyond obvious/training baseline?

**Self-Consistency Check:**

> "If I started from scratch with the same sources, would I reach the same conclusions?"
> If NO → identify divergence, pick stronger path.

---

## Final Output → `final.md`

```markdown
# [Deliverable Title]

**Generated**: YYYY-MM-DD
**Pipeline**: archive/YYYY/QQ/reports/[topic]/

## Summary

[2-3 sentences: what this is, why it matters]

## Key Insights

| Insight     | Confidence  | Sources               |
| ----------- | ----------- | --------------------- |
| [Pattern 1] | High/Medium | [Which sources agree] |
| [Pattern 2] | High/Medium | [Which sources agree] |

## [Main Content]

[The actual deliverable — guide, framework, analysis, etc.]

## Limitations & Gaps

- [What sources didn't cover]
- [Where confidence is lower]

## Sources

- [Source 1](url)
- [Source 2](url)
- [Source 3](url)
```

---

## Anti-Patterns

| Don't                        | Why                 | Do Instead              |
| ---------------------------- | ------------------- | ----------------------- |
| Treat input as specification | Locks wrong framing | "Inspiration, not spec" |
| Over-index on one source     | Confirmation bias   | Require 2+ validation   |
| Instance-only examples       | Not reusable        | Elevate to principles   |
| Pad with generic advice      | Wastes tokens       | Ask "is this obvious?"  |
| Skip disagreement            | Hides decisions     | Surface conflicts       |
| Output only to chat          | Ephemeral, lost     | Save to `archive`       |

---

## Iteration

If quality gates fail:

1. Identify weakest phase
2. Re-run from that phase (update corresponding file)
3. Re-check all gates
4. Update `final.md`

---

## Quick Reference

```bash
# Full pipeline creates:
archive/YYYY/QQ/reports/topic/
├── step-back.md
├── sources.md
├── patterns.md
├── synthesis.md
└── final.md

# Skipped pipeline (calibration = NO):
# No files created, direct execution in chat
```

---

## Related Commands

- `/analyze` - Deep-dive a specific option
- `/decide` - Full decision pipeline
- `/compare` - Side-by-side comparison

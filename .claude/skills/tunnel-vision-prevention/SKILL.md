---
name: tunnel-vision-prevention
description: Prevents AI tunnel vision — the tendency to focus narrowly on immediate targets without context. Triggers on session starts, creation requests, and proposal patterns. Forces systematic context checks before action.
allowed-tools: Read, Grep, Glob
---

# Tunnel Vision Prevention

Systematic intervention against the most common AI failure mode: narrow focus without context.

---

## Purpose

> AIs focus on an immediate target without ever taking a step back, checking context, or considering what precedes or surrounds the request.

This skill interrupts that pattern. Not a gentle reminder — a **systematic intervention**.

---

## Trigger Detection

| Pattern Type        | Examples                                                 |
| ------------------- | -------------------------------------------------------- |
| **Session Context** | Start of session, "Continue from...", "Pick up where..." |
| **Creation**        | "Create a new...", "Let's build...", "Make a..."         |
| **Proposal**        | "Here are options...", "I propose...", "We should..."    |
| **Rush**            | Multiple tasks quickly, immediate response without pause |

---

## Routing

Based on the request, read the appropriate cookbook file:

| If the request involves...                     | Read                    |
| ---------------------------------------------- | ----------------------- |
| Understanding the 8 anti-patterns and counters | `cookbook/taxonomy.md`  |
| Executing the intervention checklist           | `cookbook/checklist.md` |

---

## Quick Reference

### The Quick Check

#### 1. **REARVIEW**

— Did I review what came before?

#### 2. **CONTEXT**

— Do I understand the broader goal?

#### 3. **EXISTING**

— Have I checked for existing work?

#### 4. **TRACKING**

— Is progress being tracked?

#### 5. **LINEAR**

— Have I scanned the Hub?

### Risk Levels

| Context            | Rigor Required       |
| ------------------ | -------------------- |
| Quick question     | Light (mental check) |
| Task execution     | Standard protocol    |
| New creation       | Full checklist       |
| Strategic decision | Maximum rigor        |

### Output Format

```txt
TUNNEL VISION CHECK:
- [x] Previous context reviewed
- [x] Broader goal understood
- [x] Existing work checked
- [ ] Linear scanned
- [x] Progress tracking planned
```

---

## The Protocol (Summary)

**STOP** → Pause. Ask what you might be missing.
**CHECK** → Run the 5-point checklist.
**PROCEED** → Only after checks pass.

For detailed checklist, see `cookbook/checklist.md`.

---

_*"The tunnel is comfortable. The view is limited. Step out."*_

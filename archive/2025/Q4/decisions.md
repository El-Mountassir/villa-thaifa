# Historical — Decisions & Lessons Learned

**Last updated**: 2025-12-20
**Source**: docs/lessons-learned.md + session decisions

---

## [2025-12-19] Scout → Report → Action Pattern

### The Error

Sent message asking client for info **WITHOUT** prior report of what we discovered.

### Impact

Client receives questions without context → impression of lack of mastery.

### Correction

```
1. SCOUT    → Explore, verify feasibility
2. REPORT   → Inform client of discoveries
3. QUESTIONS → Ask for missing info (with context)
4. ACTION   → Execute when everything is clear
```

### Lesson

> Never assume the client knows what we know.
> Always make a report before asking for actions/info.

---

## [2025-12-19] Communication Tone

### The Error

Messages too informal ("tu", casual style) for 60+ year old client.

### Correction

- ✅ Formal address mandatory
- ✅ Respect without corporate rigidity
- ❌ No: "Salut", "tu", casual abbreviations

### Lesson

> Always adapt register to client context.
> When in doubt, opt for the more formal register.

---

## [2025-12-20] Ready-to-Use Deliverables

### The Error

Created `.md` file with metadata when Omar needed `.txt` ready to copy.

### Correction

| Type | Format | Naming |
|------|--------|--------|
| WhatsApp message | `.txt` | `YYYY-MM-DD-message-[subject].txt` |
| Client report | `.pdf` | `report-[subject]-YYYY-MM-DD.pdf` |
| Internal notes | `.md` | Free |

### Lesson

> A client deliverable must be ready to use, not a work document.

---

## [2025-12-20] Booking.com Promotions — Stacking Myth

### The Error

Stated that Booking.com promotions stack (40% + 10% = 50%).

### Reality

Booking.com applies **ONLY** the highest discount, not the sum.

### Impact

Stacking risk was overestimated, but individual 40%+ promotions remained destructive.

### Lesson

> Verify statements with official sources before presenting them as facts.

---

## [2025-12-20] Margin = Net Revenue

### Clarification

Question: Do margins 120-450€ represent net revenue or net profit?

**Omar's answer**: **Net revenue** (after commission, not profit after all costs).

### Impact

Calculations are correct. "Negative margin" = "insufficient revenue to cover target", not necessarily financial loss.

---

## [2025-12-20] State Centralization

### Decision

Create centralized `state/` structure for all state information.

### Chosen Approach

| Decision | Omar's Choice |
|----------|---------------|
| Data migration | **Strict SSOT** — Remove state sections from reports |
| Historical level | **Complete** — Changelogs, dated snapshots |

### Lesson

> Scattered state information creates inconsistencies.
> Centralize in SSOT (Single Source of Truth) as soon as possible.

---

_History of decisions and lessons learned_
_Updated on 2025-12-20_

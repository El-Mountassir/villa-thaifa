# Workflows — CLAUDE.md

> **Domain**: Operational workflows for Villa Thaifa
> **Parent context**: `../../CLAUDE.md` (inherits all project rules)

---

## This Directory

| Workflow | Purpose |
|----------|---------|
| `reservation.md` | Creating reservations on HotelRunner |
| `pricing.md` | Updating tariffs across platforms |
| `guest-communication.md` | Client communication patterns |

---

## Workflow Execution Rules

| Rule | Description |
|------|-------------|
| **Read lessons first** | Always check `../lessons-learned.md` before execution |
| **Platform rules** | Follow `rules/universal/ops/platform/platform-operations.md` |
| **Checkpoint pattern** | Stop at each checkpoint, verify before proceeding |

---

## Pattern: SCOUT → REPORT → QUESTIONS → ACTION

All workflows follow this pattern:

```
1. SCOUT    → Explore, verify feasibility
2. REPORT   → Present discoveries to client/Omar
3. QUESTIONS → Ask for missing info (with context)
4. ACTION   → Execute when everything is clear
```

---

## Before Any Workflow

- [ ] Read workflow file completely
- [ ] Read `../lessons-learned.md`
- [ ] Verify platform credentials are available
- [ ] Confirm confidence > 90% on all inputs

---

_Hierarchical context for docs/workflows/_

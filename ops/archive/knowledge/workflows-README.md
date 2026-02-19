# Workflows

> **Domain**: Operational workflows for Villa Thaifa

## This Directory

| Workflow                 | Purpose                              |
| ------------------------ | ------------------------------------ |
| `reservation.md`         | Creating reservations on HotelRunner |
| `pricing.md`             | Updating tariffs across platforms    |
| `guest-communication.md` | Client communication patterns        |
| `git-session-start.md`   | Starting a new git session           |

## Pattern: SCOUT → REPORT → QUESTIONS → ACTION

All workflows follow this pattern:

```
1. SCOUT    → Explore, verify feasibility
2. REPORT   → Present discoveries to client/Omar
3. QUESTIONS → Ask for missing info (with context)
4. ACTION   → Execute when everything is clear
```

## Workflow Execution Rules

| Rule                   | Description                                                          |
| ---------------------- | -------------------------------------------------------------------- |
| **Read lessons first** | Always check `../lessons-learned.md` before execution                |
| **Platform rules**     | Follow `.agents/rules/universal/ops/platform/platform-operations.md` |
| **Checkpoint pattern** | Stop at each checkpoint, verify before proceeding                    |

## Before Any Workflow

- [ ] Read workflow file completely
- [ ] Read `../lessons-learned.md`
- [ ] Verify platform credentials are available
- [ ] Confirm confidence > 90% on all inputs

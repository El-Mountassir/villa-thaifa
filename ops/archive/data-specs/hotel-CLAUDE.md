# Hotel Configuration — CLAUDE.md

> **Domain**: Room and property configuration for Villa Thaifa
> **Parent context**: `../../../CLAUDE.md` (inherits all project rules)

---

## This Directory

| File       | Purpose                                   |
| ---------- | ----------------------------------------- |
| `rooms.md` | Inventory, pricing, capacities            |

**Note**: Other hotel data was moved to `../../state/` per state management standard:

- Current reservations → [`../../state/current/reservations.md`](../../state/current/reservations.md)
- Planned pricing → [`../../state/planned/pricing.md`](../../state/planned/pricing.md)

---

## Key Rules

| Rule                | Description                                              |
| ------------------- | -------------------------------------------------------- |
| **SSOT**            | This is the Single Source of Truth for hotel data        |
| **No calculation**  | Always use exact values from the platform                |
| **Backup first**    | Before modification, create a backup in `archive/`       |

---

## Data Integrity

Before modifying any file in this directory:

1. **Verify source** — Does data come from HotelRunner or Booking.com?
2. **Create baseline** — `cp file.md archive/YYYY/QQ/snapshots/file-YYYY-MM-DD.md`
3. **Validate after** — Cross-check with the platform

---

_*Hierarchical context for data/specs/configs/hotel/*_

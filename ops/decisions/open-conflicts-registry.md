# Open Conflicts Registry

> **Purpose**: Single registry of all known data conflicts requiring human resolution.
> Agents: check this file before resolving ambiguous data. If a conflict is listed here, do NOT guess — escalate.

---

## Active Conflicts

### 1. Pets Policy
- **Source A**: `data/property/property-config.json` → "Allowed, no extra charge"
- **Source B**: `context/meta/knowledge/booking-com-data.md` → "Not allowed"
- **Source C**: Expedia Step 4 extraction → "No" (pets not allowed)
- **Resolution needed**: Said confirmation
- **Label**: Awaiting: Said
- **Impact**: Guest-facing policy on all OTAs

### 2. R06 Terrace Size
- **Source A**: `data/rooms/rooms.md` → 100 m2
- **Source B**: Said's handwritten notes (archived) → ~120 m2
- **Resolution needed**: Physical measurement or Said confirmation
- **Label**: Awaiting: Said

### 3. R07 Terrace Size
- **Source A**: `data/rooms/rooms.md` → 60 m2
- **Source B**: Said's handwritten notes (archived) → 80-100 m2
- **Resolution needed**: Physical measurement or Said confirmation
- **Label**: Awaiting: Said


---

## Resolved Conflicts (Log)

| Date | Conflict | Resolution | Source |
|------|----------|------------|--------|
| 2026-02-21 | Check-out time (11:00 vs 13:30) | 12:00 (Omar decision) | Expedia Step 3 Q&A |
| 2026-02-21 | VAT treatment (inclusive vs exclusive) | Exclusive / HT (Said confirmed) | Expedia Step 3 Q&A |
| 2026-02-21 | Smoking Policy | Designated smoking areas | Expedia Step 4 extraction |

---

_Registry created: 2026-02-21. Update this file whenever a new conflict is discovered or resolved._

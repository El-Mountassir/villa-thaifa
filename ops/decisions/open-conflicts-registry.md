# Open Conflicts Registry

> **Purpose**: Single registry of all known data conflicts requiring human resolution.
> Agents: check this file before resolving ambiguous data. If a conflict is listed here, do NOT guess — escalate.
> All Said-blocked conflicts are also tracked in: `data/admin/said-pending-questions.md §1`

---

## Active Conflicts

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


### 4. Tech Stack for VT App
- **Option A**: json-render abstraction layer (evaluated 2026-02-21)
- **Option B**: Direct Next.js + Tailwind + shadcn/ui (no abstraction)
- **Resolution**: json-render **REJECTED** — too immature, poor DX, no ecosystem. Direct stack chosen.
- **Decision record**: `ops/decisions/json-render-evaluation.md`
- **Label**: Resolved (2026-02-21)

### 5. VT App Build Approach
- **Option A**: Start building immediately with chosen stack
- **Option B**: Vision-first — create PRD, SRS, architecture docs before any code
- **Resolution**: Option B chosen. Vision seed created at `context/meta/planning/vt-app-vision.md`. PRD/SRS/architecture docs required before build begins.
- **Note**: IndyDevDan approach (AI-native dev workflow) still to be integrated into tech stack decision — stack NOT finalized.
- **Label**: In Progress

---

## Resolved Conflicts (Log)

| Date | Conflict | Resolution | Source |
|------|----------|------------|--------|
| 2026-02-21 | Check-out time (11:00 vs 13:30) | 12:00 (Omar decision) | Expedia Step 3 Q&A |
| 2026-02-21 | VAT treatment (inclusive vs exclusive) | Exclusive / HT (Said confirmed) | Expedia Step 3 Q&A |
| 2026-02-21 | Smoking Policy | Designated smoking areas | Expedia Step 4 extraction |
| 2026-02-21 | Pets policy (C1) — Allowed vs Not allowed | Not allowed — confirmed by Omar 2026-02-21, corroborated by Booking.com and Expedia Step 4 data | Omar confirmation 2026-02-21 |
| 2026-02-21 | Tech stack: json-render vs direct Next.js | json-render REJECTED — direct Next.js + Tailwind + shadcn/ui chosen | ops/decisions/json-render-evaluation.md |

---

_Registry created: 2026-02-21. Update this file whenever a new conflict is discovered or resolved._

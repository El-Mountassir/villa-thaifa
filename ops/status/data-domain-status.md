# Data Domain Status — Post Phase A Consolidation

**Last Updated**: 2026-02-16
**Phase**: Phase A Complete (Room consolidation)
**Next Phase**: Finance data population and pricing workflow

---

## Canonical Sources (Active)

### Property Core

- **Property configuration**: `data/property/property-config.json`

### Rooms Domain

- **Master table & profiles**: `data/rooms/rooms.md` (12 rooms: R01–R12)
- **Reconciliation log**: `data/rooms/rooms-reconciliation-log.md`
- **Individual profiles**: `data/rooms/R01/profile.md` through `data/rooms/R12/profile.md`
- **Support files**:
  - `data/rooms/amenities.md`
  - `data/rooms/beds.md`

### Facilities Domain

- `data/property/facilities/garden.md`
- `data/property/facilities/hall-reception.md`
- `data/property/facilities/pool.md`
- `data/property/facilities/services.md`
- `data/property/facilities/spa-hammam.md`

### Bookings Domain

- **Exports**: `data/bookings/exports/` (Trip.com GDA, initial scan JSON)
- **Requests**: `data/bookings/requests/` (guest inquiries, correspondence)
- **Reservations**: `data/bookings/reservations/reservations.md`

### Operations Domain

- `data/operations/channels.json` (OTA channel config)
- `data/operations/check-in-out.json` (procedures)
- `data/operations/emergency.json` (contacts)
- `data/operations/housekeeping.json` (schedules)
- `data/operations/maintenance.json` (logs)

### Finance Domain

- `data/finance/rates.json` (structure ready, data pending)
- `data/finance/billing.json` (structure ready, data pending)

---

## Pending Actions

### Finance Data Population

- **Status**: Schema defined, data awaiting import
- **Files**: `data/finance/rates.json`, `data/finance/billing.json`
- **Next**: Import actual rates and billing config from Booking.com/Expedia/owner records

### Pricing Workflow

- **Status**: Not yet implemented
- **Scope**: Dynamic pricing rules, seasonal adjustments, occupancy-based logic
- **Dependency**: Finance data population must complete first

---

## Archived/Reference Material

### Legacy Sources (Read-Only)

- `context/` — Architecture, planning, audits (historical reference)

### Pending Triage

- `data/pending-domains/` — Unprocessed inventory items (amenities, facilities, beds pending verification)
- `data/archive/` — Older exports and deprecated files

### Backups

- `data/rooms/backups/` — Pre-consolidation room data snapshots

---

## Phase A Completion Summary

✅ **Completed**:

- Room master table consolidated (`data/rooms/rooms.md`)
- 12 individual room profiles migrated (`data/rooms/R01/` through `R12/`)
- Reconciliation log established
- Facilities migrated to `data/property/facilities/`
- Operations domain structured in `data/operations/`
- Bookings organized in `data/bookings/`
- Property config established at `data/property/property-config.json`

⏳ **In Progress**:

- Finance data population
- Pricing workflow design

🔜 **Next**:

- Complete finance domain
- Test validation scripts against new structure
- Merge `bootstrap/2026-02-13-baseline` → `main`

---

## Directory Structure Reference

```
data/
├── rooms/                    # Room inventory (canonical)
│   ├── rooms.md
│   ├── rooms-reconciliation-log.md
│   ├── amenities.md
│   ├── beds.md
│   ├── R01/ through R12/    # Individual room profiles
├── property/
│   ├── property-config.json
│   └── facilities/          # Garden, pool, spa, services
├── bookings/
│   ├── exports/
│   ├── requests/
│   └── reservations/
├── operations/              # Channels, check-in/out, housekeeping, etc.
├── finance/                 # Rates, billing (schema ready, data pending)
├── pending-domains/         # Unverified inventory items
└── archive/                 # Deprecated exports and old files

docs/
├── core/                    # MISSION, PRINCIPLES, STRUCTURE
└── (other docs)

context/                     # Historical reference only (architecture, planning, audits)

ops/
└── status/                  # Domain migration logs and status tracking
```

---

## Notes

- All paths in this file use absolute references from repo root
- Phase A focused on room consolidation; finance and pricing are Phase B
- Git branch `bootstrap/2026-02-13-baseline` awaiting merge to `main`

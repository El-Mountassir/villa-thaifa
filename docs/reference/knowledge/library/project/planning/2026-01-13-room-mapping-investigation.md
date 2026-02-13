# Implementation Plan: Booking.com Room Mapping & Safety

> **Status**: 🟢 In Progress
> **Owner**: Antigravity
> **Context**: Moving from "Room Type" (e.g. Superior Double) to "Room Number" (e.g. Room 4) on Booking.com.

## 🚨 Risk Assessment (The "Why we paused")

Changing Room Types on Booking.com is **destructive** or **risky** for:

1.  **Reviews**: Reviews are often linked to the Room Type. Deleting "Superior Double" to create "Room 4" might hide/delete reviews associated with that type.
2.  **Photos & Content**: Existing photos are mapped to the Room Type.
3.  **Future Reservations**: Existing bookings are linked to the Room Type ID.

## 🧪 Research Strategy (Before Action)

we need to confirm:

- [ ] **Renaming**: Does renaming "Superior Double" to "Room 4" preserve the ID (and thus reviews/bookings)?
- [ ] **Unit Splitting**: Can we enable "Room Names" per unit under a single Room Type? (e.g. Type = Double -> Unit 1 = Room 4, Unit 2 = Room 5).

---

## 🛡️ Data Backup Protocol (Execution Log)

> **Objective**: Securely backup all Room Type configurations, including deep attributes (size, amenities), and prepare for standardizing names.

### Phase 1: Deep Scan & Backup (Serialized)

**Critical Instruction**: Future agents picking this up MUST start with the "Exhaustive Dictionary Scrape".

- [x] **Exhaustive Amenity Dictionary Scrape** (Done)
  - Go to `manage/facilities.html`.
  - Scrape _every single checkbox label_ (unchecked & checked) to build a "Master Amenity List".
  - Update `content/backup/booking/initial_scan_2026_01_13.json` to include this global dictionary.

#### Room Status

- [x] **Room 1**: Chambre Double Superieur 4 ; 5 (ID: 544684730)
  - [x] Scrape deep data (Size: 24m², Bed: Super-king)
  - [x] Verify renaming capability (Confirmed: Can rename)
  - [x] Log incidents in `docs/specs/knowledge/booking_extranet_incidents.md`
- [ ] **Room 2**: Suite Executive 6 (ID: 544684732)
- [ ] **Room 3**: Suite De Luxe King Size 7 (ID: 544684733)
- [ ] **Room 4**: Suite Familiale 9 ; 11 (ID: 544684736)
- [ ] **Room 5**: Suite 10 (ID: 544684737)
- [ ] **Room 6**: suite Presidentiel 12 (ID: 544684739)
- [ ] **Room 7**: Chambre Triple de Luxe 1 ; 3 ; 8 (ID: 544684740)
- [ ] **Room 8**: Chambre Double De luxe 2 (ID: 544684742)

## Phase 2: Knowledge & Standardization

- [x] Create Incident Log (`docs/specs/knowledge/booking_extranet_incidents.md`)
- [x] Create Agent Guide (`docs/specs/knowledge/booking_extranet_guide.md`)
- [ ] Analyze Naming Conventions (Prepare for "Room 1", "Room 2" standardization)
- [ ] Create `rooms_standardization_plan.md`

## 📝 Governance: "No Private Plans"

This document resides in `docs/project/plans/` to ensure all agents (present and future) can see the strategy.

- **Rule**: Do not rely on ephemeral `artifacts/`. Commit plans to the repo.

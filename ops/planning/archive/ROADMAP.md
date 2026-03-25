# Villa Thaifa Roadmap

**Milestone**: v1 - Operational Stability
**Timeline**: Weeks (urgent)
**Model Profile**: Adaptive (Opus for complex, Sonnet for mid, Haiku for quick)

---

## Phase Overview

| Phase | Name                 | Requirements                   | Status  | Duration Estimate |
| ----- | -------------------- | ------------------------------ | ------- | ----------------- |
| 1     | Operational Urgency  | OPS-01, OPS-02, OPS-03, OPS-04 | Pending | ~1 week           |
| 2     | Platform Integration | INT-02, INT-03, INT-04, INT-05 | Pending | ~1-2 weeks        |
| 3     | Data Architecture    | DATA-03                        | Pending | ~3-5 days         |
| 4     | Owner Documentation  | DOC-01                         | Pending | ~2-3 days         |

**Total**: 4 phases, 14 requirements

---

## Phase 1: Operational Urgency

**Goal**: Complete urgent operational tasks blocking daily work

**Plans:** 2 plans in 2 waves

Plans:

- [ ] 01-01-PLAN.md - Organize professional photos by room (OPS-04)
- [ ] 01-02-PLAN.md - HotelRunner session: pricing, reservation, photos (OPS-01, OPS-02, OPS-03)

**Wave Structure:**
| Wave | Plans | Parallel | Notes |
|------|-------|----------|-------|
| 1 | 01-01 | Yes | Filesystem only, no HotelRunner needed |
| 2 | 01-02 | No | Requires manual auth, batches 3 tasks |

**Requirements**:

- OPS-01: Configure HotelRunner prices for all 12 rooms (EM-149)
- OPS-02: Finalize reservation for room 11 (EM-150)
- OPS-03: Upload Room 12 photos to HotelRunner (EM-135)
- OPS-04: Organize professional photos by room (EM-144)

**Why First**: These are blocking Omar's daily operations. Must complete before platform work.

**Success Criteria**:

- All 12 rooms have pricing in HotelRunner
- Room 11 reservation confirmed
- Room 12 photos uploaded (min 5 photos)
- Photos organized in `photos/{room-id}/` structure

**Dependencies**: None (can start immediately)

**Risks**:

- HotelRunner access (need admin credentials - INT-03)
- Photo quality/quantity (may need coordination with Said)

---

## Phase 2: Platform Integration

**Goal**: Improve platform connections and reduce manual work

**Requirements**:

- INT-02: Scout HotelRunner Developer API capabilities (EM-146)
- INT-03: Obtain HotelRunner Admin Access for Omar (EM-142)
- INT-04: Connect Expedia via HotelRunner
- INT-05: Investigate Booking.com property type discrepancy (EM-143)

**Why Second**: Platform improvements can happen while operational tasks complete. Some can run in parallel with Phase 1.

**Success Criteria**:

- HotelRunner API vs browser automation tradeoffs documented
- Omar has admin access with 2FA
- Expedia connectivity enabled and tested
- Booking.com discrepancy identified and correction submitted

**Dependencies**:

- INT-03 (admin access) may be needed for Phase 1 (pricing config)
- INT-02 (API research) informs future automation decisions

**Risks**:

- Expedia 2FA (SMS to Omar's phone)
- Booking.com response time (external dependency)
- HotelRunner API rate limits (250 req/day)

---

## Phase 3: Data Architecture

**Goal**: Restructure database to room-centric model

**Requirements**:

- DATA-03: Villa Thaifa Room-Centric Restructuring (EM-141)

**Why Third**: Requires understanding of current state from Phase 1 & 2. Can't start until operations are stable.

**Success Criteria**:

- Database schema updated to room-centric model
- All 12 rooms migrated to new structure
- Admin dashboard works with new schema
- Data integrity validated

**Dependencies**:

- Phase 1 (understand current room data)
- Phase 2 (understand platform integrations)

**Risks**:

- Data migration complexity
- Breaking admin dashboard during migration
- SQLite constraints (no rollback mechanism)

---

## Phase 4: Owner Documentation

**Goal**: Enable Said to use HotelRunner independently

**Requirements**:

- DOC-01: Create HotelRunner Dashboard Guide for Said (EM-140)

**Why Last**: Can only document stable workflows. Requires Phases 1-3 to be complete so guide reflects actual system state.

**Success Criteria**:

- PDF guide with screenshots
- Covers all daily tasks (pricing, reservations, photos)
- Said confirms usability

**Dependencies**:

- Phase 1 (operational workflows must be stable)
- Phase 2 (platform connections must work)
- Phase 3 (data model must be final)

**Risks**:

- Said's digital literacy (78 years old, used to memorizing everything)
- Language preference (French or Arabic may be needed)

---

## Out of Scope (v2)

Deferred to next milestone:

- AI agent for reservation management (EM-154)
- Research commission negotiation strategy (EM-155 - for Said's use)
- Real-time webhook integration (requires HTTPS domain)
- Automated pricing strategy
- Owner mobile app (PWA)

**Why**: Focus on operational stability first. Platform improvements secondary. Strategic features after v1 ships.

---

## Parallelization Strategy

**Can run in parallel**:

- Phase 1 (OPS) + Phase 2 (INT-02, INT-05) - Research while executing ops
- Phase 2 (INT-03, INT-04) - Admin access + Expedia connection

**Must be sequential**:

- Phase 1 → Phase 3 (need stable ops before data migration)
- Phase 3 → Phase 4 (need stable data model before documenting)

---

## Risk Mitigation

| Risk                            | Mitigation                                    |
| ------------------------------- | --------------------------------------------- |
| HotelRunner access delay        | Prioritize INT-03 early in Phase 2            |
| Photo quality issues            | Coordinate with Said before Phase 1 starts    |
| Booking.com slow response       | Start INT-05 early, don't block on it         |
| Data migration breaks dashboard | Create backup, test in staging first          |
| Said can't use guide            | Include French translation, video walkthrough |

---

## Success Metrics (v1 Completion)

- **Operational**: Omar's manual hours reduced by 70%
- **Business**: Said can delegate operations using guides
- **Technical**: All 14 v1 requirements resolved
- **Integration**: HotelRunner, Booking.com, Expedia all connected
- **Data**: Room-centric model operational

---

_Created: 2026-01-30_
_Last updated: 2026-01-30_

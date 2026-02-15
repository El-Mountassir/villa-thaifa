# Villa Thaifa Requirements

**Status**: v1 (urgent operational focus)
**Timeline**: Weeks (blocking daily work)

---

## v1 Requirements (Current Milestone)

### Operational (Urgent - Weeks)

**OPS-01**: Configure HotelRunner prices for all 12 rooms
- **Status**: Pending
- **Priority**: Urgent
- **Linked**: EM-149
- **Acceptance**: All 12 rooms have pricing configured in HotelRunner dashboard

**OPS-02**: Finalize reservation for room 11
- **Status**: Pending
- **Priority**: Urgent
- **Linked**: EM-150
- **Acceptance**: Room 11 reservation confirmed in HotelRunner + Booking.com

**OPS-03**: Upload Room 12 photos to HotelRunner
- **Status**: Pending
- **Priority**: Urgent
- **Linked**: EM-135
- **Acceptance**: Room 12 has complete photo set in HotelRunner (min 5 photos)

**OPS-04**: Organize professional photos by room
- **Status**: Pending
- **Priority**: High
- **Linked**: EM-144
- **Acceptance**: Photos organized in `photos/{room-id}/` structure with naming convention

---

### Platform Integration (High Priority)

**INT-02**: Scout HotelRunner Developer API capabilities
- **Status**: Pending
- **Priority**: High
- **Linked**: EM-146
- **Acceptance**: Research document analyzing API vs browser automation tradeoffs

**INT-03**: Obtain HotelRunner Admin Access for Omar
- **Status**: Pending
- **Priority**: High
- **Linked**: EM-142
- **Acceptance**: Omar has admin credentials, 2FA configured, access verified

**INT-04**: Connect Expedia via HotelRunner
- **Status**: Pending
- **Priority**: High
- **Linked**: (new)
- **Acceptance**: Expedia connectivity enabled in HotelRunner, test reservation syncs successfully

**INT-05**: Investigate Booking.com property type discrepancy
- **Status**: Pending
- **Priority**: High
- **Linked**: EM-143
- **Acceptance**: Discrepancy identified, correction plan documented, submitted to Booking.com

---

### Data Architecture (High Priority)

**DATA-03**: Villa Thaifa Room-Centric Restructuring
- **Status**: Pending
- **Priority**: High
- **Linked**: EM-141
- **Acceptance**: Database schema updated to room-centric model, all 12 rooms migrated

---

### Documentation (Medium Priority)

**DOC-01**: Create HotelRunner Dashboard Guide for Said
- **Status**: Pending
- **Priority**: Medium
- **Linked**: EM-140
- **Acceptance**: PDF guide with screenshots, covers all daily tasks, Said confirms usability

---

## v2 Requirements (Future)

Deferred to next milestone after v1 operational tasks complete:

- **AI-01**: AI agent for reservation management (EM-154)
- **BIZ-01**: Research commission negotiation strategy (EM-155 - for Said's use)
- **INT-06**: Real-time webhook integration (requires HTTPS domain)
- **PRICE-01**: Automated pricing strategy
- **MOBILE-01**: Owner mobile app (PWA)

---

## Validated Requirements (Already Shipped)

**PUB-01**: Public hotel website with room showcase ✅
**PUB-02**: Room detail pages with static generation ✅
**PUB-03**: Facilities showcase (spa, pool, restaurant, bar) ✅
**ADMIN-01**: Admin dashboard with room management grid ✅
**ADMIN-02**: Room detail editor (metadata, amenities, beds) ✅
**ADMIN-03**: Verification workflow (DRAFT → VERIFIED status) ✅
**DATA-01**: SQLite database with room, bed, amenity tables ✅
**DATA-02**: Zod schema validation across all data ✅
**INT-01**: HotelRunner reservation extraction (96 records via browser automation) ✅

---

## Non-Functional Requirements

### Performance
- HotelRunner extraction: < 30 seconds for 100 reservations
- Admin dashboard: Page load < 2 seconds
- Database queries: < 100ms for room listings

### Security
- Credentials stored in `.env.local` (gitignored)
- Never use owner accounts without explicit approval
- All user input validated with Zod schemas
- No hardcoded secrets in codebase

### Reliability
- Daily HotelRunner extraction (5-10 min manual auth acceptable)
- SQLite WAL mode for concurrent access
- Graceful fallback if HotelRunner API unavailable

### Usability
- Said can use HotelRunner dashboard (guide provided)
- Omar can execute daily extraction in < 10 minutes
- Admin UI clear status indicators

---

## Acceptance Criteria

v1 is complete when:
- [ ] All OPS requirements resolved (4 items)
- [ ] All INT requirements resolved (4 items)
- [ ] DATA-03 resolved (room-centric restructuring)
- [ ] DOC-01 resolved (HotelRunner guide)
- [ ] Omar's manual hours reduced by 70%
- [ ] Said can delegate operations using provided guides

---

*Last updated: 2026-01-30*

# Villa Thaifa Property Management Platform

## What This Is

An AI-powered property management platform for Villa Thaifa, a 4-star boutique hotel in Marrakesh's Palmeraie district. The platform integrates HotelRunner (PMS), Booking.com, and Expedia to automate reservation management, reduce Omar's manual operational burden by 70%, and enable Said (property owner, 78) to delegate operations with confidence.

**System Type**: Hybrid Next.js web application (public hotel website + admin dashboard) with SQLite backend and external platform integrations (HotelRunner, Booking.com, Expedia).

**Current State**: Brownfield project with working public website and admin dashboard. Urgent operational tasks blocking daily work.

## Core Value

**Reduce Omar's manual operational hours by 70% through automation**, while maintaining property quality and enabling Said to delegate with zero operational burden.

If everything else fails, the system must: **automate daily HotelRunner data extraction and synchronization** so Omar spends minutes, not hours, on property management.

## Requirements

### Validated

<!-- Shipped features confirmed working in production -->

- ✅ **PUB-01**: Public hotel website with room showcase (12 rooms) — *existing*
- ✅ **PUB-02**: Room detail pages with static generation — *existing*
- ✅ **PUB-03**: Facilities showcase (spa, pool, restaurant, bar) — *existing*
- ✅ **ADMIN-01**: Admin dashboard with room management grid — *existing*
- ✅ **ADMIN-02**: Room detail editor (metadata, amenities, beds) — *existing*
- ✅ **ADMIN-03**: Verification workflow (DRAFT → VERIFIED status) — *existing*
- ✅ **DATA-01**: SQLite database with room, bed, amenity tables — *existing*
- ✅ **DATA-02**: Zod schema validation across all data — *existing*
- ✅ **INT-01**: HotelRunner reservation extraction (96 records via browser automation) — *existing*

### Active

<!-- Current v1 scope being built toward -->

**Operational (Urgent - Weeks Timeline)**:
- [ ] **OPS-01**: Configure HotelRunner prices for all 12 rooms (EM-149)
- [ ] **OPS-02**: Finalize reservation for room 11 (EM-150)
- [ ] **OPS-03**: Upload Room 12 photos to HotelRunner (EM-135)
- [ ] **OPS-04**: Organize professional photos by room (EM-144)

**Platform Integration (High Priority)**:
- [ ] **INT-02**: Scout HotelRunner Developer API capabilities (EM-146)
- [ ] **INT-03**: Obtain HotelRunner Admin Access for Omar (EM-142)
- [ ] **INT-04**: Connect Expedia via HotelRunner (pending configuration)
- [ ] **INT-05**: Investigate Booking.com property type discrepancy (EM-143)

**Data Architecture (High Priority)**:
- [ ] **DATA-03**: Villa Thaifa Room-Centric Restructuring (EM-141)

**Documentation (Medium Priority)**:
- [ ] **DOC-01**: Create HotelRunner Dashboard Guide for Said (EM-140)

### Out of Scope

<!-- Explicit boundaries with reasoning -->

- **Direct booking channel (EM-155)** — Said's business decision, not Omar's technical work. Agents can draft emails/recommendations for Said to negotiate with Booking.com, but reducing 25% commission is not Omar's operational priority.
- **Real-time reservation updates** — Batch daily extraction acceptable due to authentication barriers (reCAPTCHA, OTP). Real-time requires HTTPS domain and webhook setup (not urgent).
- **AI agent for reservation management (EM-154)** — Defer to v2. Focus on operational stability first.
- **Guest-facing mobile app** — Web-first approach. Mobile PWA deferred to future.
- **Financial accounting system** — Focus on operations, not accounting. Use existing tools for financials.
- **Staff scheduling system** — Not needed for 12-room property.
- **Building PMS from scratch** — Leverage HotelRunner as base, integrate don't replace.

## Context

### Property Background

**Villa Thaifa** is a 4-star boutique hotel in Marrakesh's Palmeraie district with 12-16 rooms, infinity pool, hammam, spa, restaurant, and bar. Located 13 km from city center, 17-19 km from airport.

**Stakeholders**:
- **Said** (Owner, 78): Manages property from memory, no digital systems. Final approval on pricing, guest communication, budget. Business decisions (commission negotiations) are his responsibility.
- **Omar** (Manager): Technical implementation lead. Handles platform operations, automation, daily workflows. Focus on reducing manual hours.
- **Guests**: International travelers seeking boutique Morocco experience.

**Current Systems**:
- HotelRunner (PMS) - Primary property management system
- Booking.com (OTA) - 25% commission distribution channel
- Expedia Group - Pending connection

**Pain Points** (Omar's perspective):
- High manual operational burden (data entry, extraction, synchronization)
- Daily HotelRunner login required due to cookie persistence bug
- Disconnected systems (HotelRunner, Booking.com, local database)
- No automation for pricing updates or photo management

### Technical Environment

**Tech Stack** (existing):
- **Core**: Next.js 16.1.3 + React 19.2.3 + TypeScript 5.9.3
- **Database**: SQLite 3 (local-first, `property.db` with WAL mode)
- **Validation**: Zod 4.3.5 (runtime schemas + TypeScript types)
- **Automation**: agent-browser (headless browser CLI, npm global)
- **Project Management**: Linear (MCP integration, 50 issues total)

**Architecture Pattern**: Feature-based structure with dual data sources (JSON for public site, SQLite for admin dashboard). No ORM, direct SQL queries via better-sqlite3.

**Integration Approach**: Browser automation (primary) + REST API (fallback) for HotelRunner. Manual auth required daily (reCAPTCHA barrier).

### Prior Work

This is a **brownfield project**. Existing validated features:
- Public website with room listings and facilities
- Admin dashboard with room management and verification workflow
- SQLite database with rooms, beds, amenities tables
- HotelRunner reservation extraction (96 records, 15-second extraction time)

See `.planning/codebase/ARCHITECTURE.md` for full system architecture.

## Constraints

### Technical Constraints

- **Authentication Barriers**: HotelRunner (Google reCAPTCHA), Booking.com (OTP via email), Expedia (SMS 2FA). Full automation blocked.
- **API Rate Limits**: HotelRunner API limited to 250 requests/day, 5 requests/minute. Batch extraction only.
- **Browser Automation Bug**: agent-browser doesn't persist cookies. Manual login required per session (5-10 min daily).
- **SQLite Deployment**: Requires persistent file storage for `property.db`. Not suitable for serverless edge without modifications.
- **Deployment**: Node.js 16+, file system access for SQLite, persistent storage required.

### Business Constraints

- **Stakeholder Approval Protocol**: Scout → Report → Questions → Action. Said approves pricing/guest ops, Omar approves technical decisions.
- **Manual Data Entry Legacy**: Said manages property from memory. No historical digital records. Data migration required from verbal knowledge.
- **Timeline**: Urgent (weeks) - operational issues blocking daily work.

### Platform Constraints

- **HotelRunner Channel Mapping**: 8 room types configured in HotelRunner, must match Booking.com room types. Discrepancy identified (EM-143).
- **Content Gaps**: Room 12 photos missing, professional photos not organized by room.
- **Pricing Gaps**: HotelRunner prices not configured for all rooms.
- **Webhook Requirements**: HotelRunner API requires HTTPS callback URL. No domain/HTTPS setup. Blocks real-time notifications.

### Scope Boundary

**Omar's Responsibility**: Technical platform operations, automation, daily workflows.
**Said's Responsibility**: Business decisions (commission negotiations, direct booking strategy), guest communication, pricing strategy.

**Agents can**: Draft emails, provide recommendations, analyze data for Said's decisions.
**Agents cannot**: Execute business decisions on Said's behalf without explicit approval.

## Key Decisions

| Decision | Rationale | Outcome |
|----------|-----------|---------|
| Use SQLite (not cloud DB) | Local-first simplicity, low operational overhead, sufficient for 12-room property | — Pending |
| Browser automation (not full API) | HotelRunner API rate-limited (250 req/day), reCAPTCHA blocks full automation. Browser extraction working (96 records, 15 sec). | — Pending |
| Defer direct booking channel | Said's business decision, not Omar's technical priority. Agents can draft emails for Said to negotiate with Booking.com. | ✓ Good |
| Urgent operational focus (weeks) | EM-149, EM-150, EM-135 blocking daily work. Platform improvements secondary. | — Pending |
| Feature-based architecture | Rooms, facilities as features vs layer-based. Clearer domain boundaries, easier to maintain. | — Pending |

---

*Last updated: 2026-01-30 after initial questioning and scope clarification*

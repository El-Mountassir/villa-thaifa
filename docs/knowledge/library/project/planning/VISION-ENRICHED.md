---
title: "Villa Thaifa Property Management Platform - Enriched Vision"
status: "enriched - ready for PROJECT.md creation"
created: 2026-01-30
last-updated: 2026-01-30
sources:
  - Linear issues (10 Villa Thaifa-specific)
  - Codebase architecture analysis
  - Google Maps public listing
  - Booking.com / Planet of Hotels listings
---

# Villa Thaifa Property Management Platform - Enriched Vision

**Status**: ✅ Enriched with public listings, codebase analysis, and Linear issues

---

## Property Overview

### Basic Information

- **Name**: Villa Thaifa
- **Star Rating**: 4-star guest house and boutique villa
- **Location**: Palmeraie district, Marrakesh, Morocco
  - 13 km (8 miles) from Marrakesh city center
  - 17-19 km from Marrakesh-Menara Airport
  - 20-30 min drive to Bahia Palace and Jemaa el-Fnaa
- **Address**: Route de Fès Km 12, Ouled Jelal, Marrakesh, 40000, Morocco
- **Contact**: +212 6 62 14 69 49

### Stakeholders

- **Owner**: Said (78 years old, manages property from memory, no digital systems)
- **Manager**: Omar El Mountassir (Chairman, technical implementation lead)
- **Guests**: International travelers seeking boutique Morocco experience
- **Distribution**: Booking.com (25% commission), HotelRunner PMS

### Property Features

**Accommodations**:

- 12 to 16 well-appointed rooms and suites
- Room types: Standard, family, presidential suites
- Room features: Air conditioning, private bathrooms, flat-screen TVs, garden/pool views

**Amenities**:

- Large outdoor infinity swimming pool and sun terrace
- On-site restaurant (Moroccan cuisine)
- Bar and coffee shop
- Wellness facilities: hammam (Turkish bath), spa services, massages
- Billiards
- Proximity to hiking trails

**Services**:

- Free on-site private parking
- Complimentary Wi-Fi
- Daily housekeeping
- Airport shuttle (paid)

**Guest Policies**:

- Check-in: 14:00 (2:00 PM)
- Check-out: 12:00 PM
- Complimentary local breakfast (served until 12:30 PM)
- Minimum age 18 for check-in
- Quiet hours: midnight - 6:00 AM

---

## Core Problem & Solution

### Problem Statement

**Current State**: Villa Thaifa operates manually with disconnected systems:

- Property owner Said (78) manages everything from memory
- No existing digital records for historical data
- Current tech: HotelRunner (PMS), Booking.com (25% commission OTA)
- No automation, high manual overhead
- Data fragmentation across platforms
- No visibility into business metrics

**Pain Points**:

- High operational burden for Omar (manual data entry, extraction)
- Revenue leakage (25% Booking.com commissions)
- Property owner can't delegate operations (no systems in place)
- No real-time insights into bookings, pricing, occupancy

### Solution Overview

**What We're Building**: AI-powered property management platform that:

- Integrates HotelRunner (PMS), Booking.com, Expedia (OTA channels)
- Automates reservation management and data synchronization
- Provides owner-friendly dashboard with analytics
- Reduces reliance on high-commission OTAs (build direct booking channel)
- Enables data-driven decision making (pricing, occupancy optimization)

**System Type**: Hybrid Next.js web application (public hotel site + admin dashboard) with SQLite backend and external platform integrations.

**Core Value**: Reduce operational burden to zero for Said, reduce Omar's manual hours by 70%, increase direct booking ratio, make property delegation-ready.

---

## Technical Architecture (From Codebase Analysis)

### Current System Components

1. **Public Website** (`/`)
   - ✅ Static hotel website with room listings
   - ✅ Facility showcase (spa, pool, restaurant, bar)
   - ✅ Server-side rendered from JSON data sources
   - ✅ Pre-generated static pages for SEO

2. **Admin Dashboard** (`/admin`)
   - ✅ Room management interface
   - ✅ Verification workflow system (DRAFT → VERIFIED status)
   - ✅ SQLite-backed database for admin data
   - ✅ Server actions for data mutations

3. **Data Layer** (Dual-source architecture)
   - **JSON files** (`src/data/`) - Public website data (rooms.json, facilities.json)
   - **SQLite database** (`property.db`) - Admin-only data with verification workflows
   - Feature-scoped bindings layer abstracts data sources

4. **External Integration Layer**
   - **HotelRunner** (via browser automation) - Primary PMS, reservation extraction
   - **Booking.com** (via HotelRunner) - OTA distribution channel
   - **Agent Browser** - Headless automation for data extraction (manual auth required)

### Technology Stack

**Core**: Next.js 16.1.3 + React 19.2.3 + TypeScript 5.9.3
**Database**: SQLite 3 (local-first, `property.db`)
**Validation**: Zod 4.3.5 (runtime schemas)
**Automation**: agent-browser (headless browser CLI)
**Project Management**: Linear (MCP integration)

**Architecture Pattern**: Feature-based structure with dual data sources (JSON for public, SQLite for admin)

---

## Validated Requirements (Already Built ✅)

### Public Website Features

1. ✅ Home page with hero section and hotel branding
2. ✅ Accommodations grid showing all 12 rooms
3. ✅ Facilities showcase (spa, pool, restaurant, bar)
4. ✅ Room detail pages (`/rooms/[id]`) with static generation
5. ✅ SEO-friendly static paths

### Admin Dashboard Features

6. ✅ Admin room management grid view
7. ✅ Room detail editor (metadata, amenities, beds)
8. ✅ Verification workflow (DRAFT → VERIFIED status)
9. ✅ SQLite-backed data storage

### Data Management

10. ✅ Feature bindings API (data abstraction layer)
11. ✅ Zod schema validation across all data
12. ✅ Database initialization from schema.sql

### Integration Capabilities

13. ✅ HotelRunner reservation extraction (96 reservations via browser automation)
14. ✅ Environment configuration for credentials (.env.local)

---

## Active Requirements (In Progress 🔄)

From Linear issues (EM-128 to EM-155):

**Operational (Urgent)**:

- EM-150: Finalize reservation room 11
- EM-149: Configure HotelRunner prices for all rooms
- EM-135: Upload Room 12 photos to HotelRunner

**Platform Integration (High)**:

- EM-146: Scout HotelRunner Developer API capabilities
- EM-142: Obtain HotelRunner Admin Access for Omar
- EM-143: Investigate Booking.com property type discrepancy
- EM-141: Villa Thaifa Room-Centric Restructuring

**Content (High)**:

- EM-144: Organize professional photos by room

**Documentation (Medium)**:

- EM-140: Create HotelRunner Dashboard Guide for Said

---

## Future Requirements (Planned 📋)

From Linear issues + roadmap:

- EM-154: AI agent for reservation management
- EM-155: Direct booking channel (reduce Booking.com dependency)
- Automated pricing strategy
- Real-time webhook integration (requires HTTPS domain)
- Owner mobile app (PWA)

---

## Platform Integrations

### 1. HotelRunner (Primary PMS) ✅ Operational

- **Integration Method**: Browser automation (manual auth daily) OR REST API (rate-limited)
- **API Limitations**: 250 requests/day, 5 requests/minute
- **Authentication Barrier**: Google reCAPTCHA on every login
- **Data Extracted**: Reservations (96 records), calendar, room types
- **Status**: Working via browser automation (15-second extraction time)

### 2. Booking.com (OTA Distribution) ✅ Connected

- **Commission**: 25% on all bookings
- **Integration Method**: XML sync via HotelRunner
- **Authentication**: OTP via email on login
- **Known Issues**: Property type discrepancy (EM-143)

### 3. Expedia Group (Future OTA) ❌ Not Connected

- **Channels**: Expedia.com, Hotels.com, Vrbo
- **Integration Method**: Via HotelRunner (pending configuration)
- **Authentication**: SMS 2FA to Omar's phone (+212643390409)
- **Requirements**: Hotel ID from Expedia Partner Central + connectivity settings

### 4. Agent Browser (Automation Tool) ✅ Operational

- **Type**: Headless browser CLI (npm global package)
- **Capabilities**: Web scraping, form automation, screenshots, PDF export, data extraction
- **Limitation**: Profile persistence bug (cookies not saved between sessions)
- **Impact**: Manual login required for each extraction session

### 5. Linear (Project Management) ✅ Configured

- **Integration**: MCP + code execution hybrid
- **Usage**: 50 issues total (10 Villa Thaifa-specific)
- **Projects**: Q1 2026 Operations, OTA Integration, Room Management

---

## Critical Constraints

### Technical Constraints

1. **Authentication Barriers**
   - HotelRunner: Google reCAPTCHA on every login (blocks full automation)
   - Booking.com: OTP via email on login
   - Expedia: SMS 2FA to Omar's phone
   - **Impact**: Daily manual intervention required (5-10 min)

2. **API Rate Limits**
   - HotelRunner API: 250 requests/day, 5 requests/minute
   - **Impact**: Batch extraction only (not real-time)

3. **Browser Automation Bug**
   - agent-browser doesn't persist cookies between sessions
   - **Impact**: Manual login required per extraction session

4. **SQLite Constraints**
   - Single-file database (`property.db`)
   - Requires persistent file storage in production
   - WAL mode for concurrency

5. **Deployment Requirements**
   - Node.js 16+ runtime
   - File system access for SQLite
   - Persistent storage for `property.db`
   - Not suitable for serverless edge without modifications

### Business/Operational Constraints

6. **Multi-Stakeholder Approval**
   - **Said (Owner)**: Final approval on pricing, guest communication, budget
   - **Omar (Manager)**: Technical decisions, platform operations
   - **Protocol**: Scout → Report → Questions → Action

7. **Commission Dependency**
   - **Booking.com**: 25% commission on all bookings
   - **Strategic Goal**: EM-155 (direct booking channel to reduce dependency)

8. **Credential Security**
   - `.env.local` contains production credentials (gitignored)
   - **Rule**: NEVER delete credentials from `.env.local`
   - **Rule**: NEVER use owner accounts without explicit approval
   - **Documented**: `docs/operations/.env.rules.md`

9. **Manual Data Entry Legacy**
   - Said manages property manually (everything memorized)
   - No existing digital records for historical data
   - Data migration required from verbal knowledge

### Platform-Specific Constraints

10. **HotelRunner Channel Mapping**
    - 8 room types configured in HotelRunner
    - Must match Booking.com room types
    - Discrepancy identified (EM-143)

11. **Content Gaps**
    - Room 12 photos missing (EM-135)
    - Professional photos not organized by room (EM-144)
    - Impacts OTA presentation quality

12. **Pricing Synchronization**
    - HotelRunner prices not configured for all rooms (EM-149)
    - Manual entry required
    - No automated pricing strategy yet

13. **Webhook Requirements**
    - HotelRunner API requires HTTPS callback URL
    - No domain/HTTPS setup identified
    - Blocks real-time webhook notifications

---

## Success Criteria (v1 Completion)

### Technical Milestones

- All 12 rooms verified in admin dashboard
- HotelRunner pricing configured for all rooms
- Expedia connected via HotelRunner
- Professional photos uploaded and organized
- Reservation extraction automated (daily batch)
- Owner dashboard guide created

### Business Metrics

- Reduce Omar's manual hours by 70%
- Reduce Said's operational burden to zero (delegation-ready)
- Increase direct booking ratio (reduce Booking.com dependency)
- Property ready for professional management handoff or exit

---

## Out of Scope

**Explicitly Not Building**:

- ❌ Full property management system from scratch (using HotelRunner as base)
- ❌ Real-time reservation updates (batch daily due to auth constraints)
- ❌ Guest-facing mobile app (web-first)
- ❌ Financial accounting system (focus on operations)
- ❌ Staff scheduling system (not needed for 12-room property)

**Why**: Leverage existing platforms (HotelRunner) and focus on integration/automation layer rather than reinventing PMS infrastructure.

---

## Next Steps

1. ✅ Create vision draft
2. ✅ Spawn codebase analysis agent
3. ✅ Enrich with public listing data
4. 🔄 **NOW**: Run `/gsd:new-project` to create PROJECT.md
5. 🔄 Define requirements from validated + active features
6. 🔄 Create roadmap with phases

---

## Sources

- **Linear**: 50 issues (10 Villa Thaifa-specific: EM-135 to EM-154)
- **Codebase**: `.planning/codebase/ARCHITECTURE.md`, `STACK.md`
- **Public Listings**: Google Maps, Booking.com, Planet of Hotels
- **Project Docs**: `docs/leadership/STAKEHOLDERS.md`, `docs/operations/.env.rules.md`
- **Integration Guides**: `sources/hotelrunner-api/STATUS-FINAL.md`, `sources/agent-browser/guide.md`

---

_Ready for PROJECT.md creation via `/gsd:new-project`_

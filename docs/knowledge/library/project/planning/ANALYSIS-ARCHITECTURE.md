# Architecture Analysis

## Current System

Villa Thaifa Property Management Platform is a **hybrid Next.js application** that serves both public-facing hotel content and an admin dashboard for property management.

**System Components**:

1. **Public Website** (`/`)
   - Static hotel website with room listings
   - Facility showcase (spa, pool, restaurant)
   - Server-side rendered from JSON data sources
   - Pre-generated static pages for SEO

2. **Admin Dashboard** (`/admin`)
   - Room management interface
   - Verification workflow system (DRAFT → VERIFIED status)
   - SQLite-backed database for admin data
   - Server actions for data mutations

3. **Data Layer** (Dual-source architecture)
   - **JSON files** (`src/data/`) - Public website data (rooms.json, facilities.json)
   - **SQLite database** (`property.db`) - Admin-only data with verification workflows
   - Feature-scoped bindings layer abstracts data sources

4. **External Integration Layer**
   - **HotelRunner** (via browser automation) - Primary PMS, reservation extraction
   - **Booking.com** (via HotelRunner) - OTA distribution channel
   - **Agent Browser** - Headless automation for data extraction (manual auth required)

**Key Architecture Decisions**:
- Feature-based structure (rooms, facilities) instead of layer-based
- No ORM - Direct SQL queries via better-sqlite3
- Server actions for mutations (Next.js App Router pattern)
- Zod schemas for runtime validation + TypeScript type generation
- WAL mode for concurrent SQLite access

## Technology Stack

**Core Framework**:
- **Next.js 16.1.3** - Full-stack React framework with App Router
- **React 19.2.3** - UI component library
- **TypeScript 5.9.3** - Type-safe development

**Data & Validation**:
- **better-sqlite3 12.6.2** - Embedded SQL database (local-first, no external DB)
- **Zod 4.3.5** - Schema validation and type inference
- **Axios 1.13.4** - HTTP client (prepared but not yet integrated)

**Development Tools**:
- **ESLint 9.39.2** - Code linting
- **PostCSS 8.5.6** - CSS processing
- **tsx 4.21.0** - TypeScript execution runtime
- **dotenv 17.2.3** - Environment variable management

**Database**:
- **SQLite 3** (embedded, file-based at `property.db`)
- WAL (Write-Ahead Logging) mode for concurrency
- Three tables: `rooms`, `beds`, `amenities`
- Indexed foreign keys for performance

**External Tools**:
- **agent-browser** (npm global) - Headless browser automation
- **HotelRunner API** - REST API (rate-limited: 250 req/day, 5/min)
- **Linear** - Project management (MCP integration)

**Platform Requirements**:
- Node.js 16+
- npm 7+
- SQLite 3 runtime
- Next.js compatible deployment (Vercel, AWS Lambda, or self-hosted)

## Validated Features

These are **already implemented and working** in the codebase:

### Public Website Features
1. **Home Page** (`/`)
   - Hero section with hotel branding
   - Accommodations grid showing all 12 rooms
   - Facilities showcase (spa, pool, restaurant, bar)
   - Server-side rendering from JSON data

2. **Room Detail Pages** (`/rooms/[id]`)
   - Individual room pages with static generation
   - Room images, features, pricing display
   - Fetched from `rooms.json`
   - SEO-friendly static paths

### Admin Dashboard Features
3. **Admin Room Management** (`/admin/rooms`)
   - Grid view of all rooms with status badges
   - Shows: ID, type, internal name, verification status, floor, base rate
   - SQLite-backed data storage

4. **Admin Room Detail** (`/admin/rooms/[id]`)
   - Detailed room editor with three data sections:
     - **Room metadata**: Floor, size, rate, kitchen status
     - **Amenities**: Grouped by category (View, Outdoor, Bathroom, Climate, Layout, Hardware)
     - **Beds**: Type, count, dimensions
   - "Verify Room" button triggers status change workflow

5. **Verification Workflow**
   - Status progression: `DRAFT` → `VERIFIED`
   - Server action updates database
   - Cache revalidation on status change
   - Visual status badges in UI

### Data Management
6. **Feature Bindings API**
   - Abstraction layer for data sources
   - `getRooms()`, `getRoom(id)` - Type-safe async functions
   - Zod schema validation on all data structures
   - Swap data sources without breaking consumers

7. **Database Initialization**
   - Auto-initialization from `schema.sql` on startup
   - Logging for initialization status

### Integration Capabilities
8. **HotelRunner Browser Extraction** (Manual)
   - Extract 96 reservations via agent-browser
   - All 14 fields accessible (status, dates, guest, price, etc.)
   - Requires manual authentication (profile persistence issue)
   - 15-second extraction time

9. **Environment Configuration**
   - `.env.local` for credentials (HotelRunner, Booking.com, Expedia)
   - `.env.example` as template
   - Admin vs Owner account separation

## Integration Points

### 1. HotelRunner (Primary PMS)
- **Type**: Channel manager + property management system
- **Integration Method**: Browser automation (manual auth) OR REST API (rate-limited)
- **Status**: ✅ Operational via browser automation
- **Credentials**: Admin (Omar) and Owner (Said) accounts
- **API Limitations**:
  - 250 requests/day, 5 requests/minute
  - Requires HTTPS callback URL for webhooks
  - reCAPTCHA on login (blocks full automation)
- **Data Extracted**: Reservations (96 records), calendar, room types
- **Documented**: `sources/hotelrunner-api/STATUS-FINAL.md`

### 2. Booking.com (OTA Distribution)
- **Type**: Online travel agency (25% commission)
- **Integration Method**: Via HotelRunner sync (XML connection)
- **Status**: ✅ Active connection
- **Credentials**: Admin (Omar) and Owner (Said) extranet accounts
- **Constraints**:
  - Property type discrepancy identified (EM-143)
  - OTP authentication on login
  - reCAPTCHA may appear
- **Data**: Room mappings, pricing, availability, guest reviews
- **Documented**: `docs/specs/knowledge/platforms/booking/`

### 3. Expedia Group (Future OTA)
- **Type**: OTA distribution (Expedia.com, Hotels.com, Vrbo)
- **Integration Method**: Via HotelRunner (pending connection)
- **Status**: ❌ Not connected
- **Credentials**: Admin account exists (SMS 2FA to Omar's phone)
- **Requirements**:
  - Hotel ID from Expedia Partner Central
  - Authorize "HotelRunner" in connectivity settings
  - 2FA may block browser automation
- **Documented**: `docs/operations/expedia/`

### 4. Agent Browser (Automation Tool)
- **Type**: Headless browser CLI (npm global package)
- **Version**: Installed globally via npm
- **Status**: ✅ Operational
- **Capabilities**: Web scraping, form automation, screenshots, PDF export, data extraction
- **Limitations**: Profile persistence bug (cookies not saved)
- **Documented**: `sources/agent-browser/guide.md`

### 5. Linear (Project Management)
- **Type**: Issue tracking and project management
- **Integration Method**: MCP (Model Context Protocol) + code execution hybrid
- **Status**: ✅ Configured, migration in progress
- **Usage**: 29 active issues (EM-128 to EM-155)
- **Projects**: Q1 2026 Operations, OTA Integration, Room Management
- **Documented**: `.agents/rules/linear-workflow.md`

## Constraints

### Technical Constraints

1. **Authentication Barriers**
   - **HotelRunner**: Google reCAPTCHA on every login (blocks full automation)
   - **Booking.com**: OTP via email on login
   - **Expedia**: SMS 2FA to Omar's phone (+212643390409)
   - **Impact**: Browser automation requires manual intervention for auth

2. **API Rate Limits**
   - **HotelRunner API**: 250 requests/day, 5 requests/minute
   - **Impact**: Can't use API for high-frequency polling
   - **Workaround**: Browser automation for batch extraction

3. **Browser Automation Limitation**
   - **agent-browser profile persistence bug**: Cookies not saved between sessions
   - **Impact**: Manual login required for each extraction session
   - **Workaround**: Daily manual extraction (5-10 min/day)
   - **Investigation**: Pending (options: cookie export/import, alternative tools, API fallback)

4. **SQLite Constraints**
   - Single-file database (`property.db`)
   - File persistence required in production
   - Concurrent access via WAL mode
   - No native replication (backup strategy needed)

5. **Static Generation Limits**
   - Public pages pre-generated at build time
   - Changes require rebuild for static pages
   - Admin pages use server actions (real-time)

6. **Deployment Requirements**
   - Node.js 16+ runtime
   - File system access for SQLite
   - Persistent storage for `property.db`
   - Not suitable for serverless edge without modifications

### Business/Operational Constraints

7. **Multi-Stakeholder Approval**
   - **Said (Owner)**: Final approval on pricing, guest communication, budget
   - **Omar (Manager)**: Approves technical decisions, platform operations
   - **Agents**: Cannot execute without Omar approval on critical ops
   - **Protocol**: Scout → Report → Questions → Action

8. **Commission Dependency**
   - **Booking.com**: 25% commission on all bookings
   - **Impact**: Significant revenue loss vs direct bookings
   - **Strategic**: EM-155 explores direct booking channel

9. **Credential Security**
   - `.env.local` contains production credentials (gitignored)
   - **Rule**: NEVER delete credentials from `.env.local`
   - **Rule**: NEVER use owner accounts without explicit approval
   - **Documented**: `docs/operations/.env.rules.md`

10. **Manual Data Entry Legacy**
    - Said manages property manually (everything memorized)
    - No existing digital records for historical data
    - Data migration required from verbal knowledge

### Platform-Specific Constraints

11. **HotelRunner Channel Mapping**
    - 8 room types configured in HotelRunner
    - Must match Booking.com room types
    - Discrepancy identified (EM-143)

12. **Booking.com Property Type**
    - Property type mismatch discovered
    - May affect search visibility
    - Requires investigation and correction

13. **Content Gaps**
    - Room 12 photos missing (EM-135)
    - Professional photos not organized by room (EM-144)
    - Impacts OTA presentation quality

14. **Pricing Synchronization**
    - HotelRunner prices not configured for all rooms (EM-149)
    - Manual entry required
    - No automated pricing strategy yet

### Integration Constraints

15. **Webhook Requirements**
    - HotelRunner API requires HTTPS callback URL
    - No domain/HTTPS setup identified
    - Blocks real-time webhook notifications

16. **Expedia Connection Prerequisites**
    - Requires Hotel ID from Expedia system
    - Requires connectivity settings change in Expedia Partner Central
    - Coordination between platforms needed

17. **Room Mapping Complexity**
    - 12 physical rooms
    - 8 HotelRunner room types
    - Booking.com room type mappings
    - Must maintain consistency across platforms

## Recommendations for PROJECT.md

### 1. Problem Statement
**Current State**: Villa Thaifa (12-room boutique hotel) operates manually with disconnected systems. Property owner Said (78) manages everything from memory. Current tech: HotelRunner (PMS), Booking.com (25% commission), no automation.

**Core Problem**: High operational burden, revenue leakage (25% commissions), data fragmentation across platforms, no visibility into business metrics.

### 2. Solution Overview
**What We're Building**: AI-powered property management platform that:
- Integrates HotelRunner, Booking.com, Expedia
- Automates reservation management
- Provides owner-friendly dashboard
- Reduces reliance on high-commission OTAs
- Enables data-driven decision making

**System Type**: Hybrid Next.js web application (public site + admin dashboard) with SQLite backend and external platform integrations.

### 3. Validated Requirements (Already Built)
From existing codebase:
- Public hotel website with room showcase
- Admin dashboard with room management
- Verification workflow (DRAFT → VERIFIED)
- HotelRunner data extraction (96 reservations via browser automation)
- Feature-scoped architecture with data abstraction layer
- Zod schema validation across all data

### 4. Active Requirements (In Progress)
From Linear issues (EM-128 to EM-155):
- Configure HotelRunner pricing for all rooms
- Upload Room 12 photos
- Connect Expedia via HotelRunner
- Organize professional photos by room
- Create HotelRunner dashboard guide for Said
- Investigate Booking.com property type discrepancy

### 5. Future Requirements (Planned)
From Linear issues + documented roadmap:
- AI agent for reservation management (EM-154)
- Direct booking channel to reduce Booking.com dependency (EM-155)
- Automated pricing strategy
- Real-time webhook integration (requires HTTPS domain)
- Owner mobile app (PWA)

### 6. Technical Architecture Section
**Pattern**: Feature-based Next.js 16 with dual data sources
- **Public site**: JSON-backed static generation
- **Admin dashboard**: SQLite-backed with server actions
- **No ORM**: Direct SQL queries
- **Validation**: Zod v4 runtime + TypeScript compile-time
- **Integrations**: Browser automation (primary) + REST API (fallback)

**Key Decision**: Local-first architecture (SQLite) for simplicity, later migrate to cloud DB if scaling needed.

### 7. Integration Strategy Section
**HotelRunner**: Primary PMS, browser automation for data extraction (manual auth daily)
**Booking.com**: OTA channel via HotelRunner XML sync
**Expedia**: Pending connection, requires configuration
**Linear**: Project management via MCP + code execution hybrid

**Critical Constraint**: All platforms have auth barriers (reCAPTCHA, OTP, 2FA) - automation requires manual intervention.

### 8. Constraints Section
**Authentication**: reCAPTCHA, OTP, and 2FA block full automation
**API Limits**: HotelRunner 250 req/day, 5/min
**Browser Automation**: Profile persistence bug requires daily manual login
**Stakeholder Approval**: Said (owner) for pricing/guest ops, Omar (manager) for technical decisions
**Commission**: 25% Booking.com commission is major revenue constraint

### 9. Success Criteria Section
**v1 Completion** (Align with existing Linear milestones):
- All 12 rooms verified in admin dashboard
- HotelRunner pricing configured for all rooms
- Expedia connected via HotelRunner
- Professional photos uploaded and organized
- Owner dashboard guide created
- Reservation extraction automated (daily batch)

**Business Metrics**:
- Reduce Omar's manual hours by 70%
- Reduce Said's operational burden to zero (delegation-ready)
- Increase direct booking ratio (reduce Booking.com dependency)
- Property ready for professional management handoff or exit

### 10. Out of Scope Section
**Explicitly Not Building**:
- Full property management system from scratch (using HotelRunner as base)
- Real-time reservation updates (batch daily instead, due to auth constraints)
- Guest-facing mobile app (web-first)
- Financial accounting system (focus on operations)
- Staff scheduling system (not needed for 12-room property)

**Why**: Leverage existing platforms (HotelRunner) and focus on integration/automation layer rather than reinventing PMS infrastructure.

---

**Key Files to Reference**:
- Architecture: `.planning/codebase/ARCHITECTURE.md`
- Stack: `.planning/codebase/STACK.md`
- Mission: `docs/project/meta/MISSION.md`
- HotelRunner Status: `sources/hotelrunner-api/STATUS-FINAL.md`
- Linear Issues: https://linear.app/el-mountassir (29 active issues)
- Stakeholders: `docs/leadership/STAKEHOLDERS.md`
- Constraints: `docs/operations/.env.rules.md`

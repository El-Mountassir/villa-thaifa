# Villa Thaifa Existing App Audit

**Audit Date**: 2026-02-13
**Project Location**: `/home/director/villa-thaifa/`
**Project Size**: 1.4GB (556 markdown files, 50,381 total LOC including node_modules)
**Status**: Partial implementation, active development paused
**Auditor**: Nova (Claude Sonnet 4.5)

---

## Executive Summary

Villa Thaifa has a **partially functional Next.js application** (App Router, ~637 LOC core implementation) with basic public and admin pages displaying 12 rooms from dual data sources. The SQLite database (`property.db`) contains an **Expedia-compliant schema** with rooms, beds, and amenities tables (12 rooms, VERIFIED status). The app serves as a **skeleton/prototype** rather than production-ready system.

**HotelRunner integration** exists as browser automation scripts (Python + agent-browser), NOT as a REST API integration. Authentication requires **manual daily intervention** due to session persistence limitations.

**Agent infrastructure** is extensive (556 markdown files, 61 doc directories, 15 agent definitions, 5 workflows) with comprehensive documentation but represents **over-engineering** for the current implementation state.

**Key Finding**: Most valuable for reuse are (1) SQLite schema design (Expedia-spec compliant), (2) room data (12 rooms with pricing/photos), and (3) workflow documentation patterns. The 637-line Next.js app itself is **not worth extending**—a fresh start is recommended.

---

## Route/Page Inventory

| Path | Status | Description | LOC | Data Source |
|------|--------|-------------|-----|-------------|
| `/` (public homepage) | **FUNCTIONAL** | Hero section + room grid + facilities grid | 252 | `src/data/rooms.json` + `src/data/facilities.json` |
| `/rooms/[id]` (public room detail) | **FUNCTIONAL** | Dynamic room detail page with pricing, images, amenities | 171 | `src/data/rooms.json` |
| `/admin` (admin dashboard) | **SKELETON** | Dashboard with hardcoded stats, links to subpages | 296 | None (hardcoded "12 rooms", "--" for metrics) |
| `/admin/rooms` (admin room list) | **FUNCTIONAL** | Room manager displaying all rooms from DB | 57 | `property.db` (SQLite) via server actions |
| `/admin/rooms/[id]` (admin room detail) | **PARTIAL** | Room detail editor (missing CSS module) | - | `property.db` via server actions |
| `/admin/reservations` | **NOT BUILT** | Link exists, no page | - | - |
| `/admin/platforms` | **NOT BUILT** | Link exists, no page | - | - |
| `/admin/calendar` | **NOT BUILT** | Link exists, no page | - | - |
| `/admin/analytics` | **NOT BUILT** | Link exists, no page | - | - |
| `/admin/settings` | **NOT BUILT** | Link exists, no page | - | - |

**Key Finding**: Public pages work from JSON. Admin pages work from SQLite. **No integration between the two data sources**. Missing admin pages are critical PMS functions.

---

## Data Source Map

| File | Format | Content | Records | Status | Notes |
|------|--------|---------|---------|--------|-------|
| `data/core/inventory.yaml` | YAML | **Master inventory** - Room types, pricing, beds, features | 12 rooms | **SSOT CLAIMED** | Most complete metadata, includes `type_fr`, `amenities`, validated 2026-01-24 |
| `src/data/rooms.json` | JSON | Public website room data | 12 rooms | **ACTIVE** | Used by public pages, subset of YAML data with descriptions |
| `src/data/facilities.json` | JSON | Property facilities (pool, spa, garden, hall) | 4 facilities | **ACTIVE** | Placeholder data ("A confirmer - M. Thaifa") |
| `property.db` (SQLite) | SQLite | **Expedia-spec database** - Rooms, beds, amenities normalized | 12 rooms + relational | **ACTIVE** | Used by admin pages, most structured, has verification_status field |
| `sources/hotelrunner-api/data/reservations/*.json` | JSON | Extracted reservation data from HotelRunner | 96 reservations (sample) | **ARCHIVE** | Browser automation output, not live integration |
| `public/images/rooms/*.jpg` | Images | Room photos (01_main.jpg through 12_main.jpg) | 12 images | **ACTIVE** | One main image per room |

**Schema Details (property.db)**:
- `rooms` table: id (R01-R12), expedia_type, internal_name, floor, occupancy_adults, size_m2, is_smoking, has_kitchen, base_rate_mad, verification_status
- `beds` table: room_id FK, type (King/Sofa Bed), width_cm, count
- `amenities` table: room_id FK, category (View/Outdoor/Bathroom/Climate/Layout/Hardware), name, value

**Critical Issue**: **THREE SOURCES OF TRUTH** for room data. YAML claims SSOT status but JSON and SQLite are actively used. No sync mechanism between them.

---

## HotelRunner Integration Code

### Integration Type: Browser Automation (Not API)

**Status**: ⚠️ **Manual intervention required** - Profile persistence broken

**Files**:
- `sources/hotelrunner-api/extract_reservations.py` (227 lines) - Python script using `agent-browser` CLI
- `sources/hotelrunner-api/STATUS-FINAL.md` - Comprehensive 298-line status doc
- `sources/hotelrunner-api/OPTIONS-ANALYSIS.md` - Analysis of 6 integration options
- `sources/hotelrunner-api/EXTRACTION-GUIDE.md` - Usage guide with limitations
- `sources/hotelrunner-api/TEST-RESULTS.md` - Test results and limitation docs

**What Works**:
- ✅ Browser automation can extract 96 reservations (14 fields each)
- ✅ Data structure: status, room, channel, client_name, confirmation_number, check_in, check_out, room_type, total, payment_total, inventory_type, confirmation_status, booking_date, nationality
- ✅ Performance: ~15 seconds for 96 reservations
- ✅ All data accessible via DOM scraping

**What Doesn't Work**:
- ❌ `agent-browser --profile` doesn't persist session cookies
- ❌ Requires manual authentication each run
- ❌ No real-time webhooks
- ❌ No REST API integration (requires HTTPS domain + callback URL setup)

**Current Process**: Manual daily extraction (5-10 min/day)

**Recommendation from docs**: Court terme = manual extraction, Moyen terme = investigate cookie export/import or Playwright, Long terme = REST API if volume increases

**Key Limitation**: This is NOT a live integration. It's a screen-scraping fallback.

---

## Agent Workflows

**Location**: `.agents/workflows/`

| Workflow | Purpose | Status | Lines |
|----------|---------|--------|-------|
| `reservation.md` | Complete process for creating HotelRunner reservation | v0.1.0-alpha.0 | 85 |
| `pricing.md` | Pricing strategy workflow | Active | - |
| `guest-communication.md` | Guest communication workflow | Active | - |
| `git-session-start.md` | Git workflow for session start | Active | - |
| `README.md` | Workflows index | Active | - |

**Agent Infrastructure**:
- `.agents/artifacts/` - Screenshots, audits, Gemini task history
- `.agents/plans/` - 5 transformation/standardization plans
- `.agents/input/jobs/missions/` - Mission queue (P0/P1/P2/P3 priorities)
  - 2 completed missions (chambre4-gouram, chambre5-sync-investigation)
  - 7 pending missions (room-restructuring, hotelrunner-admin-access, booking-data, image-organization, hotelrunner-api-scout, property-type-investigation, validation-pdf)
- `.agents/sessions/` - 2 session logs (inter-agent-sync, agent-unification)

**Documentation Structure** (`docs/` - 41 directories):
- `docs/knowledge/` - Client profiles, communications, finance, processes, property info
- `docs/leadership/` - DECISIONS.md, PRIORITIES.md, VISION.md, stakeholders, team
- `docs/operations/` - CREDENTIALS.md, Expedia integration, rules
- `docs/project/` - Architecture, audit, standards, TODOs, structure
- `docs/specs/hotel/` - Hotel specifications (referenced but missing)
- `docs/reports/` - 4 reports including BRUTAL-AUDIT-REPORT-2026-01-16.md

**Key Finding**: Extensive agent orchestration infrastructure exists but is project management focused, not code generation focused.

---

## Existing Scripts

| Script | Purpose | Status | Language |
|--------|---------|--------|----------|
| `scripts/migrate_rooms_to_db.ts` | Migrate room data from flat files to SQLite | **COMPLETED** | TypeScript |
| `scripts/verify_db.ts` | Verify SQLite database integrity | Active | TypeScript |
| `scripts/test_expedia_auth.ts` | Test Expedia API authentication | Active | TypeScript |
| `scripts/mark_all_verified.ts` | Mark all rooms as VERIFIED in DB | Active | TypeScript |
| `fix_images.sh` | Fix image paths (699 bytes) | Active | Bash |

**Migration Evidence**: Archive at `archive/legacy_structure/rooms_deprecated_20260124.md` indicates room data was migrated from Markdown to SQLite on 2026-01-24.

---

## What's REUSABLE

### ✅ HIGH VALUE - Keep & Migrate

1. **SQLite Schema** (`src/db/schema.sql` + `property.db`)
   - **Why**: Well-normalized, Expedia-spec compatible, relational structure
   - **Use**: Foundation for new PMS database schema
   - **Caution**: Needs sync with YAML master inventory

2. **Room Data** (12 rooms with complete metadata)
   - **Why**: Validated pricing (2026-01-13), complete bed/amenity/feature data
   - **Use**: Seed data for new PMS
   - **Source**: `data/core/inventory.yaml` (most complete)

3. **Room Images** (12 professional photos)
   - **Why**: Production-ready assets
   - **Use**: New PMS UI
   - **Location**: `public/images/rooms/*.jpg`

4. **Workflow Documentation** (`.agents/workflows/`)
   - **Why**: Captures business processes (reservation, pricing, guest communication)
   - **Use**: Requirements for new PMS features
   - **Format**: Markdown, easy to reference

5. **HotelRunner Extraction Logic** (screen scraping patterns)
   - **Why**: Fallback if API unavailable
   - **Use**: Emergency data recovery
   - **Caution**: Fragile, requires maintenance

### ⚠️ MEDIUM VALUE - Reference Only

6. **Next.js Component Patterns** (Navigation.tsx, feature-based structure)
   - **Why**: Shows feature organization pattern
   - **Use**: Inspiration for new UI structure
   - **Caution**: Only 368 LOC, mostly skeleton

7. **Documentation Structure** (`docs/` hierarchy)
   - **Why**: Well-organized knowledge base
   - **Use**: Migrate useful docs to new repo
   - **Caution**: 41 directories, needs filtering

8. **Agent Mission Queue** (`.agents/input/jobs/missions/`)
   - **Why**: Captures outstanding work items
   - **Use**: Convert to Linear/TASKS.md for new project
   - **Items**: 7 pending missions

### ❌ LOW VALUE - Discard or Archive

9. **Public Pages Code** (`src/app/page.tsx`, `src/app/rooms/[id]/page.tsx`)
   - **Why**: 252+171 LOC of inline styles, no design system
   - **Use**: None - rebuild with Vite+React
   - **Reason**: Next.js abandoned per tech stack decision (DEC-003)

10. **Admin Pages Code** (`src/app/admin/**`)
    - **Why**: Skeleton only, missing critical pages, no CSS modules
    - **Use**: None - requirements only
    - **Reason**: Incomplete implementation

11. **JSON Data Files** (`src/data/*.json`)
    - **Why**: Duplicate of YAML and SQLite, no added value
    - **Use**: None - consolidate to single source
    - **Reason**: Data sync nightmare

---

## What to Migrate vs Rebuild

### MIGRATE (Move to New PMS Repo)

| Asset | Destination | Format |
|-------|-------------|--------|
| SQLite schema | `db/schema.sql` | SQL |
| Room data (YAML) | `db/seeds/rooms.yaml` | YAML |
| Room images | `public/images/rooms/` | JPG |
| Workflows | `docs/workflows/` | Markdown |
| HotelRunner docs | `docs/integrations/hotelrunner/` | Markdown |
| Agent missions | Linear (as epics/tasks) | Convert |
| Leadership docs | `docs/project/` (selected) | Markdown |

### REBUILD (Requirements Only)

| Feature | Reason |
|---------|--------|
| Public website | Vite+React, design system, responsive |
| Admin dashboard | FastAPI backend, proper PMS features |
| Reservations management | Live integration (not browser automation) |
| Calendar/availability | Real-time sync, not static |
| Platform integrations | API-first (HotelRunner REST, Expedia, Booking) |
| Analytics | Actual metrics, not hardcoded "--" |

### ARCHIVE (Keep for Reference)

| Asset | Reason |
|-------|--------|
| Next.js app code | Tech debt example, shows what NOT to do |
| Browser automation scripts | Fallback if APIs fail |
| Migration scripts | Historical record |
| BRUTAL-AUDIT-REPORT-2026-01-16.md | Lessons learned |

---

## Key Findings

### 🔴 CRITICAL ISSUES

1. **No Single Source of Truth**: Room data exists in 3 places (YAML, JSON, SQLite) with NO sync mechanism. YAML claims SSOT but is not used by app.

2. **No Live Integrations**: HotelRunner "integration" is manual browser automation requiring daily human intervention. No webhooks, no real-time data.

3. **Admin Pages Missing**: 6 of 11 admin pages are links to nowhere. Core PMS functions (reservations, calendar, platforms, analytics, settings) don't exist.

4. **Data Isolation**: Public pages use JSON, admin pages use SQLite. Changes in admin don't propagate to public site.

### 🟡 MEDIUM ISSUES

5. **No Design System**: Inline styles everywhere (252 lines in homepage alone). No reusable component library.

6. **No Authentication**: Admin pages have no auth. Anyone with URL can access.

7. **Tech Debt**: Next.js App Router (368 LOC) is skeleton code. Missing CSS modules break admin detail pages.

8. **Image Management**: Only one image per room. No gallery, no room-specific photo management.

### 🟢 STRENGTHS

9. **Good Schema Design**: SQLite schema is well-normalized, Expedia-compatible, extensible.

10. **Complete Room Data**: 12 rooms fully documented with pricing, beds, amenities, features, photos.

11. **Process Documentation**: Workflows capture real business processes (reservation creation, pricing, guest communication).

12. **Agent Infrastructure**: Sophisticated task queue, session tracking, artifact storage shows mature operational thinking.

### 💡 INSIGHTS

13. **Migration Already Started**: Room data migrated from Markdown to SQLite on 2026-01-24, but JSON files not updated. Migration incomplete.

14. **Professional Approach**: OPTIONS-ANALYSIS.md, DECISION-BRIEF.md, STATUS-FINAL.md show methodical problem-solving. This wasn't cowboy coding.

15. **Real Usage Evidence**: 96 reservations in HotelRunner extraction data. This is a working business, not a toy project.

16. **Expedia Integration Planned**: `test_expedia_auth.ts` script exists. Expedia was on the roadmap.

---

**END OF AUDIT**

**Next Steps for PMS Rebuild**:
1. Export SQLite schema → new repo as foundation
2. Consolidate room data (YAML as master) → seed new DB
3. Copy room images → new public assets
4. Extract workflow requirements → Linear epics
5. Archive this codebase → reference only
6. Start fresh with Vite+React+FastAPI stack (per DEC-003)

**Estimated Migration Effort**: 2-3 days (mostly data consolidation and asset copying)
**Estimated Rebuild Effort**: 4-6 weeks (based on tech stack decision, not extending this codebase)


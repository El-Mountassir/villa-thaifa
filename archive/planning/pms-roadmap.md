# Plan: Villa Thaifa Property Management System

**Status**: Phase 0 NOT STARTED — Prerequisites in progress
**Current Phase**: Pre-execution setup (CLI installs, repo creation)
**Last Updated**: 2026-02-13

---

## Quick Status

| Phase | Status | Progress | Key Blocker |
|-------|--------|----------|-------------|
| **Prerequisites** | IN PROGRESS | 2/8 complete | Need Codex CLI + Gemini CLI install |
| **Phase 0: Foundation** | NOT STARTED | 0/5 deliverables | Blocked by prerequisites |
| **Phase 1: Documents** | NOT STARTED | 0/12 deliverables | Blocked by Phase 0 |
| **Phase 2: MVP** | NOT STARTED | 0/7 deliverables | Blocked by Phase 1 |
| **Phase 3: Reservations** | NOT STARTED | 0/5 deliverables | Blocked by Phase 2 |
| **Phase 4: Full Feature** | NOT STARTED | 0/6 deliverables | Blocked by Phase 3 |

---

## Context

Villa Thaifa is a 12-room boutique luxury hotel in Marrakech (Palmeraie) owned by Said Thaifa (78 years old). Omar El Mountassir is leading its digital transformation. Said currently manages everything from memory + HotelRunner (channel manager, actively used). The goal: a web app where both Omar and Said can manage the property, with progressive automation to reduce Said's manual burden.

**The problem**: The existing project (`~/villa-thaifa/`, 1.1GB, 1435 files) is massively over-documented (382 markdown files) but under-built (Next.js skeleton barely functional, 7% of 14 requirements completed). Data is scattered across YAML, SQLite, JSON, and markdown. Two divergent GitHub repos exist. No working app for Said to use.

**The solution**: Fresh start with a clean repo. Migrate essential data only. Build a working app fast. Deploy on Vercel for Said's browser access.

### Key Facts
- **Rooms**: 12 (verified in rooms.yaml + property.db)
- **OTAs**: 5 channels — Booking.com, Expedia, Airbnb, Agoda, Trip.com
- **Channel Hub**: HotelRunner (actively used by Said, proven integration)
- **Owner Contact**: said_thaifa@hotmail.fr (confirmed, Hotmail may have delays)
- **Currency**: EUR primary, MAD secondary (auto-fetch exchange rate API)
- **Languages**: French (Said), English (Omar)
- **Room Photo Storage**: CDN (Cloudinary or Vercel Image Optimization)
- **Task Tracking**: Linear + GitHub (Linear auto-syncs to GitHub)

---

## Current State (from 6 investigation agents)

### Data Assets (all verified, no data loss)
- `ssot/rooms.yaml` — 12 rooms, pricing EUR/MAD, features, OTA mapping (verified 2026-01-24)
- `property.db` — SQLite: 12 rooms, 21 beds, 94 amenities
- `docs/knowledge/villa-thaifa/policies/events-privatization.md` — Full privatization policy (2,000€/night)
- `docs/operations/expedia/onboarding_capture_v1.md` — Expedia onboarding (steps 1-4, 16.5% commission)
- `docs/specs/knowledge/platforms/hotelrunner/channel-mapping.md` — Booking.com mapping (8 room types, Two-Way XML)
- `docs/specs/knowledge/villa-thaifa/state/current/reserverations/reservations.md` — 96 extracted reservations
- `.env` — Live HotelRunner, Booking.com, Expedia credentials
- `sources/hotelrunner-api/` — API research, browser automation script (working, auth persistence broken)
- `.agents/workflows/` — reservation, pricing, guest-communication workflows

### What's Partially/Not Captured
- Seasonal/dynamic pricing (planned, not finalized)
- Additional OTA channels beyond initial 3 (Trip.com contract imminent)
- Breakfast group rates, children policies, spa pricing (need Said's input)
- Full check-in procedures, staff schedules

### Scattered Content in ~/omar/ (small, archival)
- `archives/grid/comms/clients/villa-thaifa.md` — communications summary
- `operational/productivity/memory/people/said-thaifa.md` — contact record
- `/media/director/data/.../villa-thaifa-pre-prompt-refactoring-*.tar.gz` — 463MB backup (2026-01-15)

### GitHub Situation
- `El-Mountassir/villa-thaifa-property-management` — Primary, 30 commits, 1 unpushed
- `omar-elmountassir/villa-thaifa` — Secondary, last push 2026-01-28
- **Decision**: New private repo `omar-elmountassir/villa-thaifa-pms`. Archive both existing repos.

### App Audit Findings (from research)
- Existing app: 368 LOC Next.js skeleton (App Router)
- 3 conflicting data sources: YAML (claims SSOT), JSON (public site), SQLite (admin)
- Browser automation for HotelRunner (NOT API) — broken, requires daily manual auth
- 5 agent workflows exist in .agents/workflows/
- **Recommendation**: Fresh start, migrate only data/assets/docs

---

## Tech Stack (for THIS project)

See `tech-decisions.md` for full rationale.

| Layer | Choice | Reasoning |
|-------|--------|-----------|
| **Framework** | Next.js 15 (App Router) | Vercel-native, single deployment, API routes built-in. Pragmatic for 2-user app. |
| **Database** | Vercel Postgres (Neon) | Free tier (256MB), serverless-compatible, standard SQL. SQLite won't work on Vercel serverless. |
| **Auth** | NextAuth.js + magic links | No password friction for Said (78 years old). Email → click → logged in. |
| **UI** | shadcn/ui + Tailwind CSS | Accessible, mobile-responsive, dark mode support. |
| **i18n** | next-intl | French primary (Said), English secondary (Omar). Server-side rendering. |
| **Validation** | Zod | Already used in existing project. Type-safe forms. |
| **OTA Client** | Custom REST wrapper | HotelRunner API integration. Read-only first, bidirectional later. |
| **Deployment** | Vercel (free tier) | Zero infra management. Auto-deploy on push. Said gets a URL. |
| **Monitoring** | Vercel Analytics (free) | Basic page views, web vitals. Enough for 2 users. |
| **Exchange Rate** | Auto-fetch API | TBD: ExchangeRate-API.com or fixer.io (both have free tiers) |

**Cost**: $0/month (free tiers: Vercel, Neon, NextAuth). Upgrade to Vercel Pro ($20/mo) only if needed.

---

## Pre-Execution Prerequisites (DO NOT skip)

Before ANY code is written, these must be done:

| # | Prerequisite | Status | Owner | Notes |
|---|--------------|--------|-------|-------|
| 1 | Install Codex CLI + auth | ✅ DONE | Omar | v0.101.0 installed |
| 2 | Install Gemini CLI + auth | ✅ DONE | Omar | v0.28.2 installed |
| 3 | Create delegation skill | ⏳ PENDING | Nova (Sonnet agent) | Extract from plan to ~/.claude/skills/ |
| 4 | Test Codex on 1 real task | ⏳ PENDING | Omar + Nova | Validate reliability claims before relying on it |
| 5 | Test Gemini CLI on 1 real task | ⏳ PENDING | Omar + Nova | Validate quality + free tier limits |
| 6 | Finalize tech stack decision | ✅ DONE | Omar | Next.js confirmed (see tech-decisions.md) |
| 7 | Create new GitHub repo | ⏳ PENDING | Omar | `omar-elmountassir/villa-thaifa-pms` (private) |
| 8 | Linear workspace setup | ⏳ PENDING | Omar | For this project specifically |

---

## Phase 0: Foundation (Day 1-2)

**Goal**: Clean repo, database schema, SSOT data seeded, ready to code.

### Deliverables
- [ ] 1. New private GitHub repo: `omar-elmountassir/villa-thaifa-pms`
- [ ] 2. Project scaffold: Next.js + TypeScript + Tailwind + shadcn/ui
- [ ] 3. Vercel Postgres schema (migrated from SQLite)
- [ ] 4. SSOT data seeded (12 rooms, beds, amenities, pricing)
- [ ] 5. Essential docs migrated from old repo (policies, OTA mapping, credentials config)

### Key Actions
```bash
1. gh repo create omar-elmountassir/villa-thaifa-pms --private
2. npx create-next-app@latest villa-thaifa-pms --typescript --tailwind --app --src-dir
3. Design Postgres schema from property.db + rooms.yaml
4. Create seed script (rooms.yaml → Postgres)
5. Migrate: .env.example, key policies, OTA mapping docs
6. Archive old repos (add deprecation notice to README)
```

### Database Schema (from existing property.db + rooms.yaml)

```sql
-- Core tables
rooms (id, internal_name, type, floor, size_m2, capacity_adults, is_smoking, has_kitchen,
       base_rate_eur, base_rate_mad, description_en, description_fr,
       verification_status, verified_at, created_at, updated_at)

beds (id, room_id FK, type, width_cm, count)

amenities (id, room_id FK, category, name, value)

-- New tables (not in old DB)
reservations (id, external_id, channel, guest_name, guest_email,
              room_id FK, check_in, check_out, total_eur, total_mad,
              status, payment_status, source, created_at)

pricing_rules (id, room_id FK, name, type, start_date, end_date,
               rate_eur, rate_mad, min_nights, created_at)

policies (id, key, value_fr, value_en, category, updated_at)

users (id, email, name, role, locale, created_at)
```

### Delegation
- **Sonnet agent**: Scaffold project, install dependencies, configure Tailwind + shadcn/ui
- **Sonnet agent**: Write migration SQL + seed script from rooms.yaml
- **Codex review**: Validate scaffold + schema quality
- **Omar**: Create GitHub repo, connect Vercel, set up Vercel Postgres

### Definition of Done
- [ ] `pnpm dev` runs locally with empty dashboard
- [ ] Vercel Postgres has 12 rooms seeded
- [ ] GitHub repo has first commit with clean scaffold
- [ ] Old repos have deprecation notice

---

## Phase 1: Specification Documents (Day 2-4)

**Goal**: Complete, approved specs. No code yet — pure documentation.

### Deliverables (12 files in `docs/`)

**MUST-HAVE (8 docs)**:
- [ ] 1. **PRD.md** — Product Requirements Document (French, for Said's context)
- [ ] 2. **SRS.md** — Software Requirements Specification
- [ ] 3. **ARCHITECTURE.md** — System Design (C4 diagrams, data flow)
- [ ] 4. **DB_SCHEMA.md** — Database Design (expanded from Phase 0)
- [ ] 5. **API_SPEC.md** — HotelRunner API contract + internal API routes
- [ ] 6. **CHANNEL_MAPPING.md** — Room type → OTA mapping for all 5 channels
- [ ] 7. **DATA_DICTIONARY.md** — All entities, fields, types, relationships
- [ ] 8. **SECURITY_SPEC.md** — Auth flow, data protection, PCI considerations

**NICE-TO-HAVE (4 docs, if capacity)**:
- [ ] 9. **WIREFRAMES_CHECKLIST.md** — Key screen wireframes for Said's approval
- [ ] 10. **DEPLOYMENT_RUNBOOK.md** — Vercel setup, env vars, DNS, monitoring
- [ ] 11. **WEBHOOK_SPEC.md** — HotelRunner webhook handling
- [ ] 12. **USER_FLOW_DIAGRAMS.md** — Said's journey, Omar's admin journey

### PRD Details (French, for Said)
- User personas (Said: owner, non-technical, mobile | Omar: admin, technical, desktop)
- User stories (25-30 stories across 4 epics)
- Feature priority matrix (MoSCoW)

### SRS Details
- Functional requirements (CRUD, reservations, OTA sync, reporting)
- Non-functional (mobile-responsive, <3s load, French i18n, accessible)
- Integration requirements (HotelRunner API, Booking.com, Expedia, Airbnb, Agoda, Trip.com)

### ARCHITECTURE.md Details
- C4 diagrams (context, container, component)
- Data flow: App ↔ Vercel Postgres ↔ HotelRunner ↔ OTAs
- Auth flow: Magic link → session → role-based access

### Delegation
- **Gemini 2.5 Pro**: Draft PRD from existing docs/project/BRIEF.md + docs/leadership/VISION.md + ROADMAP.md (1M context)
- **Gemini 2.5 Pro**: Draft SRS from PRD + existing Next.js pages + rooms.yaml schema
- **Sonnet agent**: Draft DB_SCHEMA.md from migration SQL + rooms.yaml structure
- **Sonnet agent**: Draft API_SPEC.md from HotelRunner research brief
- **Sonnet agent**: Draft CHANNEL_MAPPING.md (5 OTAs, room type mappings)
- **Codex review**: Validate all docs for consistency
- **Omar (orchestrator)**: Write ARCHITECTURE.md (integration boundaries, HotelRunner risk)

### Definition of Done
- [ ] All 8 MUST-HAVE docs in `docs/` directory, committed
- [ ] PRD has Said's approval (WhatsApp summary in French)
- [ ] SRS covers all Phase 2-4 features
- [ ] Architecture addresses HotelRunner integration risk (250 req/day limit)
- [ ] CHANNEL_MAPPING includes all 5 OTAs with room type → OTA code mapping

---

## Phase 2: MVP — Room & Pricing Management (Day 5-12)

**Goal**: Said can log in, view rooms, edit pricing. Deployed to Vercel.

### Deliverables
- [ ] 1. **Dashboard** — Overview: room count, occupancy %, revenue summary
- [ ] 2. **Room list** — Table/cards view, search, filter by type/floor/status
- [ ] 3. **Room detail** — View all data, edit pricing, edit amenities
- [ ] 4. **Pricing management** — Bulk price update, EUR↔MAD auto-conversion
- [ ] 5. **Auth** — Magic link login (Omar + Said)
- [ ] 6. **French UI** — All labels, buttons, errors in French (default)
- [ ] 7. **Mobile responsive** — Touch-friendly, single-column on phone

### Key Files
```
src/
├── app/
│   ├── [locale]/              # fr (default), en
│   │   ├── page.tsx           # Dashboard
│   │   ├── rooms/
│   │   │   ├── page.tsx       # Room list
│   │   │   └── [id]/page.tsx  # Room detail + edit
│   │   └── pricing/page.tsx   # Bulk pricing
│   └── api/
│       ├── rooms/route.ts     # CRUD
│       └── auth/[...nextauth]/route.ts
├── components/
│   ├── room-card.tsx
│   ├── room-form.tsx
│   ├── pricing-table.tsx
│   └── nav.tsx
├── lib/
│   ├── db.ts                  # Vercel Postgres client
│   ├── auth.ts                # NextAuth config
│   └── currency.ts            # EUR↔MAD conversion (auto-fetch API)
└── messages/
    ├── fr.json                # French strings
    └── en.json
```

### Delegation
- **Sonnet agent**: Room list page + room card component
- **Sonnet agent**: Room detail/edit page + form with Zod validation
- **Sonnet agent**: Pricing table with bulk edit + currency conversion
- **Gemini Flash-Lite**: French translation strings extraction (messages/fr.json)
- **Codex review**: Code review all components before merge
- **Omar**: NextAuth magic link setup, Vercel deployment, final review

### Definition of Done
- [ ] Said can log in via magic link on his phone
- [ ] 12 rooms displayed with French labels
- [ ] Omar can edit room pricing (EUR → auto MAD conversion via live API)
- [ ] Mobile responsive (tested 375px, 768px, 1024px)
- [ ] Deployed on Vercel (staging URL shared with Said)
- [ ] Zero TypeScript errors, all pages load <3s

---

## Phase 3: Reservations + HotelRunner (Day 13-22)

**Goal**: Real bookings from HotelRunner sync to app. Said sees calendar on phone.

### Deliverables
- [ ] 1. **Reservation list** — All bookings with filters (date, room, status, channel)
- [ ] 2. **Booking calendar** — Visual calendar view (FullCalendar.js)
- [ ] 3. **Guest profiles** — Name, email, nationality, booking history
- [ ] 4. **HotelRunner sync** — Hourly pull of reservations (read-only, Vercel Cron)
- [ ] 5. **Manual booking entry** — For walk-ins and phone bookings

### HotelRunner Integration Strategy
```
Phase 3 = READ-ONLY (low risk):
  HotelRunner → Vercel Cron (hourly) → Vercel Postgres → App UI

Safety:
  - No writes to HotelRunner
  - Idempotent sync (upsert by external_id)
  - Error logging (don't crash on API failures)
  - Dry-run mode for first week
  - Rate limit: 250 req/day, 5 req/min (batch all updates, cache locally)
```

### Key Files
```
src/
├── app/[locale]/
│   ├── reservations/
│   │   ├── page.tsx           # Reservation list
│   │   ├── [id]/page.tsx      # Booking detail
│   │   ├── calendar/page.tsx  # Calendar view
│   │   └── new/page.tsx       # Manual entry
│   └── guests/page.tsx        # Guest list
├── lib/
│   └── hotelrunner.ts         # API client (read-only, with caching)
└── app/api/
    └── cron/
        └── sync-reservations/route.ts  # Vercel Cron handler
```

### Delegation
- **Sonnet agent**: Reservation list + detail pages
- **Sonnet agent**: Calendar view with FullCalendar.js integration
- **Codex**: HotelRunner API client (reliability-critical, live system integration, rate-limit handling)
- **Codex review**: Validate API client safety (idempotent, error handling, caching)
- **Omar**: Test with LIVE HotelRunner credentials, monitor sync for 1 week

### Definition of Done
- [ ] Calendar shows real bookings from HotelRunner
- [ ] Said can see upcoming check-ins on his phone
- [ ] Sync runs hourly without errors for 7 consecutive days
- [ ] Manual booking entry works (walk-ins)
- [ ] No duplicate reservations (idempotent upsert)
- [ ] Rate limit not exceeded (monitor: should be <100 req/day with caching)

---

## Phase 4: OTA Sync + Automation (Day 23-35)

**Goal**: Full bidirectional sync. Said manages everything from app, not HotelRunner UI.

### Deliverables
- [ ] 1. **Bidirectional HotelRunner sync** — Push availability + pricing changes
- [ ] 2. **OTA channel dashboard** — Sync health per channel (Booking.com, Expedia, Airbnb, Agoda, Trip.com)
- [ ] 3. **Revenue reporting** — Daily/weekly/monthly, EUR + MAD
- [ ] 4. **Occupancy chart** — Room utilization % over time
- [ ] 5. **Guest communication templates** — French email templates for confirmations, reminders
- [ ] 6. **Seasonal pricing rules** — Date-based rate overrides

### Bidirectional Sync Safety
```
Phase 4 = READ + WRITE (high risk):
  App → HotelRunner (push availability, pricing)

Safety measures:
  1. DRY RUN mode for first 3 days (log API calls, don't execute)
  2. Rate limit: max 1 update per room per hour (batch all changes)
  3. Said email notification before EVERY pricing push (first month)
  4. 7-day rollback history for all pricing changes
  5. Staging test with non-production data first (if HotelRunner supports it)
  6. Transaction verification (use transaction_id endpoint to confirm success)
```

### Delegation
- **Codex**: HotelRunner push API wrapper (reliability-critical, bidirectional sync)
- **Sonnet agent**: Revenue/occupancy reporting pages with Recharts
- **Sonnet agent**: Email templates (French) + Resend integration
- **Gemini 2.5 Pro**: Seasonal pricing logic research + implementation spec
- **Codex review**: Full code review before go-live (safety-critical)
- **Omar**: Approve dry-run results, go-live decision, Said communication

### Definition of Done
- [ ] Pricing changes in app sync to HotelRunner within 30 minutes
- [ ] Revenue reports match HotelRunner data (±2%)
- [ ] Said receives email notification for every pricing sync
- [ ] Seasonal pricing rules applied correctly (test with past dates)
- [ ] Production deployment: `villa-thaifa-pms.vercel.app`
- [ ] All 5 OTAs show in channel dashboard with sync status

---

## Data Migration Strategy

See `data-inventory.md` for full details.

### What Migrates to New Repo

| Source | Destination | Method |
|--------|-------------|--------|
| `ssot/rooms.yaml` (12 rooms) | Vercel Postgres `rooms` table | Seed script |
| `property.db` beds/amenities | Vercel Postgres `beds` + `amenities` | Migration script |
| `.env.example` | `.env.example` (no secrets) | Manual copy |
| Key policies (events, cancellation) | `docs/policies/` (3-4 files max) | Agent extracts |
| OTA mapping (channel-mapping.md) | `docs/integrations/` | Manual copy |
| HotelRunner API research | `docs/integrations/hotelrunner.md` | Agent summarizes |
| Reservation extraction script | `scripts/legacy/` | Reference only |

### What Does NOT Migrate
- 382 markdown docs (over-documentation, archived in old repo)
- Agent infrastructure (.agents/, .planning/) — redesign from scratch
- Lux collaboration artifacts — historical only
- 127 photos — managed via HotelRunner/OTA platforms, not our repo
- Linear task references — new project, new task tracking

### Scattered ~/omar/ Content
- `said-thaifa.md` contact → stays in ~/omar/ (it's Omar's personal contact book)
- Grid archive files → stay in ~/omar/archives/ (historical)
- 463MB backup on /media/ → stays there (disaster recovery only)

---

## Verification Plan

### Per-Phase Verification
- **Phase 0**: `pnpm build` succeeds, DB has 12 rows in rooms table
- **Phase 1**: Docs reviewed by Omar, no contradictions between PRD/SRS/ARCH
- **Phase 2**: Manual QA on mobile (Said's phone), lighthouse score >90
- **Phase 3**: 7-day sync stability (zero errors, zero duplicates)
- **Phase 4**: Dry-run comparison (app data vs HotelRunner UI, spot-check 10 bookings)

### End-to-End Test (Phase 2+)
1. Said opens `villa-thaifa-pms.vercel.app` on phone
2. Receives magic link email, clicks, logs in
3. Sees 12 rooms in French with correct pricing
4. Edits Room 01 price from 169€ to 179€
5. Price auto-converts to MAD (via live API)
6. Saves, refreshes, price persists
7. (Phase 3+) Calendar shows today's bookings
8. (Phase 4+) Price change syncs to HotelRunner within 30 min

---

## Resolved Questions

Previously open questions, now resolved:

1. **Said's email for magic links** — ✅ said_thaifa@hotmail.fr (confirmed, Hotmail may have delays)
2. **EUR↔MAD rate update** — ✅ Auto-fetch from API (not manual .env) — need to pick API provider
3. **Room photos in app** — ✅ CDN via Cloudinary or Vercel Image Optimization
4. **Linear integration** — ✅ Continue using Linear for task tracking + GitHub auto-sync
5. **Additional OTAs** — ✅ 5 total: Booking.com, Expedia, Airbnb, Agoda, Trip.com (contract signing via HotelRunner)
6. **Booking.com special requirement** — ✅ Said wants rooms by room NUMBER (not just type) — sync needed
7. **Trip.com status** — ✅ Contract imminent, must prepare onboarding

---

## Summary

| Phase | Duration | Core Deliverable | Said Can... |
|-------|----------|-----------------|-------------|
| **Prerequisites** | 2-3 days | CLI setup, repo creation | — |
| **0: Foundation** | 2 days | Clean repo + DB + seed | — |
| **1: Documents** | 3 days | PRD + SRS + Architecture + 9 more docs | Review PRD |
| **2: MVP** | 8 days | Working CRUD app on Vercel | View/edit rooms & pricing |
| **3: Reservations** | 10 days | Calendar + HotelRunner sync | See bookings on phone |
| **4: Full Feature** | 13 days | Bidirectional sync + reports | Manage everything from app |
| **Total** | **~38-40 days** | **Full PMS on Vercel** | **Replace manual workflow** |

---

## Changelog

### 2026-02-13 — Plan Updated with New Information
- **Resolved questions**: Said's email, EUR/MAD rate handling, room photos, Linear integration, all 5 OTAs identified
- **Added HotelRunner research**: 150+ OTAs, 250 req/day limit, no SDK (need custom wrapper), API structure documented
- **Expanded Phase 1**: From 4 docs to 12 docs (8 MUST-HAVE, 4 NICE-TO-HAVE) including API_SPEC, CHANNEL_MAPPING, DATA_DICTIONARY, SECURITY_SPEC
- **App audit findings**: 368 LOC skeleton, 3 conflicting data sources, browser automation broken → fresh start confirmed
- **Added Chrome MCP**: Available for browser automation (agents can use Chrome)
- **Added Linear MCP**: Connected to Claude Code
- **Living roadmap rules**: Updated at minimum each phase end, status tracking with checkboxes, decisions logged with dates
- **Plan split**: Extracted delegation-framework.md, data-inventory.md, tech-decisions.md into separate files
- **Status section**: Added at top showing current phase + progress

### 2026-02-10 — Original Plan Created
- Initial 4-phase structure
- Tech stack finalized (Next.js, Vercel Postgres)
- Multi-model delegation framework designed
- Data migration strategy documented

---

_This is a LIVING ROADMAP — update at each phase completion._

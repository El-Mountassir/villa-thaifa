# ROADMAP -- Villa Thaifa

> **Last Updated**: 2026-02-24
> **Current Phase**: Phase 0 -- Data Foundation

---

## Strategic Principle

**App-first validation**: Data gaps are flagged, not chased. Said validates through the app interface, not through Omar. This eliminates constant back-and-forth, reduces Said's burden, and makes validation trackable and auditable.

---

## Table of Contents

- [North Star](#north-star)
- [Phase 0: Data Foundation (NOW)](#phase-0-data-foundation-now)
- [Phase 1: App Prerequisites](#phase-1-app-prerequisites)
- [Phase 2: App MVP](#phase-2-app-mvp)
- [Phase 3: Content Layer](#phase-3-content-layer)
- [Phase 4: Advanced Operations](#phase-4-advanced-operations)
- [Long-Term: LHCM-OS Vision](#long-term-lhcm-os-vision)
- [Go Siyaha Opportunity](#go-siyaha-opportunity)
- [KPIs](#kpis)
- [References](#references)

---

## North Star

> One consultant + AI agents = full management of 10+ hotel properties.

Villa Thaifa is the first property. The app we build here becomes the template for every property that follows.

---

## Phase 0: Data Foundation (NOW)

**Objective**: Audit and restructure all data in `data/` so it is complete, verified, and ready for database ingestion.

**Why first**: The codifiability analysis identified 15 proposed DB models across 4 tiers. The data is already highly structured (JSON configs, YAML blocks, 24-column table contracts), but fields still carry `owner_pending` confidence and some schemas need hardening. Building an app on incomplete data creates drift from day one.

### Key Deliverables

- [ ] Complete data audit: every field in every room profile verified or explicitly marked `owner_pending`
- [ ] Flag data gaps for in-app validation by Said (Phase 2 deliverable) — mark all `owner_pending` fields, do not chase Said directly
- [ ] Finalize operational config JSONs (check-in, housekeeping, maintenance, emergency -- currently placeholder)
- [ ] Reconcile OTA room type mapping (8 HotelRunner types vs 12 physical rooms)
- [ ] Image inventory cleanup: consistent naming, hero images identified per room
- [ ] All open conflicts in `ops/decisions/open-conflicts-registry.md` resolved or explicitly deferred

### Success Criteria

- Zero unresolved data conflicts blocking app development
- All 12 room profiles match the template contract (`context/meta/templates/room-profile-template.md`)
- `data_confidence` field populated for every data point (verified, assumed, or owner_pending)
- Operational JSON configs have real values (not placeholder TODOs) for any field the MVP will consume

---

## Phase 1: App Prerequisites

**Objective**: Complete the planning and technical foundation required before writing application code.

### Key Deliverables

- [ ] PRD/SRS document (functional requirements, user stories, acceptance criteria)
- [ ] Tech stack finalization (proposed: Next.js + Tailwind + shadcn/ui; alternatives evaluated: FastAPI, Hono, Cloudflare Workers + D1)
- [ ] Design system definition (dark theme, Said-friendly UX, Dutch/French UI, approval-first patterns)
- [ ] Database schema definition (Prisma/Drizzle) based on the 15 proposed models from the codifiability analysis
- [ ] Seed script that parses existing JSON/YAML/MD files into DB records, validated field-by-field against source files
- [ ] Auth approach finalized (Auth0 free tier vs JWT baseline)
- [ ] Deployment target confirmed (local-first, then Vercel or VPS -- SQLite needs persistent storage)

### Success Criteria

- PRD approved by Omar
- Schema covers all Tier 1 models: Room, RoomBed, RoomView, RoomBathroom, RoomLocalization, RoomOTAMapping, Rate, ExchangeRate, Property, PropertyRating, PropertyPolicy, Facility, FacilityAttribute, Reservation, Channel, Contact, Tax
- Seed script runs and produces a database matching current file data with zero discrepancies
- Said UX requirements documented and incorporated into design system

---

## Phase 2: App MVP

**Objective**: Ship a working app with the operational core -- property dashboard, room management, and reservation viewer.

**Data strategy**: JSON config files for MVP operational workflows (check-in, housekeeping), DB-driven for structured data (rooms, rates, bookings, property, channels, contacts). This follows the codifiability analysis recommendation: JSON config now, designed for DB-driven migration later.

### Key Deliverables

- [ ] Property and Rooms Dashboard (property overview, 12 room cards, pricing EUR/MAD, policies, facilities)
- [ ] Said's validation interface — interactive checklist for Said to confirm/correct data directly in the app (pool access, operational configs, contact details, all `owner_pending` fields — single-tap approval)
- [ ] HotelRunner reservation extraction viewer (daily batch, 96+ reservations)
- [ ] DB models for Tier 1 entities deployed and seeded
- [ ] API layer (REST endpoints for agents and UI)
- [ ] Dual-source data pattern: DB is write target, files kept as read-only backup during transition

### Modules

1. **Property and Rooms Dashboard** -- the seed page. Property overview, ratings, 12 room cards, pricing (EUR/MAD), capacity, policies, facilities.
2. **Said Validation Checklist** -- interactive version. Maps 1:1 to `owner_pending` fields. Said confirms, app updates confidence to `verified`.
3. **Reservation Viewer** -- daily batch extraction from HotelRunner. Guest name, dates, room type, amount, channel, status.

### Success Criteria

- Dashboard loads with real data from DB (not hardcoded)
- Said can open the app and see essential status in under 10 seconds
- Reservation extraction runs daily and populates the viewer
- Seed script verified: DB content matches file-based source of truth

---

## Phase 3: Content Layer

**Objective**: Add CMS and content management capabilities for Tier 2 data (descriptions, images, marketing copy).

### Key Deliverables

- [ ] Room narrative content management (descriptions EN/FR, taglines, OTA titles with character limit enforcement)
- [ ] Facility description management (structured attributes in DB, narrative as markdown or text field)
- [ ] Image gallery management (metadata model: sort order, hero selection, alt text -- images served from filesystem/CDN, not DB)
- [ ] Booking calendar / unified availability view (all OTAs consolidated)
- [ ] OTA status dashboard (channel sync status, last sync time, errors)
- [ ] Housekeeping status board

### Success Criteria

- Omar or Said can edit marketing copy through the app
- OTA listings manageable from the app (room titles, descriptions, amenity toggles)
- Availability visible across all connected channels in one view

---

## Phase 4: Advanced Operations

**Objective**: DB-driven workflows, deeper OTA integrations, automation, and revenue intelligence.

### Key Deliverables

- [ ] Migrate operational workflows from JSON config to DB-driven workflow engine
- [ ] OTA sync module: outbound rate/availability push to HotelRunner, Booking.com, Expedia
- [ ] Guest communication hub (WhatsApp Business API integration)
- [ ] Revenue dashboard (occupancy rate, RevPAR, ADR, revenue per room per channel)
- [ ] Dynamic pricing recommendations (demand-based, seasonal, event-aware -- requires Said approval)
- [ ] Competitive intelligence feed (comparable properties in Palmeraie)
- [ ] Agent activity log (which AI agents did what, errors surfaced)
- [ ] Quick actions: create internal reservation, block dates, update pricing

### Prerequisites (from revenue management vision)

- Multi-OTA distribution live (Expedia, Airbnb alongside Booking.com)
- Minimum 3-6 months historical booking data collected
- Said's explicit approval on pricing flexibility parameters (floor/ceiling rates, blackout periods)
- Direct booking channel established

### Success Criteria

- Operations 80%+ autonomous
- Omar: max 2h/week oversight per property
- Reservation response time: < 1h (automated)
- Average OTA commission reduced from 25% toward 12%

---

## Long-Term: LHCM-OS Vision

> LHCM-OS (Lightweight Hotel Channel Management OS) is a separate product. Villa Thaifa is the first pilot. LHCM-OS lives at `~/omar/professional/projects/lhcm-os/` -- NOT in this repo.

### What LHCM-OS Adds Beyond the VT App

- Multi-tenant architecture (data isolation per property)
- White-label UI (custom branding per client)
- AI C-Suite agent roles: General Manager, CFO, Revenue Manager
- "The Boardroom" -- voice/text command channel for property owners
- Target market: small luxury Moroccan properties (riads, maisons d'hotes, 5-15 rooms)

### Portfolio Targets

| Metric                   | Target       |
| ------------------------ | ------------ |
| Properties managed       | 10+          |
| Recurring revenue        | 150K+ EUR/yr |
| Omar's time per property | < 30min/week |

### Target Portfolio Profile

- Riads (e.g., Riad Bianca)
- Luxury villas (e.g., Villa Thaifa)
- Guest houses (e.g., Auberge Azul)
- Boutique hotels (e.g., Kohinor)

### Sequence

Prove (Villa Thaifa running well) --> Build (LHCM-OS MVP) --> Scale (2-3 paying clients). Do not skip steps.

---

## Go Siyaha Opportunity

| Field    | Value                                         |
| -------- | --------------------------------------------- |
| Program  | Go Siyaha (MarocPME)                          |
| Funding  | Up to 90% of digital transformation costs     |
| Ceiling  | 1M MAD                                        |
| Status   | Investigation pending                         |

This funding could cover app development, OTA integration costs, and initial LHCM-OS buildout.

---

## KPIs

### Operational (Phase 2 targets)

| KPI                  | Baseline      | Target          |
| -------------------- | ------------- | --------------- |
| Time per reservation | 15-20 min     | < 5 min         |
| Manual hours/week    | 10+           | < 3             |
| Data confidence      | ~60% verified | 95%+ verified   |

### Business (12-month horizon)

| KPI                    | Baseline | Target  |
| ---------------------- | -------- | ------- |
| Occupancy rate         | ~50%     | 70%     |
| RevPAR                 | ~100 EUR | 175 EUR |
| Avg OTA commission     | 25%      | 12%     |
| Direct booking share   | 0%       | 20%     |
| Reservation response   | >24h     | <1h     |

---

## References

| Document | Purpose |
| -------- | ------- |
| `context/meta/planning/vt-app-vision.md` | Full app vision, modules, tech stack, constraints |
| Codifiability analysis | 15 DB models, 4 tiers, gray zones -- `~/omar/core/context/domains/business/villa-thaifa/codifiability-analysis.md` |
| `project/MISSION.md` | Project mission |
| `project/CONTRACT.md` | Operational contract, workflow, policies |
| `ops/decisions/` | Decision records |
| `context/meta/planning/revenue-management-vision.md` | Revenue management prerequisites and vision |

---

_Living document. Updated as phases complete and priorities shift._

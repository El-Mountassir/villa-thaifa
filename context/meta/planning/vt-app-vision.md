# Villa Thaifa App — Vision

**Date**: 2026-02-21
**Status**: Concept — needs planning before any build
**For**: Omar + Said

---

## Table of Contents

1. [The Idea](#the-idea)
2. [First Module: Property & Rooms Dashboard](#first-module-property--rooms-dashboard)
3. [Module Roadmap](#module-roadmap)
4. [Said UX Requirements](#said-ux-requirements)
5. [Tech Stack](#tech-stack)
6. [Architecture Considerations](#architecture-considerations)
7. [Data Sources Available](#data-sources-available)
8. [Platform Integrations](#platform-integrations)
9. [Technical Constraints](#technical-constraints)
10. [Success Criteria](#success-criteria)
11. [Revenue Management Vision](#revenue-management-vision)
12. [LHCM-OS Relationship](#relationship-to-lhcm-os)
13. [Out of Scope](#out-of-scope)

---

## The Idea

A web app for Villa Thaifa operations. Not a full hotel PMS — a lightweight, purpose-built tool for Omar and Said to manage daily operations.

**Core value**: Reduce Omar's manual operational hours by 70% through automation. If everything else fails, the system must automate daily HotelRunner data extraction so Omar spends minutes, not hours, on property management.

**North star**: One M-shaped generalist + AI agents = full management of 10+ hotel properties. Villa Thaifa = first template property.

---

## First Module: Property & Rooms Dashboard

What the json-render demo attempted to show:

- Property overview (name, location, ratings across platforms)
- 12 room cards with pricing (EUR/MAD), capacity, category
- Key stats (total rooms, price range, exchange rate)
- Policies (check-in/out, cancellation, children, pets)
- Facilities (pool, spa, restaurant, wifi, parking, transfer)

This dashboard is the SEED — the first page of the app.

---

## Module Roadmap

### Phase 1 — Operational Core (current focus)

- Property & Rooms Dashboard (SEED — see above)
- Said's validation checklist (interactive version of data/admin/said-data-validation-checklist.md)
- HotelRunner reservation extraction viewer (96 reservations, batch daily)

### Phase 2 — Operations

- Booking calendar / unified availability view (all OTAs consolidated)
- Housekeeping status board
- OTA status dashboard (which channels active/synced/failing, last sync time)
- Agent activity log (which AI agents did what, errors surfaced)
- Quick actions: create internal reservation, block dates for maintenance, update pricing

### Phase 3 — Guest & Revenue Intelligence

- Guest communication hub (WhatsApp integration — automated confirmation, arrival instructions, follow-up, review request)
- Revenue dashboard (occupancy rate, RevPAR, ADR, revenue per room per channel)
- Competitive intelligence feed (comparable properties in Palmeraie, rate positioning)
- Dynamic pricing recommendations (demand-based, event-aware, seasonal)

### Phase 4 — Autonomy (LHCM-OS direction)

- Voice/text command interface for Said ("Boardroom" concept)
- Morning briefing push (WhatsApp or app notification)
- AI General Manager daily report (arrivals, departures, alerts)
- AI CFO view (CEG, GOP, USALI-compliant financial summary)
- AI Revenue Manager (automated rate suggestions, requires Said approval)
- Guest profile memory (returning guests, preferences, personalization)

---

## Said UX Requirements

Said is 78 years old, non-technical, Dutch-speaking (also French). These requirements are non-negotiable:

- **Simplicity over features**: He doesn't configure software — he gives objectives. The interface executes.
- **Morning briefing model**: Open app, see the essential in under 10 seconds. No configuration panels.
- **Approval-first**: Anything consequential (price change, guest communication) shows what will happen and waits for a single tap to confirm.
- **Formal tone**: Always "Monsieur Said" or "Monsieur Thaifa". Respectful, never casual.
- **WhatsApp-first**: Said already uses WhatsApp. Before a native app exists, WhatsApp is the primary channel for briefings and commands.
- **Language**: Dutch or French for any Said-facing UI. Never English.
- **Delegation-ready**: Said wants to be "Maître de Maison" — a host, not an accountant or receptionist. The system absorbs the operational burden entirely.
- **Decision authority preserved**: Said approves pricing, guest communication, and budget decisions. Agents draft, Said approves.

---

## Tech Stack

**Proposed stack** (validated by json-render demo):

- Next.js + Tailwind + shadcn/ui (frontend)
- Data source: canonical JSON files in data/ (rates.json, property-config.json, etc.) — no database needed initially
- SQLite (when admin persistence is required — already proven in existing codebase)
- Deploy: local first, then Vercel or Cloudflare Pages

**Alternative considered (from archives)**:

- FastAPI + Python backend (stronger for automation/agent orchestration layer)
- Streamlit for rapid MVP prototyping before Next.js
- Cloudflare Workers + D1 (edge-native, serverless-friendly)
- Hono (edge-native TypeScript API framework, lighter than Next.js API routes)

**Agent interface layer** (for Phase 2+):

- REST API endpoints agents can call: knowledge base, reservations, OTA status
- Code execution wrappers over HotelRunner API (more token-efficient than MCP)
- Pattern: TypeScript wrappers → agents execute code, not raw MCP calls

**Auth** (when needed):

- Auth0 free tier evaluated (up to 7,000 users, Google/GitHub social login, MFA)
- JWT + password hash as baseline alternative

---

## Architecture Considerations

**Dual data source pattern** (from existing codebase):

- JSON files in data/ — public website and agent-readable data (rooms, rates, facilities)
- SQLite — admin operations requiring persistence (verification workflow, audit trail)

**Feature-based structure** preferred over layer-based (rooms, facilities as features with their own data/UI/logic).

**Deployment constraint**: SQLite requires persistent file storage — not suitable for pure serverless edge without modifications. Vercel or a VPS preferred over Cloudflare Workers for the admin dashboard.

**Real-time vs batch**: Full automation blocked by auth barriers (HotelRunner reCAPTCHA, Booking.com OTP, Expedia SMS 2FA). Accept batch daily extraction (15-second HotelRunner extraction already proven). Real-time requires HTTPS domain + webhook setup — defer.

**Iterative delivery**: Ship incrementally. Streamlit MVP → Next.js MLP. Not waterfall.

---

## Data Sources Available

- `data/finance/rates.json` — room pricing (12 rooms, EUR/MAD)
- `data/property/property-config.json` — property overview, ratings, policies, facilities
- `data/rooms/` — per-room profiles (R01-R12)
- `data/operations/` — channels, check-in, housekeeping, maintenance, emergency configs
- `data/bookings/` — reservation exports and confirmed reservations
- `data/admin/said-data-validation-checklist.md` — Said's verified data points

**Knowledge base content types** (for agent API in Phase 2+):

- Property details, 12 room types (specs, photos, pricing)
- Operational docs (HotelRunner settings, OTA account details, pricing strategy)
- Standard Operating Procedures (booking handling, guest communication, emergency)
- Financial data (revenue per OTA, commission rates)

---

## Platform Integrations

| Platform | Status | Method | Constraint |
|---|---|---|---|
| HotelRunner (PMS) | Operational | Browser automation (primary) + REST API | 250 req/day, reCAPTCHA on login |
| Booking.com (OTA) | Connected | XML sync via HotelRunner | 25% commission, OTP on login |
| Expedia Group | Not connected | Via HotelRunner (pending) | SMS 2FA to Omar's phone |
| Airbnb | Not connected | Planned | TBD |
| WhatsApp Business | Not connected | Planned for Phase 3 | Business API access needed |

**OTA reduction goal**: Current 100% Booking.com dependency → 6-month target 70%, 12-month target 50%, with 20% direct bookings.

**Commission savings potential**: €15,000–30,000/year by reducing average commission from 25% to 12%.

---

## Technical Constraints

1. **Authentication barriers**: HotelRunner (reCAPTCHA), Booking.com (OTP email), Expedia (SMS 2FA) — daily manual intervention required (5-10 min). Blocks full automation.
2. **HotelRunner API rate limit**: 250 requests/day, 5 requests/minute — batch extraction only.
3. **Browser automation cookie bug**: agent-browser doesn't persist cookies between sessions — manual login per session.
4. **SQLite deployment**: Requires persistent file storage, not serverless edge.
5. **No HTTPS domain yet**: Blocks HotelRunner webhook real-time notifications.
6. **HotelRunner channel mapping**: 8 room types in HotelRunner must match OTA room types (discrepancy known).

---

## Success Criteria

### Omar's operational goals

- Reduce manual hours by 70%
- Daily HotelRunner extraction automated (minutes, not hours)
- All 12 rooms verified and priced in system
- Expedia connected via HotelRunner

### Said's experience goals

- Can open app and see essential status in under 10 seconds
- Receives WhatsApp morning briefing without requesting it
- Approvals are single-tap, not configuration
- Feels like "Chairman" not "admin"

### Business metrics (12-month horizon)

- Occupancy rate: 50% → 70%
- RevPAR: ~€100 → €175
- Average OTA commission: 25% → 12%
- Direct booking share: 0% → 20%
- Reservation response time: >24h → <1h (automated)

---

## Revenue Management Vision

Source: `context/meta/planning/revenue-management-vision.md`

Three structural problems to solve:

1. **Fixed pricing in a dynamic market** — rates locked until December 2026. Cannot respond to demand spikes, events, or seasonal shifts.
2. **Single-channel dependency** — 100% Booking.com at 25% commission. No leverage, no fallback, no direct booking.
3. **No market intelligence** — no system to monitor competitor positioning in Marrakech Palmeraie.

**Revenue management module prerequisites** (before building):

- All 12 rooms fully documented with verified data
- Multi-OTA distribution live (Expedia, Airbnb alongside Booking.com)
- Minimum 3-6 months historical booking data collected
- Said's explicit approval on pricing flexibility parameters (floor rates, ceiling rates, blackout periods)
- Direct booking channel established (even minimal)

**Key metrics to track**: RevPAR, ADR, occupancy rate, OTA commission cost per channel, direct booking share, booking lead time.

---

## Relationship to LHCM-OS

Villa Thaifa app = first pilot. If successful, generalize patterns into LHCM-OS framework.

**LHCM-OS** (Luxury Hospitality Cognitive Management - Operating System) is the broader product vision. Villa Thaifa is the proof of concept. LHCM-OS lives at `~/omar/professional/projects/lhcm-os/` — not in this repo.

**What LHCM-OS adds beyond the VT app**:

- Multi-tenant architecture (data isolation per property)
- White-label UI (custom branding per client)
- AI C-Suite agent roles: General Manager, CFO, Revenue Manager, CTO
- "The Boardroom" — voice/text command channel for Said to give directives to digital team
- Partner opportunity: HotelRunner partnership (white-label as "HotelRunner Intelligence")
- Target market: small luxury Moroccan properties (riads, maisons d'hôtes, 5-15 rooms)
- Pricing model: setup fee 5,000-10,000 MAD + 1,500-3,000 MAD/month subscription (~20% of hiring a GM)

**Sequence**: Prove (Villa Thaifa running well) → Build (LHCM-OS MVP) → Scale (2-3 paying clients). Do not skip steps.

---

## Out of Scope

- Building a full PMS from scratch (HotelRunner is the channel manager — integrate, don't replace)
- Real-time reservation updates (batch daily due to auth constraints)
- Guest-facing mobile app (web-first, PWA deferred)
- Financial accounting system (focus on operations)
- Staff scheduling system (not needed for 12-room property)
- Dedicated mobile app (not a priority for this scale)

---

## Next Step

Plan the app properly (ROADMAP.md) before building anything. Use /plan or architect agent.

**Source files consolidated into this document**:
- `ops/archive/planning/VISION-ENRICHED.md` (2026-01-30)
- `ops/archive/planning/VISION-DRAFT.md` (2026-01-30)
- `ops/archive/planning/villa-thaifa-internal-app-requirements-v0.1.0.md` (2025-01-09)
- `ops/archive/planning/lhcm-os-strategy-execution-plan-v0.1.0.md` (2025-01-09)
- `ops/archive/planning/villa-thaifa-workstream-master-v0.1.0.md` (2025-01-09)
- `ops/archive/planning/villa-thaifa-client-brief-v0.2.0.md` (2026-01-09)
- `ops/archive/planning/villa-thaifa-deliverables.md` (2026-01)
- `ops/archive/planning/comprehensive-transformation-plan.md` (2026-01-30)
- `context/meta/planning/revenue-management-vision.md`
- `context/meta/planning/villa-thaifa-brief.md`
- `context/meta/planning/PROJECT.md`

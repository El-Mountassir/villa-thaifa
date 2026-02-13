# External Integrations

**Analysis Date:** 2026-01-30

## APIs & External Services

**Channel Management & OTAs:**
- HotelRunner - Channel manager for room inventory, pricing, distribution
  - SDK/Client: REST API (credentials-based, setup in progress)
  - Auth: `HOTELRUNNER_TOKEN` (API key), `HOTELRUNNER_HR_ID` (property ID)
  - Rate Limit: 250 requests/day, 5 requests/minute
  - Docs: `sources/hotelrunner-api/guide.md`
  - Status: Setup in progress (credentials pending in `.env.local`)

- Booking.com - OTA reservations, promotions, guest communication
  - Login: Email + password + OTP
  - Credentials: `BOOKING_ADMIN_EMAIL`, `BOOKING_ADMIN_PASSWORD`
  - Authentication: 2FA via email, reCAPTCHA may appear
  - Browser automation required (via agent-browser)
  - Admin account: omar@el-mountassir.com (use this for operations)

- Expedia Group - Connectivity API for room content, amenities, photos
  - SDK/Client: REST API (developers.expediagroup.com)
  - Auth: `EXPEDIA_API_KEY`, `EXPEDIA_SHARED_SECRET`, `EXPEDIA_PROPERTY_ID`
  - Purpose: Direct synchronization of room content and photos
  - Portal: Expedia Partner Central (EPC) > Connectivity
  - Status: API credentials not yet configured

**Browser Automation:**
- agent-browser - Headless browser automation CLI
  - Location: `sources/agent-browser/guide.md`
  - Usage: Form automation, screenshot capture, data extraction
  - Capabilities: Click, snapshot, fill forms, PDF export, JavaScript execution
  - Reference syntax: `@e12` for element references
  - Used for: OTA login (Booking.com, Expedia), manual form interactions

## Data Storage

**Databases:**
- SQLite 3 (embedded)
  - Connection: Local file `property.db`
  - Client: better-sqlite3 12.6.2
  - Mode: WAL (Write-Ahead Logging)
  - No external DB service required

**File Storage:**
- Local filesystem only
  - Room images: `public/images/rooms/`
  - Data files: `src/data/facilities.json`, `src/data/rooms.json`
  - Hotel content: `legacy/content_source/facilities/`

**Caching:**
- Next.js built-in revalidation
  - Pattern: `revalidatePath()` in server actions
  - Used in: `src/app/admin/rooms/actions.ts` for cache invalidation

## Authentication & Identity

**Auth Provider:**
- Custom per-platform
  - HotelRunner: Email + password + API token
  - Booking.com: Email + password + OTP
  - Expedia: API key + shared secret OR email + password + 2FA

**Implementation Approach:**
- Admin dashboard: Secret-based (`ADMIN_SECRET` env var)
- OTA platforms: Direct credential storage in `.env`
- 2FA: Manual handling (SMS codes to `+212643390409` - Omar's phone)

**Account Hierarchy:**
- Admin (Omar El Mountassir): Default for all operations
  - Email: omar@el-mountassir.com
  - Phone: +212643390409 (receives 2FA codes)
- Owner (Said Thaifa): Secondary, not for routine operations
  - Reason: Avoid disturbing owner with login notifications
  - Email: said_thaifa@hotmail.fr

## Monitoring & Observability

**Error Tracking:**
- Not integrated (none detected)

**Logs:**
- Console logging in development
  - Pattern: `console.log()` and `console.error()` in `src/db/init.ts`
  - No structured logging framework

## CI/CD & Deployment

**Hosting:**
- Vercel (recommended) or self-hosted Node.js server
- Next.js deployment compatible

**CI Pipeline:**
- Not configured (none detected)

## Environment Configuration

**Required env vars:**
- `ADMIN_SECRET` - Access code for admin dashboard
- `HOTELRUNNER_TOKEN` - HotelRunner API key (setup in progress)
- `HOTELRUNNER_HR_ID` - HotelRunner property ID (setup in progress)
- `BOOKING_ADMIN_EMAIL`, `BOOKING_ADMIN_PASSWORD` - Booking.com credentials
- `EXPEDIA_API_KEY`, `EXPEDIA_SHARED_SECRET`, `EXPEDIA_PROPERTY_ID` - Expedia API credentials (not yet configured)

**Secrets location:**
- `.env` (gitignored, never committed)
- `.env.example` - Template reference with structure and documentation
- Real credentials loaded from `.env.local` at runtime

**Credential Priority:**
1. Read from `.env.local` if exists
2. Fallback to `.env` environment variables
3. Ask user for credentials at runtime if missing

## Webhooks & Callbacks

**Incoming:**
- HotelRunner webhooks: Real-time booking notifications (setup pending)
- Booking.com webhooks: Reservation updates (capability available but not integrated)

**Outgoing:**
- None configured

## Data Flow Patterns

**Room Content Sync:**
1. SQLite local database (`property.db`) - Source of truth
2. JSON data files (`src/data/rooms.json`, `src/data/facilities.json`) - Fallback/display
3. Manual sync to OTAs:
   - HotelRunner API (when token available)
   - Booking.com via browser automation (form entry)
   - Expedia via Connectivity API (when credentials configured)

**Admin Dashboard:**
- Authentication: `ADMIN_SECRET` (server action guard)
- Database operations: Server actions in `src/app/admin/rooms/actions.ts`
- Cache invalidation: `revalidatePath()` on mutations

---

*Integration audit: 2026-01-30*

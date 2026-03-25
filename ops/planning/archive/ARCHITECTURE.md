# Architecture

**Analysis Date:** 2026-01-30

## Pattern Overview

**Overall:** Hybrid Server/Client Next.js 16 application with feature-based structure and dual data sources (JSON-based public API + SQLite admin database).

**Key Characteristics:**

- Next.js 16+ App Router with server-side rendering (SSR) and server actions
- Feature-scoped architecture (rooms, facilities) with bindings layer
- Public/customer-facing pages powered by JSON data (`rooms.json`, `facilities.json`)
- Admin dashboard backed by SQLite database with verification workflows
- Zod-based schema validation for all data structures
- No ORM — direct better-sqlite3 queries in server actions

## Layers

**Presentation/Pages:**

- Purpose: Route handlers and UI rendering for customer and admin experiences
- Location: `src/app/` (Next.js App Router directory)
- Contains: Page components (`.tsx`), layouts, server actions (`.ts`)
- Depends on: Features API layer, components
- Used by: Browser clients (public site and admin)

**Features/Domain:**

- Purpose: Business logic encapsulation by feature (rooms, facilities)
- Location: `src/features/{feature}/` with `model/` (schemas) and `bindings/` (API)
- Contains: Zod schemas, query functions, data transformations
- Depends on: Database layer, data sources
- Used by: Pages, other features

**Components/UI:**

- Purpose: Reusable React UI components
- Location: `src/components/`
- Contains: Navigation, layout components (currently minimal)
- Depends on: React, styling
- Used by: Pages

**Data Access:**

- Purpose: Database and external data source access
- Location: `src/lib/db.ts` (SQLite singleton) and `src/data/` (JSON files)
- Contains: Database initialization, JSON fixture files
- Depends on: better-sqlite3, filesystem
- Used by: Feature bindings, server actions

**Database/Schema:**

- Purpose: SQLite schema definition and initialization
- Location: `src/db/schema.sql` (schema), `src/db/init.ts` (initialization script)
- Contains: Table definitions, indexes for rooms, beds, amenities
- Depends on: Database driver
- Used by: Database initialization on startup

## Data Flow

**Public Room Detail Page (`/rooms/[id]`):**

1. Next.js router matches URL parameter `id`
2. `generateStaticParams()` pre-generates static pages for all rooms
3. `getRoom(id)` fetches from `src/data/rooms.json`
4. Room rendered with inline styles; images from `room.images[0]`
5. Pricing shown from `room.price` object (EUR)

**Admin Room Management (`/admin/rooms`):**

1. Page requests `getRooms()` server action
2. Server action executes SQLite query: `SELECT id, expedia_type, internal_name, verification_status, floor, base_rate_mad FROM rooms`
3. Rooms displayed in grid with verification status badge
4. Click → `/admin/rooms/[id]` detail page

**Admin Room Detail (`/admin/rooms/[id]`):**

1. `getRoom(id)` server action executes three queries:
   - Main room data from `rooms` table
   - Amenities from `amenities` table (grouped by category)
   - Beds from `beds` table with counts and widths
2. Amenities grouped client-side by category
3. Verify button triggers `verifyRoom(id)` server action
4. After verification: `revalidatePath()` clears cache, badge updates to VERIFIED

**Public Home Page (`/`):**

1. Server-side: `getAllRooms()` and `getFacilities()` fetch async
2. Rooms: JSON data mapped to grid cards with images and prices
3. Facilities: JSON data mapped to icon cards
4. No interactive state; fully static-renderable

## State Management

**Per-page state:**

- None currently implemented for interactive features (forms, modals are stubs)

**Shared data:**

- Rooms and facilities loaded server-side, passed to components via props
- No client-side state management (useState/Context not used)

**Verification workflow:**

- `verification_status` field in database (`DRAFT` → `VERIFIED`)
- Server action `verifyRoom()` mutates database and revalidates paths
- Frontend shows conditional UI based on status

## Key Abstractions

**Schema/Type Definitions:**

- Purpose: Runtime validation and TypeScript type generation
- Examples: `RoomSchema`, `FacilitySchema`, `PriceSchema`, `FeaturesSchema` in `src/features/*/model/schema.ts`
- Pattern: Zod v4 with `z.infer<typeof Schema>` for type derivation

**Server Actions:**

- Purpose: Secure server-side mutations and complex queries
- Examples: `getRooms()`, `getRoom(id)`, `verifyRoom(id)`, `toggleAmenity()` in `src/app/admin/rooms/actions.ts`
- Pattern: `"use server"` directive; client can invoke directly via form action or async function call

**Feature Bindings:**

- Purpose: Decouple pages from data sources; swap implementations without breaking consumers
- Examples: `src/features/rooms/bindings/api.ts`, `src/features/facilities/bindings/api.ts`
- Pattern: Async functions returning typed data, type-safe via Zod

**Database Singleton:**

- Purpose: Single shared database connection across requests
- Location: `src/lib/db.ts`
- Pattern: `new Database(dbPath)` with WAL pragma for concurrent access

## Entry Points

**Public Site:**

- Location: `src/app/page.tsx`
- Triggers: User navigates to `/`
- Responsibilities: Render hero, accommodations grid, facilities grid; fetch data server-side

**Room Detail:**

- Location: `src/app/rooms/[id]/page.tsx`
- Triggers: User navigates to `/rooms/{id}`
- Responsibilities: Display room images, features, pricing; fetch from JSON; static generation

**Admin Dashboard:**

- Location: `src/app/admin/page.tsx`
- Triggers: User navigates to `/admin`
- Responsibilities: Navigation hub; link to room management, reservations (TODO), platform sync (TODO), calendar (TODO), analytics (TODO), settings (TODO)

**Admin Room Management:**

- Location: `src/app/admin/rooms/page.tsx`
- Triggers: User navigates to `/admin/rooms`
- Responsibilities: Load and display all rooms from SQLite with verification status; link to detail pages

**Admin Room Editor:**

- Location: `src/app/admin/rooms/[id]/page.tsx`
- Triggers: User navigates to `/admin/rooms/{id}`
- Responsibilities: Show room details (floor, size, rate, kitchen), grouped amenities, beds, verify button

## Error Handling

**Strategy:** Minimal error handling currently implemented; errors surface to browser.

**Patterns:**

- Room not found: `notFound()` returns 404 page in public site
- Database errors: Uncaught exceptions propagate (no try/catch in server actions)
- Missing data: Conditional rendering with fallbacks (e.g., "No image available")

**Future improvements needed:** Add error boundaries, logging, user-friendly error messages.

## Cross-Cutting Concerns

**Logging:** None currently implemented. Console.log statements exist only in `src/db/init.ts` (startup).

**Validation:** Zod schemas enforce structure on JSON data at runtime; SQLite schema enforces types at persistence.

**Authentication:** Not implemented. Admin pages are publicly accessible (no auth middleware).

**Caching:**

- Next.js default: static pages cached at build time
- `revalidatePath()` invalidates cache on database mutations (room verification)
- No HTTP caching headers configured

**Styling:** CSS-in-JS with inline `style` objects (no CSS modules except in admin). CSS variables defined in global stylesheet:

- `--primary`, `--secondary`, `--accent`, `--surface`, `--border`, `--text`
- Loaded via `globals.css` in root layout

---

_Architecture analysis: 2026-01-30_

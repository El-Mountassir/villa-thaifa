# Codebase Concerns

**Analysis Date:** 2026-01-30

## Security Issues (CRITICAL)

### Hardcoded Credentials in `.env`

**Issue:** The `.env` file contains plaintext real credentials for multiple platforms, committed to git history.

**Files:**
- `.env` (lines 27-45)

**Impact:**
- Booking.com admin password: `Na5%a?h5c9Rm2+K`
- HotelRunner owner password: `Wity.tracy@2025`
- Booking.com owner password: `Tracy.wity@2025`
- These credentials can be extracted from git history even if deleted
- Anyone with repo access has full admin access to all property platforms

**Current mitigation:**
- `.env` is listed in `.gitignore` (line 2 of `.gitignore`)

**Recommendations:**
1. **IMMEDIATE:** Rotate all exposed credentials (Booking.com, HotelRunner, Expedia)
2. Scrub git history: `git filter-repo --invert-paths --path ".env"`
3. Use `.env.example` (template-only) for future credentials
4. Implement environment-variable-based configuration for all auth
5. Use `.env.local` (gitignored) for real credentials in development
6. Document credential rotation policy in `.env.example` (90-day cycle)

**Related files:**
- `.env.example` — proper template-only format, should be the source of truth

---

## Input Validation & Type Safety

### Unsafe Type Casting in Database Queries

**Issue:** Server actions use `as any` type casts, bypassing type safety when loading database records.

**Files:**
- `src/app/admin/rooms/actions.ts` (line 48)

**Problem:**
```typescript
const room = db.prepare("SELECT * FROM rooms WHERE id = ?").get(id) as any;
```

**Impact:**
- Type checker can't catch mismatches between database schema and code
- Runtime errors possible if database schema changes
- Unsafe when building returned objects (lines 58-71)

**Fix approach:**
1. Define proper TypeScript interfaces matching database schema
2. Use type-safe database access pattern (validate after query)
3. Add runtime validation with zod for all database results

---

### Missing Input Validation in Server Actions

**Issue:** Server functions accept user input without validation or sanitization.

**Files:**
- `src/app/admin/rooms/actions.ts` (lines 78-81, line 74-75)

**Problem:**
```typescript
export async function verifyRoom(id: string) {
  // No validation that id exists, is valid format, or is allowed
  db.prepare("UPDATE rooms SET verification_status = 'VERIFIED' WHERE id = ?").run(id);
}

export async function toggleAmenity(amenityId: number, currentValue: boolean) {
  return { success: true }; // No-op stub — not implemented
}
```

**Impact:**
- Server action can update any room without validation
- `toggleAmenity` is incomplete (stub function)
- No authorization checks

**Fix approach:**
1. Add zod schemas for all server action inputs
2. Validate and parse inputs before database operations
3. Implement proper authorization (verify user can modify this room)
4. Complete `toggleAmenity` implementation

---

## Missing Authentication & Authorization

### No Access Control on Admin Routes

**Issue:** Admin dashboard and room editor pages have no authentication.

**Files:**
- `src/app/admin/page.tsx` (main dashboard)
- `src/app/admin/rooms/page.tsx` (room list)
- `src/app/admin/rooms/[id]/page.tsx` (room editor)
- `src/app/admin/rooms/actions.ts` (all server actions)

**Impact:**
- Anyone accessing `/admin` can view all room data
- Anyone can call `verifyRoom()` server action
- No user context or role tracking
- No audit trail of who modified what

**Current status:**
- No middleware, no authentication checks, no session management
- `.env.example` mentions `ADMIN_SECRET` (line 26) but it's not used anywhere

**Fix approach:**
1. Implement authentication middleware for `/admin/*` routes
2. Add role-based authorization (admin vs. owner roles)
3. Track user context in server actions
4. Add audit logging for all modifications
5. Implement logout/session expiry

---

## Error Handling

### Silent Failures in Database Initialization

**Issue:** Database init errors use `console.error` which may not be visible in production.

**Files:**
- `src/db/init.ts` (lines 9-14)

**Problem:**
```typescript
try {
    console.log('Initializing database...');
    db.exec(schema);
    console.log('Database initialized successfully.');
} catch (error) {
    console.error('Failed to initialize database:', error);
    process.exit(1);
}
```

**Impact:**
- If schema execution fails, only logs to console (may be lost)
- No graceful handling or user feedback
- `process.exit(1)` stops the server with no warning
- If schema file doesn't exist, error is unclear

**Fix approach:**
1. Replace `console.log/error` with structured logger
2. Handle missing schema file explicitly
3. Provide clear error messages to stdout/stderr
4. Add health checks that verify database is initialized

---

### Stub Functions Not Implemented

**Issue:** `toggleAmenity` function is incomplete.

**Files:**
- `src/app/admin/rooms/actions.ts` (lines 74-75)

**Problem:**
```typescript
export async function toggleAmenity(amenityId: number, currentValue: boolean) {
  return { success: true };
}
```

**Impact:**
- Function exists in UI but does nothing (returns success without side effects)
- Creates false sense of functionality
- Caller expects state change but none occurs
- Database remains unchanged

**Fix approach:**
1. Implement full update logic with validation
2. Or remove UI button if feature is deferred
3. Add test that verifies database is actually updated

---

## Test Coverage

### No Tests Exist

**Issue:** Zero test coverage detected (no `.test.ts`, `.spec.ts`, `jest.config`, or `vitest.config` files).

**Files:**
- Entire `src/` directory

**Impact:**
- 1,146 lines of TypeScript code have no test safety net
- Refactoring is high-risk (no validation of behavioral changes)
- Regressions can slip to production
- Server actions have no unit test coverage
- Database schema changes lack validation tests

**Current status:**
- `package.json` has no testing scripts or dependencies
- No test framework configured

**Fix approach:**
1. Install test framework (Vitest or Jest recommended)
2. Add testing npm scripts to `package.json`
3. Write unit tests for server actions (database, validation, auth)
4. Write integration tests for API endpoints
5. Target 80%+ coverage minimum

---

## Database

### Hardcoded Database Path

**Issue:** Database file is hardcoded to local filesystem in development and production.

**Files:**
- `src/lib/db.ts` (lines 4-5)

**Problem:**
```typescript
const dbPath = path.join(process.cwd(), 'property.db');
const db = new Database(dbPath);
```

**Impact:**
- Not portable across deployment environments
- Production data stored in working directory
- No backup strategy
- Database file not version-controlled (correctly)
- No support for external databases (Postgres, etc.)

**Fix approach:**
1. Use environment variable for database path: `DB_PATH`
2. Default to `property.db` only in development
3. Plan for production database migration (managed service)
4. Add backup/restore scripts

---

### Data Structure Mismatch

**Issue:** Two separate data models exist: JSON (`src/data/rooms.json`) and SQLite (`property.db`).

**Files:**
- `src/data/rooms.json` — used in public pages
- `property.db` — used in admin pages
- `src/features/rooms/bindings/api.ts` (line 3) — loads JSON directly

**Problem:**
```typescript
// Home page uses JSON
import roomsData from "@/data/rooms.json";
export const getAllRooms = async (): Promise<Room[]> => {
  return roomsData as Room[];
};

// Admin uses SQLite
const room = db.prepare("SELECT * FROM rooms WHERE id = ?").get(id) as any;
```

**Impact:**
- Data can diverge between public and admin interfaces
- No single source of truth
- Updates in one place don't sync to the other
- Search index must maintain both copies
- Schema changes require coordination

**Fix approach:**
1. Use database as single source of truth
2. Remove `src/data/rooms.json` (export to JSON for static generation if needed)
3. Create unified data binding layer
4. Implement database sync to JSON for public pages (if static export needed)

---

## Fragile Areas

### Large Component Files

**Issue:** Two page components exceed 250 lines (guideline is 400 max, ideal is 200).

**Files:**
- `src/app/admin/page.tsx` — 296 lines (dashboard with hardcoded stats and excessive inline styles)
- `src/app/page.tsx` — 252 lines (home page with room grid)

**Problem:**
- Inline CSS throughout (no component reuse)
- Logic mixed with rendering
- Difficult to test individual sections
- High change risk (one edit affects many elements)
- No separation of concerns

**Impact:**
- Dashboard stats are hardcoded (`Active Reservations: --`, `Occupancy Rate: --%`)
- Cannot be safely refactored
- Difficult to add new sections without risk

**Safe modification approach:**
1. Extract stat card component
2. Extract room grid into separate component
3. Separate styles into modules (already started: `editor.module.css`)
4. Move data fetching to server components
5. Keep page file <100 lines

---

### TypeScript Type Safety Issues

**Issue:** Multiple instances of `as any` and type assertions bypass type checking.

**Files:**
- `src/app/admin/rooms/actions.ts` (line 44, 48, 53, 56)

**Problem:**
```typescript
return stmt.all() as RoomSummary[];  // Hope it matches
const room = db.prepare(...).get(id) as any;  // Complete escape hatch
```

**Impact:**
- Type mismatches won't be caught until runtime
- Refactoring is dangerous
- Database schema changes aren't validated
- False confidence in type safety

**Safe modification approach:**
1. Add zod runtime validation for all database queries
2. Create database result types that match schema exactly
3. Use `.parse()` or `.parseAsync()` to validate
4. Remove all `as any` assertions

---

## Configuration Issues

### Missing `.env.local` Template

**Issue:** Development workflow doesn't have a `.env.local` file pattern, creating friction for onboarding.

**Files:**
- `.env.example` (good template exists)
- Missing `.env.local.example`

**Impact:**
- Developers unclear whether to create `.env.local` or modify `.env`
- Risk of accidentally committing real credentials to `.env`
- Onboarding takes longer

**Fix approach:**
1. Add `.env.local.example` (copy of `.env.example` with clear instructions)
2. Update README with credential setup instructions
3. Add pre-commit hook to prevent `.env` modifications

---

### Database Schema Not Validated at Startup

**Issue:** Schema file exists but is never validated to match ORM expectations.

**Files:**
- `src/db/schema.sql` — executed but not validated
- `src/db/init.ts` — no post-init verification
- `src/app/admin/rooms/actions.ts` — expects specific columns

**Problem:**
- If schema file is corrupted, app starts with wrong schema
- No verification that schema.sql matches code expectations
- Schema migrations not tracked

**Fix approach:**
1. Add schema validation at startup
2. Verify all expected tables and columns exist
3. Track schema versions (timestamp or hash)
4. Implement migration system for schema changes

---

## Performance Concerns

### No Database Indexes Beyond Schema

**Issue:** Schema has two indexes but no query optimization strategy.

**Files:**
- `src/db/schema.sql` (lines 33-34 — only amenities and beds indexed)

**Problem:**
- No index on `rooms(id)` (primary key is implicit)
- `getRoom()` queries have no optimization hints
- `getAllRooms()` loads all rooms into memory every request

**Impact:**
- As room count grows (>100), queries slow down
- No pagination or filtering support
- Memory usage unbounded

**Fix approach:**
1. Add indexes on frequently filtered columns (floor, verification_status)
2. Implement pagination in `getAllRooms()`
3. Add query analysis/profiling
4. Plan for database query optimization as data grows

---

## Incomplete Features

### Amenity Toggle Not Implemented

**Issue:** UI button for toggling amenities exists but backend function is a no-op.

**Files:**
- `src/app/admin/rooms/[id]/page.tsx` — renders amenity UI
- `src/app/admin/rooms/actions.ts` (lines 74-75) — no implementation

**Impact:**
- Users click button expecting change, nothing happens
- Creates confusion about app state
- Data can't be edited

**Priority:** High — blocks amenity management

**Fix approach:**
1. Implement database update in `toggleAmenity`
2. Add input validation (amenity exists, room exists)
3. Add authorization check
4. Add test verifying database is actually updated

---

### Dashboard Stats Are Hardcoded

**Issue:** Admin dashboard shows placeholder stats instead of live data.

**Files:**
- `src/app/admin/page.tsx` (lines 50, 65, 81)

**Problem:**
```typescript
<div style={{ fontSize: "2rem", fontWeight: "bold", color: "#333" }}>
  --  {/* Hardcoded placeholder */}
</div>
<div style={{ fontSize: "2rem", fontWeight: "bold", color: "#333" }}>
  --%  {/* Hardcoded placeholder */}
</div>
<div style={{ fontSize: "2rem", fontWeight: "bold", color: "#333" }}>
  €--  {/* Hardcoded placeholder */}
</div>
```

**Impact:**
- Dashboard is not functional
- Admin cannot see occupancy, reservations, or revenue
- Stats require implementation before launch

**Priority:** High — blocks admin functionality

**Fix approach:**
1. Query database for active reservations
2. Calculate occupancy rate from reservation dates
3. Calculate monthly revenue from bookings
4. Cache results to avoid query overhead
5. Add tests for stat calculations

---

## Code Style

### Console Statements in Production Code

**Issue:** `console.log/error` used in initialization, may not appear in production logs.

**Files:**
- `src/db/init.ts` (lines 9, 11, 13)

**Impact:**
- Production issues won't be logged properly
- Hard to debug failures in containers or serverless

**Fix approach:**
1. Use structured logger (Winston, Pino, or similar)
2. Configure with appropriate log levels
3. Integrate with observability platform

---

### Unused/Incomplete Imports

**Issue:** Some imports may be unused in components.

**Files:**
- `src/components/Navigation.tsx` (72 lines) — not reviewed for unused imports
- `src/app/layout.tsx` (17 lines) — minimal, appears clean

**Fix approach:**
1. Run TypeScript with `noUnusedLocals` flag
2. Enable ESLint rules for unused imports
3. Add pre-commit linting

---

## Knowledge & Documentation Gaps

### No Architecture Decision Log

**Issue:** Why certain choices were made (JSON vs. SQLite, Next.js specific patterns) is not documented.

**Impact:**
- Future contributors don't understand trade-offs
- Technical decisions can't be revised with context
- Onboarding takes longer

**Fix approach:**
1. Create `docs/decisions/` directory
2. Document key decisions (D001-D008) with context and trade-offs
3. Reference in code comments where appropriate

---

### API Specification Missing

**Issue:** Server actions in `actions.ts` are not documented with type information.

**Files:**
- `src/app/admin/rooms/actions.ts` — no JSDoc comments

**Impact:**
- Developers unsure of function behavior
- No contract specification
- Can't generate API docs

**Fix approach:**
1. Add JSDoc to all exported functions
2. Document parameters, return types, and side effects
3. Generate API documentation from comments

---

## Scaling Limits

### SQLite Database in Production

**Issue:** SQLite is file-based and not suitable for multi-process production.

**Files:**
- `src/lib/db.ts` (better-sqlite3 — single-process)

**Current capacity:**
- Single writer limit (better-sqlite3 is synchronous)
- ~1000 queries/sec theoretical max
- No support for distributed systems

**Limit:** Breaks at medium-scale traffic or horizontal scaling

**Scaling path:**
1. Migrate to PostgreSQL for production
2. Add connection pooling (PgBouncer or library)
3. Implement read replicas for query scaling
4. Add caching layer (Redis) for hot data

---

## Missing Critical Features

### No Reservation/Booking Integration

**Issue:** Property management system doesn't track reservations or bookings.

**Files:**
- Database schema has no `reservations` table
- Admin dashboard has placeholder for `Active Reservations`
- No Booking.com or HotelRunner sync

**Blocks:**
- Occupancy calculation
- Revenue tracking
- Availability management
- Guest communication

**Priority:** P0 — core functionality

---

### No User/Role System

**Issue:** No concept of users or permissions in the system.

**Files:**
- No `users` table
- No role-based access control
- Admin dashboard has no login

**Blocks:**
- Multi-user management
- Owner vs. Admin workflows
- Audit logging
- API authentication

**Priority:** P0 — essential for launch

---

### No Audit Trail

**Issue:** No tracking of who modified data or when (except database `created_at` columns if present).

**Impact:**
- Can't debug who made a change
- No compliance trail for business operations
- Can't restore previous states

**Fix approach:**
1. Add `updated_at` timestamps to all tables
2. Add `updated_by` user tracking
3. Create audit log table for sensitive changes
4. Query audit table for change history

---

## Integration Gaps

### HotelRunner API Not Integrated

**Issue:** HotelRunner credentials exist but no API integration code.

**Files:**
- `.env` has `HOTELRUNNER_TOKEN` and `HOTELRUNNER_HR_ID` (unused)
- No API client in codebase
- Status: "Setup in progress" per `.env.example`

**Impact:**
- Can't sync room inventory
- Can't manage pricing
- Can't receive bookings

**Related:**
- `sources/hotelrunner-api/guide.md` — documentation exists
- `sources/hotelrunner-api/SETUP.md` — setup progress tracked

---

### Booking.com Integration Not Implemented

**Issue:** Booking.com credentials exist but no integration code.

**Files:**
- `.env` has Booking.com credentials (unused)
- No API client or browser automation
- Manual setup required for testing

**Impact:**
- Can't sync reservations
- Can't manage pricing or availability
- Manual channel management required

---

### Expedia Integration Not Implemented

**Issue:** Expedia credentials partially documented but no integration code.

**Files:**
- `.env.example` has Expedia setup instructions
- Real credentials missing (marked "not documented" in template)
- No API client

**Impact:**
- Can't manage Expedia Group listings
- No sync with Hotels.com, Vrbo, Expedia.com

---

## Summary

**Critical Issues (Block Launch):**
1. Hardcoded credentials in `.env` — rotate immediately
2. No authentication on admin routes
3. Dashboard stats are hardcoded/non-functional
4. Amenity toggle button is a no-op
5. No reservation/booking system

**High Priority (Before Launch):**
1. Add input validation and error handling
2. Implement auth + role-based access control
3. Add test coverage (80%+ minimum)
4. Complete HotelRunner integration
5. Fix TypeScript type safety (remove `as any`)

**Medium Priority (Soon After):**
1. Implement Booking.com and Expedia integrations
2. Extract large components into smaller files
3. Migrate from SQLite to PostgreSQL
4. Add audit logging
5. Set up structured logging

**Low Priority (Nice to Have):**
1. Add API documentation (JSDoc)
2. Implement database indexes for performance
3. Create architecture decision log
4. Add pre-commit hooks

---

*Concerns audit: 2026-01-30*

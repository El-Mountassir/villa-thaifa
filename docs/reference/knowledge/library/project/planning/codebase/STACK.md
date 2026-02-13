# Technology Stack

**Analysis Date:** 2026-01-30

## Languages

**Primary:**

- TypeScript 5.9.3 - Full codebase, type-safe frontend and backend
- JavaScript - Build and configuration files
- SQL - Database schema (`src/db/schema.sql`)

## Runtime

**Environment:**

- Node.js 16+ (implied by Next.js 16.1.3)

**Package Manager:**

- npm (lock file: `package-lock.json`)
- Lockfile: Present

## Frameworks

**Core:**

- Next.js 16.1.3 - Full-stack React framework with file-based routing
  - React 19.2.3 - UI component library
  - React DOM 19.2.3 - DOM rendering

**Dev Tools:**

- TypeScript 5.9.3 - Static type checking
- ESLint 9.39.2 - Code linting
- PostCSS 8.5.6 - CSS processing

**Data/Validation:**

- Zod 4.3.5 - Schema validation and type inference
- better-sqlite3 12.6.2 - Embedded SQL database (local-first)

## Key Dependencies

**Critical:**

- better-sqlite3 12.6.2 - Synchronous SQLite wrapper for server-side data
  - Enables local database without external DB service
  - Used with WAL (Write-Ahead Logging) mode in `src/lib/db.ts`
- axios 1.13.4 - HTTP client for API requests (prepared but not yet integrated)
- dotenv 17.2.3 - Environment variable loading
- tsx 4.21.0 - TypeScript execution runtime

**Rendering:**

- @json-render/react 0.2.0 - JSON-driven component rendering

**Type Definitions:**

- @types/node 25.0.9
- @types/react 19.2.8

## Configuration

**Environment:**

- `.env` - Local credentials (gitignored)
- `.env.example` - Credential template reference
- Variables configured for: HotelRunner, Booking.com, Expedia Group APIs
- Admin secret for dashboard access: `ADMIN_SECRET`

**Build:**

- `next.config.js` - Next.js configuration with React Strict Mode enabled
- `tsconfig.json` - TypeScript compiler options with:
  - Path alias: `@/*` → `./src/*`
  - JSX: React 17+ mode
  - Strict mode enabled
  - Module resolution: Node

## Database

**Type:** SQLite 3 (embedded, file-based)

- Location: `property.db` (project root, created at runtime)
- Mode: WAL (Write-Ahead Logging) for concurrency
- Initialization: `src/db/init.ts` runs `src/db/schema.sql`

**Schema Tables:**

- `rooms` - Property inventory (id, expedia_type, internal_name, floor, occupancy, amenities, pricing)
- `beds` - Room bed configurations (type, dimensions, count)
- `amenities` - Room features (view, outdoor, bathroom, climate, layout, hardware)

## Platform Requirements

**Development:**

- Node.js 16+
- npm 7+
- SQLite 3 runtime

**Production:**

- Next.js compatible Node.js runtime (Vercel, AWS Lambda, self-hosted)
- SQLite database file persistence required
- Environment variables loaded from `.env` or process.env

**Build Output:**

- `.next/` directory - Compiled Next.js application
- `property.db` - SQLite database file

---

_Stack analysis: 2026-01-30_

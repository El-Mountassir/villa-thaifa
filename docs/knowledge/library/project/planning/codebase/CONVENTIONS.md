# Coding Conventions

**Analysis Date:** 2026-01-30

## Naming Patterns

**Files:**
- React components: PascalCase (e.g., `Navigation.tsx`)
- Pages: lowercase with hyphens for multi-word (e.g., `[id]/page.tsx`)
- Server actions: camelCase (e.g., `actions.ts`)
- Utilities/libraries: camelCase (e.g., `db.ts`)
- CSS modules: camelCase with `.module.css` extension (e.g., `dashboard.module.css`)
- Schema files: camelCase (e.g., `schema.ts`)

**Functions:**
- Async API/data fetching functions: camelCase (e.g., `getAllRooms()`, `getRoom()`, `getFacilities()`)
- Server action functions: camelCase (e.g., `verifyRoom()`, `toggleAmenity()`)
- React components: PascalCase function declarations (e.g., `export default function RoomsDashboard()`)

**Variables:**
- Local variables: camelCase (e.g., `rooms`, `facility`, `groupedAmenities`)
- Constants (rarely used): UPPER_SNAKE_CASE where appropriate
- Object properties: camelCase (e.g., `room.internal_name`, `bed.width_cm`)

**Types:**
- Type names: PascalCase (e.g., `Room`, `Facility`, `Amenity`, `Bed`)
- Zod schemas: PascalCase with `Schema` suffix (e.g., `RoomSchema`, `FacilitySchema`)
- Interface names: PascalCase (e.g., `RoomSummary`, `RoomDetail`)

## Code Style

**Formatting:**
- ESLint enabled (Next.js default)
- No Prettier config present — uses Next.js defaults
- Indentation: 2 spaces
- Semicolons: required throughout
- Quotes: double quotes for JSX attributes and strings

**Linting:**
- Next.js default linting rules (`eslint ^9.39.2`)
- Run with: `npm run lint`
- Strict TypeScript: `strict: true` in tsconfig.json

**React Patterns:**
- Server Components by default (Next.js App Router)
- Server Actions with `"use server"` directive (e.g., `src/app/admin/rooms/actions.ts`)
- Inline styles preferred over class-based CSS for layout components
- CSS Modules for dashboard pages (e.g., `dashboard.module.css`)

## Import Organization

**Order:**
1. External libraries (React, Next.js, axios, zod)
2. Local absolute imports using `@/` alias
3. Local relative imports (rarely used; `@/` preferred)

**Path Aliases:**
- `@/*` → `./src/*` (defined in tsconfig.json)

**Example pattern from codebase:**

```typescript
// 1. External libraries
import Database from 'better-sqlite3';
import path from 'path';

// 2. Zod schemas
import { z } from "zod";

// 3. Absolute imports
import db from "@/lib/db";
import { getAllRooms } from "@/features/rooms/bindings/api";
import { revalidatePath } from "next/cache";

// 4. Type imports (intermingled with 2-3)
import { Room } from "../model/schema";
```

## Error Handling

**Patterns:**
- Try-catch blocks in database initialization (`src/db/init.ts`):
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

- Simple null checks in async data functions:
  ```typescript
  export async function getRoom(id: string): Promise<RoomDetail | null> {
    const room = db.prepare("SELECT * FROM rooms WHERE id = ?").get(id) as any;
    if (!room) return null;
    // ... continue
  }
  ```

- JSX fallback in page components:
  ```typescript
  if (!room) return <div>Room not found</div>;
  ```

- No structured error responses; basic error handling with console logging

## Logging

**Framework:** `console.log`, `console.error` (native browser/Node.js)

**Patterns:**
- Used only in initialization scripts (`src/db/init.ts`)
- Success messages: `console.log('Database initialized successfully.')`
- Error messages: `console.error('Failed to initialize database:', error)`
- NOT used in business logic, components, or API routes

**Best practice:** Logging is minimal; most code has no logging strategy defined.

## Comments

**When to Comment:**
- Inline comments rare in codebase
- JSDoc/TSDoc not used
- Comments appear occasionally for:
  - Section markers in JSX (e.g., `{/* HERO SECTION */}`)
  - Data structure explanations in JSON comments
  - Implementation notes in schemas (e.g., `// "A confirmare"`)

**JSDoc/TSDoc:**
- Not currently in use
- No documentation strings on functions

## Function Design

**Size:** Functions vary from 5 lines (simple getters) to 100+ lines (complex components)

**Parameters:**
- Keep minimal; prefer destructuring for objects
- Async functions preferred for data operations
- Type annotations required throughout

**Return Values:**
- Explicitly typed return types (`Promise<T>`, `T | null`)
- Async functions return Promises
- React components return JSX.Element implicitly

**Example pattern:**

```typescript
export async function getRooms(): Promise<RoomSummary[]> {
  const stmt = db.prepare(`
    SELECT id, expedia_type as type, internal_name, verification_status, floor, base_rate_mad as price_mad
    FROM rooms
    ORDER BY id ASC
  `);
  return stmt.all() as RoomSummary[];
}
```

## Module Design

**Exports:**
- Named exports preferred for utilities and functions
- Default exports for React components and pages
- Mix observed:
  ```typescript
  // schema.ts: named exports
  export const RoomSchema = z.object({...});
  export type Room = z.infer<typeof RoomSchema>;

  // component: default export
  export default function Navigation() {...}
  ```

**Barrel Files:**
- Not used; direct imports from modules preferred

**Feature-Based Organization:**
- Code organized by domain: `features/rooms/`, `features/facilities/`
- Structure within feature:
  - `model/schema.ts` — Zod schemas and types
  - `bindings/api.ts` — Data fetching/integration
  - Consistent pattern across features

## Validation

**Framework:** Zod (`^4.3.5`)

**Pattern:**
```typescript
export const RoomSchema = z.object({
  id: z.string(),
  number: z.string(),
  type: z.string(),
  capacity: z.object({
    adults: z.number(),
    children: z.number().optional(),
    description: z.string(),
  }),
  beds: z.array(z.string()),
  price: PriceSchema,
  features: FeaturesSchema,
  description: z.string(),
  images: z.array(z.string()).optional(),
});

export type Room = z.infer<typeof RoomSchema>;
```

- Schemas define both validation and type inference
- Optional fields marked with `.optional()`
- Nested schemas composed (e.g., `PriceSchema` within `RoomSchema`)
- Type extraction via `z.infer<typeof Schema>`

## Database Access

**Pattern:** Direct SQL with parameterized queries via `better-sqlite3`

```typescript
const stmt = db.prepare("SELECT * FROM rooms WHERE id = ?").get(id) as any;

db.prepare(
  "UPDATE rooms SET verification_status = 'VERIFIED' WHERE id = ?",
).run(id);
```

- Parameterized queries with `?` placeholders (prevents SQL injection)
- `.get()` for single row, `.all()` for multiple rows, `.run()` for updates
- Type casting with `as any` (workaround for lack of schema enforcement)

## Component Styling

**CSS Modules:**
- Used for dashboard pages: `src/app/admin/rooms/dashboard.module.css`
- Example class names: `.container`, `.header`, `.title`, `.grid`, `.card`, `.badge`
- Naming convention: lowercase with camelCase for compound (e.g., `.badgeVerified`)

**Inline Styles:**
- Heavily used in public-facing pages (`src/app/page.tsx`)
- CSS variables referenced: `var(--accent)`, `var(--border)`, `var(--surface)`, `var(--text)`
- Style props passed directly to JSX elements:
  ```typescript
  <div style={{
    backgroundColor: "var(--surface)",
    borderBottom: "1px solid var(--border)",
    padding: "1rem 0"
  }}>
  ```

## Type Safety

**TypeScript Strictness:**
- `strict: true` enabled in tsconfig.json
- All files `.ts` or `.tsx`
- Type annotations required on function parameters and returns
- Some loose casting: `as any` used in database results

## API Conventions (if applicable)

**Server Actions:**
- Marked with `"use server"` directive
- Located in `src/app/admin/rooms/actions.ts`
- Functions: `getRooms()`, `getRoom()`, `verifyRoom()`, `toggleAmenity()`
- Return types explicitly declared

**Data Binding Layer:**
- API functions in `src/features/*/bindings/api.ts`
- Currently fetch from JSON files (development data)
- Future: will connect to HotelRunner API

---

*Convention analysis: 2026-01-30*

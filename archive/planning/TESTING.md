# Testing Patterns

**Analysis Date:** 2026-01-30

## Test Framework

**Runner:**
- Not detected — no test framework configured
- No Jest, Vitest, or other test runner in dependencies

**Assertion Library:**
- Not detected — no testing library installed

**Test Configuration:**
- No `jest.config.ts`, `vitest.config.ts`, or testing setup files found

**Run Commands:**
- Not applicable — testing framework not yet implemented

## Test File Organization

**Location:**
- No test files present in codebase
- No `*.test.ts`, `*.test.tsx`, `*.spec.ts`, or `*.spec.tsx` files found

**Naming Convention:**
- Pattern not established (no test files to reference)

**Proposed Structure (not yet implemented):**
```
src/
├── features/rooms/
│   ├── model/schema.ts
│   ├── model/schema.test.ts          # Schema validation tests
│   ├── bindings/api.ts
│   └── bindings/api.test.ts          # API binding tests
├── lib/
│   ├── db.ts
│   └── db.test.ts                    # Database initialization tests
└── app/
    └── admin/rooms/
        ├── actions.ts
        └── actions.test.ts           # Server action tests
```

## Test Coverage

**Requirements:**
- Not enforced — no coverage tooling configured

**Current Status:**
- 0% — No tests present

**Recommendation:**
- Establish 80%+ coverage target before adding new features
- Start with critical paths:
  1. Schema validation (Zod schemas)
  2. Server actions (getRooms, getRoom, verifyRoom)
  3. Database operations (queries, updates)
  4. API bindings (data fetching from JSON/API)

## Test Types

**Unit Tests:**
- Not yet implemented
- Should cover:
  - Zod schema validation (`src/features/rooms/model/schema.ts`)
  - Individual server action functions (`getRooms()`, `getRoom()`)
  - Data transformation logic

**Integration Tests:**
- Not yet implemented
- Should cover:
  - Server actions with database interaction
  - API bindings with data sources
  - Form submission workflows (e.g., `verifyRoom()`)

**E2E Tests:**
- Not yet implemented
- No E2E framework installed
- Recommendation: Use Playwright for critical user flows:
  - Admin dashboard navigation
  - Room detail viewing
  - Room verification workflow

## Mocking

**Framework:**
- Not selected — no mocking library installed

**Recommended approach:**
- Vitest with built-in mocking
- OR Jest with ts-jest for TypeScript support

**Database Mocking Pattern (recommended):**
```typescript
// Mock better-sqlite3
vi.mock('@/lib/db', () => ({
  default: {
    prepare: vi.fn().mockReturnValue({
      all: vi.fn().mockReturnValue([]),
      get: vi.fn().mockReturnValue(null),
      run: vi.fn()
    })
  }
}));
```

**API Binding Mocking (recommended):**
```typescript
// Mock JSON data loading
vi.mock('@/data/rooms.json', () => ({
  default: [
    {
      id: 'room-1',
      number: '101',
      type: 'Deluxe Suite',
      // ... other props
    }
  ]
}));
```

**What to Mock:**
- Database layer (`better-sqlite3` connections)
- File system imports (JSON data files)
- Next.js functions (revalidatePath, etc.)
- External APIs (when integrating HotelRunner)

**What NOT to Mock:**
- Zod schemas (test validation directly)
- Pure functions and utilities
- Router/navigation (unless testing page behavior)

## Fixtures and Factories

**Test Data:**
- Not implemented
- No factory libraries or test fixtures present

**Recommended Pattern:**
```typescript
// src/test/fixtures/rooms.ts
export const mockRoomSummary = (): RoomSummary => ({
  id: 'room-101',
  type: 'Deluxe Suite',
  internal_name: 'Suite 101',
  verification_status: 'VERIFIED',
  floor: 'Ground',
  price_mad: 1500,
});

export const mockRoomDetail = (): RoomDetail => ({
  ...mockRoomSummary(),
  occupancy_adults: 2,
  size_m2: 45,
  is_smoking: false,
  has_kitchen: true,
  amenities: [
    { id: 1, category: 'View', name: 'Ocean View', value: true }
  ],
  beds: [
    { id: 1, type: 'King', count: 1, width_cm: 180 }
  ]
});
```

**Location:**
- Proposed: `src/test/fixtures/` or `src/__fixtures__/`

## Existing Validation Tests (Implicit)

**Zod Schema Validation:**
- Validation happens at runtime via type casting
- Example from `src/app/admin/rooms/actions.ts`:
  ```typescript
  return stmt.all() as RoomSummary[];
  ```
- Currently relies on manual type assertion (`as`) rather than runtime validation

**Recommended Approach:**
```typescript
// Instead of `as` casting, use Zod parsing:
const rooms = stmt.all();
const validatedRooms = RoomSummarySchema.array().parse(rows);
```

## Test Structure (Template for Future Implementation)

**Basic Unit Test:**
```typescript
// src/features/rooms/model/schema.test.ts
import { describe, it, expect } from 'vitest';
import { RoomSchema } from './schema';

describe('RoomSchema', () => {
  it('should validate a complete room object', () => {
    const validRoom = {
      id: 'room-1',
      number: '101',
      type: 'Suite',
      capacity: { adults: 2, description: '2 guests' },
      beds: ['King'],
      price: { amount: 150, currency: 'EUR' },
      features: {},
      description: 'Beautiful room',
    };

    expect(() => RoomSchema.parse(validRoom)).not.toThrow();
  });

  it('should reject invalid room data', () => {
    const invalidRoom = {
      id: 'room-1',
      number: '101',
      // missing required fields
    };

    expect(() => RoomSchema.parse(invalidRoom)).toThrow();
  });
});
```

**Server Action Test:**
```typescript
// src/app/admin/rooms/actions.test.ts
import { describe, it, expect, vi, beforeEach } from 'vitest';
import { getRooms, getRoom } from './actions';

// Mock database
vi.mock('@/lib/db', () => ({
  default: {
    prepare: vi.fn()
  }
}));

describe('Room Actions', () => {
  beforeEach(() => {
    vi.clearAllMocks();
  });

  it('should fetch all rooms', async () => {
    const rooms = await getRooms();
    expect(Array.isArray(rooms)).toBe(true);
  });

  it('should return null for non-existent room', async () => {
    const room = await getRoom('non-existent');
    expect(room).toBeNull();
  });
});
```

## Missing Test Infrastructure

**Currently Not Present:**
1. Test runner (Jest, Vitest, or similar)
2. Test assertion libraries
3. Mocking frameworks
4. Test fixtures or factories
5. Any test files (0% coverage)
6. Test configuration (jest.config, vitest.config, etc.)
7. Test utilities or helpers
8. GitHub Actions or CI/CD test runs

## Recommended Testing Setup (Priority: P0)

**Phase 1: Setup**
- Install Vitest (`npm install -D vitest @vitest/ui`)
- Install testing utilities (`npm install -D @testing-library/react @testing-library/jest-dom`)
- Create `vitest.config.ts`
- Add test scripts to `package.json`:
  ```json
  {
    "test": "vitest",
    "test:ui": "vitest --ui",
    "test:coverage": "vitest --coverage"
  }
  ```

**Phase 2: Critical Tests (80% minimum coverage)**
1. Zod schema validation tests
2. Server action tests (getRooms, getRoom, verifyRoom)
3. API binding tests
4. Database query tests

**Phase 3: Advanced Coverage**
1. React component rendering tests
2. Integration tests for full workflows
3. E2E tests with Playwright for admin flows

## Coverage Goals

**Target:** 80%+ coverage

**Priority Areas (descending order):**
1. **Critical:** Schema validation, server actions, database operations (must test)
2. **High:** API bindings, data fetching (should test)
3. **Medium:** React components, page rendering (should test)
4. **Low:** CSS styling, visual elements (optional)

## Known Test Gaps

**High Risk:**
- No validation of data shapes at runtime (relies on `as` casting)
- Database operations untested (SELECT, UPDATE queries)
- Server actions untested (verifyRoom, toggleAmenity)
- No tests for error conditions

**Medium Risk:**
- React component rendering untested
- Page navigation untested
- API binding untested (currently mocked with JSON files)

**Low Risk:**
- Styling untested (CSS Modules)
- Navigation component untested

---

*Testing analysis: 2026-01-30*

# Data Inventory & Migration Strategy

**Last Updated**: 2026-02-13
**Source Project**: `~/villa-thaifa/` (1.1GB, 1435 files)
**Destination**: New repo `omar-elmountassir/villa-thaifa-pms`

---

## Executive Summary

**What we have**: 12 rooms, 21 beds, 94 amenities, 96 reservations (extracted), 382 documentation files, 127 photos, 5 agent workflows, scattered across YAML, SQLite, JSON, markdown.

**What we migrate**: Core data (rooms, beds, amenities, policies, OTA mappings). ~5% of total files.

**What we don't migrate**: 382 docs (over-documentation), agent infrastructure, photos (managed via HotelRunner), Linear references.

**Migration effort**: ~8-12 hours (mostly agent work).

---

## Data Sources (Verified, No Data Loss)

### Primary Data Files

| File                                                                             | Type     | Content                                                 | Verified   | Migrate?                                                 |
| -------------------------------------------------------------------------------- | -------- | ------------------------------------------------------- | ---------- | -------------------------------------------------------- |
| `ssot/rooms.yaml`                                                                | YAML     | 12 rooms, pricing EUR/MAD, features, OTA mapping        | 2026-01-24 | ✅ YES — Seed script                                     |
| `property.db`                                                                    | SQLite   | 12 rooms, 21 beds, 94 amenities                         | Unknown    | ✅ YES — Migration script                                |
| `docs/knowledge/villa-thaifa/policies/events-privatization.md`                   | Markdown | Full privatization policy (2,000€/night)                | Unknown    | ✅ YES — Extract to `docs/policies/`                     |
| `docs/operations/expedia/onboarding_capture_v1.md`                               | Markdown | Expedia onboarding (steps 1-4, 16.5% commission)        | Unknown    | ✅ YES — Extract to `docs/integrations/`                 |
| `docs/specs/knowledge/platforms/hotelrunner/channel-mapping.md`                  | Markdown | Booking.com mapping (8 room types, Two-Way XML)         | Unknown    | ✅ YES — Extract to `docs/integrations/`                 |
| `docs/specs/knowledge/villa-thaifa/state/current/reserverations/reservations.md` | Markdown | 96 extracted reservations                               | Unknown    | ⚠️ REFERENCE — Historical data, not seed                 |
| `.env`                                                                           | ENV      | Live HotelRunner, Booking.com, Expedia credentials      | Unknown    | ✅ YES — .env.example only (no secrets)                  |
| `sources/hotelrunner-api/`                                                       | Mixed    | API research, browser automation script                 | Unknown    | ✅ YES — Summarize to `docs/integrations/hotelrunner.md` |
| `.agents/workflows/`                                                             | YAML     | 5 workflows (reservation, pricing, guest-communication) | Unknown    | ⚠️ REFERENCE — Redesign from scratch                     |

### Asset Files (Photos, Media)

| Source          | Count   | Size    | Migrate?                                      |
| --------------- | ------- | ------- | --------------------------------------------- |
| Room photos     | 127     | ~50MB   | ❌ NO — Managed via HotelRunner               |
| Property photos | Unknown | Unknown | ❌ NO — Managed via HotelRunner/OTA platforms |

### Documentation Files

| Category                                    | Count   | Migrate?                                   |
| ------------------------------------------- | ------- | ------------------------------------------ |
| Over-documentation (382 MD files)           | 382     | ❌ NO — Archive in old repo                |
| Key policies (events, cancellation)         | 3-4     | ✅ YES — Extract essentials only           |
| OTA onboarding/mapping                      | 5-8     | ✅ YES — Summarize to `docs/integrations/` |
| Agent infrastructure (.agents/, .planning/) | ~20     | ❌ NO — Redesign from scratch              |
| Lux collaboration artifacts                 | Unknown | ❌ NO — Historical only                    |

---

## Scattered Content in ~/omar/

| File              | Location                                                                        | Content                | Migrate?                             |
| ----------------- | ------------------------------------------------------------------------------- | ---------------------- | ------------------------------------ |
| `villa-thaifa.md` | `archives/grid/comms/clients/`                                                  | Communications summary | ❌ NO — Historical archive           |
| `said-thaifa.md`  | `operational/productivity/memory/people/`                                       | Contact record         | ❌ NO — Omar's personal contact book |
| Backup tarball    | `/media/director/data/.../villa-thaifa-pre-prompt-refactoring-*.tar.gz` (463MB) | Pre-2026-01-15 state   | ❌ NO — Disaster recovery only       |

---

## Migration Table (What Goes Where)

### Core Data → Vercel Postgres

| Source                       | Destination Table | Method                               | Agent  |
| ---------------------------- | ----------------- | ------------------------------------ | ------ |
| `ssot/rooms.yaml` (12 rooms) | `rooms`           | Seed script (SQL INSERT)             | Sonnet |
| `ssot/rooms.yaml` (pricing)  | `pricing_rules`   | Seed script                          | Sonnet |
| `property.db` → `rooms`      | `rooms`           | Migration script (SQLite → Postgres) | Sonnet |
| `property.db` → `beds`       | `beds`            | Migration script                     | Sonnet |
| `property.db` → `amenities`  | `amenities`       | Migration script                     | Sonnet |

**Conflict resolution**: rooms.yaml is SSOT. If property.db conflicts, rooms.yaml wins.

### Documentation → New Repo `docs/`

| Source                   | Destination                            | Method                                                     | Agent  |
| ------------------------ | -------------------------------------- | ---------------------------------------------------------- | ------ |
| Key policies (3-4 files) | `docs/policies/`                       | Extract essentials, rewrite concisely                      | Sonnet |
| OTA mapping files        | `docs/integrations/channel-mapping.md` | Consolidate into single file                               | Sonnet |
| HotelRunner API research | `docs/integrations/hotelrunner.md`     | Summarize from `sources/hotelrunner-api/` + research brief | Sonnet |
| Expedia onboarding       | `docs/integrations/expedia.md`         | Extract from `docs/operations/expedia/`                    | Sonnet |

### Configuration → New Repo Root

| Source           | Destination    | Method                   | Agent  |
| ---------------- | -------------- | ------------------------ | ------ |
| `.env` (secrets) | NOT MIGRATED   | Secrets stay out of repo | —      |
| `.env.example`   | `.env.example` | Copy, strip secrets      | Manual |

### Scripts → New Repo `scripts/`

| Source                        | Destination                              | Purpose                          | Agent       |
| ----------------------------- | ---------------------------------------- | -------------------------------- | ----------- |
| Reservation extraction script | `scripts/legacy/extract-reservations.py` | Reference only (historical data) | Manual copy |

---

## What Does NOT Migrate

### Documentation Over-Bloat (382 files)

**Reason**: Over-documentation without execution. Archive in old repo with deprecation notice.

**Categories**:

- Project plans (never executed)
- Agent prompts (superseded)
- Research briefs (duplicated across multiple dirs)
- Meeting notes (historical)
- Decision logs (outdated)

**Action**: Add deprecation README to old repo, point to new repo.

### Agent Infrastructure

**Reason**: Agent workflows were designed for old architecture. Redesign from scratch in new repo.

**Files**:

- `.agents/workflows/` (5 workflows)
- `.planning/` (if exists)
- Agent prompt templates

**Action**: Extract CONCEPTS only (e.g., "reservation workflow needs guest comms step"), not files.

### Photos (127 files, ~50MB)

**Reason**: Managed via HotelRunner, Cloudinary, or Vercel Image Optimization. Not in git.

**Action**: Upload to CDN during Phase 2. Delete from old repo after upload.

### Linear Task References

**Reason**: New project, new Linear workspace, fresh task tracking.

**Action**: Close old Linear workspace tasks with "Migrated to villa-thaifa-pms" note.

### Lux Collaboration Artifacts

**Reason**: Historical collaboration, not relevant to new build.

**Action**: Archive in old repo.

---

## Migration Effort Estimate

| Task                                            | Agent  | Estimated Hours |
| ----------------------------------------------- | ------ | --------------- |
| Write seed script (rooms.yaml → Postgres)       | Sonnet | 1-2 hours       |
| Write migration script (property.db → Postgres) | Sonnet | 1-2 hours       |
| Extract key policies (3-4 files)                | Sonnet | 1 hour          |
| Consolidate OTA mapping                         | Sonnet | 1 hour          |
| Summarize HotelRunner API research              | Sonnet | 1 hour          |
| Extract Expedia onboarding                      | Sonnet | 0.5 hour        |
| Create .env.example                             | Manual | 0.5 hour        |
| Archive old repos (README, deprecation notice)  | Manual | 1 hour          |
| **Total**                                       | —      | **7-9 hours**   |

---

## Data Integrity Checks

### Pre-Migration Verification

- [ ] `ssot/rooms.yaml` has 12 rooms (count verified)
- [ ] `property.db` has 12 rows in `rooms` table
- [ ] `property.db` has 21 rows in `beds` table
- [ ] `property.db` has 94 rows in `amenities` table
- [ ] All 12 rooms have pricing in EUR and MAD

### Post-Migration Verification

- [ ] Vercel Postgres `rooms` table has 12 rows
- [ ] All rooms have `base_rate_eur` > 0 and `base_rate_mad` > 0
- [ ] All 21 beds linked to correct room_id (FK integrity)
- [ ] All 94 amenities linked to correct room_id (FK integrity)
- [ ] `docs/policies/` has 3-4 policy files
- [ ] `docs/integrations/` has channel-mapping.md + hotelrunner.md + expedia.md

### Conflict Resolution Rules

1. **rooms.yaml vs property.db**: rooms.yaml is SSOT
2. **Pricing discrepancies**: rooms.yaml pricing wins
3. **Missing fields**: Use NULL, don't fabricate data
4. **Duplicate amenities**: Deduplicate by (room_id, category, name)

---

## OTA Channel Mapping (5 Channels)

From HotelRunner research + existing docs:

| OTA             | Status  | Integration Type              | Villa Thaifa Rooms  | Notes                                       |
| --------------- | ------- | ----------------------------- | ------------------- | ------------------------------------------- |
| **Booking.com** | ACTIVE  | Two-Way XML (via HotelRunner) | 8 room types mapped | Said wants rooms by NUMBER, not just type   |
| **Expedia**     | ACTIVE  | Product API (via HotelRunner) | Unknown mapping     | 16.5% commission, steps 1-4 complete        |
| **Airbnb**      | ACTIVE  | 2-way API (via HotelRunner)   | Unknown mapping     | Native integration, rare for hotel software |
| **Agoda**       | ACTIVE  | Via HotelRunner               | Unknown mapping     | Standard OTA integration                    |
| **Trip.com**    | PENDING | Via HotelRunner               | Unknown mapping     | Contract imminent, prepare onboarding       |

**Action for Phase 1**: Create CHANNEL_MAPPING.md with room type → OTA code mapping for all 5 channels.

---

## Room Data Schema (from rooms.yaml + property.db)

### rooms.yaml Structure (SSOT)

```yaml
rooms:
  - id: "room-01"
    internal_name: "Room 01"
    type: "deluxe"
    floor: 1
    size_m2: 35
    capacity_adults: 2
    is_smoking: false
    has_kitchen: false
    base_rate_eur: 169
    base_rate_mad: 1813 # Updated by agent, not manual
    description_en: "..."
    description_fr: "..."
    amenities:
      - category: "comfort"
        name: "air_conditioning"
        value: true
      # ... more amenities
    beds:
      - type: "king"
        width_cm: 180
        count: 1
```

### property.db Schema

```sql
-- Existing schema (to migrate FROM)
CREATE TABLE rooms (
    id INTEGER PRIMARY KEY,
    internal_name TEXT,
    type TEXT,
    floor INTEGER,
    size_m2 INTEGER,
    capacity_adults INTEGER,
    is_smoking INTEGER,  -- SQLite boolean
    has_kitchen INTEGER,
    base_rate_eur REAL,
    base_rate_mad REAL,
    description_en TEXT,
    description_fr TEXT,
    verification_status TEXT,
    verified_at TEXT,
    created_at TEXT,
    updated_at TEXT
);

CREATE TABLE beds (
    id INTEGER PRIMARY KEY,
    room_id INTEGER,
    type TEXT,
    width_cm INTEGER,
    count INTEGER,
    FOREIGN KEY (room_id) REFERENCES rooms(id)
);

CREATE TABLE amenities (
    id INTEGER PRIMARY KEY,
    room_id INTEGER,
    category TEXT,
    name TEXT,
    value INTEGER,  -- SQLite boolean or numeric value
    FOREIGN KEY (room_id) REFERENCES rooms(id)
);
```

### Target Postgres Schema (Phase 0)

```sql
-- New schema (to migrate TO)
CREATE TABLE rooms (
    id TEXT PRIMARY KEY,  -- Changed from INTEGER to TEXT to match "room-01" format
    internal_name TEXT NOT NULL,
    type TEXT NOT NULL,
    floor INTEGER,
    size_m2 INTEGER,
    capacity_adults INTEGER NOT NULL DEFAULT 2,
    is_smoking BOOLEAN DEFAULT FALSE,
    has_kitchen BOOLEAN DEFAULT FALSE,
    base_rate_eur DECIMAL(10,2) NOT NULL,
    base_rate_mad DECIMAL(10,2) NOT NULL,
    description_en TEXT,
    description_fr TEXT,
    verification_status TEXT,
    verified_at TIMESTAMP,
    created_at TIMESTAMP DEFAULT NOW(),
    updated_at TIMESTAMP DEFAULT NOW()
);

CREATE TABLE beds (
    id SERIAL PRIMARY KEY,
    room_id TEXT NOT NULL,
    type TEXT NOT NULL,
    width_cm INTEGER,
    count INTEGER NOT NULL DEFAULT 1,
    FOREIGN KEY (room_id) REFERENCES rooms(id) ON DELETE CASCADE
);

CREATE TABLE amenities (
    id SERIAL PRIMARY KEY,
    room_id TEXT NOT NULL,
    category TEXT NOT NULL,
    name TEXT NOT NULL,
    value TEXT,  -- Changed to TEXT for flexibility (JSON, boolean string, numeric)
    FOREIGN KEY (room_id) REFERENCES rooms(id) ON DELETE CASCADE
);
```

---

## Reservation Data (96 Extracted)

**Source**: `docs/specs/knowledge/villa-thaifa/state/current/reserverations/reservations.md`

**Format**: Markdown table with 96 rows

**Fields**: guest_name, guest_email, room_type, check_in, check_out, channel, status, total_eur

**Action**: DO NOT seed these. Historical data only. Real reservations come from HotelRunner sync in Phase 3.

**Use Case**: Reference for testing HotelRunner sync (compare formats, ensure idempotent upsert works).

---

## HotelRunner Integration Data Needs

### API Credentials (from .env)

```bash
# DO NOT commit to git
HOTELRUNNER_TOKEN=xxxxx
HOTELRUNNER_HR_ID=xxxxx
BOOKING_API_KEY=xxxxx  # If direct integration (unlikely)
EXPEDIA_API_KEY=xxxxx  # If direct integration (unlikely)
```

**Action**: Create `.env.example` with placeholders, add real values to Vercel env vars.

### API Rate Limit Constraints

- **Daily**: 250 requests/day per property
- **Per-minute**: 5 requests/minute per property
- **Global**: 75 requests/minute across all properties (not relevant for 1 property)

**Impact on Migration**: No impact (migration is one-time, <10 API calls).

**Impact on Phase 3**: Must implement caching + batching to stay under limits.

### Channel Codes (for CHANNEL_MAPPING.md)

Need to extract from existing `channel-mapping.md`:

- Booking.com channel codes (8 room types)
- Expedia product codes (if available)
- Airbnb listing IDs (if available)
- Agoda property codes (if available)
- Trip.com codes (TBD, contract pending)

**Agent task**: Parse existing channel-mapping.md → structured YAML or JSON → seed to Postgres (optional).

---

## Photo Migration Strategy

### Current State

- 127 room photos in old repo (~50MB)
- Stored in git (bad practice for binary assets)
- Unknown if photos are up-to-date

### Target State (Phase 2)

- Photos stored in CDN (Cloudinary or Vercel Image Optimization)
- Database stores CDN URLs, not files
- Photos managed via HotelRunner UI (Said uploads there)

### Migration Steps

1. Extract photo filenames from old repo
2. Match photos to room IDs
3. Upload to Cloudinary (free tier: 25GB storage, 25GB bandwidth/month)
4. Store URLs in `rooms` table (new column: `photo_url TEXT`)
5. Delete photos from old repo

**Agent**: Sonnet (script to match filenames → room IDs, generate upload script)

**Manual**: Actual Cloudinary upload (requires Omar's API key)

---

## Migration Playbook (Phase 0 Execution)

### Step 1: Extract Data (Agent: Sonnet)

```bash
# In old repo ~/villa-thaifa/
1. Parse ssot/rooms.yaml → JSON
2. Export property.db tables → CSV
3. Read key policy files → extract text
4. Read OTA mapping files → consolidate
5. Summarize HotelRunner research → markdown
```

### Step 2: Create New Repo (Manual: Omar)

```bash
gh repo create omar-elmountassir/villa-thaifa-pms --private
cd ~/villa-thaifa-pms/
git init
```

### Step 3: Write Migration Scripts (Agent: Sonnet)

```bash
# In new repo
1. Create seed.sql (from rooms.yaml JSON)
2. Create migrate.sql (from property.db CSV)
3. Create docs/policies/ (from extracted text)
4. Create docs/integrations/ (from consolidated files)
```

### Step 4: Execute Migration (Manual: Omar)

```bash
# Connect to Vercel Postgres
psql $DATABASE_URL < seed.sql
psql $DATABASE_URL < migrate.sql

# Verify
psql $DATABASE_URL -c "SELECT COUNT(*) FROM rooms;"  # Should be 12
psql $DATABASE_URL -c "SELECT COUNT(*) FROM beds;"   # Should be 21
psql $DATABASE_URL -c "SELECT COUNT(*) FROM amenities;"  # Should be 94
```

### Step 5: Archive Old Repos (Manual: Omar)

```bash
# In ~/villa-thaifa/
echo "DEPRECATED: Migrated to omar-elmountassir/villa-thaifa-pms" > README.md
git add README.md
git commit -m "Archive: Migrated to new repo"
git push

# Repeat for omar-elmountassir/villa-thaifa
```

---

## Changelog

### 2026-02-13 — Data Inventory Created

- Catalogued all data sources from existing project
- Defined migration vs. archive decisions
- Created migration playbook for Phase 0
- Identified 5 OTA channels (was 3, now 5)
- Added Booking.com special requirement (rooms by NUMBER)
- Added Trip.com as pending (contract imminent)

---

_This inventory is the SSOT for what migrates and what doesn't. Update as new data sources are discovered._

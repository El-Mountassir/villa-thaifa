# Data Inventory — Villa Thaifa Codebase Audit

**Created**: 2026-01-30
**Linear Issue**: [EM-191](https://linear.app/el-mountassir/issue/EM-191)
**Status**: Complete

---

## Summary

| Category   | Files          | Status         |
| ---------- | -------------- | -------------- |
| Room Data  | 3 sources      | ⚠️ CONFLICT    |
| Facilities | 2 files        | 🟡 Placeholder |
| Finance    | 2 files        | 🟡 Placeholder |
| Processes  | 4 files        | 🟡 Placeholder |
| Photos     | 12 directories | ✅ Organized   |
| Config     | 7 files        | ✅ Working     |
| Backup     | 3 files        | 📦 Archive     |

---

## 1. ROOM DATA (3 Sources — CONFLICT)

### 1.1 `data/core/inventory.yaml` — **Claims SSOT**

- **Format**: YAML
- **Currency**: EUR
- **Rooms**: 12
- **Last Validated**: 2026-01-24
- **Fields**: id, number, type, type_fr, capacity, beds, pricing, features, images
- **Status**: ⚠️ Missing descriptions

### 1.2 `src/data/rooms.json` — **Superset of YAML**

- **Format**: JSON
- **Currency**: EUR
- **Rooms**: 12
- **Fields**: id, number, type, capacity (with description), beds, price, features, description, images
- **Status**: ⚠️ Has descriptions that YAML lacks, otherwise identical pricing

### 1.3 `property.db` (SQLite) — **MAD Currency, Different Schema**

- **Tables**: rooms (12 rows), beds (empty), amenities (empty)
- **Currency**: MAD
- **Schema**: id (R01 format), expedia_type, internal_name, floor, occupancy_adults, size_m2, is_smoking, has_kitchen, base_rate_mad, verification_status
- **Status**: ⚠️ Different structure, MAD rates (~11x EUR), all VERIFIED status

**Currency Relationship**:

```
EUR (YAML/JSON)  ×  11  =  MAD (SQLite)
169 EUR         →   1859 MAD (Room 01)
449 EUR         →   4939 MAD (Room 12)
```

---

## 2. FACILITIES DATA

### 2.1 `src/data/facilities.json`

- **Facilities**: hall, garden, pool, spa
- **Status**: 🟡 ALL values "A confirmer" — pure placeholder

### 2.2 `docs/knowledge/property/VILLA_THAIFA.json`

- **Status**: 🟡 Mostly TODO, needs inspection

---

## 3. FINANCE DATA

### 3.1 `docs/knowledge/finance/rates.json`

- **Status**: 🟡 PLACEHOLDER — all values "TODO"
- **Designed for**: Seasonal rates, discounts, policies
- **Currency**: Claims MAD but no actual data

### 3.2 `docs/knowledge/finance/billing.json`

- **Status**: Unknown — needs inspection

---

## 4. PROCESS DATA

| File                                         | Content                 |
| -------------------------------------------- | ----------------------- |
| `docs/knowledge/processes/check-in-out.json` | Check-in/out procedures |
| `docs/knowledge/processes/housekeeping.json` | Housekeeping procedures |
| `docs/knowledge/processes/maintenance.json`  | Maintenance procedures  |
| `docs/knowledge/processes/emergency.json`    | Emergency procedures    |

**Status**: 🟡 Likely placeholder — needs verification

---

## 5. PHOTOS

| Location                    | Count     | Status       |
| --------------------------- | --------- | ------------ |
| `photos/01/` - `photos/12/` | 127 total | ✅ Organized |

**Status**: ✅ DONE — Room 12 ready for OTA upload

---

## 6. CONFIGURATION FILES

| File                                  | Purpose                   | Status     |
| ------------------------------------- | ------------------------- | ---------- |
| `labels/config.json`                  | Label definitions         | ✅ Working |
| `statuses/config.json`                | Status definitions        | ✅ Working |
| `sources/hotelrunner-api/config.json` | HotelRunner API config    | ✅ Working |
| `sources/agent-browser/config.json`   | Browser automation config | ✅ Working |
| `config.json`                         | Project-level config      | ✅ Working |
| `.planning/config.json`               | Planning config           | ✅ Working |
| `views.json`                          | View definitions          | ✅ Working |

---

## 7. BACKUP/ARCHIVE DATA

| File                                                  | Content                  |
| ----------------------------------------------------- | ------------------------ |
| `content/backup/booking/initial_scan_2026_01_13.json` | Booking.com initial scan |
| `sources/hotelrunner-api/data/reservations/*.json`    | Test reservation data    |

**Status**: 📦 Historical/test data

---

## 8. AGENT/DOCUMENTATION DATA

| File                                             | Purpose                    |
| ------------------------------------------------ | -------------------------- |
| `docs/agents/registry.json`                      | Agent registry             |
| `docs/agents/managers/booking/capabilities.json` | Booking agent capabilities |
| `docs/standards/agent-capability-schema.json`    | Agent capability schema    |
| `docs/project/standards/scoring-system.json`     | Scoring system             |
| `docs/knowledge/client/PROFILE.json`             | Client profile             |
| `docs/knowledge/communications/channels.json`    | Communication channels     |

---

## 9. ARCHIVE LOCATIONS (Read-Only)

| Location                                         | Content                           |
| ------------------------------------------------ | --------------------------------- |
| `archive/rooms_pre_db_migration/golden_records/` | Pre-migration room records        |
| `archive/deprecated_2026-01-30/`                 | Deprecated tasks/ and workstream/ |
| `legacy/archive_v1/`                             | Legacy v1 content                 |

---

## Key Observations

1. **Room data exists in 3 places** with different schemas
2. **EUR is operational**, MAD appears to be derived for Moroccan context
3. **rooms.json has descriptions** that inventory.yaml lacks — not truly redundant
4. **Most facilities/finance data is placeholder** — not yet populated
5. **Photos are well-organized** — only clear success
6. **SQLite schema designed for OTA integration** (expedia_type field)

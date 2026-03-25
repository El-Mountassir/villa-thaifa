# Data Foundation Audit — 2026-02-24

> **Purpose**: Pre-app-build data completeness and structural audit.
> **Scope**: `data/` directory against the 15 proposed DB models from codifiability-analysis.md.
> **Auditor**: Nova (read-only audit; no data files modified)
> **Reference**: `/home/director/omar/core/context/domains/business/villa-thaifa/codifiability-analysis.md`

---

## Summary

The `data/` directory is structurally sound and follows a well-enforced schema contract. All 12 room profiles exist, all financial and operational JSON files are present, and facility data has graduated from placeholder to canonical. However, three findings require Omar's attention before a seed script is written: (1) a confirmed rate drift between room profiles and the authoritative source for R02 and R05, (2) a systematic schema inconsistency in YAML `access` fields for rooms with pool access, and (3) the `pending-domains/facilities.md` placeholder is superseded but not yet archived. Additionally, the entire operational workflow layer (4 of 5 operation JSONs) is in placeholder status and will produce empty or stub data in the DB seed.

---

## Findings by Area

### A. Room Profiles (R01–R12)

**Status: STRUCTURALLY COMPLETE / 2 RATE ERRORS / SCHEMA DRIFT**

**Coverage**: All 12 rooms have `profile.md` files. All 12 have `images/` subdirectories.

**Template compliance**: The canonical fields from `context/meta/templates/room-profile-template.md` are present in all profiles — header block, Identity, Narrative, Marketing Hooks, OTA Fields, Structured Data (YAML), and Provenance. The template contract is consistently followed.

**Critical finding — Rate drift (R02 and R05)**:

The room profiles for R02 and R05 contain incorrect `base_rate_eur` and `base_rate_mad` values. The authoritative source (`data/finance/rates.json`, confirmed via `ops/decisions/2026-02-21-room-pricing-hotelrunner-confirmation.md`) was corrected on 2026-02-21, but the profile YAML blocks were NOT updated. The drift:

| Room | Profile `base_rate_eur` | rates.json (authoritative) | rooms.md (authoritative) | Status |
|------|------------------------|---------------------------|--------------------------|--------|
| R02 | 149 EUR / 1,597 MAD | **159 EUR / 1,704 MAD** | 159 EUR / 1,704 MAD | **ERROR** |
| R05 | 159 EUR / 1,704 MAD | **149 EUR / 1,597 MAD** | 149 EUR / 1,597 MAD | **ERROR** |

All other 10 rooms match. This is a seed-script blocker — if the seed reads from profiles, it will write wrong prices.

**Schema inconsistency — Pool access YAML field (R09, R10, R11)**:

The `views` array for R09, R10, and R11 encodes direct pool access as a string value (`pool view (direct access)`), but the formal `access` field is set to `null` for all three. R04 is correct: it uses `access: Pool access (direct)` AND has `pool view (direct access)` in views.

| Room | views contains | access field | Status |
|------|---------------|-------------|--------|
| R04 | `pool view (direct access)` | `Pool access (direct)` | Consistent |
| R09 | `pool view (direct access)` | `null` | **INCONSISTENT** |
| R10 | `pool view (direct access)` | `null` | **INCONSISTENT** |
| R11 | `pool view (direct access)` | `null` | **INCONSISTENT** |

A DB seed from YAML will produce `access: null` for R09/R10/R11 while `views` encodes the information as a non-normalized string. The `RoomView.has_direct_access` boolean proposed in the codifiability analysis cannot be reliably populated from current data for these three rooms.

**Schema inconsistency — View string format**:

R01, R02, R03, R08 use bare view names in YAML (`garden`). R04–R07, R09–R12 use descriptive strings (`pool view`, `atlas mountain view`, `pool view (direct access)`). A DB seed will produce heterogeneous enum values.

| Pattern | Rooms | Example |
|---------|-------|---------|
| Bare noun | R01, R02, R03, R08 | `garden` |
| Descriptive phrase | R04–R07, R09–R12 | `pool view`, `atlas mountain view` |

**Schema inconsistency — Size header vs YAML (minor)**:

8 of 12 profiles show `? m²` in the markdown header block while the YAML `size_m2` field has a value. The header is human-readable; the YAML is authoritative. Not a seed blocker (seed reads YAML), but creates visible inconsistency in the human-readable section.

**Data confidence state**:

11 of 12 rooms carry `data_confidence: owner_pending`. Only R04 is `verified`. This is expected and documented — the app must treat this as a first-class field, not a cleanup item.

**Mini bar state**:

10 of 12 rooms have `mini_bar: owner_pending`. R12 is `confirmed`. Matches the pending questions registry.

**Image naming inconsistency**:

Three naming conventions coexist across rooms:
- `_DSC####-HDR.jpg` (raw DSC originals) — e.g., R06
- `UUID.jpeg` — e.g., R12 (10 UUID files + main.jpg + photo-XX.jpg)
- `r0X-XX.jpg` / `photo-XX.jpg` / `main.jpg` — mixed convention

R12 has the most chaotic image naming: 10 UUID-named files alongside `main.jpg` and `photo-XX.jpg`. This will complicate Image metadata model seeding. No `is_hero` or `sort_order` metadata exists anywhere.

---

### B. rates.json + billing.json

**Status: rates.json CORRECT (R02/R05 drift is in profiles, not here) / billing.json INCOMPLETE**

**rates.json**:
- Covers all 12 rooms.
- Schema is clean: `room_id`, `internal_name`, `category_code`, `base_rate_eur`, `base_rate_mad`, `capacity`, `max_occupancy`.
- `data_confidence: confirmed`, `locked_until: 2026-12-31`.
- Exchange rate (10.72) is embedded in the file — adequate for Phase 0, but will need normalization into a separate `ExchangeRate` record in the DB.
- **rates.json IS the authoritative source**. The profile YAML drift documented in Section A is the bug.

**billing.json**:
- `data_confidence: owner_pending`.
- Legal entity, RC number, ICE number, tax ID, address: all `null`.
- Tax rates present (tourist tax 3 MAD/night, VAT 10%, city tax 5 MAD) — values match codifiability analysis.
- Payment methods: `["TODO"]` — no confirmed values.
- Invoicing: entirely unspecified.

The `Tax` and `PropertyPolicy.payment_methods` DB models cannot be seeded from billing.json in its current state beyond the three tax rate rows. The `Property.legal_entity` field cannot be seeded at all.

---

### C. operations/ JSONs

**Status: ALL 5 FILES PRESENT / 4 OF 5 ARE PURE PLACEHOLDERS**

| File | Status | Usable Data | Gap |
|------|--------|-------------|---------|
| `channels.json` | placeholder | Expedia property ID (114807934), Booking.com enabled, partial channel list | TODO values throughout: phone numbers, WhatsApp number, social handles, response times |
| `check-in-out.json` | placeholder | Check-in 14:00, Check-out 12:00, step structure | Late check-in, documents, staff scripts: all TODO |
| `housekeeping.json` | placeholder | Daily cleaning step structure, priority level taxonomy | Timing, deep clean frequency, supplier contacts: TODO |
| `emergency.json` | placeholder | Police (19), ambulance (15), Said's phone (+212 661-134194), emergency type protocols | Hospital name, assembly point, fire extinguisher locations, manager contact: TODO |
| `maintenance.json` | placeholder | Preventive checklist structure, priority taxonomy | All supplier contacts, response times, reporting channel: TODO |
| `channels_codes.csv` | complete | 139 HotelRunner channel codes | None — reference data |

The `Channel` DB model can be seeded from `channels_codes.csv` (139 records, all `enabled: false`) plus the partial `channels.json` data. All four workflow JSONs will seed near-empty records.

---

### D. property-config.json

**Status: PARTIAL — GPS and structure confirmed, many operational fields TODO**

**Confirmed and populated**:
- Property identity: name, type, Expedia property ID
- Location: full address, GPS coordinates (confirmed Google Maps 2026-02-19), neighborhood, airport code, distances, drive times
- Capacity: total rooms (12), total beds (25), max guests (37) — verified from rooms.md
- Ratings: Booking.com 9.3, TripAdvisor 3.0/5, Google 4.5/5 (22 reviews)
- Languages spoken: Arabic, Dutch, English, French
- Policies: check-in 14:00, check-out 12:00, cancellation policy (full text), pets not allowed, smoking designated areas
- Children policy: ages 2-12 at EUR 30/person/night
- Pool: infinity pool, heated: true
- Spa: hammam: true, booking required, minimum 4 guests
- WiFi: available, Free Wi-Fi
- Parking: available, Free parking
- Airport transfer: available (paid shuttle)
- Restaurant: on-site, breakfast rating 10

**Remains TODO (cannot seed)**:
- `payment_methods: ["TODO"]`
- Pool size, spa massage details
- Amenities: heating, safe, mini_bar, terrace, garden — all `"TODO"`
- Services: laundry, room service, concierge, tours — all `"TODO"`
- `room_types` section: `[{type: TODO, count: TODO}]` — unusable
- `secondary_phone` needs Said confirmation

**Minor stale entry**: The `todo` array still references the check-out time conflict (`internal=11:00 vs destinia OTA=13:30`), which was resolved to 12:00 on 2026-02-21. This entry was not cleaned up after resolution.

The `Property`, `PropertyPolicy`, and `PropertyRating` models can be seeded with known gaps. `Facility` records for pool, spa, parking, WiFi, restaurant can be partially seeded.

---

### E. bookings/

**Status: STRUCTURALLY ADEQUATE FOR PHASE 0 / DATA IS STALE (Dec 2025)**

**Current structure**:
```
data/bookings/
  exports/
    initial_scan_2026_01_13.json   — Booking.com room type baseline + amenity dictionary
    Trip.com_GDA.pdf               — Trip.com GDA agreement (PDF, not machine-readable)
  requests/
    2026-01-28-demande-anniversaire-30-personnes.md  — Single event request
  reservations/
    reservations.md                — 11 reservations as markdown table (Dec 2025)
```

**reservations.md**: Last updated 2025-12-20. Contains 11 reservations (all Dec 2025–Jan 2026). This is a static historical snapshot, not a live feed. There is no current-state reservation data. The file references `../planned/assignments.md` — that path (`data/bookings/planned/`) does not exist. **Broken internal link.**

**initial_scan_2026_01_13.json**: Useful seed data — contains 8 Booking.com room type mappings with platform IDs, titles, and a 200+ item amenity dictionary. This is the only machine-readable OTA mapping data for `RoomOTAMapping` seeding.

**Trip.com_GDA.pdf**: PDF format only — not machine-readable. Cannot be used by a seed script.

**Gaps**:
- No current reservation data beyond Dec 2025 snapshot.
- No Expedia or Trip.com reservation mappings.
- No `source_reservation_id` values for existing reservations.

The `Reservation` model can be seeded with the 11 historical records as sample data only. `RoomOTAMapping` can be partially seeded from `initial_scan`.

---

### F. admin/client/

**Status: COMPLETE FOR OPERATIONAL USE / STRATEGIC SECTIONS NOT DB-BOUND**

**Said Thaifa profile** (`data/admin/client/profile.md`, 514 lines):
- Contact info: WhatsApp (+212 661-134194), email (said_thaifa@hotmail.fr + saidthaifa@gmail.com) — confirmed.
- Communication protocol: formal register, vouvoiement, WhatsApp preferred — documented.
- Nezha Thaifa (co-manager/wife): role documented, no direct contact details.
- Booking.com scores: Staff 9.7, Breakfast 10, Cleanliness 9.4 — seeding ready for `PropertyRating.subcategories`.
- Sections 4–12 (business context, competitive analysis, financial baseline, risks, strategy): reference-only per codifiability analysis recommendation.

**contact.md**: Clean quick-reference card — no duplication, references profile.md as canonical.

**said-pending-questions.md**: 284 lines, organized registry of all items awaiting Said's confirmation. Aligned with the `data_confidence: owner_pending` field pattern throughout data files. Well-maintained.

**Support directory** (`data/admin/client/support/`): Contains only a `README.md`. Empty directory with documentation placeholder — acceptable (intent declared).

The `Contact` model can be seeded with Said Thaifa's record. Nezha Thaifa's record is partially seedable (role known, no phone/email).

---

### G. pending-domains/

**Status: SUPERSEDED — ARCHIVE PENDING**

`data/pending-domains/facilities.md` explicitly declares itself superseded. The header reads:

> **SUPERSEDED** — Individual facility files in `data/property/facilities/` are now the canonical source.

The file lists the 5 canonical paths that replaced it. It contains no live data — only a historical overview table and placeholders marked "To be confirmed."

This file should be archived to `archive/` or `data/archive/`. It has no operational value and creates ambiguity about which file is canonical for facilities.

---

### H. Images

**Status: PRESENT / NAMING CONVENTIONS INCONSISTENT / NO METADATA**

All 12 room `images/` directories are populated. Facility `images/` directories exist for hall (36 images), pool-garden (50 images), and spa-hammam (20 images).

**Image counts per room**:

| Room | Image count | Naming convention |
|------|------------|------------------|
| R01 | 35 | DSC originals + main.jpg |
| R02 | 34 | DSC originals + main.jpg + photo-XX.jpg |
| R03 | 35 | DSC originals |
| R04 | 32 | DSC originals + main.jpg + photo-XX.jpg |
| R05 | 33 | DSC originals + main.jpg |
| R06 | 40 | DSC originals + main.jpg + photo-XX.jpg |
| R07 | 47 | DSC originals + main.jpg + photo-XX.jpg |
| R08 | 24 | DSC originals |
| R09 | 43 | DSC originals + photo-XX.jpg |
| R10 | 40 | DSC originals |
| R11 | 50 | DSC originals |
| R12 | 20 | UUID.jpeg (10) + main.jpg + photo-XX.jpg |

**Critical inconsistency**: R12 uses UUID filenames for 10 of its 20 images, incoherent with every other room. Likely originated from a different import pipeline (OTA scrape vs. direct upload). Must be resolved before building the Image metadata model.

**No Image metadata exists**: No `sort_order`, `is_hero`, or `alt_text` data is maintained anywhere. Image metadata model is correctly deferred to Tier 2 / Phase 2 per codifiability analysis. For Phase 0/1, static file serving is viable.

---

### I. Coverage vs Codifiability Models

| Model | Tier | Data Exists? | Location | Completeness | Notes |
|-------|------|-------------|----------|-------------|-------|
| Room | 1 | YES | data/rooms/R01-R12/profile.md | ~85% | Rate drift in R02/R05 profiles; access field drift in R09/R10/R11; 8/12 sizes confirmed |
| RoomBed | 1 | YES | profile.md YAML `beds` block | ~95% | All 12 rooms present; sofa_bed missing size_cm (expected) |
| RoomView | 1 | YES (schema gap) | profile.md YAML `views` array | ~70% | View string format inconsistent; pool access not normalized for R09/R10/R11 |
| RoomBathroom | 1 | YES | profile.md YAML `bathroom` field | ~95% | All rooms present; R12 walk-in shower correctly distinguished |
| RoomLocalization | 1 | YES | profile.md Narrative + OTA sections | ~90% | EN/FR descriptions, taglines, OTA titles present for all 12 rooms |
| RoomOTAMapping | 1 | PARTIAL | data/bookings/exports/initial_scan_2026_01_13.json | ~40% | Booking.com mapping only (8 room types, not 12 rooms); no Expedia/Trip.com individual room IDs |
| Rate | 1 | YES (with drift) | data/finance/rates.json | ~95% | All 12 rooms present; drift exists in R02/R05 profile YAML (not rates.json itself) |
| ExchangeRate | 1 | YES | data/finance/rates.json `exchange_rate` field | ~80% | Single rate embedded; no `effective_date` tracking; no historical records |
| Property | 1 | PARTIAL | data/property/property-config.json | ~65% | Core identity and location confirmed; legal entity, payment methods, many services: null/TODO |
| PropertyRating | 1 | YES | property-config.json + data/admin/client/profile.md | ~85% | Three platforms present; Expedia rating absent; `last_scraped` not tracked |
| PropertyPolicy | 1 | PARTIAL | property-config.json `policies` block | ~60% | Check-in/out and cancellation confirmed; payment_methods: TODO |
| Facility | 1 | PARTIAL | data/property/facilities/*, property-config.json | ~50% | Pool, spa, restaurant, parking, WiFi present; pool size, spa hours, restaurant capacity: TODO |
| FacilityAttribute | 1 | PARTIAL | data/property/facilities/*.md | ~40% | Sparse structured attributes; most data is narrative markdown |
| Reservation | 1 | YES (stale) | data/bookings/reservations/reservations.md | ~60% | 11 historical records (Dec 2025); no live data; no source_reservation_id values |
| Channel | 1 | PARTIAL | data/operations/channels.json + channels_codes.csv | ~55% | 139 codes in CSV usable as seed; channels.json mostly TODO |
| Contact | 1 | YES | data/admin/client/profile.md + contact.md + facilities/services/services.md | ~80% | Said complete; Nezha role-only; Mr. Zakaria (transport) in facilities/services.md; manager: TODO |
| Tax | 1 | PARTIAL | data/finance/billing.json | ~50% | Three tax types with rates present; legal registration numbers: null |

**No model has zero data.** All 15 Tier 1 models have at least partial data representation.

**Structured data outside data/ that seed scripts must read**:
- `PropertyRating.subcategories` (Staff 9.7, Cleanliness 9.4, etc.) — in `data/admin/client/profile.md` Section 1, not `property-config.json`.
- Mr. Zakaria (transport contact) — in `data/property/facilities/services/services.md`, not `data/admin/`.
- Said Thaifa phone — appears consistently in three files (`contact.md`, `profile.md`, `emergency.json`). Seed from `contact.md` as canonical.

---

## Findings Requiring Omar's Judgment

1. **R02/R05 rate drift** — Profiles have wrong rates vs. rates.json. Fix is obvious (rates.json + rooms.md are the authority per decision doc). Recommend fixing profile YAML directly. No Said input needed.

2. **R12 pool access ambiguity** — Legacy provenance states `Pool access (direct)` for R12 but current YAML has `access: null`. R12 has a pool view confirmed and a double terrace. Is direct pool access from R12's patio real? Requires Said confirmation or on-site check before seeding `RoomView.has_direct_access`.

3. **Seed script read strategy** — Should the seed read rates from `rates.json` (authoritative, clean) or from room profile YAML (drifted for R02/R05)? Recommend rates.json as the sole rate source and document this explicitly in the seed script.

4. **Operations workflow JSON completeness** — 4 of 5 workflow JSONs are placeholders. Should these be filled before the app build begins (Said input required) or left as "seed with what exists and show pending in UI"? The codifiability analysis recommends the latter, but Omar should confirm.

5. **R06/R07 terrace size** — These remain open conflicts (ops/decisions/open-conflicts-registry.md items 2 and 3). The DB seed will use rooms.md values (100 m² and 60 m² respectively) unless Said confirms otherwise.

---

_Audit conducted 2026-02-24. Read-only. No data files modified._
_Source evidence: direct file reads of all 12 room profiles, rates.json, billing.json, 5 operations JSONs, property-config.json, reservations.md, initial_scan, profile.md, contact.md, pending-domains/facilities.md, open-conflicts-registry.md, room-pricing-hotelrunner-confirmation.md, truth.md._

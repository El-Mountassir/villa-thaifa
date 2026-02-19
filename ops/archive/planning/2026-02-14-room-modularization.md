# Room Data Modularization Plan

**Created:** 2026-02-14
**Status:** Ready for Implementation
**Estimated Time:** ~2 hours

---

## Resume Command

```
Resume the room data modularization plan. Start with Phase 1: Prepare.
```

---

## Context

Current `rooms.md` is a 942-line monolithic file containing:
- Data contract (metadata, rules, normalization)
- Master table (12 rooms × 24 columns)
- Room profiles (12 × ~70 lines each)

**Pain Points Addressed:**
- A: Navigation — Hard to find/edit specific room data
- B: Updates — Risk of breaking other rooms, noisy git diffs
- C: Reusability — Need to feed OTA, website, CMS, API
- D: Collaboration — Multiple editors need safe access

---

## Decisions Summary

| Aspect | Decision |
|--------|----------|
| YAML format | Verbose (full profiles ~60 lines per room) |
| Provenance | Preserve (add reconciliation notes for traceability) |
| OTA exports | All current + future (extensible mapping system) |
| Automation | Pre-commit hook (GitHub Action later if needed) |
| rooms.md fate | Archive first, then generate fresh |
| CLI features | Full CRUD + Batch operations |
| Exports | Consolidate into single generate.py script |

---

## Final File Structure

```
data/core/property/inventory/rooms/
├── contract.md
├── schema.yaml
├── rooms/
│   ├── R01.yaml
│   ├── R02.yaml
│   └── ... (R03-R12.yaml)
├── views/
│   └── rooms.md              # Auto-generated, read-only
├── exports/
│   ├── mappings/             # OTA field mappings
│   │   ├── expedia.yaml
│   │   ├── booking.yaml
│   │   ├── airbnb.yaml
│   │   ├── tripadvisor.yaml
│   │   ├── vrbo.yaml
│   │   └── api.yaml
│   ├── expedia.csv
│   ├── booking.csv
│   ├── airbnb.csv
│   ├── tripadvisor.csv
│   ├── vrbo.csv
│   └── api.json
├── scripts/
│   ├── validate.py
│   ├── generate.py
│   └── room-cli.py
└── backup/
    └── rooms-backup-2026-02-14-pre-modular.md
```

---

## Implementation Phases

### Phase 1: Prepare (15 min)

**Tasks:**
1. Create directories: `rooms/`, `views/`, `scripts/`, `exports/mappings/`
2. Create `schema.yaml` with validation rules
3. Create `contract.md` (extract from current rooms.md lines 1-55)

**schema.yaml structure:**
```yaml
# Field definitions, types, required/optional, enums, character limits
room:
  id: { type: string, required: true, pattern: "^R[0-9]{2}$" }
  number: { type: string, required: true }
  category_code: { type: string, required: true }
  
identity:
  internal_name: { type: string, required: true }
  fr_name: { type: string, required: true }

pricing:
  base_eur: { type: integer, required: true, min: 1 }
  base_mad: { type: integer, required: true, min: 1 }

# ... etc
```

**Deliverables:**
- [ ] `schema.yaml`
- [ ] `contract.md`
- [ ] Directory structure created

---

### Phase 2: Extract (30 min)

**Tasks:**
1. Parse current rooms.md
2. Generate 12 verbose YAML files with full profile data
3. Include provenance section in each file

**YAML file template (verbose):**
```yaml
id: R01
number: "01"
category_code: DELUXE_TRIPLE

identity:
  internal_name: Deluxe Triple Room
  fr_name: Triple Deluxe

capacity:
  adults: 3
  max_occupancy: 3

pricing:
  base_eur: 169
  base_mad: 1812

beds:
  - type: king
    size_cm: 200
    count: 1
  - type: sofa_bed
    count: 1

location:
  floor: ground
  views: [garden]
  access: null

features:
  size_m2: 44
  outdoor: Furnished patio (Ground Floor)
  bathroom: Shower/tub combination; Hair dryer
  climate: Independent air conditioning; Heating control
  layout: [laptop_friendly_workspace]
  smoking_allowed: false
  has_kitchen: false

narrative:
  description_en: "Deluxe triple room with garden view..."
  description_fr: "Chambre 1 triple de luxe..."
  tagline: "Spacious garden retreat perfect for small families"

marketing:
  persona: Couples with child, small families, value-conscious travelers
  highlights:
    - 44 m² of living space on ground floor
    - King bed plus comfortable sofa bed
    - Direct garden access from furnished patio

ota:
  expedia_type: Triple Room
  booking_label: Chambre Triple de Luxe
  expedia_title: Deluxe Triple Room, Garden View
  booking_title: Chambre Triple de Luxe
  short_desc_en: "44 m² ground-floor room..."
  short_desc_fr: "44 m² au rez-de-chaussée..."

provenance:
  source: rooms-2.md + rooms-4.md (alias enrichment)
  legacy_features: [Jardin, Rez-de-chaussée]
  legacy_amenities: []
  last_verified: "2026-02-13"

meta:
  data_confidence: owner_pending
  status: VERIFIED
```

**Deliverables:**
- [ ] `rooms/R01.yaml` through `rooms/R12.yaml`

---

### Phase 3: Build Scripts (45 min)

**3a. scripts/validate.py**
```bash
Usage: python validate.py [--room R01] [--all]

- Validates YAML syntax
- Checks against schema.yaml
- Reports missing/invalid fields
- Exit code 1 on failure (for pre-commit)
```

**3b. scripts/generate.py**
```bash
Usage: python generate.py [view|exports|all]

Generates:
- views/rooms.md (full markdown document)
- exports/expedia.csv
- exports/booking.csv
- exports/airbnb.csv
- exports/tripadvisor.csv
- exports/vrbo.csv
- exports/api.json
```

**3c. scripts/room-cli.py**
```bash
Usage: 
  room-cli.py list                    # Show all rooms
  room-cli.py show R01                # Display room details
  room-cli.py edit R01 --field pricing.base_eur --value 179
  room-cli.py batch --price-increase 5  # Increase all prices by 5%
  room-cli.py validate                # Run validation
  room-cli.py generate                # Regenerate views/exports
```

**3d. OTA Mapping Templates**

Each OTA gets a mapping file in `exports/mappings/`:

```yaml
# exports/mappings/expedia.yaml
name: Expedia
output_file: expedia.csv
columns:
  - { source: id, target: "Room ID" }
  - { source: identity.internal_name, target: "Room Name" }
  - { source: ota.expedia_title, target: "Title" }
  - { source: ota.short_desc_en, target: "Description (EN)" }
  - { source: ota.short_desc_fr, target: "Description (FR)" }
  - { source: capacity.max_occupancy, target: "Max Occupancy" }
  - { source: beds, target: "Bed Type", format: "bed_summary" }
  - { source: features.size_m2, target: "Size (m²)" }
```

**Deliverables:**
- [ ] `scripts/validate.py`
- [ ] `scripts/generate.py`
- [ ] `scripts/room-cli.py`
- [ ] `exports/mappings/expedia.yaml`
- [ ] `exports/mappings/booking.yaml`
- [ ] `exports/mappings/airbnb.yaml`
- [ ] `exports/mappings/tripadvisor.yaml`
- [ ] `exports/mappings/vrbo.yaml`
- [ ] `exports/mappings/api.yaml`

---

### Phase 4: Verify (15 min)

**Tasks:**
1. Run `python validate.py --all` — must pass
2. Run `python generate.py view`
3. Diff generated vs original:
   ```bash
   diff views/rooms.md data/core/property/inventory/rooms/rooms.md
   ```
4. Run `python generate.py exports`
5. Verify CSV outputs match current exports

**Success Criteria:**
- [ ] All 12 YAML files validate
- [ ] Generated views/rooms.md matches current rooms.md (data only, formatting OK to differ)
- [ ] All CSV exports contain correct data

---

### Phase 5: Cutover (15 min)

**Tasks:**
1. Archive current `rooms.md`:
   ```bash
   mkdir -p backup/
   cp rooms.md backup/rooms-backup-2026-02-14-pre-modular.md
   ```
2. Delete verified-safe archives:
   ```bash
   rm archive/rooms/2026-02-13/rooms-3.md
   rm archive/rooms/2026-02-13/rooms-4.md
   ```
3. Generate fresh `views/rooms.md` with header:
   ```markdown
   <!-- AUTO-GENERATED - DO NOT EDIT -->
   <!-- Generated: 2026-02-14 -->
   <!-- Source: rooms/*.yaml -->
   ```
4. Update any references to old file location

**Deliverables:**
- [ ] `backup/rooms-backup-2026-02-14-pre-modular.md`
- [ ] Deleted `archive/rooms/2026-02-13/rooms-3.md`
- [ ] Deleted `archive/rooms/2026-02-13/rooms-4.md`
- [ ] Fresh `views/rooms.md` generated

---

### Phase 6: Automation (15 min)

**Create `.pre-commit-config.yaml`:**
```yaml
repos:
  - repo: local
    hooks:
      - id: validate-rooms
        name: Validate room YAML files
        entry: python data/core/property/inventory/rooms/scripts/validate.py --all
        language: system
        files: ^data/core/property/inventory/rooms/rooms/.*\.yaml$
        pass_filenames: false
      
      - id: generate-rooms
        name: Regenerate room views and exports
        entry: python data/core/property/inventory/rooms/scripts/generate.py all
        language: system
        files: ^data/core/property/inventory/rooms/rooms/.*\.yaml$
        pass_filenames: false
```

**Install pre-commit:**
```bash
pip install pre-commit
pre-commit install
```

**Deliverables:**
- [ ] `.pre-commit-config.yaml`
- [ ] Pre-commit installed and tested

---

## File Inventory

| Action | File |
|--------|------|
| **Create** | `schema.yaml` |
| **Create** | `contract.md` |
| **Create** | `rooms/R01.yaml` ... `rooms/R12.yaml` |
| **Create** | `scripts/validate.py` |
| **Create** | `scripts/generate.py` |
| **Create** | `scripts/room-cli.py` |
| **Create** | `views/rooms.md` (generated) |
| **Create** | `exports/mappings/*.yaml` (6 files) |
| **Create** | `.pre-commit-config.yaml` |
| **Archive** | `backup/rooms-backup-2026-02-14-pre-modular.md` |
| **Delete** | `archive/rooms/2026-02-13/rooms-3.md` |
| **Delete** | `archive/rooms/2026-02-13/rooms-4.md` |
| **Merge** | Current `exports/export-ota.py` → `scripts/generate.py` |

---

## Completed Prior Work

- [x] Archive verification: rooms-3.md and rooms-4.md fully captured in canonical
- [x] MAD pricing fix: Corrected from rate ~11.0 to 10.72 (matches metadata)
- [x] Tagline/persona fixes: R05, R06, R10 refined
- [x] CSV exports: Added Max Occupancy + Bed Type columns

---

## Estimated Effort

| Phase | Time | Complexity |
|-------|------|------------|
| 1. Prepare | 15 min | Low |
| 2. Extract | 30 min | Medium |
| 3. Build Scripts | 45 min | High |
| 4. Verify | 15 min | Medium |
| 5. Cutover | 15 min | Low |
| 6. Automation | 15 min | Low |
| **Total** | **~2 hours** | |

---

## Notes

- **Pre-commit hook** chosen over GitHub Action for now (simpler, immediate feedback)
- **Verbose YAML** chosen for self-documentation and future extensibility
- **Provenance preserved** for audit trail and reconciliation confidence
- **OTA mappings** designed for easy addition of new platforms

---

*Plan created: 2026-02-14*
*Ready for implementation*

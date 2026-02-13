# Rooms Reconciliation Log

This file tracks one-by-one consolidation of room sources into the canonical markdown table at `data/core/property/inventory/rooms/rooms.md`.

## Rules Applied

- Baseline authority: `rooms.md`
- Legacy files are read-only references
- Override only when baseline is missing or legacy value is strictly more specific and non-conflicting
- On conflicts, keep baseline and log discrepancy
- Keep exactly 12 rows (`R01` to `R12`)

## Run: 2026-02-13

### Step 1 — Source: `rooms-1.md`

- Compared fields: Room ID, Internal Name, Expedia Type, Floor, Capacity, Size, Base Rate, Status
- Accepted changes: none
- Rejected conflicts:

1. `R01 size`: `rooms-1.md` contains `44.0`; baseline already canonicalized as `44 m²` and retained
2. Floor labels in French (`Rez-de-chaussée`, `1er étage`) were not imported because baseline is English-only

- Result: baseline retained; no data row change

### Step 2 — Source: `rooms-2.md`

- Compared fields: Names, pricing (EUR/MAD in source context), floor, view, beds, features, amenities
- Accepted changes: none
- Rejected conflicts:

1. French labels and mixed FR/EN descriptors were not imported into canonical English table
2. Source includes descriptive narrative fields not part of canonical table schema

- Result: baseline retained; no data row change

### Step 3 — Source: `rooms-3.md`

- Compared fields: same dimensions as Step 2 (stable variant)
- Accepted changes: none
- Rejected conflicts:

1. Same FR/EN mixed terminology and narrative profile fields outside canonical schema

- Result: baseline retained; no data row change

### Step 4 — Source: `rooms-4.md`

- Compared fields: summary table values + detailed profile attributes
- Accepted changes: none
- Rejected conflicts:

1. Source floor/view wording includes French terms (`RDC`, `Piscine`, `Jardin`), not imported
2. Source has condensed representation (EUR-only pricing context) and no stronger canonical MAD override

- Result: baseline retained; no data row change

### Step 5 — Cross-check: `../inventory.md`

- Compared fields: room type, capacity, beds, price, view, floor, terrace/area
- Accepted changes: none
- Rejected/recorded discrepancies:

1. `inventory.md` is mixed-language and EUR-oriented; canonical `rooms.md` remains MAD-oriented and English-only
2. Descriptive granularity differs (inventory has compact terrace/feature expressions)

- Result: no canonical row changes; discrepancy documented by design

## Validation Checklist

- [x] `rooms.md` contains exactly 12 room rows (`R01` to `R12`)
- [x] No duplicate room IDs
- [x] Required canonical columns present
- [x] Canonical values remain English-only
- [x] Legacy source handling recorded (rooms-1.md/rooms-2.md retired earlier; rooms-3.md/rooms-4.md archived with checksums)
- [x] Reconciliation steps recorded

### Step 6 — External Evidence Sync: Booking Extranet Screenshot (2026-02-13)

- Source: user-provided Booking screenshot for room sizes
- Scope: `Size (m²)` column only in `rooms.md`
- Accepted updates:

1. R02: `-` -> `41 m²`
2. R03: `-` -> `44 m²`
3. R04: `-` -> `24 m²`
4. R05: `-` -> `24 m²`
5. R06: `-` -> `40 m²`
6. R07: `-` -> `61 m²`
7. R08: `-` -> `44 m²`
8. R09: `-` -> `41 m²`
9. R10: `-` -> `41 m²`
10. R11: `-` -> `41 m²`

- Already consistent before sync:

1. R01: `44 m²`
2. R12: `82 m²`

- Notes:

1. Terrace values (for example 100 m² for R06 and 60 m² for R07) remain in `Outdoor` and are not used as room size.
2. This step resolves prior `Size (m²)` incompleteness without changing any non-size field.

### Step 7 — Schema Extension: Add `Access` Column (2026-02-13)

- Change type: canonical schema extension in `rooms.md`
- Reason: capture room-level access attributes explicitly for future app usage
- Column added: `Access` (between `View` and `Outdoor`)
- Values set in this step:

1. `R04` -> `Pool access (direct)`
2. All other rooms -> `-` (pending owner confirmation)

- Notes:

1. This step does not modify legacy files (`rooms-1.md` to `rooms-4.md`).
2. This step does not alter non-access values.

### Step 8 — Schema Extension: Add Metadata Columns (2026-02-13)

- Change type: canonical schema extension in `rooms.md`
- Columns added:

1. `Room Number`
2. `Room Category Code`
3. `Max Occupancy`
4. `Access Notes`
5. `Data Confidence`

- Population rules applied:

1. `Room Number` set from room IDs (`R01` -> `01`, ..., `R12` -> `12`)
2. `Room Category Code` set to stable machine-friendly enum-style codes
3. `Max Occupancy` set as numeric equivalent of `Capacity`
4. `Access Notes` populated for `R04` only (`Confirmed via Booking screenshot (2026-02-13)`), others set to `-`
5. `Data Confidence` set to `verified` for `R04` and `owner_pending` for all other rooms pending owner confirmation of access details

- Notes:

1. No legacy room source file was modified.
2. Existing room values (size, rates, beds, amenities, status) were preserved.

### Step 9 — Schema Extension: Add `Booking.com Label` Column (2026-02-13)

- Change type: canonical schema extension in `rooms.md`
- Reason: preserve Booking.com room naming/mapping explicitly, similar to Expedia mapping
- Column added: `Booking.com Label`
- Source evidence: user-provided Booking screenshot (room-size page labels)
- Mapping applied:

1. `R01`, `R03`, `R08` -> `Chambre Triple de Luxe`
2. `R02` -> `Chambre Double De luxe`
3. `R04`, `R05` -> `Chambre Double Superieur`
4. `R06` -> `Suite Executive`
5. `R07` -> `Suite De Luxe King Size`
6. `R09`, `R11` -> `Suite Familiale`
7. `R10` -> `Suite`
8. `R12` -> `Suite Presidentiel`

- Notes:

1. Booking labels are platform-native strings and may remain non-English by design.
2. No legacy room source file was modified.
3. No non-booking field was changed in this step.

### Step 10 — Schema Extension: Add `Smoking Allowed` and `Has Kitchen` (2026-02-13)

- Change type: canonical schema extension in `rooms.md`
- Reason: preserve unique technical metadata from `rooms-1.md` before potential legacy-file deletion
- Columns added:

1. `Smoking Allowed`
2. `Has Kitchen`

- Source evidence: `rooms-1.md` technical details

1. `All rooms are non-smoking (is_smoking: 0)`
2. `No rooms have a kitchen (has_kitchen: 0)`

- Values applied:

1. `Smoking Allowed` -> `No` for all `R01` to `R12`
2. `Has Kitchen` -> `No` for all `R01` to `R12`

- Notes:

1. No other business fields were changed.
2. This closes the last known unique metadata gap from `rooms-1.md`.

### Step 11 — Contract Hardening: Table + Profile Contracts (2026-02-13)

- Change type: canonical contract update in `rooms.md`
- Scope: `## Data Contract (Markdown Canonical)` section
- Additions:

1. Explicit `Table Contract` block with required rows/columns
2. Explicit `Room Profile Contract` with required fields per `R01` to `R12`
3. Explicit normalization rules (`RDC` -> `Ground Floor`, `Piscine` -> `Pool`, `m2` -> `m²`, etc.)
4. Explicit conflict resolution policy (baseline authority + override constraints)

- Notes:

1. No room row values were changed in this step.
2. No profile text values were changed in this step.

### Step 12 — Legacy File Retirement: `rooms-3.md` (2026-02-13)

- Gate used: normalized value-level parity check (`scripts/check_unique_info.py`)
- Result: `MISSING_TOKENS: 0` (pass)
- SHA256 (pre-archive): `725cbb9b7550ce4747920a9d1ee00422533525632d71a16d3ad4e6e009029988`
- Action: moved from active inventory folder to archive
- Archive path: `archive/rooms/2026-02-13/rooms-3.md`

### Step 13 — Legacy File Retirement: `rooms-4.md` (2026-02-13)

- Gate used: normalized value-level parity check (`scripts/check_unique_info.py`)
- Result: `MISSING_TOKENS: 0` (pass)
- SHA256 (pre-archive): `3452bfbc395892af87485abf132d344718ebddae1d78f9110067af8cf35508b6`
- Action: moved from active inventory folder to archive
- Archive path: `archive/rooms/2026-02-13/rooms-4.md`

### Step 14 — Archive Traceability Artifact (2026-02-13)

- File created: `archive/rooms/2026-02-13/rooms-legacy-checksums.sha256`
- Contains pre-archive checksums for `rooms-3.md` and `rooms-4.md`

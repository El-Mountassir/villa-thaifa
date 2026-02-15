# Villa Thaifa — Room Master Table

This document provides a normalized, single-table view of all 12 Villa Thaifa rooms, including operational specs and multilingual narrative profiles.

## Repository Metadata

- **Version**: 3.0
- **Currency**: Primary: EUR | Secondary: MAD (Rate: 10.72)
- **Canonical Status**: ACTIVE
- **Source Artifacts**: `inventory.yaml`, `rooms.json`, `property.db`
- **Consolidated On**: 2026-02-13
- **Profile Schema Updated**: 2026-02-13

## Data Contract (Markdown Canonical)

- Canonical room source for this phase: `data/core/property/inventory/rooms/rooms.md`
- Reconciliation traceability: `data/core/property/inventory/rooms/rooms-reconciliation-log.md`

### Table Contract

- Required rows: exactly 12 (`R01` to `R12`)
- Required columns: Room ID, Room Number, Room Category Code, Internal Name, Expedia Type, Booking.com Label, Floor, Capacity, Max Occupancy, Smoking Allowed, Has Kitchen, Size (m²), Base Rate (MAD), Base Rate (EUR), Beds, View, Access, Access Notes, Outdoor, Bathroom, Climate, Layout, Data Confidence, Status

### Room Profile Contract

- Required profile sections: exactly 12 (`### R01` to `### R12`)
- Required subsections per profile: Identity, Narrative, Marketing Hooks, OTA Fields, Structured Data, Provenance
- Required fields per subsection:
  - **Identity**: FR Name, Internal Code
  - **Narrative**: Description (EN), Description (FR), Tagline
  - **Marketing Hooks**: Target Persona, Highlights (3-5 bullets)
  - **OTA Fields**: Expedia Title, Booking.com Title, Short Description (EN), Short Description (FR)
  - **Structured Data**: Full YAML mirror of table columns
  - **Provenance**: Legacy Features, Legacy Amenities, Profile Source, Last Verified
- Character limits:
  - Tagline: ≤80 characters
  - Expedia Title: ≤50 characters
  - Booking.com Title: ≤35 characters
  - Short Descriptions: ≤150 characters

### Normalization Rules

- Capacity format: `N adults`
- Missing optional values: `-`
- Multi-values separator: `;`
- Canonical language: English primary; platform-native labels and preserved FR profile text are allowed
- Alias normalization for reconciliation: `RDC` => `Ground Floor`; `1er`/`1er etage` => `First Floor`; `Piscine` => `Pool`; `Jardin` => `Garden`; `m2` => `m²`

### Conflict Resolution Rules

- Baseline authority: `rooms.md`
- Legacy files are reference-only sources
- Override only when baseline is missing and source is strictly more specific and non-conflicting
- On conflicts, keep baseline and log discrepancy in reconciliation log

## Room Master Table

| Room ID | Room Number | Room Category Code | Internal Name        | Expedia Type       | Booking.com Label        | Floor                  | Capacity | Max Occupancy | Smoking Allowed | Has Kitchen | Size (m²) | Base Rate (MAD) | Base Rate (EUR) | Beds                             | View                                        | Access               | Access Notes                                  | Outdoor                               | Bathroom                                 | Climate                                       | Layout                                                                            | Data Confidence | Status   | Profile Link |
| ------- | ----------- | ------------------ | -------------------- | ------------------ | ------------------------ | ---------------------- | -------- | ------------- | --------------- | ----------- | --------- | --------------- | --------------- | -------------------------------- | ------------------------------------------- | -------------------- | --------------------------------------------- | ------------------------------------- | ---------------------------------------- | --------------------------------------------- | --------------------------------------------------------------------------------- | --------------- | -------- | ------------ |
| R01     | 01          | DELUXE_TRIPLE      | Deluxe Triple Room   | Triple Room        | Chambre Triple de Luxe   | Ground Floor           | 3 adults | 3             | No              | No          | 44 m²     | 1812 MAD        | 169 EUR         | 1 x King (200 cm); 1 x Sofa Bed  | Garden view                                 | -                    | -                                             | Furnished patio (Ground Floor)        | Shower/tub combination; Hair dryer       | Independent air conditioning; Heating control | Laptop-friendly workspace                                                         | owner_pending   | VERIFIED | [Profile](../../../../../docs/content/pending/reference/rooms/01/R01_Deluxe_Triple.md) |
| R02     | 02          | DELUXE_DOUBLE      | Deluxe Double Room   | Double Room        | Chambre Double De luxe   | Ground Floor           | 2 adults | 2             | No              | No          | 41 m²     | 1704 MAD        | 159 EUR         | 1 x King (200 cm)                | Garden view                                 | -                    | -                                             | Furnished patio; 40 m² terrace        | Shower/tub combination; Hair dryer       | Independent air conditioning; Heating control | Laptop-friendly workspace                                                         | owner_pending   | VERIFIED | [Profile](../../../../../docs/content/pending/reference/rooms/02/R02_Deluxe_Double.md) |
| R03     | 03          | DELUXE_TRIPLE      | Deluxe Triple Room   | Triple Room        | Chambre Triple de Luxe   | Ground Floor           | 3 adults | 3             | No              | No          | 44 m²     | 1812 MAD        | 169 EUR         | 1 x King (200 cm); 1 x Sofa Bed  | Garden view                                 | -                    | -                                             | Furnished patio; Small terrace        | Shower/tub combination; Hair dryer       | Independent air conditioning; Heating control | Laptop-friendly workspace                                                         | owner_pending   | VERIFIED | [Profile](../../../../../docs/content/pending/reference/rooms/03/R03_Deluxe_Triple.md) |
| R04     | 04          | DOUBLE_SUPERIOR    | Double Room Superior | Double Room        | Chambre Double Superieur | Ground Floor (implied) | 2 adults | 2             | No              | No          | 24 m²     | 1597 MAD        | 149 EUR         | 1 x King (200 cm)                | Pool view (direct access)                   | Pool access (direct) | Confirmed via Booking screenshot (2026-02-13) | Furnished patio                       | Shower/tub combination; Hair dryer       | Independent air conditioning; Heating control | Laptop-friendly workspace                                                         | verified        | VERIFIED | [Profile](../../../../../docs/content/pending/reference/rooms/04/R04_Double_Superior.md) |
| R05     | 05          | DOUBLE_SUPERIOR    | Double Room Superior | Double Room        | Chambre Double Superieur | First Floor            | 2 adults | 2             | No              | No          | 24 m²     | 1597 MAD        | 149 EUR         | 1 x King (200 cm)                | Pool view                                   | -                    | -                                             | Furnished balcony; Upper floor        | Shower/tub combination; Hair dryer       | Independent air conditioning; Heating control | Laptop-friendly workspace                                                         | owner_pending   | VERIFIED | [Profile](../../../../../docs/content/pending/reference/rooms/05/R05_Double_Superior.md) |
| R06     | 06          | EXECUTIVE_SUITE    | Executive Suite      | Executive Suite    | Suite Executive          | First Floor            | 3 adults | 3             | No              | No          | 40 m²     | 1812 MAD        | 169 EUR         | 1 x King (200 cm); 1 x Sofa Bed  | Pool view; Atlas Mountain view; Garden view | -                    | -                                             | Furnished balcony; 100 m² terrace     | Shower/tub combination; Hair dryer       | Independent air conditioning; Heating control | Laptop-friendly workspace                                                         | owner_pending   | VERIFIED | [Profile](../../../../../docs/content/pending/reference/rooms/06/R06_Executive_Suite.md) |
| R07     | 07          | DELUXE_KING_SUITE  | Deluxe King Suite    | Suite              | Suite De Luxe King Size  | First Floor            | 4 adults | 4             | No              | No          | 61 m²     | 3527 MAD        | 329 EUR         | 1 x King (200 cm); 2 x Sofa Beds | Pool view; Mountain view                    | -                    | -                                             | Furnished balcony; 60 m² terrace      | Shower/tub combination; Hair dryer       | Independent air conditioning; Heating control | Laptop-friendly workspace; Separate sitting area; Separate dining area; Fireplace | owner_pending   | VERIFIED | [Profile](../../../../../docs/content/pending/reference/rooms/07/R07_Deluxe_King_Suite.md) |
| R08     | 08          | DELUXE_TRIPLE      | Deluxe Triple Room   | Triple Room        | Chambre Triple de Luxe   | First Floor            | 3 adults | 3             | No              | No          | 44 m²     | 1812 MAD        | 169 EUR         | 1 x King (200 cm); 1 x Sofa Bed  | Garden view                                 | -                    | -                                             | Furnished balcony                     | Shower/tub combination; Hair dryer       | Independent air conditioning; Heating control | Laptop-friendly workspace                                                         | owner_pending   | VERIFIED | [Profile](../../../../../docs/content/pending/reference/rooms/08/R08_Deluxe_Triple.md) |
| R09     | 09          | FAMILY_SUITE       | Family Suite         | Family Suite       | Suite Familiale          | Ground Floor           | 4 adults | 4             | No              | No          | 41 m²     | 2026 MAD        | 189 EUR         | 1 x King (200 cm); 2 x Sofa Beds | Pool view (direct access)                   | -                    | -                                             | Furnished patio; Double terrace       | Shower/tub combination; Hair dryer       | Independent air conditioning; Heating control | Laptop-friendly workspace; Fireplace                                              | owner_pending   | VERIFIED | [Profile](../../../../../docs/content/pending/reference/rooms/09/R09_Family_Suite.md) |
| R10     | 10          | SUITE              | Suite                | Suite              | Suite                    | Ground Floor (implied) | 3 adults | 3             | No              | No          | 41 m²     | 1919 MAD        | 179 EUR         | 1 x King (200 cm); 1 x Sofa Bed  | Pool view (direct access)                   | -                    | -                                             | Furnished patio; Double terrace       | Shower/tub combination; Hair dryer       | Independent air conditioning; Heating control | Laptop-friendly workspace                                                         | owner_pending   | VERIFIED | [Profile](../../../../../docs/content/pending/reference/rooms/10/R10_Suite.md) |
| R11     | 11          | FAMILY_SUITE       | Family Suite         | Family Suite       | Suite Familiale          | Ground Floor           | 4 adults | 4             | No              | No          | 41 m²     | 2026 MAD        | 189 EUR         | 1 x King (200 cm); 2 x Sofa Beds | Pool view (direct access)                   | -                    | -                                             | Furnished patio; Double terrace       | Shower/tub combination; Hair dryer       | Independent air conditioning; Heating control | Laptop-friendly workspace; Fireplace                                              | owner_pending   | VERIFIED | [Profile](../../../../../docs/content/pending/reference/rooms/11/R11_Family_Suite.md) |
| R12     | 12          | PRESIDENTIAL_SUITE | Presidential Suite   | Presidential Suite | Suite Presidentiel       | Ground Floor           | 4 adults | 4             | No              | No          | 82 m²     | 4813 MAD        | 449 EUR         | 1 x King (200 cm); 2 x Sofa Beds | Pool view                                   | -                    | -                                             | Furnished patio; Double terrace/patio | Shower only (walk-in shower); Hair dryer | Independent air conditioning; Heating control | Laptop-friendly workspace; Separate sitting area; Separate dining area            | owner_pending   | VERIFIED | [Profile](../../../../../docs/content/pending/reference/rooms/12/R12_Presidential_Suite.md) |


# Villa Thaifa — Room Master Table

This document provides a normalized, single-table view of all 12 Villa Thaifa rooms, including operational specs and multilingual narrative profiles.

## Repository Metadata

- **Version**: 2.0
- **Currency**: Primary: EUR | Secondary: MAD (Rate: 10.72)
- **Canonical Status**: ACTIVE
- **Source Artifacts**: `inventory.yaml`, `rooms.json`, `property.db`
- **Consolidated On**: 2026-02-13

## Data Contract (Markdown Canonical)

- Canonical room source for this phase: `data/core/property/inventory/rooms/rooms.md`
- Reconciliation traceability: `data/core/property/inventory/rooms/rooms-reconciliation-log.md`

Table Contract
- Required rows: exactly 12 (`R01` to `R12`)
- Required columns: Room ID, Room Number, Room Category Code, Internal Name, Expedia Type, Booking.com Label, Floor, Capacity, Max Occupancy, Smoking Allowed, Has Kitchen, Size (m²), Base Rate (MAD), Base Rate (EUR), Beds, View, Access, Access Notes, Outdoor, Bathroom, Climate, Layout, Data Confidence, Status

Room Profile Contract
- Required profile sections: exactly 12 (`### R01` to `### R12`)
- Required fields per profile: FR Name, Description (EN), Description (FR), Pricing (Legacy EUR/MAD), Legacy Features (Alias), Legacy Amenities (Alias), Profile Source

Normalization Rules
- Capacity format: `N adults`
- Missing optional values: `-`
- Multi-values separator: `;`
- Canonical language: English primary; platform-native labels and preserved FR profile text are allowed
- Alias normalization for reconciliation: `RDC` => `Ground Floor`; `1er`/`1er etage` => `First Floor`; `Piscine` => `Pool`; `Jardin` => `Garden`; `m2` => `m²`

Conflict Resolution Rules
- Baseline authority: `rooms.md`
- Legacy files are reference-only sources
- Override only when baseline is missing and source is strictly more specific and non-conflicting
- On conflicts, keep baseline and log discrepancy in reconciliation log

| Room ID | Room Number | Room Category Code | Internal Name        | Expedia Type       | Booking.com Label        | Floor                  | Capacity | Max Occupancy | Smoking Allowed | Has Kitchen | Size (m²) | Base Rate (MAD) | Base Rate (EUR) | Beds                             | View                                        | Access               | Access Notes                                  | Outdoor                               | Bathroom                                 | Climate                                       | Layout                                                                            | Data Confidence | Status   |
| ------- | ----------- | ------------------ | -------------------- | ------------------ | ------------------------ | ---------------------- | -------- | ------------- | --------------- | ----------- | --------- | --------------- | --------------- | -------------------------------- | ------------------------------------------- | -------------------- | --------------------------------------------- | ------------------------------------- | ---------------------------------------- | --------------------------------------------- | --------------------------------------------------------------------------------- | --------------- | -------- |
| R01     | 01          | DELUXE_TRIPLE      | Deluxe Triple Room   | Triple Room        | Chambre Triple de Luxe   | Ground Floor           | 3 adults | 3             | No              | No          | 44 m²     | 1859 MAD        | 169 EUR         | 1 x King (200 cm); 1 x Sofa Bed  | Garden view                                 | -                    | -                                             | Furnished patio (Ground Floor)        | Shower/tub combination; Hair dryer       | Independent air conditioning; Heating control | Laptop-friendly workspace                                                         | owner_pending   | VERIFIED |
| R02     | 02          | DELUXE_DOUBLE      | Deluxe Double Room   | Double Room        | Chambre Double De luxe   | Ground Floor           | 2 adults | 2             | No              | No          | 41 m²     | 1749 MAD        | 159 EUR         | 1 x King (200 cm)                | Garden view                                 | -                    | -                                             | Furnished patio; 40 m² terrace        | Shower/tub combination; Hair dryer       | Independent air conditioning; Heating control | Laptop-friendly workspace                                                         | owner_pending   | VERIFIED |
| R03     | 03          | DELUXE_TRIPLE      | Deluxe Triple Room   | Triple Room        | Chambre Triple de Luxe   | Ground Floor           | 3 adults | 3             | No              | No          | 44 m²     | 1859 MAD        | 169 EUR         | 1 x King (200 cm); 1 x Sofa Bed  | Garden view                                 | -                    | -                                             | Furnished patio; Small terrace        | Shower/tub combination; Hair dryer       | Independent air conditioning; Heating control | Laptop-friendly workspace                                                         | owner_pending   | VERIFIED |
| R04     | 04          | DOUBLE_SUPERIOR    | Double Room Superior | Double Room        | Chambre Double Superieur | Ground Floor (implied) | 2 adults | 2             | No              | No          | 24 m²     | 1639 MAD        | 149 EUR         | 1 x King (200 cm)                | Pool view (direct access)                   | Pool access (direct) | Confirmed via Booking screenshot (2026-02-13) | Furnished patio                       | Shower/tub combination; Hair dryer       | Independent air conditioning; Heating control | Laptop-friendly workspace                                                         | verified        | VERIFIED |
| R05     | 05          | DOUBLE_SUPERIOR    | Double Room Superior | Double Room        | Chambre Double Superieur | First Floor            | 2 adults | 2             | No              | No          | 24 m²     | 1639 MAD        | 149 EUR         | 1 x King (200 cm)                | Pool view                                   | -                    | -                                             | Furnished balcony; Upper floor        | Shower/tub combination; Hair dryer       | Independent air conditioning; Heating control | Laptop-friendly workspace                                                         | owner_pending   | VERIFIED |
| R06     | 06          | EXECUTIVE_SUITE    | Executive Suite      | Executive Suite    | Suite Executive          | First Floor            | 3 adults | 3             | No              | No          | 40 m²     | 1859 MAD        | 169 EUR         | 1 x King (200 cm); 1 x Sofa Bed  | Pool view; Atlas Mountain view; Garden view | -                    | -                                             | Furnished balcony; 100 m² terrace     | Shower/tub combination; Hair dryer       | Independent air conditioning; Heating control | Laptop-friendly workspace                                                         | owner_pending   | VERIFIED |
| R07     | 07          | DELUXE_KING_SUITE  | Deluxe King Suite    | Suite              | Suite De Luxe King Size  | First Floor            | 4 adults | 4             | No              | No          | 61 m²     | 3619 MAD        | 329 EUR         | 1 x King (200 cm); 2 x Sofa Beds | Pool view; Mountain view                    | -                    | -                                             | Furnished balcony; 60 m² terrace      | Shower/tub combination; Hair dryer       | Independent air conditioning; Heating control | Laptop-friendly workspace; Separate sitting area; Separate dining area; Fireplace | owner_pending   | VERIFIED |
| R08     | 08          | DELUXE_TRIPLE      | Deluxe Triple Room   | Triple Room        | Chambre Triple de Luxe   | First Floor            | 3 adults | 3             | No              | No          | 44 m²     | 1859 MAD        | 169 EUR         | 1 x King (200 cm); 1 x Sofa Bed  | Garden view                                 | -                    | -                                             | Furnished balcony                     | Shower/tub combination; Hair dryer       | Independent air conditioning; Heating control | Laptop-friendly workspace                                                         | owner_pending   | VERIFIED |
| R09     | 09          | FAMILY_SUITE       | Family Suite         | Family Suite       | Suite Familiale          | Ground Floor           | 4 adults | 4             | No              | No          | 41 m²     | 2079 MAD        | 189 EUR         | 1 x King (200 cm); 2 x Sofa Beds | Pool view (direct access)                   | -                    | -                                             | Furnished patio; Double terrace       | Shower/tub combination; Hair dryer       | Independent air conditioning; Heating control | Laptop-friendly workspace; Fireplace                                              | owner_pending   | VERIFIED |
| R10     | 10          | SUITE              | Suite                | Suite              | Suite                    | Ground Floor (implied) | 3 adults | 3             | No              | No          | 41 m²     | 1969 MAD        | 179 EUR         | 1 x King (200 cm); 1 x Sofa Bed  | Pool view (direct access)                   | -                    | -                                             | Furnished patio; Double terrace       | Shower/tub combination; Hair dryer       | Independent air conditioning; Heating control | Laptop-friendly workspace                                                         | owner_pending   | VERIFIED |
| R11     | 11          | FAMILY_SUITE       | Family Suite         | Family Suite       | Suite Familiale          | Ground Floor           | 4 adults | 4             | No              | No          | 41 m²     | 2079 MAD        | 189 EUR         | 1 x King (200 cm); 2 x Sofa Beds | Pool view (direct access)                   | -                    | -                                             | Furnished patio; Double terrace       | Shower/tub combination; Hair dryer       | Independent air conditioning; Heating control | Laptop-friendly workspace; Fireplace                                              | owner_pending   | VERIFIED |
| R12     | 12          | PRESIDENTIAL_SUITE | Presidential Suite   | Presidential Suite | Suite Presidentiel       | Ground Floor           | 4 adults | 4             | No              | No          | 82 m²     | 4939 MAD        | 449 EUR         | 1 x King (200 cm); 2 x Sofa Beds | Pool view                                   | -                    | -                                             | Furnished patio; Double terrace/patio | Shower only (walk-in shower); Hair dryer | Independent air conditioning; Heating control | Laptop-friendly workspace; Separate sitting area; Separate dining area            | owner_pending   | VERIFIED |

## Room Profiles (Multilingual + Narrative)

### R01 — Deluxe Triple Room

- **FR Name**: Triple Deluxe
- **Description (EN)**: Deluxe triple room with garden view, king bed and sofa bed for 2 people, ground floor of Villa Thaifa.
- **Description (FR)**: Chambre 1 triple de luxe - Vue jardin avec un canapé lit pour 2 personnes et au rez de chaussée de la villa Thaifa.
- **Pricing (Legacy EUR/MAD)**: 169 EUR / 1812 MAD
- **Legacy Features (Alias)**: Jardin, Rez-de-chaussée
- **Legacy Amenities (Alias)**: -
- **Profile Source**: rooms-2.md + rooms-4.md (alias enrichment)

### R02 — Deluxe Double Room

- **FR Name**: Deluxe Double
- **Description (EN)**: Deluxe double room with 40 m² terrace and garden view.
- **Description (FR)**: Chambre 2 chambre double de luxe avec un terrasse de 40 m2 vue jardin.
- **Pricing (Legacy EUR/MAD)**: 159 EUR / 1704 MAD
- **Legacy Features (Alias)**: rooms-2: 40 m² Terrace | rooms-4: Jardin, 40 m² Terrace
- **Legacy Amenities (Alias)**: -
- **Profile Source**: rooms-2.md + rooms-4.md (alias enrichment)

### R03 — Deluxe Triple Room

- **FR Name**: Triple Deluxe
- **Description (EN)**: Deluxe triple room with small terrace and garden view, ground floor.
- **Description (FR)**: Ch 3 triple de luxe avec une petite terrasse vue jardin au rez de chaussée.
- **Pricing (Legacy EUR/MAD)**: 169 EUR / 1812 MAD
- **Legacy Features (Alias)**: rooms-2: Petite terrasse (3-4 m²) | rooms-4: Jardin, Rez-de-chaussée, Petite terrasse (3-4 m²)
- **Legacy Amenities (Alias)**: -
- **Profile Source**: rooms-2.md + rooms-4.md (alias enrichment)

### R04 — Double Room Superior

- **FR Name**: Double Supérieure
- **Description (EN)**: Superior double room with pool access and bar access.
- **Description (FR)**: Ch 4 chambre double supérieur accès piscine et le bar.
- **Pricing (Legacy EUR/MAD)**: 149 EUR / 1597 MAD
- **Legacy Features (Alias)**: rooms-2: Pool access (direct) | rooms-4: Piscine (Accès direct)
- **Legacy Amenities (Alias)**: -
- **Profile Source**: rooms-2.md + rooms-4.md (alias enrichment)

### R05 — Double Room Superior

- **FR Name**: Double Supérieure
- **Description (EN)**: Superior double room with pool view from first floor.
- **Description (FR)**: Ch 5 chambre double supérieur vue piscine du premier etage.
- **Pricing (Legacy EUR/MAD)**: 149 EUR / 1597 MAD
- **Legacy Features (Alias)**: Piscine, 1er étage
- **Legacy Amenities (Alias)**: -
- **Profile Source**: rooms-2.md + rooms-4.md (alias enrichment)

### R06 — Executive Suite

- **FR Name**: Suite Exécutive
- **Description (EN)**: Beautiful executive suite with 100 m² terrace, pool/Atlas/garden views, first floor.
- **Description (FR)**: Suite excecutive 6 très belle avec une terrasse de 100 mètres carrés vue piscine et atlas et jardin top au premier étage.
- **Pricing (Legacy EUR/MAD)**: 169 EUR / 1812 MAD
- **Legacy Features (Alias)**: rooms-2: 100 m² Terrace | rooms-4: Piscine, Atlas, Jardin, 1er étage, 100 m² Terrace
- **Legacy Amenities (Alias)**: -
- **Profile Source**: rooms-2.md + rooms-4.md (alias enrichment)

### R07 — Deluxe King Suite

- **FR Name**: Suite Deluxe King
- **Description (EN)**: Deluxe king suite with separate living room, fireplace, 2 sofa beds, dining room, 60 m² terrace with pool and Atlas views.
- **Description (FR)**: Suite de luxe King size avec salon à part et une cheminée et 2 canapés et salle à manger et une terrasse de 60 m2 vue piscine et atlas le top.
- **Pricing (Legacy EUR/MAD)**: 329 EUR / 3527 MAD
- **Legacy Features (Alias)**: rooms-2: 60 m² Terrace | rooms-4: Piscine, Atlas, 1er étage, 60 m² Terrace
- **Legacy Amenities (Alias)**: Salon, Cheminée, Salle à manger
- **Profile Source**: rooms-2.md + rooms-4.md (alias enrichment)

### R08 — Deluxe Triple Room

- **FR Name**: Triple Deluxe
- **Description (EN)**: Triple room with sofa bed, garden view, first floor.
- **Description (FR)**: Chambre 8 avec un canapé lit vue jardin et au premier étage.
- **Pricing (Legacy EUR/MAD)**: 169 EUR / 1812 MAD
- **Legacy Features (Alias)**: Jardin, 1er étage
- **Legacy Amenities (Alias)**: -
- **Profile Source**: rooms-2.md + rooms-4.md (alias enrichment)

### R09 — Family Suite

- **FR Name**: Suite Familiale
- **Description (EN)**: Family suite with direct pool access, 2 sofa beds for 4 people, double terrace and fireplace.
- **Description (FR)**: Suite familiale accès piscine directe avec 2 canapés lits qui peut loger 4 personnes et avec double terrasse et une cheminée.
- **Pricing (Legacy EUR/MAD)**: 189 EUR / 2026 MAD
- **Legacy Features (Alias)**: rooms-2: Double terrasse, Pool access (direct) | rooms-4: Piscine + Acces direct piscine, Rez-de-chaussée, Double terrasse
- **Legacy Amenities (Alias)**: Cheminée
- **Profile Source**: rooms-2.md + rooms-4.md (alias enrichment)

### R10 — Suite

- **FR Name**: Suite
- **Description (EN)**: Spacious suite with double terrace and direct pool access.
- **Description (FR)**: Suite spacieuse avec double terrasse et accès direct piscine.
- **Pricing (Legacy EUR/MAD)**: 179 EUR / 1919 MAD
- **Legacy Features (Alias)**: rooms-2: Double terrasse spacieuse, Pool access (direct) | rooms-4: Piscine + Acces direct piscine, Double terrasse spacieuse
- **Legacy Amenities (Alias)**: -
- **Profile Source**: rooms-2.md + rooms-4.md (alias enrichment)

### R11 — Family Suite

- **FR Name**: Suite Familiale
- **Description (EN)**: Family room with direct pool access, double terrace, living room, fireplace and 2 spacious sofa beds.
- **Description (FR)**: Chambre familiale accès directe piscine avec double terrasse et avec un salon et une cheminée et avec 2 canapés lits spacieuses.
- **Pricing (Legacy EUR/MAD)**: 189 EUR / 2026 MAD
- **Legacy Features (Alias)**: rooms-2: Double terrasse, Pool access (direct) | rooms-4: Piscine + Acces direct piscine, Rez-de-chaussée, Double terrasse
- **Legacy Amenities (Alias)**: Salon, Cheminée
- **Profile Source**: rooms-2.md + rooms-4.md (alias enrichment)

### R12 — Presidential Suite

- **FR Name**: Suite Présidentielle
- **Description (EN)**: 82 m² presidential suite with dining room, living room/sleeping area, Italian shower and small bar.
- **Description (FR)**: Suite présidentielle de 82 m2 avec une salle à manger et de un salon lit pour dormir et une douche italienne et un petit bar top.
- **Pricing (Legacy EUR/MAD)**: 449 EUR / 4813 MAD
- **Legacy Features (Alias)**: rooms-2: 82 m² Area, Double terrasse, Pool access (direct) | rooms-4: Piscine + Acces direct piscine, Double terrasse, Area: 82 m2
- **Legacy Amenities (Alias)**: Salon, Salle à manger, Bar, Mini bar, Coffre fort, Douche italienne
- **Profile Source**: rooms-2.md + rooms-4.md (alias enrichment)

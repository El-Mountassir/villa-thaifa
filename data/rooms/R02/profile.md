# R02: Deluxe Double Room (Golden Record)

- **Type**: Double Room
- **Class**: Deluxe
- **Floor**: Ground Floor
- **Occupancy**: 2 Adults
- **Size**: 41 m² <!-- source: Booking.com admin 2026-02-21 -->
- **Sleeping**:
  - 1 King Bed (200cm)
- **View**: [x] Garden view
- **Outdoor**: [x] Furnished patio (40 m² Terrace)
- **Bathroom**: [x] Shower/tub combination, [x] Hair dryer
- **Kitchen**: [ ] No
- **Climate**: [x] Air conditioning (Independent), [x] Heating (Control)
- **Layout**: [x] Laptop friendly workspace, [ ] Desk (No)
- **Features**: Safe (Coffre fort) [assumed]
- **Amenities**: [x] Patio, [x] Terrace, [x] Bidet <!-- source: Booking.com admin 2026-02-21 -->
- **Mini bar**: No <!-- Confirmed: Said Thaifa 2026-02-25. Coffee/tea tray in all rooms. -->
- **Pricing**: 159 EUR <!-- Rate confirmed and locked until 2026-12-31 -->

### R02 — Deluxe Double Room

#### Identity

- **FR Name**: Deluxe Double
- **Internal Code**: DELUXE_DOUBLE

#### Narrative

- **Description (EN)**: Deluxe double room with 40 m² terrace and garden view.
- **Description (FR)**: Chambre 2 chambre double de luxe avec un terrasse de 40 m2 vue jardin.
- **Tagline**: Your private garden terrace retreat for two

#### Marketing Hooks

- **Target Persona**: Couples, romantic getaways, terrace lovers
- **Highlights**:
  - Expansive 40 m² private terrace
  - Ground floor with garden views
  - King bed in 41 m² room

#### OTA Fields

- **Expedia Title**: Deluxe Double Room, Garden View (31 chars)
- **Booking.com Title**: Chambre Double De luxe (22 chars)
- **Short Description (EN)**: 41 m² room with king bed, garden view, and stunning 40 m² private terrace. Ground floor. (88 chars)
- **Short Description (FR)**: 41 m² avec lit king, vue jardin et grande terrasse privée de 40 m². Rez-de-chaussée. (84 chars)

#### Structured Data (YAML)

```yaml
room_id: R02
room_number: '02'
category_code: DELUXE_DOUBLE
internal_name: Deluxe Double Room
expedia_type: Double Room
booking_label: Deluxe Double Room
booking_label_fr: Chambre Double De luxe
floor: Ground Floor
capacity: '2 adults'
max_occupancy: 2
smoking_allowed: false
has_kitchen: false
size_m2: 41
base_rate_mad: 1829
base_rate_eur: 169
beds:
  - type: king
    size_cm: 200
    count: 1
views:
  - garden
access: null
access_notes: null
outdoor: Furnished patio; 40 m² terrace
bathroom: Shower/tub combination; Hair dryer
climate: Independent air conditioning; Heating control
layout: Laptop-friendly workspace; Safe (Coffre fort) [assumed]
amenities: # source: Booking.com admin 2026-02-21
  cots_available: false
  sofa_bed: false
  sofa: false
  fireplace: false
  balcony: false
  patio: true
  terrace: true
  bidet: true
mini_bar: false # confirmed: Said Thaifa 2026-02-25
coffee_tea_tray: true # Espresso machine, tea sachets, kettle — Said 2026-02-25
bathroom_products: 'Shampoo, conditioner, soap, body lotion, bathrobes, shower cap' # Said 2026-02-25
data_confidence: owner_pending
status: VERIFIED
```

#### Provenance

- **Legacy Features (Alias)**: rooms-2: 40 m² Terrace | rooms-4: Jardin, 40 m² Terrace
- **Legacy Amenities (Alias)**: -
- **Profile Source**: rooms-2.md + rooms-4.md (alias enrichment)
- **Last Verified**: 2026-02-13

---

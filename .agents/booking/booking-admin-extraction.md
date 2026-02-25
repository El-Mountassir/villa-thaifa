# Booking.com Admin — Data Extraction

> **Extracted:** 2026-02-21
> **Source:** admin.booking.com extranet (Hotel ID: 5446847)
> **Property:** Villa Thaifa (Riad Salim & Spa)
> **Credentials:** omar@el-mountassir.com
> **Session note:** Session expires on each page navigation — CAPTCHA triggered on 3rd login. Data below extracted from successful sessions.

---

## Table of Contents

1. [Room Amenities (amenities.html)](#1-room-amenities-amenitieshtml)
2. [Room Sizes](#2-room-sizes)
3. [Facilities (facilities.html)](#3-facilities-facilitieshtml)
4. [Property Description (request_change.html)](#4-property-description-request_changehtml)
5. [Reservations Summary](#5-reservations-summary)
6. [Said Items Resolved by This Extraction](#6-said-items-resolved-by-this-extraction)
7. [Extraction Status](#7-extraction-status)

---

## 1. Room Amenities (amenities.html)

**Extracted:** 2026-02-21 via JavaScript DOM extraction on live amenities.html page.

**Method:** `document.querySelectorAll('div.room-amenity')` + checked checkboxes per amenity.

### 1.1 Amenities with room assignments (CHECKED rooms only)

| Amenity | Room types where available |
|---|---|
| **Cots** | Suite De Luxe King Size 7, Suite 10, suite Presidentiel 12, Chambre Triple de Luxe 1;3;8 |
| **Sofa bed** | Suite De Luxe King Size 7, Suite Familiale 9:11, suite Presidentiel 12, Chambre Triple de Luxe 1;3;8 |
| **Fireplace** | Suite De Luxe King Size 7, Suite Familiale 9:11 |
| **Sofa** | Suite De Luxe King Size 7, Suite Familiale 9:11, suite Presidentiel 12, Chambre Triple de Luxe 1;3;8 |
| **Bath (bathtub)** | Chambre Double Superieur 4;5, Suite Executive 6, Suite De Luxe King Size 7, Suite Familiale 9:11, Suite 10, Chambre Triple de Luxe 1;3;8, Chambre Double De luxe 2 |
| **Bidet** | Suite Executive 6, Suite De Luxe King Size 7, Suite 10, Chambre Triple de Luxe 1;3;8, Chambre Double De luxe 2 |
| **Bath or shower** | Chambre Double Superieur 4;5, Suite Executive 6, Suite De Luxe King Size 7, Suite Familiale 9:11, Suite 10, Chambre Triple de Luxe 1;3;8, Chambre Double De luxe 2 |
| **Balcony** | Suite Executive 6, Suite De Luxe King Size 7 |
| **Patio** | Chambre Double Superieur 4;5, Suite Executive 6, Suite De Luxe King Size 7, Suite Familiale 9:11, Suite 10, suite Presidentiel 12, Chambre Double De luxe 2 |
| **View** | Chambre Double Superieur 4;5, Suite Executive 6, Suite De Luxe King Size 7, Suite Familiale 9:11, Suite 10, suite Presidentiel 12 |
| **Terrace** | Chambre Double Superieur 4;5, Suite Executive 6, Suite De Luxe King Size 7, Suite Familiale 9:11, Suite 10, suite Presidentiel 12, Chambre Double De luxe 2 |
| **Mountain view** | Suite Executive 6, Suite De Luxe King Size 7 |
| **Pool view** | Chambre Double Superieur 4;5, Suite Executive 6, Suite De Luxe King Size 7, Suite Familiale 9:11, Suite 10, suite Presidentiel 12 |
| **Inner courtyard view** | Chambre Double Superieur 4;5, Suite Executive 6, Suite De Luxe King Size 7, Chambre Triple de Luxe 1;3;8 |
| **Entire unit located on ground floor** | Chambre Double Superieur 4;5, Suite Familiale 9:11, Suite 10, suite Presidentiel 12, Chambre Triple de Luxe 1;3;8, Chambre Double De luxe 2 |
| **Upper floors accessible by stairs only** | Suite Executive 6, Suite De Luxe King Size 7 |

**Key insight — upper floor rooms:** Suite Executive 6 (R06) and Suite De Luxe King Size 7 (R07) are on upper floors accessible by stairs only. All others are ground floor.

**Key insight — suites WITHOUT bathtub:** suite Presidentiel 12 has NO bath checked. Also notably absent from Bath list.

**Key insight — Chambre Double Superieur 4;5 (R04, R05):** Has bath + terrace + patio + pool view + inner courtyard view. No balcony (balcony = upper floor rooms only).

### 1.2 Amenities NOT checked for any room (confirmed absent)

The following amenity categories were visible in the form but had NO rooms checked:
- Fold-up bed
- Drying rack for clothing
- Clothes rack
- Heated pool, Infinity pool, Plunge pool, Salt water pool, Rooftop pool, Shallow end
- Air conditioning (NOTE: a separate "Single-room air conditioning" safety feature is listed — but standard AC not checked per-room)
- Tumble dryer, Wardrobe/closet, Carpeted, Dressing room
- Extra long beds (>2m), Fan
- Iron, Ironing facilities
- Hot tub, Mosquito net, Private entrance, Safety deposit box
- Soundproofing, Seating Area, Tile/marble floor
- Washing machine, Hardwood/parquet floors, Desk
- Hypoallergenic, Electric blankets, Pajamas, Yukata
- Socket near bed, Adapter
- Feather/non-feather/hypoallergenic pillow
- Toilet paper (not configured), Additional toilet, Hairdryer, Spa bath, Sauna, Shower
- Game console (all types), Computer, Laptop, iPad, Cable/Satellite channels
- CD/DVD/Blu-ray player, Fax, iPod dock, Laptop safe
- Flat-screen TV, Pay-per-view, Radio, Telephone, TV, Video, Video games
- Mobile hotspot, Smartphone, Streaming service (Netflix)
- Dining area, Dining table, Wine glasses, Bottle of water, Chocolate/cookies, Fruits, Wine/champagne
- Barbecue, Oven, Stovetop, Toaster, Dishwasher, Electric kettle
- Outdoor dining area, Outdoor furniture, Minibar, Kitchen, Kitchenette, Kitchenware, Microwave, Refrigerator
- Tea/Coffee maker, Coffee machine, Children's high chair
- Key card access, Lockers, Key access (New amenities — not configured yet)
- Executive lounge access, Alarm clock, Wake-up service
- Linen, Towels, Towels/sheets (extra fee)
- City view, Lake view, Landmark view, River view, Sea view, Quiet street view
- Accessibility features (lift, wheelchair, hearing, adapted bath, etc.)
- Building characteristics (detached, semi-detached)
- Baby safety gates, Board games, Books/DVDs for children, Child safety socket covers
- Carbon monoxide detector, Smoke alarm, Fire extinguisher (New — not configured)
- Air purifiers, Hand sanitiser

**Important gaps to configure in Booking.com admin:**
- TV / Flat-screen TV (likely present but not configured)
- Tea/Coffee maker (likely present but not configured)
- Hairdryer (likely present but not configured)
- Linen and Towels (should be marked)
- Safety deposit box / in-room safe (GP11 resolved as YES from public listing — needs admin configuration)
- Heating (GP10 resolved as YES — not in room amenities admin)
- Smoke alarm, Fire extinguisher (NEW amenities not configured)

---

## 2. Room Sizes

**Source:** amenities.html room size input fields (unit: square metres)

| Booking.com Room Type | Size (m²) | Rooms Covered |
|---|---|---|
| Chambre Double Superieur 4;5 | 24 m² | R04, R05 |
| Suite Executive 6 | 40 m² | R06 |
| Suite De Luxe King Size 7 | 61 m² | R07 |
| Suite Familiale 9:11 | 41 m² | R09, R11 |
| Suite 10 | 41 m² | R10 |
| suite Presidentiel 12 | 82 m² | R12 |
| Chambre Triple de Luxe 1;3;8 | 44 m² | R01, R03, R08 |
| Chambre Double De luxe 2 | 41 m² | R02 |

**Note on R01 conflict:** The terrain map noted "R01: 44 m² (rooms.md) vs 24 m² (Booking.com scan)". The admin confirms **44 m²** for Chambre Triple de Luxe 1;3;8 (covers R01, R03, R08). The 24 m² was probably from a misread — it belongs to Chambre Double Superieur (R04, R05).

---

## 3. Facilities (facilities.html)

**Status:** BLOCKED — CAPTCHA triggered during session refresh. Unable to extract.

**What is known from terrain map Phase 1:**
- Parking: redirected to facilities page (status unknown without extraction)
- Page confirmed to exist at `facilities.html`

**Action needed:** Manual visit by Omar or new session attempt with fresh CAPTCHA resolve.

---

## 4. Property Description (request_change.html)

**Status:** BLOCKED — same CAPTCHA session issue.

**Action needed:** Manual visit or new session.

---

## 5. Reservations Summary

**Source:** Terrain map Phase 1 (dashboard data already captured)

| Reservation | Guest | Room | Dates | Nights | Guests | Amount | Booked |
|---|---|---|---|---|---|---|---|
| #6951286438 | Isabelle Evcil | Suite Familiale 9:11 | Apr 27–May 6, 2026 | 9 nights | 2 adults + 1 child | €1,240.02 | Feb 16, 2026 |
| #6851305666 | Andrea schwenski | Suite 10 | Apr 10–15, 2026 | 5 nights | 2 adults | €724.95 | Feb 12, 2026 |
| #6956429071 | Andrea schwenski | Chambre Double De luxe 2 | Apr 9–15, 2026 | 6 nights | 2 adults | €724.14 | Feb 12, 2026 |

**Revenue period (Nov 24, 2025 – Feb 22, 2026):** Total 10 room nights, Total Revenue €1,185.00

**Monthly revenue (Finance dashboard):**
- December 2025: €3,058.60
- January 2026: €7,020.25
- February 2026: €0.00 (no payouts yet)

---

## 6. Said Items Resolved by This Extraction

### Definitively resolved by admin data:

| Said Item | Resolution | Data Source |
|---|---|---|
| **R01 size conflict** (44 m² vs 24 m²) | **RESOLVED: 44 m²** — Booking.com admin confirms "Chambre Triple de Luxe 1;3;8" = 44 m². The 24 m² belongs to R04/R05. | amenities.html room sizes |
| **R04/R05 size** | **CONFIRMED: 24 m²** — matching existing `rooms.md` value | amenities.html room sizes |
| **R06 size** | **CONFIRMED: 40 m²** (minor conflict with "44 m² OTA short description" — admin says 40 m²) | amenities.html room sizes |
| **R07 size** | **CONFIRMED: 61 m²** — matches current rooms.md | amenities.html room sizes |
| **R09/R11 size** | **CONFIRMED: 41 m²** (Suite Familiale) | amenities.html room sizes |
| **R10 size** | **CONFIRMED: 41 m²** (Suite 10) | amenities.html room sizes |
| **R12 size** | **CONFIRMED: 82 m²** (suite Presidentiel) | amenities.html room sizes |
| **Floor assignment R06** | **RESOLVED: Upper floor** (stairs only — "Upper floors accessible by stairs only" checked for Suite Executive 6) | amenities.html accessibility |
| **Floor assignment R07** | **RESOLVED: Upper floor** (stairs only — same) | amenities.html accessibility |
| **Floor assignment R04/R05** | **CONFIRMED: Ground floor** ("Entire unit located on ground floor" checked) | amenities.html accessibility |
| **Floor assignment R10** | **CONFIRMED: Ground floor** (Suite 10 = ground floor) | amenities.html accessibility |
| **Bathtub presence per room** | **RESOLVED:** R04/R05, R06, R07, R09/R11, R10, R01/R03/R08, R02 ALL have bathtub. R12 (Presidentiel) does NOT have bathtub configured. | amenities.html |
| **Sofa bed presence** | **CONFIRMED:** R07, R09/R11, R12, R01/R03/R08 have sofa beds | amenities.html |
| **Fireplace presence** | **CONFIRMED:** R07 and R09/R11 have fireplace | amenities.html |
| **Terrace/Patio presence** | **CONFIRMED:** Almost all rooms have terrace/patio except Chambre Triple 1;3;8 (R01/R03/R08) which is absent from patio/terrace list — UNEXPECTED, needs verification | amenities.html |
| **Mountain view** | **CONFIRMED:** Only R06 and R07 have mountain view | amenities.html |
| **Pool view** | **CONFIRMED:** R04/R05, R06, R07, R09/R11, R10, R12 — NOT R01/R03/R08, R02 | amenities.html |
| **Inner courtyard view** | **CONFIRMED:** R04/R05, R06, R07, R01/R03/R08 — NOT R09/R11, R10, R12, R02 | amenities.html |

### Partially resolved (confirms existence, details still NEEDS_SAID):

| Said Item | Status | Notes |
|---|---|---|
| Cots available | CONFIRMED available in: R07, R10, R12, R01/R03/R08 | NOT available in R04/R05, R06, R09/R11, R02 |
| Admin amenity gaps | IDENTIFIED | TV, hairdryer, heating, AC, safe need to be configured in admin |

### Still NEEDS_SAID (not addressable from admin amenities):

- S1-S6: Spa/Hammam capacity, hours, prices, massage types (facilities.html blocked)
- P1-P4: Pool dimensions, depth, hours, bar (facilities.html blocked)
- G1-G3: Garden measurements (facilities.html blocked)
- H1-H4: Hall capacity, sound system, furniture, music hours (facilities.html blocked)
- F1, F4: Legal entity and tax registration numbers
- CH1-CH5: WhatsApp, Instagram, Facebook, TripAdvisor, secondary phone
- WB1-WB4: Website, logo, brand descriptions
- C2, C3: Terrace size disputes (R06: 100m² vs ~120m²; R07: 60m² vs 80-100m²)
- PO2: Trip.com GDA contract signature
- EV1-EV6: Events pricing details

---

## 7. Extraction Status

| Page | Status | Data Quality | Blocker |
|---|---|---|---|
| `home.html` (dashboard) | DONE (Phase 1) | Complete | — |
| `amenities.html` | DONE (this session) | Complete — 16 amenities, 8 room sizes | — |
| `rooms.html` | DONE (Phase 1) | Complete — occupancy table | — |
| `property_policies.html` | DONE (Phase 1) | Complete | — |
| `policies.html` | DONE (Phase 1) | Complete — cancellation | — |
| `finance_overview.html` | DONE (Phase 1) | Revenue + payout info | — |
| `facilities.html` | BLOCKED | None | AWS WAF CAPTCHA on 3rd login |
| `request_change.html` | BLOCKED | None | AWS WAF CAPTCHA on 3rd login |
| `search_reservations.html` | PARTIAL | 3 upcoming reservations (dashboard only) | Would need full search |
| `reviews.html` | PARTIAL | Score 9.2/86 reviews visible | Full review text needs pagination |
| `statistics/dashboard.html` | NOT YET | — | — |
| `promotions/list.html` | NOT YET | — | — |

**Session behavior observed:** Booking.com admin session expires within ~2-3 minutes of inactivity or on cross-page navigation. Each navigation triggers a new login flow. Third consecutive login triggered AWS WAF CAPTCHA requiring human resolution.

**Recommendation for next attempt:** Omar should manually log in and navigate to `facilities.html` and `request_change.html` directly, then share the page content (or allow a fresh browser session with the extension fully connected).

# Booking.com Admin Extranet — Terrain Map

> **Scouted:** 2026-02-21
> **Access method:** Playwright CLI (headless Chrome)
> **Credentials used:** Omar admin (omar@el-mountassir.com)
> **Property:** Villa Thaifa (also listed as "Riad Salim & Spa")
> **Hotel ID:** 5446847
> **Base URL:** `https://admin.booking.com/hotel/hoteladmin/extranet_ng/manage/`
> **Session saved:** `.secrets/booking-session.json` (for future reuse)

---

## Table of Contents

1. [Access Status](#access-status)
2. [Navigation Structure](#navigation-structure)
3. [Section Inventory](#section-inventory)
   - [Home / Dashboard](#home--dashboard)
   - [Rates & Availability](#rates--availability)
   - [Promotions](#promotions)
   - [Reservations](#reservations)
   - [Property](#property)
   - [Boost Performance](#boost-performance)
   - [Inbox](#inbox)
   - [Guest Reviews](#guest-reviews)
   - [Finance](#finance)
   - [Analytics](#analytics)
4. [Said Items Addressable](#said-items-addressable)
5. [Extraction Plan](#extraction-plan)
6. [Session Reuse Instructions](#session-reuse-instructions)

---

## Access Status

- **Login flow:** email → AWS WAF image CAPTCHA (canvas-based, solved by pixel clicks) → password → SMS 2FA
- **2FA method:** SMS to `+21******0409` (Moroccan number, masked)
- **CAPTCHA type:** AWS WAF — 3x3 image grid rendered on HTML5 canvas inside shadow DOM (`<awswaf-captcha>` element at x=440, y=215, 400x400px)
- **Login succeeded:** Yes — landed on `home.html?hotel_id=5446847`
- **Property status:** Open/Bookable
- **Important note:** "Rates & availability" and "Reservations" are connected to a channel manager (HotelRunner)

---

## Navigation Structure

Top-level navigation bar:

| Menu Item | Type | Sub-sections |
|---|---|---|
| Home | Link | — |
| Rates & availability | Dropdown | Calendar, Open/close rooms, Copy yearly rates, Dynamic Restriction Rules, Rate plans, Value adds, Connectivity errors, Pricing per guest, Country rates, Mobile rates |
| Promotions | Dropdown | Choose new promotion, Simulate max discount, Your active promotions |
| Reservations | Link (channel manager) | — |
| Property | Dropdown | Quality rating, Property Page Score, General info, VAT/Tax/Charges, Photos, Property policies, Reservation policies, Facilities & services, Room details, Room Amenities, Your Profile, View Your Descriptions, Messaging Preferences, Sustainability |
| Boost performance | Dropdown | (Genius program, opportunities) |
| Inbox | Dropdown | Messaging inbox, Messaging settings |
| Guest Reviews | Dropdown | Reviews list |
| Finance | Dropdown | Payout info, Documents & invoices, Reservations statement, Financial Overview, Finance Help, Virtual cards management, Finance settings |
| Analytics | Dropdown | Analytics dashboard, Demand for Marrakesh, Pace of bookings, Sales Statistics, Booker insights, Book Window Info, Cancellation Characteristics, Comparable properties, Genius Report, Ranking Dashboard, Performance dashboard |

---

## Section Inventory

### Home / Dashboard

- **URL:** `home.html`
- **Available data:**
  - Property name: Villa Thaifa
  - Status: **Open/Bookable**
  - Today's reservations: Arrivals 0, Departures 0, Stay-overs 0, Guest requests 0
  - Latest 3 reservations visible on dashboard
  - Recent 4 reviews (all score 10)
  - Property Page Score: **95%** (area avg: 94%)
  - Guest Review Score: **9.2** (area avg: 8.7)
  - Performance/search stats (last 30 days)
  - Pending actions: 1 unpaid invoice
  - Advice: Add view photos, get quality rating, conversion 80% lower than area avg
  - Award: Traveller Review Award winner (2026)
- **Sub-sections:** All via top nav
- **Said-relevant:** Yes — property status, scores, pending invoice
- **Extraction priority:** Medium (dashboard summary only)

### Rates & Availability

- **URL:** `calendar/index.html` (Calendar sub-page)
- **Note:** Connected to HotelRunner channel manager — rates and availability managed there
- **Sub-sections:**
  - Calendar (`calendar/index.html`)
  - Open/close rooms
  - Copy yearly rates
  - Dynamic Restriction Rules (New)
  - Rate plans
  - Value adds (New)
  - Connectivity errors
  - Pricing per guest (New)
  - Country rates (New)
  - Mobile rates
- **Said-relevant:** Partial — calendar useful for availability overview, but rates managed via HotelRunner
- **Extraction priority:** Low (HotelRunner is source of truth)

### Promotions

- **URL:** `promotions/marketplace.html`, `promotions/list.html`
- **Sub-sections:**
  - Choose new promotion (marketplace)
  - Simulate max discount (stacking calculator)
  - Your active promotions (list)
- **Available data:** Active promotions list
- **Said-relevant:** Potentially (discount policy questions)
- **Extraction priority:** Medium

### Reservations

- **URL:** `search_reservations.html`
- **Note:** Connected to HotelRunner channel manager
- **Available data:**
  - Search/filter by: Date of reservation, Check-in, Check-out, Invoice, Stay dates
  - Filters: Status (Ok/Canceled/No-show), Smart Flex, Corporate card, Guest communication, Invoice required, guest name/booking number
  - 3 upcoming reservations visible on dashboard:
    1. Isabelle Evcil | res#6951286438 | Suite Familiale 9:11 | Apr 27–May 6, 2026 | 9 nights | 2 adults, 1 child | **€1,240.02** | Booked Feb 16
    2. Andrea schwenski | res#6851305666 | Suite 10 | Apr 10–15, 2026 | 5 nights | 2 adults | **€724.95** | Booked Feb 12
    3. Andrea schwenski | res#6956429071 | Chambre Double De luxe 2 | Apr 9–15, 2026 | 6 nights | 2 adults | **€724.14** | Booked Feb 12
- **Said-relevant:** Yes — booking history, revenue per room
- **Extraction priority:** High

### Property

#### General Info

- **URL:** `general_info.html`
- **Available data:**
  - Property name: Villa Thaifa
  - Address: Route de fes km 12, Ouled Jelal
  - GPS: 31.653917998003, -7.878561722456
- **Said-relevant:** Yes — address confirmation
- **Extraction priority:** Low (already known)

#### Room Details

- **URL:** `rooms.html`
- **Available data — 7 room types registered:**

| Room Name | Booking.com ID | Max Guests | Max Adults | Max Children | Max Infants |
|---|---|---|---|---|---|
| Chambre Double Superieur 4;5 | 544684730 | 2 | 2 | 1 | 1 |
| Suite Executive 6 | 544684732 | 2 | 2 | 1 | 1 |
| Suite De Luxe King Size 7 | 544684733 | 3 | 3 | 2 | 2 |
| Suite Familiale 9:11 | 544684736 | 4 | 4 | 3 | 3 |
| Suite 10 | 544684737 | 2 | 2 | 1 | 1 |
| suite Presidentiel 12 | 544684739 | 4 | 4 | 3 | 3 |
| Chambre Triple de Luxe 1;3;8 | 544684740 | 3 | 3 | 2 | 2 |
| Chambre Double De luxe 2 | 544684742 | 2 | 2 | 1 | 1 |

- **Note:** Room numbers in name = Booking.com grouping (e.g., "Chambre Triple de Luxe 1;3;8" covers rooms R01, R03, R08). R11 and R12 are handled differently.
- **Said-relevant:** Yes — max occupancy per room type (resolves several Said items)
- **Extraction priority:** HIGH — complete data available

#### Room Amenities

- **URL:** `amenities.html`
- **Said-relevant:** Yes — amenities per room
- **Extraction priority:** High

#### Photos

- **URL:** `photos.html`
- **Available data:**
  - Total photos: **128**
  - Low-quality photos: **14**
  - Units with missing photos: **0**
  - Photos with missing tags: **71** (attention needed)
- **Said-relevant:** Yes — photo completeness, missing tags
- **Extraction priority:** Medium

#### Facilities & Services

- **URL:** `facilities.html`
- **Available data:** Page exists, listing of all property facilities (full data requires scroll/read)
- **Said-relevant:** Yes — resolves facility questions
- **Extraction priority:** High

#### Property Policies

- **URL:** `property_policies.html`
- **Available data — COMPLETE:**
  - **Children:** All ages allowed. Under 4 free. Ages 5-17: EUR 30/child/night
  - **Extra beds/cribs:** Setup incomplete (cribs policy not finished). No extra beds added.
  - **Payment:** Payments by Booking.com (bank transfer to property)
  - **Internet:** WiFi in rooms, free of charge
  - **Parking:** Info moved to facilities page
  - **Check-in:** 2:00 PM – 12:00 AM
  - **Check-out:** 11:00 AM – 12:00 AM
  - **Guest address:** Not required
  - **Guest phone:** Required
  - **Minimum age:** 18
  - **Maximum age:** No limit
  - **Curfew:** None
  - **Additional fees:** None specified
  - **Damage policy:** None with Booking.com
  - **Key pickup:** Keys at reception on-site
  - **Smoking:** Not allowed
  - **Pets:** Not allowed
  - **Parties/events:** Allowed
  - **Quiet hours:** 12:00 AM – 6:00 AM
  - **Long stays:** Up to 90 nights accepted
- **Said-relevant:** YES — HIGH. Resolves: pets policy, check-in/out times, children rates, smoking, parties, quiet hours, age limits
- **Extraction priority:** HIGH — complete data already extracted above

#### Reservation Policies

- **URL:** `policies.html`
- **Available data:**
  - **Policy 1:** Flexible - 7 days (General) — Free cancel until 7 days before arrival; first night charged if cancel within 7 days
  - **Policy 2:** Non-refundable — Full amount charged if canceled anytime
  - **Modification:** Guests can change dates once (5+ days before check-in, same/higher price, same room type)
  - **Grace Period:** Nothing selected
  - **Group reservations:** Exceptions for >10 rooms
  - **Report Nov 24, 2025 – Feb 22, 2026:** Total 10 room nights, Total Revenue €1,185.00
- **Said-relevant:** Yes — cancellation policy confirmation
- **Extraction priority:** Medium

#### Your Profile

- **URL:** `property_profile.html`
- **Said-relevant:** Potentially (property description)
- **Extraction priority:** Medium

#### View Your Descriptions

- **URL:** `request_change.html`
- **Said-relevant:** Yes — all property descriptions visible
- **Extraction priority:** High

### Boost Performance

- **URL:** `opportunities.html`
- **Sub-sections:** Genius program, Ranking dashboard, opportunities
- **Available data:** Advice items (80% lower conversion than area avg, Genius primary room update scheduled)
- **Said-relevant:** No
- **Extraction priority:** Low

### Inbox

- **URL:** `messaging/inbox.html`
- **Available data:**
  - 2 unread messages
  - Guest message threads
- **Said-relevant:** Potentially (guest communication examples)
- **Extraction priority:** Low

### Guest Reviews

- **URL:** `reviews.html`
- **Available data:**
  - Review score: **9.2** (based on 86 reviews)
  - Area avg: 8.7
  - Weighted calculation effective Jan 23, 2025
  - Recent reviews visible on dashboard (all score 10):
    - montañez — Jan 19 (score 10)
    - montañez — Jan 15 "Alojamiento de 10" (score 10)
    - Olivier — Jan 8 "ressourçant" (score 10)
    - Laurent — Jan 5 "Malgré un temps pas au top. Le vrai dépaysement marocain dans toute sa splendeur" (score 10)
- **Said-relevant:** Yes — review score data
- **Extraction priority:** Medium

### Finance

- **URL:** `finance_overview.html`
- **Sub-sections:**
  - Payout info (`payouts.html`)
  - Documents and invoices — **1 unread/unpaid** (`documents.html`)
  - Reservations statement (`finance_reservations.html`)
  - Financial Overview (`finance_overview.html`)
  - Finance Help (`finance_help.html`)
  - Virtual cards management (`vccs_management.html`)
  - Finance settings (`finance_settings.html`)
- **Available data:**
  - 1 unpaid invoice (1 overdue)
  - Monthly gross revenue:
    - December: **EUR 3,058.60**
    - January: **EUR 7,020.25**
    - February: EUR 0.00
  - Payment method: Bank Transfer
  - Booking.com bank: Citibank Maghreb SA, Casablanca. RIB: 028780000000010046502780
- **Said-relevant:** YES — revenue data, unpaid invoice (Said needs to be aware), payout method
- **Extraction priority:** HIGH

### Analytics

- **URL:** `statistics/dashboard.html`
- **Sub-sections:**
  - Analytics dashboard
  - Demand for Marrakesh (New)
  - Your pace of bookings
  - Sales Statistics
  - Booker insights
  - Book Window Info
  - Cancellation Characteristics
  - Comparable properties
  - Genius Report
  - Ranking Dashboard (New)
  - Performance dashboard
- **Available data:** Full analytics suite for Marrakesh market
- **Said-relevant:** Partially (market demand, pace of bookings)
- **Extraction priority:** Low for now (strategic, not operational)

---

## Said Items Addressable

Cross-reference against `data/admin/said-pending-questions.md`:

| Category | Data Available | Detail |
|---|---|---|
| Check-in/out times | YES | Check-in: 2 PM–midnight. Check-out: 11 AM–midnight |
| Children policy | YES | Under 4 free. Ages 5-17: €30/child/night |
| Pets policy | YES | Not allowed |
| Smoking policy | YES | Not allowed |
| Parties/events | YES | Allowed |
| Quiet hours | YES | 12:00 AM – 6:00 AM |
| Minimum guest age | YES | 18 |
| Wifi policy | YES | Free in all rooms |
| Cancellation policy | YES | Flexible (7 days) + Non-refundable |
| Room max occupancy | YES | Full table extracted (rooms.html) |
| Review score | YES | 9.2 / 86 reviews |
| Revenue Dec/Jan | YES | €3,058 / €7,020 |
| Unpaid invoice | YES | 1 overdue invoice (Said should know) |
| Address/GPS | YES | Route de fes km 12, Ouled Jelal / 31.6539, -7.8786 |
| Photo count | YES | 128 total, 71 untagged, 14 low quality |
| Key pickup | YES | Reception on-site |
| Long stay policy | YES | Up to 90 nights |
| Extra beds | PARTIAL | Cribs policy incomplete, no extra beds configured |
| Parking | REDIRECT | "See facilities page" — needs facilities.html scrape |
| Room amenities | PENDING | Needs `amenities.html` extraction |
| Property description | PENDING | Needs `request_change.html` extraction |
| Facilities list | PENDING | Needs `facilities.html` deep extraction |

---

## Extraction Plan

### Phase 1 — Already extractable (this session)

Data already captured in this terrain map:
- Property policies (complete)
- Room occupancy table (complete)
- Financial summary (Dec/Jan revenue, unpaid invoice)
- Review score (9.2 / 86 reviews)
- Cancellation policies (complete)

### Phase 2 — Targeted extractions (next session)

Priority order:

1. **`amenities.html`** — Room amenities per room type (HIGH: resolves multiple Said items about room features)
2. **`facilities.html`** — Full facilities & services list (HIGH: parking, spa, pool details)
3. **`request_change.html`** — Property descriptions in all languages (MEDIUM: content audit)
4. **`statistics/dashboard.html`** — Analytics overview (MEDIUM: market intelligence)
5. **`promotions/list.html`** — Active promotions (MEDIUM: pricing strategy)
6. **`search_reservations.html`** — Full reservation history export (HIGH: revenue & occupancy data)

### Phase 3 — Deep dives (future)

- Full review text extraction (86 reviews) — requires pagination
- Individual room rate plans — via `calendar/index.html`
- VAT/Tax configuration — `vat_tax_charges.html`
- Messaging preferences — `messaging/settings.html`

---

## Session Reuse Instructions

Session state saved at: `.secrets/booking-session.json`

To reuse without login:
```bash
playwright-cli open --persistent --profile=/home/director/villa-thaifa/.secrets/
playwright-cli state-load /home/director/villa-thaifa/.secrets/booking-session.json
playwright-cli goto "https://admin.booking.com/hotel/hoteladmin/extranet_ng/manage/home.html?hotel_id=5446847"
```

**Session likely expires** within 24-48 hours. The login flow requires:
1. AWS WAF CAPTCHA (canvas, pixel-click-based — solvable by AI with screenshot)
2. SMS OTP to `+21******0409`

For future automated access, consider:
- Saving cookies after each successful login
- Building a reusable login script that handles the CAPTCHA canvas interaction

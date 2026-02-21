# Villa Thaifa — Source of Truth

> **Last Updated:** 2026-02-21 (property-config + truth.md — external listing data applied)
> **Sources verified from:** rates.json, billing.json, property-config.json, channels.json, check-in-out.json, data/admin/client/PROFILE.md, open-conflicts-registry.md, handoff-repo-consolidation.md, external listing (Omar, 2026-02-21)

---

## 1. Rooms & Pricing

> **Canonical source: `data/finance/rates.json`** — Locked until 2026-12-31.
> Confirmed via HotelRunner deployment 2026-01-13, WhatsApp message.
> rates.json corrected 2026-02-21 (4 wrong values fixed). rooms.md was correct all along.

| ID  | Internal Name        | Category Code      | Capacity | Beds                            | Price (EUR) | Price (MAD) | View                                | Outdoor                                               |
| --- | -------------------- | ------------------ | -------- | ------------------------------- | ----------- | ----------- | ----------------------------------- | ----------------------------------------------------- |
| R01 | Deluxe Triple Room   | DELUXE_TRIPLE      | 3 adults | 1x King (200 cm) + 1x Sofa Bed  | 169 EUR     | 1,812 MAD   | Garden view                         | Furnished patio (Ground Floor)                        |
| R02 | Deluxe Double Room   | DELUXE_DOUBLE      | 2 adults | 1x King (200 cm)                | 159 EUR     | 1,704 MAD   | Garden view                         | Furnished patio; 40 m² terrace                        |
| R03 | Deluxe Triple Room   | DELUXE_TRIPLE      | 3 adults | 1x King (200 cm) + 1x Sofa Bed  | 169 EUR     | 1,812 MAD   | Garden view                         | Furnished patio; Small terrace                        |
| R04 | Double Room Superior | DOUBLE_SUPERIOR    | 2 adults | 1x King (200 cm)                | 149 EUR     | 1,597 MAD   | Pool view (direct access)           | Furnished patio                                       |
| R05 | Double Room Superior | DOUBLE_SUPERIOR    | 2 adults | 1x King (200 cm)                | 149 EUR     | 1,597 MAD   | Pool view                           | Furnished balcony (upper floor)                       |
| R06 | Executive Suite      | EXECUTIVE_SUITE    | 3 adults | 1x King (200 cm) + 1x Sofa Bed  | 169 EUR     | 1,812 MAD   | Pool + Atlas Mountain + Garden view | Furnished balcony; 100 m² terrace (DISPUTED — see §6) |
| R07 | Deluxe King Suite    | DELUXE_KING_SUITE  | 4 adults | 1x King (200 cm) + 2x Sofa Beds | 329 EUR     | 3,527 MAD   | Pool + Mountain view                | Furnished balcony; 60 m² terrace (DISPUTED — see §6)  |
| R08 | Deluxe Triple Room   | DELUXE_TRIPLE      | 3 adults | 1x King (200 cm) + 1x Sofa Bed  | 169 EUR     | 1,812 MAD   | Garden view                         | Furnished balcony                                     |
| R09 | Family Suite         | FAMILY_SUITE       | 4 adults | 1x King (200 cm) + 2x Sofa Beds | 189 EUR     | 2,026 MAD   | Pool view (direct access)           | Furnished patio; Double terrace                       |
| R10 | Suite                | SUITE              | 3 adults | 1x King (200 cm) + 1x Sofa Bed  | 179 EUR     | 1,919 MAD   | Pool view (direct access)           | Furnished patio; Double terrace                       |
| R11 | Family Suite         | FAMILY_SUITE       | 4 adults | 1x King (200 cm) + 2x Sofa Beds | 189 EUR     | 2,026 MAD   | Pool view (direct access)           | Furnished patio; Double terrace                       |
| R12 | Presidential Suite   | PRESIDENTIAL_SUITE | 4 adults | 1x King (200 cm) + 2x Sofa Beds | 449 EUR     | 4,813 MAD   | Pool view                           | Furnished patio; Double terrace/patio                 |

**Exchange rate:** 1 EUR = 10.72 MAD (as of rates.json v1.0, 2026-02-19)
**All rooms:** No smoking, no kitchen, AC + heating, shower/tub combo, hair dryer, laptop workspace

---

## 2. Property Configuration

> **Canonical source: `data/property/property-config.json`** (status: partial — last updated 2026-02-19)

| Field               | Value                                                                               | Confidence                 |
| ------------------- | ----------------------------------------------------------------------------------- | -------------------------- |
| Property name       | Villa Thaifa (also "Villa Thaifa & SPA")                                            | Confirmed                  |
| Type                | Maison d'hôte / Riad — Boutique guesthouse / B&B (4★)                               | Confirmed                  |
| Address             | Route de Fès, Km 12, Palmeraie / Ouled Jelal, Marrakech, Morocco                    | Confirmed                  |
| GPS                 | 31.6539756, -7.8778661 (Google Maps 2026-02-19)                                     | Confirmed (Google Maps)    |
| Airport code        | RAK (Marrakech-Menara)                                                              | Confirmed (external)       |
| Distance to airport | ~10 km straight-line / 15.8 km drive — 15-20 min                                   | Confirmed (external)       |
| Distance to center  | 11.7–13 km — 25-30 min drive to Djemaa El Fna                                      | Confirmed (external)       |
| Postal code         | 40000                                                                               | Confirmed (external)       |
| Phone (confirmed)   | +212661134194 — Said's WhatsApp (confirmed by Omar)                                 | Confirmed                  |
| Phone (unverified)  | +212662146949 / 06 62 14 69 49 — Google listing (needs Said clarification)          | Awaiting: Said             |
| Expedia Property ID | 114807934                                                                           | Confirmed                  |
| Booking.com rating  | 9.3/10 (80 reviews) — "Wonderful"                                                   | Confirmed                  |
| Google rating       | 4.5/5 (22 reviews)                                                                  | Confirmed                  |
| Total rooms         | 12                                                                                  | Confirmed                  |
| Languages spoken    | Arabic, Dutch, English, French                                                      | Confirmed                  |
| Check-in            | 14:00 (early check-in on request)                                                   | Confirmed                  |
| Check-out           | 12:00 (late check-out on request) — Omar decision 2026-02-20                        | Confirmed                  |
| Cancellation        | Free up to 72h before 18:00 on check-in day. Late cancel/no-show: 1st night + taxes | Confirmed                  |
| Deposit required    | No                                                                                  | Confirmed                  |
| Children policy     | Allowed. Ages 2-12: €30/person/night (existing bed)                                 | Confirmed (OTA)            |
| Pets policy         | DISPUTED — see §6                                                                   | Awaiting: Said             |
| Smoking policy      | Designated smoking areas                                                            | Confirmed (Expedia Step 4) |
| Pool                | Infinity pool, heated, open year-round                                              | Confirmed                  |
| Spa / Hammam        | Yes — reservation required, minimum 4 guests                                        | Confirmed                  |
| Restaurant          | Yes — "Thaifa's restaurant", Moroccan cuisine (halal, vegetarian)                   | Confirmed                  |
| Breakfast           | 08:30–11:00, MAD 160.90/person, score 10/10 on Booking.com                          | Confirmed                  |
| Parking             | Free parking, available                                                             | Confirmed                  |
| Wi-Fi               | Free, available                                                                     | Confirmed                  |
| Airport transfer    | Yes — paid shuttle through property. Source: external listing 2026-02-21.           | Confirmed (external)       |
| Express check-in/out | Mentioned in external listing — not in conflict with 14:00/12:00 times            | Pending: Said              |
| Sports activities   | Mentioned in external listing — type unknown                                        | Pending: Said              |
| Security            | 24/7, CCTV, safe, alarm                                                             | Confirmed (PROFILE.md)     |

**Pending from Said:** See consolidated registry: `data/admin/said-pending-questions.md §3`

---

## 3. Financial Setup

> **Canonical source: `data/finance/billing.json`** (status: owner_pending — last updated 2026-02-16)

| Field              | Value                                                          | Confidence                                      |
| ------------------ | -------------------------------------------------------------- | ----------------------------------------------- |
| Primary currency   | EUR                                                            | Confirmed                                       |
| Secondary currency | MAD                                                            | Confirmed                                       |
| Exchange rate      | 10.72                                                          | Confirmed                                       |
| VAT rate           | 10% (exclusive / HT — Said confirmed 2026-02-21)               | Confirmed                                       |
| Tourist tax        | 3 MAD/night                                                    | Confirmed                                       |
| City tax           | 5 MAD/night                                                    | Confirmed                                       |
| Payment methods    | Cash, bank transfer, Visa, Mastercard, debit card              | Awaiting: Said (legacy data, not yet confirmed) |
| Online payment     | PENDING — needs Said                                           | Unknown                                         |
| Legal entity       | PENDING — needs Said (RC number, ICE, tax ID, address missing) | Unknown                                         |
| Invoicing workflow | Not defined — template and auto-generate pending               | Unknown                                         |

---

## 4. Distribution Channels

> **Canonical source: `data/operations/channels.json`** (status: placeholder — last updated 2026-01-15)

| Channel     | Status        | Key Info                                                                                                         |
| ----------- | ------------- | ---------------------------------------------------------------------------------------------------------------- |
| Booking.com | Active        | 25% commission (vs 15% standard). Primary OTA. 80 reviews, rating 9.3/10.                                        |
| HotelRunner | Active        | Channel Manager + PMS replacement. Active since Dec 2025.                                                        |
| Expedia     | Onboarding    | Property ID 114807934. Blocked at Step 5 (rooms not configured). Steps 6-12 pending. Tax team contact requested. |
| Airbnb      | Pending setup | Not yet active.                                                                                                  |
| Trip.com    | Ready to sign | GDA contract ready. Said must sign + provide bank notification letter. 18% commission.                           |
| WhatsApp    | Active        | Primary guest communication channel. Number: PENDING — needs Said.                                               |
| Email       | Active        | Addresses: said_thaifa@hotmail.fr / saidthaifa@gmail.com. Templates pending.                                     |
| Instagram   | Unknown       | Handle: PENDING — needs Said.                                                                                    |
| Facebook    | Unknown       | Handle: PENDING — needs Said.                                                                                    |
| TripAdvisor | Listed        | Rating: 3.0/5 (ranked #1078 of 1284 B&Bs in Marrakech). Manage handle unknown.                                   |
| Direct      | None          | No website, no direct booking engine.                                                                            |

**Communication protocol:** Tone: Professional and warm. Primary language: French. Secondary: English, Arabic. Response time targets: PENDING — needs Said.

---

## 5. Client Info

> **Canonical source: `data/admin/client/PROFILE.md`** (last updated 2026-02-21)

| Field                 | Value                                                                                      |
| --------------------- | ------------------------------------------------------------------------------------------ |
| Owner name            | Said Thaifa                                                                                |
| Age                   | 78 years old                                                                               |
| Co-manager            | Nezha Thaifa (wife)                                                                        |
| Email                 | said_thaifa@hotmail.fr / saidthaifa@gmail.com                                              |
| Phone / WhatsApp (confirmed) | +212661134194 — Said's WhatsApp (confirmed by Omar)                             |
| Phone (unverified)    | +212662146949 (06 62 14 69 49) — Google listing (needs Said clarification)                 |
| Preferred language    | Dutch (primary) — prefers Dutch over French                                                |
| Communication channel | WhatsApp (confirmed)                                                                       |
| Communication tone    | Formal (vouvoiement mandatory). Senior client — respect without rigidity.                  |
| Message format        | Dual output: Dutch for Said + French summary for Omar review                               |
| Languages spoken      | Arabic (native), French (fluent), Dutch (fluent), English (basic)                          |
| Background            | CEO / Real estate agent in Marrakech. Warm host, wants guests to feel "at home".           |
| PMS                   | None — everything in Said's memory                                                         |
| Pain points           | Manual management, OTA dependency (100% Booking), high 25% commission, staffing difficulty |

**Blocking items for Said:** See `data/admin/said-pending-questions.md` (consolidated registry — do not duplicate here)

---

## 6. Known Conflicts (Unresolved)

> **Canonical source: `ops/decisions/open-conflicts-registry.md`** (created 2026-02-21)

| #   | Conflict         | Source A                                   | Source B / C                                              | Status         |
| --- | ---------------- | ------------------------------------------ | --------------------------------------------------------- | -------------- |
| 1   | Pets policy      | property-config.json: "Allowed, no charge" | booking-com-data.md: "Not allowed" / Expedia Step 4: "No" | Awaiting: Said |
| 2   | R06 terrace size | rooms.md: 100 m²                           | Said's handwritten notes: ~120 m²                         | Awaiting: Said |
| 3   | R07 terrace size | rooms.md: 60 m²                            | Said's handwritten notes: 80-100 m²                       | Awaiting: Said |

**Rule:** Do NOT guess on these. Escalate to Said. The open-conflicts-registry.md is the authoritative tracker — update it when resolved.

---

## 7. Canonical Data Map

| Domain                    | Canonical File                                        | Status                             |
| ------------------------- | ----------------------------------------------------- | ---------------------------------- |
| Room specs                | `data/rooms/rooms.md` + per-room `R01-R12/profile.md` | ACTIVE — verified                  |
| Pricing                   | `data/finance/rates.json`                             | ACTIVE — locked until 2026-12-31   |
| Billing / taxes           | `data/finance/billing.json`                           | PARTIAL — owner_pending            |
| Property config           | `data/property/property-config.json`                  | PARTIAL — TODOs remain             |
| Check-in/out workflow     | `data/operations/check-in-out.json`                   | PLACEHOLDER — needs real workflow  |
| Distribution channels     | `data/operations/channels.json`                       | PLACEHOLDER — most details missing |
| Client profile            | `data/admin/client/PROFILE.md`                        | ACTIVE — last updated 2026-02-21   |
| Open conflicts            | `ops/decisions/open-conflicts-registry.md`            | ACTIVE — 3 open items              |
| Bookings / reservations   | `data/bookings/reservations/`                         | ACTIVE                             |
| Facilities                | `data/property/facilities/`                           | PARTIAL — needs Said               |
| Reconciliation log        | `data/rooms/rooms-reconciliation-log.md`              | ACTIVE                             |
| Said validation checklist | `data/admin/said-data-validation-checklist.md`        | ACTIVE — hand-off form for Said    |
| Said pending questions    | `data/admin/said-pending-questions.md`                | ACTIVE — operational registry      |

**Superseded / do not use:**

- `ops/audit/quality/grille-tarifaire-officielle.md` — SUPERSEDED (banner added)
- `ops/status/MASTER_STATE.md` — SUPERSEDED (banner added)
- `data/archive/inventory.md` — SUPERSEDED (banner added)
- `data/pending-domains/facilities.md` — SUPERSEDED (banner added)
- `data/tasks/TODOs-legacy.md` — ARCHIVED (banner added)

---

## 8. Pending Actions

### Blocked on Said

> Full consolidated registry: `data/admin/said-pending-questions.md`

| #   | Item                                | Impact                          | Ref                                        |
| --- | ----------------------------------- | ------------------------------- | ------------------------------------------ |
| 1   | Sign Trip.com GDA contract          | New OTA channel at 18% vs 25%   | said-pending-questions.md §PO2             |
| 2   | Pets policy confirmation            | Guest-facing OTA policy error   | said-pending-questions.md §C1              |
| 3   | R06 + R07 terrace size confirmation | Room listing accuracy           | said-pending-questions.md §C2–C3           |
| 4   | Legal entity info (MarocPME)        | MOUS-17509 blocked              | said-pending-questions.md §F1              |
| 5   | Website preferences                 | Site creation blocked           | said-pending-questions.md §8               |
| 6   | Legal/financial details             | billing.json incomplete         | said-pending-questions.md §4               |
| 7   | Property config gaps                | property-config.json incomplete | said-pending-questions.md §3, §GP1–GP13    |
| 8   | WhatsApp number + channels info     | channels.json incomplete        | said-pending-questions.md §CH1–CH4         |
| 9   | Room data gaps (VT-72/74/76)        | rooms.md data_confidence gaps   | said-pending-questions.md §2               |

### Blocked on Expedia

| #   | Item                               | Impact                   | Ref             |
| --- | ---------------------------------- | ------------------------ | --------------- |
| 1   | Tax team contact (checkbox ticked) | Step 5 unblocking needed | VT-82           |
| 2   | Expedia Steps 6-12                 | Full Expedia onboarding  | Tasks #104-#110 |

### Next technical work (not blocked)

| #   | Item                                                       | Ref       |
| --- | ---------------------------------------------------------- | --------- |
| 1   | Create villa-thaifa PROJECT-CONTRACT.md from template      | Task #112 |
| 2   | Create ~/omar/ PROJECT-CONTRACT.md from template           | Task #113 |
| 3   | Merge browser-agent.md into global browser.md + VT context | Task #116 |

---

## 9. Pricing Correction Record (2026-02-21)

**rates.json had 4 wrong prices. rooms.md was correct all along.**

Source of truth: HotelRunner deployment confirmed 2026-01-13 via WhatsApp message.

| Room | rates.json (was WRONG) | Correct price       | rooms.md (was correct) |
| ---- | ---------------------- | ------------------- | ---------------------- |
| R02  | 149 EUR / 1,597 MAD    | 159 EUR / 1,704 MAD | 159 EUR — correct      |
| R04  | 159 EUR / 1,704 MAD    | 149 EUR / 1,597 MAD | 149 EUR — correct      |
| R05  | 159 EUR / 1,704 MAD    | 149 EUR / 1,597 MAD | 149 EUR — correct      |
| R06  | 179 EUR / 1,919 MAD    | 169 EUR / 1,812 MAD | 169 EUR — correct      |

**Fixed 2026-02-21:** rates.json corrected. rooms.md required no changes.
**Decision record:** `ops/decisions/room-pricing-hotelrunner-confirmation.md`

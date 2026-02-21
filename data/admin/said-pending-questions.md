# Said Pending Questions — Villa Thaifa

> **Purpose**: Single consolidated registry of ALL items awaiting Said Thaifa's confirmation.
> **DRY enforcement**: Source files reference this file. Do not maintain "Awaiting: Said" lists elsewhere.
> **Last Updated**: 2026-02-21
> **Status tracking**: Linear label "Awaiting: Said" applied to all corresponding issues.
>
> Related document: `data/admin/said-data-validation-checklist.md` — the physical walk-through form for Said to fill in.
> This file is the operational registry (for agents/Omar). The checklist is the hand-off document (for Said).

---

## Table of Contents

- [Said Pending Questions — Villa Thaifa](#said-pending-questions--villa-thaifa)
  - [Table of Contents](#table-of-contents)
  - [Priority Legend](#priority-legend)
  - [1. Critical Conflicts (Resolve First)](#1-critical-conflicts-resolve-first)
  - [2. Room Details](#2-room-details)
    - [2.1 Room Sizes](#21-room-sizes)
    - [2.2 Floor Assignment](#22-floor-assignment)
    - [2.3 Other Room-Level Questions](#23-other-room-level-questions)
  - [3. Property Facilities](#3-property-facilities)
    - [3.1 Spa / Hammam](#31-spa--hammam)
    - [3.2 Pool](#32-pool)
    - [3.3 Garden](#33-garden)
    - [3.4 Hall / Reception](#34-hall--reception)
    - [3.5 General Property](#35-general-property)
  - [4. Financial \& Legal](#4-financial--legal)
  - [5. Policies \& Operations](#5-policies--operations)
  - [6. Channel \& Platform](#6-channel--platform)
  - [7. Contact \& Communication](#7-contact--communication)
  - [8. Website \& Brand](#8-website--brand)
  - [9. Events \& Privatization](#9-events--privatization)
  - [Resolution Log](#resolution-log)

---

## Priority Legend

| Symbol | Meaning                                      |
| ------ | -------------------------------------------- |
| P0     | Blocking active operations or OTA onboarding |
| P1     | Needed for accurate OTA listings             |
| P2     | Nice to have / secondary accuracy            |

---

## 1. Critical Conflicts (Resolve First)

These have conflicting data across sources. Do NOT guess — only Said can resolve.

| #   | Question                                  | Source A                                           | Source B                                                   | Linear | Priority |
| --- | ----------------------------------------- | -------------------------------------------------- | ---------------------------------------------------------- | ------ | -------- |
| C1  | **Pets policy**: Allowed or not?          | `property-config.json`: "Allowed, no extra charge" | `booking-com-data.md`: "Not allowed"; Expedia Step 4: "No" | VT-74  | P0       |
| C2  | **R06 terrace size**: 100 m² or ~120 m²?  | `rooms.md`: 100 m²                                 | Said's handwritten notes: ~120 m²                          | VT-74  | P1       |
| C3  | **R07 terrace size**: 60 m² or 80–100 m²? | `rooms.md`: 60 m²                                  | Said's handwritten notes: 80–100 m²                        | VT-74  | P1       |

Source: `ops/decisions/open-conflicts-registry.md`, `ops/status/truth.md §6`

---

## 2. Room Details

Items with `data_confidence: owner_pending` in room profiles. All rooms R01–R12 (except R04 and R12 for some fields) need physical confirmation.

### 2.1 Room Sizes

| Room | Current Value | Conflict?                                  | Source File                 | Linear | Priority |
| ---- | ------------- | ------------------------------------------ | --------------------------- | ------ | -------- |
| R01  | 44 m²         | Yes — 24 m² also exists (Booking.com scan) | `data/rooms/R01/profile.md` | VT-72  | P1       |
| R02  | 41 m²         | Not confirmed                              | `data/rooms/R02/profile.md` | VT-72  | P1       |
| R03  | 44 m²         | Assumed from similar rooms                 | `data/rooms/R03/profile.md` | VT-72  | P1       |
| R04  | 24 m²         | From Booking.com screenshot                | `data/rooms/R04/profile.md` | VT-72  | P1       |
| R05  | 24 m²         | Assumed from R04                           | `data/rooms/R05/profile.md` | VT-72  | P1       |
| R06  | 40 m²         | Conflict: 44 m² in OTA short description   | `data/rooms/R06/profile.md` | VT-72  | P1       |
| R07  | 61 m²         | Not confirmed                              | `data/rooms/R07/profile.md` | VT-72  | P1       |
| R08  | 44 m²         | Assumed from R01/R03                       | `data/rooms/R08/profile.md` | VT-72  | P1       |
| R09  | 41 m²         | Not confirmed                              | `data/rooms/R09/profile.md` | VT-72  | P1       |
| R10  | 41 m²         | Assumed from similar suites                | `data/rooms/R10/profile.md` | VT-72  | P1       |
| R11  | 41 m²         | Assumed from R09                           | `data/rooms/R11/profile.md` | VT-72  | P1       |
| R12  | 82 m²         | **Verified** — no action needed            | `data/rooms/R12/profile.md` | —      | —        |

### 2.2 Floor Assignment

| Room | Current Value          | Issue                    | Source File           | Linear | Priority |
| ---- | ---------------------- | ------------------------ | --------------------- | ------ | -------- |
| R04  | Ground Floor (implied) | Not explicitly confirmed | `data/rooms/rooms.md` | VT-76  | P1       |
| R10  | Ground Floor (implied) | Not explicitly confirmed | `data/rooms/rooms.md` | VT-76  | P1       |

### 2.3 Other Room-Level Questions

| #   | Question                                                            | Room | Current Value                                     | Source File                                | Linear | Priority |
| --- | ------------------------------------------------------------------- | ---- | ------------------------------------------------- | ------------------------------------------ | ------ | -------- |
| RD1 | R07: How many sofa beds? (1 or 2?)                                  | R07  | 2 sofa beds (unconfirmed — "Check count" flagged) | `data/rooms/R07/profile.md`                | VT-72  | P1       |
| RD2 | R07: Features — fireplace and separate sitting/dining area correct? | R07  | Yes (from OTA data)                               | `data/rooms/R07/profile.md`                | VT-72  | P2       |
| RD3 | R06: Terrace size — see Conflict C2 above                           | R06  | 100 m² (disputed)                                 | `ops/decisions/open-conflicts-registry.md` | VT-74  | P1       |
| RD4 | R07: Terrace size — see Conflict C3 above                           | R07  | 60 m² (disputed)                                  | `ops/decisions/open-conflicts-registry.md` | VT-74  | P1       |

Source: `data/admin/said-data-validation-checklist.md §Rooms`, `data/rooms/rooms.md`

---

## 3. Property Facilities

### 3.1 Spa / Hammam

| #   | Question                                                  | Current Value                                      | Source File                              | Linear | Priority |
| --- | --------------------------------------------------------- | -------------------------------------------------- | ---------------------------------------- | ------ | -------- |
| S1  | Hammam capacity (persons)                                 | `owner_pending`                                    | `data/property/facilities/spa-hammam.md` | VT-71  | P1       |
| S2  | Hammam operating hours                                    | `owner_pending`                                    | `data/property/facilities/spa-hammam.md` | VT-71  | P1       |
| S3  | Hammam price per person (surcharge confirmed — how much?) | "On request" for events                            | `data/property/facilities/spa-hammam.md` | VT-71  | P1       |
| S4  | Number of massage tables                                  | `owner_pending`                                    | `data/property/facilities/spa-hammam.md` | VT-71  | P1       |
| S5  | Types of massage treatments offered                       | `owner_pending`                                    | `data/property/facilities/spa-hammam.md` | VT-71  | P1       |
| S6  | Massage price per session                                 | `owner_pending`                                    | `data/property/facilities/spa-hammam.md` | VT-71  | P1       |
| S7  | Spa booking policy: "minimum 4 guests" — still correct?   | 4 persons minimum (Said, via chambre-et-vue notes) | `property-config.json`                   | VT-71  | P2       |

### 3.2 Pool

| #   | Question                              | Current Value                                                  | Source File                        | Linear | Priority |
| --- | ------------------------------------- | -------------------------------------------------------------- | ---------------------------------- | ------ | -------- |
| P1  | Pool dimensions (length × width)      | `owner_pending` (size: "TODO")                                 | `data/property/facilities/pool.md` | VT-71  | P1       |
| P2  | Pool depth (shallow and deep end)     | `owner_pending`                                                | `data/property/facilities/pool.md` | VT-71  | P2       |
| P3  | Pool operating hours                  | `owner_pending`                                                | `data/property/facilities/pool.md` | VT-71  | P2       |
| P4  | Pool bar: exists? What does it serve? | `owner_pending`                                                | `data/property/facilities/pool.md` | VT-71  | P2       |
| P5  | Number of sunbeds and parasols        | Sun loungers/umbrellas confirmed (Booking.com) — count unknown | `data/property/facilities/pool.md` | VT-71  | P2       |

### 3.3 Garden

| #   | Question               | Current Value   | Source File                          | Linear | Priority |
| --- | ---------------------- | --------------- | ------------------------------------ | ------ | -------- |
| G1  | Garden surface area    | `owner_pending` | `data/property/facilities/garden.md` | VT-71  | P2       |
| G2  | Number of palm trees   | `owner_pending` | `data/property/facilities/garden.md` | VT-71  | P2       |
| G3  | Number of orange trees | `owner_pending` | `data/property/facilities/garden.md` | VT-71  | P2       |

### 3.4 Hall / Reception

| #   | Question                                                        | Current Value   | Source File                                  | Linear | Priority |
| --- | --------------------------------------------------------------- | --------------- | -------------------------------------------- | ------ | -------- |
| H1  | Seated capacity for dining (30 guests feasible?)                | `owner_pending` | `data/property/facilities/hall-reception.md` | VT-71  | P1       |
| H2  | Sound system available?                                         | `owner_pending` | `data/property/facilities/hall-reception.md` | VT-71  | P2       |
| H3  | Event furniture (tables, chairs) — available or must be rented? | `owner_pending` | `data/property/facilities/hall-reception.md` | VT-71  | P2       |
| H4  | Music hours limit for events                                    | Not documented  | `data/property/facilities/hall-reception.md` | VT-71  | P2       |

### 3.5 General Property

| #    | Question                                                           | Current Value                                               | Source File                          | Linear | Priority |
| ---- | ------------------------------------------------------------------ | ----------------------------------------------------------- | ------------------------------------ | ------ | -------- |
| GP1  | ~~Total beds across all 12 rooms~~                                 | **RESOLVED: 25** (calculated from rooms.md)                 | `data/property/property-config.json` | VT-77  | —        |
| GP2  | ~~Max guests total~~                                               | **RESOLVED: 37** (calculated from rooms.md)                 | `data/property/property-config.json` | VT-77  | —        |
| GP3  | WiFi technology type (fiber / ADSL / 4G)                           | Free Wi-Fi confirmed — type unknown                         | `data/property/property-config.json` | VT-77  | P2       |
| GP4  | Express check-in/check-out: how does it work?                      | `pending_confirmation` (listed externally)                  | `data/property/property-config.json` | VT-77  | P2       |
| GP5  | Sports activities: what specifically is offered?                   | `pending_confirmation` (listed externally)                  | `data/property/property-config.json` | VT-77  | P2       |
| GP6  | Laundry service available? Pricing?                                | "TODO"                                                      | `data/property/property-config.json` | VT-77  | P2       |
| GP7  | Room service available? Hours and menu scope?                      | "TODO"                                                      | `data/property/property-config.json` | VT-77  | P2       |
| GP8  | Concierge service available?                                       | "TODO"                                                      | `data/property/property-config.json` | VT-77  | P2       |
| GP9  | Tours / excursion service available?                               | "TODO"                                                      | `data/property/property-config.json` | VT-77  | P2       |
| GP10 | Heating available in rooms? (listed in amenities as "TODO")        | "TODO"                                                      | `data/property/property-config.json` | VT-77  | P2       |
| GP11 | In-room safe available?                                            | "TODO"                                                      | `data/property/property-config.json` | VT-77  | P2       |
| GP12 | Mini-bar in rooms?                                                 | "TODO"                                                      | `data/property/property-config.json` | VT-77  | P2       |
| GP13 | GPS coordinates correct? (31.6539756, -7.8778661 from Google Maps) | Confirmed via Google Maps — Said confirmation still pending | `data/property/property-config.json` | VT-77  | P2       |

Source: `data/property/property-config.json §todo[]`, `data/admin/said-data-validation-checklist.md §Property-Wide`

---

## 4. Financial & Legal

| #   | Question                                                                                               | Current Value           | Source File                 | Linear | Priority |
| --- | ------------------------------------------------------------------------------------------------------ | ----------------------- | --------------------------- | ------ | -------- |
| F1  | **Legal entity info** (for MarocPME MOUS-17509) — legal form, RC number, ICE number, tax ID, address   | All null                | `data/finance/billing.json` | VT-79  | P0       |
| F2  | **Payment methods confirmed?** (legacy data suggests cash, bank transfer, Visa/Mastercard, debit card) | Unconfirmed legacy data | `data/finance/billing.json` | —      | P1       |
| F3  | **Online payment** accepted? (card via OTA vs direct payment)                                          | null / unknown          | `data/finance/billing.json` | —      | P1       |
| F4  | Tax registration numbers (RC, ICE, tax ID)                                                             | All null                | `data/finance/billing.json` | VT-79  | P0       |
| F5  | Invoicing workflow — template and process?                                                             | Not defined             | `data/finance/billing.json` | —      | P2       |

Source: `ops/status/truth.md §3`, `data/finance/billing.json`, `data/admin/client/PROFILE.md §13.3`

---

## 5. Policies & Operations

| #   | Question                                                                                            | Current Value                                      | Source File                                      | Linear | Priority |
| --- | --------------------------------------------------------------------------------------------------- | -------------------------------------------------- | ------------------------------------------------ | ------ | -------- |
| PO1 | **Pets policy** — see Conflict C1 above                                                             | Disputed                                           | `ops/decisions/open-conflicts-registry.md`       | VT-74  | P0       |
| PO2 | **Trip.com GDA contract** — sign + provide bank notification letter                                 | Awaiting signature                                 | `data/admin/client/PROFILE.md §13.1`             | —      | P0       |
| PO3 | Cancellation policy details (currently "Free up to 72h" from Expedia — confirmed for all channels?) | Expedia: confirmed. Others: assumed                | `data/property/property-config.json`             | —      | P1       |
| PO4 | Children policy for privatization events: child age limit, extra bed, baby cots?                    | Children policy (stays) confirmed. Events unclear. | `context/meta/knowledge/events-privatization.md` | VT-71  | P1       |
| PO5 | Smoking policy detail (designated areas — where exactly?)                                           | "Designated smoking areas" from Expedia            | `data/property/property-config.json`             | —      | P2       |
| PO6 | Response time targets for guest communications                                                      | Not defined                                        | `ops/status/truth.md §4`                         | —      | P2       |
| PO7 | Mr. Zakaria airport transfer — still 200 MAD flat rate? His full last name?                         | 200 MAD, Mr. Zakaria (+212 6 69 25 36 20)          | `data/admin/said-data-validation-checklist.md`   | —      | P2       |

---

## 6. Channel & Platform

| #   | Question                                                                                | Current Value                           | Source File                                 | Linear | Priority |
| --- | --------------------------------------------------------------------------------------- | --------------------------------------- | ------------------------------------------- | ------ | -------- |
| CH1 | **WhatsApp number** for property (guest communications) — not Said's personal number    | PENDING                                 | `ops/status/truth.md §4`                    | —      | P0       |
| CH2 | Instagram handle                                                                        | Unknown                                 | `ops/status/truth.md §4`                    | —      | P1       |
| CH3 | Facebook handle                                                                         | Unknown                                 | `ops/status/truth.md §4`                    | —      | P1       |
| CH4 | TripAdvisor management access                                                           | Listing exists (3.0/5). Handle unknown. | `ops/status/truth.md §4`                    | —      | P1       |
| CH5 | Secondary phone (06 62 14 69 49 from Google listing) — is this a valid property number? | Google listing — unverified             | `data/admin/client/PROFILE.md §2.1`         | —      | P1       |
| CH6 | **Expedia tax team** — follow-up (checkbox ticked, awaiting their contact)              | VT-82 created                           | `ops/handoff/handoff-repo-consolidation.md` | VT-82  | P0       |

Source: `ops/status/truth.md §4`, `data/admin/client/PROFILE.md`

---

## 7. Contact & Communication

| #   | Question                                                                            | Current Value                          | Source File                                    | Priority |
| --- | ----------------------------------------------------------------------------------- | -------------------------------------- | ---------------------------------------------- | -------- |
| CC1 | Secondary phone (06 62 14 69 49) — confirm ownership and purpose                    | Google listing only — unverified       | `data/admin/client/PROFILE.md §2.1`            | P1       |
| CC2 | Preferred communication channel for property matters (vs. Said's personal WhatsApp) | Said's personal WhatsApp +212661134194 | `data/admin/client/PROFILE.md §2.2`            | P1       |
| CC3 | Current TripAdvisor rating — Said to confirm (system shows 3.0/5)                   | 3.0/5 from listing                     | `data/admin/said-data-validation-checklist.md` | P2       |
| CC4 | Current Google rating — Said to confirm (system shows 4.5/5)                        | 4.5/5 from Google Maps                 | `data/admin/said-data-validation-checklist.md` | P2       |

---

## 8. Website & Brand

| #   | Question                                                           | Current Value          | Source File                          | Linear | Priority |
| --- | ------------------------------------------------------------------ | ---------------------- | ------------------------------------ | ------ | -------- |
| WB1 | **Website preferences**: template/examples, color codes, logo file | Blocked — waiting Said | `data/admin/client/PROFILE.md §13.2` | —      | P1       |
| WB2 | Point-of-sale descriptions (in Said's words)                       | Not provided           | `data/admin/client/PROFILE.md §13.2` | —      | P1       |
| WB3 | Social media links (Instagram, Facebook, TripAdvisor)              | Unknown                | `data/admin/client/PROFILE.md §13.2` | —      | P1       |
| WB4 | Logo file (for website and OTA listings)                           | Not provided           | `data/admin/client/PROFILE.md §13.2` | —      | P1       |

Source: `data/admin/client/PROFILE.md §13.2`

---

## 9. Events & Privatization

| #   | Question                                                     | Current Value                                 | Source File                                      | Linear | Priority |
| --- | ------------------------------------------------------------ | --------------------------------------------- | ------------------------------------------------ | ------ | -------- |
| EV1 | Breakfast rate for events — 160.90 MAD/person confirmed?     | 160.90 MAD (from Said profile) — "to confirm" | `context/meta/knowledge/events-privatization.md` | —      | P1       |
| EV2 | Spa/Hammam pricing for events (currently "on quote")         | On quote                                      | `context/meta/knowledge/events-privatization.md` | VT-71  | P1       |
| EV3 | Event decoration — managed by property or external? Pricing? | On quote                                      | `context/meta/knowledge/events-privatization.md` | —      | P2       |
| EV4 | External caterer allowed? Any surcharge?                     | Not clarified                                 | `context/meta/knowledge/events-privatization.md` | —      | P2       |
| EV5 | Internal restaurant: group menu on quote — who to contact?   | On quote                                      | `context/meta/knowledge/events-privatization.md` | —      | P2       |
| EV6 | Entertainment/music at events — allowed? Time limits?        | Not clarified                                 | `context/meta/knowledge/events-privatization.md` | —      | P2       |

Source: `context/meta/knowledge/events-privatization.md §Services`

---

## Resolution Log

When Said answers a question, move it here with the answer and date.

| Date       | Item                                   | Answer                                | Updated In                                         |
| ---------- | -------------------------------------- | ------------------------------------- | -------------------------------------------------- |
| 2026-02-21 | VAT treatment (inclusive vs exclusive) | Exclusive / HT (10%)                  | `data/finance/billing.json`, `ops/status/truth.md` |
| 2026-01-xx | Rates for all 12 rooms                 | Locked via HotelRunner Jan 2026       | `data/finance/rates.json`                          |
| (ongoing)  | Check-out time                         | 12:00 (Omar decision, Expedia Step 3) | `data/property/property-config.json`               |

Full resolved conflicts log: `ops/decisions/open-conflicts-registry.md §Resolved Conflicts`

---

_Registry created: 2026-02-21 — Consolidated from: ops/status/truth.md, ops/decisions/open-conflicts-registry.md, data/property/property-config.json, data/finance/billing.json, data/property/facilities/\*.md, data/admin/client/PROFILE.md, context/meta/knowledge/events-privatization.md, data/admin/said-data-validation-checklist.md_

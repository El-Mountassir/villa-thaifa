> **SUPERSEDED** — Pricing data in this file is outdated. Canonical rates: `data/finance/rates.json`. This file kept for historical reference only.
# Room → Platform Types Mapping — Villa Thaifa

**Last updated**: 2025-12-28
**Goal**: Explicit mapping between physical rooms and platform types (HotelRunner/Booking.com)

---

## Context

Villa Thaifa has **12 physical rooms** but platforms (HotelRunner, Booking.com) manage by **room type**.

### Platform Limitation

| Feature      | HotelRunner Free | With Paid PMS |
| ------------ | ---------------- | ------------- |
| Stop sell    | By TYPE          | By room       |
| Availability | By TYPE          | By room       |
| Pricing      | By TYPE          | By room       |

---

## Room → Type Mapping

| Room | Platform Type        | Price (EUR)  | Capacity |
| ---- | -------------------- | ------------ | -------- |
| 1    | Deluxe Triple Room   | 200          | 3        |
| 2    | Deluxe Double Room   | 200          | 2        |
| 3    | Deluxe Triple Room   | 200          | 3        |
| 4    | Double Room Superior | 160          | 2        |
| 5    | Double Room Superior | 160          | 2        |
| 6    | Executive Suite      | 240          | 2        |
| 7    | Deluxe King Suite    | [To confirm] | 2        |
| 8    | Deluxe Triple Room   | 200          | 3        |
| 9    | Family Suite         | 227          | 4        |
| 10   | Suite                | 267          | 2        |
| 11   | Family Suite         | 240          | 4        |
| 12   | Presidential Suite   | [To confirm] | 2        |

---

## Types by Group

### Rooms Sharing the Same Type

| Type                     | Rooms   | Consequence             |
| ------------------------ | ------- | ----------------------- |
| **Deluxe Triple Room**   | 1, 3, 8 | Stop sell affects all 3 |
| **Double Room Superior** | 4, 5    | Stop sell affects both  |
| **Family Suite**         | 9, 11   | Stop sell affects both  |

### Unique Types (1 room = 1 type)

| Type               | Room |
| ------------------ | ---- |
| Deluxe Double Room | 2    |
| Executive Suite    | 6    |
| Deluxe King Suite  | 7    |
| Suite              | 10   |
| Presidential Suite | 12   |

---

## Operational Implications

### Stop Sell by Type

If Said asks to "close Room 4":

- HotelRunner will block the TYPE "Double Room Superior"
- This ALSO affects Room 5

### Alternative Solution

To block a single room without affecting others of the same type:

- Create an "internal reservation" (fictitious) for this room
- Or check if the other room of the type is already occupied

---

_Source of truth for room/platform mapping_

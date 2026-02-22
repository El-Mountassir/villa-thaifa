# Decision: Room Pricing — HotelRunner Deployment Confirmation

**Date deployed:** 2026-01-13
**Date confirmed:** 2026-02-21
**Source authority:** HotelRunner platform deployment + Booking.com sync, confirmed via WhatsApp message from Omar
**Status:** Confirmed and applied

---

## Confirmed Prices (EUR, per night)

| Room | Price (EUR) | Internal Name        |
| ---- | ----------- | -------------------- |
| R01  | 169 EUR     | Deluxe Triple Room   |
| R02  | 159 EUR     | Deluxe Double Room   |
| R03  | 169 EUR     | Deluxe Triple Room   |
| R04  | 149 EUR     | Double Room Superior |
| R05  | 149 EUR     | Double Room Superior |
| R06  | 169 EUR     | Executive Suite      |
| R07  | 329 EUR     | Deluxe King Suite    |
| R08  | 169 EUR     | Deluxe Triple Room   |
| R09  | 189 EUR     | Family Suite         |
| R10  | 179 EUR     | Suite                |
| R11  | 189 EUR     | Family Suite         |
| R12  | 449 EUR     | Presidential Suite   |

---

## What Was Wrong

`data/finance/rates.json` contained 4 incorrect prices. `data/rooms/rooms.md` was correct all along.

| Room | rates.json (wrong) | Correct | rooms.md (correct) |
| ---- | ------------------ | ------- | ------------------ |
| R02  | 149 EUR            | 159 EUR | 159 EUR            |
| R04  | 159 EUR            | 149 EUR | 149 EUR            |
| R05  | 159 EUR            | 149 EUR | 149 EUR            |
| R06  | 179 EUR            | 169 EUR | 169 EUR            |

The errors originated from a previous decision (`room-pricing-confirmed.md`, 2026-02-19) which applied the wrong correction direction, swapping R02/R04/R05/R06 prices in the wrong direction.

---

## Changes Applied (2026-02-21)

- `data/finance/rates.json` — corrected R02, R04, R05, R06; updated `last_updated` and `lock_source`
- `data/archive/inventory.md` — removed incorrect stale-price notes from SUPERSEDED banner
- `ops/status/truth.md` — corrected pricing table rows for R02/R04/R05/R06; rewrote Section 9
- `ops/decisions/room-pricing-confirmed.md` — added correction note

---

## MAD Equivalents (at 10.72 exchange rate)

| Room | EUR | MAD   |
| ---- | --- | ----- |
| R02  | 159 | 1,704 |
| R04  | 149 | 1,597 |
| R05  | 149 | 1,597 |
| R06  | 169 | 1,812 |

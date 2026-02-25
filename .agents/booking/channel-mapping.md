# Channel Mapping — HotelRunner ↔ Booking.com

**Last updated**: 2025-12-29
**Source**: Sync investigation (Chrome browser)

---

## Connection Status

| Parameter       | Value            |
| --------------- | ---------------- |
| **Channel**     | Booking.com      |
| **Type**        | Two-Way XML      |
| **Status**      | Active           |
| **Last Sync**   | 2025-12-29 02:29 |
| **Hotel ID BC** | 5446847          |

---

## Room Type Mapping

| #   | Room Type HotelRunner | Room Type Booking.com           | Room ID BC | Units | Sync |
| --- | --------------------- | ------------------------------- | ---------- | ----- | ---- |
| 1   | Double Room Superior  | Chambre Double Superieur 4 ; 5  | 544684730  | 2     | XML  |
| 2   | Executive Suite       | Suite Executive 6               | 544684732  | 1     | XML  |
| 3   | Deluxe King Suite     | Suite De Luxe King Size 7       | 544684733  | 1     | XML  |
| 4   | Family Suite          | Suite Familiale 8 ; 11          | 544684736  | 2     | XML  |
| 5   | Deluxe Triple Room    | Chambre Triple Deluxe 1 ; 3 ; 8 | ?          | 3     | XML  |
| 6   | Deluxe Double Room    | Chambre Double Deluxe 2         | ?          | 1     | XML  |
| 7   | Suite                 | Suite 10                        | ?          | 1     | XML  |
| 8   | Presidential Suite    | Suite Presidentielle 12         | ?          | 1     | XML  |

**Legend**:

- Room ID BC = Booking.com Room ID
- Units = Number of physical rooms in this type
- Sync = Synchronization type

---

## Mapping Parameters (Advanced Settings)

Verified on 2025-12-29 for each room type:

| Parameter  | Value | Meaning                        |
| ---------- | ----- | ------------------------------ |
| Read only  | No    | Updates allowed to Booking.com |
| Stop sell  | No    | Sales open                     |
| Send price | Yes   | Prices synced to Booking.com   |

---

## Physical Rooms → Room Types

| Room | Room Type HotelRunner | Pool Booking.com                |
| ---- | --------------------- | ------------------------------- |
| 01   | Deluxe Triple Room    | Chambre Triple Deluxe 1 ; 3 ; 8 |
| 02   | Deluxe Double Room    | Chambre Double Deluxe 2         |
| 03   | Deluxe Triple Room    | Chambre Triple Deluxe 1 ; 3 ; 8 |
| 04   | Double Room Superior  | Chambre Double Superieur 4 ; 5  |
| 05   | Double Room Superior  | Chambre Double Superieur 4 ; 5  |
| 06   | Executive Suite       | Suite Executive 6               |
| 07   | Deluxe King Suite     | Suite De Luxe King Size 7       |
| 08   | Deluxe Triple Room    | Chambre Triple Deluxe 1 ; 3 ; 8 |
| 09   | Family Suite          | Suite Familiale 8 ; 11          |
| 10   | Suite                 | Suite 10                        |
| 11   | Family Suite          | Suite Familiale 8 ; 11          |
| 12   | Presidential Suite    | Suite Presidentielle 12         |

---

## Identified Issue (2025-12-29)

### Symptom

Reservations manually created on HotelRunner (source "Online") do not decrease availability on Booking.com.

### Evidence

| Date   | HR Reservation                          | Expected BC Availability | Actual BC Availability |
| ------ | --------------------------------------- | ------------------------ | ---------------------- |
| Dec 31 | Room 4 (Gouram) + Room 5 (Benchekroune) | 0                        | 1                      |
| Jan 1  | Room 4 + Room 5                         | 0                        | 2                      |
| Jan 2  | Room 4 only                             | 1                        | 2                      |

### Hypothesis

The Two-Way connection is configured to:

- ✓ Receive Booking.com reservations
- ✗ Not send inventory updates for internal reservations

### Actions

See full report: [`docs/reports/2025-12-29-sync-investigation.md`](../../../docs/reports/2025-12-29-sync-investigation.md)

---

## Sync Logs

| Date       | Success | Failures | Notes                                          |
| ---------- | ------- | -------- | ---------------------------------------------- |
| 2025-12-29 | 3,588   | 0        | 100% success (but internal bookings excluded?) |

---

## References

- [API Reference](api-reference.md)
- [Investigation Report](../../../docs/reports/2025-12-29-sync-investigation.md)
- [Room 04 File](../../configs/hotel/facilities/rooms/04-double-superior.md)
- [Room 05 File](../../configs/hotel/facilities/rooms/05-double-superior.md)

---

_Channel Mapping — Villa Thaifa_
_Prepared for future DB migration_

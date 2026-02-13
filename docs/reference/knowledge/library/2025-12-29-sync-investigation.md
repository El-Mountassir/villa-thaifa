# Investigation: HotelRunner ↔ Booking.com Sync Failure

| Field        | Value                    |
| ------------ | ------------------------ |
| Date         | 2025-12-29               |
| Investigator | Claude (AI Agent)        |
| Validated by | Omar El Mountassir       |
| Status       | **P0 ACTIONS COMPLETED** |
| Severity     | 🔴 Critical (mitigated)  |

---

## 🎯 P0 Actions Completed (2025-12-29)

| Action                                        | Status      | Result                                                            |
| --------------------------------------------- | ----------- | ----------------------------------------------------------------- |
| Block Dec 31 - Jan 2 on Booking.com           | ✅ **DONE** | "Chambre Double Superieur 4;5" closed via Open/Close Rooms wizard |
| Check HotelRunner "Sync Availability" setting | ✅ **DONE** | No explicit toggle found — see findings below                     |

### Key Discovery: "Allocation Type" Setting

In HotelRunner → Channels → Booking.com → Room type mapping → **Advanced settings**:

| Setting             | Current Value    | Issue                                 |
| ------------------- | ---------------- | ------------------------------------- |
| **Allocation Type** | **"No changes"** | ⚠️ Likely prevents availability push! |
| Base allotment      | (empty)          | Not configured                        |
| Last imported       | Dec 08, 2025     | 3 weeks stale                         |

**Recommendation**: Change "Allocation Type" from "No changes" to an active sync mode. Contact HotelRunner support for guidance on correct setting.

> ⚠️ **Note**: We could not view the dropdown options for "Allocation Type" during this investigation. HotelRunner support should advise on the correct setting value.

---

## Executive Summary

**Problem**: Internal/direct reservations created on HotelRunner do NOT sync to Booking.com, leaving dates available for double-booking.

**Root Cause**: The Two-Way XML sync between HotelRunner and Booking.com only processes Booking.com-originating reservations. Internal ("Online") reservations do not trigger availability updates to Booking.com.

**Risk**: Double-bookings for rooms 4 & 5 (Double Room Superior) and potentially other room types.

**Affected Reservations** (confirmed):

- Sabah Gouram: Dec 31, 2025 - Jan 3, 2026 (Room 4)
- Famille Benchekroune: Dec 31, 2025 - Jan 2, 2026 (Room 5)

---

## Investigation Summary

### Phase 1: Channel Connection Status ✓

| Check                       | Result              |
| --------------------------- | ------------------- |
| Booking.com in channel list | ✓ Active            |
| Connection type             | Two-Way XML         |
| Last sync timestamp         | Dec 29, 2025, 02:29 |

### Phase 2: Room Mapping Audit ✓

All 8 room types properly mapped:

| Room Type                | Mapping Status | Read Only | Stop Sell | Send Price |
| ------------------------ | -------------- | --------- | --------- | ---------- |
| Chambre Double Superieur | ✓ Mapped       | ✗ No      | ✗ No      | ✓ Yes      |
| Suite Executive          | ✓ Mapped       | ✗ No      | ✗ No      | ✓ Yes      |
| Suite De Luxe King Size  | ✓ Mapped       | ✗ No      | ✗ No      | ✓ Yes      |
| Suite Familiale          | ✓ Mapped       | ✗ No      | ✗ No      | ✓ Yes      |
| Chambre Triple Deluxe    | ✓ Mapped       | ✗ No      | ✗ No      | ✓ Yes      |
| Chambre Double Deluxe    | ✓ Mapped       | ✗ No      | ✗ No      | ✓ Yes      |
| Suite                    | ✓ Mapped       | ✗ No      | ✗ No      | ✓ Yes      |
| Suite Presidentielle     | ✓ Mapped       | ✗ No      | ✗ No      | ✓ Yes      |

**Conclusion**: Room mapping is NOT the problem.

### Phase 7: Transaction Logs ✓

| Metric             | Value        |
| ------------------ | ------------ |
| Total transactions | 3,588        |
| Successful         | 3,588 (100%) |
| Failed             | 0            |

**Conclusion**: No visible sync errors in logs. Transactions appear to succeed but may not include internal reservations.

### Phase 4-5: Calendar Comparison ✓

**HotelRunner Reservations for Double Room Superior (Dec 31 - Jan 3):**

| Guest                | Room | Dates          | Channel           | Status    |
| -------------------- | ---- | -------------- | ----------------- | --------- |
| Sabah Gouram         | 4    | Dec 31 - Jan 3 | Online (internal) | Confirmed |
| Famille Benchekroune | 5    | Dec 31 - Jan 2 | Online (internal) | Confirmed |

**Expected Booking.com Availability:**

| Date   | Expected Rooms | Reason                        |
| ------ | -------------- | ----------------------------- |
| Dec 31 | **0**          | Both Room 4 & 5 occupied      |
| Jan 1  | **0**          | Both Room 4 & 5 occupied      |
| Jan 2  | **1**          | Only Room 4 occupied (Gouram) |
| Jan 3  | **2**          | Both checkout                 |

**Actual Booking.com Availability:**

| Date   | Actual Rooms | Discrepancy             |
| ------ | ------------ | ----------------------- |
| Dec 31 | **1**        | 🔴 +1 extra room shown  |
| Jan 1  | **2**        | 🔴 +2 extra rooms shown |
| Jan 2  | **2**        | 🔴 +1 extra room shown  |
| Jan 3  | 2            | ✓ Correct               |

> ⚠️ **UPDATE 2025-12-29**: Dates Dec 31 - Jan 2 have been **MANUALLY BLOCKED** via Booking.com Open/Close Rooms wizard. The discrepancy above reflects the state BEFORE mitigation was applied. Double-booking risk for these specific dates is now mitigated.

---

## Root Cause Analysis

### Confirmed Behavior

1. **Booking.com → HotelRunner**: Reservations from Booking.com DO appear in HotelRunner ✓
2. **HotelRunner → Booking.com (Booking.com reservations)**: Net booked shows correctly for Dec 29-30 ✓
3. **HotelRunner → Booking.com (Internal reservations)**: **NOT syncing** ✗

### Hypothesis (Updated 2025-12-29)

The XML connection is configured for **reservation synchronization** (pulling Booking.com reservations) but NOT for **availability push** (sending internal reservations to block Booking.com calendar).

**NEW FINDING**: The "Allocation Type" setting in Room type mapping → Advanced settings is set to **"No changes"**, which likely means HotelRunner does NOT push availability updates to Booking.com for this room type.

This is a known limitation in some channel manager configurations:

- **One-Way Pull**: Only receives reservations from OTAs
- **Two-Way Reservation**: Sends/receives reservations but not manual availability blocks
- **Full Two-Way**: Sends availability updates for ALL reservations (including internal)

Villa Thaifa appears to have **Two-Way Reservation** but NOT **Full Two-Way Availability Sync**.

**Additional Evidence**:

- Last import from Booking.com: December 08, 2025 (3 weeks ago)
- "Update room availabilities after importing the reservations" checkbox exists but only applies to IMPORT, not EXPORT

---

## Evidence

### Screenshot References

1. HotelRunner Reservations page showing Gouram & Benchekroune
2. Booking.com Calendar showing incorrect availability for Dec 31 - Jan 2
3. Booking.com "XML (not editable)" confirmation
4. HotelRunner Logs showing 3,588 successful transactions

### Key Observations

| Observation                                      | Interpretation                                     |
| ------------------------------------------------ | -------------------------------------------------- |
| Booking.com calendar locked ("XML not editable") | Channel manager connection active                  |
| Dec 29-30 show "Net booked = 1"                  | Booking.com reservations sync correctly            |
| Dec 31 - Jan 2 show "Net booked = 0"             | Internal reservations NOT syncing                  |
| HotelRunner logs show 100% success               | Transactions may not include internal reservations |

### HotelRunner Connectivity Status (2025-12-29)

All services show active connection to Booking.com:

| Service                       | Status                      |
| ----------------------------- | --------------------------- |
| Connection status             | ✅ Connection is active     |
| Content                       | ✅ Connection is active     |
| Guest Reviews                 | ✅ Connection is active     |
| Messaging                     | ✅ Connection is active     |
| Performance Data And Insights | ✅ Connection is active     |
| Photos                        | ✅ Connection is active     |
| **Rate and Availability**     | ✅ **Connection is active** |
| Reporting                     | ✅ Connection is active     |
| Reservations                  | ✅ Connection is active     |

**Implication**: The capability to sync availability EXISTS. The issue is likely configuration (Allocation Type setting), not a missing feature.

---

## Omar's Hypothesis

> "Je pense que c'est à cause du fait que le mapping des chambres sur booking doit être modifier pour devenir en chambres et pas groupé par type."

**Assessment**: This hypothesis has merit. Currently:

- Booking.com shows "Chambre Double Superieur **4 ; 5**" as a single room type
- HotelRunner manages Room 4 and Room 5 as individual rooms

If a reservation is made for "Room 4" specifically on HotelRunner, the system may not know how to communicate this to Booking.com's room-type-based model.

**However**, this doesn't fully explain why the room-type availability isn't being reduced at all. Even if individual rooms aren't mapped, the total availability for the room type should decrease.

---

## Recommended Actions

### Immediate (Today)

| Priority | Action                                                                      | Owner  | Status                                    |
| -------- | --------------------------------------------------------------------------- | ------ | ----------------------------------------- |
| 🔴 P0    | Manually block Dec 31 - Jan 2 on Booking.com calendar (if possible)         | Claude | ✅ DONE                                   |
| 🔴 P0    | Verify if "Sync Availability" option exists in HotelRunner channel settings | Claude | ✅ DONE (found "Allocation Type" setting) |
| 🔴 P0    | Contact HotelRunner support with this investigation report                  | Omar   | ⏳ Pending                                |

### Short-term (This Week)

| Priority | Action                                                | Owner | Status                                     |
| -------- | ----------------------------------------------------- | ----- | ------------------------------------------ |
| 🟠 P1    | Review HotelRunner "Allocation Type" dropdown options | Omar  | ⏳ Pending (Claude couldn't open dropdown) |
| 🟠 P1    | Test "Import reservations" button to force sync       | Omar  | ⏳ Pending                                 |
| 🟠 P1    | Verify Booking.com extranet for any NON-XML settings  | Omar  | ⏳ Pending                                 |

### Medium-term

| Priority | Action                                                          | Owner              |
| -------- | --------------------------------------------------------------- | ------------------ |
| 🟡 P2    | Consider room-level mapping (individual rooms vs room types)    | Omar + HotelRunner |
| 🟡 P2    | Evaluate alternative channel managers if HotelRunner cannot fix | Omar               |
| 🟡 P2    | Document SOP for manual calendar sync as workaround             | Claude             |

---

## Support Ticket Draft

**Subject**: Internal reservations not syncing availability to Booking.com

**To**: HotelRunner Support

**Body**:

```
Property: Villa Thaifa
HR_ID: [Check credentials file]
Connection: Booking.com (Two-Way XML)

Problem:
Reservations created manually on HotelRunner (source: "Online"/internal) do not
reduce availability on Booking.com calendar. This creates double-booking risk.

Specific Example:
- Guest: Sabah Gouram
- Dates: Dec 31, 2025 - Jan 3, 2026
- Room Type: Double Room Superior (Room 4)
- Confirmation: R599233355
- Created on: HotelRunner (internal)

Expected: Booking.com should show 1 room available for Double Room Superior
(2 total - 1 booked = 1 available)

Actual: Booking.com shows 2 rooms available (no reduction)

Observations:
- Channel connection active (XML not editable on Booking.com)
- Room mapping correct (8 room types, no Read Only)
- Transaction logs show 3,588 successes, 0 failures
- Reservations FROM Booking.com appear correctly
- "Allocation Type" setting in Room type mapping → Advanced settings is set to "No changes"
- Last import from Booking.com: December 08, 2025 (3 weeks ago)
- Connectivity status shows "Rate and Availability: Connection is active"

Questions:
1. What does "Allocation Type: No changes" mean? Should this be changed to enable availability sync?
2. How do we trigger a manual sync to push availability updates to Booking.com?
3. Why hasn't the import run automatically since December 08?
4. Is there a setting to enable availability sync for internal/manual reservations?

Please advise urgently - we risk double-bookings during high season.

Thank you,
Villa Thaifa Management
```

---

## Files Created/Updated

| File                                                       | Purpose                              |
| ---------------------------------------------------------- | ------------------------------------ |
| `docs/reports/2025-12-29-sync-investigation.md`            | This report                          |
| `data/specs/platform/hotelrunner/api-reference.md`         | API documentation (previous session) |
| `docs/incidents/open/2025-12-29-webfetch-access-errors.md` | Web access issues (previous session) |

---

## Next Steps

1. **Omar reviews** this report and validates findings
2. **Omar contacts** HotelRunner support with the draft ticket
3. **Manual workaround**: Block affected dates on Booking.com calendar directly (if extranet allows despite XML)
4. **Document SOP** for future internal reservations until fix is implemented

---

## Appendix: Technical Details

### HotelRunner API Reference

```
GET /rooms?token={TOKEN}&hr_id={HR_ID}
```

Key fields to check:

- `availability_update`: Should be `true`
- `channel_codes`: Should include `bookingcom`
- `is_master`: Should be `false`

**Note**: API credentials not available in current session. Manual check via HotelRunner UI recommended.

### Booking.com Calendar Structure

```
Room Type: Chambre Double Superieur 4 ; 5
Room ID: 544684730
Inventory: 2 units (physical rooms 4 & 5)
```

The "4 ; 5" suffix indicates Booking.com knows about individual rooms but manages them as a pool under one room type.

---

## Update Log

| Date       | Version | Changes                                                                       |
| ---------- | ------- | ----------------------------------------------------------------------------- |
| 2025-12-29 | 1.0     | Initial investigation report                                                  |
| 2025-12-29 | 1.1     | P0 actions completed: Booking.com dates blocked, HotelRunner settings audited |
| 2025-12-29 | 1.2     | Added connectivity evidence, updated support ticket, calendar mitigation note |

---

_Investigation completed: 2025-12-29_
_P0 Actions completed: 2025-12-29_
_Report version: 1.2_

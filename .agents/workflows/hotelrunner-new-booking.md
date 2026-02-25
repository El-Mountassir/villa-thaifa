---
description: How to process a new direct booking end-to-end
---

# HotelRunner New Booking Workflow

**Target Platform:** HotelRunner (<https://villa-thaifa.hotelrunner.com/>) + Local Repository
**Objective:** Process a new direct booking request from the owner, ensure it exists in the PMS, sync it to the local database, and send a standard status update.

## Execution Steps

When dispatching a `browser_subagent` and processing a new booking, follow these steps:

1. **Verify or Create in HotelRunner**
   - Use the `browser_subagent` to log into HotelRunner.
   - Go to `Réservations` > `Nouvelle réservation` OR check the existing calendar/reservations list.
   - Verify if a booking with the exact guest name, dates, and room already exists (e.g., entered by the owner or OTA).
   - If it **does not exist**, manually input the details: Guest Name, Check-in/out, Guests, Room Type, and Price.
   - **CRITICAL STEP**: You MUST click "Sauvegarder" (Save/Update) or the equivalent confirmation button at the bottom right to apply the reservation.
   - If it **already exists**, simply note the Confirmation/Resolution ID and verify the parameters match.

2. **Verify Execution in HotelRunner (Mandatory)**
   - After clicking save, DO NOT proceed blindly.
   - Wait for the page to reload or show a success toast (e.g., "Réservation mise à jour").
   - Explicitly verify the booking by either seeing the confirmation ID on the page or searching for the booking on the calendar/reservations list to ensure it was permanently saved.

3. **Sync to Local Database**
   - Open `data/bookings/reservations/reservations.md`.
   - Update the "Last updated" date.
   - Locate the appropriate month category (e.g., `### February 2026`) or create it if missing.
   - Add a row for the guest with the Arrival Date, Room Type, Nights, Amount, Room Number, and Status (`✅ Assigned` if a specific room is booked).

4. **Reporting to Said**
   - After confirming HotelRunner and updating the local database, you MUST prepare a status update for the owner (Said).
   - Write this to `ops/status/reports/update/said/README.md` (prepend just under the main heading) using the exact standard Dutch template below, substituting the appropriate variables:

   ```text
   ## [DD-MM-YYYY]
   **Status:** `Draft`

   Salam Si Said,

   Missie voltooid ✅.

   Ik heb de reservering voor *[GUEST_NAME]* verwerkt op HotelRunner:
   📅 *[CHECK_IN_DUTCH] - [CHECK_OUT_DUTCH]*
   🔒 [ROOM_TYPE] (Kamer [ROOM_NUMBER])
   💶 Totaal: €[AMOUNT]

   Alles staat klaar in het systeem.
   Geen zorgen, alles is in orde! 👍

   Fijne avond! 🙏
   ```

## Example Browser Subagent Prompt

```text
Navigate to the HotelRunner dashboard for Villa Thaifa.
1. Check the existing reservations list or calendar for a booking under the name "[GUEST_NAME]" from [CHECK_IN] to [CHECK_OUT].
2. If it exists, verify the details (Guests, Room Type, Price) and return the Booking ID.
3. If it does not exist, navigate to "Réservations" > "Nouvelle réservation".
4. Enter Guest Name: [GUEST_NAME], Check-in: [CHECK_IN], Check-out: [CHECK_OUT], Guests: [GUEST_COUNT], Room: [ROOM_TYPE], Price: €[AMOUNT].
5. Click "Sauvegarder" (Save) at the bottom right to apply the booking.
6. MANDATORY VERIFICATION: Verify the booking was created successfully (wait for success message "Réservation mise à jour" or search for the new booking ID). Return the Booking ID upon confirmed success.
DO NOT double-book. Always verify existence first.
```

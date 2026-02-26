---
description: How to process a multi-room booking for the same guest via the PMS Grid
---

# HotelRunner Multi-Room Booking Workflow

**Target Platform:** HotelRunner (<https://villa-thaifa.hotelrunner.com/>)
**Objective:** Process a single booking request that requires multiple rooms for the same client, utilizing the PMS Quick Reservation grid to ensure all rooms are linked to the same guest profile.

## Context

When a guest requests multiple rooms (e.g., two suites for different family members), it is often more reliable for automated agents to use the **PMS Quick Reservation (Réservation Rapide)** grid to book each room individually while explicitly linking them to the identical guest contact. This avoids complex DOM interactions with the "Ajouter une chambre" dynamic forms in the standard booking engine.

## Execution Steps for the Browser Subagent

When prompting a `browser_subagent` to execute a multi-room booking, provide the following rigid instructions:

1. **Navigate to the PMS Grid**
   - Go to `PMS` -> `Réception` -> `Réservation rapide` (Quick Reservation).

2. **Book the First Room**
   - **Contact**: Click the search icon under the 'Contact principal' (Main Contact) column. Search for the guest's name (e.g., "Elisabeth Delacarte"). If the contact does not exist, type it in to create it, or select it if it drops down.
   - **Dates**: Set the Check-in and Check-out dates (e.g., 23/04/2026 to 27/04/2026).
   - **Room Details**: Select the appropriate room type and room number for the first room.
   - **Guests & Price**: Set the number of Adults/Children and the total price for this specific room.
   - **Save**: Click the "Sauvegarder" (Save) button at the right end of the row. Wait for the confirmation toast/modal and close it.

3. **Book the Subsequent Room(s)**
   - Remain on or return to the `PMS` -> `Réception` -> `Réservation rapide` page.
   - **CRITICAL LINKING STEP**: Under 'Contact principal' for the new row, you MUST search for and select the **exact same contact** that was used/created in Step 2. This groups the reservations under the single guest profile.
   - **Dates**: Enter the Check-in and Check-out dates again.
   - **Room Details**: Select the room type and number for the second room.
   - **Guests & Price**: Set the Adults/Children and price. _Note: If the quick grid hides the "Children" input for certain configurations, instruct the subagent to add the children count into the 'Notes' popup that appears upon saving or clicking the note icon._
   - **Save**: Click "Sauvegarder" and close the confirmation.

4. **Mandatory Verification**
   - Navigate to `Réservations` -> `Toutes les réservations`.
   - Search for the guest's name.
   - EXPLICITLY VERIFY that there are distinct Booking IDs (e.g., R080392137, R186486779) for each room requested, that the dates are correct, and the status is Confirmed (or Waiting Confirmation).

5. **Reporting**
   - After confirming success, you MUST prepare a status update for the owner (Said).
   - Write this to `ops/status/reports/update/said/README.md` (prepend just under the main heading) using the exact standard Dutch template, aggregating all rooms into a single message.
   - **Crucial**: Include the `**Status:** \`Draft\`` metadata just below the date header.

   ````markdown
   ## [DD-MM-YYYY] (Réservations [GUEST_NAME])

   **Status:** `Draft`

   ```text
   Salam Si Said,

   Missie voltooid ✅.

   Ik heb de reserveringen voor *[GUEST_NAME]* verwerkt op HotelRunner:
   📅 *[START_DATE_DUTCH] - [END_DATE_DUTCH] [YYYY]* ([N] nachten)
   🔒 [ROOM_TYPE_1] (Kamer [X]) - [A] Volwassenen, [C] Kinderen
   🔒 [ROOM_TYPE_2] (Kamer [Y]) - [A] Volwassenen, [C] Kinderen
   💶 Totaal: €[TOTAL_PRICE]

   Alles staat klaar in het systeem.
   Geen zorgen, alles is in orde! 👍

   Fijne avond! 🙏
   ```
   ````

6. **Local Sync**
   - Ensure you sync **all** newly generated reservations into the local database at `data/bookings/reservations/reservations.md`.

## Example Browser Subagent Prompt

```text
You must create a multi-room booking for [GUEST_NAME] from [CHECK_IN] to [CHECK_OUT].
We will use the PMS grid to do this reliably.

1. Go to PMS -> Réception -> Réservation rapide.
2. For Room 1 ([ROOM_TYPE_1]):
   - Set the Main Contact to "[GUEST_NAME]".
   - Set dates: [CHECK_IN] to [CHECK_OUT].
   - Set Adults: [A], Children: [C], Price: [PRICE_1].
   - Click 'Sauvegarder'.
3. Wait for the save confirmation.
4. For Room 2 ([ROOM_TYPE_2]):
   - In a new quick reservation row, set the Main Contact to the EXACT same "[GUEST_NAME]".
   - Set dates: [CHECK_IN] to [CHECK_OUT].
   - Set Adults: [A], Children: [C], Price: [PRICE_2].
   - Click 'Sauvegarder'.
5. Navigate to the main Reservations list and visually confirm both bookings exist for [GUEST_NAME].
```

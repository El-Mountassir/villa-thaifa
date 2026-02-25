---
description: How to correctly apply a Stop Sell on HotelRunner (Row-by-Row Method)
---

# HotelRunner Stop Sell Workflow

**Target Platform:** HotelRunner (<https://villa-thaifa.hotelrunner.com/>)
**Objective:** Set a Stop Sell (availability to 0 and "Stop Sell" flag to "Oui") for a specific date or date range across all rooms and rate plans.

## Context & Warnings

> [!WARNING]
> DO NOT use the "Mises à jour par bloque" (Bulk Updates) tool for automated browser agents. Previous executions have shown that while the subagent can interact with the bulk update modal, HotelRunner frequently fails to properly save and sync the Stop Sell flags across all grids when submitted via automation.

To ensure visual validation and 100% success rate, **always use the manual row-by-row method** documented below.

## Row-by-Row Execution Steps

When dispatching a `browser_subagent` to perform a Stop Sell on HotelRunner, use the following rigid steps in your prompt:

1. **Navigate to Advanced Updates**
   - Go to `Calendrier` -> `Mises à jour avancées` (Calendar -> Advanced Updates).

2. **Set the Target Date Range**
   - Click `Personnaliser le calendrier`.
   - Set both the **Start Date** and **End Date** to your exact target dates.
   - Select the checkbox for **"Tout"** (All Rooms).
   - Click the **"Continuer"** button to refresh the grid.

3. **Enable Stop Sell Visibility**
   - At the top right of the grid, check the **"Stop sell"** checkbox. This expands the grid to show the Stop Sell dropdown for every specific room and rate plan.

4. **Apply Changes Room by Room**
   - Tell the subagent to iterate through **EVERY SINGLE ROOM** visible on the page (e.g., Chambre Double Superieur, Suite Familiale, etc.).
   - For every room:
     - Change the **Disponibilité** (Availability) input to `0`.
     - Click the **Stop sell** dropdown and explicitly select **"Oui"**.
   - _Note: There are usually about 8-10 rooms. The subagent must do this for each of them individually._

5. **Global Save**
   - Scroll to the very bottom right of the page.
   - Click the **"Mise à jour"** (Update) button to apply the changes.
   - A modal will appear asking to confirm the distribution channels (e.g., Online, Booking.com). Ensure all are selected and click to confirm/continue.

6. **Mandatory Verification**
   - Wait for the page to reload or show a success toast.
   - EXPLICITLY VERIFY that the availability (Disponibilité) is 0 and the calendar column for the target date is highlighted in RED (indicating a full block). Note: The Stop Sell dropdown may revert to a dash `-` rather than "Oui" when availability is 0. Do not assume success until visually verified.

7. **Reporting**
   - After confirming success, you MUST prepare a status update for the owner (Said).
   - Write this to `ops/status/reports/update/said/README.md` (prepend just under the main heading) using the exact standard Dutch template below, substituting the dates:

   ````markdown
   ## [DD-MM-YYYY]

   **Status:** `Draft`

   ```text
   Salam Si Said,

   Missie voltooid ✅.

   Ik heb de beschikbaarheid voor *[TARGET_DATE_DUTCH]* bijgewerkt op HotelRunner:
   📅 *[TARGET_DATE_DUTCH]*
   🔒 Alle kamertypes geconfigureerd (Stop Sell)
   💶 Beschikbaarheid op 0 gezet

   Alles is veiliggesteld voor deze datum.
   Geen zorgen, alles is in orde! 👍

   Fijne avond! 🙏
   ```
   ````

## Example Browser Subagent Prompt

```text
You must set the entire villa to 'Stop sell' for [TARGET_DATE]. DO NOT use the Bulk Update tool (Mises à jour par bloque) as it has proven buggy in previous runs.

Instead:
1. Go to "Calendrier" -> "Mises à jour avancées" (Advanced Updates).
2. Use "Personnaliser le calendrier" to change the date range to exactly [TARGET_DATE].
3. Check the "Stop sell" checkbox at the top right so the stop sell rows become visible.
4. IMPORTANT: For EVERY SINGLE ROOM listed on the page, navigate to its "Stop sell" dropdown for [TARGET_DATE] and select "Oui". There are about 8-10 rooms. You MUST do this for each of them.
5. Also, for every room, make sure the "Disponibilité" input field is set to 0.
6. Once you have selected "Oui" for every room's stop sell dropdown, scroll to the bottom right and click the "Mise à jour" (Update) button to apply the changes.
7. Confirm any channel distribution modals that appear.
8. MANDATORY VERIFICATION: Verify that the availability is 0 and the calendar column is RED for [TARGET_DATE] after the save operation completes. Do not assume it worked.

After successful execution, draft the standard Dutch completion message for Said targeting `ops/status/reports/update/said/README.md` (remembering to include `**Status:** \`Draft\``).
```

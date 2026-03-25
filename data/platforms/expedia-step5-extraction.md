# Expedia Partner Central — Step 5 Extraction

**Property**: Villa Thaifa (htid=114807934)
**Step**: 5 of 12
**Title**: Rooms and rates
**URL**: https://apps.expediapartnercentral.com/supply/pc-onboard/roomsAndRates?htid=114807934
**Extracted**: 2026-02-21
**Note**: READ ONLY — no form values were modified during extraction

---

## Step Overview

Step 5 is the **"Rooms and rates" gateway page**. It serves as a landing screen where room types are listed and new ones can be added. The actual room configuration (basic info, amenities, room name, rates) happens in subsequent sub-steps that open when a room type is added. The step description states: "We'll help you set up basic room info, room amenities, room name, and rates over the next few steps. You can always update this after you're live."

This page is currently **empty** — no room types have been created yet. The "Next" button is grayed out (disabled) because at least 1 room is required to proceed.

---

## Onboarding Progress Bar (Step Map)

Captured from the accessibility tree progress bar:

| Step | Slug                   | Status in Progress Bar       |
|------|------------------------|------------------------------|
| 1    | basicPropertyHotelier  | Complete (solid blue)        |
| 2    | contract               | Complete (solid blue)        |
| 3    | policiesAndSettings    | Complete (solid blue)        |
| 4    | modularAmenities       | Complete (solid blue)        |
| 5    | roomsAndRates          | **Current** (hatched blue)   |
| 6    | ratePlans              | Not reached (gray)           |
| 7    | ratesAndAvailability   | Not reached (gray)           |
| 8    | promotions             | Not reached (gray)           |
| 9    | photos                 | Not reached (gray)           |
| 10   | taxes                  | Not reached (gray)           |
| 11   | regulatory             | Not reached (gray)           |
| 12   | connectivitySettings   | Not reached (gray)           |

---

## Section 1: Room Type List

### Tab Navigation

| Tab              | Count | State                    |
|------------------|-------|--------------------------|
| Finished rooms   | 0     | Active (selected)        |
| Unfinished rooms | 0     | Not selected             |

### Finished Rooms Tab (Active)

| Element               | Value / Text                                        | State              |
|-----------------------|-----------------------------------------------------|--------------------|
| Heading               | "Add your most popular room type to get started"   | Displayed          |
| Add room type button  | "Add room type"                                     | Enabled (clickable)|
| Helper text           | "You can add more, but you need at least 1 to go live." | Displayed      |
| Room list             | (empty — no rooms added)                            | Empty              |

### Unfinished Rooms Tab

| Element     | Value / Text                                | State     |
|-------------|---------------------------------------------|-----------|
| Message     | "Your unfinished rooms will appear here."   | Displayed |
| Room list   | (empty — no unfinished rooms)               | Empty     |

---

## Section 2: Navigation Controls

| Element      | State                        | Notes                                     |
|--------------|------------------------------|-------------------------------------------|
| Back button  | Enabled                      | Returns to Step 4 (modularAmenities)      |
| Next button  | Disabled (grayed out)        | Requires at least 1 finished room type    |

---

## Key Observations

1. **Step 5 is a gateway, not a form.** No form fields are presented directly on this page. The actual room data entry happens inside the room type creation flow (triggered by "Add room type").
2. **Blocked progression.** The "Next" button is disabled — the onboarding cannot advance past Step 5 until at least one room type is fully configured.
3. **Two-tab structure.** Rooms are tracked as either "Finished" or "Unfinished", giving the user a way to save incomplete room configurations and return later.
4. **Zero rooms currently.** Both tabs show empty states, indicating no room types have been set up in the Expedia onboarding wizard for Villa Thaifa yet.
5. **Post-live editing allowed.** The page explicitly states "You can always update this after you're live" — not a hard lock.

---

## Extraction Summary

- **Total fields**: 6 (tab selectors, button, helper texts, empty states, nav buttons)
- **Filled/checked**: 0 form fields (page is empty — no rooms added)
- **Empty/unchecked**: 0 finished rooms, 0 unfinished rooms
- **Modules**: Room Type List (Finished Rooms tab, Unfinished Rooms tab), Navigation Controls
- **Page type**: Gateway / list page (no direct form fields — room config is in sub-steps)
- **Blocker**: "Next" is disabled; at least 1 room type must be added and finished before advancing

# HotelRunner — Bulk Updates Guide (Restrictions & More)

## Property Context

- **Property**: Villa Thaifa
- **Admin URL**: `villa-thaifa.hotelrunner.com/admin`
- **Channels**: Online (direct channel) + Booking.com
- **Rate Plans**: Master rate, Breakfast included Flexible, Breakfast included Non-refundable (all in EUR)
- **Rooms** (8 types): Double Room Superior, Deluxe Double Room, Deluxe Triple Room, Suite, Deluxe King Suite, Family Suite, Executive Suite, Presidential Suite

---

## Workflow: Modifying a Restriction (Stop Sell, CTA, CTD, etc.) via Bulk Updates

### Access Path

`Calendar > Bulk Updates` Direct URL: `https://villa-thaifa.hotelrunner.com/admin/products/villa-thaifa/channel/prices/bulk_update`

### Detailed Steps

**1. Configure the filters on the left:**

- **Rate plans**: Leave "All rate plans" (unless specific targeting)
- **Currency**: Leave "All currencies"
- **"What do you want to update?"**: Check the desired restriction (e.g., "Stop sell")
- **Date Range**:
  - **Date format**: `MM/DD/YYYY` (US format!)
  - Ex: March 12, 2026 → `03/12/2026`, December 16, 2026 → `12/16/2026`
  - You can type directly in the field or use the popup calendar
- **Days**: Leave "All" checked (unless targeting specific days)
- **Channels** (on the right): Keep "All" checked to apply to Online AND Booking.com

**2. Use the Master Dropdown (crucial tip):**

- After checking a restriction, a 🔗 icon appears in the "Restrictions" column header
- **Click on this icon** → reveals a "master" dropdown at the top of the column + a ↓ arrow
- **Select the value in the master dropdown** (e.g., "No" to remove, "Yes" to activate)
- **Click on the ↓ arrow** → propagates the value to ALL rooms and rate plans at once!

**3. Visually verify** that all rows display the desired value (scroll down to see all rooms)

**4. Click "Update"** → A **Preview** panel appears with:

- Summary of dates, days, channels
- Table of all rooms with changes
- Scroll right in the Preview to see the "Restrictions" column and confirm (e.g., "Stop sell: ✕" = disabled)

**5. Confirm by clicking "Update"** in the Preview (blue button bottom right)

**6. Post-action verification:**

- Go to `Calendar > Simple Updates` (URL: `.../channel/prices?f=1`)
- Navigate to a date in the modified range
- **Online Channel**: immediate change (white background = OK, red background = Stop Sell active)
- **Booking.com**: may show "Waiting Response from Channel" during sync (normal)

---

## Restriction Values

| Restriction                  | Possible Values | Meaning                                    |
| ---------------------------- | --------------- | ------------------------------------------ |
| **Stop Sell**                | Yes / No        | Yes = room closed for sale, No = room open |
| **CTA** (Close to Arrival)   | Yes / No        | Yes = no new arrivals on this day          |
| **CTD** (Close to Departure) | Yes / No        | Yes = no departures on this day            |
| **Minimum Stay**             | Number (days)   | Minimum length of stay                     |
| **Maximum Stay**             | Number (days)   | Maximum length of stay                     |
| **Cut off time**             | Number (hours)  | Reservation lead time before arrival       |
| **Availability**             | Number          | Rooms available                            |
| **Price**                    | Amount (€)      | Base price                                 |

---

## Visual Indicators in Simple Updates (Calendar)

| Indicator                           | Meaning                                     |
| ----------------------------------- | ------------------------------------------- |
| **White** background + price        | Room available, no restriction              |
| **Red** background + red icons      | Stop Sell active or blocking restriction    |
| **Red dot** at bottom of cell       | Active restriction (Stop Sell, CTA, CTD...) |
| **Green check** ✓                   | Sync OK with channel                        |
| "**Waiting Response from Channel**" | Update sent, awaiting channel confirmation  |
| **N/A**                             | No price defined on this channel            |

---

## Common Pitfalls to Avoid

1. **Date format**: Always `MM/DD/YYYY` (month/day/year), not European format
2. **"-" in dropdowns**: Means "no change" — must explicitly choose "Yes" or "No"
3. **Forgetting the ↓ arrow**: Changing the master dropdown is not enough, must click arrow to propagate
4. **End Date before Start Date**: The Advanced Updates calendar will show nothing
5. **Booking.com Sync**: Don't panic if "Waiting Response from Channel" — it's normal
6. **Check the scroll**: Family Suite, Executive Suite, Presidential Suite rooms are at the bottom of the list

---

## Other Similar Bulk Update Operations

The same workflow applies to bulk modify:

- **Availability** → change the number of available rooms
- **Price** → adjust rates
- **Price adjustment** → adjust by % or amount
- **Minimum/Maximum stay** → stay length restrictions
- **CTA/CTD** → close/open arrivals or departures
- **Cut off time** → booking lead time

For each, the process is identical: check the box on left → configure dates/days/channels → use master dropdown + arrow ↓ → Preview → Update.

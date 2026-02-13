# Booking.com Extranet UI Nuances

> **Context**: This document captures specific UI behaviors, hidden toggles, and "gotchas" in the Booking.com Extranet to prevent future agent oversight.

## ⚠️ Critical Hidden Toggles

### "Show Advanced View" (Room Details)

- **Location**: Often found on the **Room Details** overview page ( `/hotel/hoteladmin/extranet_ng/manage/rooms.html` ), usually near the top right of the list or filter section.
- **Impact**: Without this toggled, critical settings like **Occupancy Breakdowns** (Adults vs Children), **Room IDs**, and **Derived Pricing** rules might be hidden.
- **Agent Rule**: ALWAYS look for "Show/Hide Advanced View" or similar expansion toggles when navigating list views on Booking.com. Do not assume the default view shows all data.

## 🧠 General UI Lessons

- **Expand All**: Before scraping/reading a page, always check for "Expand All" or accordion elements.
- **Edit vs. View**: Some details (like full amenities list or specific bed constraints) are ONLY visible after clicking "Edit", even if they aren't meant to be changed.
- **Pagination**: Booking.com lists are often paginated. Always check for "Next" buttons.

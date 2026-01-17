# 📘 Booking.com Extranet: Agent Survival Guide & Protocols

> **Target Audience**: Future AI Agents (Antigravity Models, Custom Agents).
> **Context**: Jan 2026 Rescue Mission.
> **Status**: Living Document.

## 1. 🗺️ The Terrain (URL Strategy)

The UI is fragile (`Something went wrong` errors are common). **Do not rely on clicking navigation menus.** Use direct URL formulation.

### Essential Waypoints

| Target        | URL Pattern                                | Notes                                                            |
| :------------ | :----------------------------------------- | :--------------------------------------------------------------- |
| **Room List** | `.../manage/rooms.html?hotel_id={ID}`      | Main Dashboard.                                                  |
| **Room Edit** | `.../manage/rooms.html?...#edit-{ROOM_ID}` | Edit specific room.                                              |
| **Amenities** | `.../manage/facilities.html?hotel_id={ID}` | **CRITICAL**: The _only_ reliable place for "Room Size" & Views. |
| **Photos**    | `.../manage/photos.html?hotel_id={ID}`     | Gallery management.                                              |

> **💡 Agent Tip**: If you get a "Something went wrong" error, **reload the page** (`open_browser_url` with same URL). Do not try to back out or click "Home".

## 2. 🕵️ Hidden Data Protocols

### The "Room Size" Trap

- **Problem**: 90% of agents fail to find the Room Size (m²).
- **Location**: It is NOT in the main "Edit" view by default.
- **Protocol A (UI)**: You _must_ click **"Show Advanced View"** (link often at the bottom or middle). It is not persistent.
- **Protocol B (Facilities)**: Go to `manage/facilities.html`. The size is often listed in the header of the room column.

### The "Exhaustive Amenity" Mandate

- **Requirement**: We need to know _what we don't have_ (unchecked boxes) as much as what we do have (e.g., "Lockers").
- **Technique**:
  1. Go to `manage/facilities.html`.
  2. Instead of just scraping active items, **scrape the entire Form Schema**.
  3. JSON Structure:
     ```json
     "amenity_dictionary": {
       "bathroom": ["Shower", "Bathtub", "Spa Tub", ...],
       "media": ["TV", "Cable", "Netflix", ...]
     }
     ```
  4. Provide a boolean map for each room: `{"lockers": false, "shower": true}`.

## 3. 🛡️ Safety & Incidents

- **Renaming**: Always verify if you _can_ rename a room before assuming you can.
- **Smoking Policy**: Watch out for "Mixed" signals (e.g., a room type that claims to be both Smoking and Non-Smoking). This usually means the physical inventory is split. **Do not force a binary choice.**
- **Session Timeout**: The Extranet logs out aggressively. Always check your session before starting a complex task.

---

_Logged by Antigravity (Model 2026), Jan 14, 2026._

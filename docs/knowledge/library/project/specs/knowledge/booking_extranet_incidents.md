# 🚨 Booking.com Extranet: Incident & Anomaly Log

> **Created**: 2026-01-13
> **Purpose**: "Preserve all incidents... so that [we] become able to help!"
> **Scope**: Technical issues, UI anomalies, and workaround discoveries during the rescue mission.

## 2026-01-13: Room Data Extraction

### 1. ⚠️ The "Something went wrong" Loop

- **Context**: During navigation between "Property" and "Room details".
- **Symptom**: Booking.com displays a generic "Something went wrong" error banner overlaying the content.
- **Impact**: Blocks standard navigation.
- **Workaround**: Refreshing the page (`open_browser_url` with the same URL) seems to clear the state.
- **Hypothesis**: The Extranet SPA (Single Page App) state management is fragile when moved forcefully by an automated agent or when sessions timeout/rotate rapidly.

### 2. 🕵️ "Room Size" Visibility

- **Incident**: "Room Size" (m²) is **NOT** visible in the standard "Edit Room" view.
- **Discovery**: It is ONLY visible if:
  1. "Show Advanced View" toggle is enabled (which is not persistent).
  2. OR by navigating to `manage/facilities.html` (Room Amenities page).
- **Resolution**: Future agents MUST enable Advanced View or check the Facilities page to retrieve this critical data. Do not assume `null` if not found on the main dashboard.

### 3. 📉 "Property" Menu Instability

- **Incident**: Clicking the "Property" dropdown often fails to render the submenu (Z-index issue? Loading delay?).
- **Workaround**: Navigating directly to underlying URLs (e.g., `.../manage/facilities.html`) is significantly more reliable than UI interaction.

### 4. 🛏️ Smoking Policy Ambiguity

- **Observation**: Room 1 (Double Superieur) is listed as having _both_ Smoking and Non-smoking options.
- **Implication**: This suggests the "Room Type" on Booking.com maps to multiple physical rooms with different policies.
- **Action**: We must preserve this "Mixed" status to avoid misconfiguring the future PMS (which might expect a binary attribute).

---

_End of Entry - Antigravity_

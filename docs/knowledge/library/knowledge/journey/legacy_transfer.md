# 🧠 Legacy Transfer: Lessons & Workflows

> **Created**: 2026-01-13
> **Context**: "Rescue Mission" — Pricing Update

## 🚨 Critical Constraints

### 1. Booking.com XML Lock

- **Insight**: We cannot manually update prices or inventory on `admin.booking.com`.
- **Reason**: The connection to **HotelRunner** (Channel Manager) locks these fields.
- **Protocol**: ALL price/inventory changes **MUST** be done via HotelRunner.
- **Workaround**: None found on Booking.com. Don't waste tokens trying to "find the button".

### 2. Room Naming & Mapping (Type vs Number)

- **Issue**: Owner prefers "Room 4" (Number) but Booking.com shows "Superior Double" (Type).
- **HotelRunner Capability**: **Negative**. HotelRunner Mapping is strictly ID-to-ID. It cannot push a "Display Name" or "Remote Name" to Booking.com.
- **Resolution Path**: Must be changed on Booking.com Extranet (Property > Room Details) or via Support.
- **Warning**: Even if renamed on Booking.com, HotelRunner might need a "Fetch Room Types" sync to reflect the change locally, but the _link_ is maintained by ID, so it shouldn't break the connection.

## 🛠️ Operational Workflows

### HotelRunner Bulk Update (Browser Agent)

**URL**: `https://villa-thaifa.hotelrunner.com/admin` -> **Initial Dashboard**

1. **Navigation**:
   - The "Calendar" dropdown is tricky.
   - **Direct Link**: `https://villa-thaifa.hotelrunner.com/admin/products/villa-thaifa/channel/prices/bulk_update`
   - _Note_: This link might be session/product-id specific. If 404, go to Dashboard -> My Property -> Bulk Updates.

2. **Execution**:
   - Select "Prices" checkbox.
   - Set Start/End Dates.
   - **Important**: The datepicker inputs (`#bulk_end_date_temp`) require explicit event triggering (`input`, `change`, `blur`) or jQuery datepicker calls (`.datepicker('setDate', ...)`) to register changes. React/Legacy JS mix.
   - Use the specific Room Type IDs found in the DOM (e.g., `v_1202181`) to map to room names.

3. **Room Mapping (2026)**:
   - `Double Supérieure`: 149€
   - `Deluxe Double`: 159€
   - `Triple Deluxe`: 169€
   - `Suite Exécutive`: 169€
   - `Deluxe King Suite`: 329€
   - `Suite`: 179€
   - `Family Suite`: 189€
   - `Presidential Suite`: 449€

## 🤖 Future Self Advice

- **Don't Trust the Extranet**: Just because you have credentials doesn't mean you have write access. Check for XML/Channel Manager connections immediately.
- **HotelRunner UI**: It's robust but uses older JS frameworks. Browser automation needs to be "noisy" with events (click, focus, blur, change) to ensure data sticks.

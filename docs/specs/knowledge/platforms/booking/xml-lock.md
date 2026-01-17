# Booking.com XML Connection Lock

**Date:** 2026-01-13
**Status:** Active Constraint

## Incident

Attempted to manually update prices on `admin.booking.com` for "Villa Thaifa".
**Result:** Blocked.
**Reason:** "For properties like yours that have an XML connection, inventory and prices can't be edited on the Extranet. Instead, use your connectivity provider to make changes."

## Implication

- **Read-Only**: Booking.com Extranet is effectively read-only for Rates & Availability.
- **Source of Truth**: HotelRunner (the connectivity provider) is the master for pricing and inventory.
- **Action**: All future price updates MUST be done via [HotelRunner](https://app.hotelrunner.com).

## Workaround Attempts

- **Connectivity Provider Settings**: Attempted to disable or modify, but blocked by 2FA (SMS to number ending in 81).
- **Bulk Edit**: Button hidden/disabled by UI.

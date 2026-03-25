# Scripts

Operational tools for Villa Thaifa data management and validation.

## Root Level

- **domain_verify.py** — Domain-level verification summary for Rooms (canonical file + reconciliation log).
- **validate_contracts.py** — Validate canonical markdown table contracts (rooms.md headers, columns, uniqueness).

## audit/

- **artifact_inventory.py** — Walks repository tree, classifies every file using artifact classification rules.
- **artifact_migrate.py** — Centralizes context files into the `context/` directory tree.
- **check_unique_info.py** — Checks if source markdown contains room-scoped values missing from canonical markdown.

## hotelrunner/

- **extract_reservations.py** — Extract daily reservations data from HotelRunner dashboard using browser automation.

## inventory/

- **export-ota.py** — Export room profiles to OTA-compatible CSV formats (Expedia, Booking.com).

## organization/

- **reorganize_room_images.py** — Organize and deduplicate room image files.

## structure/

- **generate_structure_cards.py** — Generate role-based structure cards for Villa Thaifa codebase from agent definitions and role mappings.
- **role_mappings.yaml** — Role mapping configuration for structure card generation.

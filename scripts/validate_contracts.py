#!/usr/bin/env python3
"""Validate canonical markdown table contracts (KISS v1).

Current scope:
- rooms canonical file
- required header columns
- minimum row count and unique room IDs
"""

from __future__ import annotations

from pathlib import Path
import re
import sys

ROOMS_PATH = Path("data/core/property/inventory/rooms/rooms.md")
REQUIRED_COLUMNS = [
    "Room ID",
    "Room Number",
    "Room Category Code",
    "Internal Name",
    "Expedia Type",
    "Booking.com Label",
    "Floor",
    "Capacity",
    "Max Occupancy",
    "Smoking Allowed",
    "Has Kitchen",
    "Size (m²)",
    "Base Rate (MAD)",
    "Base Rate (EUR)",
    "Beds",
    "View",
    "Access",
    "Access Notes",
    "Outdoor",
    "Bathroom",
    "Climate",
    "Layout",
    "Data Confidence",
    "Status",
]


def parse_table(md: str) -> tuple[list[str], list[list[str]]]:
    header_line = next((l for l in md.splitlines() if l.startswith("| Room ID")), None)
    if header_line is None:
        raise ValueError("Missing canonical header row starting with '| Room ID'.")
    headers = [c.strip() for c in header_line.split("|")[1:-1]]

    rows: list[list[str]] = []
    for line in md.splitlines():
        if line.startswith("| R") and not line.startswith("| Room ID"):
            cols = [c.strip() for c in line.split("|")[1:-1]]
            rows.append(cols)
    return headers, rows


def main() -> int:
    if not ROOMS_PATH.exists():
        print(f"ERROR: missing file: {ROOMS_PATH}")
        return 1

    md = ROOMS_PATH.read_text(encoding="utf-8")
    headers, rows = parse_table(md)

    missing_cols = [c for c in REQUIRED_COLUMNS if c not in headers]
    if missing_cols:
        print("ERROR: missing required columns:")
        for col in missing_cols:
            print(f"- {col}")
        return 1

    if len(rows) != 12:
        print(f"ERROR: expected 12 room rows, found {len(rows)}")
        return 1

    room_id_idx = headers.index("Room ID")
    ids = [r[room_id_idx] for r in rows]
    if len(set(ids)) != len(ids):
        print("ERROR: duplicate Room ID detected")
        return 1

    bad_ids = [rid for rid in ids if not re.fullmatch(r"R\d{2}", rid)]
    if bad_ids:
        print("ERROR: invalid Room ID format(s):")
        for rid in bad_ids:
            print(f"- {rid}")
        return 1

    print("OK: contracts validated for rooms.md")
    print(f"- columns: {len(headers)}")
    print(f"- rows: {len(rows)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())

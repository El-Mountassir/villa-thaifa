#!/usr/bin/env python3
"""Domain-level verification summary for Rooms (v1)."""

from __future__ import annotations

from pathlib import Path
import re
import sys

ROOMS_CANONICAL = Path("data/core/property/inventory/rooms/rooms.md")
ROOMS_RECON_LOG = Path("data/core/property/inventory/rooms/rooms-reconciliation-log.md")


def main() -> int:
    if not ROOMS_CANONICAL.exists():
        print("ERROR: missing canonical rooms.md")
        return 1
    if not ROOMS_RECON_LOG.exists():
        print("ERROR: missing rooms-reconciliation-log.md")
        return 1

    md = ROOMS_CANONICAL.read_text(encoding="utf-8")
    rows = [l for l in md.splitlines() if l.startswith("| R") and not l.startswith("| Room ID")]
    profile_count = len(re.findall(r"^### R\d{2} — ", md, flags=re.M))

    print("Rooms Domain Verify")
    print(f"- canonical file: {ROOMS_CANONICAL}")
    print(f"- room table rows: {len(rows)}")
    print(f"- profile sections: {profile_count}")
    print(f"- reconciliation log: {ROOMS_RECON_LOG}")

    if len(rows) != 12:
        print("ERROR: expected 12 room rows")
        return 1
    if profile_count != 12:
        print("ERROR: expected 12 room profiles")
        return 1

    print("OK: domain verification passed")
    return 0


if __name__ == "__main__":
    sys.exit(main())

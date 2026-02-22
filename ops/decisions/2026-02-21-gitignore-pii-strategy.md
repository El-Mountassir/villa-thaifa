# Decision: Gitignore Strategy for SQLite and PII Files

**Date:** 2026-02-20
**Context:** Issue [VT-43](https://linear.app/el-mountassir/issue/VT-43)
**Status:** Accepted

## Context

The working tree contains SQLite database files (e.g., `messages.db`, `whatsapp.db`) and other files containing Personally Identifiable Information (PII), such as booking and room exports in `csv` and `json` formats.
Without an explicit `.gitignore` policy covering these export directories, there is a risk of inadvertently committing guest communication data and other sensitive internal records to version control.

## Decision

We have added explicit exclusions in `.gitignore` for the directories known to stage SQLite and PII export files.

The following rules were added/verified:

- `*.db`, `*.sqlite`, `*.sqlite3` (Verified existing rule)
- `WhatsApp Chat*.md`, `WhatsApp Chat*.txt`, `*.vcard`, `*.vcf` (Verified existing rule)
- `data/bookings/exports/` (Added rule to block JSON/CSV export files)
- `data/bookings/requests/` (Added rule to block request files containing PII)
- `data/pending-domains/whatsapp/` (Added rule to block SQLite files and other WhatsApp dumps)
- `data/rooms/exports/` (Added rule to block CSV/JSON room pricing and booking listings)

## Rationale

- **Security:** Prevents PII (guest names, phone numbers from WhatsApp, booking details) from entering the git history.
- **Compliance:** Ensures compliance with fundamental data protection principles for guest information.
- **Safety Net:** Catch-all rules for extensions like `*.db` ensure that even if a database file is misplaced outside the named directories, it will not be committed.

## Consequences

- Developers and agents must ensure any necessary structure in these folders (like empty subdirectories) is either not required to be tracked, or tracked via `.gitkeep` files committed explicitly.
- Data exports must remain in these explicitly ignored directories.

# AI Session Starter (60s)

## 1) Read these first (in order)

1. `AGENTS.md`
2. `ROADMAP.md`
3. `ops/status/INDEX.md`
4. `ops/status/working.md`
5. `data/core/property/inventory/STATUS.md`

## 2) Non-negotiable rules

1. Treat unprocessed sources as contestable by default.
2. For ambiguity, ask Omar with options + one recommendation.
3. One sensitive file at a time.
4. Backup before mutation.
5. No deletion without reconciliation evidence.
6. No force operations on remote `main`.

## 3) Current truth snapshot

- Rooms domain is stabilized and canonical:
  - `data/core/property/inventory/rooms/rooms.md`
  - `data/core/property/inventory/rooms/rooms-reconciliation-log.md`
- Archived rooms legacy:
  - `archive/rooms/2026-02-13/rooms-3.md`
  - `archive/rooms/2026-02-13/rooms-4.md`
- Pending inventory domains:
  - `amenities.md`, `facilities.md`, `beds.md`, `inventory.md`

## 4) Where to put/update status

- Global ops board:
  - `ops/status/inbox.md`
  - `ops/status/working.md`
  - `ops/status/planned.md`
  - `ops/status/canonical.md`
  - `ops/status/archived.md`
- Intake queue:
  - `ops/intake/unprocessed/manifest.csv`
- Inventory domain state:
  - `data/core/property/inventory/status/*`

## 5) Branching / sync

- Active branch baseline: `bootstrap/2026-02-13-baseline`
- Remote baseline branch exists on GitHub.
- Remote `main` has independent history; integration is pending and must stay non-destructive.

## 6) Safe working loop

1. SCOUT
2. REPORT
3. QUESTIONS
4. ACTION
5. VERIFY (`make test` + relevant domain scripts)
6. LOG (status + reconciliation)

## 7) If blocked

- Record blocker in `ops/status/working.md`.
- Ask Omar with:
  - options (2-3)
  - recommended option
  - impact summary

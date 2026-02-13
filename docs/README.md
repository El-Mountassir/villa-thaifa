# docs/ — Navigation and Authority Map

This folder includes active operations docs, historical references, and drafts.
Use this file to avoid confusion.

## 1) Active Operational Docs (authoritative first)

- `docs/project/management/planning/`
- `docs/project/templates/`
- `docs/agents/instructions/`
- `docs/project/management/missions/` (queue/completed workflow context)
- `docs/content/active/`

## 2) Canonical Reference Docs (domain truth support)

- `docs/knowledge/property/specs/`
- selected files explicitly referenced by `AGENTS.md`, `ROADMAP.md`, and `ops/status/*`

## 3) Historical / Reference Archive (not auto-authoritative)

- `docs/reference/knowledge/library/`
- `docs/reference/agents/standards/`
- `docs/reference/knowledge/duplicates/`
- `docs/content/reference/`

These are valuable but potentially outdated or conflicting.
Treat as contestable unless promoted into active operational docs.

## 4) Backups (do not use as input)

- `docs/backups/`

Backup artifacts are retained for rollback only.
Never use them as canonical or planning input.

## 5) Draft / Unverified Docs

- `docs/drafts/client-admin/drafts/`
- `docs/content/pending/`

Never treat draft files as canonical input without explicit review.

## Usage Rule

When sources conflict:
1. prefer canonical data contracts and reconciliation logs
2. then active operational docs
3. then historical/reference docs
4. then drafts

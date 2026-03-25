```markdown
# Villa Thaifa Repository — Consolidation Audit

## Your Mission

You are performing a deep structural audit of the Villa Thaifa repository. Your goal: identify EVERYTHING that needs to be consolidated, regrouped, unified, cleaned up, or restructured. The repo manages a boutique hotel's operations but has accumulated significant structural debt across multiple migration waves.

You have a 1M context window. USE IT. Read every file. Don't sample, don't skim, don't infer from filenames. Read actual content.

## Repository Location

`/home/director/villa-thaifa`

## What This Repo Is

Villa Thaifa is a riad/boutique hotel in Marrakech. This repo is its operational data system — rooms, bookings, pricing, facilities, guest comms, platform integrations (HotelRunner, Booking.com). It serves as the canonical source of truth for AI agents and the hotel owner (Said Thaifa).

## Directory Contracts (What SHOULD Be)

Each top-level directory has a defined purpose:

| Directory | Purpose | What goes here | What does NOT go here |
|---|---|---|---|
| `data/` | Canonical source-of-truth | Room profiles, bookings, finance, property config, operational configs, facility data + images | Docs, audits, scripts, reference material |
| `docs/` | Operational documentation | Foundational defs (MISSION, PRINCIPLES, STRUCTURE), workflows, client/stakeholder info | Data, audits, reference material, scripts |
| `context/` | Read-only reference material | Architecture docs, planning docs, knowledge refs, templates, agent configs | Live operational state, canonical data, workflows |
| `ops/` | Live operational state | Audits, decisions, handoffs, status dashboards, intake items | Data, docs, reference material, scripts |
| `scripts/` | Validation and tooling | Scripts, automation, migration tools | Docs, data, operational artifacts |
| `archive/` | Global archive | Fully processed, completed, deprecated files | Active/live content |
| `tests/` | Test suite | pytest files | Production scripts, data |
| `infra/` | Infrastructure config | Docker, CI/CD, deployment | App code, data, docs |
| `src/` | Application source code | App code, libraries | Scripts, tests, data |

### data/ Subdirectories

| Subdir | Contents |
|---|---|
| `data/rooms/` | Per-room profiles (R01-R12/profile.md + images/), master table, amenities, beds |
| `data/bookings/` | Exports, requests, reservations |
| `data/finance/` | billing.json, rates.json |
| `data/operations/` | Operational config JSON files (channels, check-in, emergency, housekeeping, maintenance) |
| `data/property/` | Property-level config and facility data (descriptions + images) |
| `data/property/facilities/` | Per-facility directories with descriptions + images |
| `data/pending-domains/` | Domains not yet fully hardened |
| `data/admin/` | Client profiles, contact info |

### context/meta/ Subdirectories

| Subdir | Contents |
|---|---|
| `context/meta/architecture/` | System architecture docs |
| `context/meta/knowledge/` | Knowledge base articles, API references, platform guides |
| `context/meta/planning/` | Planning docs, briefs, strategies |
| `context/meta/templates/` | Templates for rooms, reports, etc. |
| `.agents/` | Agent-specific configs, guides, READMEs |

### ops/ Subdirectories

| Subdir | Contents |
|---|---|
| `ops/audit/` | Audit reports |
| `ops/decisions/` | Decision records (should have date prefixes) |
| `ops/handoff/` | Session handoff documents |
| `ops/status/` | Status dashboards, snapshots |
| `ops/intake/` | Unprocessed incoming items |
| `ops/archive/` | WARNING: Contains unprocessed historical legacies from past migrations |

## Audit Dimensions (10 Categories)

For EACH of these, identify every instance in the repo:

### 1. Misplaced Files
Files that violate the directory contracts above. Data in docs/, docs in context/, operational artifacts in wrong dirs, structured data in knowledge dirs, etc.

### 2. Scattered/Fragmented Domains
The same topic (e.g., spa, pricing, HotelRunner, Booking.com, rooms) split across 3+ locations. Map each domain and all its locations.

### 3. Duplicate/Overlapping Content
Files covering the same ground. Exact duplicates, near-duplicates, translations of each other, files that should be merged. Check file CONTENTS, not just names.

### 4. Naming Inconsistencies
Mixed naming conventions within the same directory level. Date formats, case styles, prefix patterns, image naming schemes.

### 5. Orphaned/Unreferenced Files
Files that don't belong to any clear structure, aren't referenced from any index or status file, and seem disconnected from the rest of the repo.

### 6. Stale/Outdated Content
Files with old dates, superseded content without notices, pricing that contradicts canonical rates.json, references to paths that no longer exist, broken cross-references.

### 7. Empty/Meaningless Directories
Directories with no real content. NOTE: empty taxonomy dirs (infra/, src/) are intentional scaffolds — those are fine. Flag dirs that SHOULD have content but don't.

### 8. ops/archive/ Legacy Assessment
This directory contains "unprocessed historical legacies from past migrations." Inventory every subdirectory, assess what's valuable vs truly archivable, identify anything that belongs elsewhere.

### 9. context/meta/ Sprawl
Known problem areas: knowledge/ (~20 files), planning/ (~14 files), templates/ (~15 files when only 4 are documented). Assess each file — does it belong here? Should it move? Is it stale?

### 10. Git Status Assessment
There are ~345 uncommitted changes. Assess what they represent — is this a half-finished migration? What needs to be committed vs reverted?

## Known Signals (Starting Points, NOT Complete)

These were identified in a preliminary scan. Use them as hints but DO YOUR OWN thorough exploration:

- Markdown files stored inside `images/` dirs (spa-hammam-reception/images/ has .md files)
- `data/admin/amenities-minibar-safe-analysis.md` is an analysis doc in a data dir
- `data/finance/promotions.md` is a session execution log, not financial data
- `context/meta/knowledge/rules.md` contains behavioral rules, not knowledge
- `context/meta/knowledge/channels_codes.csv` is structured data, not knowledge (and is duplicated in ops/archive/)
- `context/meta/sub-agent-registry.md` is a loose file at wrong level
- `ops/intake/IMG_20260126_0001.pdf` has no semantic name
- `.archived/` hidden directory at root is undocumented
- `CONTACT.md` at root is empty (0 bytes)
- `VERSION.txt` at root duplicates `context/meta/architecture/VERSION.md`
- `.playwright-cli/` directory is not gitignored
- Room images have 5 different naming conventions per room (_DSC, rXX-NN, photo-NN, WhatsApp, UUID)
- Facility dirs have inconsistent naming (hall/, pool-garden/, spa-hammam-reception/, services/)
- ops/decisions/ files lack date prefixes despite contract requiring them
- context/meta/templates/ has 15 files but only 4 are actual templates
- Guest testimonials exist in 2 locations
- ops/status/ has ~19+ files, many overlapping
- ops/archive/planning/ has 68 files including LHCM-OS content (explicitly doesn't belong in VT repo)
- data/pending-domains/facilities.md superseded notice points to now-deleted files
- Stale pricing in platform-mapping.md contradicts rates.json

## Output Requirements

### Format

Write your COMPLETE findings to a file. Structure it as:

1. **Executive Summary** (10 lines max) — overall health assessment
2. **Per-Dimension Findings** (dimensions 1-10) — for EACH issue:
   - File path(s)
   - What's wrong (which contract violated, what's inconsistent)
   - Suggested fix (consolidate to X, merge with Y, archive, delete)
3. **Domain Consolidation Map** — for each scattered domain, the target unified location
4. **Priority Matrix** — P0 (blocking/breaking), P1 (important), P2 (should fix), P3 (nice to have)
5. **Proposed Consolidation Plan** — phased approach to clean up

### Output File

Write findings to: `/home/director/villa-thaifa/tmp/gemini-repo-audit-findings.md`

### Important Notes

- Be SPECIFIC. File paths, line numbers where relevant, exact content comparisons.
- Don't just list problems — propose specific solutions for each one.
- Group related issues together (e.g., all HotelRunner fragmentation under one heading).
- If two files seem like duplicates, actually READ both and confirm.
- When you find stale content, note what the current correct value should be (check rates.json, truth.md, etc.).
- This audit may take multiple passes. Be thorough in this pass and note areas that need deeper investigation.
```
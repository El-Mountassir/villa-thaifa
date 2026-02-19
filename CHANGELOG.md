# Changelog

All notable changes to this workspace will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com).

## [Unreleased]

### Added

- add automated changelog generation via git-cliff — - Install git-cliff 2.12.0 for Conventional Commits → Keep a Changelog
- migrate 14 Villa Thaifa files from ~/omar/ with contract-compliant paths — Audited and migrated VT-specific content from ~/omar/ to this repo:
- complete agent team with 7 new specialized agents — - Add incident-reporter (orange): structured error documentation
- add property type investigation mission + scout report — - Created mission to investigate Booking.com property type (Hotel vs Maison d'Hôtes)
- add claude-md-agent for CLAUDE.md maintenance — Expert agent for governance updates with:
- add governance rules for git, confidence, and AskUserQuestion — - Add Git Workflow section with commit/push discipline

### Changed

- repo restructure — relocate archives to docs/, add structure documentation system — - Relocate archive/2025/Q4/ content to docs/reports/, docs/briefs/, docs/changelogs/
- session closeout — archive expired missions, update CHANGELOG — - Archive 2 expired missions (Dec 2025 reservations, dates long passed)
- cleanup deprecated agents and standards — Remove deprecated agents and standards that are now managed at collective level.
- reorganize project structure + add mandatory archive policy — Structure reorganization (CLAUDE.md externalization initiative):
- simplify workflow to unified CORE LOOP — - Archive fragmented rules, workflows, patterns to .archived/
- Phase 6 — audit + final placement fixes — - Full migration placement audit (436 files scanned, 13 violations found)
- Phase 5 — enforce ops/ subdirectory placement + data cleanup — Move all loose ops/ root files to correct subdirectories per AGENTS.md:
- Phase 3 — archive MANIFEST.md, update docs/README.md, gitignore tmp/logs — - Archive outdated docs/MANIFEST.md → ops/archive/2026-01/photo-manifest.md
- Phase 2 — consolidate audit artifacts from context/ to ops/ — - Move context/audit/history/ → ops/audit/archive/history/ (18 files)
- Phase 1 — move agent docs, facility images, decisions to correct dirs — - Split docs/agents/ → context/agents/ (reference) + ops/ (operational)
- complete Phase A data consolidation — dedup profiles, update paths — - Deduplicate all 12 room profiles (R01-R12): removed exact duplicate
- data consolidation Phase A + Gemini workflow standardization — Data consolidation (recovered from broken session 017eb935):
- reorganize repo — move foundational docs to docs/core/ — - Move MISSION.md and STRUCTURE.md to docs/core/ alongside PRINCIPLES.md
- second-round brutal audit remediation — 14 findings fixed — Phase 1: Formats & Naming
- tier 1+2 audit remediation — 12 findings fixed — Tier 1 (Structure):
- final cleanup — remove backups, dedup context, tidy ops — - Remove config/ from AGENTS.md structure tree (dir no longer exists)
- flatten agents + consolidate client docs
- centralize 291 context files + cleanup
- preserve open loops and isolate docs content lanes
- isolate duplicate stakeholders set from active knowledge paths
- remove legacy finance paths after pending isolation
- isolate pending finance files and refresh intake tracking
- physically isolate reference and draft zones
- physically isolate pending files and room backups
- bootstrap baseline workspace governance and inventory controls

### Documentation

- fix markdown lint warnings in handoff, regenerate changelog
- add session handoff for Linear audit + file triage — - Handoff for next villa-thaifa session: audit 41 stale VT issues,
- add structure freshness rule and commit step to mandatory workflow — - AGENTS.md: Add step 5 (COMMIT) to mandatory workflow sequence
- update CHANGELOG with session work — Linear decision, migration audit, placement fixes, handoff preparation.
- add Linear migration preparation handoff — Linear approved as primary backlog tool (score 8.675 vs GitHub Issues 7.225).
- session closeout — update handoffs, remove stale open loops — - Remove completed SCM branch merge from AGENTS.md open loops
- define product deliverables for client (Said Thaifa) — Comprehensive deliverables document covering:
- update sync investigation report — 🤖 Generated with [Claude Code](https://claude.com/claude-code)
- add decision-evaluator agent pattern note — Pattern identified during credential management evaluation.
- Phase 4 — rewrite AGENTS.md and STRUCTURE.md for crystal-clear navigation — - Add File Placement Decision Tree: flowchart for where any file belongs
- add full migration audit to handoff open items — Facility images were missed — need exhaustive audit before declaring
- update handoff — facility images decision (move to data/)
- update handoff — facilities audit, remove handled items
- add handoff for Gemini standardization session — Session artifacts: model delegation rule, skill updates, Google AI Pro
- add 60-second AI session starter
- add holistic roadmap and decouple docs/data status indexes
- update git sync note for post-bootstrap divergence handling
- lock contestability policy and full-depth isolation status

### Fixed

- remove stale docs/agents/ references from AGENTS.md and STRUCTURE.md — Agent docs live in context/agents/ (reference) and ops/ (operational).



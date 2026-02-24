# Changelog

All notable changes to this workspace will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com).

## [Unreleased]

### Added

- room image migration + facilities restructure + archive cleanup — - Rename room images R01-R11 to canonical rXX-NN.jpg format
- room schema governance + safe/minibar data + price fixes — - Add Room Schema Change Protocol to AGENTS.md (template-first rule)
- scout Booking.com admin extranet — terrain map, room sizes, session learnings — - Admin extranet scouted via Playwright CLI (2FA + CAPTCHA documented)
- add SYNC workflow step + Linear issues intake + MCP routing fix — - AGENTS.md: add SYNC checklist as step 5 of mandatory workflow
- scrape Booking.com 2026-02-21 — update scores, facilities, resolve 7 Said items — - Review count: 80 → 86 (+6 reviews)
- integrate MoSCoW+Eisenhower priority system (P0-P5) + AGENTS.md work-overview reference — - Add Priority System section (matrix + legend) to work-overview.md and template
- add Cascade Update rule + consolidate VT app vision + commit policy ACT — - universal.md: new Cascade Update rule (grep before declaring data edit done)
- add json-render evaluation decision + VT app vision seed — json-render REJECTED (1/10 after spec fix — renderer broken).
- add PROJECT-CONTRACT.md + comprehensive work-overview.md — - PROJECT-CONTRACT.md: agent output paths, platform conventions, data flow rules
- consolidate Said questions (57 items) + DRY enforcement + data fixes — - Create said-pending-questions.md: single registry of all 57 pending Said items
- enrich property-config.json with location data from external sources — - GPS confirmed (Google Maps, more precise: 31.6539756, -7.8778661)
- rename 160 spec images with descriptive names and normalized directories — - 14 subdirectories renamed to lowercase/hyphenated convention
- VT-46 triage (185 files archived), Google Maps data, image visual review — - VT-46: Triage 212 files — 27 KEEP, 185 ARCHIVED across 3 directories
- G2-G15 fixes, data/specs migration, old repo refs, Said checklist — - Migrate data/specs/ non-image files (36 archived to ops/archive/data-specs/)
- Wave 3 follow-up — OTA titles, contract update, archive missions + reports — - Translate 12 room booking_label fields to English, add booking_label_fr
- Wave 3 — translate 8 French files to English, process manifest.csv
- add automated changelog generation via git-cliff — - Install git-cliff 2.12.0 for Conventional Commits → Keep a Changelog
- migrate 14 Villa Thaifa files from ~/omar/ with contract-compliant paths — Audited and migrated VT-specific content from ~/omar/ to this repo:
- complete agent team with 7 new specialized agents — - Add incident-reporter (orange): structured error documentation
- add property type investigation mission + scout report — - Created mission to investigate Booking.com property type (Hotel vs Maison d'Hôtes)
- add claude-md-agent for CLAUDE.md maintenance — Expert agent for governance updates with:
- add governance rules for git, confidence, and AskUserQuestion — - Add Git Workflow section with commit/push discipline

### Changed

- migrate project identity from docs/core/ to project/ — Establishes project/ as the project constitution directory, separating
- update changelog after Vague B consolidation
- archive remaining stale ops/status/snapshots/ — Move 8 remaining snapshot files from ops/status/snapshots/ to
- triage context/meta/knowledge/ — relocate 19 of 22 files to correct directories — - rules.md → context/agents/hotelrunner/ (platform ops rules, agent-facing, HR/BC specific)
- expand agent tool lists + minor hotelrunner archive fix — - auditor: add Edit, Bash, Glob, Grep (was Read, Write only)
- add session ID to work-overview for resume
- commit accumulated content updates across docs, data, and context — Batch of previously uncommitted changes: stakeholder profiles, facility
- standardize browser-agent to generic global pattern with project context — Browser-agent.md now auto-discovers project-specific context from
- move Linear docs to ~/omar/, add blocker labels, elevate linear-agent — - Move linear-workflow.md and linear-github-setup.md to ~/omar/protocols/
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

- close VT-54, final handoff with session summary before compaction
- final session update — handoff Phase 3 complete, 23 issues Done
- fix handoff Phase 3 status, optimize readability with tables — - Correct Phase 3 from COMPLETED to IN PROGRESS (triage not done)
- update handoff with Wave 2 completion and pending manual actions
- update migration checklist and handoff with cleanup progress
- add execution roadmap to handoff for next session — Replace completed Phase 1-3 task graph with 5-wave execution roadmap
- add Capture Before Archive protocol to handoff triage instructions — Prevents archiving files without extracting actionable content first.
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

- merge .archived/ into archive/, move LHCM-OS files, redact credentials — - Merge .archived/ into archive/2025/ (strategy doc + 3 workflows preserved, 2 superseded files deleted)
- Vague A consolidation — misplaced files, duplicates, stale notices — - Add .playwright-cli/ to .gitignore
- R06 YAML rate 179→169 EUR + data format evaluation + delete superseded inventory — - Fix R06/profile.md YAML: base_rate_eur 179→169, base_rate_mad 1919→1812 (confirmed via Said)
- close 3 AGENTS.md gaps — stale counts, Said file roles, PROJECT-CONTRACT ref — - Open Loops: update file counts (54→19, 96→14, 62→3), clarify facilities.md status
- resolve 11 Said items + pets policy (C1) + enrich work-overview with Linear fields — - Mark 11 Said pending items as RESOLVED in Resolution Log (from repo cross-reference)
- correct room prices in rates.json + add truth.md SSOT file — Prices confirmed via HotelRunner deployment (2026-01-13) + Booking.com sync.
- fix 181 stale path references across 54 files (data/specs/ and data/core/ → canonical) — All remaining data/specs/ and data/core/ references replaced with current
- complete repo consolidation phase 4 — relocate docs/, archive legacy, fix snapshots — - Relocate 27 misplaced docs/ files to correct dirs per AGENTS.md contract
- repo consolidation phases 1-3 + partial phase 4 — Phase 1 — Defuse landmines:
- mark all room rates CONFIRMED + locked until Dec 2026 — - rates.json: add locked_until and lock_source fields
- remove 53 verified duplicate images, consolidate credential eval — - Remove 45 DSC7296-7319 duplicates from R05-R09 (MD5 verified vs R04)
- sync room rates, merge Said's notes, add validation gap tracking — - G1: Fix rate mismatches in R02/R04/R05/R06 profiles (align with rates.json)
- remove stale docs/agents/ references from AGENTS.md and STRUCTURE.md — Agent docs live in context/agents/ (reference) and ops/ (operational).

### Ops

- complete Wave 1-2, execute GitHub migration to El-Mountassir org — Wave 1 (P1 blockers):
- complete Linear audit Phase 3 — 14 new VT issues, 209-file triage — Phase 3 scan + triage completed:
- complete Linear audit Phase 1-2 — close 15 stale VT issues, update handoff — Phase 1 (Unblock): Closed VT-26 P0 blocker, identified repo alignment issue.

### Security

- remove tracked passwords, harden gitignore for PII — - Remove WhatsApp chat containing 4 plaintext passwords from git tracking



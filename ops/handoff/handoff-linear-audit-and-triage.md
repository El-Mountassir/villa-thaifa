# Session Handoff: Linear Audit + File Triage

**Created**: 2026-02-19 | **Workspace**: `~/villa-thaifa/` | **Priority**: High

---

## Quick Navigation

| Section                                                      | Status                             |
| ------------------------------------------------------------ | ---------------------------------- |
| [Latest Session (2026-02-21)](#latest-session-2026-02-21)   | 10 work items completed            |
| [Context](#context)                                          | Background + Linear state snapshot |
| [Phase 1: Unblock](#phase-1-unblock--completed)              | COMPLETED                          |
| [Phase 2: Audit](#phase-2-audit--completed)                  | COMPLETED                          |
| [Phase 3: Scan + Triage](#phase-3-scan--triage--completed)   | COMPLETED                          |
| [Rules Updated](#rules-updated-this-session)                 | 4 files updated                    |
| [Execution Roadmap](#execution-roadmap--next-sessions)       | Waves 1-5 + Deferred               |
| [Omar Manual Actions](#omar-manual-actions--pending)         | Pending                            |
| [Triage Reports](#triage-reports-from-phase-3)               | /tmp/ — ephemeral                  |
| [Key Files](#key-files)                                      | Reference links                    |
| [Completion Status](#completion-status)                      | Post-audit Linear state            |

---

## Latest Session (2026-02-21)

**Status**: 10 work items completed | 1 commit

### Work Completed

| # | Item | Linear | Type | Outcome |
| - | ---- | ------ | ---- | ------- |
| 1 | VT-42 closed | VT-42 | Decision | Branch linking research complete. Linear has NO sidebar feature. Issue sync works correctly. Closed as Done. Research: `~/omar/knowledge/research/development/vt-42-branch-linking-online-research.md` |
| 2 | VT-77 decomposed | VT-77 | Planning | 22 TODOs audited, split into 4 focused issues: VT-78/79/80/81. All Said-blocked except VT-81 (Omar). |
| 3 | Linear labels created | VT-46 | Operations | 3 labels created: "Awaiting: Said" (15 issues), "Awaiting: Omar" (6 issues), "Ready" (24 issues). All 46 open issues labeled. |
| 4 | Linear agent elevated | VT-46 | Infrastructure | Custom `linear-agent.md` created with label management + stale triage. Moved to `~/omar/core/tools/agents/` with symlinks (global + project). Enables delegation pattern. |
| 5 | Linear docs migrated | VT-46 | Refactoring | `linear-workflow.md` and `linear-github-setup.md` moved from villa-thaifa to `~/omar/operational/productivity/protocols/`. 5 files updated for references. |
| 6 | Orchestrator rule added | VT-46 | Governance | ALL Linear ops → linear-agent delegated. Added to CLAUDE.md + mcp-memory. Enforces zero-MCP pattern. |
| 7 | Expedia Step 3 extracted | — | Research | Partner Central policies (VAT risk identified: 10% on top, potential double-charge). Data captured. French questions: `~/omar/artifacts/reports/expedia-etape3-questions-fr.md` |
| 8 | Expedia Step 4 extracted | — | Research | Amenities: 115 checkboxes, 12 modules, exhaustive capture. Report: `~/omar/knowledge/research/business/expedia-step4-extraction.md` |
| 9 | Expedia Step 5 analyzed | — | Research | Rooms & rates: EMPTY — zero rooms configured. Blocks steps 6-12. Cross-ref report: `~/omar/knowledge/research/business/expedia-data-crossref-report.md` |
| 10 | Browser agent plan decided | — | Design | Keep global browser.md, add auto-discovery rule, externalize VT content. NOT YET EXECUTED. |

### Key Artifacts Created

| File | Purpose |
| ---- | ------- |
| `~/omar/knowledge/research/development/vt-42-branch-linking-online-research.md` | Research findings: Linear limitation |
| `~/omar/knowledge/research/business/expedia-extraction-protocol.md` | Extraction protocol for Steps 3-12 |
| `~/omar/knowledge/research/business/expedia-step4-extraction.md` | Amenities data (115 checkboxes, 12 modules) |
| `~/omar/knowledge/research/business/expedia-step5-extraction.md` | Rooms & rates analysis (zero rooms issue) |
| `~/omar/knowledge/research/business/expedia-data-crossref-report.md` | Cross-reference analysis |
| `~/omar/artifacts/reports/expedia-etape3-questions-fr.md` | French questions for Omar re: Step 3 VAT |
| `~/omar/core/tools/agents/linear-agent.md` | Custom linear-agent (canonical, symlinked) |

### Commits

- `3f9a879`: chore: move Linear docs, add labels, elevate linear-agent

### Pending / Next Session

| Item | Blocker | Status |
| ---- | ------- | ------ |
| #112: Create VT PROJECT-CONTRACT.md | #114 (template) | Blocked |
| #113: Create ~/omar/ PROJECT-CONTRACT.md | #114 (template) | Blocked |
| #116: Merge browser-agent.md | Design phase only | Not executed |
| #104-110: Expedia Steps 6-12 | Rooms not configured (Step 5) | Blocked |
| Expedia Step 3 French questions | Omar response | Awaiting |
| VT-78/79/80/81 | Said input | Awaiting |
| Said validation checklist | Said input | Awaiting at `data/admin/said-data-validation-checklist.md` |

---

## Context

The villa-thaifa codebase underwent massive restructuring (200+ files relocated, directory contract established, structure documentation system added, 14 files migrated from ~/omar/). Linear issues created before this restructuring are likely stale.

**Current Linear state (as of 2026-02-19):**

| Item                          | State                                                                                 |
| ----------------------------- | ------------------------------------------------------------------------------------- |
| VT projects                   | 4: Room Management, Q1 2026 Operations, OTA Integration, SSOT Migration (all Backlog) |
| Total issues                  | 41: 36 Backlog, 6 Done, 1 In Progress                                                 |
| GitHub integration            | NOT active                                                                            |
| VT-26 (P0 Architecture Audit) | Likely completed by recent restructuring                                              |
| VT-19 (Anniversary event)     | 19 days overdue                                                                       |
| VT-40, VT-41                  | Just created this session (Logo design, Resume ops)                                   |

---

## Progress (2026-02-19 Session)

### Phase 1: Unblock — COMPLETED

| Issue / Item              | Action                     | Outcome                                                                                               |
| ------------------------- | -------------------------- | ----------------------------------------------------------------------------------------------------- |
| Linear-GitHub integration | Investigated current state | Already active; repo alignment mismatch found — filed to `ops/intake/linear-github-repo-alignment.md` |
| VT-26 P0 blocker          | Closed as Done             | Architecture audit complete via Safe Harbor + Feb restructuring; 6 downstream issues unblocked        |
| Linear MCP tools          | Documented working pattern | Orchestrator calls only (not sub-agents); persisted in MEMORY.md                                      |

### Phase 2: Audit — COMPLETED

**15 issues closed** (41 → 26 remaining):

| Category  | Issues                                                                     | Count |
| --------- | -------------------------------------------------------------------------- | ----- |
| Done      | VT-15, VT-28, VT-29, VT-41                                                 | 4     |
| Cancelled | VT-14, VT-16, VT-17, VT-18, VT-19, VT-20, VT-2, VT-30, VT-31, VT-32, VT-33 | 11    |

**Other actions:**

| Item                      | Outcome                                                       |
| ------------------------- | ------------------------------------------------------------- |
| VT-2 merged into VT-9     | Sub-issues VT-3→8 re-parented                                 |
| SSOT Migration project    | All 4 issues closed as obsolete                               |
| Anniversary event         | Cancelled by Said; all 5 issues closed                        |
| VT-22 (agent brief)       | Kept open — partially done is NOT done                        |
| Completion Integrity rule | Added to universal.md                                         |
| Delegation Thresholds     | Strengthened in rules.md (zero tolerance)                     |
| Dashboard                 | `~/omar/artifacts/dashboards/vt-linear-audit-2026-02-19.html` |

### Phase 3: Scan + Triage — COMPLETED

**Scans (3a):** 4 parallel scans completed:

| Source                | Items Found | Topics                                                        |
| --------------------- | ----------- | ------------------------------------------------------------- |
| AGENTS.md Open Loops  | 2           | facilities hardening, 212-file triage                         |
| ops/intake/           | 25+         | GitHub strategy, migration conflicts, manifest CSV            |
| ops/handoff/          | 13          | repo alignment, language audit, archive lifecycle, governance |
| data/pending-domains/ | 2           | facilities.md, WhatsApp DBs                                   |

**Triage (3b):** 3 directories triaged (209 files total):

| Directory               | Total   | KEEP   | ARCHIVE | NEEDS-EXTRACTION |
| ----------------------- | ------- | ------ | ------- | ---------------- |
| context/meta/knowledge/ | 51      | 28     | 21      | 2                |
| context/meta/planning/  | 96      | 29     | 53      | 14               |
| ops/audit/quality/      | 62      | 18     | 38      | 6                |
| **Total**               | **209** | **75** | **112** | **22**           |

**Linear issues created (3c):** 14 new issues (VT-42 through VT-55):

| Batch   | Priority | Issues                                                                                                                                                          |
| ------- | -------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Batch 1 | P1       | VT-42 (GitHub integration fix), VT-43 (gitignore/PII strategy), VT-44 (hook E2E test)                                                                           |
| Batch 2 | P2       | VT-45 (facilities hardening), VT-46 (212-file triage), VT-47 (repath 10 docs), VT-48 (language audit), VT-49 (data/ migration audit), VT-50 (manifest CSV processing) |
| Batch 3 | P3       | VT-51 (GitHub identity strategy), VT-52 (Said profile consolidation), VT-53 (communications.md review), VT-54 (TTS decision), VT-55 (archive old repo)          |

**Deferred items (6):** Not yet promoted to Linear issues:

| Item                            | Reason                    |
| ------------------------------- | ------------------------- |
| Stale GitHub issues migration   | After VT-42               |
| Old repo archive strategy       | After VT-51               |
| ~/omar/ repo strategy           | Strategic decision needed |
| WhatsApp domain work            | After VT-43               |
| Archive/lifecycle system design | Strategic session         |
| WOS architecture                | Strategic session         |

**Skipped items (3):**

| Item                         | Reason                    |
| ---------------------------- | ------------------------- |
| Create ops/archive/sessions/ | ACT-tier — do it directly |
| Resume project               | Stale                     |
| GitHub template repos        | Blocked                   |

**Phase 3 artifacts:**

| Artifact                      | Path                                                                |
| ----------------------------- | ------------------------------------------------------------------- |
| Triage report — knowledge     | `/tmp/triage-context-meta-knowledge.md`                             |
| Triage report — planning      | `/tmp/triage-context-meta-planning.md`                              |
| Triage report — audit quality | `/tmp/triage-ops-audit-quality.md`                                  |
| Scan evaluation               | `/tmp/scan-items-evaluation.md`                                     |
| Dashboard                     | `~/omar/artifacts/dashboards/vt-scan-consolidation-2026-02-19.html` |

### Rules Updated This Session

| File                                                              | Change                                                          |
| ----------------------------------------------------------------- | --------------------------------------------------------------- |
| `~/.claude/rules/rules.md`                                        | Delegation Thresholds rewritten with zero-tolerance enforcement |
| `~/omar/core/resources/rules/universal.md`                        | Completion Integrity rule added                                 |
| `~/.claude/skills/delegate/SKILL.md`                              | Gemini-from-Claude-Code pattern documented                      |
| `~/.claude/projects/-home-director-villa-thaifa/memory/MEMORY.md` | Gemini delegation pattern added                                 |

### New Files Created

| File                                                                            | Purpose                       |
| ------------------------------------------------------------------------------- | ----------------------------- |
| `ops/intake/linear-github-repo-alignment.md`                                    | Repo naming mismatch problem  |
| `~/omar/artifacts/dashboards/vt-linear-audit-2026-02-19.html`                   | Audit dashboard               |
| `~/omar/knowledge/research/business/vt-linear-audit-verification-2026-02-19.md` | Verification report (pending) |

---

## Execution Roadmap — Next Sessions

### Dependency Chain

```
VT-42 (GitHub integration fix)
  └── VT-55 (archive old repo) [blocked]
  └── enables GitHub ↔ Linear sync for all future work

VT-43 (gitignore/PII strategy)
  └── unblocks WhatsApp domain work (deferred SCAN-08)

VT-51 (GitHub identity strategy)
  └── VT-55 (archive old repo) [blocked]

VT-44 (hook E2E test) — independent, can run anytime
```

### Recommended Execution Sequence

| Wave                    | Issue | Description                     | Priority | Effort | Status          | Notes                                                                                                                                                                                                           |
| ----------------------- | ----- | ------------------------------- | -------- | ------ | --------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Wave 1 — Blockers**   | VT-42 | Fix Linear GitHub integration   | P1       | 2pts   | **DONE**        | Investigation done; manual UI fix required by Omar. Report: `~/omar/knowledge/research/development/vt-42-github-integration-investigation.md`                                                                   |
|                         | VT-43 | Define gitignore strategy       | P1       | 2pts   | **DONE**        | .gitignore hardened, WhatsApp chat untracked. **URGENT: Omar must rotate 4 exposed passwords** (HotelRunner, Booking.com x2, OVH). Report: `~/omar/knowledge/research/development/vt-43-gitignore-pii-audit.md` |
|                         | VT-44 | E2E test delegation hooks       | P1       | 2pts   | **DONE**        | 4/4 tests passed; closed in Linear                                                                                                                                                                              |
| **Wave 2 — Quick Wins** | VT-52 | Consolidate Said profile        | P2       | 2pts   | **DONE**        | Canonical: `data/admin/client/PROFILE.md`                                                                                                                                                                       |
|                         | VT-53 | Review communications.md        | P2       | 2pts   | **DONE**        | Archived to `ops/archive/2026-02/`                                                                                                                                                                              |
|                         | VT-51 | GitHub identity strategy        | P2       | 2pts   | **DONE**        | Option B (migrate to org) executed same session                                                                                                                                                                 |
| **Wave 3 — Deep Work**  | VT-47 | Move 10 misplaced docs          | P2       | 4pts   | **Done**        | All 10 docs already correct, no moves needed                                                                                                                                                                    |
|                         | VT-48 | Language audit — French removal | P2       | 8pts   | **In Progress** | 8 files translated, OTA titles done. ~80 historical exempt. Said comms exempt.                                                                                                                                  |
|                         | VT-49 | Post-bootstrap migration audit  | P2       | 8pts   | **In Progress** | Audit complete. missions/ archived (5 issues VT-66-70). docs/reports/ deduped. data/ migration plan ready.                                                                                                          |
|                         | VT-50 | Process manifest.csv            | P2       | 4pts   | **Done**        | 7 issues created (VT-59-65). CSV archived.                                                                                                                                                                      |
| **Wave 4 — Epics**      | VT-45 | Harden facilities domain        | P2       | 8pts   | Backlog         | needs Said input                                                                                                                                                                                                |
|                         | VT-46 | Phase 3 triage — 212 files      | P2       | 16pts  | **Done**        | 185 files archived, credential eval consolidated                                                                                                                                                                |
|                         | VT-55 | Archive old repo                | P3       | 1pt    | Blocked         | blocked by VT-51 (now done — unblocked)                                                                                                                                                                         |
| **Wave 5 — Decisions**  | VT-54 | TTS provider decision           | P3       | 2pts   | **Done**        | Piper default since 2026-02-17. ElevenLabs exhausted.                                                                                                                                                           |
| **Deferred**            | —     | Migrate stale GitHub issues     | —        | —      | Deferred        | after VT-42                                                                                                                                                                                                     |
|                         | —     | WhatsApp domain work            | —        | —      | Deferred        | after VT-43                                                                                                                                                                                                     |
|                         | —     | Archive/Lifecycle system design | —        | —      | Deferred        | strategic session                                                                                                                                                                                               |
|                         | —     | Governance templates decision   | —        | —      | Deferred        | needs /decide                                                                                                                                                                                                   |
|                         | —     | WOS Architecture                | —        | —      | Deferred        | strategic session                                                                                                                                                                                               |

**GitHub Migration — EXECUTED (2026-02-19)**:

| Item                   | Result                                                                |
| ---------------------- | --------------------------------------------------------------------- |
| Repo transfer          | `omar-elmountassir/villa-thaifa` → `El-Mountassir/villa-thaifa`       |
| Old repo               | Archived: `El-Mountassir/villa-thaifa-property-management`            |
| Git remote             | Updated locally                                                       |
| Linear integration     | VT team correctly linked; issue sync working; branch linking untested |
| GitHub issues migrated | VT-56 (MarocPME form), VT-57 (website elements)                       |
| Remaining cleanup      | `ops/decisions/github-migration-to-org.md` § Cleanup Remaining        |

### Omar Manual Actions — PENDING

| Action                            | Status    | Notes                                                                                                                             |
| --------------------------------- | --------- | --------------------------------------------------------------------------------------------------------------------------------- |
| Test branch linking               | Pending   | Push a branch referencing a NEW VT issue (not VT-42 — GitHub #2 conflict prevents auto-linking). Format: `omar/vt-XX-description` |
| Verify Linear branch auto-linking | Pending   | Confirm it works on a clean issue                                                                                                 |
| Full migration checklist          | Reference | `ops/decisions/github-migration-to-org.md`                                                                                        |

### Task Graph Instructions for Next Instance

The next session MUST:

1. Read this handoff document first
2. Create atomic tasks via TaskCreate for the wave being worked on
3. Set up blockedBy dependencies between tasks
4. Mark tasks in_progress before starting, completed when done
5. Delegate ALL execution to sub-agents (orchestrator = 0 MCP calls, 0 file writes for non-rules content)
6. Update this handoff at end of session

### Wave 3 Execution — IN PROGRESS

**Work completed earlier in sub-session:**

| Item                        | Source | Action Taken                                                        | Outcome                                                                          |
| --------------------------- | ------ | ------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| OTA title translation       | VT-48  | Translated R01-R12 booking_label to English, added booking_label_fr | 12 rooms updated                                                                 |
| Expand directory contract   | VT-49  | Updated AGENTS.md + STRUCTURE.md to include infra/ + src/           | Directory contract expanded                                                      |
| Archive missions/           | VT-49  | Capture Before Archive — extracted to Linear, then archived         | 5 issues created (VT-66-70), dir archived                                        |
| Dedup docs/reports/         | VT-49  | Compared vs ops/audit/, rescued unique files                        | 40 dupes archived, 2 unique rescued                                              |
| Scope data/ migration | VT-49  | Analyzed 196 files, produced migration plan                         | Plan at ~/omar/knowledge/research/development/vt-49-data-specs-migration-plan.md |

**Work completed this sub-session (Wave 3 follow-up):**

| Item                               | Issue    | Description                                                      | Status | Outcome                                         |
| ---------------------------------- | -------- | ---------------------------------------------------------------- | ------ | ----------------------------------------------- |
| Fix G1 rate mismatches             | VT-49    | Sync R02/R04/R05/R06 profile rates with rates.json               | Done   | 4 rooms corrected, MAD rates also fixed         |
| Update rates.json from HotelRunner | VT-49    | Capture confirmed pricing for all 12 rooms                       | Done   | Decision recorded in ops/decisions/             |
| Deprecation notice rooms.md        | VT-49    | Add SSOT notice pointing to R01-R12/profile.md                   | Done   | Read-only summary                               |
| Merge chambre_et_vue.md            | VT-49    | Extract Said's notes into R03/R06/R07 profiles + property-config | Done   | Terrace sizes, spa policy added                 |
| Image copy error investigation     | VT-49    | MD5 verify R05-R09 duplicates of R04 images                      | Done   | 45 duplicate files confirmed                    |
| Validation PDF completeness audit  | VT-48/49 | Check all fields from original sign-off template                 | Done   | 15 gaps found (G1-G15), 7 Linear issues created |
| Create Linear issues for gaps      | VT-48/49 | G2-G15 tracked as VT-71 through VT-77                            | Done   | 7 issues in backlog                             |

**Work completed this sub-session (latest):**

| Item | Issue | Description | Status | Outcome |
| ---- | ----- | ----------- | ------ | ------- |
| Rename 160 spec images | #85 | Renamed 14 dirs + 160 files to lowercase/hyphenated convention | Done | Commit 5c5d19c — r01-r11, pool-garden, spa-hammam, hall |
| VT-42 branch linking guide | VT-42 | Gemini researched Linear GitHub branch linking fix | Done | Guide at ~/omar/knowledge/research/development/vt-42-github-branch-linking-guide.md |
| Browser investigation VT-42 | VT-42 | Browser agent diagnosed root cause: branch prefix mismatch (omar ≠ omar-elmountassir) | Done | Webhook confirmed working (200 OK). Root cause: username prefix. |
| Option C applied + tested | VT-42 | Omar changed Linear format to identifier-title. Test branch vt-42-test-option-c pushed. | Testing | Branch pushed, awaiting confirmed link on VT-42. Clean up test branch after. |
| VT-42 deep investigation | VT-42 | Browser + Gemini + researcher: full investigation of branch auto-linking | Done | Root cause: "Branches" sidebar feature doesn't work despite correct config. Issue sync (commits/PR titles) works fine. Tested: Option C format change, lowercase/uppercase branches, Draft PR — none triggered sidebar. Recommendation: close as "good enough" or escalate to Linear support. |
| Image rename committed | #85 | 160 images + 14 dirs renamed, committed 5c5d19c | Done | Pushed to main |
| ---------------------------------- | -------- | ---------------------------------------------------------------- | ------ | ----------------------------------------------- |
| Fix G1 rate mismatches             | VT-49    | Sync R02/R04/R05/R06 profile rates with rates.json               | Done   | 4 rooms corrected, MAD rates also fixed         |
| Update rates.json from HotelRunner | VT-49    | Capture confirmed pricing for all 12 rooms                       | Done   | Decision recorded in ops/decisions/             |
| Deprecation notice rooms.md        | VT-49    | Add SSOT notice pointing to R01-R12/profile.md                   | Done   | Read-only summary                               |
| Merge chambre_et_vue.md            | VT-49    | Extract Said's notes into R03/R06/R07 profiles + property-config | Done   | Terrace sizes, spa policy added                 |
| Image copy error investigation     | VT-49    | MD5 verify R05-R09 duplicates of R04 images                      | Done   | 45 duplicate files confirmed                    |
| Validation PDF completeness audit  | VT-48/49 | Check all fields from original sign-off template                 | Done   | 15 gaps found (G1-G15), 7 Linear issues created |
| Create Linear issues for gaps      | VT-48/49 | G2-G15 tracked as VT-71 through VT-77                            | Done   | 7 issues in backlog                             |

| data/ migration | VT-49 | 36 .md files archived, 160 images left for rename | Done | ops/archive/2026-02/ |
| Old repo ref cleanup | VT-55 | 3 active files updated to El-Mountassir/villa-thaifa | Done | cliff.toml, linear-workflow, linear-github-setup |
| Fix R01/R06 sizes | G7-G8 | Align header sizes with YAML values | Done | R01: 44m², R06: 40m² (owner_pending) |
| Fix R07 sofa beds | G4 | Align header with YAML: 2 sofa beds | Done | VT-73 closed |
| Research property config | G10-G15 | Address, GPS, ratings, check-in times from web | Done | property-config.json updated |
| Populate facility files | G2 | Extract data from specs, OTA, Said's notes | Done | 4 files populated, Said gaps remain |
| Said validation checklist | G3+G5-G9 | Consolidated all owner_pending fields | Done | data/admin/said-data-validation-checklist.md |
| Remove 53 duplicate images | VT-49 | MD5 verified, visual confirmed, git rm | Done | R05-R09 DSC + R05 photos |
| Consolidate credential eval | VT-46 | Merged archived copy, removed duplicate | Done | Single canonical in knowledge/ |
| Google Maps data | G10-G15 | Address, GPS, 4.5 rating, phone, parking, WiFi, airport | Done | property-config.json |
| Branch linking test | VT-42 | Tested on Done + Backlog issues — NOT working | Open | Issue sync works, branch linking doesn't |

**New Linear issues this sub-session**: VT-59-65 (from manifest.csv), VT-66-70 (from missions/ extraction), VT-71-77 (validation gaps)

**Pending decisions (from missions/ archive)**:

- chambre5-sync-investigation: Dec 2025 P0 sync problem — dates expired but root cause unclear
- validation-pdf: French sign-off doc for Said — still needed or obsolete?
- rooms.md deprecation: Should master table get deprecation notice pointing to R01-R12 profiles?

**Pending decisions (from data/ migration scoping)**:

- R7/R12 premium pricing: Were decisions made? (440€ vs 280€ for R7, 600€ vs 350€ for R12)
- Image anomaly: R05-R09 share R04 image filenames — intentional or copy error?
- chambre_et_vue.md extraction: 12 lines of Said's notes on room views/terrace/spa not in profiles
- HDR originals: Verify specs images are genuinely same as canonical (not different resolutions)

**Remaining Wave 3 work (tracked in Linear)**:

- VT-48: Close once OTA title translation confirmed (~80 historical files exempt, Said comms exempt)
- VT-49: Execute data/ migration (~85 min after Omar answers 4 questions above). Close after migration done.
- Migration plan reference: `~/omar/knowledge/research/development/vt-49-data-specs-migration-plan.md`

### Session Summary (2026-02-19, continued)

**Commits this session**:

- `6ff9e25` fix handoff Phase 3 status, optimize readability with tables
- `2a567d4` Wave 3 — translate 8 French files, process manifest.csv
- `97acbad` Wave 3 follow-up — OTA titles, contract update, archive missions + reports
- `70e5dcf` sync room rates, merge Said's notes, add validation gap tracking
- `1410c50` G2-G15 fixes, data/specs migration, old repo refs, Said checklist
- `5d344f1` VT-46 triage (185 files archived), Google Maps data, image visual review
- `eb9c9b5` remove 53 verified duplicate images, consolidate credential eval
- `d1a4d16` final session update — Phase 3 complete
- `31be9a9` mark all room rates CONFIRMED + locked until Dec 2026
- `5c5d19c` feat: rename 160 spec images with descriptive names and normalized directories

**Linear issues closed this session**: VT-44, VT-46, VT-47, VT-48, VT-49, VT-50, VT-52, VT-53, VT-54, VT-55, VT-73, VT-75 (12 total)
**Linear issues created this session**: VT-56-58, VT-59-65, VT-66-70, VT-71-77 (20 total)

**Remaining open work**:

| Item                      | Linear | Status   | Blocker                                               |
| ------------------------- | ------ | -------- | ----------------------------------------------------- |
| Branch linking fix        | VT-42  | Investigated — Decision Pending | Omar: close as good-enough (issue sync works) or escalate to Linear support. Research: ~/omar/knowledge/research/development/vt-42-branch-linking-deep-research.md |
| Facility files completion | VT-71  | Partial  | Said: dimensions, capacity, hours                     |
| Room sizes confirmation   | VT-72  | Pending  | Said: physical measurements                           |
| Terrace size conflicts    | VT-74  | Pending  | Said: on-site verification                            |
| Floor assignments         | VT-76  | Pending  | Said: R04/R10 floor confirmation                      |
| property-config TODOs     | VT-77  | Partial  | Mixed: some researchable, some Said                   |
| Facilities hardening      | VT-45  | Pending  | Said meeting                                          |
| Image rename (160 files)  | #85    | Done     | Commit 5c5d19c                                        |

**Key artifacts**:

- Said validation checklist: `data/admin/said-data-validation-checklist.md`
- Triage report: `~/omar/knowledge/research/development/vt-46-triage-report.md`
- Migration plan: `~/omar/knowledge/research/development/vt-49-data-specs-migration-plan.md`
- Image investigation: `~/omar/knowledge/research/development/vt-49-image-copy-investigation.md`
- Validation audit: `~/omar/knowledge/research/development/validation-pdf-completeness-audit.md`

---

### Triage Reports (from Phase 3)

These `/tmp/` files are EPHEMERAL — lost on reboot:

| File                                    | Contents                                     |
| --------------------------------------- | -------------------------------------------- |
| `/tmp/triage-context-meta-knowledge.md` | 51 files: 28 keep, 21 archive, 2 extraction  |
| `/tmp/triage-context-meta-planning.md`  | 96 files: 29 keep, 53 archive, 14 extraction |
| `/tmp/triage-ops-audit-quality.md`      | 62 files: 18 keep, 38 archive, 6 extraction  |
| `/tmp/scan-items-evaluation.md`         | 23 items evaluated, 14 promoted              |

**CRITICAL**: If `/tmp/` files are gone, VT-46 (triage epic) will need to re-run the triage agents. File categorizations are also captured in the VT-46 issue description.

---

## Key Files

| File                                                                | Purpose                                           |
| ------------------------------------------------------------------- | ------------------------------------------------- |
| `AGENTS.md`                                                         | Directory contract + open loops                   |
| `ops/intake/migration-conflict-check.md`                            | Migration audit from this session                 |
| `ops/intake/migration-path-validation.md`                           | Path compliance audit                             |
| `~/omar/operational/productivity/protocols/linear-workflow.md`       | Linear workflow conventions                       |
| `ops/handoff/handoff-linear-migration-preparation.md`               | Prior Linear session handoff                      |
| `/tmp/scan-items-evaluation.md`                                     | Scan evaluation — ephemeral                       |
| `/tmp/triage-*.md`                                                  | Triage reports — ephemeral (lost on reboot)       |
| `~/omar/artifacts/dashboards/vt-scan-consolidation-2026-02-19.html` | Scan dashboard                                    |
| `~/omar/artifacts/dashboards/vt-linear-audit-2026-02-19.html`       | Audit dashboard                                   |
| `~/.claude/rules/rules.md`                                          | Rules updated: zero-tolerance delegation, 0 MCP   |
| `~/omar/core/resources/rules/universal.md`                          | Universal rules: Completion Integrity, Task-First |
| `~/.claude/skills/delegate/SKILL.md`                                | Delegate skill: timeout guide, retry protocol     |

---

## Entry Command

```bash
# Quick state check
cd ~/villa-thaifa && git status && git log --oneline -5

# Check Linear backlog
# (delegate to sub-agent — orchestrator does NOT call MCP tools)

# Check if triage reports survived reboot
ls /tmp/triage-*.md /tmp/scan-items-evaluation.md 2>/dev/null || echo "Triage reports lost — VT-46 needs re-triage"
```

---

## Completion Status

**Phases 1 & 2 COMPLETED; Phase 3 COMPLETED** as of 2026-02-19. VT-46 done (185 files archived). 53 duplicate images removed. VT-42 remains open (branch linking broken). G3/G5-G6/G9: Said validation checklist created, awaiting Said.

### Linear State Post-Audit

| Metric                      | Count  | Notes                                                                                                                              |
| --------------------------- | ------ | ---------------------------------------------------------------------------------------------------------------------------------- |
| Total VT issues             | ~77    | Was 57; +VT-59-65 (manifest.csv), +VT-66-70 (missions/ extraction), +VT-71-77 (validation gaps) = 19 new this sub-session          |
| Done                        | ~24    | +VT-46, VT-49, VT-54, VT-55, VT-73, VT-75 closed this round; +VT-48 from earlier; VT-71/72/74/76/77 partially done (awaiting Said) |
| Canceled                    | 11     | —                                                                                                                                  |
| Backlog                     | ~49    | VT-48, VT-49 in progress; remainder backlog                                                                                        |
| New issues this session     | 16     | VT-42→VT-55 (14) + VT-56, VT-57 from GitHub migration                                                                              |
| New issues this sub-session | 19     | VT-59-65 (manifest.csv), VT-66-70 (missions/ extraction), VT-71-77 (validation gaps)                                               |
| SSOT Migration project      | Closed | All 4 issues closed as obsolete                                                                                                    |

### Remaining Work (tracked in Linear)

| Issue       | Description                | Priority |
| ----------- | -------------------------- | -------- |
| VT-42       | Fix GitHub integration     | P1       |
| VT-43       | Gitignore/PII strategy     | P1       |
| VT-44       | Hook E2E testing           | P1       |
| VT-47–VT-55 | 9 issues at P2-P3 priority | P2–P3    |

### Rules Updated This Session

| File             | Changes                                                                   |
| ---------------- | ------------------------------------------------------------------------- |
| `rules.md`       | Delegation Thresholds rewritten (zero tolerance), Linear MCP cap          |
| `universal.md`   | Completion Integrity, Task-First Execution, Prompt-to-Task Pipeline added |
| `delegate skill` | Timeout guide + retry protocol added                                      |
| `MEMORY.md`      | Post-audit state, Gemini delegation pattern, Linear spelling anti-pattern |

### This Handoff File

This file can be ARCHIVED after Omar confirms all phases are satisfactory. Follow Capture Before Archive protocol — extract any remaining actionable items to Linear before archiving.

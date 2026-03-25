# ops/archive/planning/ Inventory

**Total files:** 100
**Assessed:** 2026-02-22
**Method:** First 15-20 lines read per file, grep for LHCM-OS indicators where ambiguous.

---

## LHCM-OS (should move to ~/omar/professional/projects/lhcm-os/)

Files that explicitly define, describe, or plan the LHCM-OS product vision — content that belongs to the broader platform, not Villa Thaifa operations specifically.

- `lhcm-os-strategy-execution-plan-v0.1.0.md` — Primary LHCM-OS document. Full strategy & execution plan for the "Luxury Hospitality Cognitive Management - Operating System" product. Named explicitly. Defines the three-person founding team (Najib/Omar/Said), the VT-to-platform roadmap, and the "Digital C-Suite" concept. 29K words.
- `villa-thaifa-internal-app-requirements-v0.1.0.md` — Requirements for the internal app that is explicitly framed as "Foundation for LHCM-OS Platform." Subtitle is "Villa Thaifa pilot → Will evolve into LHCM-OS Platform." Contains LHCM-OS vision section and cross-references the strategy doc.
- `villa-thaifa-workstream-master-v0.1.0.md` — Master workstream coordination doc. Has explicit "Secondary Goal: Build LHCM-OS platform (scale to other Moroccan properties)" and LHCM-OS Vision section pointing to the 29K-word strategy doc. Hybrid (VT + LHCM-OS), but primary strategic content is LHCM-OS.

**LHCM-OS count: 3**

---

## VT-Specific (keep in VT repo)

Files that are exclusively about Villa Thaifa operations, room data, OTA management, HotelRunner, bookings, or Said Thaifa client work.

**Operational missions & task records:**

- `2025-12-23-thaifa-booking-data.md` — Mission to extract room data from Booking.com for VT.
- `2025-12-23-thaifa-image-organization.md` — Mission to organize VT room images.
- `2025-12-23-thaifa-room-restructuring.md` — Mission for VT room-centric repo restructuring.
- `2025-12-23-thaifa-validation-pdf.md` — Mission to create validation PDF for Said.
- `2025-12-28-thaifa-chambre4-gouram.md` — VT booking mission: Room 4 Gouram reservation.
- `2025-12-28-thaifa-chambre5-sync-investigation.md` — VT investigation: Room 5 sync desync between HotelRunner and Booking.com.
- `2025-12-28-thaifa-hotelrunner-api-scout.md` — VT mission: Scout HotelRunner Developer API for automation.
- `2025-12-29-thaifa-hotelrunner-admin-access.md` — VT mission: Obtain admin HotelRunner access for Omar.
- `2026-01-08-thaifa-property-type-investigation.md` — VT mission: Investigate property type on Booking.com (hotel vs. guesthouse).
- `2026-01-13-room-mapping-investigation.md` — VT implementation plan: Booking.com room mapping safety investigation.
- `2026-01-24-extend-pricing-2026.md` — VT operational record: Extension of Said's pricing grid through end of 2026.
- `2026-01-24-stop-sell-mars.md` — VT operational record: Stop-sell for the whole villa March 8-12 2026.
- `2026-01-28-expedia-tax-correction.md` — VT letter: Tax rate correction request to Expedia for VT property ID 114807934.
- `2026-02-13-next-7-days.md` — VT execution plan: 7-day sprint for rooms/amenities/facilities domains.
- `2026-02-14-room-modularization.md` — VT plan: Modularizing the monolithic rooms.md file.
- `FICHE-MISSION-OMAR-29-JANVIER.md` — VT mission sheet: Anniversary event inquiry (30 people, May 2026).
- `ROOM_DATA_SHEET_FOR_SAID.md` — VT data collection sheet for Said: golden records for 12 rooms.
- `mission-ota-progressive.md` — VT mission: Progressive OTA onboarding (deadline Jan 12, 2026).
- `onboarding_capture_v1.md` — VT data capture: Expedia onboarding steps 1-4 for VT property.
- `implementation_plan_expedia.md` — VT plan: Expedia onboarding via browser automation.
- `developer_onboarding_guide.md` — VT guide: How to obtain Expedia Connectivity API access for VT.
- `amenities_gap_analysis.md` — VT analysis: Expedia amenities gap analysis (infinity pool, hammam) for VT.
- `amenities_gap_analysis_FR.md` — Same as above in French.
- `amenities_recommendation.md` — VT recommendation: Expedia amenities list for VT property.
- `amenities_recommendation_FR.md` — Same as above in French.
- `jisr-mokawala-investigation-2025-12.md` — VT-focused investigation of the Moroccan government Jisr platform in context of Villa Thaifa's OTA dependency problem.
- `hotelrunner-poc-2025-12-19.md` — Original French brain dump: first HotelRunner proof-of-concept for VT (room 11 booking urgency).
- `hotelrunner-poc-2025-12-19-en.md` — English translation of the same brain dump.
- `REPRISE-APRES-MIGRATION.md` — VT session handoff: state of work after Pop!\_OS 24.04 migration (HotelRunner integrations, browser automation, 96 reservations extracted). VT-specific context.
- `FICHE-MISSION-OMAR-29-JANVIER.md` — (already listed above)
- `management-briefs-2025-12-22-hws-introduction.md` — VT project brief: full brief on Villa Thaifa mission context (Said Thaifa, HotelRunner, OTA platforms). Dated 2025-12-22.
- `2025-12-22-hws-introduction.md` — English version of the same brief (different filename, same content).
- `project-briefs-2025-12-22-hws-introduction.md` — Third copy/variant of the same Dec 22 brief. All three are VT-specific.
- `villa-thaifa-client-brief-v0.2.0.md` — VT client brief v0.2.0: business context, stakeholders (Said, Najib), objectives. Primarily VT-focused; mentions LHCM as Omar's consulting company name, not the product.
- `villa-thaifa-project-brief-v0.2.0.md` — VT project execution brief v0.2.0: technical guide for agents executing OTA Phase 1.
- `villa-thaifa-brief.md` — English translation/variant of project-BRIEF.md.
- `villa-thaifa-overview.md` — VT project overview: 12 rooms, Palmeraie, HotelRunner, Booking.com.
- `villa-thaifa-quick-start-v0.1.0.md` — VT migration guide: how to import VT context into a new Claude.ai project.
- `villa-thaifa-decisions-log-v0.1.0.md` — VT decisions log: records architectural decisions for VT.
- `villa-thaifa-open-questions-v0.1.0.md` — VT open questions: unresolved questions for VT project (B/T/O/F categories).
- `villa-thaifa-deliverables.md` — VT deliverables doc: defines final deliverables for Said Thaifa's digital transformation.
- `villa-thaifa-todos-historical.md` — Historical VT task list (Dec 2025). English version of TODOs.md.
- `ROOM_DATA_SHEET_FOR_SAID.md` — (already listed above)
- `property-db-migration.md` — VT data: SQLite property.db extraction summary (12 rooms, 22 beds, 94 amenities).
- `DATA-INVENTORY.md` — VT data inventory: room data sources, facilities, finance, photos. Conflict map for VT audit (EM-191).
- `CONFLICT-MAP.md` — VT conflict map: EUR vs MAD currency conflicts across VT data sources (EM-191).
- `CONSOLIDATION-PLAN.md` — VT consolidation plan: data migration plan for VT canonical sources (EM-191).
- `audit-REQUIREMENTS.md` — VT requirements: dual currency, single source of truth, OTA compatibility for VT (EM-191).
- `ARCHITECTURE-PROPOSAL.md` — VT architecture proposal: single source of truth for VT room data (EM-191).
- `HANDOFF-EM-191.md` — VT handoff: EM-191 codebase architecture audit status (Phase 1 complete).
- `audit_tracker.md` — VT artifact audit tracker: systematic analysis of VT repository.
- `comprehensive_work_log.md` — VT work log: documents 2+ months of VT R&D, specifications, process discovery.
- `scope_audit.md` — VT engagement audit: role gap analysis (agentic engineer vs. operational factotum) for VT project.
- `pms-data-migration-strategy.md` — VT data migration: from old VT repo (1.1GB, 1435 files) to new repo. VT-specific inventory (12 rooms, 96 reservations, 382 docs).
- `pms-roadmap.md` — VT PMS roadmap: Phase 0-4 plan for Villa Thaifa Property Management System build.
- `ROADMAP.md` — VT roadmap: v1 operational stability phases (HotelRunner pricing, room mapping, data architecture).
- `STATE.md` — VT state snapshot: Phase 1 progress, plan 1 of 4.
- `planning-REQUIREMENTS.md` — VT requirements v1: operational requirements (OPS-01 through OPS-04) for VT.
- `INTEGRATIONS.md` — VT integrations analysis: HotelRunner API, Booking.com, Expedia for VT (analysis dated 2026-01-30).
- `CONCERNS.md` — VT codebase concerns: security issues (hardcoded credentials in .env), data conflicts for VT.
- `CREDENTIALS.md` — VT credentials guide: how agents access platform credentials for VT.
- `ANALYSIS-ARCHITECTURE.md` — VT architecture analysis: hybrid Next.js app (public website + admin dashboard) for VT.
- `ARCHITECTURE.md` — VT architecture: Next.js 16+ App Router, SQLite, Zod schema for VT (analysis 2026-01-30).
- `STACK.md` — VT tech stack: TypeScript, Next.js, SQLite, Node.js for VT (analysis 2026-01-30).
- `CONVENTIONS.md` — VT coding conventions: naming patterns, file structure for VT codebase.
- `TESTING.md` — VT testing: no test framework configured (analysis 2026-01-30).
- `NEXT_STEPS.md` — VT next steps: UX/UI improvements roadmap for VT public website.

**VT-specific count: 56**

---

## General/Ambiguous (needs Omar decision)

Files that originated from the VT context but concern Omar's workspace governance, AI tooling, or methodology that has since been generalized to ~/omar/ — or files that are VT-branded but contain reusable patterns.

**Workspace & governance (now lives in ~/omar/):**

- `2026-01-08-claude-md-externalization.md` — Alignment doc on externalizing CLAUDE.md into pointer files. VT-branded but addresses Omar's cross-CLI workspace structure — now superseded by current ~/omar/ setup.
- `2026-01-08-core-loop-simplification.md` — Plan to archive fragmentation and simplify Claude workflow. Addresses ~/.claude/ structure. Now part of Omar's global workspace, not VT-specific.
- `2026-01-08-document-evaluation.md` — Self-evaluation of the claude-md-externalization doc. Meta-document about Omar's planning process, not VT operations.
- `unified-workspace-governance.md` — Implementation plan for unified agentic workspace with GitHub Issues, verification, and artifact management. Now superseded by current AGENTS.md/rules.md system.
- `workspace.md` — Old workspace rules for .agents/ directory structure. Superseded by current AGENTS.md/directory contract.
- `workspace-standardization-plan.md` — Dual-track transformation plan: Workspace Excellence + Owner Platform. Contains both VT operational work and meta-workspace planning. Mentions "Platform ready to transform Morocco's boutique hospitality sector" — bridges VT and broader vision.
- `git.md` — Git workflow rules for all agents (branch creation, commit standards). Now superseded by current rules.md.
- `git-branching-strategy.md` — Implementation plan for git branching in multi-agent workflow. Now superseded by current workflow.
- `rules-README.md` — Short table of key rules (Resilience, Anti-Dodge, SSOT, STOP & ASK). Precursor to current rules.md.
- `verification.md` — Verification and testing rules for agents. Now part of current rules.md/AGENTS.md.
- `missions-README.md` — README for the missions/ system (drafts/, queue/, active/, archive/). Old task system, now superseded by Linear.
- `tasks-README.md` — Task prioritization system (MoSCoW + Eisenhower matrix). Superseded by Linear.
- `TODOs.md` — Old VT task list (Dec 2025, French). Superseded by Linear.
- `specs-README.md` — Old placeholder README for specs/ directory. Superseded.

**Planning methodology & historical context:**

- `active.md` — Old documentation optimization task list (phases 1-1.6). Historical record of early repo structuring work.
- `01-01-PLAN.md` — Structured execution plan (phase 01-01) for photo organization. Old planning format, no longer in use.
- `01-01-SUMMARY.md` — Subsystem summary for phase 01-01. Same old format.
- `01-02-PLAN.md` — Phase 01-02 plan (pricing configuration, room 12 photos). Old planning format.
- `01-RESEARCH.md` — Phase 1 research doc: HotelRunner automation, photo management. Old format, VT content.
- `gemini-lux-action-plan.md` — Plan to use Gemini 3 Pro + Lux (old Claude.ai model) for VT analysis. References old tooling/workflow, historical.
- `generate-structure-map.md` — Plan to generate STRUCTURE.md using tree command. Historical, already done.
- `repository_tree.md` — Snapshot of old VT repo tree from early 2026. Historical reference.
- `villa-thaifa-structure-v5.md` — Old proposed directory structure v5 for VT. Superseded by current structure.
- `villa-thaifa-migration-plan-v0.1.0.md` — Migration plan from claude.ai to Nexus + Vibe Kanban (old tooling). Historical, superseded.
- `project-BRIEF.md` — VT project brief (French, session 2026-01-08). Largely duplicates villa-thaifa-brief.md and villa-thaifa-project-brief-v0.2.0.md.

**Vision & strategy (mixed VT + broader):**

- `ROADMAP-2.md` — VT roadmap v2 with explicit "Système réplicable pour 10+ établissements" north star. Mixed: VT milestone plan + multi-property vision.
- `comprehensive-transformation-plan.md` — Dual-track plan (Workspace Excellence + Owner Platform). Mentions 1,500+ riads, Morocco market. Bridges VT and LHCM-OS.
- `2026-02-13-agentic-kiss-transformation-plan.md` — VT-specific KISS transformation plan (digital OS for VT). Explicitly scoped to VT.
- `strategic_reframing.md` — Reframing VT "debris" as foundation assets. Explicitly mentions LHCM-OS but analyzes VT engagement. Decision: VT audit artifact that references LHCM-OS.
- `vision_2026.md` — 2026 transformation plan: "Morocco's first AI-powered owner business platform," targets 1,500+ riads. Clear LHCM-OS-level ambition, VT as pilot.
- `VISION-DRAFT.md` — Vision draft for VT property management platform. Scoped to VT but frames it as a platform seed.
- `VISION-ENRICHED.md` — Enriched vision: VT 4-star guesthouse in Palmeraie. Mixed: VT property details + platform vision elements.
- `scope_audit.md` — Already in VT list above. (Actually VT-specific.)

**Other:**

- `hotelrunner-poc-2025-12-19-en.md` — (already in VT list — English translation of the French brain dump)

**General/Ambiguous count: 31**

---

## Summary

| Category                                                | Count   |
| ------------------------------------------------------- | ------- |
| LHCM-OS (move to ~/omar/professional/projects/lhcm-os/) | 3       |
| VT-Specific (keep in VT repo)                           | 56      |
| General/Ambiguous (needs Omar decision)                 | 31      |
| **Total**                                               | **100** |

---

## Notes for Omar

**On LHCM-OS (3 files):** These are clearly out-of-place. `lhcm-os-strategy-execution-plan-v0.1.0.md` is the core document — 29K words defining the product. The two companion files frame VT as a pilot for that product. These should move to `~/omar/professional/projects/lhcm-os/`.

**On General/Ambiguous (31 files):** Most fall into 3 sub-groups:

1. **Superseded workspace governance** (git.md, workspace.md, rules-README.md, etc.) — content now absorbed into current rules.md/AGENTS.md. Safe to archive or delete if confirmed.
2. **Old planning format artifacts** (01-01-PLAN.md, 01-RESEARCH.md, etc.) — VT history, no active value.
3. **Vision documents with mixed scope** (ROADMAP-2.md, comprehensive-transformation-plan.md, vision_2026.md) — contain both VT milestones AND multi-property platform ambition. Omar must decide: keep in VT as historical context, or split/move the platform-level content to lhcm-os/.

**Credentials warning:** `CREDENTIALS.md` and `hotelrunner-poc-2025-12-19.md` / `-en.md` contain plaintext credentials for HotelRunner and Booking.com. These are in an archived directory but still in the repo. CONCERNS.md also references that the original `.env` had hardcoded passwords. Worth flagging separately.

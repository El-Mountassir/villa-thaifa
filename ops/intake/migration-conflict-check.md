# Migration Conflict Check

**Date**: 2026-02-19
**Purpose**: Audit 18 proposed migration target paths for (1) existence at target, (2) redundant content elsewhere in repo, (3) source file presence in ~/omar/.
**Scope**: Proposed target paths only — path compliance analysis is in `ops/intake/migration-path-validation.md`.

---

## Summary Table

| # | Target Path | Status | Notes |
|---|---|---|---|
| 1 | `docs/planning/pms-roadmap.md` | CLEAR | Target dir does not exist. No equivalent in repo. |
| 2 | `docs/planning/data-inventory.md` | REDUNDANT | Overlaps `context/meta/planning/DATA-INVENTORY.md` (different scope, different source) |
| 3 | `docs/planning/delegation-framework.md` | CLEAR | No equivalent found in repo. |
| 4 | `docs/planning/tech-decisions.md` | CLEAR | No equivalent found in repo. |
| 5 | `docs/planning/sessions/2026-02-13-session-capture.md` | CLEAR | No equivalent found in repo. |
| 6 | `docs/research/existing-app-audit.md` | CLEAR | Not at target. Lightweight reference in `ops/intake/migration-path-validation.md` only. |
| 7 | `docs/research/missing-yaml-investigation.md` | CLEAR | Not at target. No equivalent in repo. |
| 8 | `docs/research/yaml-backup-search.md` | CLEAR | Not at target. No equivalent in repo. |
| 9 | `docs/research/repo-strategy-decision.md` | CLEAR | Not at target. No equivalent in repo. |
| 10 | `docs/research/consolidation-app-eval.md` | CLEAR | Not at target. No equivalent in repo. |
| 11 | `docs/client/said-thaifa.md` | REDUNDANT | `docs/client/stakeholders.md` already contains a Said Thaifa profile section. |
| 12 | `docs/client/communications.md` | CLEAR | Not at target. No equivalent in repo. |
| 13 | `docs/integrations/whatsapp-mcp-setup.md` | CLEAR | Target dir does not exist. No equivalent in repo. |
| 14 | `data/whatsapp/messages.db` | CLEAR | Target dir does not exist. No binary equivalent in repo. |
| 15 | `data/whatsapp/whatsapp.db` | CLEAR | Target dir does not exist. No binary equivalent in repo. |
| 16 | `docs/integrations/whatsapp-context.md` | CLEAR | Target dir does not exist. No equivalent in repo. |
| 17 | `docs/backlog/logo-design.md` | CLEAR | Target dir does not exist. No equivalent file in repo. |
| 18 | `docs/backlog/resume-project.md` | CLEAR | Target dir does not exist. No equivalent file in repo. |

---

## Detailed Findings

### 1. `docs/planning/pms-roadmap.md`

**Source**: `~/omar/specs/plans/villa-thaifa-pms/README.md`
**Status**: CLEAR

- `docs/planning/` does not exist in the repo.
- No file in the repo covers the PMS 4-phase roadmap (Prerequisites → Phase 0–4, 38-day plan).
- Source exists and is substantive (phases, blockers, tech stack, context).

---

### 2. `docs/planning/data-inventory.md`

**Source**: `~/omar/specs/plans/villa-thaifa-pms/data-inventory.md`
**Status**: REDUNDANT — different scope, not a conflict, but overlapping topic

- `docs/planning/` does not exist in the repo.
- **Existing file**: `context/meta/planning/DATA-INVENTORY.md` (created 2026-01-30, Linear EM-191)
- **Scope difference**:
  - Existing `DATA-INVENTORY.md`: Audits the current villa-thaifa repo (rooms.yaml, property.db, facilities, finance, photos). Covers 9 categories, status per category. Focused on WHAT EXISTS NOW.
  - Source `data-inventory.md`: Migration strategy for the NEW repo (villa-thaifa-pms). What to migrate (5%), what to skip, migration effort estimates. Focused on WHAT TO MOVE.
- **Conclusion**: These are complementary, not redundant. The naming creates confusion but the content is distinct. The incoming file covers migration strategy; the existing file covers current-state audit.
- **Action**: If migrated, choose a name that disambiguates — e.g., `pms-data-migration-strategy.md`.

---

### 3. `docs/planning/delegation-framework.md`

**Source**: `~/omar/specs/plans/villa-thaifa-pms/delegation-framework.md`
**Status**: CLEAR

- `docs/planning/` does not exist in the repo.
- No equivalent found. Searched for "delegation", "multi-model", "routing matrix", "CLI arsenal" across the repo — found mentions in `CHANGELOG.md` and `docs/client/stakeholders.md` only (passing references, not a framework).
- Source is a full multi-model delegation routing matrix (Claude Code, Codex CLI, Gemini CLI, Kilo CLI) specific to Villa Thaifa PMS. Unique content.

---

### 4. `docs/planning/tech-decisions.md`

**Source**: `~/omar/specs/plans/villa-thaifa-pms/tech-decisions.md`
**Status**: CLEAR

- `docs/planning/` does not exist in the repo.
- Searched for "next.js", "vercel", "tech stack", "nextauth", "shadcn" in `docs/` — only `docs/project/BRIEF.md` and `docs/client/stakeholders.md` reference these, but at a very high level.
- Source is a full decision rationale document with comparison tables (Next.js vs. Vite+React+FastAPI). Unique content.
- **Note**: `ops/decisions/` already has `2026-02-16-database-architecture.md`, `hotelrunner-decision-brief.md`, and `repo-organization-decision.md`. This belongs there (per path validation).

---

### 5. `docs/planning/sessions/2026-02-13-session-capture.md`

**Source**: `~/omar/specs/plans/villa-thaifa-pms/sessions/2026-02-13-session-capture.md`
**Status**: CLEAR

- Neither `docs/planning/` nor `docs/planning/sessions/` exist in the repo.
- Searched for "session capture", "2026-02-13", "d3c50344" — no matches in the repo.
- Source is a session transcript with prerequisites checklist, 6 research files produced, 5 open questions resolved, and blockers for next session. Unique content.
- `ops/archive/` already exists. `ops/archive/sessions/` would be a new subdirectory.

---

### 6. `docs/research/existing-app-audit.md`

**Source**: `~/omar/knowledge/research/business/villa-thaifa-existing-app-audit.md`
**Status**: CLEAR

- `docs/research/` does not exist in the repo.
- Searched for "existing app audit", "existing-app" in the repo — found only a reference in `ops/intake/migration-path-validation.md` ("368 LOC skeleton audit"), which is a description, not the document itself.
- Source is a 368+ line detailed audit (route inventory, SQLite schema, agent infrastructure, 14 requirements vs. implementation status). Unique content.

---

### 7. `docs/research/missing-yaml-investigation.md`

**Source**: `~/omar/knowledge/research/business/villa-thaifa-missing-yaml-investigation.md`
**Status**: CLEAR

- `docs/research/` does not exist in the repo.
- No equivalent found. The topic (property.yaml/pricing.yaml/policy.yaml never existed as separate files; consolidated into 3 SSOT files) is not documented anywhere in the repo.
- Source is a completed investigation with findings. Unique content.

---

### 8. `docs/research/yaml-backup-search.md`

**Source**: `~/omar/knowledge/research/business/villa-thaifa-yaml-backup-search.md`
**Status**: CLEAR

- `docs/research/` does not exist in the repo.
- No equivalent found. The topic (full filesystem search for YAML files across /home/director/ and /media/director/data/, confirming property.yaml was never committed) is not documented in the repo.
- Source is a completed filesystem search with findings. Unique content.
- **Note**: Items 7 and 8 are closely related (same YAML incident, different investigation legs). Consider consolidating when migrating.

---

### 9. `docs/research/repo-strategy-decision.md`

**Source**: `~/omar/knowledge/research/development/villa-thaifa-repo-strategy-decision.md`
**Status**: CLEAR

- `docs/research/` does not exist in the repo.
- Searched for "repo strategy", "new repo", "villa-thaifa-pms" — found references in `ops/handoff/handoff-linear-migration-preparation.md` and `docs/2025-12-22-target-structure.md` but not the decision document itself.
- `ops/decisions/repo-organization-decision.md` exists but covers the repo directory structure, not the "new repo vs. existing repo" GitHub strategy decision.
- Source is a formal decision record (DEC-VT-001) with context, options, scoring matrix, 8.95/10 score for new repo. Unique content.

---

### 10. `docs/research/consolidation-app-eval.md`

**Source**: `~/omar/knowledge/research/prompt-evaluations/villa-thaifa-consolidation-app-eval.md`
**Status**: CLEAR

- `docs/research/` does not exist in the repo.
- No equivalent found. Searched for "consolidation", "prompt evaluation", "workstream" in the repo — found only `context/meta/planning/villa-thaifa-workstream-master-v0.1.0.md` (different content: a workstream master plan, not a prompt evaluation).
- Source is a prompt quality evaluation (2.8/10 score) with 7 extracted workstreams. Unique content.

---

### 11. `docs/client/said-thaifa.md`

**Source**: `~/omar/operational/productivity/memory/people/said-thaifa.md`
**Status**: REDUNDANT — partial overlap with existing stakeholders.md

- `docs/client/` exists. `docs/client/said-thaifa.md` does NOT exist yet.
- **Existing overlap**: `docs/client/stakeholders.md` already contains a full Said Thaifa section (lines 24–46) with: contact info (email + WhatsApp + phone), age, property details, platform accounts, key facts (Booking.com 9.3/10, communication rules, vouvoiement), and a pointer to `profiles/SAID-THAIFA.md`.
- **Source content** (`said-thaifa.md`): Shorter — name, role, company, age, active-since date, and project phase (3 lines of context). Subset of what's already in `stakeholders.md`.
- **Conclusion**: The source file is a lightweight Omar-side memory note. The repo already has a more detailed Said Thaifa entry. Migrating as-is would create a duplicate with less information.
- **Action**: Merge any unique facts from source into `docs/client/stakeholders.md` rather than creating a separate file. If a dedicated profile is desired, create `docs/client/profiles/said-thaifa.md` (already referenced as a planned file in `stakeholders.md` line 45).

---

### 12. `docs/client/communications.md`

**Source**: `~/omar/archives/grid/comms/clients/villa-thaifa.md`
**Status**: CLEAR

- `docs/client/communications.md` does not exist in the repo.
- Source is a historical communications summary (project overview, recent accomplishments as of Jan 2026, pending work, technical component status table, file locations). No equivalent found in the repo.
- **Note**: Source content references an OLD project location (`~/grid/clients/villa-thaifa/`) and an older codebase state (Next.js with working HotelRunner API, Booking.com via browser automation). The "Current Status" is dated January 24, 2026, and the "pending work" (stop-sell for March 2026, rate parity automation) may already be stale relative to the 2026-02-13 session which decided on a fresh start. Review for accuracy before migrating.

---

### 13. `docs/integrations/whatsapp-mcp-setup.md`

**Source**: `~/omar/operational/infrastructure/el-mountassir/integrations/whatsapp-mcp.md`
**Status**: CLEAR

- `docs/integrations/` does not exist in the repo.
- Searched for "whatsapp" in the repo — found mentions in `docs/lessons-learned.md`, `docs/project/BRIEF.md`, `docs/client/stakeholders.md`, and several `context/meta/planning/` files, but none contain setup/installation documentation.
- Source is a full setup guide (architecture diagram, installation steps, bridge status, tool inventory). Unique content.

---

### 14. `data/whatsapp/messages.db`

**Source**: `~/omar/operational/infrastructure/el-mountassir/integrations/whatsapp-mcp-repo/whatsapp-bridge/store/messages.db`
**Status**: CLEAR

- `data/whatsapp/` does not exist in the repo.
- No WhatsApp database files exist anywhere in the repo.
- Source file exists at the given path.
- **Note**: Binary SQLite file. May contain guest PII. Should be gitignored before committing. A separate gitignore decision is needed. See `ops/intake/migration-path-validation.md` §SQLite files in git.

---

### 15. `data/whatsapp/whatsapp.db`

**Source**: `~/omar/operational/infrastructure/el-mountassir/integrations/whatsapp-mcp-repo/whatsapp-bridge/store/whatsapp.db`
**Status**: CLEAR

- `data/whatsapp/` does not exist in the repo.
- Source file exists.
- Same PII/gitignore caveat as item 14.

---

### 16. `docs/integrations/whatsapp-context.md`

**Source**: `~/omar/specs/el-mountassir/surfaces/whatsapp/CLAUDE.md`
**Status**: CLEAR

- `docs/integrations/` does not exist in the repo.
- Source is a full agent context file for the WhatsApp communication surface: identity (Guest Communication Specialist), available tools (search_contacts, list_messages, send_text, etc.), risk levels, decision rules for guest communication. No equivalent in the repo.
- **Note**: Source is named `CLAUDE.md` — it is an agent instruction file, not a standard documentation file. The content is partially agent-configuration and partially operational context. Consider whether the agent-config portions belong in `context/agents/` rather than in a docs or knowledge directory.

---

### 17. `docs/backlog/logo-design.md`

**Source**: `~/omar/archives/grid/archives/2026-01-31-workstream-to-linear/backlog/villa-thaifa-logo-design.md`
**Status**: CLEAR (but reject migration as file — see path validation)

- `docs/backlog/` does not exist in the repo and must not be created (task registry rule).
- No equivalent logo design task found in the repo.
- Source is a full task card with frontmatter (priority P2, created 2026-01-29), Instagram handle, property details, design deliverables.
- Per `ops/intake/migration-path-validation.md`: this is a work item, not a document. Must be created as a Linear VT-team issue, not migrated as a file.

---

### 18. `docs/backlog/resume-project.md`

**Source**: `~/omar/archives/grid/archives/2026-01-31-workstream-to-linear/backlog/villa-thaifa-resume.md`
**Status**: CLEAR (but reject migration as file — see path validation)

- `docs/backlog/` does not exist in the repo and must not be created.
- No equivalent resume-project task in the repo.
- Source is a task card with project location, GitHub URL, and pending tasks from January 2026. Content is stale (references `~/grid/clients/villa-thaifa/` and the old `develop` branch) — the 2026-02-13 session supersedes this entirely.
- Per `ops/intake/migration-path-validation.md`: must be a Linear issue. Reference context (if needed) belongs in `context/meta/`.
- **Note**: Source content is likely obsolete given the decision to start fresh with villa-thaifa-pms (2026-02-13).

---

## Cross-Cutting Notes

### No target paths currently exist

All 18 proposed target directories (`docs/planning/`, `docs/research/`, `docs/integrations/`, `docs/backlog/`, `data/whatsapp/`) are absent from the repo. No "EXISTS" conflicts found.

### Existing similar content found in repo

| Repo File | Overlaps With |
|---|---|
| `context/meta/planning/DATA-INVENTORY.md` | Item 2 (different scope — current-state audit vs. migration strategy) |
| `docs/client/stakeholders.md` (Said section) | Item 11 (stakeholders.md is a superset of said-thaifa.md) |

### Stale source content warnings

| Item | Issue |
|---|---|
| 12 | `communications.md` source references old project paths and Jan 2026 state — review before migrating |
| 18 | `resume-project.md` source is obsolete (old laptop paths, develop branch, pre-2026-02-13 state) |

### Path compliance

All 18 target paths have been independently analyzed for contract compliance in `ops/intake/migration-path-validation.md`. This document covers content conflicts only. The two documents should be read together before executing any migration.

### Items requiring pre-migration decisions

| Item | Blocking Decision |
|---|---|
| 14, 15 | Gitignore strategy for SQLite files containing potential guest PII |
| 11 | Merge into `stakeholders.md` vs. create `docs/client/profiles/said-thaifa.md` |
| 17, 18 | Create Linear VT issues before discarding source content |
| 12 | Verify content accuracy before migrating (references stale state) |

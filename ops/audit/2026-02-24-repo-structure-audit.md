# Repository Structure Audit — 2026-02-24

> **Scope**: docs/, ops/, context/meta/, project/ — correctness of file placement,
> data vs state separation, intake triage, archive compliance.
> **Auditor**: Nova (Claude Sonnet 4.6)
> **Safety**: Read-only. Zero modifications to existing files.

---

## Summary

The repository structure is largely sound after the 2026-02-13/02-19 consolidation work. The
canonical data layer (data/) is clean and well-organised. The primary concerns are: (1) five
intake files that are fully processed but have never been actioned or moved; (2) a large
ops/archive/ tree (~150+ files) where Capture Before Archive compliance is partial — several
files contain unextracted knowledge that is now buried; (3) context/meta/architecture/ has four
legacy/superseded files that should be archived; (4) context/meta/planning/PROJECT.md is a
near-duplicate of project/CONTRACT.md and should be resolved; (5) truth.md in ops/status/
duplicates structured room and pricing data that lives canonically in data/ — this is the most
significant structural concern requiring a decision.

---

## Findings by Area

### A. docs/client/

**Files found:** admin.md, stakeholders.md, support.md

**Assessment:**
- `admin.md`: Near-empty shell. Contains only a heading, a one-line description ("Internal project
  notes, transcripts, and brainstorming"), a CONTACT section with an empty nested heading, and a
  `kiss_principle_notes` label with no content. Structurally incoherent and adds zero value.
- `stakeholders.md`: Correctly a pointer-only file (collapsed 2026-02-21). Original 98KB content
  migrated to `data/admin/client/PROFILE.md` and `data/admin/client/CONTACT.md`. This file now
  serves as a cross-reference card. Content is correct and minimal (17 lines). KEEP.
- `support.md`: Contains HWS/HotelRunner support contact (Ikram). Belongs in docs/client/ per
  directory contract. Content is current (first contact 2025-12-22). Should cross-reference
  data/admin/ if an admin contact file exists there.

**Verdict:**
- `admin.md`: ARCHIVE — empty shell, zero extraction needed.
- `stakeholders.md`: KEEP — correct pointer file.
- `support.md`: KEEP — verify if content is also in data/admin/; add cross-reference if so.

---

### B. docs/workflows/

**Files found:** pricing.md, whatsapp-mcp-setup.md

**Assessment:**
- `pricing.md`: Workflow guide for price updates. Correctly placed in docs/workflows/. References
  data/finance/rates.json and data/rooms/rooms.md as expected. Version v0.1.0-alpha.0. KEEP.
- `whatsapp-mcp-setup.md`: Full WhatsApp MCP server setup guide (283 lines). Correctly placed
  per migration-path-validation.md. Status: "Installation in Progress (Bridge Running)" as of
  2026-02-09. Note: references ~/el-mountassir/infrastructure/ paths — may need updates when
  el-mountassir infrastructure is reorganised.

**Verdict:** Both files KEEP. Flag whatsapp-mcp-setup.md for path update during next
el-mountassir infra session.

---

### C. ops/status/

**Files found:** truth.md, work-overview.md, data-domain-status.md, plus empty archive/ and snapshots/.

**Critical finding — truth.md §1 contains duplicated structured data:**

truth.md Section 1 contains a full 12-room pricing table with EUR/MAD rates, capacity, bed
configuration, view, and outdoor data. Canonical sources for this data are:
- `data/rooms/rooms.md` (room specs)
- `data/finance/rates.json` (pricing)

truth.md also contains:
- §2-§5: Property configuration, financial, channels, client info — all as summaries referencing
  canonical sources (correct pattern).
- §6: Known conflicts (referencing open-conflicts-registry.md as canonical — correct).
- §7: Canonical data map (pure index — excellent).
- §8: Pending actions (operational status — correct for ops/).
- §9: Pricing correction record — a DECISION LOG ENTRY, not status. Belongs in ops/decisions/.
- §10: VT App & Tech Stack Status — borderline but acceptable in status file.

`work-overview.md`: Correctly placed. Task dashboard, last updated 2026-02-22. KEEP.

`data-domain-status.md`: Correctly placed. Phase A completion summary. Contains a stale reference
to `docs/core/` (line 120) which should be `project/` — the 2026-02-19 migration superseded
docs/core/.

**ops/status/archive/**: Empty.
**ops/status/snapshots/**: Empty.

**Verdict:**
- truth.md §1 room table: DECISION NEEDED — replace with 3-line summary + links, or accept
  as agreed redundancy. See Recommendations #3.
- truth.md §9: Extract to ops/decisions/ as a decision record.
- data-domain-status.md: Fix stale docs/core/ reference to project/.

---

### D. ops/intake/

**Files found:** context-window-cost-analysis.md, IMG_20260126_0001.pdf, linear-github-repo-alignment.md,
linear-issues-agents-md-gaps.md, migration-conflict-check.md, migration-path-validation.md.
Plus: processed/ (manifest.csv, README.md, unprocessed-files.md) and unprocessed/ (empty).

**Assessment of each:**

| File | Processing Status | Recommended Destination |
|------|-------------------|------------------------|
| context-window-cost-analysis.md | Complete analysis, created 2026-02-24 | Move to context/meta/architecture/ — it is reference material about the repo's @reference chain architecture |
| IMG_20260126_0001.pdf | Unknown — binary PDF not read | OMAR INPUT NEEDED — identify content; likely data/admin/ if property doc |
| linear-github-repo-alignment.md | Status says "Resolved" but no ops/decisions/ record found | Verify/create decision record in ops/decisions/, then archive |
| linear-issues-agents-md-gaps.md | 7 Linear issues pending creation | Create 7 issues via linear-agent, then archive |
| migration-conflict-check.md | Fully processed — 18 path conflict assessments complete | Archive to ops/archive/ |
| migration-path-validation.md | Fully processed — 18 path verdicts complete | Archive to ops/archive/ together with migration-conflict-check.md |

**Summary**: 4 of 6 files are ready to action. 1 requires Omar's input (PDF). 1 requires Linear
check before archiving.

---

### E. ops/archive/ — Capture Before Archive Compliance

**Archive volume**: ~150+ files across 10 subdirectories.

**Sample files reviewed:**

**ops/archive/knowledge/decision-evaluator-agent-pattern.md**
- Content: Structured evaluation pattern for credentials management (decision scoring matrix).
- Compliance: PARTIAL — contains a reusable agent pattern (Decision Evaluator with weighted
  scoring) that should live in ~/omar/core/resources/skills/. Archived without extraction.
- Unextracted item: Agent pattern → ~/omar/core/resources/skills/ or context/meta/knowledge/.

**ops/archive/knowledge/consolidation-app-eval.md**
- Content: Prompt quality evaluation (2.8/10) that extracted 7 workstreams.
- Compliance: PARTIAL — workstreams were extracted as context, but the evaluation FINDINGS
  (what makes a good prompt, what scope creep looks like) were not captured as a lesson in
  context/meta/knowledge/lessons-learned.md.

**ops/archive/planning/villa-thaifa-open-questions-v0.1.0.md**
- Content: 2026-01-09 open questions with blocking questions still marked "AWAITING RESPONSE".
- Compliance: NON-COMPLIANT — blocking questions were not converted to Linear issues or
  ops/decisions/pending/ items before archiving. The questions may have been answered since
  (vt-app-vision.md exists) but closure was never recorded.

**Compliance verdict:** PARTIAL overall. The archive was built during rapid migration work.
Retroactive full extraction is not recommended (high effort, low immediate value). The 2-3
identified gaps can be addressed opportunistically during ~/omar/ sessions.

---

### F. context/meta/architecture/

**Files found:** ADR-001-structure.md, architecture-README.md, stack-README.md, tech-stack-decision.md,
tech_stack.md, tech-stack-omar-v0.1.3-lux-annotated.md, villa-thaifa-technical-context-v0.1.0.md

| File | Date | Assessment | Verdict |
|------|------|-----------|---------|
| ADR-001-structure.md | 2026-01-12 | Domain-driven architecture (src/domains/ vs src/areas/). Accepted, relevant to VT app. | KEEP |
| architecture-README.md | 2026-01-12 | References VERSION.txt (deleted per git status: D context/meta/architecture/VERSION.md). "Under construction". | ARCHIVE |
| stack-README.md | no date | Describes "Antigravity as CTO", Markdown data layer. Pre-2026-02-13 mental model. | ARCHIVE |
| tech-stack-decision.md | 2026-01-29 | Next.js + CSS Modules (no Tailwind). Partially superseded by vt-app-vision.md (Tailwind+shadcn/ui). | ARCHIVE or UPDATE |
| tech_stack.md | 2026-01-17 | Defines json-render as UI engine. json-render REJECTED 2026-02-21. Actively wrong. | ARCHIVE IMMEDIATELY |
| tech-stack-omar-v0.1.3-lux-annotated.md | 2026-01-07 | Self-declared "DRAFT/EVOLVING/Inaccurate". References LHCM-OS (lives at ~/omar/, not here). | ARCHIVE |
| villa-thaifa-technical-context-v0.1.0.md | 2026-01-09 | Describes browser automation as "current approach". Superseded by HotelRunner API. | ARCHIVE |

**Summary**: 1 of 7 files is current (ADR-001-structure.md). 5 are archived candidates. 1
(tech-stack-decision.md) needs a decision about whether to update or archive.

Note: context-window-cost-analysis.md (currently in ops/intake/) should be moved here after
the superseded files are archived.

---

### G. context/meta/knowledge/

**Files found:** events-privatization.md, guest-communication.md, lessons-learned.md

| File | Assessment | Verdict |
|------|-----------|---------|
| events-privatization.md | Active privatization policy. Contains room capacity table duplicating data/rooms/rooms.md. Also has broken cross-references to non-existent paths (../../data/rooms/inventory.yaml, ../../../leadership/profiles/SAID-THAIFA.md). | KEEP — fix broken cross-references to correct paths (data/rooms/rooms.md, data/admin/client/PROFILE.md) |
| guest-communication.md | Communication workflow (SCOUT→REPORT→QUESTIONS→ACTION). Correctly placed. Output Files section references data/communication/whatsapp/ path which does not exist. | KEEP — flag non-existent output path |
| lessons-learned.md | 7 operational lessons from Dec 2025. Valuable. Correctly placed. | KEEP |

**Summary**: All 3 correctly placed. Two have stale internal references that need updating.

---

### H. context/meta/planning/

**Files found:** 2026-02-13-agentic-operating-playbook.md, delegation-framework.md, language-policy.md,
PROJECT.md, revenue-management-vision.md, vt-app-vision.md

| File | Assessment | Verdict |
|------|-----------|---------|
| 2026-02-13-agentic-operating-playbook.md | Weekly cadence, daily workflow, template references. Current. | KEEP |
| delegation-framework.md | Multi-model delegation routing matrix (v2.0, 2026-02-13). Current. | KEEP |
| language-policy.md | 10-line file superseded by CLAUDE.md Language Override + universal.md Communication rule. | ARCHIVE — zero extraction needed |
| PROJECT.md | Near-duplicate of project/CONTRACT.md. Contains unique validated requirements list (PUB-01 through INT-01) documenting what was ALREADY BUILT in the existing brownfield app. | DECISION NEEDED — see Recommendations #2 |
| revenue-management-vision.md | Revenue management vision (3 structural problems, dynamic pricing strategy). Well-structured. | KEEP |
| vt-app-vision.md | VT app vision seed (2026-02-21). Referenced in truth.md §7. Tech stack: Next.js + Tailwind + shadcn/ui. "Concept — needs planning before build". | KEEP |

**PROJECT.md specific finding**: Contains a validated requirements list (PUB-01, ADMIN-01,
DATA-01, INT-01 etc.) describing features already built in the existing app
(omar-elmountassir/villa-thaifa-pms or equivalent). This content is not in project/CONTRACT.md.
If the brownfield app is still relevant, these requirements need migration. If it was fully
superseded by the fresh-start decision (2026-02-13), the file can be archived as historical.

---

### I. project/ directory

**Files found:** CONTRACT.md, MISSION.md, PRINCIPLES.md, ROADMAP.md, STRUCTURE-card-*.md (6 cards),
STRUCTURE-filtered.txt, STRUCTURE.md

All files are correctly placed. ROADMAP.md was updated today (2026-02-24) and is current.
STRUCTURE-card-*.md files are generated artifacts (make structure-cards) — correct placement.
STRUCTURE.md stats are from 2026-02-19 — run `make structure-update` after any moves.

**No misplaced content found in project/.**

---

### J. Cross-cutting: Data in Wrong Places

**truth.md §1 room pricing table** (ops/status/truth.md):
12-row table with EUR/MAD pricing, capacity, beds, views embedded in a status file. Canonical
sources: data/finance/rates.json + data/rooms/rooms.md.

**truth.md §9 pricing correction record** (ops/status/truth.md):
A decision log entry (rates.json had 4 wrong values, corrected 2026-02-21) embedded in status.
Belongs in ops/decisions/.

**events-privatization.md room capacity table** (context/meta/knowledge/):
Full 12-room capacity table duplicating data/rooms/rooms.md. Acceptable as event-context
reference but will drift from canonical if room changes occur.

**data-domain-status.md stale reference** (ops/status/):
Line 120 references docs/core/ — superseded by project/ in 2026-02-19 migration.

**No raw JSON data structures found** in docs/, ops/, context/ — the data/ layer is clean.

---

## Misplaced Files Inventory

| File | Current Location | Correct Location | Priority |
|------|-----------------|-----------------|----------|
| context-window-cost-analysis.md | ops/intake/ | context/meta/architecture/ | MEDIUM |
| tech_stack.md | context/meta/architecture/ | ops/archive/ | HIGH |
| tech-stack-omar-v0.1.3-lux-annotated.md | context/meta/architecture/ | ops/archive/ | HIGH |
| villa-thaifa-technical-context-v0.1.0.md | context/meta/architecture/ | ops/archive/ | MEDIUM |
| architecture-README.md | context/meta/architecture/ | ops/archive/ | MEDIUM |
| stack-README.md | context/meta/architecture/ | ops/archive/ | MEDIUM |
| language-policy.md | context/meta/planning/ | ops/archive/ | LOW |
| PROJECT.md | context/meta/planning/ | Extract then archive | HIGH |
| admin.md | docs/client/ | ops/archive/ | LOW |
| migration-conflict-check.md | ops/intake/ | ops/archive/ | MEDIUM |
| migration-path-validation.md | ops/intake/ | ops/archive/ | MEDIUM |

---

## Recommendations

### High Priority

1. **Archive `context/meta/architecture/tech_stack.md` immediately** — Contains json-render as
   UI engine. json-render was REJECTED 2026-02-21. This file is actively wrong and will mislead
   any agent reading it. Decision record already exists at ops/decisions/json-render-evaluation.md.

2. **Resolve `context/meta/planning/PROJECT.md`** — Two options:
   - (a) Extract the validated requirements list (PUB-01 through INT-01) into a new file
     `ops/decisions/brownfield-requirements.md` or into project/CONTRACT.md, then archive.
   - (b) If the brownfield app is fully superseded by the fresh start (2026-02-13 decision),
     confirm with Omar and archive directly as historical.
   REQUIRES OMAR'S DECISION on whether brownfield app requirements are still relevant.

3. **Decide on truth.md §1 room pricing table** — Two options:
   - (a) Replace §1 with a 3-line summary + links to data/finance/rates.json and
     data/rooms/rooms.md (reduces redundancy, prevents drift).
   - (b) Accept as agreed-upon redundancy (easier to read, but will drift on rate changes).
   REQUIRES OMAR'S DECISION.

### Medium Priority

4. **Move `context-window-cost-analysis.md`** from ops/intake/ to context/meta/architecture/ —
   It is a complete architectural analysis, not an unprocessed intake item.

5. **Archive 4 superseded architecture files**: architecture-README.md, stack-README.md,
   tech-stack-omar-v0.1.3-lux-annotated.md, villa-thaifa-technical-context-v0.1.0.md.
   All are pre-2026-02-13 state, self-declared inaccurate, or reference deleted files.

6. **Extract truth.md §9 to ops/decisions/** — The pricing correction record (rates.json had 4
   wrong values, corrected 2026-02-21) is a decision log entry. Create
   ops/decisions/rates-json-correction-2026-02-21.md.

7. **Triage `ops/intake/IMG_20260126_0001.pdf`** — Unknown content. Omar must identify what this
   PDF is and where it belongs (likely data/admin/ if property documentation).

8. **Create 7 Linear issues from `ops/intake/linear-issues-agents-md-gaps.md`** — Delegate to
   linear-agent. Issues cover AGENTS.md governance gaps (cascade protocol, archive criteria,
   Capture Before Archive reference, cross-linking, tech-decisions.md, handoff criteria, SYNC
   examples). After creation, archive the intake file.

9. **Archive `ops/intake/migration-conflict-check.md` + `migration-path-validation.md`** —
   Both fully processed. Move to ops/archive/.

10. **Fix broken cross-references in `context/meta/knowledge/events-privatization.md`** —
    Links to `../../data/rooms/inventory.yaml` and `../../../leadership/profiles/SAID-THAIFA.md`
    do not exist. Update to: data/rooms/rooms.md and data/admin/client/PROFILE.md.

11. **Run `make structure-update`** after any of the above moves.

### Low Priority

12. **Archive `context/meta/planning/language-policy.md`** — 10-line file superseded by
    CLAUDE.md Language Override + universal.md Communication rule. Zero extraction needed.

13. **Archive `docs/client/admin.md`** — Empty shell. Zero extraction needed.

14. **Fix stale `docs/core/` reference in `ops/status/data-domain-status.md`** — Should
    reference `project/` not `docs/core/`.

15. **Verify `ops/intake/linear-github-repo-alignment.md`** — File says "Resolved" but no
    corresponding record found in ops/decisions/. Create brief decision record, then archive.

16. **Extract decision-evaluator-agent-pattern** from ops/archive/knowledge/ — The structured
    option scoring pattern is reusable. Consider extracting to ~/omar/core/resources/skills/
    during next ~/omar/ session (not blocking for VT work).

---

## Files Safe to Archive (No Extraction Needed)

- context/meta/architecture/tech_stack.md — actively wrong (json-render rejected)
- context/meta/architecture/tech-stack-omar-v0.1.3-lux-annotated.md — self-declared "Inaccurate"
- context/meta/architecture/architecture-README.md — references deleted VERSION.md
- context/meta/architecture/stack-README.md — pre-2026-02-13 mental model
- context/meta/architecture/villa-thaifa-technical-context-v0.1.0.md — superseded by current HotelRunner API approach
- context/meta/planning/language-policy.md — superseded by CLAUDE.md + universal.md
- docs/client/admin.md — empty shell
- ops/intake/migration-conflict-check.md — fully processed
- ops/intake/migration-path-validation.md — fully processed

---

## Files Requiring Extraction or Decision Before Archive

- context/meta/planning/PROJECT.md — unique brownfield requirements list; needs Omar's decision
- ops/intake/linear-issues-agents-md-gaps.md — 7 Linear issues must be created first
- ops/intake/linear-github-repo-alignment.md — verify/create ops/decisions/ record first
- ops/intake/IMG_20260126_0001.pdf — Omar must identify content

---

## Integrity Assessment

No data loss risk identified. All files in data/ are correctly placed and the canonical data
layer is clean. The issues above are placement and redundancy concerns, not data integrity
failures.

ops/archive/ retroactive extraction: A full pass on ~150 files is not recommended (high effort,
low immediate value). 2-3 gaps found via sampling can be addressed opportunistically.

---

_Audit performed: 2026-02-24 | Files read: 37 | Directories listed: 15 | Zero modifications made_

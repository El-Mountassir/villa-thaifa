# Migration Placement Audit

**Date**: 2026-02-16
**Auditor**: Claude Opus 4.6
**Scope**: Every file in the villa-thaifa repository, checked against AGENTS.md File Placement Decision Tree and Directory Contract.
**Total files scanned**: 436 (excluding .git, cache, images directories)

---

## Table of Contents

1. [Executive Summary](#executive-summary)
2. [Violations — Must Fix](#violations--must-fix)
3. [Warnings — Should Review](#warnings--should-review)
4. [Compliant Files by Directory](#compliant-files-by-directory)
5. [Recommendations](#recommendations)

---

## Executive Summary

**Violations found: 16**
**Warnings: 8**
**Compliant: ~412**

The largest category of violations is **ops/ root files that should be in subdirectories** (9 files). The second category is **data/STATUS.md**, which is an operational status artifact placed in the data directory. There are also some borderline files in `docs/client/` and `context/meta/knowledge/` worth reviewing.

---

## Violations -- Must Fix

### V1. Handoff files in ops/ root instead of ops/handoff/

Per the Directory Contract, session handoff docs belong in `ops/handoff/`. These 5 files sit in `ops/` root:

| # | Current Location | Correct Location |
|---|-----------------|------------------|
| 1 | `ops/handoff-2026-02-16-gemini-standardization.md` | `ops/handoff/handoff-2026-02-16-gemini-standardization.md` |
| 2 | `ops/handoff-archive-lifecycle-system.md` | `ops/handoff/handoff-archive-lifecycle-system.md` |
| 3 | `ops/handoff-critical-session-state.md` | `ops/handoff/handoff-critical-session-state.md` |
| 4 | `ops/handoff-github-template-repos.md` | `ops/handoff/handoff-github-template-repos.md` |
| 5 | `ops/handoff-governance-decide.md` | `ops/handoff/handoff-governance-decide.md` |

**Decision Tree path**: Live operational artifact? YES --> ops/ --> Session handoff? --> ops/handoff/

---

### V2. Audit files in ops/ root instead of ops/audit/

Per the Directory Contract, audit reports belong in `ops/audit/`. These 5 files sit in `ops/` root:

| # | Current Location | Correct Location |
|---|-----------------|------------------|
| 1 | `ops/audit-content-integrity.md` | `ops/audit/audit-content-integrity.md` |
| 2 | `ops/audit-dedup-profiles.md` | `ops/audit/audit-dedup-profiles.md` |
| 3 | `ops/audit-dedup-safety-check.md` | `ops/audit/audit-dedup-safety-check.md` |
| 4 | `ops/audit-docs-context-placement.md` | `ops/audit/audit-docs-context-placement.md` |
| 5 | `ops/audit-finance-data.md` | `ops/audit/audit-finance-data.md` |

**Note**: `ops/audit-unstaged-files.md` is also in ops/ root -- same violation. That makes 6 audit files total.

| 6 | `ops/audit-unstaged-files.md` | `ops/audit/audit-unstaged-files.md` |

**Decision Tree path**: Live operational artifact? YES --> ops/ --> Audit report? --> ops/audit/

---

### V3. Session recovery file in ops/ root

| # | Current Location | Correct Location |
|---|-----------------|------------------|
| 1 | `ops/session-recovery-017eb935.md` | `ops/handoff/session-recovery-017eb935.md` |

**Reasoning**: A session recovery brief is functionally a handoff document. It belongs in `ops/handoff/`.

---

### V4. data/STATUS.md -- operational status in data/

| # | Current Location | Correct Location |
|---|-----------------|------------------|
| 1 | `data/STATUS.md` | `ops/status/data-domain-status.md` |

**Reasoning**: This file tracks "Data Domain Status -- Post Phase A Consolidation" with phase tracking and next-step planning. Per the Decision Tree: "Is it a live operational artifact (audit, decision, handoff, status)? YES --> ops/ --> status dashboard? --> ops/status/". Status tracking does NOT belong in `data/` -- the `data/` contract explicitly says "What does NOT go here: Documentation, operational artifacts (audits, decisions)."

---

### V5. docs/repo-organization-decision.md -- file referenced in git status but not on disk

Git status shows `docs/repo-organization-decision.md` as modified, but the file does not exist at that path. A file with the same name exists at `ops/decisions/repo-organization-decision.md`. This appears to be a move that was staged correctly -- the old path is a stale git reference. **No action needed** if the move was intentional; confirm that `docs/repo-organization-decision.md` was properly removed.

---

## Warnings -- Should Review

### W1. context/meta/knowledge/ -- massive accumulation (54 files)

The `context/meta/knowledge/` directory contains 54 files. While the Directory Contract allows "knowledge references" in `context/`, this directory has become a catch-all. Several files have questionable placement:

| File | Concern |
|------|---------|
| `pricing.md` | Deleted per git status (good -- this was likely data, not reference) |
| `chambre_et_vue.md` | Room/view descriptions -- may be data, not reference |
| `events-privatization.md` | Operational policy -- may belong in `data/operations/` or `docs/workflows/` |
| `guest-communication.md` | Operational workflow -- may belong in `docs/workflows/` |
| `gemini-onboarding-prompt.md` | Agent config -- may belong in `context/agents/` |
| `gemini-system-prompt.md` | Agent config -- may belong in `context/agents/` |
| `protocols.md` | Operational protocols -- may belong in `docs/workflows/` |
| `rules.md` | Unclear scope vs project rules -- review for duplication |
| `decision-evaluator-agent-pattern.md` | Agent pattern -- may belong in `context/agents/` |
| `frontmatter-schema.md` | Template/schema -- may belong in `context/meta/templates/` |

**Recommendation**: Triage these 54 files. Many are legitimate reference material, but at least 10 should be reclassified per the Decision Tree.

---

### W2. context/meta/planning/ -- massive accumulation (96 files)

The `context/meta/planning/` directory contains 96 files spanning from December 2025 to February 2026. This is the largest single directory in the repo. Many files appear to be completed/historical plans that should move to `ops/archive/`:

**Examples of likely-completed plans**:
- `01-01-PLAN.md`, `01-01-SUMMARY.md`, `01-02-PLAN.md` -- old plans
- `ROADMAP.md`, `ROADMAP-2.md` -- likely superseded
- `comprehensive-transformation-plan.md` -- likely completed
- `CONSOLIDATION-PLAN.md` -- likely completed (Phase A done)
- `STATE.md`, `NEXT_STEPS.md`, `TODOs.md` -- stale operational state
- `FICHE-MISSION-OMAR-29-JANVIER.md` -- dated one-time artifact

**Recommendation**: This directory needs a separate triage pass. Active plans should stay; completed plans should archive to `ops/archive/`. This aligns with the "completed work never gets archived" pain point noted in MEMORY.md.

---

### W3. ops/audit/quality/ -- 62 files, many historical

The `ops/audit/quality/` directory contains 62 files spanning many months. Many appear to be completed audit artifacts (execution logs, old reports, one-time analyses). These should be triaged: active/recurring audits stay, completed ones archive to `ops/archive/`.

**Examples of likely-archivable files**:
- `execution-log-001.md`, `execution-log-002.md` -- completed
- `rapport-demo-20-dec-2025.md` -- dated, one-time
- `BRUTAL-AUDIT-REPORT-2026-01-16.md` -- dated, one-time
- `FINAL-REPORT-2026-01-16.md` -- dated, one-time
- `PHASE-2-COMPLETION-REPORT.md` -- completed phase
- `MIGRATION-REPORT.md` -- completed migration
- `prompt.md`, `prompt-en.md` -- agent prompts, not audit reports (misplaced)

---

### W4. ops/audit/archive/history/ -- contains non-audit files

The `ops/audit/archive/history/` directory contains files that are not audit artifacts:
- `WhatsApp Chat with Said Thaifa.md` -- communication transcript, not an audit
- `WhatsApp Ptt 2026-02-06 at 13.03.07.md` and `.ogg` -- voice message, not an audit
- `MISSION.md` -- foundational doc backup (archived correctly, just odd location)
- `CHANGELOG.md` -- version history backup
- `Agentic Mastery.md` -- knowledge/reference, not an audit

These appear to have been swept into archive without classification. They are in archive so not actively harmful, but the directory name suggests "audit history" not "general archive."

---

### W5. docs/client/MESSAGE-POUR-SAID.md -- French language content

Per global rules: "English only. Everything -- chat, files, HTML, agents." This file is entirely in French. While it is a WhatsApp message draft for Said (who speaks French), the rule says files should be English. This may warrant an exception as it is client-facing content in the client's language.

---

### W6. ops/status/snapshots/ -- 21 files, many stale

The `ops/status/snapshots/` directory contains 21 files. Many are old README placeholders or stale state files:
- `STRUCTURE.md`, `STRUCTURE_CLEAN.md` -- structural snapshots (stale?)
- `ROADMAP.md` -- old roadmap snapshot
- `CLIENT.md`, `client-profile.md` -- client data that may belong in `docs/client/`
- Various `-README.md` files -- appear to be old directory README stubs

**Recommendation**: Triage for archive vs active use.

---

### W7. data/README.md and docs/README.md -- not in STRUCTURE.md

These directory-level README files are not explicitly listed in the STRUCTURE.md tree, but they are standard practice for documenting directory purpose. **Acceptable** -- no action needed.

---

### W8. docs/workflows/ -- only 1 file

The `docs/workflows/` directory has only `pricing.md`. Several files in `context/meta/knowledge/` (guest-communication.md, protocols.md, events-privatization.md) may be workflow documentation that belongs here. Cross-reference with W1.

---

## Compliant Files by Directory

### Root (all compliant)

- `AGENTS.md` -- required at root per rules
- `CLAUDE.md` -- required at root per rules
- `GEMINI.md` -- required at root per rules
- `README.md` -- required at root per rules
- `CHANGELOG.md` -- required at root per rules
- `Makefile` -- listed in STRUCTURE.md
- `pyproject.toml` -- listed in STRUCTURE.md
- `uv.lock` -- listed in STRUCTURE.md
- `.gitignore` -- listed in STRUCTURE.md
- `.labels.json` -- listed in STRUCTURE.md

### data/ (compliant, 1 exception)

All data files are correctly placed:
- `data/rooms/R01-R12/profile.md` -- per contract
- `data/rooms/rooms.md`, `amenities.md`, `beds.md`, `rooms-reconciliation-log.md` -- per contract
- `data/rooms/exports/` -- per contract
- `data/finance/billing.json`, `rates.json` -- per contract
- `data/operations/*.json` (5 files) -- per contract
- `data/property/property-config.json`, `data/property/facilities/*.md` -- per contract
- `data/bookings/**` -- per contract
- `data/pending-domains/facilities.md` -- per contract
- `data/archive/inventory.md` -- per contract

**Exception**: `data/STATUS.md` -- see V4 above.

### docs/ (compliant)

- `docs/core/MISSION.md`, `PRINCIPLES.md`, `STRUCTURE.md` -- foundational definitions, correct
- `docs/client/admin.md`, `stakeholders.md`, `support.md` -- client info, correct
- `docs/client/MESSAGE-POUR-SAID.md` -- client communication, correct placement (see W5 for language)
- `docs/workflows/pricing.md` -- workflow documentation, correct

### context/ (compliant, with warnings)

- `context/agents/booking/`, `browser/`, `hotelrunner/` -- agent reference configs, correct
- `context/meta/architecture/` -- architecture reference, correct
- `context/meta/templates/` -- templates, correct
- `context/meta/knowledge/` -- knowledge reference, correct (see W1 for triage needs)
- `context/meta/planning/` -- planning reference, correct (see W2 for archive needs)

### ops/ (compliant in subdirectories, violations in root)

- `ops/handoff/AI-SESSION-STARTER.md`, `HANDOFF.md` -- correct
- `ops/decisions/*.md` -- correct
- `ops/status/*.md` and `ops/status/snapshots/` -- correct placement (see W6 for triage)
- `ops/audit/quality/`, `ops/audit/archive/` -- correct placement (see W3, W4)
- `ops/intake/` -- correct
- `ops/archive/2026-01/` -- correct

**Violations in root**: See V1, V2, V3 above (12 files in ops/ root that belong in subdirectories).

### scripts/ (compliant)

All scripts correctly placed in `scripts/` with appropriate subdirectories (`audit/`, `hotelrunner/`, `inventory/`, `organization/`).

### tests/ (compliant)

Single test file `tests/test_scripts.py` -- correct.

### .claude/ (compliant)

Agent definitions in `.claude/agents/`, commands in `.claude/commands/`, settings in `.claude/settings.local.json` -- all correct for Claude Code configuration.

### logs/ and tmp/ (compliant)

Gitignored runtime directories with expected contents.

---

## Recommendations

### Priority 1 -- Quick Wins (12 file moves)

Move the 12 ops/ root files into their correct subdirectories. This is mechanical and low-risk:

```bash
# Handoffs (5 files)
mv ops/handoff-2026-02-16-gemini-standardization.md ops/handoff/
mv ops/handoff-archive-lifecycle-system.md ops/handoff/
mv ops/handoff-critical-session-state.md ops/handoff/
mv ops/handoff-github-template-repos.md ops/handoff/
mv ops/handoff-governance-decide.md ops/handoff/

# Audits (6 files)
mv ops/audit-content-integrity.md ops/audit/
mv ops/audit-dedup-profiles.md ops/audit/
mv ops/audit-dedup-safety-check.md ops/audit/
mv ops/audit-docs-context-placement.md ops/audit/
mv ops/audit-finance-data.md ops/audit/
mv ops/audit-unstaged-files.md ops/audit/

# Session recovery -> handoff (1 file)
mv ops/session-recovery-017eb935.md ops/handoff/
```

After moves: update any references in MEMORY.md, HANDOFF.md, or other docs that point to these files.

### Priority 2 -- Status file relocation (1 file)

```bash
mv data/STATUS.md ops/status/data-domain-status.md
```

Update references in data/README.md and any handoff docs.

### Priority 3 -- Triage passes (separate sessions)

1. **context/meta/knowledge/** (54 files) -- classify each as: stays / moves to context/agents/ / moves to docs/workflows/ / moves to data/operations/ / archives
2. **context/meta/planning/** (96 files) -- classify each as: active (stays) / completed (archives to ops/archive/)
3. **ops/audit/quality/** (62 files) -- classify each as: active / completed (archives) / misplaced (relocate)
4. **ops/status/snapshots/** (21 files) -- classify each as: active / stale (archives)

These triage passes are substantial work -- each should be a dedicated sub-agent task.

### Priority 4 -- Reference updates

After all moves, run a grep for old paths across the entire repo and update references. Pay special attention to:
- `ops/handoff/HANDOFF.md`
- `ops/handoff/AI-SESSION-STARTER.md`
- `AGENTS.md` Open Loops section (already mentions loose ops files)
- `.claude/` memory files

---

## File-by-File Verdict Summary

| Verdict | Count | Description |
|---------|-------|-------------|
| COMPLIANT | ~412 | Correctly placed per rules |
| VIOLATION | 13 | Wrong directory, must move |
| WARNING | ~11 | Borderline, needs review |
| TOTAL | ~436 | All files in repo |

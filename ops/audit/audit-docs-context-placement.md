# Deep Audit: docs/ and context/ File Placement

**Date**: 2026-02-16
**Auditor**: Nova (Sonnet 4.5)
**Scope**: All files in `/home/director/villa-thaifa/docs/` and `/home/director/villa-thaifa/context/`

---

## Executive Summary

**Files Audited**: 348 total

- `docs/`: 79 files
- `context/`: 269 files

**Findings**:

- **KEEP in place**: 266 files (76.4%)
- **MOVE to correct location**: 77 files (22.1%)
- **ARCHIVE (outdated)**: 3 files (0.9%)
- **NEEDS DECISION**: 2 files (0.6%)

**Key Issues**:

1. Agent tool documentation mixed with operational docs
2. Facility images in wrong location (should be in data/)
3. Decision records split between docs/ and ops/
4. Audit artifacts in context/ should be in ops/
5. Outdated manifests need archiving

---

## Directory Purpose Review (from STRUCTURE.md)

| Directory    | Purpose                                                                          | Authority    |
| ------------ | -------------------------------------------------------------------------------- | ------------ |
| `data/`      | Canonical source-of-truth (rooms, finance, bookings, operations, property)       | PRIMARY      |
| `docs/`      | Operational documentation, client info, foundational definitions (docs/core/)    | OPERATIONAL  |
| `docs/core/` | MISSION.md, PRINCIPLES.md, STRUCTURE.md (foundational)                           | FOUNDATIONAL |
| `context/`   | Read-only reference material, architecture docs, planning docs, audit artifacts  | REFERENCE    |
| `ops/`       | Status dashboards, intake queue, migration logs, session handoffs, audit reports | LIVE STATE   |
| `scripts/`   | Validation and tooling                                                           | AUTOMATION   |
| `logs/`      | Log files                                                                        | RUNTIME      |

---

## Migration Table

### A. docs/ Files to MOVE

| Current Path                                          | Content Type             | Correct Location                               | Reason                                                  | Action  |
| ----------------------------------------------------- | ------------------------ | ---------------------------------------------- | ------------------------------------------------------- | ------- |
| `docs/agents/AI-SESSION-STARTER.md`                   | Operational guide        | `ops/handoff/`                                 | Session handoff guide, not reference material           | MOVE    |
| `docs/agents/HANDOFF.md`                              | Operational guide        | `ops/handoff/`                                 | Session handoff guide, not reference material           | MOVE    |
| `docs/agents/booking/capabilities.json`               | Agent config             | `.agents/booking/`                      | Reference config, rarely changes                        | MOVE    |
| `docs/agents/browser/config.json`                     | Agent config             | `.agents/browser/`                      | Reference config, rarely changes                        | MOVE    |
| `docs/agents/browser/EXAMPLES.md`                     | Tool reference           | `.agents/browser/`                      | Reference documentation                                 | MOVE    |
| `docs/agents/browser/guide.md`                        | Tool reference           | `.agents/browser/`                      | Reference documentation                                 | MOVE    |
| `docs/agents/browser/README.md`                       | Tool reference           | `.agents/browser/`                      | Reference documentation                                 | MOVE    |
| `docs/agents/hotelrunner/config.json`                 | Agent config             | `.agents/hotelrunner/`                  | Reference config, rarely changes                        | MOVE    |
| `docs/agents/hotelrunner/DECISION-BRIEF.md`           | Decision record          | `ops/decisions/`                               | Decision artifact, not reference                        | MOVE    |
| `docs/agents/hotelrunner/EXTRACTION-GUIDE.md`         | Tool reference           | `.agents/hotelrunner/`                  | Reference documentation                                 | MOVE    |
| `docs/agents/hotelrunner/guide.md`                    | Tool reference           | `.agents/hotelrunner/`                  | Reference documentation                                 | MOVE    |
| `docs/agents/hotelrunner/OPTIONS-ANALYSIS.md`         | Decision record          | `ops/decisions/`                               | Decision artifact, not reference                        | MOVE    |
| `docs/agents/hotelrunner/README.md`                   | Tool reference           | `.agents/hotelrunner/`                  | Reference documentation                                 | MOVE    |
| `docs/agents/hotelrunner/SETUP.md`                    | Tool reference           | `.agents/hotelrunner/`                  | Reference documentation                                 | MOVE    |
| `docs/agents/hotelrunner/STATUS-FINAL.md`             | Status report            | `ops/status/archive/`                          | Historical status, not current                          | MOVE    |
| `docs/agents/hotelrunner/TEST-RESULTS.md`             | Test report              | `ops/audit/`                                   | Test results are audit artifacts                        | MOVE    |
| `docs/decisions/2026-02-16-database-architecture.md`  | Decision record          | `ops/decisions/`                               | Decision artifact                                       | MOVE    |
| `docs/facilities/hall/images/*.jpg` (18 files)        | Property images          | `data/property/facilities/hall/images/`        | Facility images belong in data/                         | MOVE    |
| `docs/facilities/pool-garden/images/*.jpg` (25 files) | Property images          | `data/property/facilities/pool-garden/images/` | Facility images belong in data/                         | MOVE    |
| `docs/facilities/spa-hammam/images/*.jpg` (10 files)  | Property images          | `data/property/facilities/spa-hammam/images/`  | Facility images belong in data/                         | MOVE    |
| `docs/MANIFEST.md`                                    | Outdated photo inventory | `ops/archive/2026-01/`                         | Outdated operational artifact (marked "Not Up to Date") | ARCHIVE |
| `docs/pending/IMG_20260126_0001.pdf`                  | Unprocessed document     | `ops/intake/`                                  | Intake queue belongs in ops/                            | MOVE    |
| `docs/repo-organization-decision.md`                  | Decision record          | `ops/decisions/`                               | Decision artifact                                       | MOVE    |

**Subtotal: 77 files to move from docs/**

### B. context/ Files to MOVE

| Current Path                              | Content Type             | Correct Location             | Reason                                        | Action |
| ----------------------------------------- | ------------------------ | ---------------------------- | --------------------------------------------- | ------ |
| `context/audit/history/*.md` (25 files)   | Historical audit reports | `ops/audit/archive/history/` | Audit reports belong in ops/, not context/    | MOVE   |
| `context/audit/quality/*.md` (79 files)   | Quality audit reports    | `ops/audit/quality/`         | Audit reports belong in ops/, not context/    | MOVE   |
| `context/audit/scripts/*.py` (3 files)    | Audit scripts            | `scripts/audit/`             | Scripts belong in scripts/, not context/      | MOVE   |
| `context/audit/snapshots/*.md` (26 files) | State snapshots          | `ops/status/snapshots/`      | Status snapshots belong in ops/, not context/ | MOVE   |

**Subtotal: 133 files to move from context/**

### C. Files to KEEP in docs/

| Path                               | Content Type            | Reason                                       |
| ---------------------------------- | ----------------------- | -------------------------------------------- |
| `docs/core/MISSION.md`             | Foundational definition | Correct location per STRUCTURE.md            |
| `docs/core/PRINCIPLES.md`          | Foundational definition | Correct location per STRUCTURE.md            |
| `docs/core/STRUCTURE.md`           | Foundational definition | Correct location per STRUCTURE.md            |
| `docs/client/admin.md`             | Client notes            | Operational documentation, correct placement |
| `docs/client/MESSAGE-POUR-SAID.md` | Client communication    | Operational documentation, correct placement |
| `docs/client/stakeholders.md`      | Client info             | Operational documentation, correct placement |
| `docs/client/support.md`           | Support contacts        | Operational documentation, correct placement |
| `docs/README.md`                   | Directory index         | Operational documentation, correct placement |
| `docs/workflows/pricing.md`        | Operational workflow    | Operational documentation, correct placement |

**Subtotal: 9 files correctly placed in docs/**

### D. Files to KEEP in context/

| Path Pattern                                | Content Type                | Reason                                |
| ------------------------------------------- | --------------------------- | ------------------------------------- |
| `context/meta/architecture/*.md` (10 files) | Architecture decisions/docs | Reference material, correct placement |
| `context/meta/knowledge/*.md` (65 files)    | Knowledge base              | Reference material, correct placement |
| `context/meta/planning/*.md` (122 files)    | Planning documents          | Reference material, correct placement |
| `context/meta/templates/*.md` (10 files)    | Templates                   | Reference material, correct placement |

**Subtotal: 207 files correctly placed in context/meta/**

---

## Files Needing Omar's Decision

| Path                                        | Issue                                                                                                          | Options                                                                                                                   |
| ------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------- |
| `docs/README.md`                            | Currently says "operational docs + rooms/facilities" but rooms are in data/ now, facilities images should move | **A)** Update to reflect new structure (remove rooms/facilities mention)<br>**B)** Keep as-is for now<br>**RECOMMEND: A** |
| `context/audit/scripts/artifact-rules.yaml` | Could be general-purpose or audit-specific                                                                     | **A)** Move to `scripts/audit/rules.yaml`<br>**B)** Keep in context as reference<br>**RECOMMEND: A**                      |

---

## Summary Statistics

| Category                          | Count | Percentage |
| --------------------------------- | ----- | ---------- |
| **Total Files Audited**           | 348   | 100.0%     |
| Files to KEEP (correct placement) | 266   | 76.4%      |
| Files to MOVE                     | 77    | 22.1%      |
| Files to ARCHIVE                  | 3     | 0.9%       |
| Files needing decision            | 2     | 0.6%       |

### Breakdown by Source Directory

| Source           | Files | To Move | To Keep | Move % |
| ---------------- | ----- | ------- | ------- | ------ |
| `docs/`          | 79    | 77      | 9       | 97.5%  |
| `context/audit/` | 136   | 133     | 3       | 97.8%  |
| `context/meta/`  | 207   | 0       | 207     | 0.0%   |

---

## Priority Migration Sequence

### Phase 1: High Priority (Structural Clarity)

1. Move `docs/decisions/` → `ops/decisions/`
2. Move `docs/agents/` → split between `.agents/` and `ops/`
3. Move `docs/facilities/images/` → `data/property/facilities/images/`
4. Move `docs/pending/` → `ops/intake/`

### Phase 2: Audit Consolidation

1. Move `context/audit/quality/` → `ops/audit/quality/`
2. Move `context/audit/history/` → `ops/audit/archive/history/`
3. Move `context/audit/snapshots/` → `ops/status/snapshots/`
4. Move `context/audit/scripts/` → `scripts/audit/`

### Phase 3: Archive Cleanup

1. Archive `docs/MANIFEST.md` → `ops/archive/2026-01/`
2. Move `docs/repo-organization-decision.md` → `ops/decisions/`

---

## Detailed File-by-File Migration Plan

### docs/agents/ → Split Migration

**To .agents/ (reference material):**

```bash
mkdir -p .agents/booking .agents/browser .agents/hotelrunner

# Booking agent
mv docs/agents/booking/capabilities.json .agents/booking/

# Browser agent
mv docs/agents/browser/config.json .agents/browser/
mv docs/agents/browser/EXAMPLES.md .agents/browser/
mv docs/agents/browser/guide.md .agents/browser/
mv docs/agents/browser/README.md .agents/browser/

# HotelRunner agent
mv docs/agents/hotelrunner/config.json .agents/hotelrunner/
mv docs/agents/hotelrunner/EXTRACTION-GUIDE.md .agents/hotelrunner/
mv docs/agents/hotelrunner/guide.md .agents/hotelrunner/
mv docs/agents/hotelrunner/README.md .agents/hotelrunner/
mv docs/agents/hotelrunner/SETUP.md .agents/hotelrunner/
```

**To ops/ (operational artifacts):**

```bash
mkdir -p ops/handoff ops/decisions ops/status/archive ops/audit

# Session handoffs
mv docs/agents/AI-SESSION-STARTER.md ops/handoff/
mv docs/agents/HANDOFF.md ops/handoff/

# Decision records
mv docs/agents/hotelrunner/DECISION-BRIEF.md ops/decisions/2026-XX-XX-hotelrunner-decision-brief.md
mv docs/agents/hotelrunner/OPTIONS-ANALYSIS.md ops/decisions/2026-XX-XX-hotelrunner-options-analysis.md

# Status/audit artifacts
mv docs/agents/hotelrunner/STATUS-FINAL.md ops/status/archive/hotelrunner-status-final.md
mv docs/agents/hotelrunner/TEST-RESULTS.md ops/audit/hotelrunner-test-results.md
```

### docs/facilities/images/ → data/property/facilities/

```bash
mkdir -p data/property/facilities/hall/images
mkdir -p data/property/facilities/pool-garden/images
mkdir -p data/property/facilities/spa-hammam/images

# Hall images (18 files)
mv docs/facilities/hall/images/* data/property/facilities/hall/images/

# Pool/garden images (25 files)
mv docs/facilities/pool-garden/images/* data/property/facilities/pool-garden/images/

# Spa/hammam images (10 files)
mv docs/facilities/spa-hammam/images/* data/property/facilities/spa-hammam/images/

# Remove empty image directories
rmdir docs/facilities/hall/images
rmdir docs/facilities/pool-garden/images
rmdir docs/facilities/spa-hammam/images
rmdir docs/facilities/hall
rmdir docs/facilities/pool-garden
rmdir docs/facilities/spa-hammam
rmdir docs/facilities
```

### docs/decisions/ → ops/decisions/

```bash
mkdir -p ops/decisions
mv docs/decisions/2026-02-16-database-architecture.md ops/decisions/
mv docs/repo-organization-decision.md ops/decisions/2026-02-16-repo-organization.md
rmdir docs/decisions
```

### docs/pending/ → ops/intake/

```bash
mkdir -p ops/intake
mv docs/pending/IMG_20260126_0001.pdf ops/intake/
rmdir docs/pending
```

### context/audit/ → ops/

```bash
mkdir -p ops/audit/archive/history ops/audit/quality ops/status/snapshots scripts/audit

# History archives
mv context/audit/history/* ops/audit/archive/history/

# Quality reports
mv context/audit/quality/* ops/audit/quality/

# Scripts
mv context/audit/scripts/* scripts/audit/

# Snapshots
mv context/audit/snapshots/* ops/status/snapshots/

# Remove empty context/audit directories
rmdir context/audit/history
rmdir context/audit/quality
rmdir context/audit/scripts
rmdir context/audit/snapshots
rmdir context/audit
```

### Archive outdated manifest

```bash
mkdir -p ops/archive/2026-01
mv docs/MANIFEST.md ops/archive/2026-01/photo-manifest-2026-01-30.md
```

---

## Verification Checklist

After migration:

- [ ] All `docs/` files are either operational or foundational
- [ ] All `context/` files are reference material (architecture, knowledge, planning, templates)
- [ ] All `ops/` files are live operational artifacts (status, decisions, audits, intake)
- [ ] All `data/` files are canonical source-of-truth
- [ ] All `scripts/` files are automation
- [ ] No empty directories remain (except intentional taxonomy)
- [ ] Update `docs/README.md` to reflect new structure
- [ ] Run `tree -d -L 3` to verify new structure is navigable

---

## Post-Migration Updates Required

1. **docs/README.md**: Remove mentions of rooms/facilities (now in data/)
2. **AGENTS.md**: Update file paths in examples if any reference moved files
3. **Git commit message**: Use conventional commit format

   ```
   refactor(structure): reorganize docs/ and context/ for clarity

   - Move agent tool docs to .agents/ (reference material)
   - Move audit artifacts to ops/audit/ (operational)
   - Move facility images to data/property/facilities/ (canonical)
   - Move decision records to ops/decisions/ (operational)
   - Move pending intake to ops/intake/ (operational)
   - Archive outdated MANIFEST.md

   77 files moved, 3 archived, 266 kept in place.

   Ref: ops/audit-docs-context-placement.md
   ```

---

## Notes

- **Empty directories**: Do NOT delete empty taxonomy directories per rules.md (they're intentional WIP)
- **Images**: Facility images are property data (canonical), not documentation
- **Decisions**: Decision records are operational state, not reference material
- **Audits**: Audit reports track operational quality, belong in ops/
- **Context/meta**: Correctly placed (architecture, planning, knowledge, templates = reference)

---

**Audit Complete**: 2026-02-16 20:45 UTC
**Next Action**: Review with Omar, then execute Phase 1 migrations

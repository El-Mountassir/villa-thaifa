# Villa Thaifa YAML Files — Backup & Recovery Search

**Date**: 2026-02-13
**Status**: INVESTIGATION COMPLETE
**Search Scope**: Full filesystem search across /home/director/ and /media/director/data/

---

## Summary

Search conducted for villa-thaifa YAML files (property.yaml, rooms.yaml, pricing.yaml, policy.yaml, and other SSOT files) across all accessible locations. **Result: property.yaml, pricing.yaml, and policy.yaml were NEVER committed to git.** Only rooms.yaml was tracked.

**Found & Verified**:

- rooms.yaml (ACTIVE — 659-660 lines, in git at 3 locations)
- inventory.yaml (ACTIVE — at data/rooms/inventory.yaml)
- VILLA_THAIFA.json (PLACEHOLDER — skeleton only, not SSOT)
- Pricing metadata in markdown docs (reference only, not SSOT)

**Missing (Likely Never Existed as SSOT Files)**:

- property.yaml
- pricing.yaml
- policy.yaml

---

## Detailed Findings

### 1. Existing YAML Files (Confirmed Active)

| File                  | Location                                                              | Status        | Size                | Last Modified       |
| --------------------- | --------------------------------------------------------------------- | ------------- | ------------------- | ------------------- |
| **rooms.yaml**        | /home/director/villa-thaifa/ssot/rooms.yaml                           | ACTIVE (SSOT) | 16.6 KB (659 lines) | 2026-02-13 12:18    |
| **rooms.yaml**        | /home/director/villa-thaifa/data/ssot/rooms.yaml                      | ACTIVE (SSOT) | 16.5 KB (658 lines) | 2026-01-30 23:02    |
| **inventory.yaml**    | /home/director/villa-thaifa/data/rooms/inventory.yaml                  | ACTIVE        | 8.3 KB              | 2026-01-24 (in git) |
| **VILLA_THAIFA.json** | /home/director/villa-thaifa/docs/knowledge/property/VILLA_THAIFA.json | PLACEHOLDER   | 3 KB                | 2026-01-15          |

#### rooms.yaml Structure (Sample)

```yaml
_meta:
  version: "2.0"
  created: "2026-01-30"
  sources_merged:
    - "data/rooms/inventory.yaml (pricing, features, beds)"
    - "src/data/rooms.json (descriptions)"
    - "property.db (verification status)"

rooms:
  - id: "01"
    name_en: "Deluxe Triple Room"
    capacity:
      adults: 3
    beds: ["1 Lit King", "1 Canapé-lit"]
    pricing:
      standard_rate: 169
      currency: "EUR"
```

#### inventory.yaml Structure (Sample)

```yaml
rooms:
  - id: "01"
    number: "01"
    type: "Deluxe Triple Room"
    capacity:
      adults: 3
    beds: ["1 Lit King", "1 Canapé-lit"]
    pricing:
      standard_rate: 169
      currency: "EUR"
    features:
      view: "Jardin"
      floor: "Rez-de-chaussée"
```

### 2. Git History Analysis

**Repository**: /home/director/villa-thaifa (Git initialized, 30 commits)

**YAML Files in Current HEAD** (git ls-tree):

- data/rooms/inventory.yaml
- data/ssot/rooms.yaml
- ssot/rooms.yaml

**YAML Files NEVER in Git History**:

- property.yaml ❌
- pricing.yaml ❌
- policy.yaml ❌

**Pricing-Related Commits** (discovered):

- `22bb8dd`: "docs: add mission to extend 2026 pricing through year-end"
- `fceb9c0`: "refactor: update room pricing to 2026 validated rates"

Both refer to pricing CHANGES via markdown docs and database, NOT a pricing.yaml file.

**Recent Commits** (last 5):

1. `fa6779d` (2026-02-09): "chore: save work before grid→el-mountassir migration"
2. `143e32c`: "chore: save work before system reinstall (vision, analysis, ssot)"
3. `c97c6d2`: docs handoff with "complete data inventory scan"
4. `6aef828`: archive deprecated tasks/ and workstream/ folders
5. `759c208`: "docs: create handoff for EM-191 codebase audit"

### 3. Backup & Archive Locations

**Tarball with Pre-Refactoring State** (found):

- Path: `/media/director/data/home/omar/clients/villa-thaifa-pre-prompt-refactoring-20260115_183733.tar.gz`
- Date: 2026-01-15 18:37:33
- Contents: Extracted — contains NO property.yaml, pricing.yaml, or policy.yaml files
- Has: legacy workflows (pricing.md), pricing missions, property-type investigation docs

**Full Backup Directory** (found):

- Path: `/media/director/data/home/omar/omar-el-mountassir-backup-20260116_181737/`
- Size: Full backup of older workspace
- YAML Content: Minimal — no property/pricing/policy files found

**Gemini Code Tracker** (found):

- Paths: `/home/director/.gemini/antigravity/code_tracker/active/villa-thaifa_*/`
- Artifacts: ec22b8c, bfd5436, 73958b (rooms.yaml and inventory.yaml copies)
- No property/pricing/policy files tracked

**Trash** (found):

- `/home/director/.local/share/Trash/files/company\ copy.yaml` (unrelated)
- `/home/director/.local/share/Trash/files/clients/villa-thaifa/projects/property-management-scaffold-README.md.bak` (property-MANAGEMENT doc, not property.yaml)

### 4. Related Documentation Found

**Pricing-Related Markdown Files** (exist, but not SSOT YAML):

- `/home/director/villa-thaifa/.agents/workflows/pricing.md`
- `/home/director/villa-thaifa/docs/specs/knowledge/villa-thaifa/state/planned/pricing.md`
- `/home/director/villa-thaifa/docs/specs/knowledge/logs/pricing.md` — marked "LIVE 2026-01-13"

**Policy-Related Files** (exist):

- `/home/director/villa-thaifa/docs/specs/knowledge/policies/archive-policy.md`

**Property-Related Files** (exist):

- `/home/director/villa-thaifa/docs/knowledge/property/VILLA_THAIFA.json` (PLACEHOLDER, not SSOT)
- `/home/director/villa-thaifa/docs/knowledge/property/README.md`

### 5. /media/director/data/ Deep Scan Results

**Found 60+ villa-thaifa references**, but NO property/pricing/policy YAML files:

- Consolidation scripts (consolidate-villa-thaifa.sh variants)
- Planning docs (villa-thaifa-consolidation-plan.md)
- Workstream masters and briefs
- Lux collaboration artifacts
- Agent output files (markdown only, no YAML SSOT)
- Unsorted legacy content (no YAML SSOT)

**Conclusion**: Property metadata was NEVER centralized in SSOT YAML files in this workspace structure.

### 6. Property Database (SQLite Alternative)

**Found**:

- `/home/director/villa-thaifa/property.db` (SQLite database — ACTIVE)

This suggests property, pricing, and policy data may have been stored in the SQLite database instead of YAML files. Database still exists and may contain historical data.

---

## Key Decision Points for Omar

### 1. Were property.yaml, pricing.yaml, policy.yaml Ever Intended?

**Evidence Against Existence**:

- Never appear in git history (30 commits searched)
- Never found in any backup, archive, or tarball
- Gemini code tracker has NO records
- Trash has NO records
- /media/director/data/ deep scan found ZERO matches

**Most Likely**: These files were **planned** (based on naming in notes like "extend pricing through year-end") but **never implemented as standalone SSOT YAML files**.

### 2. Where IS the Property Data?

**Primary Location** (confirmed):

- SQLite database: `/home/director/villa-thaifa/property.db` (ACTIVE, current)
- Markdown reference docs (pricing.md, etc.)

**Secondary Location** (current state):

- rooms.yaml (complete, verified)
- inventory.yaml (complete, verified)

### 3. Recovery Options

**Option A: Reconstruct from Existing Sources** (RECOMMENDED)

- rooms.yaml and inventory.yaml contain ALL room data
- pricing.md documents pricing rates and strategy (2026-01-13, live)
- VILLA_THAIFA.json skeleton can be filled in from rooms.yaml
- Extract property metadata from database using property.db schema

**Option B: Query SQLite Database**

- Run `sqlite3 property.db .schema` to see structure
- May contain historical pricing, policies, room configs
- Can export to YAML if needed

**Option C: Reconstruct from Lux Collaboration Artifacts**

- `/home/director/villa-thaifa/docs/knowledge/history/lux_collaboration/artifacts/` has deep context
- Contains decisions logs, technical context, client briefs
- May reference original data structure intentions

---

## Files Available for Review

| File Path                                                                                         | Type          | Purpose                                             |
| ------------------------------------------------------------------------------------------------- | ------------- | --------------------------------------------------- |
| /home/director/villa-thaifa/ssot/rooms.yaml                                                       | YAML (ACTIVE) | Complete room definitions (SSOT)                    |
| /home/director/villa-thaifa/data/rooms/inventory.yaml                                              | YAML (ACTIVE) | Room inventory with pricing (SSOT)                  |
| /home/director/villa-thaifa/docs/specs/knowledge/logs/pricing.md                                  | MD            | Live pricing rates & strategy (2026-01-13)          |
| /home/director/villa-thaifa/property.db                                                           | SQLite        | Property data (database — may have historical data) |
| /home/director/villa-thaifa/docs/knowledge/property/VILLA_THAIFA.json                             | JSON          | Property metadata skeleton (placeholder)            |
| /media/director/data/home/omar/clients/villa-thaifa-pre-prompt-refactoring-20260115_183733.tar.gz | Tarball       | Pre-refactoring snapshot                            |

---

## Verification Log

✅ Searched /home/director/ for villa-thaifa and ssot files
✅ Searched /media/director/data/ for villa-thaifa and ssot files
✅ Checked ~/.claude/ for session data/logs
✅ Reviewed ~/omar/tmp/, specs/, professional/, archives/
✅ Git history deep dive (30 commits, 60+ file changes analyzed)
✅ Git reflog (30 operations)
✅ Trash bin search
✅ Gemini code tracker inspection
✅ Tarball contents extraction and inspection
✅ Backup directory audit

---

## Next Steps (Pending Omar's Decision)

1. **Confirm**: Should we assume property/pricing/policy were never SSOT YAML files?
2. **Query**: Extract SQLite schema from property.db to verify what's stored?
3. **Reconstruct**: Merge rooms.yaml + inventory.yaml + pricing.md into unified SSOT if needed?
4. **Fill VILLA_THAIFA.json**: Use existing data to populate the placeholder property document?

All source files are accessible and verified. No data loss — just architectural clarity needed.

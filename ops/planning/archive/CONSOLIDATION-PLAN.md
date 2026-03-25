# Consolidation Plan — Villa Thaifa Data Migration

**Created**: 2026-01-30
**Linear Issue**: [EM-191](https://linear.app/el-mountassir/issue/EM-191)

---

## Guiding Principles

1. **NO DATA LOSS** — Everything archived, nothing deleted
2. **Progressive** — One step at a time, verify each step
3. **Reversible** — Can rollback at any point
4. **Dual Currency** — EUR and MAD both preserved

---

## Phase Overview

| Phase | Name | Effort | Risk |
|-------|------|--------|------|
| 1 | Create SSOT file | Low | Low |
| 2 | Build sync tooling | Medium | Low |
| 3 | Deprecate old files | Low | Medium |
| 4 | Update code references | Medium | Medium |
| 5 | Populate placeholders | High | Low |

---

## Phase 1: Create SSOT File

**Goal**: Merge inventory.yaml + rooms.json into unified SSOT

### Tasks

- [ ] Create `data/ssot/` directory
- [ ] Create `data/ssot/rooms.yaml` with new schema
- [ ] Merge data from:
  - `data/rooms/inventory.yaml` (pricing, features, beds)
  - `src/data/rooms.json` (descriptions)
  - `property.db` rooms table (MAD prices, verification status)
- [ ] Add `_meta` section with conversion rate (EUR→MAD = 11.0)
- [ ] Verify all 12 rooms present with complete data

### Validation

```bash
# Check room count
grep -c "^  - id:" data/ssot/rooms.yaml  # Should be 12

# Verify dual pricing
grep "base_rate_eur\|base_rate_mad" data/ssot/rooms.yaml
```

### Deliverable

```yaml
# data/ssot/rooms.yaml — complete, validated, dual-currency
```

---

## Phase 2: Build Sync Tooling

**Goal**: Create script to generate outputs from SSOT

### Tasks

- [ ] Create `scripts/sync-rooms.ts`
- [ ] Implement YAML → JSON converter
- [ ] Implement YAML → SQLite sync
- [ ] Add validation (schema, conversion rate check)
- [ ] Add `npm run sync:rooms` command

### Script Behavior

```
Input:  data/ssot/rooms.yaml
Output:
  - data/generated/rooms.json (EUR for Next.js)
  - property.db rooms table (updated)

Warnings:
  - "Room 07: MAD price 3620 differs from EUR×11 (3619)"
```

### Deliverable

```bash
npm run sync:rooms  # Works, generates outputs
```

---

## Phase 3: Deprecate Old Files

**Goal**: Mark old files as deprecated, not authoritative

### Tasks

- [ ] Add deprecation header to `data/rooms/inventory.yaml`:
  ```yaml
  # ⚠️ DEPRECATED — See data/ssot/rooms.yaml
  # Kept for reference only. DO NOT EDIT.
  ```
- [ ] Add deprecation header to `src/data/rooms.json`:
  ```json
  {
    "_deprecated": "See data/ssot/rooms.yaml — this file is auto-generated",
    ...
  }
  ```
- [ ] Update `.gitignore` to ignore `data/generated/`
- [ ] Document deprecation in `data/README.md`

### Validation

- Old files still exist (no data loss)
- New SSOT is clearly marked as authoritative
- Generated files are gitignored

---

## Phase 4: Update Code References

**Goal**: Point application code to new data sources

### Tasks

- [ ] Find all imports of `src/data/rooms.json`
- [ ] Update to use `data/generated/rooms.json`
- [ ] Find all direct SQLite queries for room data
- [ ] Ensure they work with updated schema
- [ ] Run test suite

### Search Commands

```bash
# Find room data imports
grep -r "rooms.json" src/ --include="*.ts" --include="*.tsx"
grep -r "inventory.yaml" . --include="*.ts" --include="*.tsx"
grep -r "property.db" src/ --include="*.ts" --include="*.tsx"
```

### Validation

```bash
npm run build  # No errors
npm run test   # All pass
```

---

## Phase 5: Populate Placeholders

**Goal**: Fill in actual data for facilities, rates, etc.

### Tasks

- [ ] Create `data/ssot/facilities.yaml` from actual property data
- [ ] Create `data/ssot/rates.yaml` with real pricing rules
- [ ] Remove placeholder values ("A confirmer", "TODO")
- [ ] Mark remaining unknowns with `null` + comment

### Validation

```bash
# No placeholders remaining
grep -r "A confirmer\|TODO" data/ssot/
```

---

## Rollback Procedure

If any phase fails:

1. **Phase 1**: Delete `data/ssot/` — no impact
2. **Phase 2**: Delete `scripts/sync-rooms.ts` — no impact
3. **Phase 3**: Remove deprecation headers
4. **Phase 4**: `git checkout src/` to restore old imports
5. **Phase 5**: No rollback needed (additive only)

---

## Archive Plan

After successful migration:

```bash
# Archive deprecated files (don't delete)
mkdir -p archive/pre-ssot-migration-2026-01
mv data/rooms/inventory.yaml archive/pre-ssot-migration-2026-01/
# Keep src/data/rooms.json as auto-generated
```

---

## Timeline Estimate

| Phase | Dependency | Estimate |
|-------|------------|----------|
| 1 | None | 1-2 hours |
| 2 | Phase 1 | 2-4 hours |
| 3 | Phase 2 | 30 min |
| 4 | Phase 2 | 1-2 hours |
| 5 | Owner input | Variable |

**Total**: ~6-8 hours of agent work + owner validation

---

## Success Criteria

- [ ] Single file (`data/ssot/rooms.yaml`) contains all room data
- [ ] Both EUR and MAD prices stored explicitly
- [ ] Sync script regenerates derived files
- [ ] No duplicate maintenance required
- [ ] All 12 rooms verified complete
- [ ] Application builds and runs correctly

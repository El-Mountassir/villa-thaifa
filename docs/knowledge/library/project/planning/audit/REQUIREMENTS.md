# Requirements — Villa Thaifa Data Architecture

**Created**: 2026-01-30
**Linear Issue**: [EM-191](https://linear.app/el-mountassir/issue/EM-191)

---

## Owner Requirements

These requirements come directly from Omar (Chairman/Admin) and are **non-negotiable**.

### REQ-001: Dual Currency Support (EUR + MAD)

**Source**: Omar, 2026-01-30
**Priority**: MUST HAVE

> "We need to be able to have both values EUR and MAD if possible! The issue is the conversion rate or the logic."

**Implementation**:
- Store BOTH `base_rate_eur` and `base_rate_mad` explicitly
- Do NOT compute on-the-fly (avoids precision issues)
- Store conversion rate in metadata for audit
- Allow manual override for rounded prices

**Example**:
```yaml
pricing:
  base_rate_eur: 169
  base_rate_mad: 1812  # Stored, not computed (169 × 10.72)
  conversion_rate_used: 10.72
  rate_date: "2026-01-30"
```

---

### REQ-002: No Data Loss

**Source**: Omar (implied by context)
**Priority**: MUST HAVE

> "I really want to delete everything but I can't"
> "2+ months of work that can't be deleted"

**Implementation**:
- Archive everything, delete nothing
- Progressive migration, not big-bang
- Keep deprecated files with clear headers

---

### REQ-003: Single Source of Truth

**Source**: EM-191 scope
**Priority**: MUST HAVE

**Implementation**:
- One YAML file for all room data
- Generated files are clearly marked as derived
- No manual editing of generated files

---

## Resolved Questions

| Question | Answer | Source |
|----------|--------|--------|
| EUR→MAD rate | **10.72** (not 11.0) | XE.com, Jan 2026 |
| Rate update frequency | **Weekly** | Industry best practice |

## Open Questions (Need Owner Input)

| Question | Context | Default |
|----------|---------|---------|
| Price rounding | 1812 vs 1800 (rounded) | Exact |
| Facilities data | Who provides actual values? | Said (Owner) |

---

## REQ-004: Correct Exchange Rate

**Source**: Web research, 2026-01-30
**Priority**: MUST HAVE

**Finding**: Current DB uses rate 11.0, but correct EUR→MAD rate is **10.72**.

**Impact**: All existing MAD prices are ~2.6% inflated and need recalculation.

**Implementation**:
- Use rate **10.72** for all new conversions
- Verify rate weekly (XE.com or ECB)
- See `~/grid/memory/knowledge/patterns/currency-handling.md` for full details

---

## Stakeholder Reference

See [STAKEHOLDERS.md](../../docs/leadership/STAKEHOLDERS.md) for roles:
- **Said** (Owner) — Property knowledge authority
- **Omar** (Admin) — Technical decisions authority

# Changelog — Booking.com Promotions

**Last updated**: 2025-12-20
**Format**: Reverse chronological (newest first)

---

## [2025-12-20] Audit V2 — Complete Documentation

### Changes

| Action | Detail |
|--------|--------|
| **Identified** | 3 undocumented promotions |

### Discovered Promotions

| Promotion | Discount | Performance | Status |
|-----------|----------|-------------|--------|
| Early Booker Deal | 10% | -- | ✅ NEW (compliant) |
| Mobile Rate | 10% | 27 bookings, €15,614 | ✅ Performing |
| Abroad (geo-targeted) | 10% | 2 bookings, €160 | ✅ OK |

### Impact

- All promotions now documented
- All within optimal range (10-15%)
- No corrective action required

---

## [2025-12-20] Cleanup Plan Execution

### Changes

| Action | Quantity | Detail |
|--------|----------|--------|
| **P0 Deactivations** | 6 | Destructive promotions |
| **P1 Reductions** | 2 | Percentage adjustments |

### Deactivations (6)

| Promotion | Discount | Reason |
|-----------|----------|--------|
| Early Booker Deal | 40% | Insufficient margin |
| Basic Deal | 38% | Insufficient margin |
| Late Escape Deal | 43% | Destructive discount |
| Late Escape Deal | 42% | Destructive discount |
| Geo-targeted Europe | 10% | Stacking risk (overestimated) |
| Geo-targeted Morocco | 10% | Stacking risk (overestimated) |

### Reductions (2)

| Promotion | Before | After |
|-----------|--------|-------|
| Basic Deal (3 nights min) | 33% | **15%** |
| Basic Deal (Standard) | 30% | **10%** |

### Impact

- Active promotions: 8 → 5
- Max discount: 43% → 15%
- Max combined impact: ~58% → ~35%

---

## [2025-12-20] Initial Audit

### Discovered State

| Metric | Value | Problem |
|--------|-------|---------|
| Active promotions | **8** | Too many |
| Maximum discount | **43%** | Destructive |
| Promotions > 30% | **5** | Negative margins |

### Identified Promotions

| # | Promotion | Discount | Status |
|---|-----------|----------|--------|
| 1 | Basic Deal | 30% | Too high |
| 2 | Basic Deal | 33% | Too high |
| 3 | Basic Deal | 38% | Destructive |
| 4 | Early Booker Deal | 40% | Destructive |
| 5 | Late Escape Deal | 43% | Destructive |
| 6 | Late Escape Deal | 42% | Destructive |
| 7 | Geo-targeted Europe | 10% | Stacking risk |
| 8 | Geo-targeted Morocco | 10% | Stacking risk |

### Decision

Cleanup plan validated by M. Said Thaifa.

---

## Baseline

→ State before audit: [../baseline/promotions-2025-12-20.md](../baseline/promotions-2025-12-20.md)

---

_Promotions changelog — append-only_
_Updated on 2025-12-20_

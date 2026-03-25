# Dedup Report — 2026-03-25

**Scope**: archive/missions/ vs archive/planning/ (Task 2.1) + archive/audit/ flat files vs archive/audit/reports/ (Task 2.2)
**Method**: `diff -q` byte-for-byte comparison. Delete ONLY if IDENTICAL confirmed.
**Status**: Staged (not committed). 32 files staged for deletion.

---

## Task 2.1 — archive/missions/ vs archive/planning/

| File | Action | Evidence |
|------|--------|----------|
| 2025-12-23-thaifa-booking-data.md | `git rm` staged | IDENTICAL |
| 2025-12-23-thaifa-image-organization.md | `git rm` staged | IDENTICAL |
| 2025-12-23-thaifa-room-restructuring.md | `git rm` staged | IDENTICAL |
| 2025-12-23-thaifa-validation-pdf.md | `git rm` staged | IDENTICAL |
| 2025-12-28-thaifa-chambre4-gouram.md | KEPT (both copies) | DIFFERS — whitespace/table alignment only |
| 2025-12-28-thaifa-chambre5-sync-investigation.md | KEPT (both copies) | DIFFERS — trailing newlines + table alignment |
| 2025-12-28-thaifa-hotelrunner-api-scout.md | KEPT (both copies) | DIFFERS — language (EN in missions/, FR in planning/) |
| 2025-12-29-thaifa-hotelrunner-admin-access.md | KEPT (both copies) | DIFFERS — language (EN in missions/, FR in planning/) |
| 2026-01-08-thaifa-property-type-investigation.md | KEPT (both copies) | DIFFERS — table alignment only |
| archive/missions/README.md | KEPT | No equivalent in planning/ |

**Result**: 4 deleted, 5 kept (DIFFERS), README kept. archive/missions/ still has 6 files — NOT empty, NOT removed.

---

## Task 2.2 — archive/audit/ flat files vs archive/audit/reports/

Full scan of all flat `.md` files at archive/audit/ root for same-named matches anywhere under archive/audit/reports/.

| Flat file | Reports/ counterpart | Action | Evidence |
|-----------|----------------------|--------|----------|
| 2025-12-19-exploration-reservations-hotelrunner.md | reports/2025-12-19-exploration-reservations-hotelrunner.md | `git rm` staged | IDENTICAL |
| 2025-12-19-rapport-reservations-said.md | reports/2025-12-19-rapport-reservations-said.md | `git rm` staged | IDENTICAL |
| 2025-12-20-rapport-reservations-v2.md | reports/2025-12-20-rapport-reservations-v2.md | `git rm` staged | IDENTICAL |
| 2025-12-20-resilience-erreurs-techniques.md | reports/2025-12-20-resilience-erreurs-techniques.md | `git rm` staged | IDENTICAL |
| audit-promotions-booking.md | reports/pricing-strategy-session/audit-promotions-booking.md | `git rm` staged | IDENTICAL |
| blocage-prix-booking.md | reports/hotelrunner-demo/blocage-prix-booking.md | `git rm` staged | IDENTICAL |
| client-profile-optimization-final.md | reports/client-profile-optimization/final.md | `git rm` staged | IDENTICAL |
| client-profile-optimization-patterns.md | reports/client-profile-optimization/patterns.md | `git rm` staged | IDENTICAL |
| client-profile-optimization-sources.md | reports/client-profile-optimization/sources.md | `git rm` staged | IDENTICAL |
| client-profile-optimization-step-back.md | reports/client-profile-optimization/step-back.md | `git rm` staged | IDENTICAL |
| client-profile-optimization-synthesis.md | reports/client-profile-optimization/synthesis.md | `git rm` staged | IDENTICAL |
| execution-log-booking.md | reports/pricing-strategy-session/execution-log-booking.md | `git rm` staged | IDENTICAL |
| execution-log-hotelrunner.md | reports/pricing-strategy-session/execution-log-hotelrunner.md | `git rm` staged | IDENTICAL |
| plan-promotions-booking.md | reports/pricing-strategy-session/plan-promotions-booking.md | `git rm` staged | IDENTICAL |
| pm-template-selection-final.md | reports/pm-template-selection/final.md | `git rm` staged | IDENTICAL |
| pm-template-selection-patterns.md | reports/pm-template-selection/patterns.md | `git rm` staged | IDENTICAL |
| pm-template-selection-sources.md | reports/pm-template-selection/sources.md | `git rm` staged | IDENTICAL |
| pm-template-selection-step-back.md | reports/pm-template-selection/step-back.md | `git rm` staged | IDENTICAL |
| pm-template-selection-synthesis.md | reports/pm-template-selection/synthesis.md | `git rm` staged | IDENTICAL |
| project_standards.md | reports/pm-template-selection/project_standards.md | `git rm` staged | IDENTICAL |
| prompt-en.md | reports/pm-template-selection/prompt-en.md | `git rm` staged | IDENTICAL |
| prompt.md | reports/pm-template-selection/prompt.md | `git rm` staged | IDENTICAL |
| rapport-audit-v2.md | reports/audit-promotions-v2/rapport-audit-v2.md | `git rm` staged | IDENTICAL |
| rapport-demo-20-dec-2025.md | reports/hotelrunner-demo/rapport-demo-20-dec-2025.md | `git rm` staged | IDENTICAL |
| rapport-promotions-msaid.md | reports/pricing-strategy-session/rapport-promotions-msaid.md | `git rm` staged | IDENTICAL |
| rapport-session-20-dec-2025.md | reports/pricing-strategy-session/rapport-session-20-dec-2025.md | `git rm` staged | IDENTICAL |
| rdv-prep-agenda.md | reports/profile-reorganization/rdv-prep-agenda.md | `git rm` staged | IDENTICAL |
| rdv-prep-checklist.md | reports/profile-reorganization/rdv-prep-checklist.md | `git rm` staged | IDENTICAL |
| 2025-12-29-sync-investigation.md | reports/2025-12-29-sync-investigation.md | KEPT (both) | DIFFERS |
| 2026-01-08-property-type-scout-report.md | reports/2026-01-08-property-type-scout-report.md | KEPT (both) | DIFFERS |

**Result**: 28 flat files staged for deletion. 2 kept (DIFFERS). Canonical copies preserved in reports/ subdirs.

---

## Summary

| Task | Files staged for deletion | Files kept (DIFFERS) | Files kept (no match) |
|------|--------------------------|----------------------|-----------------------|
| 2.1 archive/missions/ | 4 | 5 | 1 (README.md) |
| 2.2 archive/audit/ flat | 28 | 2 | ~60 (no match in reports/) |
| **Total** | **32** | **7** | — |

All staged deletions confirmed IDENTICAL by `diff -q`. No guesses, no assumptions.
archive/missions/ is NOT empty — rmdir NOT performed.

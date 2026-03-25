# Assessment: .archived/ Directory

**Date:** 2026-02-22
**Status:** Completed

## Summary
The `.archived/` directory contains legacy rules, strategic documents from late 2025, and old operational workflows. These files represent previous iterations of the Villa Thaifa operating system (v0.1.0-alpha). Most have been superseded by the current `docs/`, `rules/`, and `context/` structures, but they contain valuable historical context on strategy (direct bookings vs OTAs) and early workflow definitions.

## File Assessments

### 1. `.archived/rules/README.md`
- **Summary:** A brief 9-line file defining 4 core rules (Resilience, Anti-Dodge, SSOT, STOP & ASK).
- **Current Equivalent:** `rules/rules.md` (comprehensive rules file).
- **Recommendation:** **DELETE**. The core principles are fully integrated into the active `rules/rules.md`. This file provides no unique historical value.

### 2. `.archived/strategic/2025-12-28-platform-mastery-strategy.md`
- **Summary:** A detailed strategic analysis of the "Platform Mastery" project, focusing on the economic impact of commissions (25%), the knowledge gap regarding HotelRunner/Booking.com sync, and a proposed multi-phase plan to master these platforms.
- **Current Equivalent:** `context/meta/planning/` or `ops/decisions/` likely contain evolved versions, but this specific strategic snapshot is valuable.
- **Recommendation:** **KEEP**. This is a high-quality "Decision Record" or "Strategy Paper" that explains the *why* behind current operations. It should eventually be moved to `archive/2025/strategy/` or `context/meta/history/` to preserve the reasoning, but for now, it is safely stored in `.archived`.

### 3. `.archived/workflows/CLAUDE.md`
- **Summary:** A meta-document describing the purpose of the workflow files in this directory and defining the "SCOUT → REPORT → QUESTIONS → ACTION" pattern.
- **Current Equivalent:** `docs/workflows/README.md` or similar meta-documentation in `docs/workflows/`.
- **Recommendation:** **DELETE**. The patterns described here are now standard operating procedure defined in `AGENTS.md` and `rules/rules.md`.

### 4. `.archived/workflows/guest-communication.md`
- **Summary:** Defines protocols for guest communication (vouvoiement, message formats for WhatsApp/Email).
- **Current Equivalent:** `docs/workflows/guest-communication.md` (or similar active workflow).
- **Recommendation:** **ARCHIVE/MERGE**. Check if the specific templates (WhatsApp 1st message vs follow-up) are preserved in the active documentation. If yes, delete. If no, migrate useful templates to `docs/workflows/` then delete.

### 5. `.archived/workflows/pricing.md`
- **Summary:** Process for updating tariffs on HotelRunner/Booking.com, including a baseline capture and validation steps.
- **Current Equivalent:** `docs/workflows/pricing.md`.
- **Recommendation:** **ARCHIVE/MERGE**. Similar to guest communication, ensure the "Baseline → Plan → Confirm → Execute" rigour is present in the current workflow.

### 6. `.archived/workflows/reservation.md`
- **Summary:** Step-by-step process for creating reservations on HotelRunner manually, emphasizing the "PARSE → VERIFY → REPEAT BACK" pattern.
- **Current Equivalent:** `docs/workflows/reservation.md`.
- **Recommendation:** **ARCHIVE/MERGE**. The "REPEAT BACK" pattern is a critical safety mechanism. Ensure it's in the live docs.

## Conclusion
The `.archived/` directory serves as a holding pen for v0.1.0 artifacts. 
- The **rules** and **meta-docs** are obsolete and safe to delete.
- The **strategy document** is valuable context and should be preserved in the proper `archive/` structure.
- The **workflows** contain specific operational wisdom (templates, safety checks) that must be verified against current `docs/workflows/` before deletion.

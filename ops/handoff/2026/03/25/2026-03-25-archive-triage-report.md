# Archive Triage Report — 2026-03-25

Tasks completed: F-028, F-029, F-030, F-031, F-032, F-018

---

## Triage Table: .agents/archive/

| Old path | Action | New path | Reason |
|---|---|---|---|
| `.agents/archive/baseline.md` | git rm (duplicate) | `data/archive/promotions-baseline-2025-12-20.md` (existing) | Exact duplicate confirmed via diff |
| `.agents/archive/current.md` | git mv | `data/archive/booking-promotions-state-2025-12-20.md` | Booking promotions state snapshot 2025-12-20 |
| `.agents/archive/chambre_et_vue.md` | git mv | `.agents/hotelrunner/chambre-et-vue-said-notes.md` | Said's room/view notes — HotelRunner domain |
| `.agents/archive/claude-code-hotelrunner-investigation-prompt.md` | git mv | `.agents/hotelrunner/sync-investigation-prompt.md` | HotelRunner sync investigation prompt |
| `.agents/archive/legacy_transfer.md` | git mv | `.agents/hotelrunner/legacy-transfer-lessons.md` | HotelRunner operational lessons (bulk update, XML lock) |
| `.agents/archive/platform-mapping.md` | git mv | `.agents/hotelrunner/platform-mapping-superseded.md` | Rooms-to-types mapping, marked SUPERSEDED in content |
| `.agents/archive/reservation.md` | git mv | `.agents/hotelrunner/reservation-workflow.md` | HotelRunner reservation creation workflow |
| `.agents/archive/support-README.md` | git mv | `.agents/hotelrunner/support-contacts.md` | HWS support contact (Ikram, +212 717 51 85 92) |
| `.agents/archive/Expedia_Group_Partner_Central.md` | rename + git mv | `.agents/booking/expedia-group-partner-central.md` | Expedia onboarding step 5 (rooms and rates) |
| `.agents/archive/expedia_central_partner.md` | rename + git mv | `.agents/booking/expedia-central-partner-onboarding-steps.md` | Expedia onboarding steps 1-3 |
| `.agents/archive/Onboarding.md` | rename + git mv | `.agents/booking/expedia-onboarding-amenities-step4.md` | Expedia onboarding step 4 (amenities) |
| `.agents/archive/Onboarding_-_Policies_and_Settings.md` | rename + git mv | `.agents/booking/expedia-onboarding-policies-step3.md` | Expedia onboarding step 3 (policies and settings) |
| `.agents/archive/OVERVIEW.md` | rename (kebab) | `.agents/archive/overview.md` | Keep in archive — generic project overview card |
| All 21 remaining files | keep in place | `.agents/archive/` | Historical: Gemini prompts, governance, placeholders, investigations |

---

## archive/ tasks

| Old path | Action | New path | Task |
|---|---|---|---|
| `archive/reviews/agentic-loop-external-review.md` | cp + git rm | `~/omar/core/context/domains/ai/reviews/` | F-031 |
| `archive/reviews/agentic-loop-review-package.md` | cp + git rm | `~/omar/core/context/domains/ai/reviews/` | F-031 |
| `archive/reviews/agentic-loop-review-prompt.md` | cp + git rm | `~/omar/core/context/domains/ai/reviews/` | F-031 |
| `archive/reviews/kilo-agentic-loop-review-2.md` | cp + git rm | `~/omar/core/context/domains/ai/reviews/` | F-031 |
| `archive/reviews/kilo-agentic-loop-review.md` | cp + git rm | `~/omar/core/context/domains/ai/reviews/` | F-031 |
| `archive/reviews/kimi-agentic-loop-review.md` | cp + git rm | `~/omar/core/context/domains/ai/reviews/` | F-031 |
| `archive/audit_rooms.py` | git mv | `scripts/archive/audit_rooms.py` | F-032 |

---

## ops/audit/archive/history/ tasks (F-018)

| Old path | Action | New path |
|---|---|---|
| `ops/audit/archive/history/WhatsApp Ptt 2026-02-06 at 13.03.07.ogg` | git mv | `archive/legacy/media/said-voice-note-2026-02-06.ogg` |
| `ops/audit/archive/history/WhatsApp Ptt 2026-02-06 at 13.03.07.md` | git mv | `archive/legacy/media/said-voice-note-2026-02-06.md` |
| `ops/audit/archive/history/Agentic Mastery.md` | rename | `ops/audit/archive/history/agentic-mastery.md` |

---

## Staged changes summary

- Deleted: 8 files (1 exact duplicate, 6 reviews migrated to ~/omar)
- Renamed/moved: 17 files across hotelrunner, booking, data/archive, scripts, archive/legacy
- New directories created: scripts/archive/, archive/legacy/media/
- External copy: 6 files to ~/omar/core/context/domains/ai/reviews/
- Unstaged pre-existing modification not touched: data/admin/client/contact.md

---

## Verification

- baseline.md confirmed exact duplicate via diff before git rm
- archive/reviews/ confirmed fully copied to ~/omar before git rm
- WhatsApp companion .md found and co-located with .ogg
- All renamed files use kebab-case (no UPPERCASE, no underscores remaining)
- No commit made — all changes staged only, ready for make changelog + commit


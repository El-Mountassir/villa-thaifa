# Task: Connect to Expedia Partner Central

- [x] **Room Data Standardization Strategy** <!-- id: 4 -->
  - [x] Create `ROOM_MASTER_TEMPLATE.md` (Strict Expedia Fields) <!-- id: 5 -->
  - [x] Gap Analysis (Audit R1 vs Requirements) <!-- id: 6 -->
  - [x] Create `ROOM_DATA_SHEET_FOR_SAID.md` (Questionnaire) <!-- id: 7 -->
  - [x] Initialize "Golden Records" (R01-R12) as individual files <!-- id: 8 -->
  - [x] **MIGRATE TO DATABASE** (SQLite) <!-- id: 9 -->
    - [x] Init DB Schema (`src/db/schema.sql`)
    - [x] ETL Script (`scripts/migrate_rooms_to_db.ts`)
    - [x] Verify Data & Archive MD files
- [x] **Data Verification App** (Next.js) <!-- id: 10 -->
  - [x] Create Dashboard (`/admin/rooms`) <!-- id: 11 -->
  - [x] Create Editor (`/admin/rooms/[id]`) <!-- id: 12 -->
  - [x] **ACTION**: Said validates Views/Outdoors for R01-R11 (Confirmed by User) <!-- id: 13 -->

## Next Session: Expedia Integration <!-- id: 14 -->

- [ ] **Expedia Onboarding (Browser)** <!-- id: 15 -->
  - [x] Create Developer Onboarding Guide (Discarded - Locked API)
  - [ ] Review `implementation_plan_expedia.md` (Browser Pivot) <!-- id: 16 -->
- [ ] **Execution (The 1-by-1 Flow)** <!-- id: 18 -->
  - [ ] Script: `scripts/auto_onboard_browser.ts` <!-- id: 19 -->
  - [ ] Room 12 Onboarding Dry Run (Screenshot check) <!-- id: 20 -->
  - [ ] Bulk Onboarding (R01-R11) <!-- id: 21 -->
  - [x] Document findings/status in `walkthrough.md` <!-- id: 7 -->

- [x] Expedia Onboarding Advice: Deposits <!-- id: 8 -->
  - [x] Research existing deposit policies <!-- id: 9 -->
  - [x] Prepare explanation for Said Thaifa (NL/FR) <!-- id: 10 -->
  - [x] Provide recommendation for Expedia settings <!-- id: 11 -->

- [x] Expedia Onboarding Advice: Cancellation Policy <!-- id: 12 -->
  - [x] Research existing cancellation policies <!-- id: 13 -->
  - [x] Prepare explanation for Said Thaifa (NL/FR) <!-- id: 14 -->
  - [x] Provide recommendation for Expedia settings <!-- id: 15 -->

- [x] Expedia Onboarding Advice: Taxes and Fees <!-- id: 16 -->
  - [x] Research tax handling in existing systems <!-- id: 17 -->
  - [x] Explain Taxe de Séjour vs TPT (NL/FR) <!-- id: 18 -->
  - [x] Prepare explanation for Said Thaifa (NL/FR) <!-- id: 19 -->
  - [x] Provide recommendation for Expedia settings <!-- id: 20 -->

- [x] Tax Discrepancy Investigation <!-- id: 21 -->
  - [x] Verify content of `~/Downloads/IMG_20260126_0001.pdf` <!-- id: 22 -->
  - [x] Research official "Taxe de Séjour" rates for Marrakech 2025/2026 <!-- id: 23 -->
    - [x] Analyze 3 MAD vs 30 MAD discrepancy <!-- id: 24 -->
    - [x] Formulate correction strategy for Expedia <!-- id: 25 -->
    - [x] Draft correction message for Expedia Tax Team <!-- id: 26 -->

- [x] Expedia Amenities Configuration <!-- id: 27 -->
  - [x] Review `VILLA_THAIFA.json` and `PROFILE.md` for amenity details <!-- id: 28 -->
  - [x] Navigate to Expedia Amenities page <!-- id: 29 -->
  - [x] Capture available amenity options <!-- id: 30 -->
  - [x] Create recommendation file `docs/operations/expedia/amenities_recommendation.md` <!-- id: 31 -->

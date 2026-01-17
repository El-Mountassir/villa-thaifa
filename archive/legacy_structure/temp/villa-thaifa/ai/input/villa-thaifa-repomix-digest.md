# REPOMIX DIGEST — Villa Thaifa Repository Analysis

**Analyzed:** 2026-01-09
**Repomix Content:** ~180k tokens (Full repository history & state)
**Digest Status:** Ready for integration into Briefs v0.3.0

---

## EXECUTIVE SUMMARY

The repository is in a transition phase between a monolithic structure and an "Everything-as-Code" (EaC) agentic architecture. The `data/` directory is established as the Single Source of Truth (SSOT). **Critical operational data (Rooms, Pricing, Reservations) exists and is accessible**, primarily in `data/specs/`.

However, there is a divergence in room configuration strategies (Grouped by Type vs. Individual Rooms) which is documented but requires final unification. HotelRunner is connected but suffering from a specific synchronization issue regarding internal reservations. The "App" vision is currently defined as a set of options rather than a concrete technical specification.

---

## CRITICAL FINDINGS (For Brief Updates)

### Room Configuration

**Source Files:** `data/specs/configs/hotel/facilities/rooms/*.md` and `data/specs/configs/hotel/platform-mapping.md`

- **Total Count:** 12 Physical Rooms.
- **Numbering Strategy:** 1 to 12.
- **Current Mapping (HotelRunner):** 8 Room Types mapped to 12 physical rooms.
  - **Room 1, 3, 8:** Deluxe Triple Room
  - **Room 2:** Deluxe Double Room
  - **Room 4, 5:** Double Room Superior (Pooled in Booking.com)
  - **Room 6:** Executive Suite
  - **Room 7:** Deluxe King Suite
  - **Room 9, 11:** Family Suite
  - **Room 10:** Suite
  - **Room 12:** Presidential Suite
- **Booking.com Specifics:** Room 4 & 5 are pooled under ID `544684730`. Same issues for 1 & 3 & 8. And same for 9 & 11.
- **Pricing:** Baseline pricing exists in `data/specs/configs/hotel/rooms/*.md` (e.g., Room 4 @ 160€, Room 7 @ 440€).

### HotelRunner Integration

**Source Files:** `data/specs/platform/hotelrunner/*` and `docs/reports/2025-12-29-sync-investigation.md`

- **Status:** **Active but Partially Broken (Sync Issue).**
- **Critical Issue:** Internal reservations created on HotelRunner (Source: "Online") do **NOT** push availability updates to Booking.com.
- **Root Cause Identified:** "Allocation Type" setting in HotelRunner is set to "No changes".
- **Connection Type:** Two-Way XML confirmed.
- **API Reference:** Found in `data/specs/platform/hotelrunner/api-reference.md`.
- **Channel Mapping:** Documented in `data/specs/platform/hotelrunner/channel-mapping.md`.

### Property Details

**Source Files:** `data/admin/client/PROFILE.md` and `data/specs/platform/booking/booking-com-data.md`

- **Type:** Maison d'hôtes de charme / B&B (4★).
- **Location:** Route de Fès, Km 12, Palmeraie / Ouled Jelal, Marrakech.
- **Amenities:** Infinity pool, Spa/Hammam, Restaurant (Moroccan), Garden, Rooftop, WiFi (8.8/10), AC.
- **House Rules:** Check-in 14:00-00:00, Check-out 11:00, No pets, No smoking (designated areas only).
- **Breakfast:** Score 10/10 (included in rate plans).
- **Photos:** Directory structure `data/specs/configs/hotel/images/` exists in file tree, but binary content obviously excluded from text repomix. File paths indicate photos exist for Rooms 1-11, Spa, and Hall. **Room 12 photos noted as missing/needing contact with Ikram.**

### "Transform to App" Vision

**Source Files:** `docs/project/BRIEF.md`

- **Status:** **Not formally specified.** Presented as 3 options in `BRIEF.md`:
  - **Option A:** Web App (Next.js Dashboard + Python Backend).
  - **Option B:** Automation-First (Scripts + Cron).
  - **Option C (Recommended):** Hybrid (Scripts now -> Streamlit/Gradio/SQLite/FastAPI/Python 3.12+(UV)-> Full App later).
- **Current State:** `src/` directory contains empty placeholders (`apps/dashboard`, `apps/api`). No actual application code exists yet.

### Agent Systems (`ai/` directory)

**Source Files:** `ai/inventory/sub-agent_registry.md`

- **Existing Agents:**
  - `meta-agent`: Agent configuration generator. Creates new sub-agents from descriptions. Use PROACTIVELY when user requests a new agent or when a specialized agent is needed for a recurring task.
  - `browser-agent`: Chrome automation Browser automation specialist. Handles Chrome automation for scraping, form filling, and platform interactions. Use PROACTIVELY when browser operations are any web interface (HotelRunner/Booking/ Expedia/etc).
  - `deep-research-agent`: Critical research agent for HIGH impact topics (config, security, architecture). ALWAYS verifies with local commands.
  - `reservation-manager`: Lifecycle of reservations.
  - `pricing-analyst`: Revenue optimization.
  - `calendar-agent`: Availability analysis.
  - `platform-validator`: Gatekeeper before platform ops.
  - `incident-reporter`: Incident documentation specialist. Creates structured incident reports when errors, failures, or unexpected behavior occurs. Use PROACTIVELY when any error or failure needs to be logged.
- **Architecture:** Hierarchical `CLAUDE.md` context inheritance.
- **Readiness:** Agents are defined in markdown (`.claude/agents/`) but rely on CLI tooling to execute.

### Data Structure (`data/` directory)

**Source Files:** `data/specs/state/README.md`

- **SSOT Pattern:** Implemented.
- **Structure:**
  - `current/`: Live state (reservations).
  - `planned/`: Proposals (pricing).
  - `configs/`: Static data (rooms, facilities).
- **Quality:** High. explicit separation of "What is" vs "What will be".

### Documentation State (`docs/`)

**Source Files:** `docs/lessons-learned.md`, `docs/workflows/`

- **Workflows:** Reservation, Pricing, Guest Communication documented.
- **Lessons Learned:** **CRITICAL**. Contains "Scout → Report → Action" protocol and "Booking.com Stacking Myth" correction.
- **Gaps:** Specific "Monteurs" definition and activation process is listed as [RESEARCH NEEDED] in previous analysis.

---

## REPO STRUCTURE OVERVIEW

```text
villa-thaifa/
├── .claude/
│   ├── agents/         # Operational agent prompts (browser, pricing, etc.)
│   └── rules/          # Behavioral constraints
├── ai/
│   └── inventory/      # Registry of available agents
├── archive/            # Historical artifacts (2025/Q4) - Heavy volume
├── data/               # SINGLE SOURCE OF TRUTH
│   ├── admin/          # Client profile & contacts
│   └── specs/
│       ├── configs/    # Hotel static specs (Rooms 1-12)
│       ├── platform/   # HotelRunner/Booking rules & mapping
│       ├── promotions/ # Baseline & Current promo states
│       └── state/      # Dynamic state (Current Reservations)
├── docs/
│   ├── incidents/      # Log of technical failures (Sync issue logged here)
│   ├── reports/        # Investigation reports
│   └── workflows/      # Operational procedures
├── missions/           # Task management (Active/Queue)
└── src/                # Empty placeholders for future App
```

---

## WHAT'S WORKING vs "BORDEL"

**Working:**

- **State Management:** `data/specs/state` is clean and logical.
- **Room Definition:** `data/specs/configs/hotel/facilities/rooms/` provides granular detail per room.
- **Incident Tracking:** The sync issue is perfectly documented in `docs/reports/2025-12-29-sync-investigation.md`.

**"Bordel" (Disorganized):**

- **Legacy Archives:** `archive/` contains significant duplication of briefs and reports from late 2025. Some are yet to be recycled because not previously processes/ archived way too fast!
- **Room Configuration Duplication:** `data/specs/configs/hotel/rooms.md` is marked DEPRECATED but still contains data that might not be fully mirrored in individual files.

**Missing:**

- **App Specification:** No technical design document for the "App".
- **Room 12 Photos:** Explicitly noted as missing.
- **Market Research:** "Monteurs" definition and specific competitor benchmarking are placeholders.

---

## RECOMMENDATIONS FOR LUX

### Immediate Updates to Briefs (v0.3.0)

**Client Brief Updates:**

- **Update "Tech Stack":** Confirm HotelRunner is Active (Two-Way XML) but requires configuration fix ("Allocation Type").
- **Update "Property":** Confirm 12 Rooms, specific amenities, and 4★ positioning.

**Project Brief Updates:**

- **Fill [REPO] Placeholders:**
  - Room Config: 12 Rooms (1-12), mapped to 8 Types.
  - HotelRunner: Connected to Booking.com, Sync Issue (Internal reservations don't block calendar).
  - Photos: Folder structure exists, Room 12 missing.
- **Fill [APP] Placeholder:** Define as "Option C: Hybrid (Automation Scripts first)".

### Phase 1 Execution Impact

**Blockers Resolved:**

- **Room Mapping:** We know exactly which physical rooms map to which OTA types.
- **Promotion Strategy:** 10-15% discount range validated; 40% promos deactivated.

**New Blockers Identified:**

- **Sync Risk (P0):** Internal reservations (made by Omar/Said) DO NOT block Booking.com dates. **Action:** Must manually block dates on Booking.com or fix "Allocation Type" setting in HotelRunner immediately.

**Workarounds Available:**

- **Manual Block:** Use Booking.com Extranet to close dates for manual reservations until HotelRunner config is fixed.

---

## QUESTIONS FOR OMAR

1. **Sync Fix:**
   - **\*Question:** Have you or Ikram changed the "Allocation Type" in HotelRunner from "No changes" yet? This is a P0 critical risk for double bookings.
   - **Omar's Answer:** HotelRunner Support Team / Ikram didn't properly answer me about this, because they talked directly to Said Thaifa saying that the sync problem was fixed. So we'll have to mark this as done
2. **Room 12 Photos:**
   - **\*Question:** Did we get the photos for the Presidential Suite from Ikram?
   - **Omar's Answer:** Yes, we'll have to create a new message for them HotelRunner Support Team / Ikram to ask for that. But, we can already run the browser agent to get the photos for the Presidential Suite from booking because many are already there.
3. **App Decision:**
   - **Question:** Do you confirm "Option C (Hybrid)" for the App vision, or should we strictly stick to existing CLI agents for now?
   - **Omar's Answer:** That seems decent but I'm not sure that we have to do it that way... nowadays, our tools / agentic system can build entier apps end-to-end.. so we don't need to be very caution about **The Golden Path** - _"Always start from Gold - best case, reality-bounded outcome"_ We need to target the Golden still needs some work/ details and all documentation for project inception so that Omar get all the tasks to be added to Vibe-Kanban as high level tickets or something like that (we'll have to investigate more about the best way for us to exploit Vibe-Kanban (Claude Code CLI + Gemini CLI if needed)) , what matters for me is that we get a great UX/UI + backend + DB (for all the facilities, etc)

---

## APPENDICES

### A. File Inventory (Key Files Only)

1. `data/specs/state/current/reservations.md`: **SSOT** for current bookings.
2. `data/specs/configs/hotel/facilities/rooms/*.md`: **SSOT** for room details (12 files).
3. `docs/reports/2025-12-29-sync-investigation.md`: Detailed analysis of the HotelRunner sync failure.
4. `data/admin/client/PROFILE.md`: Comprehensive client profile & business context.
5. `data/specs/platform/rules.md`: Operational rules (90% confidence rule).
6. `docs/lessons-learned.md`: History of errors (communication, technical).

### B. Code Snippets (Configuration)

**HotelRunner Sync Config (from Investigation Report):**

```text
Setting: Allocation Type
Current Value: "No changes"
Issue: Likely prevents availability push from HR to Booking.com
```

### C. Critical Data (Room Types)

```text
Room 4, 5 -> Double Room Superior (Pooled ID: 544684730)
Room 1, 3, 8 -> Deluxe Triple Room
Room 7 -> Deluxe King Suite (Premium Pricing: 440 EUR)
Room 12 -> Presidential Suite (Premium Pricing: 600 EUR)
```

---

**END OF DIGEST**

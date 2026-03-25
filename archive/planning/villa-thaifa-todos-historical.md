# Tasks — Villa Thaifa

> Last updated: 2025-12-20 21:45

---

## Prioritization System

**Hybrid Approach**: MoSCoW (importance) + Eisenhower (urgency)

### Priority Matrix

|                        | **URGENT**                | **NOT URGENT**              |
| ---------------------- | ------------------------- | --------------------------- |
| **MUST** (Critical)    | 🔴 P0 — Do NOW            | 🟠 P1 — Schedule this week  |
| **SHOULD** (Important) | 🟡 P2 — Do today/tomorrow | 🟢 P3 — Schedule this month |
| **COULD** (Desirable)  | 🔵 P4 — If time allows    | ⚪ P5 — Backlog             |
| **WON'T** (Excluded)   | ❌ Out of scope           | ❌ Out of scope             |

### Legend

| Priority | Meaning                   | Deadline       |
| -------- | ------------------------- | -------------- |
| 🔴 P0    | Critical + Urgent         | Immediate      |
| 🟠 P1    | Critical + Not urgent     | This week      |
| 🟡 P2    | Important + Urgent        | Today/Tomorrow |
| 🟢 P3    | Important + Not urgent    | This month     |
| 🔵 P4    | Nice-to-have + Urgent     | If time allows |
| ⚪ P5    | Nice-to-have + Not urgent | Backlog        |

---

## Work in Progress

### 🔴 P0 — Critical + Urgent

- [ ] **⚠️ META-WORKFLOW : Configure Claude instances for files, not chat**
  - **Problem**: Questions, issues, important info remain in ephemeral chat
  - **Impact**: Omar cannot cleanly manage/track
  - **Solution**: All valuable info → file (not chat)
  - **Target files**:
    - Questions → `.claude/output/.../questions-pending.md`
    - Issues → `.claude/output/.../blocages.md`
    - Pending decisions → in reports with answer space
  - **Action**: Update `.claude/rules` with this rule
  - See: `.claude/output/2025/Q4/reports/pricing-strategy-session/rapport-session-20-dec-2025.md`

- [ ] **Configure HotelRunner pricing** — Pricing session in progress
  - Interface: Calendar → Simple Updates
  - Computed prices: see session report
  - **Waiting on**: Omar's validation of premium prices (7, 12)

- [x] ~~**Access Booking.com Extranet** — Promotions audit~~ ✅ DONE
  - URL: `admin.booking.com`
  - **Executed Dec 20, 2025**
  - 6 promotions deactivated (P0)
  - 2 promotions reduced (P1)
  - See: `.claude/output/2025/Q4/reports/pricing-strategy-session/execution-log-booking.md`

- [x] ~~**⚠️ URGENT : Assign rooms Arne Cordes**~~ ✅ DONE
  - Rooms 4 and 5 assigned (Dec 20-25, 5 nights)
  - Total: €1,235

- [ ] **Finalize reservation room 11** — Awaiting reply from M. Thaifa
  - Dates: Dec 19→21, 2025 (2 nights)
  - Room: Family Suite (n°11)
  - Missing info: guest name, rate, adults count
  - Blocker: client reply

### 🟠 P1 — Critical + Not urgent

- [ ] **Assign rooms Nicolas Lamblain** — Arrival Dec 26
  - 2 Double Room Superior reservations
  - Confirmations: 6538291598 / 6538291598-1
  - Deadline: Dec 25

- [ ] **Assign rooms Jean Damien Aubril** — Arrival Dec 27
  - 2 Deluxe Triple Room reservations
  - Confirmations: 5352537667 / 5352537667-1
  - Suggested rooms: 1, 3, or 8
  - Deadline: Dec 26

- [ ] **Assign room Quentin Warembourg** — Arrival Dec 29
  - 1 Suite reservation (Booking.com)
  - Confirmation: 5446634150
  - Suggested room: 10 (Suite)
  - Dates: Dec 29 → **Jan 5** (7 nights)
  - Assignment deadline: Dec 28
  - **✅ VERIFIED 2025-12-20**:
    - Reservation confirmed since Nov 8, 2025
    - Total: €973 | Booking commission: €262.71
    - HotelRunner: Payment Total €0 | Mode: Hotel Collect
    - Booking.com: Status **OK** | Payment via Booking.com / Bank transfer
    - Cancellation policy: Flexible – 5 days (**limit: Dec 24**)
    - 2 adults, 0 children | Bed & breakfast
  - ⚠️ **See P2 task**: Decision required before Dec 24

### 🟡 P2 — Important + Urgent

- [x] ~~**⚠️ DEADLINE DEC 24: Decision Quentin Warembourg**~~ ✅ **RESOLVED**
  - **Initial context**: Mr. Said worried due to "no news" from guest
  - **Investigation 2025-12-20**:
    - HotelRunner: Status "Reservation", Hotel Collect, €0 received
    - Booking.com: Status "OK", Paid via Booking.com (payout scheduled Feb 1, 2026)
  - **✅ POSITIVE SIGNALS FOUND**:
    - Guest asked for airport shuttle info → **definitely plans to arrive**
    - Arrival time specified: 9-10 PM
    - Reservation made 6 weeks ago (Nov 8, 2025)
    - Payment guaranteed by Booking.com
  - **Decision**: Legitimate reservation, contact guest for shuttle

- [x] ~~**📩 Reply to Quentin Warembourg: Airport Shuttle**~~ ✅ **SENT**
  - **Guest request**: Interested in airport shuttle service
  - **Message sent**: 2025-12-20 ~18h via Booking.com
  - **Note**: Shortened version (missing rates). 200 MAD rate to be communicated if guest confirms
  - **Draft**: `.claude/output/2025/Q4/drafts/message-quentin-navette.md`
  - **Waiting on**: Guest reply (flight number, landing time)

### 🟢 P3 — Important + Not urgent

- [ ] **Prepare structured brief for future agents** — HotelRunner workflow documentation
- [ ] **Investigate Jisr l'Mokawala portal** — Go Siyaha / Maroc PME
- [x] **Meeting Monday Dec 22 10AM** — First official meeting with Mr. Thaifa - Already done... but STRONGLY badly started based on Omar's criteria... Discovery, documentation, capturing, contracting, etc. clearly not done (or poorly executed).

### 🔵 P4 — Nice-to-have

- [ ] **Explore HotelRunner API** — For future automation
- [ ] **Create mission report template** — Reusable for other clients

### ⚪ P5 — Backlog

- [ ] **Develop AI agent for reservation management** — Long-term project
- [ ] **Reduce Booking.com dependency** — Direct booking channels strategy

---

## Completed Tasks

### 2025-12-20

- [x] **V2 Audit Booking.com Promotions** ✅
  - 3 undocumented promotions identified
  - Early Booker Deal 10% (NEW)
  - Mobiles Rate 10% (€15,614 revenue)
  - Abroad (geo-targeted) 10%
  - All compliant with strategy (10-15% optimal)
  - 4 files updated
- [x] **Execute Booking.com promotions plan** ✅
  - 6 P0 promotions deactivated (40%, 38%, 43%, 42%, 10% Europe, 10% Morocco)
  - 2 P1 promotions reduced (33%→15%, 30%→10%)
  - Log file: `execution-log-booking.md`
- [x] Assign rooms Arne Cordes rooms 4 and 5 ✅
- [x] Locate price modification interface (Calendar → Simple Updates) ✅
- [x] Compute Booking.com prices (formula: margin/0.75) ✅
- [x] Create pricing session report ✅
- [x] Document mapping rooms ↔ types ✅
- [x] Investigate Quentin Warembourg reservation (Suite 10, Dec 29 - Jan 5) ✅
  - Result: Legitimate reservation, payment by Booking.com
  - Positive signals: shuttle request, arrival time stated (9-10 PM)
- [x] Create shuttle message draft for Quentin Warembourg ✅
  - File: `.claude/output/2025/Q4/drafts/message-quentin-navette.md`
- [x] Document transport service ✅
  - File: `docs/services-transport.md`
- [x] Send shuttle message to Quentin Warembourg ✅
  - Via Booking.com (res 5446634150)
  - Shortened version sent (session interrupted)
  - Waiting on guest reply

### 2025-12-19

- [x] Connect to HotelRunner ✅
- [x] Fix credentials in doc ✅
- [x] Check room 11 availability ✅
- [x] Create mission report ✅
- [x] Create lessons-learned.md file ✅
- [x] Document communication error (pattern Scout→Report→Action) ✅
- [x] Document tone/register error (formal addressing + WhatsApp fluidity) ✅
- [x] Restructure folders (`communication/` → root) ✅
- [x] Create `CLAUDE.md` (fixed: root, not `.claude/`) ✅
- [x] Add TODOs.md workflow to CLAUDE.md ✅
- [x] Document CLAUDE.md placement error (global patterns.md) ✅
- [x] Revamp folder structure (plan + research sources) ✅
- [x] Create `admin/`, `assets/`, `projects/` ✅
- [x] Migrate files to new structure ✅
- [x] Create global client template (`~/Documents/templates/client/`) ✅
- [x] Update CLAUDE.md with new paths ✅
- [x] Create gold standard report template (`docs/templates/`) ✅
- [x] Explore HotelRunner reservations ✅
- [x] Identify 10 unassigned reservations ✅
- [x] Create exploration report (`governance/inbox/ai/reports/`) ✅

---

## Current Blockers

| Blocker                  | Impact                     | Dependency              | Action            |
| ------------------------ | -------------------------- | ----------------------- | ----------------- |
| Reply from M. Thaifa     | Cannot finalize res rm 11  | Client                  | Wait              |
| ~~Booking.com Access~~   | ~~Cannot audit promos~~    | ~~Omar authorizes~~     | ✅ RESOLVED 20/12 |
| Premium price validation | HotelRunner config blocked | Omar responds in report | Reply in file     |

---

## Notes

### Client Context

- **Client**: Said Thaifa (70+ years old)
- **Property**: Villa Thaifa (guest house, Marrakech)
- **Relationship**: Potential new client (high-ticket)
- **Communication**: Formal, respectful, mandatory formal "vous"

### Next Deadline

- **Monday Dec 22, 2025, 10AM** — Meeting with Mr. Thaifa // Already done...

---

## Sources — Prioritization System

- [Highberg - Comparison of prioritization methods](https://highberg.com/insights/a-comparison-of-prioritization-methods)
- [Medium - MoSCoW vs Eisenhower](https://medium.com/@nowacki.lukasz/moscow-method-vs-eisenhower-matrix-prioritization-of-tasks-in-the-project-372f8553c12a)
- [Product School - 9 Prioritization Frameworks](https://productschool.com/blog/product-fundamentals/ultimate-guide-product-prioritization)

> **SUPERSEDED** — Task tracking moved to [Linear](https://linear.app/el-mountassir) (VT team). This file is retained as historical reference only.
> Original date: 2025-12-20. Superseded by Linear migration Feb 2026.

# Tasks — Villa Thaifa

> Last updated : 2025-12-20 21:45

---

## Prioritization System

**Hybrid approach** : MoSCoW (importance) + Eisenhower (urgency)

### Priority Matrix

|                        | **URGENT**                | **NOT URGENT**          |
| ---------------------- | ------------------------- | ----------------------- |
| **MUST** (Critical)    | 🔴 P0 — Do NOW            | 🟠 P1 — Plan this week  |
| **SHOULD** (Important) | 🟡 P2 — Do today/tomorrow | 🟢 P3 — Plan this month |
| **COULD** (Desirable)  | 🔵 P4 — If time permits   | ⚪ P5 — Backlog         |
| **WON'T** (Excluded)   | ❌ Out of scope           | ❌ Out of scope         |

### Legend

| Priority | Meaning                   | Deadline        |
| -------- | ------------------------- | --------------- |
| 🔴 P0    | Critical + Urgent         | Immediate       |
| 🟠 P1    | Critical + Not urgent     | This week       |
| 🟡 P2    | Important + Urgent        | Today/tomorrow  |
| 🟢 P3    | Important + Not urgent    | This month      |
| 🔵 P4    | Nice-to-have + Urgent     | If time permits |
| ⚪ P5    | Nice-to-have + Not urgent | Backlog         |

---

## Tasks in progress

### 🔴 P0 — Critical + Urgent

- [ ] **⚠️ META-WORKFLOW: Configure Claude instances for files, not chat**
  - **Problem**: Questions, issues, important info stay in the ephemeral chat
  - **Impact**: Omar cannot properly manage/track
  - **Solution**: All valuable info → file (not chat)
  - **Target files**:
    - Questions → `.claude/output/.../questions-pending.md`
    - Issues → `.claude/output/.../blocages.md`
    - Pending decisions → in reports with response space
  - **Action**: Update `CLAUDE.md` with this rule
  - See: `.claude/output/2025/Q4/reports/pricing-strategy-session/rapport-session-20-dec-2025.md`

- [ ] **Configure HotelRunner pricing** — Pricing session in progress
  - Interface: Calendar → Simple Updates
  - Calculated prices: see session report
  - **Pending**: Omar validation for premium prices (7, 12)

- [x] ~~**Access Booking.com Extranet** — Promotions audit~~ ✅ DONE
  - URL: `admin.booking.com`
  - **Executed on Dec 20, 2025**
  - 6 promotions deactivated (P0)
  - 2 promotions reduced (P1)
  - See: `.claude/output/2025/Q4/reports/pricing-strategy-session/execution-log-booking.md`

- [x] ~~**⚠️ URGENT: Assign rooms for Arne Cordes**~~ ✅ DONE
  - Rooms 4 and 5 assigned (Dec 20-25, 5 nights)
  - Total: €1,235

- [ ] **Finalize Room 11 reservation** — Pending reply from Mr. Thaifa
  - Dates: Dec 19→21, 2025 (2 nights)
  - Room: Family Suite (n°11)
  - Missing info: guest name, rate, number of adults
  - Blocker: client response

### 🟠 P1 — Critical + Not urgent

- [ ] **Assign rooms for Nicolas Lamblain** — Arrival Dec 26
  - 2 Double Room Superior reservations
  - Confirmations: 6538291598 / 6538291598-1
  - Deadline: Dec 25

- [ ] **Assign rooms for Jean Damien Aubril** — Arrival Dec 27
  - 2 Deluxe Triple Room reservations
  - Confirmations: 5352537667 / 5352537667-1
  - Suggested rooms: 1, 3 or 8
  - Deadline: Dec 26

- [ ] **Assign room for Quentin Warembourg** — Arrival Dec 29
  - 1 Suite reservation (Booking.com)
  - Confirmation: 5446634150
  - Suggested room: 10 (Suite)
  - Dates: Dec 29 → **Jan 5** (7 nights)
  - Assignment deadline: Dec 28
  - **✅ VERIFIED 2025-12-20**:
    - Reservation confirmed since Nov 8, 2025
    - Total: €973 | Booking commission: €262.71
    - HotelRunner: Payment Total €0 | Mode: Hotel Collect
    - Booking.com: Status **OK** | Payment by Booking.com / Bank transfer
    - Cancellation policy: Flexible – 5 days (**limit: Dec 24**)
    - 2 adults, 0 children | Bed & breakfast
  - ⚠️ **See P2 task**: Decision required before Dec 24

### 🟡 P2 — Important + Urgent

- [x] ~~**⚠️ DEADLINE DEC 24: Decision for Quentin Warembourg**~~ ✅ **RESOLVED**
  - **Initial context**: Mr. Said worried because "no news" from the client
  - **Investigation 2025-12-20**:
    - HotelRunner: Status "Reservation", Hotel Collect, €0 received
    - Booking.com: Status "OK", Payments by Booking.com (transfer scheduled Feb 1, 2026)
  - **✅ POSITIVE SIGNALS FOUND**:
    - Client requested airport shuttle info → **definitely plans to come**
    - Specified arrival time: 9PM-10PM
    - Reservation since 6 weeks ago (Nov 8, 2025)
    - Payment guaranteed by Booking.com
  - **Decision**: Legitimate reservation, contact client for shuttle

- [x] ~~**📩 Reply to Quentin Warembourg: Airport shuttle**~~ ✅ **SENT**
  - **Client request**: Interested in airport shuttle service
  - **Message sent**: 2025-12-20 ~18h via Booking.com
  - **Note**: Shortened version (missing rates). Rate 200 MAD to be communicated if client confirms
  - **Draft**: `.claude/output/2025/Q4/drafts/message-quentin-navette.md`
  - **Pending**: Client reply (flight number, landing time)

### 🟢 P3 — Important + Not urgent

- [ ] **Prepare structured brief for future agents** — HotelRunner workflow documentation
- [ ] **Investigate Jisr l'Mokawala portal** — Go Siyaha / Maroc PME
- [ ] **Meeting Monday Dec 22 10AM** — First official meeting with Mr. Thaifa

### 🔵 P4 — Nice-to-have

- [ ] **Explore HotelRunner API** — For future automation
- [ ] **Create mission report template** — Reusable for other clients

### ⚪ P5 — Backlog

- [ ] **Develop AI agent for reservation management** — Long-term project
- [ ] **Reduce Booking.com dependency** — Direct channels strategy

---

## Completed tasks

### 2025-12-20

- [x] **V2 Audit Booking.com Promotions** ✅
  - 3 undocumented promotions identified
  - Early Booker Deal 10% (NEW)
  - Mobile Rate 10% (€15,614 revenues)
  - Abroad (geo-targeted) 10%
  - All compliant with strategy (10-15% optimal)
  - 4 files updated
- [x] **Execute Booking.com promotions plan** ✅
  - 6 P0 promotions deactivated (40%, 38%, 43%, 42%, 10% Europe, 10% Morocco)
  - 2 P1 promotions reduced (33%→15%, 30%→10%)
  - Log file: `execution-log-booking.md`
- [x] Assign Arne Cordes rooms 4 and 5 ✅
- [x] Locate price modification interface (Calendar → Simple Updates) ✅
- [x] Calculate Booking.com prices (formula: margin/0.75) ✅
- [x] Create pricing session report ✅
- [x] Document room ↔ types mapping ✅
- [x] Investigate Quentin Warembourg reservation (Suite 10, Dec 29 - Jan 5) ✅
  - Result: Legitimate reservation, Payments by Booking.com
  - Positive signals: shuttle request, specific arrival time (9PM-10PM)
- [x] Create shuttle message draft for Quentin Warembourg ✅
  - File: `.claude/output/2025/Q4/drafts/message-quentin-navette.md`
- [x] Document transport service ✅
  - File: `docs/services-transport.md`
- [x] Send shuttle message to Quentin Warembourg ✅
  - Via Booking.com (reservation 5446634150)
  - Shortened version sent (interrupted session)
  - Pending client reply

### 2025-12-19

- [x] Connect to HotelRunner ✅
- [x] Fix credentials in docs ✅
- [x] Check availability for room 11 ✅
- [x] Create mission report ✅
- [x] Create lessons-learned.md file ✅
- [x] Document communication error (Scout→Report→Action pattern) ✅
- [x] Document tone/register error (formal "vous" + WhatsApp fluidity) ✅
- [x] Restructure folders (`communication/` → root) ✅
- [x] Create `CLAUDE.md` (fixed: root, not `.claude/`) ✅
- [x] Add TODOs.md workflow in CLAUDE.md ✅
- [x] Document CLAUDE.md location error (global patterns.md) ✅
- [x] Folder structure overhaul (plan + research sources) ✅
- [x] Create `admin/`, `assets/`, `projects/` ✅
- [x] Migrate files to new structure ✅
- [x] Create global client template (`~/Documents/templates/client/`) ✅
- [x] Update CLAUDE.md with new paths ✅
- [x] Create gold standard report template (`docs/templates/`) ✅
- [x] Explore HotelRunner reservations ✅
- [x] Identify 10 unassigned reservations ✅
- [x] Create exploration report (`governance/inbox/ai/reports/`) ✅

---

## Current blockers

| Blocker                  | Impact                        | Dependency             | Action            |
| ------------------------ | ----------------------------- | ---------------------- | ----------------- |
| Mr. Thaifa reply         | Cannot finalize rm.11 booking | Client                 | Wait              |
| ~~Booking.com Access~~   | ~~Cannot audit promos~~       | ~~Omar authorizes~~    | ✅ RESOLVED 12/20 |
| Premium price validation | HotelRunner config blocked    | Omar replies in report | Reply in file     |

---

## Notes

### Client Context

- **Client**: Said Thaifa (+60 years old)
- **Establishment**: Villa Thaifa (guesthouse, Marrakech)
- **Relationship**: New prospective client (high-ticket)
- **Communication**: Formal, respectful, "vous" mandatory

### Next Deadline

- **Monday December 22, 2025, 10AM** — Meeting with Mr. Thaifa

---

## Sources — Prioritization System

- [Highberg - Comparison of prioritization methods](https://highberg.com/insights/a-comparison-of-prioritization-methods)
- [Medium - MoSCoW vs Eisenhower](https://medium.com/@nowacki.lukasz/moscow-method-vs-eisenhower-matrix-prioritization-of-tasks-in-the-project-372f8553c12a)
- [Product School - 9 Prioritization Frameworks](https://productschool.com/blog/product-fundamentals/ultimate-guide-product-prioritization)

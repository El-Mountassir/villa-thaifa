# Brownfield Requirements -- Villa Thaifa

> **Extracted from**: `context/meta/planning/PROJECT.md` on 2026-02-24
> **Context**: These requirements document the existing brownfield app (Next.js property management platform) that preceded the current operations-focused repo. They serve as the requirements baseline for future app development.

---

## Validated (Existing Features -- Confirmed Working)

| ID       | Requirement                                                       | Status    | Notes                      |
| -------- | ----------------------------------------------------------------- | --------- | -------------------------- |
| PUB-01   | Public hotel website with room showcase (12 rooms)                | Validated | Existing in brownfield app |
| PUB-02   | Room detail pages with static generation                          | Validated | Existing in brownfield app |
| PUB-03   | Facilities showcase (spa, pool, restaurant, bar)                  | Validated | Existing in brownfield app |
| ADMIN-01 | Admin dashboard with room management grid                         | Validated | Existing in brownfield app |
| ADMIN-02 | Room detail editor (metadata, amenities, beds)                    | Validated | Existing in brownfield app |
| ADMIN-03 | Verification workflow (DRAFT -> VERIFIED status)                  | Validated | Existing in brownfield app |
| DATA-01  | SQLite database with room, bed, amenity tables                    | Validated | Existing in brownfield app |
| DATA-02  | Zod schema validation across all data                             | Validated | Existing in brownfield app |
| INT-01   | HotelRunner reservation extraction (96 records via browser auto.) | Validated | Existing in brownfield app |

## Active (v1 Scope -- Pending Implementation)

### Operational (Urgent -- Weeks Timeline)

| ID     | Requirement                                   | Status | Linear | Notes                     |
| ------ | --------------------------------------------- | ------ | ------ | ------------------------- |
| OPS-01 | Configure HotelRunner prices for all 12 rooms | Active | EM-149 | Blocking daily operations |
| OPS-02 | Finalize reservation for room 11              | Active | EM-150 | Blocking daily operations |
| OPS-03 | Upload Room 12 photos to HotelRunner          | Active | EM-135 | Content gap               |
| OPS-04 | Organize professional photos by room          | Active | EM-144 | Content gap               |

### Platform Integration (High Priority)

| ID     | Requirement                                       | Status | Linear | Notes                 |
| ------ | ------------------------------------------------- | ------ | ------ | --------------------- |
| INT-02 | Scout HotelRunner Developer API capabilities      | Active | EM-146 | Integration research  |
| INT-03 | Obtain HotelRunner Admin Access for Omar          | Active | EM-142 | Access blocker        |
| INT-04 | Connect Expedia via HotelRunner                   | Active | --     | Pending configuration |
| INT-05 | Investigate Booking.com property type discrepancy | Active | EM-143 | Data consistency      |

### Data Architecture (High Priority)

| ID      | Requirement                             | Status | Linear | Notes               |
| ------- | --------------------------------------- | ------ | ------ | ------------------- |
| DATA-03 | Villa Thaifa Room-Centric Restructuring | Active | EM-141 | Architecture change |

### Documentation (Medium Priority)

| ID     | Requirement                                 | Status | Linear | Notes                  |
| ------ | ------------------------------------------- | ------ | ------ | ---------------------- |
| DOC-01 | Create HotelRunner Dashboard Guide for Said | Active | EM-140 | End-user documentation |

## Out of Scope (Explicit Boundaries)

| Item                                   | Rationale                                                      |
| -------------------------------------- | -------------------------------------------------------------- |
| Direct booking channel (EM-155)        | Said's business decision, not Omar's technical priority        |
| Real-time reservation updates          | Batch daily acceptable; reCAPTCHA/OTP barriers block real-time |
| AI agent for reservation mgmt (EM-154) | Defer to v2; operational stability first                       |
| Guest-facing mobile app                | Web-first; mobile PWA deferred                                 |
| Financial accounting system            | Use existing tools; not in scope                               |
| Staff scheduling system                | Not needed for 12-room property                                |
| Building PMS from scratch              | Leverage HotelRunner; integrate, don't replace                 |

## Technical Context (from PROJECT.md)

### Tech Stack (Existing)

- **Core**: Next.js 16.1.3 + React 19.2.3 + TypeScript 5.9.3
- **Database**: SQLite 3 (local-first, `property.db` with WAL mode)
- **Validation**: Zod 4.3.5 (runtime schemas + TypeScript types)
- **Automation**: agent-browser (headless browser CLI, npm global)
- **Architecture**: Feature-based, dual data sources (JSON public / SQLite admin), no ORM

### Key Constraints

- **Authentication barriers**: HotelRunner (reCAPTCHA), Booking.com (OTP), Expedia (SMS 2FA)
- **API rate limits**: HotelRunner 250 req/day, 5 req/min
- **Browser automation bug**: agent-browser doesn't persist cookies (manual login per session)
- **SQLite deployment**: Requires persistent file storage (not serverless-compatible)
- **Webhook requirements**: HotelRunner API needs HTTPS callback URL (no domain/HTTPS setup)

### Key Decisions (from PROJECT.md)

| Decision                          | Rationale                                          | Status  |
| --------------------------------- | -------------------------------------------------- | ------- |
| Use SQLite (not cloud DB)         | Local-first simplicity, sufficient for 12 rooms    | Pending |
| Browser automation (not full API) | API rate-limited, reCAPTCHA blocks full automation | Pending |
| Defer direct booking channel      | Said's business decision                           | Good    |
| Urgent operational focus (weeks)  | EM-149, EM-150, EM-135 blocking daily work         | Pending |
| Feature-based architecture        | Clearer domain boundaries, easier to maintain      | Pending |

---

_Source: `context/meta/planning/PROJECT.md` (last updated 2026-01-30). Archived to `archive/context-meta-planning-PROJECT.md`._

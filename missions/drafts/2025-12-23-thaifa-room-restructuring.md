# Mission: Villa Thaifa Room-Centric Restructuring

```yaml
# Core Metadata
mission_id: 2025-12-23-thaifa-room-restructuring
type: FEATURE
status: DRAFT
priority: P1 # Client request, blocking other missions

# Assignment
assigned_to: Claude Code
created: 2025-12-23
assigned:
claimed_at:
claimed_by:
completed:
archived:

# Source tracking
source_session: "Thaifa session 2025-12-23"
source_insight: "M. Said Thaifa prefers room-number-centric view over type-grouped"

# Verification (Updated by /mission complete)
verification:
  self_reviewed: false
  gates_passed: "0/7"
  blocking_issues: []
  last_verified:
```

---

## Context

After state-management restructuring, we presented data to M. Said Thaifa. He provided feedback that the type-grouped room structure confused him — he habitually references rooms by number in daily operations ("Room 7 needs...").

**Business Impact**: Structure must match client's mental model for effective communication and management.

**Decision Reference**: `shared/memory/decisions.md` — [2025-12-23] Room-Centric Data Model

---

## Objectives

- [ ] Create 12 individual room files following room-centric structure
- [ ] Create facilities files (spa, pool, garden, hall)
- [ ] Create master index files (hotel/README.md, facilities/README.md)
- [ ] Update cross-references in pricing and CLAUDE.md
- [ ] Deprecate old rooms.md with header notice

---

## Success Criteria

| #   | Criterion                               | Status | Evidence |
| --- | --------------------------------------- | ------ | -------- |
| 1   | 12 room files exist in rooms/           | ⬜     |          |
| 2   | 4 facility files exist in facilities/   | ⬜     |          |
| 3   | hotel/README.md indexes all rooms       | ⬜     |          |
| 4   | facilities/README.md indexes all        | ⬜     |          |
| 5   | rooms.md has deprecation notice         | ⬜     |          |
| 6   | pricing.md references new structure     | ⬜     |          |
| 7   | CLAUDE.md data locations updated        | ⬜     |          |

---

## Constraints

- Must use existing room data from current rooms.md
- File naming: `XX-type.md` (e.g., `01-deluxe-triple.md`)
- Unknown data marked as `[TBD - Ask Said]` or `[TBD - Booking.com]`
- Maintain compatibility with state-management standard

---

## Specification

### Requirements

| ID      | Description                        | Acceptance Criteria               | Priority | Status |
| ------- | ---------------------------------- | --------------------------------- | -------- | ------ |
| REQ-001 | Individual room files              | 12 files, each with template data | MUST     | ⬜     |
| REQ-002 | Facilities directory               | spa, pool, garden, hall files     | MUST     | ⬜     |
| REQ-003 | Master indexes                     | README.md in hotel/ and facilities/ | MUST   | ⬜     |
| REQ-004 | Cross-reference updates            | pricing.md, CLAUDE.md updated     | MUST     | ⬜     |
| REQ-005 | Deprecation notice                 | rooms.md header warns users       | SHOULD   | ⬜     |

### Task Breakdown

| ID       | Task                                      | Requirement | Status | Evidence |
| -------- | ----------------------------------------- | ----------- | ------ | -------- |
| TASK-001 | Create rooms/ directory                   | REQ-001     | ⬜     |          |
| TASK-002 | Create 12 room files from template        | REQ-001     | ⬜     |          |
| TASK-003 | Fill room data from rooms.md              | REQ-001     | ⬜     |          |
| TASK-004 | Create facilities/ directory              | REQ-002     | ⬜     |          |
| TASK-005 | Create spa.md (includes hammam)           | REQ-002     | ⬜     |          |
| TASK-006 | Create pool.md                            | REQ-002     | ⬜     |          |
| TASK-007 | Create garden.md                          | REQ-002     | ⬜     |          |
| TASK-008 | Create hall.md                            | REQ-002     | ⬜     |          |
| TASK-009 | Create hotel/README.md index              | REQ-003     | ⬜     |          |
| TASK-010 | Create facilities/README.md index         | REQ-003     | ⬜     |          |
| TASK-011 | Update pricing.md references              | REQ-004     | ⬜     |          |
| TASK-012 | Update CLAUDE.md data locations           | REQ-004     | ⬜     |          |
| TASK-013 | Add deprecation notice to rooms.md        | REQ-005     | ⬜     |          |

### Technical Plan

**Directory Structure**:
```
data/specs/configs/
├── hotel/
│   ├── README.md                   # INDEX of all assets
│   ├── rooms.md                    # DEPRECATED (kept for transition)
│   └── rooms/                      # NEW: Individual room files
│       ├── 01-deluxe-triple.md
│       ├── 02-deluxe-double.md
│       ├── ... (rooms 03-11)
│       └── 12-presidential-suite.md
│
├── facilities/                     # NEW: Non-room assets
│   ├── README.md
│   ├── spa.md                      # Including hammam as sub-area
│   ├── pool.md
│   ├── garden.md
│   └── hall.md
```

---

## Execution Log

> Append-only. Add entries as work progresses.

### 2025-12-23

- 19:45 - Mission created in drafts/ directory

---

## Deviations

[Document any differences from original spec. What changed and why.]

---

## Lessons Learned

[What to do differently next time. Patterns to extract. Rules to add.]

---

## Quality Gates (Pre-Archive)

- [ ] All success criteria have evidence
- [ ] All requirements validated
- [ ] All tasks completed
- [ ] Execution log is complete
- [ ] Deviations documented
- [ ] Lessons learned captured
- [ ] Files in correct archive location

---

_Mission created from template v0.3.0 (verification-enhanced)_

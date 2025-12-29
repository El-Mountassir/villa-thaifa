# Mission: Extract Room Data from Booking.com — Villa Thaifa

```yaml
# Core Metadata
mission_id: 2025-12-23-thaifa-booking-data
type: RESEARCH
status: DRAFT
priority: P2

# Assignment
assigned_to: Claude Code (with --chrome)
created: 2025-12-23
assigned:
claimed_at:
claimed_by:
completed:
archived:

# Source tracking
source_session: "Thaifa session 2025-12-23"
source_insight: "Need individual room characteristics for new room-centric structure"

# Verification (Updated by /mission complete)
verification:
  self_reviewed: false
  gates_passed: "0/7"
  blocking_issues: []
  last_verified:
```

---

## Context

Villa Thaifa has 12 rooms. The new room-centric structure needs individual characteristics per room (size, view, unique features). Booking.com may have this data.

**Agent Required**: Claude Code with `--chrome` flag for browser automation

**Dependencies**: M1 (room files must exist to receive data)

---

## Objectives

- [ ] Navigate to Villa Thaifa Booking.com listing
- [ ] Extract per-room data if available (size, view, features)
- [ ] Document extraction findings in structured report
- [ ] Update individual room files with extracted data

---

## Success Criteria

| #   | Criterion                                        | Status | Evidence |
| --- | ------------------------------------------------ | ------ | -------- |
| 1   | Booking.com listing accessed                     | ⬜     |          |
| 2   | All 12 rooms checked for individual data         | ⬜     |          |
| 3   | Extraction report generated                      | ⬜     |          |
| 4   | "Not available" documented if type-level only    | ⬜     |          |
| 5   | Room files updated with any extracted data       | ⬜     |          |

---

## Constraints

- Target URL: https://www.booking.com/hotel/ma/riad-salim-amp-spa.html
- Use `--chrome` flag for proper browser access
- If only type-level data exists, document that clearly
- Do not modify room files if no new data found

---

## Research Protocol

### Data to Extract (per room if available)

| Data Point | Source | Priority |
|------------|--------|----------|
| Room size (m²) | Booking.com room details | High |
| View type | Booking.com or photos | High |
| Unique features | Room description | Medium |
| Room-specific photos | Photo gallery | Low |

### Expected Outcomes

| Scenario | Action |
|----------|--------|
| Per-room data available | Extract and update room files |
| Only type-level data | Document limitation, Omar to ask Said |
| Data partially available | Extract what's there, mark rest TBD |

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

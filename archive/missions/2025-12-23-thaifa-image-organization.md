# Mission: Villa Thaifa Image Organization

```yaml
# Core Metadata
mission_id: 2025-12-23-thaifa-image-organization
type: STANDARD
status: DRAFT
priority: P2

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
source_insight: "Professional photos exist but need organization by room/facility"

# Verification (Updated by /mission complete)
verification:
  self_reviewed: false
  gates_passed: "0/7"
  blocking_issues: []
  last_verified:
```

---

## Context

Omar mentioned `images/` folder with professional photos from HWS/HotelRunner photographer (Ikram). These need to be organized by room and facility for the new room-centric structure.

**Known Issue**: Room 12 photos are missing — Omar to contact Ikram.

---

## Objectives

- [ ] Verify images directory exists and inventory contents
- [ ] Create organized directory structure (rooms/XX/, facilities/)
- [ ] Move/organize photos into correct directories
- [ ] Document missing photos (especially Room 12)
- [ ] Create image index README.md

---

## Success Criteria

| #   | Criterion                               | Status | Evidence |
| --- | --------------------------------------- | ------ | -------- |
| 1   | Images directory audited                | ⬜     |          |
| 2   | rooms/ subdirectories created (01-12)   | ⬜     |          |
| 3   | facilities/ subdirectories created      | ⬜     |          |
| 4   | Photos organized into correct locations | ⬜     |          |
| 5   | Missing photos documented (Room 12)     | ⬜     |          |
| 6   | images/README.md index created          | ⬜     |          |

---

## Constraints

- Do not delete any photos
- Preserve original filenames
- Document source of each photo if known
- Room 12 missing — flag for Omar action

---

## Specification

### Target Structure

```
images/
├── README.md                 # Photo inventory with metadata
├── rooms/
│   ├── 01/
│   ├── 02/
│   ├── ...
│   └── 12/                   # MISSING - Omar to contact Ikram
├── facilities/
│   ├── spa/
│   ├── hammam/
│   ├── pool/
│   ├── garden/
│   └── hall/
└── general/
    ├── exterior/
    └── common-areas/
```

### Task Breakdown

| ID       | Task                        | Status | Evidence |
| -------- | --------------------------- | ------ | -------- |
| TASK-001 | Verify images/ exists       | ⬜     |          |
| TASK-002 | Inventory current photos    | ⬜     |          |
| TASK-003 | Create directory structure  | ⬜     |          |
| TASK-004 | Organize photos by room     | ⬜     |          |
| TASK-005 | Organize photos by facility | ⬜     |          |
| TASK-006 | Document missing (Room 12)  | ⬜     |          |
| TASK-007 | Create README.md index      | ⬜     |          |

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

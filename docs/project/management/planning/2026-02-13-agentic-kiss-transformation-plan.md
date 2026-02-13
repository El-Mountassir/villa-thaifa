# Agentic KISS Transformation Plan (v1)

## Objective

Build a reliable, low-complexity digital operating system for Villa Thaifa that supports 2 human operators (Omar and Said) and multiple AI agents, without over-engineering.

## Context and Constraints

- Team size: 2 humans + AI agents
- Priority: correctness, traceability, speed of operations
- Principle: KISS (no premature backend/platform complexity)
- Current state: canonical markdown consolidation in progress by domain

## Strategic Direction

1. Data-first canonical layer (markdown SSOT)
2. Deterministic automation layer (validation + reconciliation scripts)
3. Minimal internal app only after data contracts stabilize

## Timeline (No Time Bias)

| Phase   | Duration | Goal                                                           |
| ------- | -------- | -------------------------------------------------------------- |
| Phase 1 | Week 1   | Stabilize canonical data + contracts + reconciliation workflow |
| Phase 2 | Week 2   | Add automation scripts and one-command verification            |
| Phase 3 | Week 3   | Launch minimal internal read-first app on top of stable data   |

## Target Architecture (KISS)

### Layer 1: Canonical Data

- Format: Markdown tables + structured profile sections where needed
- Each canonical file must include:
  - data contract
  - required fields/columns
  - allowed values/defaults
  - reconciliation traceability
- Legacy files are deleted only after strict unique-information checks pass.

### Layer 2: Validation and Reconciliation

Template pack for repeatable artifacts:
- `docs/project/templates/canonical-domain-template.md`
- `docs/project/templates/reconciliation-entry-template.md`
- `docs/project/templates/deletion-safety-report-template.md`
- `docs/project/templates/weekly-summary-template.md`

- Python CLI scripts to:
  - validate schema shape
  - compare legacy vs canonical
  - emit deletion safety reports
- One command runs all checks for priority domains.
- Template engine for large-scale generation:
  - Jinja2 templates rendered from structured data
  - Deterministic generation only (no free-form AI text at render step)

### Layer 3: Minimal Internal App (later)

- Read-first app for operations visibility
- Form-based edits only for selected high-confidence fields
- App consumes canonical data; app does not become SSOT in v1

## Recommended Tech Stack

### Now

- Markdown (canonical SSOT)
- Git (history, rollback, audit)
- Python 3 CLI scripts managed with uv
- Jinja2 for scripted markdown generation from structured data
- Pytest for validation tests (via uv)

### Later (Phase 3)

- FastAPI (internal API)
- HTMX + server-rendered templates (simple UI)
- SQLite optional read index (if needed for faster queries)

### Explicitly Deferred

- Microservices
- Kubernetes
- Complex event architecture
- Multi-tenant auth platforms

## SDLC Operating Model (Human + Agent)

| Step        | Owner | Output                             |
| ----------- | ----- | ---------------------------------- |
| Scout       | Agent | facts, source inventory, risks     |
| Consolidate | Agent | canonical update + backup          |
| Verify      | Agent | strict diff + uniqueness report    |
| Approve     | Omar  | go/no-go for deletion or next step |
| Log         | Agent | reconciliation record + evidence   |

## Definition of Done (Per Domain)

A domain is done only when all are true:

1. Canonical file has explicit data contract.
2. Required columns/fields are complete.
3. Validation scripts pass.
4. Reconciliation log includes source mapping and decisions.
5. Legacy files are either:
   - safely deleted, or
   - kept with explicit reason and owner.

## Domain Sequence (Suggested)

1. Rooms (finish current thread)
2. Amenities
3. Facilities
4. Pricing rules
5. Reservation mapping and workflow references

## Risk Controls

- Backup before each mutation (`cp file file.backup-YYYY-MM-DD`)
- One file at a time
- No deletion without strict unique-info gate
- Keep irreversible actions only after explicit confirmation

## Decision Rules

- If a value conflicts and confidence is low: do not overwrite, mark `owner_pending`.
- If two sources disagree and one is platform-confirmed (Booking/HotelRunner): prioritize platform-confirmed value and log evidence.
- If a field is useful but unstable: keep it in profile/alias section, not as strict table field.

## Success Metrics

- % of priority domains with canonical contracts complete
- # of legacy files safely retired
- # of validation failures per week
- Lead time from new source to canonical update

## Exit Criteria to Start App Coding

Start coding app layer only when:

1. At least 3 core domains are canonical and validated.
2. One-command verification is stable.
3. Deletion workflow is proven on at least one domain.
4. Omar confirms schema freeze for v1 operations.

# Agentic Operating Playbook (v1)

## Purpose

Provide a practical operating system for Omar, Said, and AI agents to run digital transformation work safely and consistently.

## Weekly Cadence

| Day | Focus | Output |
| --- | --- | --- |
| Monday | Prioritize domains and risks | weekly backlog lock |
| Tuesday-Thursday | Consolidation + validation | canonical updates + logs |
| Friday | Review and freeze | deletion decisions + carry-over list |

## Daily Workflow

1. Select one domain and one source file.
2. Read source + canonical + reconciliation log.
3. Apply minimal changes to canonical.
4. Run strict verification.
5. Update reconciliation log with evidence.
6. Decide keep/delete for processed source.

## Template Pack

Use templates from `docs/project/templates/` for consistent execution artifacts:

1. `canonical-domain-template.md`
2. `reconciliation-entry-template.md`
3. `deletion-safety-report-template.md`
4. `weekly-summary-template.md`

## Template Engine (Jinja2)

Use Jinja2 for high-volume, repeatable generation from structured data.

Rules:

1. Keep templates deterministic and reviewable in Git.
2. Use structured inputs (JSON/YAML/CSV), not free-form prompts.
3. Generate into explicit target paths, then run verification scripts.
4. Treat generated output as draft until reconciliation checks pass.

## Backlog Template

Use this structure for each work item:

```markdown
## [ID] Domain - Source file
- Goal:
- Source:
- Canonical target:
- Unique info to migrate:
- Verification command(s):
- Deletion gate result:
- Final decision:
```

## Standard Commands (Guideline)

```bash
# inventory and context
ls -la data/core/property/inventory/rooms

# strict text scan
rg -n "pattern" data/core/property/inventory/rooms

# compare files
diff -u source.md canonical.md

# install/sync Python deps
uv sync

# run validation scripts
uv run python scripts/domain_verify.py

# quick row count checks (example)
uv run python scripts/validate_contracts.py
```

## Test Commands

```bash
# run full script tests
make test

# run specific tests
uv run pytest tests/test_scripts.py
```

## Proposed Script Set (Phase 2)

| Script | Purpose |
| --- | --- |
| `scripts/validate_contracts.py` | Verify required columns/fields in canonical files |
| `scripts/check_unique_info.py` | Detect source-only data before deletion |
| `scripts/domain_verify.py` | One-command domain verification summary |

## Reconciliation Log Standard

Each step entry must include:

1. Source file and date
2. Fields compared
3. Accepted changes
4. Rejected conflicts
5. Evidence source (platform screenshot, docs)
6. Deletion safety outcome

## Deletion Safety Gate

A source file can be deleted only if:

1. No unique semantic information remains outside canonical.
2. Canonical includes all required metadata and profile content.
3. Validation checks pass.
4. Decision and evidence are logged.

## Agent Role Split

| Role | Responsibility |
| --- | --- |
| Scout Agent | gather and structure source facts |
| Builder Agent | mutate canonical safely |
| Auditor Agent | strict checks and deletion gate |
| Owner (Omar) | approve final decisions on ambiguous points |

## Escalation and Stop Rules

Stop and ask Omar when:

1. contradictory values with no trusted evidence
2. destructive action not explicitly approved
3. schema change has broad downstream impact

## Practical Scope Guardrails

Do now:

- canonical data quality
- deterministic verification
- one-domain-at-a-time cleanup

Do later:

- broad UI implementation
- complex backend services
- non-essential integrations

## Phase Transition Checklist

Transition from Phase 1 to Phase 2 when:

- 3 domains have canonical contracts
- reconciliation process is stable
- deletion gate is proven

Transition from Phase 2 to Phase 3 when:

- one-command verify is reliable
- v1 schema is frozen
- Omar validates operational readiness

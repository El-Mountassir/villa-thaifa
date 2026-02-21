# Agent Handoff (Quick Start)

## Read Order (fast)

1. `AGENTS.md`
2. `ROADMAP.md`
3. `ops/status/INDEX.md`
4. `ops/status/working.md`
5. `ops/status/canonical.md`

## Critical Context

- Repository is WIP and partially decoupled.
- Unprocessed sources are contestable by default.
- Rooms domain is currently the most stabilized inventory domain.
- Remote main integration is pending; bootstrap branch contains latest local operational baseline.
- Content lanes exist and must be respected: `data/`, `context/meta/`, `data/pending-domains/`.

## Must-Preserve Open Loops

1. Pending inventory domains:

- `data/pending-domains/amenities.md`
- `data/pending-domains/facilities.md`
- `data/pending-domains/beds.md`
- `data/pending-domains/inventory.md`

2. Pending finance domain:

- `data/finance/`

3. Contestable duplicate docs:

- `context/meta/knowledge/`

4. Content triage backlog:

- `context/meta/`

5. SCM integration backlog:

- safe integration plan for `origin/main`

## Mandatory Behavior

1. Work one sensitive data file at a time.
2. Backup before mutation.
3. Run verification scripts before closing task.
4. Log decisions in status and reconciliation artifacts.
5. Ask Omar for high-impact ambiguities with options + recommendation.

## Ultra-Fast Entry

- `ops/handoff/AI-SESSION-STARTER.md`

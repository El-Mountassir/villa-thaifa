# Decision: json-render Framework Evaluation

**Date**: 2026-02-21
**Status**: REJECTED
**Participants**: Omar, Nova

## Context

Evaluated Vercel Labs' json-render framework for generating Villa Thaifa operational dashboards from JSON specs via AI.

## Evaluation

- Built a full Next.js demo with VT rates.json + property-config.json data
- Tested twice: original spec (3/10) and fixed spec (1/10 — worse)
- Framework concept is sound (component catalog constraining AI output)
- Renderer is broken: grids don't work, cards overlap, spacing nonexistent

## Decision

**REJECTED for all immediate use.**

- Villa Thaifa: No. Overkill + broken renderer.
- LHCM-OS: Watch & wait. Revisit if Vercel stabilizes the renderer.
- The end-to-end pipeline CONCEPT (prompt → LLM → spec → UI) remains valuable for LHCM-OS and Nova UI project.

## Alternative chosen

Option B+C: Build dashboards with frontend-ui agent + Next.js + Tailwind + shadcn/ui directly (no json-render abstraction layer).

## Artifacts

- Demo: ~/omar/labs/demos/json-render-villa-thaifa/
- Evaluation: ~/omar/knowledge/research/development/json-render-evaluation.md
- Skill created: ~/omar/core/resources/skills/framework-evaluation.md
- Rule added: rules.md §Demo & Prototype Preservation
- Agent created: frontend-ui (~/omar/core/resources/agents/development/frontend-ui.md)

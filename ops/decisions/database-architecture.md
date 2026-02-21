# Decision: Villa Thaifa Database Architecture

> **Date**: 2026-02-16
> **Status**: Approved
> **Decider**: Omar

## Decision

**Neon** (serverless PostgreSQL) — scored 7.95/10 in weighted analysis.

## Context

Data is currently in markdown/JSON files. Need a database optimized for AI agent access via MCP, with multi-property scale and modern human UI capability.

## Options Evaluated

| Option | Score | Status |
|--------|-------|--------|
| Neon (serverless PostgreSQL) | 7.95 | **Selected** |
| Supabase (hosted PG + BaaS) | 7.70 | Runner-up |
| Self-hosted PostgreSQL | 6.93 | Viable |
| SQLite + Turso | 6.23 | Too limited |
| Neo4j | 5.25 | Paradigm mismatch |
| Airtable | 4.50 | Rate-limited |
| Status Quo (files) | 2.80 | Inadequate |

## Why Neon

1. Purpose-built MCP server for AI agents (schema introspection, query tuning, safe migrations)
2. Database branching (git-like branches for safe schema testing)
3. Scale-to-zero without pausing (free tier actually usable)
4. Database-per-tenant for multi-property isolation
5. ~2.5x cheaper than Supabase for intermittent workloads

## Sensitivity

Result is BRITTLE on UI Readiness dimension. If human UI urgency increases, Supabase overtakes. Acceptable because: agents are primary consumers, UI is a separate later concern, and migration between them is standard pg_dump/restore.

## Phasing

- **Phase A (NOW)**: Consolidate scattered data into data/ as SSOT (no DB yet)
- **Phase B (FUTURE)**: Migrate to Neon when data is complete
  - Free tier: 100 CU-hours/mo, 0.5 GiB
  - Paid: Launch $19/mo or Scale $69/mo

## Contingency

If UI urgency spikes, migrate to Supabase in <1 day via pg_dump/restore.

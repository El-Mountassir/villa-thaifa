# AGENTS.md — Villa Thaifa Workspace Contract

## Repository Structure

@STRUCTURE.md

## Mission

@MISSION.md

## Mandatory Workflow

Use this sequence for every operational task:

1. SCOUT
2. REPORT
3. QUESTIONS
4. ACTION

## Core Principles

1. Canonical-first: one active source of truth per domain.
2. One-file-at-a-time changes for sensitive inventory domains.
3. Backup before mutation using `cp file archives/YYYY/QQ/file.backup-YYYY-MM-DD-HHMMSS.md`.
4. No deletion without a documented reconciliation gate.
5. Keep state visible in `ops/status/`.
6. KISS default: markdown-first until contracts are stable.
7. If confidence is low, mark as `owner_pending` and escalate.

## Contestability Policy (Critical)

1. Treat all unprocessed data as potentially outdated, suboptimal, or contestable.
2. Do not silently trust legacy sources.
3. Ask Omar for clarification whenever decisions are ambiguous or high impact.
4. When asking, provide short options with one recommended default.
5. Log the chosen decision in status/reconciliation artifacts.

## Data Handling Policy

1. Legacy files are reference-only until reconciled.
2. Archive with checksum before removal from active scope.
3. Record accepted/rejected conflicts in domain reconciliation logs.
4. Do not overwrite conflicting values without trusted evidence.

## Git/GitHub Sync Policy

1. Keep repo synced at least:
   - start of day
   - after each completed domain milestone
   - end of day
2. Work from short-lived branches with explicit scope.
3. Never keep critical local-only changes unpushed.

## Definition of Done (Per Domain)

All must be true:

1. Canonical contract is explicit.
2. Validation scripts pass.
3. Reconciliation log is updated with evidence.
4. Legacy files are archived/deleted with explicit justification.
5. Status files are updated.

## Open Loops (Do Not Drop)

1. Pending data domains: `data/pending-domains/` (amenities, beds, facilities)
2. Pending content triage: `docs/pending/`
3. Finance data: `data/finance/` (billing/rates not yet onboarded)
4. SCM branch merge: `bootstrap/2026-02-13-baseline` → `main`

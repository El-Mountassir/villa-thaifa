# AGENTS.md — Villa Thaifa Workspace Contract

## Repository Structure

@docs/core/STRUCTURE.md

### File Organization Rules

**Files that MUST remain at repository root:**

- `AGENTS.md` — AI agent workspace contract (this file)
- `CLAUDE.md` — Claude Code project instructions
- `GEMINI.md` — Gemini AI project instructions
- `README.md` — Standard repository documentation (universal convention)
- `CHANGELOG.md` — Version history (standard convention)

**Rationale:** AI agent contract files (AGENTS.md, CLAUDE.md, GEMINI.md) must be at root for AI systems to discover and load them. README.md and CHANGELOG.md follow universal open-source conventions.

**Foundational definitions** (MISSION, STRUCTURE, PRINCIPLES) live in `docs/core/`.

## Mission

@docs/core/MISSION.md

## Mandatory Workflow

Use this sequence for every operational task:

1. SCOUT
2. REPORT
3. QUESTIONS
4. ACTION

## Scope

This repo is **Villa Thaifa operations** — property data, rooms, bookings, guest comms, WhatsApp integration, Said Thaifa (owner) context.

## LHCM-OS (broader vision)

LHCM-OS (Lightweight Hotel Channel Management OS) is a separate, broader product vision where Villa Thaifa is the first pilot. LHCM-OS lives at `~/omar/professional/projects/lhcm-os/` — NOT in this repo. You may reference LHCM-OS docs but do not duplicate or merge them here.

## Core Principles

@docs/core/PRINCIPLES.md

## Policies

### Contestability Policy (Critical)

1. Treat all unprocessed data as potentially outdated, suboptimal, or contestable.
2. Do not silently trust legacy sources.
3. Ask Omar for clarification whenever decisions are ambiguous or high impact.
4. When asking, provide short options with one recommended default.
5. Log the chosen decision in status/reconciliation artifacts.

### Data Handling Policy

1. Legacy files are reference-only until reconciled.
2. Archive with checksum before removal from active scope.
3. Record accepted/rejected conflicts in domain reconciliation logs.
4. Do not overwrite conflicting values without trusted evidence.

### Git/GitHub Sync Policy

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

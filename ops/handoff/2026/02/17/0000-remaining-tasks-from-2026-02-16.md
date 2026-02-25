# Handoff: Remaining Tasks (Non-Linear)

> **Updated**: 2026-02-17
> **Scope**: All pending tasks EXCEPT Linear/Work Orchestration System items
> **Linear tasks**: See `ops/handoff/handoff-linear-migration-preparation.md` and `ops/handoff/handoff-work-orchestration-system.md`

---

## How to Use This File

For each task:

1. **VERIFY** the "check if done" step first
2. If already done → mark DONE and move on
3. If partially done → pick up where it left off
4. If not started → execute using the instructions

**Goal**: All durable items here should eventually migrate to Linear as issues. This file is a transitional artifact.

---

## Completed Tasks (for reference)

- [x] **Enforce Edit-over-Write hook** — DONE. Hook at `~/.claude/hooks/enforce-edit-over-write.sh`, tested 4/4 pass.
- [x] **Gemini delegation hook** — DONE. Hook at `~/.claude/hooks/block-html-writes.sh`, tested 4/4 pass.
- [x] **Hooks end-to-end test** — DONE (2026-02-17). All 4 tests passed.

---

## Task: Language Audit — Scan for French

**Priority**: Medium
**Check if done**: `grep -rl 'Chambre\|Réservation\|Bienvenue\|Bonjour' ~/.claude/handlers/ ~/.claude/hooks/ --include='*.py'` — if no results, handlers are clean. Also check `~/.claude/output-styles/nova-dyad.md` for French.
**What**: Scan all .md, .py, .json files in villa-thaifa/ and ~/.claude/ for French text. Fix by replacing with English.
**Exceptions**: French room descriptions in data/rooms/RXX/profile.md are OTA data from Booking.com — KEEP those in French (they're canonical data, not our output).
**What to scan**: `~/.claude/handlers/*.py`, `~/.claude/hooks/*.py`, `ops/handoff/*.md`, `docs/**/*.md`

---

## Task: /decide Governance Format

**Priority**: Medium
**Check if done**: `ls ~/omar/knowledge/research/development/repo-organization/governance-*` — if a decision file exists with a clear verdict, it's done.
**What**: Use /decide skill to evaluate: human-standard governance (CONTRIBUTING.md, CODE_OF_CONDUCT.md, etc.) vs AI-adapted versions.
**Handoff file**: `ops/handoff/handoff-governance-decide.md` — read this for full context.
**Decision**: Which governance files to include and in what format for AI-managed repos.

---

## Task: Design Archive/Lifecycle System

**Priority**: Medium
**Check if done**: `ls ~/omar/knowledge/research/development/ | grep archive` — if a design doc exists, it's done or in progress.
**What**: Design a system for archiving completed work. Omar's pain point: completed work never gets archived, cluttering active directories.
**Approach**: Use skills: /systems-thinking, /sequential-thinking, /brainstorming, /decide
**Key questions**: When to archive? Where? How to find archived items? Automated triggers?
**Output**: Design doc at ~/omar/knowledge/research/development/archive-lifecycle-design.md

---

## Task: GitHub Template Repos

**Priority**: Low (blocked by governance decision)
**Check if done**: Check if GitHub template repos exist at github.com/omar-elmountassir
**What**: Create GitHub Template Repos for Villa Thaifa patterns.
**Handoff file**: `ops/handoff/handoff-github-template-repos.md`
**Blocker**: Governance format decision must be made first.

---

## Task: Build /repo-bootstrap Skill

**Priority**: Low (after governance)
**Check if done**: `ls ~/.claude/skills/ | grep repo-bootstrap`
**What**: Build the /repo-bootstrap skill using Copier (Jinja2 template engine).
**Design doc**: `~/omar/knowledge/research/development/repo-bootstrap/skill-design.md`
**Blocked by**: Governance decision (#24)

---

## Task: Comprehensive Model Routing Strategy

**Priority**: Low
**Check if done**: `ls ~/omar/knowledge/research/ai/ | grep model-routing`
**What**: Full strategy doc covering all Claude + Gemini model variants, when to use each.
**Current state**: Lightweight heuristic in `~/.claude/rules/rules.md` § AI Model Delegation. Needs expansion.

---

## Summary

6 non-Linear tasks remain. Priority order:
1. Language audit (medium)
2. /decide governance format (medium, blocks #3 and #4)
3. Design archive/lifecycle system (medium)
4. GitHub Template Repos (low, blocked by governance)
5. Build /repo-bootstrap skill (low, blocked by governance)
6. Comprehensive model routing strategy (low)

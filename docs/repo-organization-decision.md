# Repository Organization — Decision & Action Plan

**Status:** Decided
**Date:** 2026-02-16
**Decision:** Move MISSION.md and STRUCTURE.md to `docs/core/` (scored 8.05/10, full analysis archived)

---

## Constraints (Settled)

| File | Location | Why |
|------|----------|-----|
| AGENTS.md | Root | AI agent discoverability (Claude Code loads from root) |
| CLAUDE.md | Root | Claude Code requires root placement |
| GEMINI.md | Root | Gemini requires root placement |
| README.md | Root | Universal convention, GitHub displays first |
| CHANGELOG.md | Root | Industry standard, changelog tools expect root |

Documented in AGENTS.md under "File Organization Rules".

---

## Target Structure (After All Actions)

```
Root (5 .md files + config):
├── AGENTS.md          AI agent workspace contract
├── CLAUDE.md          Claude Code project instructions
├── GEMINI.md          Gemini project instructions
├── README.md          Repository overview
├── CHANGELOG.md       Version history
├── pyproject.toml     Python config
├── uv.lock            Lock file
├── Makefile           Build tasks
├── .gitignore         Git ignore
└── .labels.json       Labels config

docs/core/ (foundational definitions):
├── PRINCIPLES.md      Core principles (rename from PRINCIPLES)
├── MISSION.md         Project mission (move from root)
└── STRUCTURE.md       Repository layout (move from root)
```

---

## Action Checklist

### Immediate (from this session) — COMPLETED

- [x] Move `MISSION.md` → `docs/core/MISSION.md`
- [x] Move `STRUCTURE.md` → `docs/core/STRUCTURE.md`
- [x] Update `AGENTS.md`: `@MISSION.md` → `@docs/core/MISSION.md`
- [x] Update `AGENTS.md`: `@STRUCTURE.md` → `@docs/core/STRUCTURE.md`
- [x] Rename `docs/core/PRINCIPLES` → `docs/core/PRINCIPLES.md` (was already .md)
- [x] Update `AGENTS.md`: `@docs/core/PRINCIPLES.md` (verified — already correct)
- [x] Update `STRUCTURE.md` content to reflect its new location and final layout
- [x] Verify @reference chain works: CLAUDE.md → AGENTS.md → docs/core/* (ALL PASS)
- [x] Delete redundant files:
  - `docs/research-repo-organization.md` (deleted)
  - `~/omar/knowledge/research/development/repo-organization/contracts-directory-decision.md` (deleted)

### Missing Items (identified by research)

- [ ] Verify/add `LICENSE` at root (required for tool detection, currently absent)
- [ ] Review `README.md` content (should have project overview + links to docs/core/)
- [ ] Decide: Add `.github/` directory? (for CODEOWNERS, issue templates, workflows)
- [ ] Decide: Add `CONTRIBUTING.md`? (root or docs/ — only if expecting contributions)
- [ ] Decide: Add `CODE_OF_CONDUCT.md`? (only if open-source)
- [ ] Decide: Add `SECURITY.md`? (only if open-source)

---

## Key Research Findings (Summary)

- GitHub recognizes governance files in: root, `.github/`, `docs/`
- LICENSE must be at root for scanner tools
- ~10-15 root files is optimal, >20 is cluttered (we'll be at ~10)
- CLAUDE.md and AGENTS.md are emerging conventions, always at root
- `docs/core/` already had PRINCIPLES — adding MISSION and STRUCTURE creates semantic coherence

Full research sources archived in git history.

---

## docs/core/ Scope Rule

**Purpose:** Foundational project definitions that rarely change.

**Belongs here:** PRINCIPLES, MISSION, STRUCTURE
**Does NOT belong here:** Policies, SLAs, processes → use `docs/policies/` when needed

If docs/core/ grows beyond 5-7 files, reassess whether governance needs a separate namespace.

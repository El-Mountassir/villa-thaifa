# Repository Organization — Decision & Action Plan

**Status:** Decided
**Date:** 2026-02-16
**Decision:** Move MISSION.md and STRUCTURE.md to `docs/core/` (scored 8.05/10, full analysis archived)

---

## Constraints (Settled)

| File         | Location | Why                                                    |
| ------------ | -------- | ------------------------------------------------------ |
| AGENTS.md    | Root     | AI agent discoverability (Claude Code loads from root) |
| CLAUDE.md    | Root     | Claude Code requires root placement                    |
| GEMINI.md    | Root     | Gemini requires root placement                         |
| README.md    | Root     | Universal convention, GitHub displays first            |
| CHANGELOG.md | Root     | Industry standard, changelog tools expect root         |

Documented in AGENTS.md under "File Organization Rules".

---

## Target Structure (After All Actions)

```sh
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
- [x] Verify @reference chain works: CLAUDE.md → AGENTS.md → docs/core/\* (ALL PASS)
- [x] Delete redundant files:
  - `docs/research-repo-organization.md` (deleted)
  - `~/omar/knowledge/research/development/repo-organization/contracts-directory-decision.md` (deleted)

### Governance Items — APPROVED (Full Governance, adapted for AI agents — 8.85/10)

All governance items approved 2026-02-16. Implementation tracking via /repo-bootstrap skill.

- [x] Add `LICENSE` at root (proprietary, protect IP)
- [x] Update `README.md` content (project overview + quick-start + links to docs/core/)
- [x] Create `.github/` directory (PR template, issue template for Linear integration, CODEOWNERS)
- [x] Add `CONTRIBUTING.md` at root — migrate workflow ("SCOUT, REPORT, QUESTIONS, ACTION") from AGENTS.md here. AGENTS.md references @CONTRIBUTING.md (DRY fix)
- [x] Add `CODE_OF_CONDUCT.md` at root — adapted for AI agents (behavioral boundaries, data ethics, decision constraints)
- [x] Add `SECURITY.md` at root — agent security policies (data access rules, secret handling, vulnerability reporting)
- [x] Update `AGENTS.md` — replace Mandatory Workflow section with @CONTRIBUTING.md reference, update File Organization Rules with new root files
- [x] Update `docs/core/STRUCTURE.md` — add new governance files to layout
- [x] Verify root file count stays under 15

Full analysis: `~/omar/knowledge/research/development/repo-organization/governance-items-decision.md`

---

## repo-bootstrap Skill Decisions

Decisions (all approved 2026-02-16):

| #   | Decision                    | Choice                                     | Notes                                                                           |
| --- | --------------------------- | ------------------------------------------ | ------------------------------------------------------------------------------- |
| M   | Villa Thaifa approach       | Incremental fix                            | Score 7.8/10. Archive /context/, tidy structure, add governance, merge to main. |
| 1   | Template engine             | Copier                                     | External tool with Jinja2, YAML config, template lifecycle management.          |
| 2   | Workflow in CONTRIBUTING.md | Preset-specific                            | SCOUT/REPORT for ops, Fork/Branch for library, etc.                             |
| 3   | Git/GitHub init             | Ask-first                                  | Skill asks before git init and GitHub creation.                                 |
| 4   | Governance templates        | Human-standard (with AI adaptation TBD)    | Standard open-source format. Pending /decide on whether to adapt for AI agents. |
| 5   | Skill name                  | /repo-bootstrap                            | Clearest combination of scope + intent.                                         |
| 6   | Implementation              | Skill-only (+ GitHub Template Repos later) | Claude Code skill first. GitHub template repos as future enhancement.           |

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

---

## Follow-up Items (from decisions)

- [ ] /decide: Should governance templates (CODE_OF_CONDUCT, SECURITY) be adapted for AI agents or stay human-standard?
- [ ] Create GitHub Template Repo(s) — not one template but multiple per project type. Skill templates should reference these repos.
- [ ] Update skill if/when GitHub template repos are created (templates may point to repo templates)
- [ ] Test skill-suggester.py via `claude -p` to verify auto-suggestions work

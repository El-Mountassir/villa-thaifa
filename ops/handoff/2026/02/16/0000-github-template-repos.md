# Handoff: Create GitHub Template Repo(s) for repo-bootstrap

## Status

**Pending.** Planned as future enhancement after skill-only implementation works.

---

## Context

### What is repo-bootstrap?

The `/repo-bootstrap` skill scaffolds new repositories with:
- Complete directory structure (governance, data, operational patterns)
- AI agent contracts (CLAUDE.md, AGENTS.md, GEMINI.md)
- Project governance files
- Foundational documentation

### Current Implementation

Skill-only approach: Templates are embedded in the skill itself. Omar explicitly wants this as a *first step* only.

### Next Step: GitHub Template Repos

Omar's decision (Feb 2026):
> "on devra créer les GitHub Template Repo (car comme t'avais dis précédemment, un seul template n'est pas la bonne chose à faire. et cela nous permettra aussi de faire évoluer tout cela! Bien sur, une fois qu'on aura fait cela, on devra s'assurer que notre skill soit mis à jour si besoin. Cela dit, je me demande si les templates dans le skill ne devront pas pointer sur le(s) github template repo qu'on créera ou pas? Idéalement pour nous bien sur!"

**Translation**: We must create GitHub Template Repos (because one template isn't the right approach). This allows us to evolve the templates continuously. After that, we need to ensure the skill is updated if needed. The question: should the skill's templates point to the GitHub template repos?

---

## Template Repos to Create

**One repo per project type** (matching skill presets).

### 1. omar/template-ops

**Purpose**: Operational systems (pattern: villa-thaifa)

**Structure**:
```
template-ops/
├── data/          canonical source-of-truth
├── docs/          operational docs, configs
├── ops/           status dashboards, logs
├── scripts/       validation utilities
├── tests/         pytest suite
├── logs/          operation logs (archive)
├── .github/       PR templates, issue templates, workflows
├── CLAUDE.md      AI partner contract
├── AGENTS.md      Agent workflow and policies
├── GEMINI.md      Gemini integration (if applicable)
├── README.md      Quick start
└── LICENSE
```

**Pre-populated files**:
- `.github/PULL_REQUEST_TEMPLATE.md` — Standard PR guidance
- `.github/ISSUE_TEMPLATE/bug.md` — Bug report structure
- `.github/workflows/tests.yml` — CI/CD baseline
- `CLAUDE.md` — Template with mission/structure references
- `AGENTS.md` — Workflow and policy skeleton
- `README.md` — Setup instructions
- `data/README.md` — Data governance notes

---

### 2. omar/template-library

**Purpose**: Reusable Python libraries

**Structure**:
```
template-library/
├── src/           package source code
├── tests/         pytest suite
├── docs/          API docs, guides
├── .github/       PR templates, workflows
├── CLAUDE.md      AI contract
├── pyproject.toml package config (uv)
├── README.md      Library overview
└── LICENSE
```

**Pre-populated files**:
- `pyproject.toml` — uv-based Python setup
- `.github/workflows/tests.yml` — Run tests on push
- `src/__init__.py` — Package structure
- `tests/test_*.py` — Test example
- `docs/API.md` — API documentation template

---

### 3. omar/template-app

**Purpose**: Deployable applications (web, CLI, services)

**Structure**:
```
template-app/
├── src/           application source
├── tests/         test suite
├── docs/          user guides, architecture
├── config/        environment configs
├── .github/       PR templates, workflows, deployment actions
├── CLAUDE.md      AI contract
├── README.md      Setup and deployment
└── LICENSE
```

**Pre-populated files**:
- `config/defaults.yaml` — Configuration template
- `.github/workflows/tests.yml` — Test automation
- `.github/workflows/deploy.yml` — Deployment skeleton
- `docs/ARCHITECTURE.md` — Design notes template
- `README.md` — Development and production setup

---

### 4. omar/template-monorepo

**Purpose**: Multi-project workspaces

**Structure**:
```
template-monorepo/
├── apps/          application projects
├── packages/      shared libraries
├── docs/          workspace docs
├── .github/       org-wide templates, workflows
├── CLAUDE.md      workspace AI contract
├── AGENTS.md      shared policies
├── README.md      repo orientation
└── LICENSE
```

**Pre-populated files**:
- `.github/PULL_REQUEST_TEMPLATE.md` — Cross-project PR guidance
- `docs/WORKSPACE.md` — Project discovery and setup
- `CLAUDE.md` — Shared AI contract (references per-project overrides)
- `README.md` — Which project is which

---

## Critical Design Question

**Should the /repo-bootstrap skill's local templates POINT TO the GitHub template repos, or remain independent?**

### Option A: Skill Pulls Templates from GitHub Repos
- **How**: Skill downloads template zips from GitHub repos, extracts, customizes
- **Pros**: Single source of truth. Templates evolve in one place. DRY.
- **Cons**: Requires network access. Slower. Complex error handling.
- **Best for**: Stable template ecosystem with shared governance

### Option B: Skill Has Independent Templates, GitHub Repos Are Separate
- **How**: Templates live in the skill. GitHub repos are manually synced versions.
- **Pros**: Works offline. Fast. Skill is self-contained.
- **Cons**: Two sources to maintain. Risk of divergence.
- **Best for**: Simple initial implementation

### Option C: GitHub Repos ARE the Templates, Skill Just Runs `gh repo create --template`
- **How**: User runs: `gh repo create --template omar/template-ops my-repo`
- **Pros**: Simplest. GitHub handles cloning. No skill complexity.
- **Cons**: No local customization. User must use GitHub CLI. Less integration.
- **Best for**: Users already in GitHub workflow

**Recommendation**: Start with **Option A** for long-term maintainability. Omar can evolve templates without touching skill code.

---

## Key Reference Files

Read these to understand the design decisions:

1. **Scaffolding Research**
   - Path: `~/omar/knowledge/research/development/repo-bootstrap/scaffolding-research.md`
   - Contains: Best practices, template standards, GitHub features analysis

2. **Skill Design**
   - Path: `~/omar/knowledge/research/development/repo-bootstrap/skill-design.md`
   - Contains: Current skill structure, preset mapping, customization flow

3. **Repo Organization Decision**
   - Path: `/home/director/villa-thaifa/docs/repo-organization-decision.md`
   - Contains: Why multiple templates needed, governance patterns

4. **Governance Items Decision**
   - Path: `~/omar/knowledge/research/development/repo-organization/governance-items-decision.md`
   - Contains: What belongs in each template type

---

## Instructions for Next Session

Follow this sequence:

### 1. SCOUT
- Read all reference files above
- Verify GitHub CLI is available: `gh auth status`
- Confirm Omar's GitHub account access

### 2. REPORT
- Summarize current state of scaffolding research
- Note any changes to template specifications since this handoff was written

### 3. QUESTIONS
- Ask Omar which option (A/B/C) for skill-template relationship
- Confirm template repo ownership (all under `omar/`?)
- Verify deployment/visibility requirements (private vs public)

### 4. ACTION
- Create first template repo: `omar/template-ops` as pilot
- Add all pre-populated files listed above
- Write README with setup instructions
- Test: Create a new repo from template using `gh repo create --template`
- Verify cloned repo has correct structure and files
- Document any friction points

### 5. ITERATE
- Create remaining templates (library, app, monorepo)
- Update `/repo-bootstrap` skill to reference GitHub repos if decision warrants
- Test skill with new GitHub template repos
- Document template maintenance workflow

---

## Constraints & Notes

- **Language**: All files in English
- **Tools**: GitHub CLI (`gh`) required. Verify with `gh auth status`
- **Ownership**: Confirm repo namespace (assuming `omar/`)
- **Delegation**: Hard rule — delegate complex research to Gemini agent
- **Output routing**: Complex output (analysis, recommendations) → HTML dashboard or file. Simple status → chat.
- **Verification**: After creating templates, test by cloning one and verifying structure
- **Sync**: After template repos are live, sync this repo and the skill repo

---

## Related Work

- **Skill implementation**: `/home/director/.claude/agents/repo-bootstrap/` (if skill file exists)
- **Villa-thaifa pattern** (ops template source): `/home/director/villa-thaifa/` (reference for structure)
- **GitHub template docs**: https://docs.github.com/en/repositories/creating-and-managing-repositories/creating-a-template-repository

---

## Success Criteria

Template repo work is DONE when:

1. Four template repos exist under `omar/` (ops, library, app, monorepo)
2. Each template has complete pre-populated files per spec above
3. README for each template explains its purpose and when to use it
4. Test: Create a new repo from `omar/template-ops`, verify structure matches expected
5. Skill integration decision is documented (A/B/C choice)
6. Skill code is updated if decision requires it (Option A)
7. Both this repo and skill repo are pushed to GitHub

---

_Handoff written: 2026-02-16_
_Next action: Read reference files and scout current state_

# Dual Archive Audit — 2026-03-25

**Scope**: `/home/director/villa-thaifa/`
**Auditor**: Nova (Workspace Architect)
**Status**: PROPOSED — awaiting Omar decision

---

## 1. Executive Summary

Three archive locations coexist in this repo (excluding worktree mirrors):

| Path | Files | Character |
|---|---|---|
| `archive/` | 30 files, 9 dirs | Repo-level graveyard: legacy artifacts, migration scraps, structural superseded files |
| `ops/archive/` | 320 files, 28 dirs | Massive: planning history, audit history, data specs, missions, reports, sessions, status snapshots |
| `ops/audit/archive/` | ~31 files, 3 dirs | Superseded audit artifacts only |

AGENTS.md says one rule, one location: `Fully archived? --> archive/`. It also says `ops/` holds operational artifacts. The conflict is real — `ops/archive/` is simultaneously valid (it contains archived *operational* artifacts) and ambiguous (nothing distinguishes it from `archive/` for a decision-making agent).

Additionally, a worktree at `.claude/worktrees/swift-elm-b44a/` mirrors both problems AND introduces `archives/` (plural) — a direct naming convention violation.

---

## 2. What Is In Each Location

### `archive/` (root level) — 30 files

Content character: structural superseded files, migration artefacts, legacy strategy docs, pre-migration booking backups.

Key sub-directories:
- `2026/Q1/booking-merge-backup/` — 13 room profile backups + registry (pre-merge state)
- `legacy/2025/` — strategy + workflow docs from 2025 era
- `legacy/exports/` — 3 zip exports of legacy state
- Root-level flat files — superseded context files (context-meta-architecture-tech_stack.md, docs-client-admin.md, etc.)

Semantic: **structural and cross-domain legacy**. Files that belonged to no single `ops/` subdomain.

---

### `ops/archive/` (operational archive) — 320 files

Content character: **everything that ever lived in `ops/`** — planning, audits, data specs, missions, reports, sessions, status snapshots.

Key sub-directories:

| Sub-dir | Content | Count |
|---|---|---|
| `planning/` | 80+ historical plan files, ROADMAPs, TODOs, structure proposals | ~85 files |
| `audit-quality/` | Superseded audit reports (duplicates `reports/` partially) | ~56 files |
| `reports/` | Structured report archive with sub-groupings | ~35 files |
| `data-specs/` | Superseded room specs, channel mappings, platform rules | ~33 files |
| `knowledge/` | Historical knowledge capture, onboarding prompts, baselines | ~33 files |
| `status/` | Old status snapshots, MASTER_STATE, INDEX, archived.md, etc. | ~35 files |
| `missions/` | Archive-within-archive: `missions/archive/` and `missions/drafts/` | ~8 files |
| `sessions/` | Session capture artifacts | 3 files |
| `changelogs/` | Superseded changelogs | 2 files |
| `data-specs-images-*/` | Empty image config directory | 0 files |
| `promotions.md` | Loose superseded promotions file | 1 file |

Semantic: **operational history dump**. This is where old `ops/` content goes to die. It has grown to 10x the size of `archive/`.

---

### `ops/audit/archive/` — 31 files

Content character: superseded audit artifacts specifically. Scoped to the `audit/` domain.

Sub-directories:
- `history/` — historical audit transcripts, changelogs, session notes from Jan 2026

Semantic: **audit-domain archive**. Correct by Separation of Concerns — audit files archive within their domain directory.

---

## 3. Analysis: Is the Ambiguity Structural or Definitional?

### The core problem

AGENTS.md decision tree routes ALL archived content to `archive/`. But `ops/archive/` also exists and is actively used. An agent following the routing table exactly would never put anything in `ops/archive/` — yet 320 files are there.

This creates two failure modes:

1. **Agent indeterminism**: Agent asks "where does this archived operational artifact go?" AGENTS.md says `archive/`. But `ops/archive/` exists and is full of similar content. No tiebreaker.
2. **Scope confusion**: `ops/archive/` functions as a catch-all for ALL operational history, not just formally archived operational artifacts. It includes loose planning docs, drafts, and abandoned ideas that never had a clear lifecycle.

### The `ops/audit/archive/` pattern

This is actually correct. It follows the principle: a domain's own archive lives within that domain. `ops/audit/` is a domain → `ops/audit/archive/` is its archive. This is Separation of Concerns applied consistently.

The question is: should this pattern extend to ALL `ops/` sub-domains? If yes, then `ops/archive/` (a catch-all) violates it.

### The worktree violation

`.claude/worktrees/swift-elm-b44a/archives/` (plural) directly violates: "Archive convention: Always `archive/` (singular). Never `archives/`." The worktree appears to be an active worktree (branch `worktree-swift-elm-b44a`). This is secondary to the main audit but must be noted.

---

## 4. Options

---

### Option A — Merge `ops/archive/` into `archive/ops/`

**What changes**: All 320 files in `ops/archive/` move to `archive/ops/`. Single canonical archive at root level.

**Pros**:
- Perfect alignment with AGENTS.md routing rule (`archive/` for everything)
- Zero ambiguity — one archive, one path
- Agents always know where to go
- Eliminates the dual-location problem permanently

**Cons**:
- `archive/ops/` becomes massive (320+ files) — navigability degrades
- Loses the operational-domain grouping that `ops/archive/` preserves
- Migration effort: 320 files + all references to `ops/archive/` in docs, INDEX files, etc.
- `ops/audit/archive/` and `ops/archive/missions/archive/` create nested inconsistency (some domain archives stay in `ops/`, others move)

**Migration effort**: HIGH — ~320 files, grep-and-update across all reference files.

**Determinism score**: 9/10 — agents follow one rule, one location. The remaining 1 point lost because "operational artifacts" is still a judgment call at archival time.

---

### Option B — Keep both, clarify scope in AGENTS.md

**What changes**: AGENTS.md gets an explicit two-tier archive rule:
- `archive/` = structural, cross-domain, or non-operational legacy
- `ops/archive/` = superseded operational artifacts (plans, reports, audits, data specs)

**Pros**:
- Zero migration cost
- Preserves existing operational grouping
- `ops/audit/archive/` pattern remains consistent with `ops/archive/`
- Better Separation of Concerns: operational history stays with operational domain

**Cons**:
- Two-tier rule introduces ambiguity at the boundary ("is this operational or cross-domain?")
- Determinism is lower — agent must make a judgment call at archival time
- Current `archive/` content is not fully consistent with "structural/cross-domain" — some files there are operational
- Doesn't resolve the naming inconsistency: `ops/archive/` has no sub-domain structure, just a massive flat/shallow dump

**Migration effort**: LOW — only AGENTS.md update, no file moves.

**Determinism score**: 6/10 — "operational vs structural" is ambiguous for many edge cases (e.g., where does an archived handoff go?).

---

### Option C — Domain-scoped archives (recommended)

**What changes**: Establish a consistent pattern across ALL `ops/` sub-domains: each domain owns its archive. Consolidate `ops/archive/` content by routing each file to its owning domain's `archive/` sub-directory. Reserve `archive/` (root) for content with no `ops/` domain affiliation.

**Pattern**:
```
ops/handoff/archive/      (already: ops/handoff/{YYYY}/{MM}/{DD}/ = de facto archive)
ops/audit/archive/        (already exists — correct)
ops/decisions/archive/    (create if needed)
ops/status/archive/       (create for superseded status snapshots)
archive/                  (root: non-ops legacy, structural, cross-domain)
```

Content currently in `ops/archive/` routes as:
- `planning/` → `archive/` (planning is pre-`ops/` era, cross-domain)
- `audit-quality/`, `reports/` → `ops/audit/archive/history/`
- `data-specs/` → `archive/` (pre-data/ era, structural)
- `knowledge/` → `archive/` (pre-domain era, cross-domain)
- `status/` → `ops/status/archive/` (new)
- `missions/` → already inside `ops/archive/missions/` → dissolve into `ops/` domain when missions domain is formalized
- `changelogs/` → `archive/` (repo-level)
- `sessions/` → `ops/handoff/archive/` or `archive/` depending on content

**Pros**:
- Highest determinism: each domain owns its lifecycle (same as `ops/audit/archive/` model)
- Scalable: adding a new `ops/` sub-domain automatically includes its archive pattern
- Eliminates `ops/archive/` catch-all which is the root of the ambiguity
- Clean separation: `archive/` at root = truly cross-domain or pre-ops era content only
- Consistent with Separation of Concerns rule

**Cons**:
- Highest migration effort: 320 files need routing decisions per file, not bulk move
- Requires judgment per sub-directory in `ops/archive/` (some ambiguous)
- Creates multiple new `archive/` sub-directories in `ops/` — slightly more to navigate
- Some `ops/archive/` content has no clear domain (historical planning docs from era before current structure)

**Migration effort**: HIGH (but can be phased — dissolve `ops/archive/` incrementally, one sub-directory at a time).

**Determinism score**: 8.5/10 — domain ownership is clear for new content. Historical content routing still requires judgment once during migration, then determinism is high thereafter.

---

## 5. Recommendation

**Adopt Option C (domain-scoped archives) as the target state, with Option B as the immediate bridge.**

### Rationale

Option A (merge into `archive/ops/`) trades one ambiguity for another: it makes `archive/` canonical but creates a 350-file mass that violates navigability. The operational content at `ops/archive/` has natural domain groupings — destroying them to force a single-location rule is a net loss.

Option B (clarify AGENTS.md) is safe but leaves the determinism gap open permanently. Agents will keep making judgment calls at "structural vs operational" boundaries.

Option C matches how `ops/audit/archive/` already works — it just extends the pattern consistently. The migration is high-effort but phases cleanly: each `ops/archive/` sub-directory can be dissolved one at a time over multiple sessions.

### Immediate action (low-risk, high-value)

1. **Update AGENTS.md** with explicit two-tier rule (Option B bridge) — stops new content from landing in wrong location NOW
2. **Dissolve `ops/archive/planning/`** — largest sub-directory (85+ files), cleanest routing: all pre-ops planning → `archive/` (cross-domain legacy)
3. **Create `ops/status/archive/`** — migrate `ops/archive/status/` there (clear domain ownership)

### AGENTS.md update (proposed wording)

```
**Archive locations**:
- `archive/` (root) — cross-domain legacy, structural superseded, pre-2026 content with no ops/ domain affiliation
- `ops/{domain}/archive/` — superseded operational artifacts, scoped to owning domain (e.g., ops/audit/archive/, ops/status/archive/)
- `ops/archive/` — DEPRECATED. Do not add new content here. Dissolve incrementally.
```

---

## 6. Additional Findings

### `ops/archive/missions/archive/` — nested archive

A nested `archive/` inside `ops/archive/missions/`. This is an archive-within-archive pattern — unavoidable consequence of the unstructured `ops/archive/` catch-all. Dissolves under Option C.

### `ops/audit/archive/` — correct

This pattern is the MODEL to replicate. No action needed.

### Worktree violation: `.claude/worktrees/swift-elm-b44a/archives/` (plural)

Direct naming convention violation. The worktree mirrors the repo structure but introduced `archives/` (plural). This is in an active worktree branch (`worktree-swift-elm-b44a`). Recommend: confirm worktree status with Omar before touching; if stale, delete via `git worktree remove`.

### `data-specs-images-2026-02-21/configs/hotel/images/` — empty directory in ops/archive/

An entirely empty directory tree (0 files). No value. Can be removed once `ops/archive/` dissolution begins.

---

## 7. Decision Required From Omar

One decision needed: **which option to adopt** (A, B, or C).

If Option C (recommended): also confirm whether to phase the `ops/archive/planning/` dissolution first, or tackle `ops/archive/` sub-directory by sub-directory in a dedicated session.

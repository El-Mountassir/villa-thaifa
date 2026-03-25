# Evaluation: Villa Thaifa Repository Structure

> **Date**: 2026-03-24
> **Type**: Repository Structure / Architecture
> **Evaluator**: Auditor Agent

## Global Score: 5.1 / 10

**Verdict**: A repo with a thoughtful governance spec betrayed at every turn by ghost directories, dual archive systems, image naming anarchy, stale documentation, and a `tmp/` junk drawer committed into version control.

---

## Scores by Dimension

| Dimension | Score | Evidence |
|-----------|-------|----------|
| **Clarity** | 5/10 | Top-level directories are legible (`data/`, `ops/`, `project/`) but `infra/`, `src/`, `logs/`, and `tmp/` are empty or contain session debris with zero operational value. A new agent cannot trust the tree because ghost directories contaminate the signal. |
| **Completeness** | 6/10 | Core domains covered (rooms, bookings, finance, property). Missing: `data/pending-domains/` referenced in AGENTS.md decision tree and `data/README.md` does not exist in the same state as described. `.agents/` exists but workflows are not enumerated in any index. |
| **Correctness** | 4/10 | Multiple files violate the AGENTS.md placement decision tree: `data/platforms/` (research docs belong in `context/` or `ops/audit/`), `ops/planning/` (undocumented directory not in decision tree), `docs/tmp/` (a tmp directory inside docs is incoherent), `logs/` at root (not mentioned anywhere in governance). The `tmp/` directory at root is committed to git — a structural violation of every "session artifacts belong in /tmp" rule in the system. |
| **Actionability** | 6/10 | `ops/status/truth.md` and `data/rooms/` are well-structured and agent-navigable. `ops/handoff/INDEX.md` has 3 "active" entries for what should be 1. The AGENTS.md decision tree is clear but the actual layout contradicts it on 6+ points, making the tree misleading rather than helpful. |
| **Value** | 6/10 | Room data (R01-R12 with `profile.md` + `images/`) is genuinely canonical and colocated. `data/finance/rates.json` as locked source of truth is correct. `ops/status/truth.md` is well-maintained. These are real value. But 1.8 GB total size with massive image naming chaos and ~276 images using 3 redundant naming schemes dilutes that value severely. |

---

## Structure-Specific Scores

| Criterion | Score | Evidence |
|-----------|-------|----------|
| **DRY** | 4/10 | Two archive systems coexist: `archive/` at root and `ops/archive/`. `PRINCIPLES.md` references `archives/YYYY/QQ/` (plural, wrong path) while `AGENTS.md` mandates `archive/` (singular). Six cross-duplicate image files confirmed between R09 and R10 (`16c97eec`, `2839f125`, `353c9e76`, `9cc5df3b`, `main.jpg`, `photo-07.jpg`). `data/README.md` references `pending-domains/` and `status/` subdirectories that do not exist under `data/`. |
| **Naming** | 4/10 | Image naming has 4 concurrent schemes across all rooms with no declared winner. R12 has zero `r12-XX` canonical images. Archive root has flat files named with path-encoded names (`context-meta-architecture-tech_stack.md`) — lazy archival archaeology baked into filenames. `ops/intake/linear-issues-agents-md-gaps.md` sits outside the `processed/`/`unprocessed/` subdirectory structure it governs. |
| **Depth** | 6/10 | `data/rooms/RXX/images/` is correct colocated depth. `context/meta/{architecture,planning,knowledge,templates}/` is appropriate. The opposite problem: `ops/archive/` has 12 subdirectories with opaque names (`audit-quality`, `data-specs-images-2026-02-21`) that have no index and cannot be navigated without reading every file. |
| **Separation** | 5/10 | `data/platforms/` blurs data vs research: `hotelrunner-platform-research.md` is a research document not structured domain data. `ops/planning/` is undocumented and sits between ops and data semantics. `docs/tmp/Api.md` mixes reference documentation with a temp pattern. `docs/security/` contains a single policy document that belongs in `context/meta/`. |
| **Scalability** | 5/10 | The per-room `RXX/` pattern scales correctly. The `ops/decisions/` date-prefixed files scale correctly. But `logs/` grows unboundedly (currently 19MB) with no rotation policy. Image directories already have 4 competing naming schemes with no resolution path. `archive/` root will accumulate flat files indefinitely. |

---

## Tree Output (Annotated)

```
/home/director/villa-thaifa                       [1,117 files | 154 dirs | 1.8 GB]
├── archive/                                       [ROOT ARCHIVE — 6 loose flat files at root]
│   ├── 2026/Q1/                                   [EMPTY — 83 days into Q1, nothing archived here]
│   └── legacy/
│       ├── 2025/
│       └── exports/
├── context/meta/
│   ├── architecture/                              [6 files — valid]
│   ├── knowledge/                                 [3 files]
│   ├── planning/                                  [4 files]
│   └── templates/                                 [9 template files — valid]
├── data/
│   ├── admin/
│   ├── bookings/
│   ├── finance/
│   ├── operations/
│   ├── platforms/                                 [6 RESEARCH MD FILES — MISPLACED]
│   ├── property/
│   ├── rooms/                                     [R01-R12/, 4 canonical md files]
│   └── README.md                                  [STALE — references non-existent subdirs]
├── docs/
│   ├── client/
│   ├── security/                                  [.env-credentials-policy.md — wrong location]
│   ├── tmp/                                       [Api.md — junk drawer inside docs/]
│   └── workflows/
├── infra/
│   ├── docker/                                    [EMPTY — .gitkeep only]
│   └── envs/dev,prod,staging/                     [ALL EMPTY — .gitkeep only]
├── logs/                                          [19MB+ session logs COMMITTED TO GIT]
├── ops/
│   ├── archive/                                   [12 subdirs — COMPETING with root archive/]
│   ├── audit/                                     [15 files + archive/, incidents/, quality/]
│   ├── decisions/                                 [16 date-prefixed decision files — valid]
│   ├── handoff/active/                            [1 file vs 3 "active" in INDEX]
│   ├── intake/                                    [file sitting OUTSIDE processed/unprocessed]
│   ├── planning/                                  [UNDOCUMENTED DIR — not in decision tree]
│   └── status/                                    [truth.md, work-overview.md — valid]
├── project/                                       [valid constitution files]
├── scripts/                                       [valid tooling]
├── src/
│   ├── apps/api,automation,dashboard/             [ALL EMPTY — .gitkeep only]
│   ├── packages/                                  [EMPTY]
│   └── tools/                                     [EMPTY]
│   └── CLAUDE.md                                  [orphaned — governs non-existent app]
├── tests/                                         [1 test file]
├── tmp/                                           [17 FILES COMMITTED TO GIT — session debris]
├── AGENTS.md, CLAUDE.md, GEMINI.md, README.md, CHANGELOG.md  [valid root files]
├── Makefile, cliff.toml, pyproject.toml, uv.lock             [valid tooling]
└── villa-thaifa.code-workspace                               [IDE file at root — minor]

STRUCTURE.md claims: 637 files | 89 dirs | Last Updated 2026-02-19
Actual: 1,117 files | 154 dirs | 2026-03-24
Drift: +480 files, +65 directories, 34 days stale
```

---

## Ruthless Diagnostics

### Critical Failures

**1. `tmp/` directory committed to version control**
- Path: `/home/director/villa-thaifa/tmp/`
- 17 files: agentic loop reviews, audit prompts, triage JSONs, workflow research — all session debris.
- The global rules explicitly mandate session artifacts go to `/tmp/` (system temp). A committed `tmp/` directory in the repo is the exact anti-pattern the rule exists to prevent.
- This content has zero operational value and consumes agent context when the tree is scanned.

**2. `logs/` directory committed to version control**
- Path: `/home/director/villa-thaifa/logs/`
- `chat.json` (15.7 MB), `subagent_stop.json` (2.8 MB), `stop.json` (528 KB), `subagent_debug.log` (125 KB).
- Total: ~19 MB of machine-generated session telemetry in git with no `.gitignore` and no rotation policy.
- `chat.json` almost certainly contains PII (guest names, booking details, WhatsApp conversations) — a data governance violation.

**3. Dual archive system with no arbitration**
- `archive/` at repo root: AGENTS.md says "fully archived content".
- `ops/archive/` nested: 12 subdirectories of operational artifacts.
- These are two competing archive destinations. No document defines the routing rule that distinguishes them.
- `PRINCIPLES.md` line 3 compounds the damage by referencing `archives/YYYY/QQ/` (plural, wrong name, wrong path entirely — the convention is `archive/` singular).
- Agents cannot determine where to archive without guessing.

**4. `src/` and `infra/` are entirely phantom**
- Every directory under `src/` and `infra/` contains only `.gitkeep`. Zero actual files.
- `src/CLAUDE.md` governs code that does not exist.
- 9+ directories: `src/apps/api/`, `src/apps/automation/`, `src/apps/dashboard/`, `src/packages/`, `src/tools/`, `infra/docker/`, `infra/envs/dev/`, `infra/envs/prod/`, `infra/envs/staging/`.
- These are aspirational scaffolding for an unbuilt app. They pollute every `tree` output, every agent scan, every structure card. Pure noise masquerading as signal.

**5. `STRUCTURE.md` is 34 days stale and 43% wrong**
- Claims: 637 files, 89 directories. Actual: 1,117 files, 154 directories.
- `make structure-update` is a mandatory post-change hook per AGENTS.md. It has not been run for over a month.
- Any agent reading STRUCTURE.md will operate on a fundamentally incorrect map of the repository.

### Misplaced Files

| File/Directory | Current Location | Correct Location per AGENTS.md | Violation |
|---|---|---|---|
| `hotelrunner-platform-research.md` | `data/platforms/` | `context/meta/knowledge/` or `ops/audit/` | Research doc placed in data/ (not structured domain data) |
| `expedia-*.md` (5 files) | `data/platforms/` | `ops/audit/` or `context/meta/knowledge/` | Research/extraction reports, not canonical structured data |
| `2026-02-26-booking-elisabeth.md` | `ops/planning/` | `data/bookings/requests/` or `ops/intake/` | `planning/` not in AGENTS.md decision tree |
| `docs/tmp/Api.md` | `docs/tmp/` | `.agents/hotelrunner/api-channel-codes.md` | "tmp" inside docs is incoherent; content is reference API channel list |
| `docs/security/.env-credentials-policy.md` | `docs/security/` | `context/meta/architecture/` | Policy/architecture document, not operational docs |
| `archive/*.md` (6 flat files) | `archive/` root | `archive/legacy/` dated subdir | Flat files with path-encoded names at archive root |
| `ops/intake/linear-issues-agents-md-gaps.md` | `ops/intake/` (root level) | `ops/intake/unprocessed/` | Bypasses the processed/unprocessed structure the directory provides |
| `data/operations/whatsapp/messages.db` | `data/operations/whatsapp/` | Excluded from git entirely | SQLite DB with likely PII committed to version control |
| `data/operations/whatsapp/whatsapp.db` | same | same | Same violation |

### Orphaned / Stale Content

| Item | Problem |
|---|---|
| `tmp/` (17 files, ~280KB) | Session debris from 2026-02-25. Should never have been committed. |
| `logs/` (6 files, 19MB) | Machine telemetry committed to git. Grows without bound. |
| `ops/planning/` | Entire directory undocumented in AGENTS.md. Created for one booking file. |
| `data/platforms/` | Entire directory undocumented in AGENTS.md decision tree. |
| `src/` + `infra/` (9 empty dirs) | Aspirational scaffolding for unbuilt app. Dead weight in every scan. |
| `archive/2026/Q1/` | Empty directory. 83 days into Q1 2026, nothing has been placed here. |
| `ops/handoff/INDEX.md` | Lists 3 "active" entries; only 1 handoff file exists in `active/`. The entry for `0154-linear-mcp-global-audit` points to both `ops/handoff/active/` AND `ops/handoff/2026/02/26/` simultaneously — self-contradictory. The 0227 entry is untracked per git status and missing from INDEX. |
| `data/README.md` | References `pending-domains/` and `status/` as `data/` subdirectories. Neither exists. |
| `project/STRUCTURE.md` | 34 days stale. +480 files, +65 directories drift. Every stat is wrong. |
| `ops/intake/linear-issues-agents-md-gaps.md` | Created 2026-02-21, status "PENDING CREATION — MCP not connected." Unprocessed for 31 days. |

### Naming Issues

**Image naming anarchy — 4 concurrent schemes with no declared canonical standard:**

| Scheme | Count | Status |
|--------|-------|--------|
| `rXX-NN.jpg` | 107 | Correct — canonical, room-scoped |
| `photo-NN.jpg` | 107 | Wrong — generic sequential with no room prefix; R05 starts at photo-09, creating false sense of global sequence |
| `_DSC7xxx-HDR.jpg` | 107 | Wrong — raw photographer filenames, no room context |
| `WhatsApp Image YYYY-MM-DD at HH.MM.SS (N).jpeg` | 55 | Wrong — raw imports with spaces and timestamps |

R12 has zero `r12-XX` canonical images: only UUIDs (10 files) and `photo-XX` (9 files). The canonical scheme was never applied to R12.

**Six R09/R10 cross-duplicate images** (survived the "53 duplicate removal" effort):
`16c97eec-db21-4e5e-be2d-2b05ac313f03.jpeg`, `2839f125-782d-4bc3-8be6-e49137b62603.jpeg`, `353c9e76-ce9d-4d6f-8c85-8ad0f68ef0b6.jpeg`, `9cc5df3b-fb13-48ee-893e-5b5cfb910e2d.jpeg`, `main.jpg`, `photo-07.jpg`

**`PRINCIPLES.md` line 3 naming conflict:**
States `archives/YYYY/QQ/` (plural). AGENTS.md explicitly mandates `archive/` (singular, "Never `archives/`"). The governing document contradicts the rule that governs naming.

**Archive root flat-file names:**
`context-meta-architecture-tech_stack.md`, `docs-client-admin.md`, `migration-conflict-check.md` — path-encoded filenames instead of proper subdirectory placement. Future agents must decode the filename to understand provenance.

### Missing Elements

| Missing | Why It Matters |
|---|---|
| `.gitignore` entries for `logs/`, `tmp/`, `*.db`, `data/finance/*.pdf` | Currently committing 19MB+ logs, SQLite DBs with guest data, and the tourism tax declaration PDF |
| `data/pending-domains/` directory | Referenced in AGENTS.md decision tree and `data/README.md`; does not exist |
| Image naming convention document | 4 schemes active, no declared winner, no migration plan |
| Archive routing decision | Two archive locations, zero arbitration document |
| `ops/planning/` in AGENTS.md decision tree | Either document it or eliminate it |
| R12 canonical `r12-XX` images | Only room without canonical-scheme images |
| Handoff INDEX.md 0227 entry | File exists in `ops/handoff/active/`, not in INDEX.md |

---

## Path to Excellence

### To reach 6/10 (Minimum Viable Clean)

1. Add `logs/`, `tmp/`, `*.db`, `data/finance/*.pdf` to `.gitignore`. Remove from git tracking.
2. Move committed `tmp/` contents to `ops/archive/2026-02/session-debris/`. Remove `tmp/` from git.
3. Run `make structure-update` to sync `project/STRUCTURE.md` with reality (34 days stale).
4. Fix `PRINCIPLES.md` line 3: `archives/` → `archive/` (critical naming conflict with AGENTS.md mandate).
5. Delete `src/` and `infra/` entirely. If app development begins, restore then.

### To reach 8/10 (Operationally Sound)

6. Move all 6 files in `data/platforms/` to `ops/audit/platform-research/`. Delete `data/platforms/`.
7. Resolve `ops/planning/`: add to AGENTS.md decision tree, or move its file and remove the directory.
8. Move `docs/tmp/Api.md` to `.agents/hotelrunner/api-channel-codes.md`.
9. Move `docs/security/.env-credentials-policy.md` to `context/meta/architecture/`.
10. Fix `data/README.md`: remove references to `pending-domains/` and `status/` that do not exist.
11. Fix `ops/handoff/INDEX.md`: reconcile 3 "active" entries to 1, add 0227 missing entry.
12. Move `ops/intake/linear-issues-agents-md-gaps.md` into `ops/intake/unprocessed/`.
13. Resolve 6 cross-duplicate images between R09 and R10.
14. Write the archive routing rule: one sentence in AGENTS.md for `archive/` vs `ops/archive/`.

### To reach 9+/10 (Agent-Excellence Grade)

15. Declare canonical image naming: `rXX-NN.jpg` wins. Write and execute migration script. Apply to R12 (zero canonical images).
16. Move `data/operations/whatsapp/messages.db` and `whatsapp.db` out of git (PII in SQLite, wrong medium).
17. Add YAML frontmatter (`id`, `type`, `status`) to all files in `ops/decisions/` and `ops/handoff/`.
18. Create `data/pending-domains/` and document the hardening protocol.
19. Establish `logs/` rotation policy in `Makefile` or declare logs permanently `.gitignore`d.
20. Flatten archive root: move 6 loose files into `archive/legacy/` dated subdirectories.

---

## Next Actions

| Priority | Action | Target Path | Est. Effort |
|----------|--------|-------------|-------------|
| P0 | Add `logs/`, `tmp/`, `*.db` to `.gitignore`, remove from git tracking | `.gitignore` | 10 min |
| P0 | Move `tmp/` contents to `ops/archive/`, remove `tmp/` from git | `tmp/` | 15 min |
| P0 | Run `make structure-update` | `project/STRUCTURE.md` | 2 min |
| P0 | Fix `PRINCIPLES.md` L3: `archives/` → `archive/` | `project/PRINCIPLES.md` | 1 min |
| P0 | Remove empty ghost dirs `src/` and `infra/` | `src/`, `infra/` | 5 min |
| P1 | Move `data/platforms/` (6 files) to `ops/audit/platform-research/` | `data/platforms/` | 10 min |
| P1 | Fix `ops/handoff/INDEX.md`: reconcile active entries, add 0227 | `ops/handoff/INDEX.md` | 10 min |
| P1 | Move `docs/tmp/Api.md` → `.agents/hotelrunner/api-channel-codes.md` | `docs/tmp/` | 5 min |
| P1 | Move `docs/security/.env-credentials-policy.md` → `context/meta/architecture/` | `docs/security/` | 5 min |
| P1 | Fix `data/README.md`: remove non-existent subdir references | `data/README.md` | 5 min |
| P1 | Resolve `ops/planning/`: document in AGENTS.md or delete | `AGENTS.md` | 10 min |
| P1 | Fix 6 cross-duplicate images R09/R10 | `data/rooms/R09,R10/images/` | 20 min |
| P2 | Declare canonical image scheme; migrate all rooms; apply to R12 | `data/rooms/` | 2-3 hours |
| P2 | Add YAML frontmatter to `ops/decisions/` and `ops/handoff/` files | `ops/decisions/`, `ops/handoff/` | 1-2 hours |
| P2 | Create `data/pending-domains/` and document hardening protocol | `data/` | 20 min |
| P2 | Write archive routing rule in AGENTS.md (`archive/` vs `ops/archive/`) | `AGENTS.md` | 15 min |

---

### Final Verdict

**Tier:** D
**Score:** 51%
**Status:** REJECTED

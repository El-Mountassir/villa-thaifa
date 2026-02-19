# Migration Path Validation

**Date**: 2026-02-19
**Purpose**: Validate 18 proposed migration target paths against the Villa Thaifa directory contract (AGENTS.md).
**Contract sources**: `AGENTS.md` §File Placement Decision Tree + §Directory Contract, `docs/core/STRUCTURE.md`

---

## Summary Table

| # | Proposed Path | Verdict | Correct Path (if different) |
|---|---|---|---|
| 1 | `docs/planning/pms-roadmap.md` | REPATH | `context/meta/planning/pms-roadmap.md` |
| 2 | `docs/planning/data-inventory.md` | REPATH | `context/meta/planning/data-inventory.md` |
| 3 | `docs/planning/delegation-framework.md` | REPATH | `context/meta/planning/delegation-framework.md` |
| 4 | `docs/planning/tech-decisions.md` | REPATH | `ops/decisions/tech-decisions.md` |
| 5 | `docs/planning/sessions/2026-02-13-session-capture.md` | REPATH | `ops/archive/sessions/2026-02-13-session-capture.md` |
| 6 | `docs/research/existing-app-audit.md` | REPATH | `ops/audit/existing-app-audit.md` |
| 7 | `docs/research/missing-yaml-investigation.md` | REPATH | `context/meta/knowledge/missing-yaml-investigation.md` |
| 8 | `docs/research/yaml-backup-search.md` | REPATH | `context/meta/knowledge/yaml-backup-search.md` |
| 9 | `docs/research/repo-strategy-decision.md` | REPATH | `ops/decisions/repo-strategy-decision.md` |
| 10 | `docs/research/consolidation-app-eval.md` | REPATH | `context/meta/knowledge/consolidation-app-eval.md` |
| 11 | `docs/client/said-thaifa.md` | COMPLIANT | — |
| 12 | `docs/client/communications.md` | COMPLIANT | — |
| 13 | `docs/integrations/whatsapp-mcp-setup.md` | REPATH | `docs/workflows/whatsapp-mcp-setup.md` |
| 14 | `data/whatsapp/messages.db` | REPATH | `data/pending-domains/whatsapp/messages.db` |
| 15 | `data/whatsapp/whatsapp.db` | REPATH | `data/pending-domains/whatsapp/whatsapp.db` |
| 16 | `docs/integrations/whatsapp-context.md` | REPATH | `context/meta/knowledge/whatsapp-context.md` |
| 17 | `docs/backlog/logo-design.md` | REJECT | Create as Linear issue (VT team) |
| 18 | `docs/backlog/resume-project.md` | REJECT | Create as Linear issue (VT team) |

---

## Detailed Verdicts

### Items 1–5: Planning Documents

---

**1. `docs/planning/pms-roadmap.md`** — 4-phase PMS roadmap, tech stack, 38-day plan

- Decision tree: Not structured domain data. Not a live operational artifact. Is it read-only reference material (planning)? YES.
- Contract: "Reference material (architecture docs, planning docs, templates, agent configs) lives in `context/`. Planning → `context/meta/{topic}`."
- `docs/planning/` does not exist in the contract. `docs/` is for workflow guides, client info, and foundational definitions only.
- **VERDICT: REPATH → `context/meta/planning/pms-roadmap.md`**
- Note: `context/meta/planning/` already exists per STRUCTURE.md.

---

**2. `docs/planning/data-inventory.md`** — Data migration strategy

- Same reasoning as #1: a planning/strategy document is read-only reference material.
- A migration strategy is consumed as background reference, not an operational how-to guide.
- **VERDICT: REPATH → `context/meta/planning/data-inventory.md`**

---

**3. `docs/planning/delegation-framework.md`** — Multi-model agent delegation

- Agent-related architecture/planning material is explicitly `context/` territory.
- Decision tree: read-only reference material → `context/meta/{topic}`. Agent configs → `context/agents/`. Since this is a framework/planning doc (not per-agent config), `context/meta/planning/` is correct.
- **VERDICT: REPATH → `context/meta/planning/delegation-framework.md`**

---

**4. `docs/planning/tech-decisions.md`** — Tech stack decision rationale

- Decision tree: Is it a live operational artifact? A decision record? YES — tech stack decisions are explicit decisions, not passive planning reference.
- Contract: "Is it a decision record? → `ops/decisions/`". Decision records carry date prefix by convention.
- **VERDICT: REPATH → `ops/decisions/tech-decisions.md`**
- Structural note: Add date prefix if the decision timestamp is known (e.g., `ops/decisions/2026-02-13-tech-decisions.md`).

---

**5. `docs/planning/sessions/2026-02-13-session-capture.md`** — Session transcript

- A session transcript is a historical/completed artifact. Decision tree: Is it old/completed? → `ops/archive/`. Not a handoff (not forward-looking), not an audit report, not a status dashboard.
- `docs/planning/sessions/` does not exist in the contract and has no basis in the directory contract.
- **VERDICT: REPATH → `ops/archive/sessions/2026-02-13-session-capture.md`**
- Structural note: `ops/archive/sessions/` is a new subdirectory. It aligns with the `ops/archive/` purpose ("archived operational artifacts by date"). Acceptable to create.

---

### Items 6–10: Research Documents

---

**6. `docs/research/existing-app-audit.md`** — 368 LOC skeleton audit

- "Audit" is explicitly named in the decision tree and contract: "Is it an audit report? → `ops/audit/`".
- `docs/research/` has no basis in the contract; `docs/` does not accommodate research or audit content.
- **VERDICT: REPATH → `ops/audit/existing-app-audit.md`**

---

**7. `docs/research/missing-yaml-investigation.md`** — YAML backup search

- An investigation/research document that has concluded is read-only knowledge/reference material, not a live operational artifact.
- Decision tree: read-only reference material → `context/meta/{topic}`. Knowledge references → `context/meta/knowledge/`.
- **VERDICT: REPATH → `context/meta/knowledge/missing-yaml-investigation.md`**

---

**8. `docs/research/yaml-backup-search.md`** — Data recovery research

- Same category as #7: concluded research, now reference-only knowledge.
- **VERDICT: REPATH → `context/meta/knowledge/yaml-backup-search.md`**
- Structural note: Items 7 and 8 are closely related (YAML investigation + backup search). Consider consolidating into one file if they cover the same incident, per DRY rule.

---

**9. `docs/research/repo-strategy-decision.md`** — GitHub repo decision

- The name contains "decision" and describes a GitHub repo strategy choice — this is a decision record, not a passive research document.
- Contract: decision records → `ops/decisions/`, with date prefix.
- **VERDICT: REPATH → `ops/decisions/repo-strategy-decision.md`**
- Structural note: Add date prefix if timestamp is known.

---

**10. `docs/research/consolidation-app-eval.md`** — App evaluation

- An app evaluation that has concluded is reference material (knowledge) rather than a live operational artifact. It is consumed passively going forward.
- Decision tree: read-only reference → `context/meta/knowledge/`.
- **VERDICT: REPATH → `context/meta/knowledge/consolidation-app-eval.md`**

---

### Items 11–12: Client Documents

---

**11. `docs/client/said-thaifa.md`** — Client profile (Said, 78 years old)

- Decision tree: "Is it operational documentation — client/stakeholder info? → `docs/client/`."
- Contract: "`docs/client/` = stakeholder profiles, admin notes, support contacts." Client profile is an exact match.
- **VERDICT: COMPLIANT**

---

**12. `docs/client/communications.md`** — Historical comms summary

- A historical communications summary for a client belongs with the client's profile context.
- Contract: "`docs/client/` = stakeholder profiles, admin notes, support contacts." Communications history is support/stakeholder context.
- **VERDICT: COMPLIANT**

---

### Items 13–16: WhatsApp / Integrations

---

**13. `docs/integrations/whatsapp-mcp-setup.md`** — WhatsApp MCP server setup guide

- "Setup guide" = a how-to procedure for an operational tool. Decision tree: "Is it operational documentation — a workflow or procedure? → `docs/workflows/`."
- `docs/integrations/` does not exist in the contract. The contract does not define an integrations subdirectory under `docs/`.
- A setup guide is a workflow/procedure, not a foundational definition or client doc.
- **VERDICT: REPATH → `docs/workflows/whatsapp-mcp-setup.md`**
- Structural note: No new directory needed; `docs/workflows/` already exists.

---

**14. `data/whatsapp/messages.db`** — WhatsApp messages database (SQLite)

- Decision tree: Is it structured domain data? YES — a SQLite database is structured domain data.
- However, `data/whatsapp/` does not exist in the contract's defined subdirectories. WhatsApp messages are a new domain not yet represented in `data/`.
- Contract: "Is it a new domain not yet hardened? → `data/pending-domains/`."
- WhatsApp as a data domain is not yet in the contract schema (rooms, bookings, finance, operations, property are the defined domains). It needs hardening before being a first-class `data/` subdomain.
- **VERDICT: REPATH → `data/pending-domains/whatsapp/messages.db`**
- Structural note: Once the WhatsApp domain contract is defined (schema, retention policy, purpose), it can graduate to `data/whatsapp/`. Until then, `data/pending-domains/` is the correct staging area.

---

**15. `data/whatsapp/whatsapp.db`** — WhatsApp metadata database (SQLite)

- Same reasoning as #14: structured domain data for an uncontracted domain.
- **VERDICT: REPATH → `data/pending-domains/whatsapp/whatsapp.db`**
- Structural note: Both WhatsApp DBs (#14, #15) should land together in `data/pending-domains/whatsapp/`. Consider also whether SQLite files should be gitignored (they are binary, potentially large, and may contain PII) — this warrants a separate decision.

---

**16. `docs/integrations/whatsapp-context.md`** — WhatsApp surface context

- "Context" material that describes how a surface works is read-only reference, not a workflow or client doc.
- Decision tree: read-only reference material → `context/meta/{topic}`. Knowledge references → `context/meta/knowledge/`.
- `docs/integrations/` has no basis in the contract.
- **VERDICT: REPATH → `context/meta/knowledge/whatsapp-context.md`**

---

### Items 17–18: Backlog Items

---

**17. `docs/backlog/logo-design.md`** — Logo design task

- A backlog item is a work item / task, not a document. AGENTS.md is explicit: "Primary backlog: Linear — all durable work items live here."
- `docs/backlog/` has no basis in the contract and violates the task registry rule: durable work items belong in Linear, not in files.
- A logo design task is a VT-team issue (or EM-team if it spans the broader brand), not a documentation artifact.
- **VERDICT: REJECT — Create as a Linear issue in the VT (or EM) team instead of migrating as a file.**

---

**18. `docs/backlog/resume-project.md`** — Project resume task

- Same reasoning as #17: a project resume item is a work item, not a document.
- Migrating it as a file under `docs/backlog/` would create an undiscoverable parallel task registry outside Linear, violating the single-registry principle.
- **VERDICT: REJECT — Create as a Linear issue in the VT team. If it contains reference context needed for resuming, extract that context to the appropriate `context/meta/` file and link from the Linear issue.**

---

## Structural Concerns

### New subdirectories required (if repaths are accepted)

| New Directory | Reason |
|---|---|
| `ops/archive/sessions/` | Session transcripts need a home in `ops/archive/`. |
| `data/pending-domains/whatsapp/` | WhatsApp DB domain staging area. |

Both are low-risk: `ops/archive/` and `data/pending-domains/` already exist; these are subdirectories within established areas.

### `docs/planning/` and `docs/research/` — Do not create

Neither `docs/planning/` nor `docs/research/` should be created. They have no basis in the directory contract. All content proposed for these paths belongs in `context/meta/planning/`, `context/meta/knowledge/`, or `ops/`.

### `docs/integrations/` — Do not create

This subdirectory has no basis in the contract. Its two proposed files split correctly to `docs/workflows/` (setup guide) and `context/meta/knowledge/` (context doc).

### SQLite files in git

Items 14–15 are binary SQLite databases. Consider whether they should be gitignored or committed. They may contain guest PII and grow large. This warrants a decision record in `ops/decisions/` before migration.

### Decision record date prefixes

Items 4 and 9 should carry date prefixes per contract convention (`ops/decisions/YYYY-MM-DD-{name}.md`). Confirm timestamps before finalizing paths.

---

## Action Checklist

- [ ] Confirm timestamps for items 4 and 9 to apply correct date prefixes in `ops/decisions/`
- [ ] Decide gitignore strategy for SQLite files (items 14–15) before migrating
- [ ] Create Linear issues for items 17–18 before discarding source content
- [ ] Consolidate items 7+8 if they cover the same YAML incident
- [ ] Run `make structure-cards` after migration to regenerate role-based structure cards

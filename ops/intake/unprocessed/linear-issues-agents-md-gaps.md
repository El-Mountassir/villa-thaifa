# Linear Issues — AGENTS.md Governance Gaps

> **Created:** 2026-02-21
> **Team:** VT (Villa Thaifa)
> **Status:** PENDING CREATION — MCP Linear server not connected in this session
> **Action Required:** Run `/linear` in a session where MCP Linear is connected, or create manually via Linear UI
> **Target State:** Backlog | Label: `working` (governance/process issues)

---

## Issues to Create

### Issue 1

- **Title:** Add cascade update protocol to AGENTS.md
- **Priority:** 3 (Normal / P2 Medium)
- **Labels:** `working`, `📚 Documentation`
- **State:** Backlog
- **Description:** When a decision is made or data changes, there is no protocol ensuring ALL impacted files get updated. Need a cascade checklist: if you change X, also update Y and Z. Example: decision made → update ops/decisions/, open-conflicts-registry.md, truth.md. SYNC step was added to the Mandatory Workflow but needs formalization as a reusable protocol with explicit examples.

---

### Issue 2

- **Title:** Clarify archive vs delete criteria in AGENTS.md
- **Priority:** 2 (High / P1)
- **Labels:** `working`, `📚 Documentation`
- **State:** Backlog
- **Description:** Current AGENTS.md does not clearly define when to archive vs delete. Universal rules have Preserve First and Capture Before Archive but AGENTS.md does not reference them for VT-specific contexts. Need: VT-specific examples, a decision tree for archive/delete, and explicit reference to universal rules.

---

### Issue 3

- **Title:** Reference Capture Before Archive in VT workflow
- **Priority:** 2 (High / P1)
- **Labels:** `working`, `📚 Documentation`
- **State:** Backlog
- **Description:** universal.md has a comprehensive Capture Before Archive protocol but AGENTS.md does not reference it. VT agents archiving files may skip extraction. Add explicit reference and VT-specific extraction destinations: which ops/ files to update, which Linear labels to apply.

---

### Issue 4

- **Title:** Add cross-linking convention to AGENTS.md
- **Priority:** 3 (Normal / P2 Medium)
- **Labels:** `working`, `📚 Documentation`
- **State:** Backlog
- **Description:** No convention exists for how files should reference each other. When a decision in ops/decisions/ relates to data in data/, there is no standard for bidirectional links. Need: a link format convention and mandatory cross-reference rules between related files.

---

### Issue 5

- **Title:** Create ops/decisions/tech-decisions.md for tech stack tracking
- **Priority:** 4 (Low / P3)
- **Labels:** `working`, `📚 Documentation`, `⚙️ Config`
- **State:** Backlog
- **Description:** Tech decisions (json-render rejected, Next.js+Tailwind chosen, DB TBD) are scattered across multiple files. Need a dedicated tech decisions tracker referenced from the AGENTS.md SYNC checklist. The SYNC checklist already references this file but it does not exist yet.

---

### Issue 6

- **Title:** Define handoff trigger criteria in AGENTS.md
- **Priority:** 3 (Normal / P2 Medium)
- **Labels:** `working`, `📚 Documentation`
- **State:** Backlog
- **Description:** No defined criteria for when a session handoff should be created. Currently ad-hoc. Need: trigger conditions (session end, context approaching limit, domain switch, blocking issue), handoff template reference, and mandatory fields for a valid handoff.

---

### Issue 7

- **Title:** Document SYNC step rationale and examples
- **Priority:** 4 (Low / P3)
- **Labels:** `working`, `📚 Documentation`
- **State:** Backlog
- **Description:** SYNC step (step 5) was added to the Mandatory Workflow but lacks supporting documentation. Need concrete examples showing a properly synced change vs a drift-causing change. Likely home: docs/workflows/sync-protocol.md.

---

## Notes

- No "governance" label confirmed in workspace. Closest match: `working` (Ways of Working — methodology, processes, workflows). Apply `working` as primary label for all 7 issues.
- Priority mapping used: High (P1) = Linear priority 2, Medium (P2) = Linear priority 3, Low (P3) = Linear priority 4.
- All issues target Backlog state per request.
- MCP Linear server must be active to create these via mcp__linear__create_issue.

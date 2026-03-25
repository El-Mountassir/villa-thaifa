# Workflow Research — Comprehensive Catalog & Analysis

> **Date**: 2026-02-23
> **Purpose**: Catalog every workflow definition across Omar's workspace to inform unified Core Workflow design
> **Researcher**: Nova (Claude Opus 4.6)
> **Scope**: ~/omar/, ~/.claude/, ~/villa-thaifa/ — all workflow definitions, patterns, and process documents

---

## Table of Contents

1. [Summary Table](#1-summary-table)
2. [Per-Workflow Detail](#2-per-workflow-detail)
3. [Gap Analysis](#3-gap-analysis)
4. [Overlap Analysis](#4-overlap-analysis)
5. [Synthesis](#5-synthesis)

---

## 1. Summary Table

**Total workflows found: 16** (plus 4 workflow-adjacent skills with embedded process definitions)

| # | Name | Location | Scope | Phases | Status |
|---|------|----------|-------|--------|--------|
| 1 | **Original Core Loop** | `villa-thaifa/ops/planning/archive/2026-01-08-core-loop-simplification.md` | Universal (VT) | 6 phases | Archived — superseded |
| 2 | **VT Mandatory Workflow** | `villa-thaifa/AGENTS.md` §Mandatory Workflow | VT operations | 6 phases | Active |
| 3 | **Kael Core Loop** | `~/omar/operational/el-mountassir/members/silicon/kael/sys/core/prompt/README.md` §3 | Universal (EM) | 10 phases | Active (Kael-specific) |
| 4 | **Unified Workflow Guide** | `~/omar/intent/workflow/unified-guide.md` | Universal (all work) | 5 phases | Active — v1.0 |
| 5 | **Thinking Cycle** | `~/omar/intent/workflow/thinking-cycle.md` | Cross-cutting cognitive | 6 phases | Active — v0.1 |
| 6 | **Development Workflow** | `~/omar/intent/workflow/development-workflow.md` | Software development | 5 phases | Active — v0.2 |
| 7 | **Agent Lifecycle Pattern** | `~/omar/intent/workflow/agent-lifecycle-pattern.md` | Agent management | 9 phases | Active — v0.1 |
| 8 | **ERV Workflow** | `~/omar/intent/workflow/processes/workflows/evaluate-remediate-verify.md` | Quality improvement | 7 steps | Active — v1.1 |
| 9 | **Workspace Org Playbook** | `~/omar/intent/workflow/cleanup-playbook.md` | Workspace maintenance | 9 steps | Active — v2.0 |
| 10 | **VT Price Update** | `villa-thaifa/docs/workflows/pricing.md` | VT pricing ops | 6 steps | Active |
| 11 | **VT Reservation (archived)** | `villa-thaifa/archive/2025/workflows/reservation.md` | VT reservation ops | 5 steps | Archived |
| 12 | **VT Guest Communication (archived)** | `villa-thaifa/archive/2025/workflows/guest-communication.md` | VT guest comms | 4 steps | Archived |
| 13 | **VT Pricing (archived, French)** | `villa-thaifa/archive/2025/workflows/pricing.md` | VT pricing ops | 6 steps | Archived — French original |
| 14 | **OTA Capture** | `~/omar/core/resources/skills/ota-capture/SKILL.md` | OTA data sync | 5 steps | Active skill |
| 15 | **Taxonomy Consolidation ADW** | `~/omar/core/resources/workflows/taxonomy-consolidation-adw.md` | Workspace restructuring | 3 steps | Active |
| 16 | **Task Routing Protocol** | `~/omar/intent/workflow/task-routing-protocol.md` | Work routing | Decision tree | Active |
| — | **WOS Skill** | `~/omar/core/resources/skills/wos/SKILL.md` | Work orchestration routing | Routing tables | Active skill |
| — | **Orchestrate Skill** | `~/omar/core/resources/skills/orchestrate.md` | Delegation decision | 5 steps | Active skill |
| — | **Decide Skill** | `~/omar/core/resources/skills/decide/SKILL.md` | Decision analysis | 11 steps | Active skill |
| — | **Framework Evaluation** | `~/omar/core/resources/skills/framework-evaluation.md` | Tech evaluation | 3 phases + checklist | Active skill |

### Governance-Embedded Workflows (not standalone, but contain workflow phases)

| Rule/Pattern | Location | Workflow Content |
|---|---|---|
| Five Rails | `universal.md` §Five Rails | 131 pattern, DRY, TDD, Fix Rules, Plan First |
| Phase Gate | `universal.md` §Phase Gate | No Advancement Without Approval |
| Autonomy Tiers | `universal.md` §Autonomy Tiers | ACT / INFORM / ASK decision tree |
| Mode System Dispatch | `~/.claude/CLAUDE.md` | 6 modes x 8 behaviors = 48 behavioral rules |
| ADR-005 Signature | `~/omar/intent/decisions/adr-005-execution-requires-signature.md` | Execution requires formal approval |
| Cascade Update | `universal.md` §Cascade Update | Post-edit verification protocol |
| Capture Before Archive | `universal.md` §Capture Before Archive | 5-step pre-archive extraction |
| Zero-Loss Operations | `universal.md` §Zero-Loss Operations | Safety net → Read → Verify chain |

---

## 2. Per-Workflow Detail

### WF-01: Original Core Loop (2026-01-08)

**Location**: `/home/director/villa-thaifa/ops/planning/archive/2026-01-08-core-loop-simplification.md`
**Status**: ARCHIVED — the genesis document

**Phases**:
1. **COMPRENDRE** — What is being asked?
2. **EXPLORER** — What context exists?
3. **CLARIFIER** — Confidence >= 94%? If not, AskUserQuestion
4. **EXECUTER** — Delegate to sub-agents
5. **VERIFIER** — Is it done correctly?
6. **REPORTER** — Communicate result (in French)

**Guard-rails**: 94% confidence threshold (hard stop). Platform checklist before HotelRunner actions.

**Decision points**: Phase 3 (CLARIFIER) — if confidence < 94%, loop back.

**Unique value**: The 94% confidence threshold is a numerical gate that no other workflow uses. The loop-back mechanism (CLARIFIER → COMPRENDRE if low confidence) is explicit and measurable.

**Scope**: Designed as THE universal workflow for VT — intended to replace all fragmented workflows.

---

### WF-02: VT Mandatory Workflow (AGENTS.md)

**Location**: `/home/director/villa-thaifa/AGENTS.md` §Mandatory Workflow
**Status**: ACTIVE — current VT contract

**Phases**:
1. **SCOUT** — Understand current state
2. **REPORT** — Summarize findings
3. **QUESTIONS** — Ask for clarification (with context)
4. **ACTION** — Execute after confirmation
5. **SYNC** — Update all impacted files (with explicit checklist)
6. **COMMIT** — Run `make changelog`, commit. Pushing = ASK tier.

**Guard-rails**: SYNC checklist (6 "If you changed X, also update Y" rules). Committing = Tier 1 (ACT), pushing = Tier 3 (ASK). Contestability Policy (treat unprocessed data as potentially outdated).

**Decision points**: Phase 3 (QUESTIONS) — human-in-the-loop. Phase 5 (SYNC) — checklist-driven.

**Unique value**: The SYNC phase with its explicit impact checklist is unique — no other workflow has a structured "what else did this change affect?" phase. The COMMIT phase making commit/push a first-class workflow step is also unique.

**Scope**: VT operations only — referenced from AGENTS.md.

---

### WF-03: Kael Core Loop

**Location**: `/home/director/omar/operational/el-mountassir/members/silicon/kael/sys/core/prompt/README.md` §3
**Status**: ACTIVE — Kael's identity-bound workflow

**Phases**:
1. **RECEIVE** — Capture intent with full details. Read POP + priority queue at session start.
2. **DELEGATION CHECK** — MANDATORY: Can sub-agent do this? Is it deterministic? Am I acting as executor?
3. **CLASSIFY** — Trivial (<3 steps) or Complex (3+ steps)?
4. **ROUTE** — Trivial → execute. Complex → Plan Mode → Delegate → Verify. Specs → intent/.
5. **VERIFY** — Never claim completion without proof.
6. **REPORT** — Brief status update with links to artifacts.
7. **HANDOFF** — Linear updated, handoff file ready.
8. **TASKS.md UPDATE** — Immediate, non-optional.
9. **POST-OUTPUT TASKS SCAN** — Scan output for implicit actionable items.
10. **GHOST ITEM DETECTION** — Continuous scan for untracked work.

**Guard-rails**: 17 named guardrails (CONTEXT BURN, SOLO CODING, WALL OF TEXT, NO LINEAR, NO EVIDENCE, LOST KNOWLEDGE, BULK OPS, NO TASK GRAPH, FLAT STRUCTURE, MEMORY BRIEF, DELEGATION CHECK, WARM-UP TRAP, TOOL MISMATCH, MANUAL SESSION CLOSE, TASKS.md DELAY, SKILL UNKNOWN, SELF-EXCLUSION, QUESTION TAX, MARATHON COMPLETION, NO DEEP THINKING, ERV AUDIT, FOURRE-TOUT FILE, PARTNERSHIP MODE).

**Decision points**: Phase 2 (DELEGATION CHECK) — 3-question mandatory self-check. Phase 3 (CLASSIFY) — complexity routing.

**Unique value**: The most elaborate workflow — 10 phases + 20+ guardrails. The GHOST ITEM DETECTION phase (continuous) is unique. The MARATHON COMPLETION template pattern ("Fait: [X]. Prochain: [Y].") prevents question-asking at task boundaries. The QUESTION TAX guardrail with explicitly FORBIDDEN phrases.

**Scope**: Universal for Kael (the EM workspace agent).

---

### WF-04: Unified Workflow Guide

**Location**: `/home/director/omar/intent/workflow/unified-guide.md`
**Status**: ACTIVE v1.0 — the closest thing to a unified workflow

**Phases**:
1. **Frame** (WHY/WHAT) — Understand the problem
2. **Research** (CONTEXT) — Gather context, check prior work
3. **Plan** (HOW) — Define what to build, TaskCreate graph
4. **Execute** (BUILD) — Delegate aggressively, orchestrate
5. **Verify** (DONE?) — Two-stage review (spec compliance + quality)

**Guard-rails**: Gates between phases require Omar's acknowledgment. >200 lines read OR >100 lines write = spawn sub-agent. Phase skipping guide per task type.

**Decision points**: Every phase gate. Frame phase (Omar validates direction). Plan phase (Omar reviews plan file). Verify phase (Omar reviews final result).

**Unique value**: Maps all 5 work types (Development, Research, Operations, Business, Creative) to the same 5 phases with type-specific quick references. Massive Skill Dispatch Table (60+ skills mapped to phases). Phase skipping guidance.

**Scope**: Universal — all work types, all domains. Explicitly the "master guide."

---

### WF-05: Thinking Cycle

**Location**: `/home/director/omar/intent/workflow/thinking-cycle.md`
**Status**: ACTIVE v0.1 — cognitive engine

**Phases**:
1. **Frame** — Define the problem
2. **Research** — Understand what exists
3. **Evaluate** — Score options (MANDATORY scoring, 0-10)
4. **Ground** — Confront theory with reality
5. **Re-evaluate** — Loop back if grounding reveals issues
6. **Design** — Create the solution

**Guard-rails**: Scoring is MANDATORY (no gut feelings). Any phase can loop back. Grounding must confront theory with actual data.

**Decision points**: Phase 5 (Re-evaluate) — loop or proceed decision. Phase 3 (Evaluate) — scoring forces explicit comparison.

**Unique value**: The GROUND phase (theory-reality confrontation) is unique across all workflows. The loop-back from any phase is explicitly modeled. Research of 15 frameworks (OODA, Cynefin, etc.) informed the design. Explicitly called an "ENGINE" that powers domain workflows — it is not a workflow itself but the cognitive process within workflow phases.

**Scope**: Cross-cutting — used WITHIN other workflows for non-trivial problems.

---

### WF-06: Development Workflow

**Location**: `/home/director/omar/intent/workflow/development-workflow.md`
**Status**: ACTIVE v0.2

**Phases**:
0. **Discover** (LEARN) — Research what exists, audit current state
1. **Brainstorm** (WHY) — Understand problem, propose approaches, recommend one
2. **Plan & Design** (WHAT) — Design doc, bite-sized tasks, task graph
3. **Execute (TDD)** (HOW) — RED → GREEN → REFACTOR per task
4. **Review** (VERIFY) — Two-stage: spec compliance + quality

**Guard-rails**: Gates require Omar's approval per phase. TDD cycle mandatory. Plan First (no plan = no execution). Phase skip guide by task type.

**Decision points**: Phase 1 gate (Omar says "go"). Phase 2 gate (Omar reviews plan). Phase 4 (predictive failure analysis).

**Unique value**: TDD cycle (RED-GREEN-REFACTOR) as first-class Execute sub-phases. Retrospective template (4 questions). Phase skip guide is well-detailed.

**Scope**: Software development only.

---

### WF-07: Agent Lifecycle Pattern

**Location**: `/home/director/omar/intent/workflow/agent-lifecycle-pattern.md`
**Status**: ACTIVE v0.1

**Phases**:
1. **Trigger** — Something creates need for agent work
2. **Decide** — Choose execution model + agent type
3. **Brief** — Structured brief (Goal, Context, Scope, Output, Constraints, References)
4. **Launch** — Execute the decision
5. **Monitor** — Check on running agents
6. **Collect** — Gather results
7. **Verify** — Two-stage review (spec + quality)
8. **Dissolve** — Clean up
9. **Integrate** — Merge results into knowledge/workflow

**Guard-rails**: Anti-trigger list (when NOT to delegate). Brief checklist (6 items). Cost awareness (match model to task importance). Integration is NOT optional.

**Decision points**: Phase 2 (execution model decision tree). Phase 5 (intervention criteria). Phase 7 (quick vs full verify).

**Unique value**: Only workflow that explicitly covers agent lifecycle from trigger to integration. Decision tree for solo/sub-agent/team selection. Model cost awareness built in. The DISSOLVE phase (cleanup) and INTEGRATE phase (connect to existing work) are unique.

**Scope**: Cross-cutting — agent management across all work types.

---

### WF-08: ERV Workflow (Evaluate-Remediate-Verify)

**Location**: `/home/director/omar/intent/workflow/processes/workflows/evaluate-remediate-verify.md`
**Status**: ACTIVE v1.1

**Steps**:
1. **SPOT** — Notice issue, capture artifact path
2. **EVALUATE** — Run critical-evaluation skill
3. **TRIAGE** — Categorize findings into P0/P1/P2 tiers
4. **GRAPH** — Create task graph with dependencies
5. **EXECUTE** — Phase 1 (Critical) → Phase 2 (Tests) → Phase 3 (Quality)
6. **VERIFY** — Run validation post-fix
7. **CLOSE** — TRACKER reconciliation and summary

**Guard-rails**: Score < 7/10 triggers ERV. Dependency chain: fix critical → add tests → refactor. Within a phase, tasks run parallel IF no file conflicts. Re-evaluation after Phase 3.

**Decision points**: Phase 2 (score threshold). Phase 3 (triage severity). Phase 5 (phased execution respecting dependencies).

**Unique value**: The phased execution with dependency chains (critical → tests → quality) is unique. Layer 3 in a 3-layer quality system. Token cost awareness (~80K per audit). Score calibration discussion.

**Scope**: Quality improvement — any artifact scoring < 7/10.

---

### WF-09: Workspace Organization Playbook

**Location**: `/home/director/omar/intent/workflow/cleanup-playbook.md`
**Status**: ACTIVE v2.0

**Steps**:
1. **Protect** — Identify do-not-touch items
2. **Snapshot** — Baseline metrics
3. **Prune** — Delete regenerable junk (zero-decision patterns only)
4. **Classify** — Understand content types, activity levels, domain mapping
5. **Consolidate** — Merge related items
6. **Route** — Apply file placement rules
7. **Execute** — Move/rename/restructure
8. **Verify** — Compare against snapshot
9. **Maintain** — Loop back for next cycle

**Guard-rails**: Protect phase before any mutations. Zero-decision pruning (only clearly regenerable items). Snapshot for before/after comparison.

**Decision points**: Phase 3 (what to prune). Phase 6 (where to route files).

**Unique value**: Only workflow for workspace maintenance. Protect-first approach. Zero-decision pruning concept. Before/after snapshot comparison.

**Scope**: Workspace organization — any directory tree.

---

### WF-10: VT Price Update

**Location**: `/home/director/villa-thaifa/docs/workflows/pricing.md`
**Status**: ACTIVE

**Steps**:
1. **BASELINE** — Capture current state (backup)
2. **PLAN** — Document changes (old rate, new rate, reason, effective date)
3. **CONFIRM** — Omar validation (comparative table, wait for explicit approval)
4. **EXECUTE** — Apply on HotelRunner
5. **VERIFY** — Confirm on Booking.com (propagation check)
6. **UPDATE DATA** — Update rooms.md, log in archive, changelog entry

**Guard-rails**: Risk table (3 risks with mitigations). 15-min propagation check. Double-check before validation.

**Decision points**: Phase 3 (CONFIRM) — Omar must explicitly validate.

**Unique value**: Domain-specific with platform integration steps (HotelRunner, Booking.com). Risk mitigation table. Propagation verification timing.

**Scope**: VT pricing operations only.

---

### WF-11: VT Reservation (Archived)

**Location**: `/home/director/villa-thaifa/archive/2025/workflows/reservation.md`
**Status**: ARCHIVED

**Steps**:
1. **PARSE** — Extract: dates, room, guest name, adults/children, source
2. **VERIFY** — Check against data/specs/ for conflicts
3. **REPEAT BACK** — Confirm with Omar (explicit "oui" required)
4. **EXECUTE** — Create on HotelRunner
5. **CONFIRM** — Verify success, update data

**Guard-rails**: Confidence > 90% on all parsed fields. Screenshot before submission. Error escalation protocol (don't panic, screenshot, escalate, document).

**Decision points**: Phase 3 (REPEAT BACK) — Omar must say "oui."

**Unique value**: PARSE phase (structured data extraction from unstructured input). REPEAT BACK pattern (explicit confirmation with exact values). Error recovery protocol.

**Scope**: VT reservation operations.

---

### WF-12: VT Guest Communication (Archived)

**Location**: `/home/director/villa-thaifa/archive/2025/workflows/guest-communication.md`
**Status**: ARCHIVED

**Steps**:
1. **SCOUT** — Verify available info, prepare what we know, identify gaps
2. **REPORT** — Inform of discoveries first
3. **QUESTIONS** — Ask what's missing (with context)
4. **ACTION** — Execute when all info received

**Guard-rails**: Vouvoiement always with Said/clients. Report before asking. Message format templates (WhatsApp first message, follow-ups, formal).

**Decision points**: Phase 3 (QUESTIONS) — only after REPORT.

**Unique value**: Communication-specific templates. Vouvoiement enforcement. Anti-patterns table (tutoiement, questions sans contexte, mur de texte).

**Scope**: VT guest/stakeholder communication.

---

### WF-13: VT Pricing (Archived, French)

**Location**: `/home/director/villa-thaifa/archive/2025/workflows/pricing.md`
**Status**: ARCHIVED — French original of WF-10

Identical structure to WF-10 but in French and referencing old `data/specs/` paths. Superseded by WF-10.

---

### WF-14: OTA Capture Skill

**Location**: `/home/director/omar/core/resources/skills/ota-capture/SKILL.md`
**Status**: ACTIVE skill

**Steps**:
1. **CAPTURE** — Browser agent extracts raw data from OTA page
2. **TRIAGE** — Classify each data point via DRY Routing Table
3. **REVIEW** — Human reviews contradictions and ambiguous items
4. **SYNC** — Update target SSOT files with source annotations
5. **VALIDATE** — Cross-check SSOT against captured data

**Guard-rails**: CONTRADICTION and IMPLAUSIBLE flags require human review. DRY routing (each fact in ONE file). Source annotations mandatory.

**Decision points**: Phase 3 (REVIEW) — human approves contradictions.

**Unique value**: Data quality flags system. DRY routing for multi-source data. Browser agent integration for live platform scraping.

**Scope**: OTA platform data capture (Booking.com, Expedia, etc.).

---

### WF-15: Taxonomy Consolidation ADW

**Location**: `/home/director/omar/core/resources/workflows/taxonomy-consolidation-adw.md`
**Status**: ACTIVE

**Steps**:
1. **Cartographie** (Architect Mode - Gemini) — Analyze area, create migration spec
2. **Delegation Tactique** (Execution Mode - Nova) — Execute via CLI with strict inline prompt
3. **Verification** — Verify results via list_dir

**Guard-rails**: Strict table of operations (Source, Action, Target). YOLO mode (`--dangerously-skip-permissions`) for batch execution.

**Decision points**: Phase 1 (migration spec review before execution).

**Unique value**: Multi-model workflow (Gemini architects, Nova executes). "The Plan is the Prompt" philosophy. Batch execution pattern.

**Scope**: Workspace taxonomy restructuring.

---

### WF-16: Task Routing Protocol

**Location**: `/home/director/omar/intent/workflow/task-routing-protocol.md`
**Status**: ACTIVE

**Structure**: Decision tree routing work to Linear / TASKS.md / Native tasks based on lifecycle and scope.

**Unique value**: Clear boundary between Linear (permanent, strategic), TASKS.md (permanent, operational), and Native tasks (ephemeral, session-scoped). Reference pattern (TASKS.md → Linear, not reverse).

**Scope**: Work routing — where to track work.

---

### Workflow-Adjacent Skills

**Decide Skill** (`~/omar/core/resources/skills/decide/SKILL.md`): 11-step structured decision analysis with weighted scoring, sensitivity analysis, Type 1/Type 2 reversibility classification, and Option 0 (Status Quo) mandate.

**Orchestrate Skill** (`~/omar/core/resources/skills/orchestrate.md`): 5-step delegation assessment (I/O size, independence, perspectives, stakes → SOLO/SUB-AGENTS/TEAM recommendation).

**Framework Evaluation** (`~/omar/core/resources/skills/framework-evaluation.md`): 3-phase tech evaluation (Pre-steps → Build → Document) with mandatory demo preservation and adoption verdict.

**WOS Skill** (`~/omar/core/resources/skills/wos/SKILL.md`): 4-layer routing (Command/Execution/Continuity/Governance) with work type and information routing tables.

---

## 3. Gap Analysis

### What is MISSING across all workflows

| Gap | Description | Which workflows miss it | Impact |
|-----|-------------|------------------------|--------|
| **G1: Session lifecycle** | No workflow covers session start → work → session close as a unified flow | All except Kael (WF-03) which has RECEIVE + POP check | Context lost between sessions; no handoff discipline in most workflows |
| **G2: Failure/rollback** | Only WF-11 (Reservation) has error recovery. Others assume success. | WF-01–WF-10, WF-14–WF-16 | When execution fails, agents improvise instead of following a recovery protocol |
| **G3: State persistence** | Only WF-02 (SYNC) and WF-03 (TASKS.md UPDATE) explicitly persist state changes. Others treat persistence as implicit. | WF-01, WF-04, WF-05, WF-06 | Knowledge and decisions lost at compaction |
| **G4: Scope declaration** | Focus Guardian (rules.md) requires session scope, but no workflow embeds it as a phase. | All 16 workflows | Drift goes undetected because scope was never declared |
| **G5: Cross-session continuity** | Only WF-03 (Kael) has HANDOFF. Others end without ensuring next session can resume. | WF-01, WF-02, WF-04–WF-16 | Every new session starts with archaeology |
| **G6: Business operations workflow** | Unified Guide (WF-04) lists "Business" as TBD. Guest comms (WF-12) is archived. No active business ops workflow. | All — only archived domain workflow exists | Villa Thaifa's core work (guest interaction, owner updates) has no active workflow |
| **G7: Mode-awareness** | CLAUDE.md defines 6 modes with 48 behavioral rules, but no workflow adapts its ceremony to the mode. | All 16 workflows | Low-energy Omar gets the same 5-phase ceremony as high-energy Omar |
| **G8: Learning/retrospective** | Only WF-06 (Dev Workflow) has a retrospective template. No other workflow captures lessons. | WF-01–WF-05, WF-07–WF-16 | Same mistakes repeated because lessons are never extracted |
| **G9: Parallel execution** | Only WF-07 (Agent Lifecycle) and WF-08 (ERV) address parallel work. Others are purely sequential. | WF-01–WF-06, WF-09–WF-16 | Serialization wastes Omar's time |
| **G10: Token/cost awareness** | Only WF-07 and WF-08 mention model cost. The rest are cost-blind. | WF-01–WF-06, WF-09–WF-16 | Expensive models used for trivial tasks |

---

## 4. Overlap Analysis

### What is DUPLICATED across workflows

| Overlap | Workflows | Nature of duplication | Resolution |
|---------|-----------|----------------------|------------|
| **O1: SCOUT/REPORT/QUESTIONS/ACTION ≈ Frame/Research/Plan/Execute** | WF-02 (VT Mandatory) vs WF-04 (Unified Guide) | Same 4-phase pattern with different names. SRQA is VT-specific language; FRPE is universal. | SRQA is a VT instantiation of the universal FRPE. Should be explicit: "VT uses SCOUT=Frame, REPORT=Research, QUESTIONS=Plan, ACTION=Execute." |
| **O2: COMPRENDRE/EXPLORER/CLARIFIER ≈ Frame/Research/Plan** | WF-01 (Original Core Loop) vs WF-04 (Unified Guide) | French-named original, English-named successor. | Resolved — WF-01 is archived. But the 94% confidence gate from WF-01 was lost in the transition. |
| **O3: Verify phase** | WF-04, WF-06, WF-07, WF-08 all have Verify | All use "two-stage review (spec compliance + quality)" from Superpowers. Identical logic in 4 places. | Define Verify ONCE, reference everywhere. |
| **O4: Delegation decision tree** | WF-03 (Kael DELEGATION CHECK), WF-04 (Phase 4 decision tree), WF-07 (Phase 2 Decide), Orchestrate skill | Same logic: "Can a sub-agent do this? Is it quick? Is it parallel?" — defined 4 times. | Single canonical decision tree, referenced by all. |
| **O5: Human-in-the-loop gate** | WF-01 (CLARIFIER), WF-02 (QUESTIONS), WF-04 (gates), WF-06 (phase gates), WF-10 (CONFIRM), WF-11 (REPEAT BACK) | Every workflow has "wait for Omar" but with different triggers and formats. | Standardize gate types: ACKNOWLEDGE (Omar sees it), APPROVE (Omar says yes), DECIDE (Omar chooses from options). |
| **O6: Task graph/tracking** | WF-03 (TASKS.md UPDATE + GHOST DETECTION), WF-04 (Plan phase TaskCreate), WF-08 (GRAPH step), WF-16 (Task Routing) | Four different descriptions of how to track work. | WOS skill should be the single routing authority. |
| **O7: Pricing workflow** | WF-10 (active, English) vs WF-13 (archived, French) | Exact same workflow, different language and paths. | Already resolved — WF-13 archived. But the active WF-10 still references old paths. |

---

## 5. Synthesis

### What the Unified Core Workflow MUST Include

Based on analyzing 16 workflows, 4 skills, and 8 governance-embedded processes:

#### 5.1 Universal Phases (the core skeleton)

The 5-phase structure from WF-04 (Unified Guide) is the strongest candidate because it already maps to all 5 work types. But it needs augmentation from the gaps:

```
SESSION START (from WF-03 Kael: scope declaration + context load)
  ↓
1. FRAME (from WF-04: understand WHY + WHAT)
     Absorbs: COMPRENDRE, SCOUT, RECEIVE, PARSE
  ↓
2. RESEARCH (from WF-04: gather context)
     Absorbs: EXPLORER, REPORT, DISCOVER, BASELINE
  ↓
3. PLAN (from WF-04: define HOW)
     Absorbs: CLARIFIER, QUESTIONS, PLAN & DESIGN, TRIAGE, GRAPH
  ↓
4. EXECUTE (from WF-04: build it)
     Absorbs: EXECUTER, ACTION, EXECUTE (TDD), LAUNCH+MONITOR+COLLECT
  ↓
5. VERIFY (from WF-04: confirm quality)
     Absorbs: VERIFIER, VERIFY, CONFIRM, REVIEW, VALIDATE
  ↓
6. SYNC (from WF-02 VT Mandatory: persist + propagate changes)
     Absorbs: UPDATE DATA, TASKS.md UPDATE, HANDOFF, INTEGRATE, CLOSE
     NEW — not in WF-04 but critical (G3, G5)
  ↓
SESSION CLOSE (from WF-03 Kael: handoff + ghost detection)
```

#### 5.2 Cross-cutting Engines (invoked WITHIN phases, not phases themselves)

| Engine | When invoked | Source |
|--------|-------------|--------|
| **Thinking Cycle** (WF-05) | Within any phase for non-trivial problems | Frame→Research→Evaluate→Ground→Re-evaluate→Design |
| **Agent Lifecycle** (WF-07) | Within Execute phase for delegation | Trigger→Decide→Brief→Launch→Monitor→Collect→Verify→Dissolve→Integrate |
| **Delegation Decision Tree** | Before any execution | Solo / Sub-agent / Team |
| **Mode Calibration** | Modulates ceremony at every phase | CLAUDE.md Mode System |

#### 5.3 Guard-rail Categories (unified from all workflows)

| Category | Best examples | Must include |
|----------|-------------|-------------|
| **Confidence gates** | WF-01 (94% threshold), WF-11 (90% on fields) | Measurable confidence check before execution |
| **Human-in-the-loop** | WF-02 (QUESTIONS), WF-10 (CONFIRM), WF-11 (REPEAT BACK) | Three gate types: ACKNOWLEDGE, APPROVE, DECIDE |
| **Context protection** | WF-03 (CONTEXT BURN, >50% window) | Hard stop when context window is at risk |
| **Delegation enforcement** | WF-03 (DELEGATION CHECK), rules.md (200r/100w threshold) | Self-check before every tool call |
| **State persistence** | WF-02 (SYNC checklist), WF-03 (TASKS.md UPDATE + GHOST DETECTION) | Every state change persisted, verified |
| **Quality assurance** | WF-04 (two-stage review), WF-08 (ERV phased remediation) | Spec compliance + quality review |
| **Safety net** | universal.md (Zero-Loss Operations) | Read before modify, verify after, backup before mutate |
| **Anti-drift** | rules.md (Focus Guardian Protocol) | Session scope declaration + drift detection |

#### 5.4 What Should Be DROPPED

| Drop | Reason |
|------|--------|
| Kael's 20+ named guardrails as separate items | Consolidate into categories (5.3). Individual guardrails like MARATHON COMPLETION and QUESTION TAX are behavioral training, not workflow phases. |
| French-language duplicate workflows | Already archived. Keep English canonical versions only. |
| Platform-specific steps (HotelRunner login, Booking.com check) | These are domain workflow details, not Core Workflow content. They belong in domain-specific skill docs. |
| POP CHECK ceremony from Kael | Session start context should come from manifest.json + MEMORY.md + handoff, not a separate "POP" file. |

#### 5.5 Top 5 Insights

1. **There are 3 competing "universal" workflows** — the Original Core Loop (archived), the VT Mandatory Workflow (active in AGENTS.md), and the Unified Guide (active in intent/workflow/). They use different phase names for the same logic (SCOUT=Frame, REPORT=Research, etc.) but nobody has ever explicitly mapped them to each other.

2. **The biggest gap is SYNC** — Phase 5 (Verify) exists everywhere, but the "propagate changes to all impacted files" step only exists in VT's AGENTS.md. The Unified Guide jumps from Verify to done. This is why data drift is a persistent problem.

3. **The Thinking Cycle is the most underused asset** — A 6-phase cognitive engine backed by research of 15 frameworks, but only referenced in the Unified Guide as a "domain workflow reference." It should be the cognitive engine invoked WITHIN every non-trivial phase, not a sibling document.

4. **Mode-awareness is completely absent from workflows** — CLAUDE.md defines 48 behavioral rules across 6 modes, but zero workflows adapt. A low-energy session should skip Phase 2 (Research) for known domains. A focused session should collapse Phase 1 (Frame) to a single line. This adaptation is documented in CLAUDE.md's mode table but never operationalized in any workflow.

5. **The Kael Core Loop is the most complete but least portable workflow** — Its 10 phases + 20+ guardrails cover session lifecycle, delegation, task tracking, ghost detection, and handoff — all gaps in other workflows. But it is deeply embedded in Kael's identity prompt and not referenced by any other system. Extracting its unique innovations (GHOST DETECTION, MARATHON COMPLETION, SESSION CLOSE delegation) into the unified Core Workflow would be the highest-leverage improvement.

---

_Research complete. 16 workflows cataloged. 10 gaps identified. 7 overlaps documented. Synthesis provides the skeleton for a unified Core Workflow._

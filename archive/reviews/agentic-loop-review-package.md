# Agentic Loop — External Review Package

**Prepared for**: Independent AI systems architect review
**Date**: 2026-02-23
**Version**: 0.1 (proposal stage — pre-implementation)

---

## Section 1: Context

The **Agentic Loop** is a unified operational workflow for a human-AI partnership where one human (Omar) works with multiple AI CLI tools (Claude Code, Gemini CLI, Codex CLI) as orchestrators across personal and professional domains. It replaces 16 fragmented workflows that accumulated over 3 months of organic growth — each addressing a real need but creating overlapping phase names, duplicated guard-rails, and inconsistent ceremony.

The human operates in **6 energy/context modes** (normal, low-energy, high-energy, focused, review, emergency) that fundamentally change how much ceremony, interaction, and autonomy the workflow should provide. No published agentic framework addresses this — mode-awareness is the Agentic Loop's primary innovation.

The AI orchestrator's role is strictly non-executing: it delegates all work to sub-agents that operate in their own context windows, protecting the orchestrator's context from bloat. The orchestrator orients, plans, delegates, monitors, and verifies — it never writes code, reads large files, or produces deliverables directly.

The design synthesizes 16 internal workflows and external research across 14 sources covering OODA, ReAct, PDCA, Orchestrator-Worker, and Evaluator-Optimizer patterns.

---

## Section 2: The Agentic Loop Design

### 2.1 Architecture Overview

The Agentic Loop is a **PDCA shell** (Plan-Do-Check-Act as the outer structure) with an **OODA inner loop** (Observe-Orient-Decide-Act for rapid iteration within execution phases) and an **Evaluator gate** (Producer != Verifier as a structural invariant).

**Architectural Formula:**

```
Agentic Loop = PDCA(shell) + OODA(inner) + Evaluator(gate) + Mode(modulator) + SYNC(propagator)
```

Where:
- **PDCA** provides the audit trail and quality gates (ORIENT=Plan, EXECUTE=Do, VERIFY=Check, SYNC=Act)
- **OODA** provides rapid iteration within EXECUTE (ReAct thought-action-observation cycles)
- **Evaluator** enforces Producer != Verifier at the VERIFY gate
- **Mode** modulates ceremony, autonomy, and information density at every phase
- **SYNC** propagates state changes to all impacted files (the critical missing phase from all external frameworks)

### Design Principles

1. **6 phases, not 5** — SYNC is the critical missing phase (the #1 gap from internal research). It is a first-class citizen, not an afterthought.
2. **Session bookends** — ANCHOR (session start) and CLOSE (session end) are structural events, not phases. They bracket the loop.
3. **Mode modulation** — Every phase has a mode variant. The base workflow is the "normal" mode. Other modes compress, expand, or skip phases.
4. **Delegation-native** — The orchestrator's actions are explicitly listed per phase. Everything else is delegated.
5. **Engines, not phases** — The Thinking Cycle and Agent Lifecycle are cross-cutting engines invoked WITHIN phases, not competing workflows.
6. **Guard-rails attach to phases** — Every guard-rail has a home phase where it activates.

---

### 2.2 Phase Structure

```
SESSION START: ANCHOR (scope + context + mode)
    |
    v
1. ORIENT    — What & Why (understand intent, map work type, recommend approach)
    |
    v
2. SURVEY    — Gather context (audit state, check prior work, persist findings)
    |
    v
3. PLAN      — How & Who (define "done", decompose tasks, assign agents)
    |
    v
4. EXECUTE   — Delegate & Build (brief agents, launch, monitor, collect)
    |
    v
5. VERIFY    — Independent check (spec compliance + quality, producer != verifier)
    |          \
    |           --> FAIL: loop back to EXECUTE with fix instructions
    v
6. SYNC      — Propagate state (cascade updates, persist knowledge, commit)
    |
    v
SESSION END: CLOSE (ghost scan, handoff, persist learnings, next priorities)
```

**Skip conditions:**
- Trivial task -> skip from ORIENT directly to EXECUTE
- Known domain, fresh context -> skip SURVEY, go to PLAN
- VERIFY fail -> loop back to EXECUTE (not restart from ORIENT)

---

### 2.3 Phase Details

#### SESSION BOOKEND: ANCHOR

**Purpose**: Establish session scope, load context, set mode — creating the Focus Anchor that all drift detection measures against.

| Step | Action |
|------|--------|
| 1 | Read current mode (energy/context state) |
| 2 | Read relevant handoff from prior session |
| 3 | Read work overview for current priorities |
| 4 | Declare or confirm session scope |
| 5 | Confirm: "Session scope: [X]. Mode: [Y]. Proceeding." |

**Exit Criteria**: Scope declared. Mode set. Context loaded.

**Anti-patterns**:
- Starting work without declaring scope (drift becomes undetectable)
- Reading 10+ files at ANCHOR (context burn before work starts)
- Asking "What do you want to work on?" when the priority list has clear P0/P1 items

---

#### PHASE 1: ORIENT

**Purpose**: Understand WHAT is being asked and WHY it matters — before touching anything.

| Step | Action | Who |
|------|--------|-----|
| 1 | Parse human's intent (explicit + implicit) | Orchestrator |
| 2 | Map to work type (Development / Research / Operations / Business / Creative) | Orchestrator |
| 3 | Identify 2-3 approaches, recommend 1 | Orchestrator |
| 4 | Surface decisions requiring human judgment NOW | Orchestrator |

**Exit Criteria**: Human validates direction (or orchestrator proceeds per autonomy tier).

**Anti-patterns**:
- Jumping to execution without understanding WHY (tunnel vision)
- Asking 5 questions at once (question tax)
- Presenting a menu without a recommendation (decision burden on human)
- Researching during ORIENT (that is SURVEY's job)

**Skip condition**: Trivial task (typo fix, obvious next step) -> skip to EXECUTE.

---

#### PHASE 2: SURVEY

**Purpose**: Gather context — know what exists before building.

| Step | Action | Who |
|------|--------|-----|
| 1 | Check prior work (knowledge bases, decision records) | Orchestrator (light scan) or sub-agent (deep audit) |
| 2 | Audit current state of relevant files/code/configs | Sub-agent (delegated) |
| 3 | Identify constraints, dependencies, blockers | Orchestrator (synthesizes) |
| 4 | Persist findings to knowledge directory | Sub-agent |

**Exit Criteria**: Enough context to plan. Findings persisted (not just in chat).

**Anti-patterns**:
- Research rabbit holes (timebox to 5-10 min for standard tasks)
- Researching only in chat (lost at context compaction — findings MUST go to files)
- Orchestrator reading 200+ lines directly (delegate)
- Re-researching what already exists in knowledge files

**Skip condition**: Known domain where prior work is fresh and accessible -> skip to PLAN.

---

#### PHASE 3: PLAN

**Purpose**: Define HOW the work will be done, WHO does each part, and WHAT "done" looks like — before executing anything.

| Step | Action | Who |
|------|--------|-----|
| 1 | Define "done" criteria (TDD: define done before starting) | Orchestrator |
| 2 | Decompose into tasks (2-5 min each for dev work) | Orchestrator or planning agent |
| 3 | Assign: solo (orchestrator) / sub-agent / team / external CLI | Orchestrator |
| 4 | Surface ALL decisions requiring human input before execution | Orchestrator |
| 5 | Produce plan artifact (for complex work) | Orchestrator or agent to file |

**Exit Criteria**: Human approves plan (or orchestrator proceeds per autonomy tier). Every task has: what to do, who does it, expected outcome, verification method.

**Anti-patterns**:
- Plans only in chat (lost at compaction)
- Vague tasks ("implement auth" instead of "add JWT middleware to /api/auth")
- No expected outcomes (untestable tasks)
- Launching execution agents in parallel with planning agents (respect the dependency graph)

**Delegation Decision Tree:**

```
Single focused task?
  YES -> Quick (<2 min)? -> Do inline : Sub-agent
  NO  -> Tasks independent? -> Parallel sub-agents : Dependent? -> Sequential chain : Team
```

**Hard rule**: >200 lines to read OR >100 lines to write = sub-agent. No exceptions.

**Skip condition**: Trivial task where the plan IS the task (e.g., "fix the typo in line 42").

---

#### PHASE 4: EXECUTE

**Purpose**: Build it. The orchestrator delegates and monitors. Sub-agents execute in their own context windows.

| Step | Action | Who |
|------|--------|-----|
| 1 | Brief sub-agents (Goal, Context, Scope, Output, Constraints, References) | Orchestrator |
| 2 | Include safety block in every agent prompt | Orchestrator |
| 3 | Launch agents (parallel when independent, sequential when dependent) | Orchestrator |
| 4 | Monitor: check for blockers, confidence-gate escalations | Orchestrator |
| 5 | Collect results (agent writes to file, reports path + summary) | Orchestrator |

**Exit Criteria**: All planned tasks completed. Agent output in files (not chat). Ready for verification.

**Anti-patterns**:
- Orchestrator writing code directly
- Orchestrator reading 200+ lines (context burn)
- "Just one quick edit" x 5 = bulk work that should have been 1 sub-agent (batching rule)
- Briefing agents from memory instead of reference files
- Using general-purpose agent when a specialist exists

**Mandatory Safety Block** (included in every agent prompt):

```
SAFETY — MANDATORY, NON-NEGOTIABLE:
- Read every file before modifying it
- Verify every file after modifying it
- For moves: confirm content at destination BEFORE removing source
- For deletes: confirm content preserved elsewhere FIRST
- If unsure about ANY operation: STOP and report back. Do NOT guess.
- ZERO data loss tolerance. When in doubt, preserve.
```

---

#### PHASE 5: VERIFY

**Purpose**: Independently confirm that the work meets the "done" criteria defined in PLAN. The producer is NEVER the verifier.

| Step | Action | Who |
|------|--------|-----|
| 1 | **Stage 1 — Spec Compliance**: Did the work match the plan? Anything missing? Anything extra? | Verification agent |
| 2 | **Stage 2 — Quality**: Is the output accurate, well-structured, integrated? Red flags? | Verification agent or human |
| 3 | Compare key facts against source data (not agent self-report) | Verification agent |
| 4 | Surface gaps as structured summary (not full output) | Orchestrator |

**Exit Criteria**:
- PASS: Both stages clear. Advance to SYNC.
- FAIL: Issues found. Loop back to EXECUTE with specific fix instructions.

**Anti-patterns**:
- Self-verification (producer = verifier — systematically biased)
- Skipping because "tests pass" (tests cover code, not intent)
- Reviewing only the last commit (must verify against full plan scope)
- Trusting agent's self-reported "success" without reading the file

---

#### PHASE 6: SYNC

**Purpose**: Propagate all state changes to every impacted file, persist knowledge, update tracking systems, and commit. This is the anti-drift phase.

| Step | Action | Who |
|------|--------|-----|
| 1 | **Impact Scan**: "What files are impacted by this change?" | Orchestrator (judgment) |
| 2 | **Cascade Update**: Update all impacted files | Sub-agent (delegated for >3 files) |
| 3 | **Knowledge Persist**: Extract decisions, learnings to canonical locations | Orchestrator (routes) + sub-agent (writes) |
| 4 | **Task Update**: Update tracking systems | Orchestrator |
| 5 | **Commit**: Changelog + git commit | Orchestrator |

**SYNC Checklist** (universal):

| If you changed... | Also update... |
|---|---|
| A decision was made/resolved | Decision records, conflict registries, status dashboards |
| Data files (any domain) | Status/truth files, reconciliation logs |
| A conflict was resolved | Conflict registry, status dashboards |
| Repository structure | Structure documentation |
| A rule or governance file | All references to that rule |
| Knowledge was gained | Research directories, skill files, or memory service |
| A task was completed | Work overview, issue tracker |
| A handoff is needed | Handoff file, status dashboard |

**Exit Criteria**: All impacted files updated. Search for old values confirms zero remaining occurrences. Commit successful.

**Anti-patterns**:
- Skipping SYNC ("the task is done, why bother?") — this is how data drift happens
- Partial cascade (updating the primary file but not cross-references)
- Committing without changelog
- Forgetting to update work overview

---

#### SESSION BOOKEND: CLOSE

**Purpose**: Ensure the next session (or next agent instance) can resume without archaeology.

| Step | Action |
|------|--------|
| 1 | **Ghost Scan**: Check for untracked work items in conversation |
| 2 | **Handoff**: Write/update handoff file (what was done, what remains, blockers) |
| 3 | **Persist**: Store durable learnings to memory service |
| 4 | **Mirror**: Session review — drift count, patterns, cost |
| 5 | **Next priorities**: Surface top 2-3 from work overview |

**Exit Criteria**: Handoff file exists. No ghost items. Next session can start from ANCHOR without guesswork.

**Anti-patterns**:
- Ending a session without a handoff (next session starts with archaeology)
- Skipping ghost scan (untracked work = lost work)

---

### 2.4 Mode Modulation Table

The base workflow is the "normal" mode. Other modes compress, expand, or skip phases. This is the primary innovation — no published framework has this.

#### Phase Behavior by Mode

| Phase | normal | low-energy | high-energy | focused | review | emergency |
|-------|--------|------------|-------------|---------|--------|-----------|
| **ANCHOR** | Full 5-step. Confirm scope. | Read handoff + mode. Propose scope. Launch. | Full + share reasoning on scope choice. | 1-line scope from context. "Continuing [X]." | Full + enumerate pending reviews. Wait for pick. | Skip. Infer scope from message. Act. |
| **ORIENT** | 2-3 approaches, recommend 1. Wait for "go". | 1 recommendation only. "Doing [X]. Starting." | All approaches with scored matrix. Discuss. | Infer from context. 1-liner. Execute. | All approaches with weighted scoring. Wait. | Skip. Best approach. Execute. |
| **SURVEY** | Delegate to researcher agent. Review summary. | Skip if domain known. Otherwise: 1 quick scan. | Full research + share findings. Discuss. | Skip if domain known. Minimal scan otherwise. | Full survey. Present all findings before planning. | Skip entirely. Act on available context. |
| **PLAN** | Plan -> approve -> execute. Quality > speed. | Lightweight plan. Internal only. Speed ~= quality. | Full plan + rationale. Co-define done with human. | Plan silently. Execute. Speed + quality. | Detailed plan for approval. Quality >> speed. | No plan. Act on best judgment. Document after. |
| **EXECUTE** | Delegate >200r/100w. Track all tasks. | Delegate aggressively. Coarse tracking. | Fine-grained tracking. Share agent progress. | Silent agents. Minimal tracking. Max autonomy. | Standard tracking. Decisions at orchestrator level. | Maximum autonomy. Skip optional steps. Speed >> quality. |
| **VERIFY** | Two-stage review. Report at milestones. | Quick verify. End of batch. Auto-proceed if clean. | Full two-stage + discuss findings. After each step. | Zero mid-work checkpoints. Summary at end. | Full two-stage after each decision. Wait for approval. | Skip if reversible. Ship, then verify. |
| **SYNC** | Full checklist. Commit proactively. | Minimal sync (task update + commit). Deep cascade deferred. | Full + explain what was updated and why. | Auto-sync. Silent commit. Zero discussion. | Full. Enumerate all updates for review before commit. | Skip optional syncs. Commit essentials. Log what was skipped. |
| **CLOSE** | Full 5-step. | Steps 1-3 only. Skip Mirror. Brief handoff. | Full + retrospective (what went well/didn't). | Minimal: handoff + ghost scan. No discussion. | Full + session quality assessment. | Skip. Log "CLOSE skipped — emergency" in handoff. |

#### Human-in-the-Loop Gates by Mode

| Mode | ORIENT Gate | PLAN Gate | VERIFY Gate |
|------|-------------|-----------|-------------|
| normal | APPROVE | APPROVE | ACKNOWLEDGE |
| low-energy | — (auto) | — (auto) | — (auto, end of batch) |
| high-energy | APPROVE | APPROVE | APPROVE |
| focused | — (auto) | — (auto) | — (auto, summary at end) |
| review | DECIDE | APPROVE | APPROVE |
| emergency | — (auto) | — (auto) | — (auto) |

**Gate types:**
- **ACKNOWLEDGE** — Human sees the output. No explicit approval needed.
- **APPROVE** — Human says "go" or equivalent. Work stops until approval.
- **DECIDE** — Human chooses from presented options.

---

### 2.5 Cross-Cutting Engines

These are NOT phases. They are cognitive or operational engines invoked WITHIN phases as needed.

#### Thinking Cycle (Cognitive Engine)

A 6-phase internal reasoning process invoked for non-trivial problems:

| Agentic Loop Phase | Thinking Cycle Phase(s) Used |
|---|---|
| ORIENT | Frame |
| SURVEY | Research |
| PLAN | Evaluate + Ground |
| EXECUTE | Ground (does execution match plan?) |
| VERIFY | Ground + Re-evaluate |

Rule: Mandatory scoring (0-10) when the Thinking Cycle is invoked. No gut feelings.

#### Agent Lifecycle (Delegation Engine)

A 9-phase agent management process invoked within EXECUTE (and sometimes VERIFY):

Trigger -> Decide -> Brief -> Launch -> Monitor -> Collect -> Verify -> Dissolve -> Integrate

Each phase maps back to the Agentic Loop: Trigger from PLAN, Verify feeds into VERIFY, Integrate feeds into SYNC.

#### Focus Guardian (Drift Engine)

Continuous — active at ALL phases. Measures every action against the Focus Anchor declared at ANCHOR.

| Signal | Level | Intervention |
|---|---|---|
| Topic switch | NUDGE | "Captured to [destination]. Back to [session scope]." |
| Scope expansion | NUDGE | "Captured to [destination]. Back to [session scope]." |
| Rabbit hole (3rd tangent follow-up) | FLAG | "Second tangent this session. Complete [current task]." |
| Complexity spiral | FLAG | "Adding layers to simple problem. Returning to [task]." |
| Analysis paralysis | BLOCK | "FOCUS CHECK: [X] messages on [tangent]. Parking. Returning to [task]." |

#### Confidence Gate (Escalation Engine)

Active at any point during any phase when the agent encounters uncertainty.

Three escalation triggers:
1. **Confidence threshold breach** — uncertainty exceeds acceptable level
2. **Scope boundary encounter** — task touches something outside declared scope
3. **Structural failure** — tool failure, API error, system unavailable

Mandatory escalation package:
- What the agent was trying to accomplish (goal)
- What it has done so far (progress)
- What it needs from the human (specific ask)
- Why it cannot proceed alone (blocker)
- What the default action would be (recommendation)

---

### 2.6 Guard-Rail Inventory

Every guard-rail has a HOME PHASE where it primarily activates, plus phases where it may also fire.

| Guard-Rail | Home Phase | Trigger | Action |
|---|---|---|---|
| **SCOPE ANCHOR** | ANCHOR | No session scope declared | STOP. Declare scope before proceeding. |
| **CONTEXT BURN** | EXECUTE | >50% context window on single task | STOP. Delegate or handoff. |
| **DELEGATION CHECK** | EXECUTE | About to execute ANY work | STOP. Ask: "Can a sub-agent do this?" |
| **QUESTION TAX** | ORIENT | About to ask a trivial question | STOP. If obviously "yes" -> DO IT + notify. |
| **PLAN FIRST** | PLAN | Complex work starting without a plan | STOP. Plan before executing. |
| **PHASE GATE** | All transitions | Advancing without approval | STOP. Wait for explicit approval (mode-dependent). |
| **PRODUCER != VERIFIER** | VERIFY | Same agent verifying its own output | STOP. Spawn separate verification agent. |
| **CASCADE UPDATE** | SYNC | Data edited but cross-references not checked | STOP. Search for old value + related keywords. |
| **GHOST DETECTION** | CLOSE | Untracked work items in conversation | STOP. Add to task tracker immediately. |
| **FOCUS DRIFT** | All | Drift signal detected | NUDGE/FLAG/BLOCK per graduated intervention. |
| **MEMORY BRIEF** | EXECUTE | About to brief agent from memory | STOP. Read reference files first. |
| **TOOL MISMATCH** | EXECUTE | Using agents for deterministic tasks | STOP. Use scripts/code instead. |
| **WALL OF TEXT** | All | About to output >30 lines in chat | STOP. Write to file, link it. |
| **NO EVIDENCE** | VERIFY | Claiming "done" without proof | STOP. Provide proof first. |
| **ZERO LOSS** | EXECUTE | About to modify/move/delete without safety net | STOP. Create safety net first. |
| **COMPLETION INTEGRITY** | VERIFY | Marking done when not ALL requirements met | STOP. Verify against original scope. |

---

### 2.7 Domain Examples

#### Example 1: Hotel Booking Fix (Operations)

A guest reports their booking dates are wrong on the channel manager. The human asks the AI to fix it.

| Phase | What Happens |
|---|---|
| **ANCHOR** | Mode: normal. Scope: "Fix booking date discrepancy for guest [X]." |
| **ORIENT** | Parse message. Work type: Operations. Straightforward fix — no alternatives needed. |
| **SURVEY** | Sub-agent reads booking data. Browser agent checks channel manager. Report: "Booking shows Jan 15-18, channel manager shows Jan 15-17. Discrepancy: checkout date." |
| **PLAN** | (1) Update channel manager checkout to Jan 18, (2) Verify propagation to OTA, (3) Update local booking data. "Done" = all three systems show Jan 15-18. |
| **EXECUTE** | Browser agent updates channel manager. Wait for propagation. Browser agent checks OTA. Sub-agent updates local data. |
| **VERIFY** | Verification agent reads all 3 locations. Confirms all show Jan 15-18. PASS. |
| **SYNC** | Update reconciliation log. Update status file. Commit. |

**Mode variant**: In emergency mode, SURVEY and PLAN collapse — go straight to EXECUTE. In review mode, human sees the plan and approves before any platform changes.

#### Example 2: Code Feature (Development)

Human wants to add a validation script that checks data profiles against a template.

| Phase | What Happens |
|---|---|
| **ANCHOR** | Mode: normal. Scope: "Build profile validation script." |
| **ORIENT** | Work type: Development. Approaches: (A) Python + pytest, (B) Bash + regex, (C) JSON Schema. Recommend A. Human: "Go." |
| **SURVEY** | Sub-agent audits: template (the schema), 12 profile instances, existing audit patterns. Findings persisted to knowledge file. |
| **PLAN** | Tasks: (1) Parse template into field list, (2) Parse each profile, (3) Compare fields, (4) Report discrepancies. TDD: test with known-good instance + deliberately broken fixture. "Done" = all profiles pass, test suite passes. |
| **EXECUTE** | Sub-agent with TDD skill: RED -> GREEN -> REFACTOR. Reports: "Script complete. 12/12 pass. 2 minor inconsistencies found." |
| **VERIFY** | Verification agent: reads script, runs tests, confirms 12/12 pass. Reads flagged profiles, confirms issues are real (not hallucinated). PASS. |
| **SYNC** | Add make target. Create tracking issues for flagged items. Update work overview. Changelog + commit. |

#### Example 3: Research Task

Human wants to evaluate 3 booking engine APIs before building an app.

| Phase | What Happens |
|---|---|
| **ANCHOR** | Mode: high-energy. Scope: "Evaluate booking engine APIs." |
| **ORIENT** | Work type: Research. Frame: "Which API best fits a 12-room property with multi-channel management?" Scoring criteria defined. Human adds a criterion. |
| **SURVEY** | 3 parallel researcher agents, one per API. Each writes to a knowledge file. |
| **PLAN** | Evaluation matrix: 3 APIs x 6 criteria. Collect reports, build comparison, demo top 2, recommend 1. |
| **EXECUTE** | Orchestrator reads 3 reports. Builds scored matrix. Top 2 identified. Demo agents spawned. |
| **VERIFY** | Human occupies the Evaluator role (high-energy mode). Reviews matrix, demos, reasoning. Asks probing questions. Decides: "Option A, but verify integration X actually works." -> loops back to EXECUTE. |
| **SYNC** | Decision record created. Planning docs updated. Work overview updated. Decision stored in memory service. Commit. |

---

### 2.8 Comparison with Predecessor Workflows

| Dimension | Predecessor Average | Agentic Loop |
|---|---|---|
| **Phases** | 5-6 (varies) | 6 phases + 2 bookends |
| **Session lifecycle** | None (except 1 of 16) | ANCHOR + CLOSE bookends |
| **State propagation** | 1 of 16 has SYNC | SYNC as Phase 6 (first-class) |
| **Mode-awareness** | 0 of 16 | Full mode modulation (every phase x 6 modes) |
| **Delegation model** | Implicit in most | Delegation-native (orchestrator actions explicit per phase) |
| **Verification model** | Self-verify OK in most | Producer != Verifier (mandatory separate agent) |
| **Focus/drift prevention** | 0 of 16 | Focus Guardian (structural, continuous, graduated) |
| **Guard-rails** | 1-3 each | 16 named, attached to specific phases |
| **Cross-session continuity** | 1 of 16 | CLOSE bookend (handoff, ghost scan, mirror) |
| **CLI portability** | Single-CLI | Universal (any AI CLI) |

---

### 2.9 Risk Assessment

| Risk | Likelihood | Impact | Mitigation |
|---|---|---|---|
| **Adoption resistance** — agents ignore the loop and follow training defaults | High | High | Embed reference in auto-loaded config. Guard-rail hooks enforce key phases. |
| **Over-ceremony** — low-energy human gets 6-phase ceremony | Medium | High | Mode modulation is structural, not optional. Low-energy compresses to 2-3 phases. |
| **Under-ceremony** — emergency mode skips critical SYNC | Medium | Medium | SYNC is never fully skippable. Even emergency mode does essentials + logs what was skipped. |
| **Complexity** — 6 phases + 2 bookends + 4 engines + 16 guard-rails overwhelms agents | Medium | Medium | The design doc is comprehensive; the implementation is a concise reference card (< 100 lines). |
| **CLI portability** — some CLIs cannot read the config file | Low | Medium | Canonical file lives in shared layer, not CLI-specific directory. |

---

## Section 3: What We're Asking

We want brutal, specific feedback on this design. Not politeness. Tell us what's wrong.

### Specific Questions

1. **Phase decomposition**: Is 6 phases + 2 bookends the right number? Too many? Too few? Are the boundaries between phases correct? Should any phases be merged or split?

2. **Mode modulation table**: Is it well-calibrated? Are there modes that are too similar? Is the "emergency" mode too aggressive in skipping phases? Is "low-energy" mode skipping too much or not enough?

3. **Blind spots**: What failure modes are we not seeing? What anti-patterns are we introducing with this design itself?

4. **What would you change, add, or remove?** Be specific — "I would merge SURVEY into ORIENT because..." or "I would add a Phase 2.5 for..."

5. **Comparison to state-of-the-art**: How does this compare to OODA, ReAct, PDCA, and modern agentic workflow patterns? Are we reinventing something that already exists in a better form? Are we missing patterns that have proven effective?

6. **Guard-rails**: Are 16 guard-rails too many? Are they at the right granularity? Are there important ones missing?

7. **SYNC as a first-class phase**: We believe state propagation being a mandatory phase (not an afterthought) is our strongest structural decision. Do you agree? Is there a better way to solve the data drift problem?

8. **Naming**: Is "Agentic Loop" the right name? Does it communicate the right things? Alternative candidates were "Core Loop" (overloaded) and "DRIVE Loop" (forced acronym).

9. **The engines concept**: Is treating the Thinking Cycle, Agent Lifecycle, Focus Guardian, and Confidence Gate as "cross-cutting engines" (invoked within phases) architecturally sound? Or should some of these be phases?

10. **Scalability**: This design assumes a single human + multiple AI orchestrators. How well does it scale if the human has a team? If there are multiple humans? If the AI orchestrators need to coordinate across sessions?

### Grounding Sources

The design was informed by external research on these frameworks and sources. Use them as reference points for your evaluation:

- Anthropic: "Building Effective Agents" (composable patterns, ground truth principle)
- Anthropic: "How We Built Our Multi-Agent Research System" (orchestrator-worker, context isolation)
- OODA Loop applied to agentic AI (EMA, Sogeti, Atlas SC)
- PDCA for AI code generation (InfoQ)
- ReAct pattern (Google Research / ICLR 2023)
- Evaluator-Optimizer pattern (Anthropic, Reflexion, Self-Refine)
- Vellum 2026 Guide to Agentic Workflows (architecture comparison)
- IBM: Agentic Drift (behavioral drift causes and detection)
- Tacnode: Context Drift (architectural mismatch, external state)
- Permit.io, Replicant, Zapier, Orkes: HITL best practices and escalation design
- glaforge: Agentic anti-patterns
- Concentrix: 12 failure patterns of agentic AI systems

---

**OVERALL SCORE: 6/10**

The design is ambitious and addresses real gaps (mode-awareness, SYNC-as-phase), but it suffers from **implementation-naive optimism** and **enforcement gaps**. The guard-rails are well-named but lack teeth. When agents inevitably drift or ignore rules, the system has no mechanical enforcement—only persuasive text. This is a specification, not a system.

---

**TOP 3 STRENGTHS** (what is genuinely good and should be preserved)

1. **Mode modulation table (§2.4)** — First-mover advantage. No published framework encodes human energy/context as a structural variable. The calibration of gate types (APPROVE vs ACKNOWLEDGE vs DECIDE) is genuinely useful and prevents the "one-size-fits-all" problem plaguing OODA/ReAct implementations.

2. **SYNC as Phase 6, not an afterthought** — Correct identification of the #1 failure mode in agentic systems: cascading staleness. Making state propagation mandatory with a concrete checklist is the strongest structural decision. Most frameworks say "update relevant files"; this one enumerates what "relevant" means.

3. **PRODUCER != VERIFIER as a structural invariant (§2.6, §2.3-VERIFY)** — This is borrowed from Anthropic's evaluator-optimizer pattern but made non-negotiable. The four verification anti-patterns (§2.3-VERIFY lines 239-244) are specific and correct.

---

**TOP 5 WEAKNESSES** (what is wrong, risky, or poorly designed)

**1. Guard-rails have no enforcement mechanism**

- **Problem**: All 16 guard-rails are described with "STOP" language (lines 399-414), but "STOP" is not a system primitive—it's text in a config file that an LLM may or may not follow. There's no mention of hooks, middleware, or programmatic enforcement.
- **Impact**: In practice, agents under time pressure or with competing training priorities will skip guard-rails. The design assumes compliance is the default; real systems assume non-compliance is the default.
- **Evidence**: Anthropic's "Building Effective Agents" (§When to Use Agents) explicitly warns: "Guardrails that rely on model behavior are unreliable." Production systems use code-enforced validation, not text instructions. The risk assessment (§2.9, line 487) acknowledges "agents ignore the loop and follow training defaults" as HIGH likelihood but offers "embed reference in auto-loaded config" as mitigation—that's documentation, not enforcement.
- **Suggested fix**: (1) Identify which guard-rails are enforceable via hooks (e.g., PHASE GATE, DELEGATION CHECK) and implement them as code. (2) For non-enforceable guard-rails, add a "guard-rail audit" phase in CLOSE that asks: "Which guard-rails fired this session? Which were skipped? Why?"

**2. Mode detection is undefined—human must self-report**

- **Problem**: The design depends on knowing the current mode (6 modes), but §2.4 and ANCHOR (§2.3) never explain HOW mode is determined. Is the human expected to self-declare? Is there a detection heuristic?
- **Impact**: If the human forgets to declare mode (or declares wrong), the entire behavioral dispatch table is misapplied. A "focused" human gets "normal" ceremony. An "emergency" human gets "normal" latency.
- **Evidence**: ANCHOR Step 1 says "Read current mode" (line 94) but doesn't say from where. The risk assessment (§2.9) doesn't list "mode mismatch" as a risk.
- **Suggested fix**: (a) Add explicit mode input mechanism (CLI flag, file, or explicit human declaration as part of ANCHOR Step 5). (b) Add mode-detection heuristics: message length, response latency, time-of-day patterns. (c) Add a "mode mismatch" guard-rail: "Human behavior suggests [X] mode but [Y] mode is active. Confirm?"

**3. SKIP conditions are subjective and easy to abuse**

- **Problem**: Multiple phases have skip conditions (ORIENT §2.3 line 128, SURVEY line 151, PLAN line 185) that rely on subjective judgment: "trivial task," "known domain," "fresh context." No objective criteria are provided.
- **Impact**: Agents under context pressure will interpret these loosely. "Trivial" expands. "Known" becomes assumption. The workflow degrades to "EXECUTE everything" because skipping is easier than justifying.
- **Evidence**: The delegation decision tree (§2.3-PLAN lines 177-182) provides concrete thresholds (>200r/100w lines), but skip conditions provide none. This asymmetry is telling.
- **Suggested fix**: (a) Define objective skip criteria: "Trivial = <5 lines changed AND no external dependencies AND <2 min estimated." (b) Require explicit skip logging: "Skipping [PHASE] because [CRITERION MET]." (c) Add a "skip audit" to CLOSE.

**4. Low-energy mode may hide problems from the human**

- **Problem**: Low-energy mode (§2.4, lines 310-318) auto-skips ORIENT, PLAN, and VERIFY gates. The human gets results without seeing the reasoning. This is intentional (reduce burden) but creates an **opaque system** where the human cannot catch agent errors.
- **Impact**: In low-energy mode, a subtly wrong assumption in ORIENT propagates through EXECUTE undetected because VERIFY is also auto. The human only sees the final output and may not have energy to question it. This is the "trusted advisor" failure mode—over-reliance on a system you can't inspect.
- **Evidence**: Mode modulation table shows low-energy has all three gates as "— (auto)". Emergency mode also has this, but emergency implies urgency > quality. Low-energy implies low-capacity, not low-stakes. The distinction matters.
- **Suggested fix**: (a) Add a "trust but verify" rule: in low-energy mode, the CLOSE phase MUST include a diff summary of what was done, not just "task completed." (b) Add a "low-energy risk acknowledgment" at ANCHOR: "Low-energy mode active. [X] phases will be auto. Confirm or upgrade to normal mode."

**5. The "orchestrator never executes" rule is idealistic and under-specified**

- **Problem**: The design insists "The orchestrator's role is strictly non-executing" (Section 1, line 15) and "orchestrator never writes code" (§2.3-PLAN line 183, EXECUTE line 204), but offers no mechanism to enforce this. Additionally, the delegation threshold (>200r/100w lines) creates a gray zone where small tasks are "allowed" to be done by the orchestrator—this is a loophole that will expand.
- **Impact**: The orchestrator will execute "quick" tasks to avoid spawning overhead. Context bloat happens incrementally. The 200r/100w threshold becomes 250/125 becomes 300/150. The protection erodes.
- **Evidence**: The safety block (§2.3-EXECUTE lines 212-220) is included in "every agent prompt" but not in orchestrator prompts—implying orchestrator execution doesn't need the same safeguards. This is inconsistent.
- **Suggested fix**: (a) Make the threshold hard, not soft: ANY write operation >0 lines to code/data files = sub-agent. No exceptions. (b) Add a "context budget" per session with enforcement. (c) Add an "orchestrator execution audit" to CLOSE that counts how many times orchestrator executed vs delegated.

---

**SUGGESTED CHANGES** (prioritized, most impactful first)

1. **Add programmatic enforcement for critical guard-rails**
   - **Priority**: P0
   - **Effort**: High
   - **Rationale**: Without hooks or middleware, the 16 guard-rails are documentation, not constraints. PHASE GATE, DELEGATION CHECK, and PRODUCER != VERIFIER should be enforced in code. This is the single biggest gap between design and implementation.

2. **Define mode detection mechanism**
   - **Priority**: P0
   - **Effort**: Medium
   - **Rationale**: Mode modulation is the primary innovation, but mode itself is undefined. Add: (a) explicit input mechanism, (b) detection heuristics, (c) mismatch guard-rail.

3. **Add objective skip criteria + logging requirement**
   - **Priority**: P1
   - **Effort**: Low
   - **Rationale**: Subjective skip conditions will be abused. Define thresholds, require logging, audit in CLOSE.

4. **Add "low-energy risk acknowledgment" and CLOSE diff summary**
   - **Priority**: P1
   - **Effort**: Low
   - **Rationale**: Low-energy mode hides too much. Force acknowledgment of what's being skipped. Force visibility of what was done (diff summary, not just "completed").

5. **Harden the "orchestrator never executes" rule**
   - **Priority**: P1
   - **Effort**: Medium
   - **Rationale**: The delegation threshold is soft and will erode. Make it absolute for writes. Add context budget. Add execution audit.

6. **Add "guard-rail audit" to CLOSE**
   - **Priority**: P1
   - **Effort**: Low
   - **Rationale**: CLOSE should include: "Which guard-rails fired? Which were skipped? Why?" This creates accountability for non-enforceable guard-rails.

7. **Separate "low-stakes" from "low-energy"**
   - **Priority**: P2
   - **Effort**: Medium
   - **Rationale**: Low-energy ≠ low-stakes. A tired human working on a critical task should have different protections than an energetic human working on a trivial task. Consider adding a "stakes" dimension orthogonal to "energy."

8. **Add failure mode: "mode oscillation"**
   - **Priority**: P2
   - **Effort**: Low
   - **Rationale**: What happens if human switches modes mid-session? Currently undefined. ANCHOR sets mode once. Add rule: mode change = re-ANCHOR or explicit mode-update event.

---

**ANSWERS TO SPECIFIC QUESTIONS**

**1. Is the phase decomposition sound? Too many? Too few? Wrong boundaries?**

6 phases is acceptable. The boundaries are mostly sound, but:
- **SURVEY and PLAN overlap in purpose**: SURVEY "identifies constraints" (line 140); PLAN "surfaces decisions" (line 164). Both gather information for execution. Consider whether SURVEY's constraint-identification belongs in PLAN.
- **ORIENT is thin**: 4 steps, all orchestrator, mostly about "understanding." In practice, this phase will be compressed or skipped because it feels like overhead.
- **ANCHOR/CLOSE as "bookends not phases" is semantic**: They have steps, exit criteria, and anti-patterns. They're phases. Calling them "bookends" doesn't change their nature.

**2. Is the mode modulation table well-calibrated?**

Partially. Issues:
- **low-energy and emergency are too similar**: Both skip all gates. The difference is in phase behavior (emergency skips SYNC optional; low-energy defers deep cascade). This is too subtle. Emergency should be more aggressive—consider collapsing to 3 phases (ORIENT → EXECUTE → minimal SYNC).
- **review mode is unclear on time expectations**: "Full survey. Present all findings before planning" sounds thorough but could take 30+ minutes. Is the human in review mode expecting that? Add time expectations per mode.
- **focused mode is underspecified**: "Silent agents. Minimal tracking. Max autonomy." This is the mode most likely to produce opaque results. Add a "focused mode debrief" in CLOSE.

**3. Are there blind spots or anti-patterns being introduced?**

Yes:
- **"Loop back to EXECUTE" on VERIFY fail (§2.3-VERIFY line 237)** creates an infinite loop risk if the fix doesn't address the root cause. Add: max loop count, escalation on repeated failure.
- **No concept of "session budget"**: Time, context, cost are all unbounded. A session could run forever in PLAN-EXECUTE-VERIFY loops.
- **No concept of "session interruption"**: What if human disappears mid-session? What if session times out? CLOSE assumes controlled exit.
- **ANCHOR assumes handoff exists**: "Read relevant handoff from prior session" (line 95). First session has no handoff. Add fallback behavior.

**4. What would you change, add, or remove?**

- **Add**: Session budget (time/context/cost), interruption handling, loop limits on VERIFY fail
- **Change**: Merge ORIENT's decision-surfacing into SURVEY, make ANCHOR/CLOSE explicit phases
- **Remove**: The distinction between "bookends" and "phases" is unnecessary; just call them all phases

**5. How does this compare to OODA, ReAct, PDCA, and modern agentic patterns?**

- **vs OODA**: Agentic Loop is more structured (6 phases vs 4) but loses OODA's speed advantage. The mode modulation is novel.
- **vs ReAct**: Agentic Loop doesn't have ReAct's thought-action-observation loop explicitly, though it's implied in EXECUTE's OODA inner loop. ReAct is simpler and thus more robust; Agentic Loop is more comprehensive but heavier.
- **vs PDCA**: The PDCA shell is a reasonable mapping (ORIENT=Plan, EXECUTE=Do, VERIFY=Check, SYNC=Act), but ANCHOR, SURVEY, and CLOSE are additions without PDCA equivalents.
- **vs Orchestrator-Worker (Anthropic)**: Agentic Loop's delegation model is similar, but Anthropic's system enforces delegation via context limits; Agentic Loop relies on rules.
- **Missing from external patterns**: The mode modulation is genuinely novel. The SYNC phase is also novel in its explicitness.

**6. Are 16 guard-rails the right number?**

16 is too many for an agent to reliably follow. Humans can't remember 16 rules; LLMs won't either. Recommendation:
- **Tier 1 (always enforceable, must implement as code)**: SCOPE ANCHOR, PHASE GATE, PRODUCER != VERIFIER, DELEGATION CHECK, ZERO LOSS (5)
- **Tier 2 (context-dependent, include in agent prompts)**: The remaining 11
- Consider consolidating: QUESTION TAX + WALL OF TEXT both concern output verbosity. FOCUS DRIFT + SCOPE ANCHOR both concern scope maintenance.

**7. Is SYNC as a first-class phase the right call?**

Yes. State propagation is the #1 failure mode in agentic systems. Making it mandatory is correct. The SYNC checklist (§2.3-SYNC lines 261-270) is specific and useful. The only improvement would be to add a "SYNC audit" in CLOSE: "Which SYNC items were updated? Which were skipped? Why?"

**8. Is "Agentic Loop" the right name?**

It's acceptable but generic. "Agentic" is overused. Alternatives:
- **HOODA** (Human-OODA) — emphasizes the human-in-the-loop
- **MODE Loop** — emphasizes the primary innovation
- **DRIFT Loop** — emphasizes the anti-drift focus
- **ANCHOR Loop** — emphasizes session scope

None are perfect. "Agentic Loop" is fine but doesn't communicate the mode-awareness innovation.

**9. Is the "engines" concept (cross-cutting processes invoked within phases) architecturally sound?**

Yes. Treating Thinking Cycle, Agent Lifecycle, Focus Guardian, and Confidence Gate as engines invoked within phases (not parallel workflows) is sound. However:
- **Focus Guardian should have enforcement hooks**: Currently it only "nudges" (line 369-373). Add: after 3 FLAGs, force PHASE GATE check.
- **Agent Lifecycle Phase 7 (Verify) conflicts with Phase 5 (VERIFY)**: The Agent Lifecycle has a "Verify" step (line 359) that feeds into Agentic Loop VERIFY. This naming collision is confusing. Rename one.

**10. How well does this scale beyond a single human + multiple AI orchestrators?**

Poorly. The design is explicitly single-human (Section 1, line 11). Scaling issues:
- **No coordination protocol for multiple humans**: If two humans work on the same repo, ANCHOR reads one handoff, CLOSE writes one handoff. Race conditions.
- **No session ownership**: Sessions are anonymous. If human A starts a session and hands off to human B, there's no tracking.
- **No multi-session serialization**: Two AI orchestrators working in parallel could conflict. The design assumes serial sessions.
- **CLOSE's "next priorities" (line 293)** is single-human: it surfaces top 2-3 from work overview, but doesn't consider what other humans/agents might be working on.

To scale: add session ownership, multi-session locking, shared priority coordination.

---

**COMPARISON TO STATE OF THE ART**

| Framework | What Agentic Loop Does Better | What Agentic Loop Does Worse | What It's Missing |
|-----------|-------------------------------|------------------------------|-------------------|
| **Anthropic "Building Effective Agents"** | Mode modulation, SYNC as phase, explicit anti-patterns per phase | Enforcement mechanisms, simpler mental model | Prompt chain patterns, router pattern |
| **Anthropic Multi-Agent Research System** | Focus Guardian, session lifecycle (ANCHOR/CLOSE) | Context isolation enforcement is weaker (relies on rules, not system limits) | Dynamic agent spawning, shared memory protocols |
| **OODA Loop (agentic)** | More comprehensive phase structure, mode-aware | Simplicity, speed | OODA's "tempo" concept—acting faster than opponent |
| **PDCA for AI code generation** | SYNC phase, Producer != Verifier | PDCA's iterative quality improvement focus | Explicit quality metrics |
| **ReAct** | More structured, mode-aware | Simplicity, robustness | ReAct's thought-action-observation loop is simpler to implement |
| **Vellum 2026 taxonomy** | Mode modulation, focus/drift prevention | Vellum's pattern catalog is more exhaustive | Memory patterns, tool use patterns |
| **IBM Agentic Drift** | Focus Guardian is a concrete implementation of drift detection | IBM's drift taxonomy is more formal | Drift metrics, drift thresholds |
| **Tacnode Context Drift** | ANCHOR/SCOPE ANCHOR addresses context drift | Tacnode's architectural analysis is deeper | External state management patterns |
| **HITL best practices (Permit.io, etc.)** | Mode-aware HITL, graduated interventions (NUDGE/FLAG/BLOCK) | HITL pattern catalog is more exhaustive | Async HITL patterns |
| **glaforge anti-patterns** | Specific anti-patterns per phase | glaforge's patterns are more focused on production failures | Failure mode catalog is smaller |
| **Concentrix 12 failure patterns** | SYNC phase addresses staleness, PRODUCER != VERIFIER addresses self-verification bias | Concentrix's patterns are more comprehensive | Missing: loop detection, resource exhaustion, cascading failures |

---

**ONE THING YOU WOULD SHIP DIFFERENTLY**

**Replace the 16 guard-rails with a smaller set of enforceable hooks + a session audit.**

Currently, the guard-rails are text instructions hoping for agent compliance. I would ship:
1. **5 code-enforced hooks**: SCOPE ANCHOR (block work without declared scope), PHASE GATE (block phase transition without approval per mode), DELEGATION CHECK (block orchestrator writes >0 lines), PRODUCER != VERIFIER (spawn separate agent for VERIFY), ZERO LOSS (block delete/move without confirmation)
2. **Session audit in CLOSE**: For all other guard-rails, CLOSE asks: "Did [GUARD-RAIL] fire? If no, why?" This creates accountability without requiring enforcement.

The current design optimizes for comprehensiveness. I would optimize for enforceability. A system with 5 enforced rules is more reliable than a system with 16 aspirational ones.

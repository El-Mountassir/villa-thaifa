# Research Brief: AI Agent Operational Workflow Best Practices

**Topic**: AI agent workflow patterns for human-AI partnership scenarios
**Researcher**: Nova (Claude Sonnet 4.6)
**Date**: 2026-02-23
**Scope**: Patterns, guard-rails, anti-patterns, and design principles for orchestrator-human workflows

---

## Executive Summary

The field has converged on several stable patterns since 2024. The most effective human-AI workflows are NOT monolithic loops — they are composable phases with explicit checkpoints, confidence-gated escalation, and adaptive behavior based on task type and human state. Anthropic's own architecture confirms: simplicity + clear orchestration + well-defined tools beats complexity every time. The deepest failure mode is not capability gaps but architectural ones: no checkpoint discipline, no scope contracts, and no agentic drift detection. For a human-partner scenario (Omar + Nova), the key insight is that the workflow must be bidirectional — AI adapts to the human's energy/focus, and the human receives structured escalations rather than noise.

---

## Key Findings

### Finding 1: Five Dominant Workflow Patterns

#### Pattern 1: OODA Loop (Observe-Orient-Decide-Act)
**Origin**: Colonel John Boyd, military strategy (Korean War).
**Application to AI**: The most popular base loop in production agentic systems.
**Phases**:
1. **Observe** — Gather context from environment, user inputs, external sources
2. **Orient** — Update internal model; analyze data; recall relevant knowledge
3. **Decide** — Select next action from available options
4. **Act** — Execute; produce output or call tool
5. (Implicit) **Loop** — Return to Observe with new state

**Key insight**: The Orient phase is the most important. Speed of orientation (how fast the agent updates its world model) determines competitive advantage. For AI: high-quality context engineering at this phase determines output quality.

**Strengths**: Fast iteration, adversarial resilience, continuously adaptive.
**Weaknesses**: Can sacrifice precision for speed; less auditable than PDCA; no explicit quality gate.
**Fit for human-AI partnership**: High — natural checkpoint at Decide phase for human intervention.

**Source**: [Agentic AI and the OODA Loop — EMA](https://www.ema.co/blog/agentic-ai/agentic-ai-and-the-ooda-loop-a-new-era-of-intelligent-collaboration), [Sogeti Global](https://www.sogeti.com/featured-articles/harnessing-the-ooda-loop-for-agentic-ai/), [Atlas SC — Cybernetic Recursion](https://atlassc.net/2026/02/13/cybernetic-recursion-ai-agent-loops)

---

#### Pattern 2: ReAct (Reasoning + Acting)
**Origin**: Google Research / ICLR 2023.
**Application**: Industry-standard loop for LLM agents with tool access.
**Phases**:
1. **Thought** — Internal reasoning trace: "I need to X because Y"
2. **Action** — Tool call or output generation
3. **Observation** — Result from tool/environment
4. (repeat)

**Key insight**: Interleaving reasoning with action reduces hallucination by grounding each reasoning step in actual tool results. The agent cannot advance its plan without real observations.

**Strengths**: Reduces hallucination; handles unpredictable tool outputs; highly adaptable; transparent reasoning trace.
**Weaknesses**: "Tunnel vision" risk — agent optimizes locally while losing global goal; sequential (not parallel by default); no hard quality gate.
**Fit for human-AI partnership**: Medium-High — reasoning traces provide auditability; humans can intervene at observation points.

**Source**: [ReAct — Anthropic's Building Effective Agents](https://www.anthropic.com/research/building-effective-agents), [Vellum 2026 Guide](https://www.vellum.ai/blog/agentic-workflows-emerging-architectures-and-design-patterns), [Atlas SC](https://atlassc.net/2026/02/13/cybernetic-recursion-ai-agent-loops)

---

#### Pattern 3: PDCA (Plan-Do-Check-Act) / Plan-and-Solve
**Origin**: W. Edwards Deming, industrial quality management.
**Application**: High-stakes, auditable AI workflows; code generation; structured tasks.
**Phases**:
1. **Plan** — Define scope, generate multi-step roadmap before any execution
2. **Do** — Execute plan step by step (small scale)
3. **Check** — Evaluate results against criteria; measure outcomes
4. **Act** — Adjust and iterate or close

**Key insight**: Forces upfront planning before execution, creating an audit trail and reducing long-horizon errors. The Check phase is explicit — not implicit like in OODA/ReAct.

**Strengths**: High auditability; explicit quality gate; reduces scope drift; well-understood by humans.
**Weaknesses**: Slower iteration; less adaptive to dynamic environments; overhead for simple tasks.
**Fit for human-AI partnership**: Very High — the Plan phase is a natural collaboration point; Check phase is a natural review/approval gate.

**Source**: [PDCA for AI Code Generation — InfoQ](https://www.infoq.com/articles/PDCA-AI-code-generation/), [Atlas SC](https://atlassc.net/2026/02/13/cybernetic-recursion-ai-agent-loops)

---

#### Pattern 4: Orchestrator-Worker (Hierarchical Multi-Agent)
**Origin**: Anthropic, LangGraph, production multi-agent systems.
**Application**: Complex research, multi-domain tasks, parallel execution.
**Phases**:
1. **Decompose** — Lead agent breaks query into subtasks with clear boundaries
2. **Delegate** — Assign subtasks to specialized workers with context + output format spec
3. **Execute (parallel)** — Workers operate in their own context windows simultaneously
4. **Evaluate** — Lead agent reviews worker outputs; identifies gaps
5. **Synthesize** — Compile into final output; spawn additional workers if gaps remain
6. **Cite/Verify** — Attribution or verification pass (optional dedicated agent)

**Key insight**: Workers having their own context windows (not sharing the lead's) is the key efficiency gain. This protects the orchestrator's context from bloat while enabling parallelism.

**Strengths**: Parallelism (up to 90% time reduction per Anthropic); specialization; context isolation; scales to complex tasks.
**Weaknesses**: 15x token cost vs single-agent; coordination overhead; harder to debug; non-deterministic paths.
**Fit for human-AI partnership**: High for complex tasks — human interacts with lead only; workers are invisible. Natural decision point: after Evaluate, before Synthesize.

**Source**: [Anthropic — How We Built Our Multi-Agent Research System](https://www.anthropic.com/engineering/multi-agent-research-system), [Vellum 2026 Guide](https://www.vellum.ai/blog/agentic-workflows-emerging-architectures-and-design-patterns)

---

#### Pattern 5: Evaluator-Optimizer (Iterative Refinement Loop)
**Origin**: Anthropic's composable workflow patterns; also used in Reflexion, Self-Refine.
**Application**: Quality-sensitive tasks where first output is rarely final (writing, code review, planning).
**Phases**:
1. **Generate** — Initial output from Generator agent
2. **Evaluate** — Separate Evaluator agent assesses against criteria (or human reviews)
3. **Feedback** — Structured critique with specific improvement targets
4. **Revise** — Generator incorporates feedback
5. (Repeat until criteria met or iteration limit)

**Key insight**: The Producer and Verifier must be SEPARATE agents (or human). Self-evaluation is systematically biased. The "Producer != Verifier" principle is the foundation of this pattern's value.

**Strengths**: Higher output quality; catches errors missed by generator; can be automated (LLM-as-Judge) or human-powered.
**Weaknesses**: Resource-intensive; risk of infinite loops without stopping criteria; needs clear evaluation rubric.
**Fit for human-AI partnership**: Very High — humans can occupy the Evaluator role, making this the most natural human-AI collaboration pattern. The human adds judgment; the AI adds execution speed.

**Source**: [Anthropic — Building Effective Agents](https://www.anthropic.com/research/building-effective-agents), [Vellum 2026 Guide](https://www.vellum.ai/blog/agentic-workflows-emerging-architectures-and-design-patterns)

---

### Finding 2: Comparison Matrix

| Pattern | Phases | Strengths | Weaknesses | Human-AI Fit | Best Task Type |
|---|---|---|---|---|---|
| **OODA Loop** | Observe → Orient → Decide → Act | Fast, adaptive, adversarial-resilient | Less auditable, speed over precision | High (pause at Decide) | Operational, real-time, monitoring |
| **ReAct** | Thought → Action → Observation | Transparent reasoning, grounded in reality | Tunnel vision, sequential by default | Medium-High (at Observation) | Tool-heavy tasks, research, debugging |
| **PDCA** | Plan → Do → Check → Act | Auditable, quality gate, scope control | Slower, overhead for simple tasks | Very High (Plan = collaborate, Check = review) | Complex execution, code, structured deliverables |
| **Orchestrator-Worker** | Decompose → Delegate → Execute → Evaluate → Synthesize | Parallel, specialized, context-isolated | 15x token cost, hard to debug | High (interact with lead only) | Multi-domain research, large complex tasks |
| **Evaluator-Optimizer** | Generate → Evaluate → Feedback → Revise | Highest quality output, catches errors | Resource-intensive, needs stopping criteria | Very High (human as evaluator) | Writing, review, quality-critical output |

---

### Finding 3: Universal Principles — What ANY Good Agent Workflow Must Have

These appeared across 8+ independent sources:

#### 1. Explicit Scope Contracts (confirmed: multiple sources)
Agents MUST have a declared scope at task start. Without it, drift is mathematically inevitable. "Scope protection prevents drift—explicit scope contracts and checkpoint validation ensure agents fix only what's requested."
Source: [Tacnode — Context Drift](https://tacnode.io/post/your-ai-agents-are-spinning-their-wheels)

#### 2. External Memory / Single Source of Truth (confirmed: multiple sources)
Agents cannot rely on in-context "memory" for state across phases. External state management (files, databases, memory services) prevents context drift — the state that the agent reads must be the authoritative state, not an approximation.
Source: [Tacnode](https://tacnode.io/post/your-ai-agents-are-spinning-their-wheels), [Vellum](https://www.vellum.ai/blog/agentic-workflows-emerging-architectures-and-design-patterns)

#### 3. Confidence-Gated Escalation (confirmed: multiple sources)
Agents should operate autonomously by default but must have defined confidence thresholds that trigger escalation. The pattern: if confidence < threshold → pause and escalate to human. "HITL workflows reduce agent error rates by up to 60% in complex decision-making tasks."
Source: [Permit.io — HITL Best Practices](https://www.permit.io/blog/human-in-the-loop-for-ai-agents-best-practices-frameworks-use-cases-and-demo), [Replicant — Escalation Rules](https://www.replicant.com/blog/when-to-hand-off-to-a-human-how-to-set-effective-ai-escalation-rules)

#### 4. Producer != Verifier (confirmed: Anthropic, multiple framework authors)
The agent that generates output CANNOT reliably verify its own output. A separate verification pass — whether another agent, a different prompt, or human review — is required for quality-critical work.
Source: [Anthropic — Building Effective Agents](https://www.anthropic.com/research/building-effective-agents), [Vellum](https://www.vellum.ai/blog/agentic-workflows-emerging-architectures-and-design-patterns)

#### 5. Ground Truth at Every Step (confirmed: Anthropic)
Agents require "ground truth from the environment at each step" to properly evaluate outcomes. Agents that proceed without verifying actual state (vs. assumed state) accumulate errors. Every action should produce a verifiable observation before the next action.
Source: [Anthropic — Building Effective Agents](https://www.anthropic.com/research/building-effective-agents)

#### 6. Task Decomposition Over Monoliths (confirmed: multiple sources)
"Early agent implementations often become a single do-everything agent that is the AI equivalent of a monolith." The correct pattern: break into smaller, purpose-built agents orchestrated as a pipeline. Each agent handles ONE concern.
Source: [Tacnode](https://tacnode.io/post/your-ai-agents-are-spinning-their-wheels), [glaforge — Anti-Patterns](https://glaforge.dev/talks/2025/12/02/ai-agentic-patterns-and-anti-patterns/)

#### 7. Iteration Limits / Stopping Criteria (confirmed: Anthropic)
All loops need stopping conditions. Without them, agents enter infinite refinement cycles or perpetual re-planning loops. Define max iterations and exit conditions upfront.
Source: [Anthropic — Building Effective Agents](https://www.anthropic.com/research/building-effective-agents)

#### 8. Context Window Protection (confirmed: Anthropic, multiple sources)
The orchestrator's context window is the most precious resource. Keep the lead agent's context clean by offloading execution to workers. "Facilitates compression by operating in parallel with their own context windows."
Source: [Anthropic — Multi-Agent Research System](https://www.anthropic.com/engineering/multi-agent-research-system)

---

### Finding 4: Guard-Rails for Drift Prevention

Three types of drift confirmed across sources, each with a different prevention mechanism:

#### Type A: Scope Drift (agent "improves" beyond requested scope)
- **Mechanism**: Explicit scope contracts + checkpoint validation
- **Pattern**: Define what is IN scope at task start; agent checks before each action
- **Trigger for intervention**: Any action outside declared scope → pause and escalate
- Source: [Tacnode](https://tacnode.io/post/your-ai-agents-are-spinning-their-wheels)

#### Type B: Context Drift (stale data → divergent reality)
- **Mechanism**: External memory + single source of truth
- **Pattern**: All state reads from canonical external storage, not in-context assumption
- **Trigger**: Re-plan frequency spike → signals context mismatch
- Source: [Tacnode](https://tacnode.io/post/your-ai-agents-are-spinning-their-wheels), [IBM — Agentic Drift](https://www.ibm.com/think/insights/agentic-drift-hidden-risk-degrades-ai-agent-performance)

#### Type C: Behavioral Drift (model updates, training shifts)
- **Mechanism**: Continuous automated testing with intent-based evaluation (not exact string match)
- **Pattern**: Test at individual response level → scenario level → business function level
- **Trigger**: Regression test failure → flag for human review
- Source: [IBM — Agentic Drift](https://www.ibm.com/think/insights/agentic-drift-hidden-risk-degrades-ai-agent-performance)

---

### Finding 5: Task-Type Workflow Adaptation

Different task types need different workflow shapes. This is confirmed but less systematically documented than the base patterns:

| Task Type | Best Pattern | Key Adaptation |
|---|---|---|
| **Research** | Orchestrator-Worker + OODA | Parallel subagents; dynamic re-planning; gap-identification loop; citation verification pass |
| **Execution / Code** | PDCA | Explicit plan before any code; Check = test suite; human approval gate at Plan and Check |
| **Review / Critique** | Evaluator-Optimizer | Human as primary evaluator; AI as executor; structured rubric required |
| **Creative** | Evaluator-Optimizer + PDCA hybrid | Plan phase = explore options; Generate-Evaluate-Revise loop; human aesthetic judgment required at Evaluate |
| **Monitoring / Ops** | OODA | Speed over auditability; automated most phases; human escalation for anomalies only |

**Source**: [Vellum 2026 Guide](https://www.vellum.ai/blog/agentic-workflows-emerging-architectures-and-design-patterns), [IBM — Agentic Workflows](https://www.ibm.com/think/topics/agentic-workflows), [Anthropic — Building Effective Agents](https://www.anthropic.com/research/building-effective-agents)

---

### Finding 6: Mode-Awareness — Adapting to the Human's State

This is a gap in the existing literature. No major framework explicitly addresses "workflow adaptation based on human energy/context/focus level." However, the following principles are extractable:

#### What IS documented:
- **Confidence-gated routing**: The agent routes to humans based on its OWN confidence — but not based on the human's current capacity to review
- **Async vs. synchronous escalation**: Some decisions can wait (async channel) vs. require real-time approval (sync interrupt). This maps loosely to "human energy" — low-energy humans should only receive async, low-stakes escalations
- **Context summarization for handoffs**: When handing off to a human, provide "focused, summarized context rather than raw data" — this is proto-mode-awareness (calibrate information density to human state)

#### What must be designed custom:
A true mode-aware workflow requires an explicit "human state" signal (energy level, focus context, time available) that modulates:
1. **Escalation threshold** — higher threshold (less interruption) in low-energy mode
2. **Information density** — fewer options, shorter summaries in low-energy mode
3. **Autonomy level** — more autonomous execution when human is unavailable; more checkpoints when human wants high-visibility
4. **Question batching** — batch decisions in low-energy mode vs. surface them individually in high-energy review mode

**Source**: [Zapier — HITL Patterns](https://zapier.com/blog/human-in-the-loop/), [Permit.io](https://www.permit.io/blog/human-in-the-loop-for-ai-agents-best-practices-frameworks-use-cases-and-demo), [Orkes — HITL](https://orkes.io/blog/human-in-the-loop/)

---

### Finding 7: Anti-Patterns (Confirmed Failure Modes)

From multiple independent sources, the following patterns cause system-level failures:

| Anti-Pattern | Description | Prevention |
|---|---|---|
| **The Monolith Agent** | One do-everything agent accumulates state, loses global view, can't scale | Decompose into specialized agents with single concerns |
| **Tunnel Vision** | Agent optimizes locally; solves sub-problems while drifting from global goal (ReAct failure mode) | Global goal reminder at each iteration; explicit stopping criteria |
| **Silent Confabulation** | Agent invents information confidently; no citation → undetectable without verification | Require source citations; "Immediately Validatable Output" design |
| **Context Drift Loop** | Agent re-plans repeatedly because perceived state ≠ actual state; creates infinite loop | Single source of truth for state; external canonical storage |
| **Scope Creep Execution** | Agent "improves" things beyond requested scope | Explicit scope contract at task start; checklist before each action |
| **Self-Verification Bias** | Agent verifies its own output and approves it (systematically biased) | Producer != Verifier rule; separate verification pass |
| **Complexity Escalation** | Adding more agents/tools/layers without clear performance gain | "Does this provide demonstrable improvement?" test before adding complexity |
| **Premature Escalation** | Routing to human every time confidence is uncertain; creates noise | Confidence threshold with fallback strategies before escalating |
| **No Stopping Criteria** | Refinement loop runs indefinitely; resource waste; no completion signal | Define max iterations and exit conditions at workflow design time |
| **Chatbot Mandate** | Building conversational interfaces where background execution would be better | AI should often remain invisible; conversation is one UX pattern, not the default |

**Sources**: [Concentrix — 12 Failure Patterns](https://www.concentrix.com/insights/blog/12-failure-patterns-of-agentic-ai-systems/), [glaforge — Anti-Patterns](https://glaforge.dev/talks/2025/12/02/ai-agentic-patterns-and-anti-patterns/), [Anthropic](https://www.anthropic.com/research/building-effective-agents), [Tacnode](https://tacnode.io/post/your-ai-agents-are-spinning-their-wheels)

---

### Finding 8: Handoff, Checkpoint, and Escalation Design

This is the most operationally relevant finding for a human-AI partnership.

#### The Three Escalation Triggers (confirmed by multiple sources)
1. **Confidence threshold breach** — agent confidence < defined threshold → route to human
2. **Scope boundary encounter** — task touches something outside declared scope → pause
3. **Structural failure signal** — tool failure, API error, system unavailability → pause

#### The Handoff Context Contract
When escalating to a human, the escalation package MUST include:
- What the agent was trying to accomplish (goal, not just action)
- What it has done so far (progress summary, not full context)
- What specifically it needs from the human (decision, approval, information)
- Why it cannot proceed alone (specific blocker)
- What the default action would be if the human approves without input

"Keep the request clear, focused, and explain why it's needed" — providing raw context dumps is an anti-pattern.

#### Async vs. Sync Escalation Selection
- **Sync (immediate interrupt)**: Irreversible actions, high-stakes decisions, blockers
- **Async (queue for review)**: Quality checks, optional approvals, low-stakes decisions
- **Never escalate**: Obvious fixes, reversible actions, single-reasonable-answer situations

#### Phase Gate Design
Multi-phase work should NEVER auto-advance. Each phase produces a deliverable; human reviews deliverable; explicit approval triggers next phase. This prevents the compound error problem — errors in Phase 1 amplify through Phase 2 and 3.

**Sources**: [Permit.io](https://www.permit.io/blog/human-in-the-loop-for-ai-agents-best-practices-frameworks-use-cases-and-demo), [Replicant](https://www.replicant.com/blog/when-to-hand-off-to-a-human-how-to-set-effective-ai-escalation-rules), [Zapier — HITL](https://zapier.com/blog/human-in-the-loop/), [Orkes](https://orkes.io/blog/human-in-the-loop/)

---

## Recommendation: Elements to Adopt for a Unified Core Workflow

Based on all findings, the optimal unified Core Workflow for the Omar-Nova partnership combines:

### Recommended Architecture: PDCA Shell + OODA Inner Loop + Evaluator Gate

```
PHASE 1: ORIENT (OODA-inspired)
  - Human declares session scope
  - Nova orients: reads relevant context, confirms understanding
  - Nova confirms: "Session scope: [X]. Proceeding."
  -- CHECKPOINT: Human approves scope before any execution --

PHASE 2: PLAN (PDCA-inspired)
  - Nova decomposes task into subtasks
  - Assigns task types → selects workflow shape per task type
  - Surface decisions requiring human judgment NOW (not mid-execution)
  - Produces plan artifact
  -- CHECKPOINT: Human approves plan OR Nova executes autonomously based on autonomy tier --

PHASE 3: EXECUTE (Orchestrator-Worker)
  - Delegate to specialized sub-agents
  - Orchestrator context stays clean
  - Workers report to files, not to chat
  -- ESCALATION: confidence gate monitors during execution --

PHASE 4: EVALUATE (Evaluator-Optimizer)
  - Separate verification pass (different agent or human)
  - Compare outputs against original scope contract
  - Surface gaps, not full output
  -- CHECKPOINT: Human reviews summary + gaps before Accept/Revise --

PHASE 5: ACT / CLOSE
  - Approved outputs committed
  - State persisted (files, memory, handoffs)
  - Next priorities surfaced from task graph
```

### Mode-Aware Modulation Layer (maps to current Mode System)

The above is the base workflow. Mode modulates:
- **Checkpoints** activated at Phase 1 and 4 in all modes; Phase 2 only in review/high-energy
- **Escalation threshold** higher in low-energy (less interruption) vs. lower in review (more visibility)
- **Information density at handoffs** — terse in low-energy/emergency; detailed in review/high-energy
- **Plan ceremony** — lightweight in low-energy; full rationale in high-energy

### Key Design Principles to Preserve

1. External state for everything that matters — never trust in-context memory
2. Producer != Verifier — always a separate verification pass
3. Scope contract at session start — no scope = no protection against drift
4. Handoff context contract — goal + progress + need + blocker + default, never raw dumps
5. Task decomposition by type — research vs. execution vs. review need different inner loops

---

## Sources

| Source | URL | Key Contribution |
|---|---|---|
| Anthropic — Building Effective Agents | https://www.anthropic.com/research/building-effective-agents | 6 composable patterns, ground truth principle, anti-patterns |
| Anthropic — Multi-Agent Research System | https://www.anthropic.com/engineering/multi-agent-research-system | Orchestrator-Worker in production; parallel tool calling; token economics |
| Atlas SC — Cybernetic Recursion | https://atlassc.net/2026/02/13/cybernetic-recursion-ai-agent-loops | OODA vs PDCA vs ReAct comparison; effective loop design |
| Vellum — 2026 Guide to Agentic Workflows | https://www.vellum.ai/blog/agentic-workflows-emerging-architectures-and-design-patterns | Architecture comparison matrix; 4 core workflow components |
| IBM — Agentic Drift | https://www.ibm.com/think/insights/agentic-drift-hidden-risk-degrades-ai-agent-performance | Behavioral drift causes and detection |
| Tacnode — Context Drift | https://tacnode.io/post/your-ai-agents-are-spinning-their-wheels | Context drift loops; architectural mismatch; external state |
| Permit.io — HITL Best Practices | https://www.permit.io/blog/human-in-the-loop-for-ai-agents-best-practices-frameworks-use-cases-and-demo | Checkpoint design; escalation patterns; handoff context contract |
| Replicant — Escalation Rules | https://www.replicant.com/blog/when-to-hand-off-to-a-human-how-to-set-effective-ai-escalation-rules | Three escalation trigger categories; handoff language |
| Zapier — HITL Patterns | https://zapier.com/blog/human-in-the-loop/ | Confidence-based routing; async vs sync escalation |
| glaforge — Agentic Anti-Patterns | https://glaforge.dev/talks/2025/12/02/ai-agentic-patterns-and-anti-patterns/ | 4 anti-patterns; tool design principles |
| Concentrix — 12 Failure Patterns | https://www.concentrix.com/insights/blog/12-failure-patterns-of-agentic-ai-systems/ | Comprehensive failure taxonomy |
| EMA — OODA + Agentic AI | https://www.ema.co/blog/agentic-ai/agentic-ai-and-the-ooda-loop-a-new-era-of-intelligent-collaboration | OODA applied to agentic systems |
| InfoQ — PDCA for AI Code | https://www.infoq.com/articles/PDCA-AI-code-generation/ | PDCA applied to human-AI coding collaboration |
| Orkes — HITL | https://orkes.io/blog/human-in-the-loop/ | LangGraph interrupt() pattern; real-world HITL walkthrough |

---

## Gaps and Uncertainties

### Gap 1: Mode-Awareness Is Custom Territory (low literature coverage)
No published framework addresses workflow adaptation based on human energy/focus level. The concept exists implicitly in async vs. sync escalation routing, but no formal model treats human state as a first-class workflow variable. The Omar-Nova mode system is ahead of published literature on this dimension. **Confidence**: High that this gap is real.

### Gap 2: Multi-Agent Token Economics at Scale (single source)
The 15x token cost figure comes from Anthropic alone — not cross-validated by other sources. May be task-specific. **Confidence**: Medium.

### Gap 3: Optimal Confidence Thresholds Are Underdetermined
Multiple sources cite confidence-gated escalation as best practice, but none provide universal threshold recommendations. The 0.85 figure cited in one source is illustrative, not authoritative. Thresholds must be tuned per domain. **Confidence**: High that this is domain-specific, no universal answer.

### Gap 4: Long-Running Workflow Continuity
Most literature covers session-bounded workflows. Cross-session continuity patterns (handoffs, memory persistence, context reconstruction) are under-documented relative to their operational importance. The WOS architecture (local, from Omar's skills) is more developed on this dimension than any external source found.

### Gap 5: Contradiction — Single Agent vs. Multi-Agent Performance
Vellum reports: "Research indicates single-agent systems with strong prompts achieve comparable performance to multi-agent setups." Anthropic reports 15x token cost for multi-agent with significant quality gains for research tasks. These are not necessarily contradictory (task type matters), but the nuance is not well-documented in either source. **Confidence**: Medium — highly task-dependent.

---

## Local Context Notes

The following local patterns from Omar's system are more advanced than anything found in external literature and should be PRESERVED, not replaced:

- **WOS 4-Layer Architecture** (Command / Execution / Continuity / Governance): No equivalent found externally. This is novel design.
- **Mode System (6 modes modulating behavior)**: No external equivalent. Literature has HITL but not human-state-adaptive behavior modulation.
- **Producer != Verifier** as governance invariant: Found externally (Anthropic) but less strictly enforced. Local implementation (mandatory separate verification agent) is stricter and more explicit.
- **Focus Guardian Protocol**: No external equivalent. The AI actively countering human drift patterns is novel.
- **Handoff files as cross-session bridge**: Found conceptually in literature but not as a first-class architectural primitive.

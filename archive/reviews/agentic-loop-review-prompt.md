# Agentic Loop — Review Prompt

Send this prompt to an external AI along with the contents of `agentic-loop-review-package.md`.

---

## The Prompt

You are a senior AI systems architect specializing in human-AI orchestration workflows, agentic design patterns, and operational workflow engineering. You have deep expertise in OODA loops, PDCA cycles, ReAct patterns, multi-agent orchestration (Anthropic's orchestrator-worker pattern), and evaluator-optimizer loops. You have designed and shipped production agentic systems.

I'm going to share a workflow design called the **Agentic Loop** — a unified operational workflow for a human-AI partnership. I need your most honest, brutal, and specific critique. Do not be polite. Do not pad with compliments. Tell me exactly what is wrong, what is right, and what you would change.

### What This Is

The Agentic Loop is a 6-phase + 2-bookend operational workflow for a solo human working with multiple AI CLI orchestrators (Claude Code, Gemini CLI, Codex CLI). It replaces 16 fragmented workflows that accumulated organically. The design synthesizes internal research (catalog of all 16 predecessors, gap analysis, overlap analysis) and external research (14 sources including Anthropic, IBM, Vellum, Tacnode, and others on agentic workflow patterns).

Key innovations:
- **Mode-aware ceremony modulation**: 6 human energy/context modes modulate every phase's behavior (no published framework has this)
- **SYNC as a first-class phase**: State propagation (updating all impacted files after a change) is Phase 6, not an afterthought
- **Focus Guardian**: The AI actively detects and counters human drift patterns with graduated interventions
- **Architectural formula**: PDCA(shell) + OODA(inner) + Evaluator(gate) + Mode(modulator) + SYNC(propagator)

### Your Task

Read the attached design document carefully. Then provide your review in EXACTLY this structure:

---

**OVERALL SCORE: [X]/10**

Brief (2-3 sentence) overall assessment.

---

**TOP 3 STRENGTHS** (what is genuinely good and should be preserved)

1. [Strength] — [Why it matters] — [How it compares to industry practice]
2. ...
3. ...

---

**TOP 5 WEAKNESSES** (what is wrong, risky, or poorly designed)

For each weakness:
- **Problem**: What exactly is wrong
- **Impact**: What happens if not fixed
- **Evidence**: Why you believe this (cite specific sections, external frameworks, or production experience)
- **Suggested fix**: How to address it

1. ...
2. ...
3. ...
4. ...
5. ...

---

**SUGGESTED CHANGES** (prioritized, most impactful first)

For each change:
- **Change**: What to do
- **Priority**: P0 (must fix before shipping) / P1 (should fix) / P2 (nice to have)
- **Effort**: Low / Medium / High
- **Rationale**: Why

1. ...
2. ...
3. ...
(as many as needed)

---

**ANSWERS TO SPECIFIC QUESTIONS**

Answer each of these directly:

1. Is the phase decomposition sound? Too many? Too few? Wrong boundaries?
2. Is the mode modulation table well-calibrated?
3. Are there blind spots or anti-patterns being introduced?
4. What would you change, add, or remove?
5. How does this compare to OODA, ReAct, PDCA, and modern agentic patterns?
6. Are 16 guard-rails the right number?
7. Is SYNC as a first-class phase the right call?
8. Is "Agentic Loop" the right name?
9. Is the "engines" concept (cross-cutting processes invoked within phases) architecturally sound?
10. How well does this scale beyond a single human + multiple AI orchestrators?

---

**COMPARISON TO STATE OF THE ART**

How does this design compare to:
- Anthropic's "Building Effective Agents" composable patterns
- Anthropic's multi-agent research system architecture
- OODA Loop as applied to agentic AI (EMA, Sogeti Global, Atlas SC)
- PDCA for AI code generation (InfoQ)
- ReAct (Google Research / ICLR 2023)
- Vellum's 2026 agentic workflow taxonomy
- IBM's agentic drift framework
- Tacnode's context drift analysis
- HITL best practices (Permit.io, Replicant, Zapier, Orkes)
- glaforge and Concentrix failure pattern taxonomies

What is this design doing better than these? What is it doing worse? What is it missing from them?

---

**ONE THING YOU WOULD SHIP DIFFERENTLY**

If you were building this system from scratch with the same requirements (1 human, multiple AI CLIs, 6 energy modes, delegation-native, cross-session continuity), what is the single biggest thing you would design differently?

---

### Evaluation Criteria for Your Review

Grade yourself on:
- **Specificity**: Did you cite specific sections, phases, guard-rails, or table cells? Generic feedback is useless.
- **Actionability**: Can the designer take your feedback and implement changes without a follow-up conversation?
- **Grounding**: Did you reference external frameworks, production experience, or published research?
- **Honesty**: Did you identify genuine problems, or did you pad with safe observations?

### The Design Document

[ATTACH: Full contents of agentic-loop-review-package.md]

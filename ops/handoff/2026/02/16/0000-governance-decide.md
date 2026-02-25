# Handoff: /decide — Governance Templates Format

**Status**: Pending decision. Omar approved human-standard governance (CODE_OF_CONDUCT.md, SECURITY.md) but wants structured evaluation of whether to adapt templates for AI agents.

**Created**: 2026-02-16
**For**: Future Claude session running `/decide`

---

## Background

Villa Thaifa uses AI agents (Claude, Gemini) as primary operators alongside human contributors. As part of repo-bootstrap skill design, governance files are being established. Omar initially selected "human-standard" (Contributor Covenant) but flagged a question:

> "je me demande si on devrait s'inspirer / prendre le meilleur du Format classique open-source. Reconnu partout, mais bien sur l'adapter aux agents AI ou pas?"

Translation: "I wonder if we should draw inspiration from the classic open-source format, recognized everywhere, but of course adapt it for AI agents or not?"

This handoff bundles the context and options for structured decision-making.

---

## What Needs Deciding

**Question**: Should governance templates remain human-standard, be human-standard-but-AI-adapted, or be AI-only?

**Scope**: CODE_OF_CONDUCT.md and SECURITY.md templates for repo-bootstrap skill.

**Why it matters**: Governance documents set expectations for contributors, define boundaries, and shape collaboration norms. The wrong choice creates friction; the right choice accelerates onboarding.

---

## Three Options to Evaluate

### 1. Human-Standard (Contributor Covenant)
**Description**: Use Contributor Covenant (or similar) unchanged. Established, recognized globally, proven in thousands of repos.

**Pros**:
- Instantly recognizable to human contributors
- Battle-tested across open-source ecosystem
- No bespoke interpretation needed
- Strong enforcement precedents exist

**Cons**:
- Silent on AI agent behavior and boundaries
- Doesn't address data ethics concerns specific to AI
- No guidance on decision constraints or model limitations
- May feel misaligned with actual team composition (mostly AI)

---

### 2. Human-Standard Adapted for AI
**Description**: Take the structure and principles of Contributor Covenant but add dedicated sections for AI agent behavior, data handling, decision constraints, and ethical guardrails.

**Pros**:
- Recognizable foundation (lowers onboarding friction for humans)
- Explicitly addresses AI-specific concerns (data ethics, model limits, decision oversight)
- Hybrid approach: speaks to both humans and agents
- Best of both worlds: trust + clarity

**Cons**:
- Requires new sections not found in standard templates
- Slightly longer, more complex document
- No established precedent to fall back on for edge cases

---

### 3. AI-Only
**Description**: Pure AI agent governance. Focused exclusively on agent responsibilities, data handling, decision authority, behavioral boundaries, and ethical constraints. No human contributor sections.

**Pros**:
- Perfectly aligned with actual team (mostly AI agents)
- No ambiguity about scope (agents, not humans)
- Shorter, clearer for AI-specific concerns

**Cons**:
- Not recognizable to human contributors
- Feels niche, not established
- May alienate human collaborators or open-source contributors
- Creates disconnect if humans join later

---

## Key Reference Files

All files referenced below contain templates, detailed analysis, and decision rationale:

1. **Decision skeleton**
   `/home/director/villa-thaifa/docs/repo-organization-decision.md`
   Initial decision record (may contain partial analysis or prior choices).

2. **Full governance analysis**
   `~/omar/knowledge/research/development/repo-organization/governance-items-decision.md`
   Complete template drafts for all 3 options. Includes CODEs OF CONDUCT and SECURITY.md samples for each approach. Start here for detailed options.

3. **Skill design context**
   `~/omar/knowledge/research/development/repo-bootstrap/skill-design.md`
   Section on governance templates. Current assumption: human-standard. Verify if decision changes this assumption.

4. **Operating rules**
   `~/.claude/rules/rules.md`
   Section: "Decision Integrity" (no complexity dismissal, no elimination without testing). Apply these principles to option evaluation.

5. **Omar's CLAUDE.md mode system**
   `~/.claude/CLAUDE.md`
   Behavioral dispatch table. Check current mode before structuring the decision output (summary length, option presentation, confirmation cadence).

---

## Decision Routing

**Execution path**:
1. Read all three reference files above to internalize options and context.
2. Run `/decide` with the three options formatted per decision-integrity rules.
3. Show Omar the structured evaluation (no dismissals without testing equivalence).
4. Capture the chosen option in `/home/director/villa-thaifa/docs/repo-organization-decision.md`.
5. If human-standard-adapted is chosen, verify that skill design (repo-bootstrap) is updated to reflect AI-specific sections.

**Output format rule**:
- If decision complexity warrants dashboard: delegate to Gemini to generate HTML summary of options + decision matrix.
- Otherwise: present 3 options in `/decide` format with recommendation.

---

## Constraints & Non-Negotiables

- All governance files must be in **English**.
- Delegation rule: Research and template validation → Gemini (hard rule per rules.md).
- Decision Integrity rules apply (no complexity dismissal; test all options for equivalence).
- Final decision persists to `docs/repo-organization-decision.md` with explicit justification.
- If templates are adapted (Option 2 or 3), update skill-design.md reference to reflect AI-agent sections.

---

## Post-Decision Checklist

Once Omar decides:

- [ ] Update `/home/director/villa-thaifa/docs/repo-organization-decision.md` with chosen option + rationale
- [ ] If Option 2 (adapted) or Option 3 (AI-only): generate/finalize CODE_OF_CONDUCT.md and SECURITY.md templates
- [ ] Verify `repo-bootstrap` skill design references correct governance approach
- [ ] Archive this handoff file to `docs/plans/archive/handoff-governance-decide-[date].md`
- [ ] Close open loop in AGENTS.md (governance templates)

---

**End handoff. Proceed to `/decide` with options above.**

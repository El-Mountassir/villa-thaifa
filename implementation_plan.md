# IMPL PLAN: Governance & Agentic Standards

> **Goal**: Establish the "Rules of Engagement" and "Documentation Standards" before starting technical implementation.

## User Review Required

- **Agentic Unified Process**: Validation of the proposed workflow (Plan -> Act -> Document -> Verify).
- **PRD/SRS Templates**: Confirmation of the document structure.

## Proposed Changes

### 1. Governance Standards `docs/project/standards/`

#### [NEW] agentic-process.md

- Definition of our custom "Agentic Unified Process".
- **Core Loop**:
  1. **Context Loading** (Gemini/Agents.md)
  2. **Planning** (Impl Plan)
  3. **Execution** (Atomic Steps)
  4. **Memory Verification** (Update Specs)
- **Rules**: Explicit constraints (Safe Mode, Validation).

#### [NEW] prd-template.md & srs-template.md

- "AI-Optimized" templates.
- **PRD**: Focus on User Stories & Business Value.
- **SRS**: Focus on Technical Logic & Data Structures (Domains).

### 2. Quality Audit (Existing Files)

#### [UPDATE] tasks/active.md

- Add specific audit tasks for `content/` and `docs/`.

#### [REFINE] content/

- Systematically review `content/facilities` to ensure Markdown is clean and structured for AI ingestion.

## Verification Plan

### Manual Verification

- **User Review**: You review the created standards.
- **Agent Self-Check**: Next task (Audit) must follow the new `agentic-process.md` strictly.

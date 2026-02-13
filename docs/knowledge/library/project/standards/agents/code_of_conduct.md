# 🚨 Agent Code of Conduct & Cognitive Rules

> **Authority**: Referenced by `AGENTS.md` (Master Manifest).
> **Scope**: Mandatory for ALL Agents (Gemini, Claude, etc.).

## 🚫 Non-Negotiable Rules (The "Red Lines")

### 1. **Strict MVC + Bindings**:

    - All features MUST follow `src/features/[name]/{model,view,controller,bindings}`.
    - **No Cross-Controller Calls**: Features can ONLY communicate via `bindings/api.ts` or `bindings/events.ts`.
    - **DIRECT IMPORTS ARE FORBIDDEN**.

### 2. **JSON-First Architecture**:

    - Views should primarily be schemas/configs for `json-render`.
    - The UI is a projection of Agent State.

### 3. **No Orphaned Files**:

    - Every file must be part of a defined Feature or Core System.
    - Do not create random files in the root directory.

### 4. **No Silent Failures**:

    - If a tool call fails (e.g., `replace_file_content`), YOU MUST REPORT IT.
    - Never pretend a failed action succeeded.

### 5. **Everything is a File (Persistence First)**:

    - **CRITICAL**: Chat context is ephemeral and fragile. NEVER rely on it for storage.
    - **Rule**: ALL valuable output (Drafts, Plans, Reports, Handover notes) MUST be written to a file immediately.
    - **Internal & External**: This applies to messages for Clients (Said), for Users (Omar), and for other Agents.
    - **Workflow**: Write to file -> Reference file in chat.

## 🧠 Cognitive Guidelines

### 1. **Check the Brain First**:

    - Before asking "What is X?", check `GEMINI.md`, `AGENTS.md`, and `docs/knowledge/`.
    - Use `grep_search` if you are lost.

### 2. **Preserve Knowledge**:

    - If you learn something new (API, Credential, Constraint), WRITE IT DOWN in `docs/knowledge/`.
    - Knowledge inside your context window dies with the session; Knowledge in `docs/` lives forever.

### 3. **System 2 Thinking**:

    - Pause before complex refactors.
    - Write a plan in `docs/project/plans/` if the task exceeds 5 steps.

### 4. **Documentation First**:

    - Before writing code, read/update the relevant Architecture Decision Record (ADR).
    - Specifically: `docs/architecture/ADR-002-feature-mvc.md`.

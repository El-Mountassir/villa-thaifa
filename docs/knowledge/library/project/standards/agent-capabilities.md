# 🤖 Agent Capabilities & Workflow Manual

> **Purpose**: Maximize the potential of Villa Thaifa's AI workforce by documenting advanced capabilities and standardized workflows.
> **Audience**: Antigravity, Gemini CLI, Claude Code Agents, and Omar.

## 1. The AI Ecosystem

### 🧠 Antigravity (The CTO / Architect)

- **Role**: Strategic Planning, Complex Refactoring, Browser Automation.
- **Top Capabilities**:
  - **Browser Agent**: Can browse, test UI, and scrape data (Sandboxed Chrome).
  - **Artifacts**: Generates verifiable deliverables (Plans, Reports).
  - **Manager View**: Orchestrates multi-agent workflows.
  - **Planning Mode**: Creates "Blueprints" before coding.
  - **Sub-Agent Fleet**: Access via `claude @agent` (See [`registry.md`](docs/project/standards/agents/registry.md)).
- **Workflow**:
  1. **Plan**: Analyze requirement -> Create `implementation_plan.md`.
  2. **Execute**: Use Editor + Terminal + Browser.
  3. **Verify**: Test changes via Browser Agent.

### ⚡ Gemini CLI (The Rapid Operator)

- **Role**: Quick Contextual Tasks, System Administration.
- **Top Capabilities**:
  - **Context Loading**: Supports `@path/to/file` and `@directory/` syntax.
  - **`GEMINI.md`**: Automatically maps project context.
  - **Wildcards**: Processes `@*.js` for bulk analysis.
- **Best For**:
  - "Read this file and explain X".
  - "Refactor this specific directory".

### 💻 Claude Code CLI (The Coder & Reviewer)

- **Role**: TDD, Deep Coding, Code Reviews.
- **Top Capabilities**:
  - **Slash Commands**: Custom commands in `.claude/commands`.
  - **TDD Workflow**: Write tests -> Write code -> Pass tests.
  - **Multitasking**: Handles large refactors via multiple terminal tabs.

## 2. Advanced Workflows

### 🔄 The "Agentic Unified Process" (Villa Thaifa Standard)

1.  **Context Injection (The "Download")**

    - **ALL Agents**: MUST read `GEMINI.md` first.
    - **Syntax**: `gemini @GEMINI.md` or `claude @GEMINI.md`.
    - _Note_: `GEMINI.md` now uses `@path` syntax to auto-load critical files.

2.  **The "Planner-Executor" Loop**

    - **Antigravity** (Planner) creates the architectural strategy (`ADR`, `Impl Plan`).
    - **Claude/Gemini** (Executor) implements specific files using the plan as context.
    - **Antigravity** (Verifier) uses Browser Agent to validate the result.

3.  **Knowledge Preservation (The "Upload")**
    - **Rule**: If you learn something, you write it down.
    - **Target**: `docs/specs/knowledge/` (Technical) or `admin/` (Business).
    - **Never** leave knowledge "in the chat".

## 3. Tool-Specific Optimization

### Antigravity

- **Always** use `task_boundary` to structure work.
- **Always** create `artifacts` for human review.
- **Use** `search_web` to bridge the 2026 knowledge gap.

### Gemini CLI

- **Maximize** `@` syntax: `@src/domains/booking/` to load a full module.
- **Use** `/memory refresh` to reload context after changes.

### Claude Code

- **Use** `/clear` frequently to save tokens.
- **Use** `CLAUDE.md` for project-specific slash commands.

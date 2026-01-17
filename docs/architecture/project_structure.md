# 🌍 Project Structure (The "AI-First" Layout)

> **Authority**: Referenced by `AGENTS.md` (Master Manifest).
> **Purpose**: Defines the canonical directory structure for Villa Thaifa.

## Root Directory

| Directory         | Purpose                                            |
| :---------------- | :------------------------------------------------- |
| **`/.ai/`**       | Agent workspace (Memory, automated workflows).     |
| **`/AGENTS.md`**  | **Master Manifest** & Entry Point.                 |
| **`/GEMINI.md`**  | Gemini/Antigravity specific context.               |
| **`/CLAUDE.md`**  | Claude Code CLI specific context.                  |
| **`/src/`**       | **Source Code**. Next.js + json-render App.        |
| **`/docs/`**      | **Knowledge Base**. Specs, Architecture, Plans.    |
| **`/content/`**   | **The "Truth"**. Photos, Markdown content, Assets. |
| **`/tasks/`**     | **Work Management**. `active.md` is the Kanban.    |
| **`/legacy/`**    | **Archive**. Old/Chaotic files (Reference only).   |
| **`/artifacts/`** | **Outputs**. Complex agent deliverables.           |

## Key Sub-Directories

### `src/` (The Application)

- **`src/features/`**: Domain-Driven Vertical Slices (MVC).
- **`src/systems/`**: Core technical infrastructure (Auth, Database).

### `docs/` (The Brain)

- **`docs/architecture/`**: Technical decisions (ADRs).
- **`docs/knowledge/`**: Business facts, Client profiles.
- **`docs/project/standards/`**: Rules, Protocols, Code of Conduct.

### `content/` (The Data)

- **`content/facilities/`**: Room descriptions, photos.
- **`content/policies/`**: Hotel rules.

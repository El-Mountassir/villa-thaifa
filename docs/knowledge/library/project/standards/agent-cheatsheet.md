# 🤖 Agent Cheatsheet

## Context Loading Syntax

| Tool            | Syntax  | Note                       |
| :-------------- | :------ | :------------------------- |
| **Antigravity** | `@file` | Instruction in `GEMINI.md` |
| **Gemini CLI**  | `@file` | Native support             |
| **Claude Code** | `@file` | Native support             |

## Key Capabilities (2026)

- **Browser Agent** (Antigravity): Can scrape, test, and debug web UIs.
- **Artifacts**: Always generate `implementation_plan.md` before coding.
- **Knowledge**: Write strictly to `docs/specs/knowledge/`.

## The "Golden Rule"

**Context First**: Always check `GEMINI.md` -> `AGENTS.md` before acting.

# 🤝 Agent Collaboration Protocol (ACP-001)

> **Context**: We are a Multi-Agent Team (Gemini CLI, Claude Code, Antigravity).
> **Problem**: Private context (instance artifacts) leads to data silos and loss of continuity.
> **Mandate**: **Shared Memory First.**

## 1. The "No Silo" Rule

**Core Principle**: "If it is not in the Project Repository, it does not exist."

- ❌ **Bad**: Creating a standard `task.md` in your private brain/artifact directory (`~/.gemini/...`).
- ✅ **Good**: Updating `tasks/active.md` or creating a specific plan in `docs/project/plans/`.

## 2. Shared Memory Locations

All agents must read/write to these canonical paths:

| Artifact Type       | Canonical Path               | Description                                       |
| :------------------ | :--------------------------- | :------------------------------------------------ |
| **Active Tasks**    | `tasks/active.md`            | The central flight board.                         |
| **Knowledge/Facts** | `docs/specs/knowledge/`      | Discoveries, URLs, Credentials (refs), Incidents. |
| **Plans/Strategy**  | `docs/project/plans/`        | Detailed execution steps for specific missions.   |
| **Decisions**       | `docs/architecture/ADR-*.md` | Structural choices (e.g., Folder structure).      |
| **Data Backups**    | `content/backup/`            | Raw scrapes, JSON dumps.                          |

## 6. Zero Tolerance for Silent Failures (Strict)

**Rule**: "Stop, Report, Fix."

1.  **Observability**: If a tool fails (e.g., `replace_file_content` returns an error), you MUST NOT proceed as if it succeeded.
2.  **No "Hallucinated Success"**: Never tell the user "I decided to..." when the reality is "The tool failed and I ignored it."
3.  **Corrective Action**:
    - **Retry**: If transient, retry _with modified parameters_.
    - **Escalate**: If persistent, stop and Notify User.
    - **Log**: Check `AGENTS.md` to see if a systemic issue needs logging.

## 7. Handover Protocol

Before ending a session, an Agent **MUST**:

1.  **Flush to Disk**: Write all in-memory plans to a file in the repo.
2.  **Update Status**: Mark completed items in `tasks/active.md` or the relevant Plan file.
3.  **Leave Breadcrumbs**: If a task is paused, write a "Next Actions" note in the Plan file.

## 4. Cross-Agent Compatibility

- **Markdown Friendly**: Use standard MD. Avoid agent-specific XML tags in shared files unless agreed upon.
- **Path Awareness**: Always use relative paths from the project root (or absolute if OS-specific, but prefer relative for portability).

## 5. The Linkage Mandate (Strict)

**Rule**: "You Create It -> You Link It."

1.  **Orphans Forbidden**: Never create a file in `docs/` or `plans/` without immediately linking it in a parent index (`AGENTS.md`, `tasks/active.md`, or a specific TOC).
2.  **Context Maintenance**: If you add a new capability or guide, update `AGENTS.md` so the Next Agent knows it exists.

---

_Ratified: 2026-01-14_

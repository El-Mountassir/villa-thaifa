# CLAUDE.md - Claude Code CLI Context

> **Role**: Specialized Agent Interface for Claude Code CLI.
> **Master Manifest**: [AGENTS.md](AGENTS.md).

## ⚡ Quick Start

1.  **Know Your Stakeholders** ⭐: [`docs/leadership/STAKEHOLDERS.md`](docs/leadership/STAKEHOLDERS.md) - Who is who, roles, rules
2.  **Read the Rules**: `docs/project/standards/agents/code_of_conduct.md`.
3.  **Read the Brain**: `GEMINI.md` contains the Strategic Vision.
4.  **Check The Team**: `docs/leadership/TEAM.md`.

## 🤖 Claude-Specific Context

### Identity

- You are a **Sub-Agent** or **Specialized Unit** within the Villa Thaifa ecosystem.
- Your output must be compatible with the Antigravity Framework.

### Handovers

- When finishing a session, follow the protocol in `docs/project/standards/agents/collaboration_protocol.md`.

### Available Tools

**Browser Automation** - You have access to `agent-browser`, a headless browser automation CLI.

- **Location**: Installed globally via npm
- **Usage**: Via Bash tool
- **Documentation**: [`sources/agent-browser/guide.md`](sources/agent-browser/guide.md)
- **Quick Example**:
  ```bash
  agent-browser open https://example.com
  agent-browser snapshot -i -c  # Get interactive elements
  agent-browser click @e12      # Click by reference
  agent-browser close
  ```

**Capabilities**: Web scraping, form automation, screenshots, PDF export, data extraction, JavaScript execution.

**See**: [`AGENTS.md`](AGENTS.md) for full capabilities list.

---

_For all other contexts (Vision, Architecture, Roadmap), refer to `AGENTS.md`._

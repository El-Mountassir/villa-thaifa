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

- You are an Agentic CLI, with **Sub-Agents** or **Specialized Units** within the Villa Thaifa ecosystem.
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

**HotelRunner API** - You have access to HotelRunner REST API for property management.

- **Type**: REST API (HR-v1)
- **Status**: ⏳ Setup in progress (credentials pending)
- **Documentation**: [`sources/hotelrunner-api/guide.md`](sources/hotelrunner-api/guide.md)
- **Setup Progress**: [`sources/hotelrunner-api/SETUP.md`](sources/hotelrunner-api/SETUP.md)
- **Credentials**: `.env.local` (HOTELRUNNER_TOKEN, HOTELRUNNER_HR_ID)
- **Rate Limits**: 250 requests/day, 5 requests/minute

**Capabilities**: Manage rooms, retrieve reservations, update calendar (rates/availability), real-time booking webhooks.

**See**: [`AGENTS.md`](AGENTS.md) for full capabilities list.

### Platform Credentials

**For HotelRunner, Booking.com, and other platforms:**

- **Location**: `.env.local` (project root)
- **Access**: Read file at runtime, extract needed credentials
- **Default**: Use ADMIN (Omar) accounts, not OWNER (Said) accounts
- **Security**: Never log or output credentials
- **🔴 CRITICAL**: See [`docs/operations/.env.rules.md`](docs/operations/.env.rules.md) before ANY modification to `.env.local`
- **Full Guide**: [`docs/operations/CREDENTIALS.md`](docs/operations/CREDENTIALS.md)

**Quick access pattern:**

```bash
# Read credentials from .env.local
# Extract HOTELRUNNER_ADMIN_EMAIL and HOTELRUNNER_ADMIN_PASSWORD
# Use with agent-browser or API calls
```

---

_For all other contexts (Vision, Architecture, Roadmap), refer to `AGENTS.md`._

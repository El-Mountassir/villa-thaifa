# AGENTS.md

> **Specification**: [AGENTS.md Standard](https://agents.md)
> **Identity**: Universal Agent Manifest.
> **Last Updated**: 2026-01-17

## 🤖 Manifest

- **Project**: Villa Thaifa - Digital Transformation
- **Owner**: Omar El Mountassir
- **Capabilities Required**: `fs_read`, `fs_write`, `cli_exec`.

## 🚨 PRIME DIRECTIVE (Governance)

> **RULE #1**: ALL WORK MUST BE REGISTERED IN `ROADMAP.md` FIRST.
> No agent shall execute a task that is not explicitly defined in the Project Roadmap.
> If a task is missing, **STOP**, update `ROADMAP.md`, and request user approval.

## 📌 References (The "Constitution")

| Concept             | Source                                                                                                               |
| :------------------ | :------------------------------------------------------------------------------------------------------------------- |
| **Stakeholders** ⭐ | [`docs/leadership/STAKEHOLDERS.md`](docs/leadership/STAKEHOLDERS.md) **READ FIRST**                                |
| **Team & Roles**    | [`docs/leadership/TEAM.md`](docs/leadership/TEAM.md)                                                                 |
| **Structure**       | [`docs/architecture/project_structure.md`](docs/architecture/project_structure.md)                                   |
| **Code of Conduct** | [`docs/project/standards/agents/code_of_conduct.md`](docs/project/standards/agents/code_of_conduct.md)               |
| **Collaboration**   | [`docs/project/standards/agents/collaboration_protocol.md`](docs/project/standards/agents/collaboration_protocol.md) |

## 🚀 Active Context

- **Work**: [`tasks/active.md`](tasks/active.md)
- **Vision**: [`MISSION.md`](MISSION.md)

## 🚀 Active Plans & Status

- **Tasks**: `tasks/active.md` (The Kanban).
- **Architecture**: `docs/architecture/` (The Blueprints).
- **Rescue**: We are currently in "Phase 1: Stabilization & Cleanup".

## 🔧 Available Tools & Capabilities

### **Browser Automation** - `agent-browser`

**Status**: ✅ Installed & Operational (Jan 2026)

Agent-browser is a fast headless browser automation CLI available globally. Use it via Bash for web automation tasks.

**Installation**:
```bash
agent-browser --version  # Already installed globally
```

**Key Capabilities**:
- **Navigation**: Open URLs, click elements, fill forms, submit data
- **Extraction**: Snapshots with element refs (@e1, @e2...), get text/HTML/attributes
- **Actions**: Click, type, hover, drag-drop, upload files, scroll
- **Data Collection**: Screenshots (full-page), PDF export, JSON snapshots
- **Automation**: Search forms, login flows, data scraping
- **JavaScript**: Execute custom JS code on pages

**Quick Examples**:
```bash
# Navigate and extract interactive elements
agent-browser open https://example.com
agent-browser snapshot -i -c  # Interactive elements with refs

# Click by reference and capture
agent-browser click @e12
agent-browser screenshot --full output.png

# Form automation
agent-browser fill "input[name='search']" "query"
agent-browser press Enter

# Data extraction
agent-browser get text "h1"
agent-browser eval "document.title"
agent-browser pdf output.pdf

# Cleanup
agent-browser close
```

**Sessions & Profiles**:
- `--session <name>`: Isolated browser sessions
- `--profile <path>`: Persistent browser profiles (saved cookies, auth)

**Best Practices**:
- Always close the browser with `agent-browser close` when done
- Use snapshot refs (@eX) for reliable element targeting
- Combine multiple commands with `&&` for workflows
- Use `--json` flag for structured output parsing

**Documentation**: Run `agent-browser --help` for full command reference

### **HotelRunner API** - Property Management System

**Status**: ⏳ Setup In Progress (Credentials Pending) - Jan 2026

HotelRunner REST API (HR-v1) provides programmatic access to Villa Thaifa's property management system for automation.

**API Details**:
- **Base URL**: `https://am.hotelrunner.com/custom-apps/rest-api`
- **Authentication**: TOKEN + HR_ID (header-based)
- **Rate Limits**: 250 requests/day, 5 requests/minute
- **Integration Type**: HR-v1 (REST API with JSON)

**Key Capabilities**:
- **Rooms**: Get room list, manage inventory
- **Reservations**: Retrieve bookings, search by date/status
- **Calendar**: Update rates and availability for specific dates
- **Webhooks**: Real-time push notifications (confirmed, modified, cancelled)

**Credentials** (`.env.local`):
```bash
HOTELRUNNER_TOKEN=<pending>     # API authentication token
HOTELRUNNER_HR_ID=<pending>      # Hotel property ID
```

**Quick Example** (Python):
```python
import os
import requests

headers = {
    'Authorization': f'Bearer {os.getenv("HOTELRUNNER_TOKEN")}',
    'HR-ID': os.getenv('HOTELRUNNER_HR_ID')
}

# Get today's reservations
response = requests.get(
    'https://am.hotelrunner.com/custom-apps/rest-api/reservations',
    headers=headers
)
```

**App Configuration**:
- **Name**: Villa Thaifa AI Automation
- **Type**: PMS (Property Management System)
- **Created**: 2026-01-24
- **Permissions**: Full access (rooms, reservations, calendar, webhooks)

**Best Practices**:
- Cache room/rate data to minimize API calls
- Monitor daily/minute rate limits carefully
- Implement retry logic with exponential backoff
- Never log or commit credentials

**Documentation**:
- **Setup Progress**: [`sources/hotelrunner-api/SETUP.md`](sources/hotelrunner-api/SETUP.md) - **Check this for current status**
- **Usage Guide**: [`sources/hotelrunner-api/guide.md`](sources/hotelrunner-api/guide.md)
- **Quick Reference**: [`sources/hotelrunner-api/README.md`](sources/hotelrunner-api/README.md)
- **Official Docs**: https://developers.hotelrunner.com/custom-apps/rest-api

**Current Progress** (as of 2026-01-24 13:30):
- ✅ Research completed - API section located
- ✅ Integration type selected (HR-v1)
- ✅ App creation form filled
- ✅ Source folder created with full documentation
- ⏳ Awaiting app creation completion
- ⏳ Credentials (TOKEN + HR_ID) pending
- ❌ Connection test not yet performed
- ❌ Source not yet enabled

**Next Steps**: Complete app creation in dashboard, obtain credentials, test connection.

---

_*Created during the "AI-First" Refactor - Jan 2026*_

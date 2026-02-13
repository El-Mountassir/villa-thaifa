# agents/instructions/AGENTS.md

> **Specification**: [agents/instructions/AGENTS.md Standard](https://agents.md)
> **Identity**: Universal Agent Manifest
> **Last Updated**: 2026-02-14

## 🤖 Manifest

- **Project**: Villa Thaifa - Digital Transformation
- **Owner**: Omar El Mountassir

## ⚡ Quick Start

1. **Know Your Stakeholders** ⭐: [`docs/client/STAKEHOLDERS.md`](docs/client/STAKEHOLDERS.md) - Who is who, roles, rules
2. **Read the Rules**: `docs/project/standards/agents/code_of_conduct.md`.
3. **Read the Brain**: `agents/instructions/GEMINI.md` contains the Strategic Vision.
4. **Check The Team**: `docs/client/TEAM.md`.

## 📋 Agent Rules (Governance)

> **All agents MUST follow these rules:**

> **RULE #0**: CREATE A BRANCH BEFORE ANY WORK ([git.md](./.agents/rules/git.md))
> **RULE #1**: ALL WORK MUST BE REGISTERED IN LINEAR FIRST.
> **Effective**: 2026-01-30 (Phase 2 Complete)
>
> No agent shall execute a task that is not registered as a Linear Issue.
> If a task is missing, **STOP**, create a Linear Issue, and request user approval.
>
> **Forbidden**:
>
> - Creating `tasks/*.md` files
> - Creating `workstream/*.md` files (except README)
> - Creating `.agents/input/jobs/missions/*.md` files
> - Using any local task tracking system
>
> **See**: `.agents/rules/linear-workflow.md` for full workflow.

## 📌 References (The "Constitution")

| Concept              | Source                                                                                                               |
| :------------------- | :------------------------------------------------------------------------------------------------------------------- |
| **Stakeholders** ⭐  | [`docs/client/STAKEHOLDERS.md`](docs/client/STAKEHOLDERS.md) **READ FIRST**                                  |
| **Communication** 🗣️ | [`docs/knowledge/client/COMMUNICATION.md`](docs/knowledge/client/COMMUNICATION.md) **DUTCH FIRST**                   |
| **Team & Roles**     | [`docs/client/TEAM.md`](docs/client/TEAM.md)                                                                 |
| **Structure**        | [`project/architecture/DIRECTORY_MAP.txt`](project/architecture/DIRECTORY_MAP.txt)                                   |
| **Code of Conduct**  | [`docs/project/standards/agents/code_of_conduct.md`](docs/project/standards/agents/code_of_conduct.md)               |
| **Collaboration**    | [`docs/project/standards/agents/collaboration_protocol.md`](docs/project/standards/agents/collaboration_protocol.md) |
| **🔴 Credentials**   | [`docs/operations/.env.rules.md`](docs/operations/.env.rules.md) **READ BEFORE MODIFYING .env**                      |
| **⚠️ Git Workflow**  | [`.agents/rules/git.md`](.agents/rules/git.md) **10 MANDATORY RULES - Branches, PRs, Atomic Commits**                |

| Rule Set            | File                                                                     | Purpose                                                   |
| :------------------ | :----------------------------------------------------------------------- | :-------------------------------------------------------- |
| **Workspace**       | [`.agents/rules/workspace.md`](./.agents/rules/workspace.md)             | Artifact paths, directory structure, plan management      |
| **Git Workflow**    | [`.agents/rules/git.md`](./.agents/rules/git.md)                         | Branching, commits, PR workflow, multi-agent coordination |
| **Verification**    | [`.agents/rules/verification.md`](./.agents/rules/verification.md)       | Testing, evidence, Definition of Done                     |
| **Linear Workflow** | [`.agents/rules/linear-workflow.md`](./.agents/rules/linear-workflow.md) | Issue lifecycle, labels, sprints                          |

### Quick Rules Summary

- **Rule #0**: CREATE A BRANCH BEFORE ANY WORK ([git.md](./.agents/rules/git.md))
- **Rule #1**: ALL WORK REGISTERED IN LINEAR FIRST ([workspace.md](./.agents/rules/workspace.md), [linear-workflow.md](./.agents/rules/linear-workflow.md))
- **Rule #2-10**: Git workflow, atomic commits, PRs, secrets ([git.md](./.agents/rules/git.md))
- **Rule #3-4**: Linear workflow, archiving ([workspace.md](./.agents/rules/workspace.md))

## 📌 References (The "Constitution")

| Concept                | Source                                                                                                               | Read Priority             |
| :--------------------- | :------------------------------------------------------------------------------------------------------------------- | :------------------------ |
| **🙋 Omar (Owner)** ⭐ | [`docs/client/OMAR.md`](docs/client/OMAR.md)                                                                 | **READ FIRST**            |
| **Stakeholders** ⭐    | [`docs/client/STAKEHOLDERS.md`](docs/client/STAKEHOLDERS.md)                                                 | **READ FIRST**            |
| **Communication** 🗣️   | [`docs/knowledge/client/COMMUNICATION.md`](docs/knowledge/client/COMMUNICATION.md)                                   | **DUTCH FIRST**           |
| **Team & Roles**       | [`docs/client/TEAM.md`](docs/client/TEAM.md)                                                                 | High                      |
| **Structure**          | [`project/architecture/DIRECTORY_MAP.txt`](project/architecture/DIRECTORY_MAP.txt)                                   | High                      |
| **Code of Conduct**    | [`docs/project/standards/agents/code_of_conduct.md`](docs/project/standards/agents/code_of_conduct.md)               | Medium                    |
| **Collaboration**      | [`docs/project/standards/agents/collaboration_protocol.md`](docs/project/standards/agents/collaboration_protocol.md) | Medium                    |
| **🔴 Credentials**     | [`docs/operations/.env.rules.md`](docs/operations/.env.rules.md)                                                     | **BEFORE MODIFYING .env** |

## 🚀 Active Context

### Current Work

- **Tasks**: [Linear Workspace](https://linear.app/el-mountassir) → Filter "Villa Thaifa" - 28 issues active (EM-128 to EM-155)
- **Projects**:
  - Villa Thaifa - Q1 2026 Operations (12 issues)
  - Villa Thaifa - OTA Integration (13 issues)
  - Villa Thaifa - Room Management (3 issues)
- **Plans**: [`.agents/plans/`](./.agents/plans/) (Implementation plans)
- **Sessions**: [`.agents/sessions/`](./.agents/sessions/) (Recent activity logs)

### Strategic Context

- **Vision**: [`MISSION.md`](MISSION.md)
- **Phase**: "Phase 1 + 2: Workspace Standardization (Rules + Linear Integration) - COMPLETE"
- **Architecture**: `docs/architecture/` (The Blueprints)
- **Migration**: Phase 2 Complete (2026-01-30) - All tasks in Linear

## 🔧 Available Tools & Capabilities

### Browser Automation - `agent-browser`

**Status**: ✅ Installed & Operational

Fast headless browser automation CLI for web scraping, form automation, and data extraction.

**Quick Start:**

```bash
agent-browser open https://example.com
agent-browser snapshot -i -c  # Interactive elements
agent-browser click @e12      # Click by reference
agent-browser screenshot --full output.png
agent-browser close
```

**Documentation**: [`sources/agent-browser/guide.md`](sources/agent-browser/guide.md)

### HotelRunner Integration

**Status**: ✅ Operational via Browser Automation

Access to Villa Thaifa reservations, calendar, and reports from HotelRunner.

**Current Method**: Browser automation with persistent profile
**Alternative**: REST API (rate-limited, webhook callback required)

**Quick Usage:**

```bash
cd sources/hotelrunner-api
python3 extract_reservations.py
# Output: data/reservations/latest.json (96 reservations)
```

**Documentation:**

- **Status**: [`sources/hotelrunner-api/STATUS-FINAL.md`](sources/hotelrunner-api/STATUS-FINAL.md) ⭐
- **Guide**: [`sources/hotelrunner-api/EXTRACTION-GUIDE.md`](sources/hotelrunner-api/EXTRACTION-GUIDE.md)
- **API Docs**: [`sources/hotelrunner-api/guide.md`](sources/hotelrunner-api/guide.md)

## 🤖 Agent Index

### Claude Code CLI

**Capabilities:**

- Code generation and refactoring
- Browser automation (via agent-browser)
- File operations (read, write, edit)
- Git operations (commit, push, branch)
- Plan mode for complex tasks

**Context File**: [`agents/instructions/CLAUDE.md`](agents/instructions/CLAUDE.md)

**Best For:**

- Implementation tasks
- Code reviews
- Documentation writing
- Browser automation workflows

### Gemini CLI (via Antigravity)

**Capabilities:**

- Strategic planning
- Architecture decisions
- Multi-file refactoring
- Long-context analysis

**Context File**: [`agents/instructions/GEMINI.md`](agents/instructions/GEMINI.md)

**Best For:**

- High-level design
- Codebase exploration
- Strategic decisions
- Complex architectural changes

### Multi-Agent Coordination

**Branch Strategy**: Each agent works on isolated branches
**Format**: `agent/<name>/<date>-<task>`

**Examples:**

- `agent/gemini/2026-01-29-expedia-onboarding`
- `agent/claude/2026-01-30-pricing-review`

See [`.agents/rules/git.md`](./.agents/rules/git.md) for full workflow.

## 📋 Workspace Standardization Plan

**Status**: Phase 1 + 2 - COMPLETE (2026-01-30)

**Track A Progress:**

| Phase                            | Status          | Notes                                                      |
| -------------------------------- | --------------- | ---------------------------------------------------------- |
| Phase 0: Foundations             | ✅ COMPLETE     | Linear MCP, .secrets/ access                               |
| **Phase 1: Rules Consolidation** | ✅ **COMPLETE** | All 4 rules created (.agents/rules/), agents/instructions/AGENTS.md refactored |
| **Phase 2: Linear Integration**  | ✅ **COMPLETE** | 29 issues migrated + audited (92 pts), standard template   |
| Phase 3: GitHub Integration      | 🔴 NOT STARTED  | Templates, CI/CD                                           |
| Phase 4: Great Consolidation     | 🔴 NOT STARTED  | Legacy cleanup                                             |

**Full Plan**: [`.agents/plans/comprehensive-transformation-plan.md`](./.agents/plans/comprehensive-transformation-plan.md)

## ⚠️ CRITICAL: Workspace Rules

> **ALL artifacts MUST be stored in `.agents/` folder**
> **NEVER** use `~/.claude/plans/` or any personal directory.

| Type      | Location             |
| :-------- | :------------------- |
| Plans     | `.agents/plans/`     |
| Artifacts | `.agents/artifacts/` |
| Sessions  | `.agents/sessions/`  |

**Before creating any plan:**

1. Check `.agents/plans/` for existing plans
2. Read `.agents/README.md` for rules
3. Cross-reference with other agents' work

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
- **Credentials**: `.secrets/.env.local` (HOTELRUNNER_TOKEN, HOTELRUNNER_HR_ID)
- **Rate Limits**: 250 requests/day, 5 requests/minute

**Capabilities**: Manage rooms, retrieve reservations, update calendar (rates/availability), real-time booking webhooks.

**See**: [`agents/instructions/AGENTS.md`](agents/instructions/AGENTS.md) for full capabilities list.

### Project Resources

**Branding & Design** - Logo design and brand identity documentation.

- **Logo Design Brief**: [`project/meta/logo-design-brief.md`](project/meta/logo-design-brief.md)
- **Status**: 🟡 Awaiting consultation with Said (Owner)
- **Workstream Entry**: Tracked in Linear (workstream deprecated)
- **Purpose**: Professional logo suite for Villa Thaifa (currently no formal branding exists)

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

_For all other contexts (Vision, Architecture, Roadmap), refer to `agents/instructions/AGENTS.md`._

## 📚 Knowledge Base

### Integration Guides

- **Linear**: `~/grid/memory/knowledge/integrations/linear-guide.md`
- **MCP Setup**: `~/grid/memory/knowledge/integrations/mcp-setup-by-cli.md`

### Patterns

- **Long-Running Agents**: `~/grid/memory/knowledge/patterns/long-running-agents.md`
- **MCP + Code Execution**: `~/grid/memory/knowledge/patterns/mcp-code-execution.md`
- **Project Management Stack**: `~/grid/memory/knowledge/patterns/project-management-stack.md`

### Operations

- **Capability Blindness RCA**: `~/grid/memory/knowledge/operations/capability-blindness-rca.md` ⚠️ **CRITICAL**
- **Risk Disclosure Protocol**: `~/grid/memory/knowledge/operations/risk-disclosure-protocol.md`
- **Verification Protocol**: `~/grid/memory/knowledge/operations/verification-protocol.md`

---

_For detailed rules, see files in `.agents/rules/`. For active work, check Linear workspace._

_**Last Updated**: 2026-01-30 during Phase 1 + 2 (Rules Consolidation + Linear Integration)_

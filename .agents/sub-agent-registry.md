# Inventory - Sub-Agent Registry

> **SSOT for Villa Thaifa sub-agents.** Generic agents are now centralized at org level.

---

## Model Selection Guidelines

| Model      | Complexity | Use Cases                                            | Speed   |
| ---------- | ---------- | ---------------------------------------------------- | ------- |
| **Haiku**  | Non/Low    | Summarizations, web searches, simple lookups         | Fastest |
| **Sonnet** | Low → Mid  | Browser automation, form filling, moderate analysis  | Fast    |
| **Opus**   | Mid → High | Complex reasoning, report generation, agent creation | Slower  |

> **Rule**: Always use the MINIMUM model capable of the task. Haiku by default, escalate only when needed.

---

## Org-Level Agents (Shared)

> **Location**: `@../../collective/who/agents/`

These generic agents have been migrated to the organization level for reuse across projects:

| Agent               | Purpose                | Model  |
| ------------------- | ---------------------- | ------ |
| `meta-agent`        | Agent creation         | opus   |
| `browser-agent`     | Chrome automation      | sonnet |
| `research-agent`    | Web research           | haiku  |
| `claude-md-agent`   | CLAUDE.md maintenance  | opus   |
| `incident-reporter` | Incident documentation | haiku  |
| `translation-agent` | Multilingual support   | haiku  |

---

## Villa Thaifa Agents (Local)

> **Location**: `.claude/agents/`

These agents are specific to Villa Thaifa hotel operations:

| Agent                 | Purpose                     | Tools                         | Model  | When to Use                                    |
| --------------------- | --------------------------- | ----------------------------- | ------ | ---------------------------------------------- |
| `platform-validator`  | Platform gatekeeper         | Read, Glob, Grep              | sonnet | BEFORE any HotelRunner/Booking.com operation   |
| `guest-communicator`  | Guest messaging             | Read, Write                   | sonnet | Welcome messages, check-in instructions        |
| `calendar-agent`      | Availability analysis       | Read, Glob, Grep              | sonnet | Checking availability, gaps, conflicts         |
| `pricing-analyst`     | Revenue optimization        | Read, Glob, Grep, WebSearch   | opus   | Pricing strategy review, rate optimization     |
| `reservation-manager` | Reservation lifecycle       | Read, Write, Edit, Glob, Grep | sonnet | Any reservation create/modify/cancel operation |
| `data-sync-checker`   | Data consistency validation | Read, Glob, Grep              | sonnet | BEFORE sync or when data drift suspected       |

---

## Agent Creation Protocol

When creating new Villa Thaifa-specific agents:

1. **CREATE** the agent file in `.claude/agents/<name>.md`
2. **VERIFY** the file was written successfully
3. **ADD** the new agent to the local agents table above
4. **REPORT** back to orchestrator with success/failure status

> **NOTE**: For generic/reusable agents, create at org level (`collective/who/agents/`) and reference from there.

> **CRITICAL**: If creation fails, use `incident-reporter` (org level) for structured logging.

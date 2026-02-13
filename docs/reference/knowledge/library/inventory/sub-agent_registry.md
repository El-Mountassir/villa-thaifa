# Inventory - Sub-Agent Registry

> **SSOT for Villa Thaifa sub-agents.** Generic agents are now centralized at org level.

---

## Model Selection Guidelines

| Model      | Complexity  | Use Cases                                            | Speed   |
| ---------- | ----------- | ---------------------------------------------------- | ------- |
| **Haiku**  | Non/Low     | Summarizations, web searches, simple lookups         | Fastest |
| **Sonnet** | Low -> Mid  | Browser automation, form filling, moderate analysis  | Fast    |
| **Opus**   | Mid -> High | Complex reasoning, report generation, agent creation | Slower  |

> **Rule**: Always use the MINIMUM model capable of the task. Haiku by default, escalate only when needed.

---

## Project-Level Agents

> **Location**: `.claude/agents/`

These generic/methodological agents are available for cross-project utility:

| Agent                    | Purpose                | Tools                                        | Model  | When to Use                                              |
| :----------------------- | :--------------------- | :------------------------------------------- | :----- | :------------------------------------------------------- |
| `meta-agent`             | Agent creation         | Read, Write, Edit, WebFetch, WebSearch       | opus   | Creating/configuring new sub-agents based on standards.  |
| `browser-agent`          | Chrome automation      | Read, Write, Chrome-MCP                      | sonnet | Web scraping, form filling, and platform interactions.   |
| `research-agent`         | Web research (Low)     | WebSearch, WebFetch, Read, Write             | haiku  | Researching documentation, tutorials, or general info.   |
| `claude-md-agent`        | CLAUDE.md maintenance  | Read, Edit, Write, Glob, WebSearch, WebFetch | opus   | Optimizing project instructions and governance files.    |
| `incident-reporter`      | Incident documentation | Read, Write, Glob                            | haiku  | Logging errors, failures, or unexpected system behavior. |
| `translation-agent`      | Multilingual support   | Read, Write                                  | haiku  | Translating between French, English, and Arabic.         |
| `auditor`                | Process auditing       | Chrome-MCP, Read, Write                      | sonnet | Enforcing "Brutal Excellence" standards via browser.     |
| `security-auditor`       | Security review        | Read, Write, Edit, Bash                      | opus   | Reviewing auth flows, vulnerabilities, and OWASP.        |
| `smart-contract-auditor` | Crypto security        | Specialized Tools                            | sonnet | Auditing DeFi protocols and smart contract exploits.     |

---

## Villa Thaifa Agents (Local)

> **Location**: `.claude/agents/`

These agents are specialized for Villa Thaifa hospitality operations:

| Agent                 | Purpose               | Tools                         | Model  | When to Use                                         |
| :-------------------- | :-------------------- | :---------------------------- | :----- | :-------------------------------------------------- |
| `platform-validator`  | Platform gatekeeper   | Read, Glob, Grep              | sonnet | BEFORE any platform operation.                      |
| `guest-communicator`  | Guest messaging       | Read, Write                   | sonnet | Drafting welcome messages or check-in instructions. |
| `calendar-agent`      | Availability analysis | Read, Glob, Grep              | sonnet | Checking room gaps, conflicts, or occupancy.        |
| `pricing-analyst`     | Revenue optimization  | Read, Glob, Grep, WebSearch   | opus   | Analyzing market rates for pricing recommendations. |
| `reservation-manager` | Reservation lifecycle | Read, Write, Edit, Glob, Grep | sonnet | Creating, modifying, or cancelling reservations.    |
| `data-sync-checker`   | Data sync validation  | Read, Glob, Grep              | sonnet | Detecting discrepancies between SSOT and platforms. |

---

## Agent Creation Protocol

When creating new Villa Thaifa-specific agents:

1. **CREATE** the agent file in `.claude/agents/<name>.md`.
2. **VERIFY** the file was written successfully and follows standards.
3. **ADD** the new agent to the local agents table above.
4. **REPORT** back to orchestrator with success/failure status.

> **NOTE**: For generic/reusable agents, create at org level and reference here.

> **CRITICAL**: If creation fails, use `incident-reporter` for structured logging.

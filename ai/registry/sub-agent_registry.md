# Sub-Agent Registry

> **SSOT for all sub-agents.** Meta-agent must update this file after creating new agents.

---

## Model Selection Guidelines

| Model       | Complexity    | Use Cases                                           | Speed   |
| ----------- | ------------- | --------------------------------------------------- | ------- |
| **Haiku**   | Non/Low       | Summarizations, web searches, simple lookups        | Fastest |
| **Sonnet**  | Low → Mid     | Browser automation, form filling, moderate analysis | Fast    |
| **Opus**    | Mid → High    | Complex reasoning, report generation, agent creation | Slower  |

> **Rule**: Always use the MINIMUM model capable of the task. Haiku by default, escalate only when needed.

---

## Registered Agents

| Agent                   | Purpose           | Tools             | Model  | When to Use                             |
| ----------------------- | ----------------- | ----------------- | ------ | --------------------------------------- |
| `browser-agent`         | Chrome automation | MCP Chrome tools  | sonnet | Web scraping, form filling, screenshots |
| `html-report-generator` | Report creation   | Read, Write, Glob | opus   | HTML/CSS/JS reports                     |
| `explore-agent`         | Codebase research | Glob, Grep, Read  | haiku  | Pattern discovery, file search          |
| `meta-agent`            | Agent creation    | Write, Firecrawl  | opus   | Creating new sub-agents                 |
| `research-agent`        | Web research      | WebSearch, WebFetch, Read, Write | haiku  | Best practices, docs lookup, comparisons |

---

## Agent Creation Protocol

When meta-agent creates a new sub-agent:

1. **CREATE** the agent file in `.claude/agents/<name>.md`
2. **VERIFY** the file was written successfully
3. **ADD** the new agent to the table above
4. **REPORT** back to orchestrator with success/failure status

> **CRITICAL**: If creation fails, meta-agent MUST report to orchestrator for incident logging.

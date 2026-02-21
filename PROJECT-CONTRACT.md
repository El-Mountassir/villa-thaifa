# Project Contract — Villa Thaifa

<!-- What this file is: operational conventions for agents working in this project.
     AGENTS.md defines workspace structure and file placement rules.
     This file defines WHO writes WHERE, which platforms are in scope, and how data flows.
     Copy this template, replace all {PLACEHOLDER} values, and commit at the project root. -->

---

## 1. Project Identity

| Field       | Value                       |
| ----------- | --------------------------- |
| Name        | Villa Thaifa                |
| Slug        | villa-thaifa                |
| Repo        | El-Mountassir/villa-thaifa  |
| Linear Team | VT                          |
| Repo root   | /home/director/villa-thaifa |

---

## 2. Agent Output Paths

| Agent type       | Output directory                                          | Notes                                      |
| ---------------- | --------------------------------------------------------- | ------------------------------------------ |
| browser-agent    | /home/director/villa-thaifa/data/pending-domains/browser/ | Screenshots, scraped HTML, raw extractions |
| research-agent   | ~/omar/knowledge/research/{DOMAIN}/                       | Findings and reports (global knowledge)    |
| general-purpose  | /home/director/villa-thaifa/ops/intake/                   | Unclassified artifacts awaiting triage     |
| linear-agent     | (in-memory only)                                          | Writes to Linear, no local file output     |
| Default fallback | /home/director/villa-thaifa/ops/intake/                   | When agent type is not listed above        |

---

## 3. Platform Conventions

| Platform    | Credentials location        | Agent guide                               | Safety                                 |
| ----------- | --------------------------- | ----------------------------------------- | -------------------------------------- |
| HotelRunner | ~/.hotelrunner (gitignored) | context/agents/hotelrunner/README.md      | Read-only unless explicitly authorized |
| Booking.com | ~/.booking (gitignored)     | context/agents/booking/README.md          | Read-only                              |
| Expedia     | (none stored)               | context/agents/browser/browser-context.md | Read-only extraction only              |
| WhatsApp    | (none stored)               | context/agents/browser/browser-context.md | Read-only unless Omar approves send    |

---

## 4. Agent Context Discovery

Pattern: `context/agents/{agent-name}/`

| File                   | Purpose                                               |
| ---------------------- | ----------------------------------------------------- |
| README.md              | Agent role, scope, and operating constraints          |
| extraction-protocol.md | Step-by-step extraction instructions for the platform |
| platform-rules.md      | Platform-specific safety and behavioral rules         |
| capabilities.md        | What this agent can and cannot do in this project     |

Agents MUST read their own `context/agents/{agent-name}/` directory before taking any platform action.

---

## 5. Data Flow Rules

```
External platform
      |
      v
Raw extraction --> /home/director/villa-thaifa/data/pending-domains/{DOMAIN}/     (unvalidated)
      |
      v
Validated data --> /home/director/villa-thaifa/data/{DOMAIN}/                     (reconciled, sourced)
      |
      v
Canonical truth --> /home/director/villa-thaifa/data/{DOMAIN}/{FILE}.md or .json  (single source of truth)
```

Rules:

- Raw extractions are NEVER edited in place.
- Conflicts between raw and canonical are logged before resolving.
- No data is promoted to canonical without a documented evidence source.

---

## 6. External References

| Resource                   | Canonical path                                               |
| -------------------------- | ------------------------------------------------------------ |
| Universal rules            | ~/omar/core/resources/rules/universal.md                     |
| Claude Code rules          | ~/.claude/rules/rules.md                                     |
| Agent definitions (shared) | ~/omar/core/resources/agents/                                |
| Linear workflow protocol   | ~/omar/operational/productivity/protocols/linear-workflow.md |
| Output styles              | ~/omar/core/context/output-styles/                           |
| Knowledge base             | ~/omar/knowledge/                                            |

---

<!-- CONTRACT VERSION: 1.0
     Template source: /home/director/Templates/PROJECT-CONTRACT.md
     Last updated: 2026-02-21 -->

# Incident Tracking — Villa Thaifa

> **Purpose**: Track and resolve issues encountered by AI agents.
> **Policy**: ALL incidents documented here, NOT in chat.

---

## Quick Links

| Status    | Directory                | Count |
| --------- | ------------------------ | ----- |
| Open      | [open/](open/)           | TBD   |
| Resolved  | [resolved/](resolved/)   | TBD   |
| Recurring | [recurring/](recurring/) | TBD   |

---

## Severity Levels

| Icon | Level    | Action Required             |
| ---- | -------- | --------------------------- |
| 🔴   | Critical | Immediate - blocks all work |
| 🟠   | Major    | High - blocks current task  |
| 🟡   | Minor    | Medium - workaround exists  |
| 🔵   | Info     | Low - FYI only              |

---

## Incident Types

| Type                | Examples                         |
| ------------------- | -------------------------------- |
| HTTP Errors         | 404, 403, 500, timeouts          |
| Tool Failures       | Permission denied, unavailable   |
| Data Issues         | Corrupted, incomplete, conflicts |
| Unexpected Behavior | Wrong output, silent failures    |
| System Warnings     | Deprecations, limits reached     |
| Blockers            | Deadlocks, missing resources     |

---

## File Naming

```
YYYY-MM-DD-HHmm-short-description.md
```

**Examples:**

- `2025-12-29-1430-webfetch-404-hotelrunner-support.md`
- `2025-12-29-1445-chrome-tab-disconnection.md`

---

## Template

```markdown
# Incident: [Short Description]

| Field     | Value                                   |
| --------- | --------------------------------------- |
| Date/Time | YYYY-MM-DD HH:mm                        |
| Severity  | 🔴/🟠/🟡/🔵                             |
| Type      | HTTP Error / Tool Failure / Data / etc. |
| Status    | Open / Resolved / Recurring             |

## Context

[What the agent was trying to do]

## Symptoms

[Exact error message, observed behavior]

## Impact

[Task blocked? Alternative found? Data lost?]

## Action Taken

[Alternative used / Escalated / Waiting]

## Resolution (if applicable)

[How it was fixed]

## Prevention (if applicable)

[How to avoid in future]
```

---

## Chat Notification Format

When logging an incident, notify in chat with:

```
⚠️ [Incident: Short description](docs/incidents/open/filename.md)
```

**Example:**

```
⚠️ [Incident: WebFetch 404](docs/incidents/open/2025-12-29-1430-webfetch-404.md)
```

---

_Incident Management System — Villa Thaifa_

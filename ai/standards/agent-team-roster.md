# Agent Team Roster — Villa Thaifa

> **Purpose**: Complete documentation of all agents needed for Villa Thaifa operations.
> **Pattern**: One team, complete coverage, clear responsibilities.

---

## Team Overview

```
┌─────────────────────────────────────────────────────────────────────────┐
│                        VILLA THAIFA AGENT TEAM                          │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                         │
│  ORCHESTRATOR (Claude Opus 4.5)                                         │
│       │                                                                 │
│       ├── INFRASTRUCTURE ─────┬── meta-agent (red)                      │
│       │                       └── claude-md-agent (white)               │
│       │                                                                 │
│       ├── OPERATIONS ─────────┬── browser-agent (cyan)                  │
│       │                       ├── platform-validator (yellow)           │
│       │                       └── reservation-manager (purple) [PLANNED]│
│       │                                                                 │
│       ├── INTELLIGENCE ───────┬── research-agent (green)                │
│       │                       ├── pricing-analyst (blue) [PLANNED]      │
│       │                       └── calendar-agent (green) [PLANNED]      │
│       │                                                                 │
│       ├── COMMUNICATION ──────┬── guest-communicator (pink) [PLANNED]   │
│       │                       └── translation-agent (cyan) [PLANNED]    │
│       │                                                                 │
│       └── QUALITY ────────────┬── incident-reporter (orange) [PLANNED]  │
│                               └── data-sync-checker (yellow) [PLANNED]  │
│                                                                         │
└─────────────────────────────────────────────────────────────────────────┘
```

---

## Current Team (Active)

| Agent | Color | Role | Status |
|-------|-------|------|--------|
| `meta-agent` | red | Creates new agents | ✅ Active |
| `browser-agent` | cyan | Chrome automation for platforms | ✅ Active |
| `research-agent` | green | Web research and documentation | ✅ Active |
| `claude-md-agent` | white | CLAUDE.md maintenance | ✅ Active |
| `platform-validator` | yellow | Validates before platform ops | ✅ Active |

---

## Planned Team (To Create)

### Priority 1 — Core Operations

| Agent | Color | Purpose | Why Needed |
|-------|-------|---------|------------|
| `incident-reporter` | orange | Creates incident reports when errors occur | Currently manual, should be automated |
| `reservation-manager` | purple | Handles reservation CRUD operations | Core business operation |
| `pricing-analyst` | blue | Analyzes pricing, makes recommendations | Revenue optimization |

### Priority 2 — Guest Experience

| Agent | Color | Purpose | Why Needed |
|-------|-------|---------|------------|
| `guest-communicator` | pink | Drafts guest communications | Consistent messaging |
| `translation-agent` | cyan | French/English/Arabic translations | Multi-language guests |

### Priority 3 — Data Quality

| Agent | Color | Purpose | Why Needed |
|-------|-------|---------|------------|
| `calendar-agent` | green | Availability analysis across platforms | Prevent double bookings |
| `data-sync-checker` | yellow | Validates data consistency HotelRunner↔Booking | Data integrity |

---

## Role Coverage Matrix

| Business Function | Current Coverage | Agent(s) | Gap |
|-------------------|------------------|----------|-----|
| **Agent Creation** | ✅ Full | meta-agent | None |
| **Browser Automation** | ✅ Full | browser-agent | None |
| **Web Research** | ✅ Full | research-agent | None |
| **Governance** | ✅ Full | claude-md-agent | None |
| **Platform Validation** | ✅ Full | platform-validator | None |
| **Incident Reporting** | ⚠️ Manual | — | Need: incident-reporter |
| **Reservations** | ⚠️ Partial | browser-agent | Need: reservation-manager |
| **Pricing** | ❌ None | — | Need: pricing-analyst |
| **Guest Comms** | ❌ None | — | Need: guest-communicator |
| **Translation** | ❌ None | — | Need: translation-agent |
| **Calendar Sync** | ❌ None | — | Need: calendar-agent |
| **Data Sync Check** | ❌ None | — | Need: data-sync-checker |

---

## Agent Specifications (Planned)

### incident-reporter (Priority 1)

```yaml
name: incident-reporter
description: Incident documentation specialist. Creates structured incident reports. Use PROACTIVELY when any error, failure, or unexpected behavior occurs.
color: orange
model: haiku
tools: Read, Write, Glob
permissionMode: default
```

**Purpose**: Automatically creates incident files at `docs/incidents/open/YYYY-MM-DD-HHmm-description.md` following project protocol.

---

### reservation-manager (Priority 1)

```yaml
name: reservation-manager
description: Reservation operations engineer. Handles reservation creation, modification, and cancellation. Use PROACTIVELY for any reservation-related task.
color: purple
model: sonnet
tools: Read, Write, Edit, Glob, Grep
permissionMode: default
```

**Purpose**: Manages reservation lifecycle, updates `data/specs/state/current/reservations.md`, coordinates with browser-agent for platform updates.

---

### pricing-analyst (Priority 1)

```yaml
name: pricing-analyst
description: Revenue optimization strategist. Analyzes pricing data and recommends rate adjustments. Use PROACTIVELY when pricing decisions are needed.
color: blue
model: opus
tools: Read, Glob, Grep, WebSearch
permissionMode: plan
```

**Purpose**: Analyzes occupancy, competitor rates, seasonal demand. Produces pricing recommendations for Omar's approval.

---

### guest-communicator (Priority 2)

```yaml
name: guest-communicator
description: Guest messaging specialist. Drafts professional guest communications. Use PROACTIVELY when guest messages need to be composed.
color: pink
model: sonnet
tools: Read, Write
permissionMode: default
```

**Purpose**: Creates welcome messages, check-in instructions, response templates. Maintains consistent voice per `data/admin/client/PROFILE.md`.

---

### translation-agent (Priority 2)

```yaml
name: translation-agent
description: Multilingual translator. Translates content between French, English, and Arabic. Use when translation is needed for guest communications or documentation.
color: cyan
model: haiku
tools: Read, Write
permissionMode: default
```

**Purpose**: Handles translation for Marrakech's international guests. Preserves tone and context.

---

### calendar-agent (Priority 3)

```yaml
name: calendar-agent
description: Availability analyzer. Analyzes room availability across platforms. Use PROACTIVELY to check for conflicts or optimize occupancy.
color: green
model: sonnet
tools: Read, Glob, Grep
permissionMode: plan
```

**Purpose**: Scans reservations, identifies gaps, flags conflicts. Supports revenue optimization.

---

### data-sync-checker (Priority 3)

```yaml
name: data-sync-checker
description: Data integrity validator. Validates consistency between HotelRunner and Booking.com. Use periodically or when sync issues are suspected.
color: yellow
model: sonnet
tools: Read, Glob, Grep
permissionMode: plan
```

**Purpose**: Compares platform data, flags discrepancies, prevents data drift.

---

## Team Statistics

| Metric | Current | Planned | Total |
|--------|---------|---------|-------|
| **Total Agents** | 5 | 7 | 12 |
| **By Model** | | | |
| └─ Haiku | 1 | 2 | 3 |
| └─ Sonnet | 2 | 4 | 6 |
| └─ Opus | 2 | 1 | 3 |
| **By Color** | | | |
| └─ Red (Creation) | 1 | 0 | 1 |
| └─ Orange (Debug) | 0 | 1 | 1 |
| └─ Yellow (Valid) | 1 | 1 | 2 |
| └─ Green (Research) | 1 | 1 | 2 |
| └─ Blue (Executive) | 0 | 1 | 1 |
| └─ Purple (Engineer) | 0 | 1 | 1 |
| └─ Cyan (Utility) | 1 | 1 | 2 |
| └─ Pink (Comms) | 0 | 1 | 1 |
| └─ White (Docs) | 1 | 0 | 1 |

---

## Creation Order

When creating planned agents, follow this order:

1. **incident-reporter** — Enables better error tracking immediately
2. **reservation-manager** — Core business operation
3. **pricing-analyst** — Revenue impact
4. **guest-communicator** — Guest experience
5. **translation-agent** — International guests
6. **calendar-agent** — Optimization
7. **data-sync-checker** — Data quality

---

## Usage

To create a planned agent:

```
Omar: "Crée l'agent incident-reporter"
Orchestrator: [Uses meta-agent with spec from this file]
```

The meta-agent should reference this roster for planned agent specifications.

---

_Agent Team Roster — Villa Thaifa Project_

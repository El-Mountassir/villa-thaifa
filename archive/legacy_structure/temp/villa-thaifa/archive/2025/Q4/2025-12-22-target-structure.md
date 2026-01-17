# Target Structure — Villa Thaifa v2.0

> **Purpose**: Study this BEFORE implementing. Don't be donkeys.
> **Date**: 2025-12-22

---

## 🎯 Proposed Structure v4 (EaC + Agentic AI)

```
thaifa/
│
├── .claude/                      # 🎭 ORCHESTRATOR (root = lead agent)
│   ├── commands/                 # Slash commands
│   ├── rules/                    # Behavioral rules
│   ├── agents/                   # Sub-agent configs
│   └── settings.local.json
│
├── archive/                      # 📦 ONE place for ALL history
│   └── 2025/Q4/
│       ├── briefs/
│       ├── reports/
│       └── execution/
│
├── core/                         # 🧠 AGENTIC AI CORE (NEW)
│   ├── contexts/                 # Agent context definitions
│   │   ├── hotel-ops.md          # Hotel operations context
│   │   ├── guest-comms.md        # Guest communication context
│   │   └── pricing.md            # Pricing context
│   ├── models/                   # Model configurations
│   │   ├── defaults.md           # Default model settings
│   │   └── specialized/          # Task-specific model configs
│   ├── prompts/                  # Prompt templates
│   │   ├── system/               # System prompts
│   │   ├── user/                 # User prompt templates
│   │   └── few-shot/             # Few-shot examples
│   └── tools/                    # Agent tools definitions
│       ├── hotelrunner/          # HotelRunner tools
│       ├── booking/              # Booking.com tools
│       └── communication/        # WhatsApp/email tools
│
├── data/                         # 📊 All data
│   ├── admin/                    # 🔒 Sensitive data
│   │   └── client/
│   │       ├── CONTACT.md
│   │       ├── CREDENTIALS.md
│   │       └── PROFILE.md
│   ├── specs/                    # 📋 Business specifications
│   │   ├── hotel/
│   │   │   ├── rooms.md
│   │   │   ├── pricing.md
│   │   │   └── reservations.md
│   │   │   └── CLAUDE.md         # ← Hierarchical context
│   │   ├── promotions/
│   │   │   ├── current.md
│   │   │   └── baseline.md
│   │   └── platform/
│   │       ├── rules.md
│   │       └── booking-com-data.md
│   └── communication/            # 💬 Messages
│       └── whatsapp/
│
├── docs/                         # 📚 Docs-as-Code
│   ├── briefs/                   # Active briefs
│   ├── templates/
│   ├── workflows/
│   │   └── CLAUDE.md             # ← Hierarchical context
│   ├── lessons-learned.md
│   └── services-transport.md
│
├── infra/                        # 🏗️ Infrastructure-as-Code
│   ├── docker/
│   └── envs/
│       ├── dev/
│       ├── staging/
│       └── prod/
│
├── project/                      # 🎯 Project management
│   ├── TODOs.md
│   ├── milestones.md
│   └── decisions.md
│
├── src/                          # 💻 Source code
│   ├── apps/                     # Applications
│   │   ├── dashboard/
│   │   │   └── CLAUDE.md         # ← Hierarchical context
│   │   ├── api/
│   │   │   └── CLAUDE.md         # ← Hierarchical context
│   │   └── automation/
│   ├── packages/                 # Shared libraries
│   └── tools/                    # Build scripts
│
├── CLAUDE.md                     # 🎭 ROOT CONTEXT (orchestrator)
├── README.md                     # Single entry point
├── ROADMAP.md                    # Strategic vision
└── .gitignore
```

### 🧠 Agentic AI Core Components

From [Anthropic's Context Engineering](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents):

| Component | Folder | Purpose |
|-----------|--------|---------|
| **Contexts** | `core/contexts/` | Domain-specific context definitions |
| **Models** | `core/models/` | Model configs, temperature, parameters |
| **Prompts** | `core/prompts/` | System prompts, templates, few-shot |
| **Tools** | `core/tools/` | Tool definitions (MCP-style) |

### 🎭 Hierarchical CLAUDE.md Pattern

```
CLAUDE.md (root)           ← Orchestrator, global rules
├── data/specs/hotel/CLAUDE.md    ← Hotel-specific context
├── docs/workflows/CLAUDE.md      ← Workflow-specific rules
├── src/apps/dashboard/CLAUDE.md  ← Dashboard dev context
└── src/apps/api/CLAUDE.md        ← API dev context
```

Each level inherits from parent + adds local context.

### Key EaC Principles Applied

| Principle | Folder | What's "as Code" |
|-----------|--------|------------------|
| **Docs-as-Code** | `docs/` | Markdown, version-controlled |
| **Config-as-Code** | `.claude/`, `infra/envs/` | Agent config, environments |
| **Infra-as-Code** | `infra/` | Docker, deployments |
| **Data-as-Code** | `data/specs/` | Business rules as structured files |
| **Agents-as-Code** | `core/` | Context, models, prompts, tools |

---

## 🔬 RESEARCH: Everything-as-Code (EaC) Patterns

From [monorepo best practices](https://lucapette.me/writing/how-to-structure-a-monorepo/) and [IaC structure guides](https://infrastructure-as-code.com/posts/repository-structure.html):

### EaC Folder Additions

| Folder | Purpose | Examples |
|--------|---------|----------|
| `infra/` | Infrastructure-as-Code | Terraform, Docker, K8s manifests |
| `config/` | Configuration-as-Code | ESLint, linters, CI/CD configs |
| `envs/` | Environment configs | dev/, staging/, prod/ |
| `tools/` | Build/utility scripts | Scripts, CLI tools |

### Monorepo Pattern (from [Monadical](https://monadical.com/posts/from-chaos-to-cohesion.html))

```
project/
├── apps/           # Applications
├── packages/       # Shared libraries
├── infra/          # IaC (Terraform, Docker)
├── config/         # Shared configs
├── tools/          # Build scripts
└── docs/           # Docs-as-Code
```

---

## ❓ QUESTIONS TO RESOLVE

### 1. What goes in `project/`?

| Option | Content                  | Rationale                |
| ------ | ------------------------ | ------------------------ |
| A      | TODOs, tasks, milestones | Project management stuff |
| B      | Briefs, requirements     | Project scope definition |
| C      | Both A + B               | Full project lifecycle   |
| D      | Something else?          | ???                      |

**Current `tasks/TODOs.md`** — should this go to `project/`?

### 2. `project/` vs `docs/briefs/`?

Is there overlap? Or are they different?

- `docs/briefs/` = reference documentation for tasks
- `project/` = active project management?

### 3. Relationship to parent `missions/`?

Parent org has `missions/` system. Should `project/` mirror that?

```
project/
├── active/      # Current work (like missions/active/)
├── queue/       # Ready to start
└── completed/   # Done (before archiving)
```

### 4. Or simpler?

```
project/
├── TODOs.md           # Current tasks
├── milestones.md      # Key dates/goals
└── decisions.md       # Project decisions
```

---

## 📊 Comparison: Current vs Target

| Aspect              | Current        | Target        |
| ------------------- | -------------- | ------------- |
| **Directories**     | 44             | ~18           |
| **History systems** | 3              | 1 (archive/)  |
| **State folders**   | 5              | 0 (→ specs/)  |
| **Entry points**    | 5 .md files    | 1 (README.md) |
| **Software-ready**  | ❌             | ✅ (app/)     |
| **Project mgmt**    | tasks/TODOs.md | project/      |

---

## 🤔 STUDY QUESTIONS

Before implementing, answer these:

1. **What is `project/` for exactly?**

   - Day-to-day task tracking?
   - Strategic planning?
   - Both?

2. **Does `specs/` need subfolders?**

   - `specs/hotel/` vs flat `specs/rooms.md`?
   - Is hierarchy helpful or overkill?

3. **Where do NEW reports go?**

   - `docs/` (documentation)?
   - `archive/` (historical)?
   - Temporary in `.claude/output/` then archive?

4. **Communication: active vs archived?**
   - Old WhatsApp messages → `archive/`?
   - Or keep all in `communication/`?

---

## ✏️ NOTES

_Add your thoughts here before we implement:_

-
-
- ***

_Don't implement until this is resolved._

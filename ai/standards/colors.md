# Color Semantic System

> **Purpose**: Define the complete color palette for agent role identification.
> **Pattern**: One color = One role type = One semantic meaning

---

## Complete Color Reference

| Color      | Role Type       | Semantic Meaning                           | Example Agents                    |
|------------|-----------------|--------------------------------------------|------------------------------------|
| **red**    | Creation        | Building, generating, scaffolding          | meta-agent, template-generator     |
| **orange** | Debugging       | Error investigation, flow analysis         | debugger, log-analyzer             |
| **yellow** | Validation      | Gatekeeper, checks, warnings, caution      | platform-validator, data-checker   |
| **green**  | Research        | Discovery, exploration, data gathering     | research-agent, explore-agent      |
| **blue**   | Executive       | Strategy, decisions, summaries, oversight  | planner, summarizer, orchestrator  |
| **purple** | Engineer        | Technical implementation, coding           | code-reviewer, implementer         |
| **cyan**   | Utility         | General purpose, helpers, formatting       | formatter, converter, helper       |
| **pink**   | Communication   | User-facing, messaging, notifications      | notifier, messenger, ui-agent      |
| **gray**   | Infrastructure  | System maintenance, background tasks       | cleaner, archiver, system-agent    |
| **white**  | Documentation   | Docs, reports, knowledge management        | doc-generator, claude-md-agent     |

---

## Color Selection Decision Tree

```
What is the agent's PRIMARY function?
│
├─► Creates/generates things? ────────────────► RED
│
├─► Investigates errors/debugging? ───────────► ORANGE
│
├─► Validates/checks before action? ──────────► YELLOW
│
├─► Researches/explores/gathers info? ────────► GREEN
│
├─► Makes decisions/strategizes? ─────────────► BLUE
│
├─► Implements/codes/engineers? ──────────────► PURPLE
│
├─► General helper/utility task? ─────────────► CYAN
│
├─► Communicates with users/sends messages? ──► PINK
│
├─► System maintenance/background? ───────────► GRAY
│
└─► Documentation/knowledge? ─────────────────► WHITE
```

---

## Color Psychology & Visual Hierarchy

| Color      | Visual Signal      | User Perception                |
|------------|--------------------|--------------------------------|
| **red**    | Action, creation   | "Something new is being made"  |
| **orange** | Warning, attention | "Investigating a problem"      |
| **yellow** | Caution, pause     | "Checking before proceeding"   |
| **green**  | Go, discovery      | "Finding information"          |
| **blue**   | Trust, authority   | "Making important decisions"   |
| **purple** | Technical, expert  | "Deep technical work"          |
| **cyan**   | Neutral, helper    | "General assistance"           |
| **pink**   | Friendly, social   | "Communicating with people"    |
| **gray**   | Background, system | "Maintenance happening"        |
| **white**  | Clean, knowledge   | "Documentation work"           |

---

## Usage Rules

1. **One primary color per agent** — No mixing
2. **Color = Role, not Task** — Choose based on what the agent IS, not what it does once
3. **Consistency** — Same role type = same color across all agents
4. **Default to cyan** — When role type is unclear, use cyan (utility)

---

## Examples by Color

### Red (Creation)
```yaml
name: meta-agent
color: red
# Creates new agent configurations
```

### Orange (Debugging)
```yaml
name: error-investigator
color: orange
# Analyzes errors and stack traces
```

### Yellow (Validation)
```yaml
name: platform-validator
color: yellow
# Validates data before platform operations
```

### Green (Research)
```yaml
name: research-agent
color: green
# Gathers information from web sources
```

### Blue (Executive)
```yaml
name: strategic-planner
color: blue
# Makes high-level implementation decisions
```

### Purple (Engineer)
```yaml
name: code-reviewer
color: purple
# Reviews code for quality and security
```

### Cyan (Utility)
```yaml
name: format-converter
color: cyan
# Converts between file formats
```

### Pink (Communication)
```yaml
name: guest-notifier
color: pink
# Sends notifications to hotel guests
```

### Gray (Infrastructure)
```yaml
name: log-archiver
color: gray
# Archives old log files
```

### White (Documentation)
```yaml
name: doc-generator
color: white
# Generates documentation from code
```

---

_Color Semantic System — Agent Creation Standards_

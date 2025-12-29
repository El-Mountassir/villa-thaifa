# Tunnel Vision Intervention Checklist

Step-by-step protocol for when tunnel vision risk is detected.

---

## The Three Phases

### STOP

Before responding, pause and ask:

1. "Am I seeing the complete context or just the target?"
2. "What PRECEDES this request?"
3. "Is this specific or general? What's the pattern?"
4. "What might I have forgotten?"
5. "Does something existing already cover this?"

### CHECK

| Check    | Question                          | Action if No               |
| -------- | --------------------------------- | -------------------------- |
| REARVIEW | Did I review what came before?    | Review previous context    |
| CONTEXT  | Do I understand the broader goal? | Ask or research            |
| EXISTING | Have I checked for existing work? | Search before creating     |
| TRACKING | Is progress being tracked?        | Ensure visibility          |
| LINEAR   | Have I scanned the Hub?           | Check Linear if applicable |

### PROCEED

Only after checks pass:

1. State what context you loaded
2. Confirm approach
3. Execute systematically
4. Track progress

---

## Output Format

When skill triggers, response should include:

```
TUNNEL VISION CHECK:
- [x] Previous context reviewed (or N/A for new)
- [x] Broader goal understood
- [x] Existing work checked
- [ ] Linear scanned (if applicable)
- [x] Progress tracking planned
```

Then proceed with the actual work.

---

## Anti-Patterns

### DO NOT

- Skip the check because "it's obvious"
- Rush through checklist mechanically
- Treat this as optional
- Forget to document what context was loaded

### DO

- Actually pause and reflect
- Be honest about gaps in understanding
- Ask for context if missing
- Document the check even when brief

---

## Example Interventions

### Creation Request

**Trigger:** "Create a new config file for the project"

**Without skill:** Creates config file immediately

**With skill:**

```
TUNNEL VISION CHECK:
- Checking for existing config files...
- Found: config.json (partial), .env (template)
- Broader context: This is for deployment configuration
- Previous work: Deployment was discussed in FOUNDER-87

Proceeding with config creation, extending existing config.json.
```

### Planning Request

**Trigger:** "What should we work on next?"

**Without skill:** Proposes options based on immediate memory

**With skill:**

```
TUNNEL VISION CHECK:
- REARVIEW: Let me review what was accomplished recently
- LINEAR: Scanning active projects and issues...
- PREVIOUS: Checking plan files and journal entries...

Based on context review:
[Informed proposal]
```

---

_"The checklist is the antidote to the rush."_

# Description Best Practices

> **Purpose**: Define how to write effective agent descriptions that trigger automatic delegation.
> **Critical**: The description field directly influences when Claude invokes the agent.

---

## Description Anatomy

```
[Role/Expertise]. [Primary Capability]. [Action Trigger].
```

### Components

| Component | Purpose | Example |
|-----------|---------|---------|
| **Role/Expertise** | What the agent IS | "Code review specialist" |
| **Primary Capability** | What it DOES | "Reviews code for quality and security" |
| **Action Trigger** | WHEN to use it | "Use immediately after writing code" |

---

## Action Trigger Phrases

### Proactive Triggers (Automatic Invocation)

| Phrase | When Claude Uses It |
|--------|---------------------|
| "Use PROACTIVELY when..." | Claude should invoke without being asked |
| "MUST BE USED for..." | Mandatory for certain tasks |
| "Use immediately after..." | Triggered by completing a task |
| "Use BEFORE any..." | Gatekeeper pattern |

### Conditional Triggers

| Phrase | When Claude Uses It |
|--------|---------------------|
| "Use when user requests..." | Only on explicit request |
| "Use if encountering..." | Triggered by specific conditions |
| "Use when needed for..." | Situational use |

---

## Templates by Role Type

### Red (Creation)
```
[Type] generator. Creates [output] from [input]. Use PROACTIVELY when user needs [output type].
```
**Example**: "Agent configuration generator. Creates sub-agents from descriptions. Use PROACTIVELY when user requests a new agent."

### Orange (Debugging)
```
[Area] debugging specialist. Investigates [problem type] and finds root causes. Use PROACTIVELY when [error condition].
```
**Example**: "Error investigation specialist. Analyzes stack traces and logs to find root causes. Use PROACTIVELY when any error or exception occurs."

### Yellow (Validation)
```
[Domain] validation gatekeeper. Validates [data type] before [action]. Use BEFORE any [platform/action].
```
**Example**: "Platform data validator. Validates reservation data before submission. Use BEFORE any HotelRunner or Booking.com operation."

### Green (Research)
```
[Domain] researcher. Gathers and synthesizes [information type]. Use PROACTIVELY when [knowledge need].
```
**Example**: "Documentation researcher. Finds and synthesizes best practices from multiple sources. Use PROACTIVELY when external knowledge is needed."

### Blue (Executive)
```
Strategic [role]. [Decision type] with [consideration]. Use BEFORE [complex task].
```
**Example**: "Strategic planner. Creates implementation plans with trade-off analysis. Use BEFORE starting any complex multi-step task."

### Purple (Engineer)
```
[Technical area] engineer. [Technical capability] following [standards]. Use PROACTIVELY when [technical task].
```
**Example**: "Code implementation engineer. Writes production-quality code following project patterns. Use PROACTIVELY when code changes are needed."

### Cyan (Utility)
```
[Function] utility. [Simple capability]. Use when [simple need].
```
**Example**: "Format converter utility. Converts between file formats. Use when format conversion is needed."

### Pink (Communication)
```
[Communication type] agent. [Messaging capability]. Use when [communication need].
```
**Example**: "Guest notification agent. Sends formatted messages to hotel guests. Use when guest communication is required."

### Gray (Infrastructure)
```
[System function] agent. [Maintenance capability]. Use [schedule/trigger].
```
**Example**: "Log archival agent. Archives logs older than 30 days. Use at end of each session or when storage is low."

### White (Documentation)
```
[Doc type] specialist. [Documentation capability]. Use when [doc need].
```
**Example**: "API documentation specialist. Generates docs from code comments. Use after API changes or when docs are requested."

---

## Good vs Bad Examples

### Good Descriptions

```
✅ "Expert code review specialist. Proactively reviews code for quality, security, and maintainability. Use immediately after writing or modifying code."

✅ "Platform validation gatekeeper. Validates all data before HotelRunner/Booking.com operations. Use BEFORE any platform submission to prevent errors."

✅ "Debugging specialist for errors, test failures, and unexpected behavior. Use PROACTIVELY when encountering any issues."
```

### Bad Descriptions

```
❌ "Code reviewer"
   Problem: Too vague, no trigger
   Fix: Add expertise + capability + trigger

❌ "Helps with debugging"
   Problem: Passive language, no directive
   Fix: Use active language with specific trigger

❌ "An agent that can do research"
   Problem: Vague capability, no when
   Fix: Specify research type and trigger condition

❌ "Validates things"
   Problem: No specificity
   Fix: What things? When? For what purpose?
```

---

## Checklist

Before finalizing a description:

- [ ] Has clear role/expertise statement
- [ ] Has specific primary capability
- [ ] Has action trigger phrase
- [ ] Uses active, not passive language
- [ ] Is specific, not vague
- [ ] Length: 1-3 sentences (not too long)

---

## Description Length Guidelines

| Length | Verdict | Example |
|--------|---------|---------|
| 1 sentence | Too short | "Validates data." |
| 2-3 sentences | Ideal | "Data validation gatekeeper. Validates all inputs before platform operations. Use BEFORE any HotelRunner action." |
| 4+ sentences | Too long | Trim to essentials |

---

_Description Best Practices — Agent Creation Standards_

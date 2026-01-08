# Tool Selection Patterns

> **Purpose**: Define tool selection patterns for different agent types.
> **Rule**: Always use MINIMUM tools required. Security through restriction.

---

## Available Tools

### Core Tools (Built-in)

| Tool | Purpose | Risk Level |
|------|---------|------------|
| `Read` | Read file contents | Low |
| `Write` | Create/overwrite files | Medium |
| `Edit` | Modify existing files | Medium |
| `Glob` | Find files by pattern | Low |
| `Grep` | Search file contents | Low |
| `Bash` | Execute shell commands | High |

### Web Tools

| Tool | Purpose | Risk Level |
|------|---------|------------|
| `WebSearch` | Search the web | Low |
| `WebFetch` | Fetch URL content | Low |

### MCP Tools (Project-Specific)

| Tool Pattern | Purpose | Example |
|--------------|---------|---------|
| `mcp__claude-in-chrome__*` | Browser automation | Screenshots, form filling |
| `mcp__firecrawl-mcp__*` | Advanced web scraping | Deep site crawling |

---

## Tool Patterns by Role Type

### Read-Only Pattern
```yaml
tools: Read, Glob, Grep
```
**Use for**: Validators, researchers, explorers, analyzers

**Agents**: `platform-validator`, `explore-agent`, `code-analyzer`

### Writer Pattern
```yaml
tools: Read, Write, Edit
```
**Use for**: Generators, modifiers, fixers

**Agents**: `doc-generator`, `code-fixer`

### Full Writer Pattern
```yaml
tools: Read, Write, Edit, Glob, Grep
```
**Use for**: Complex generators needing search + write

**Agents**: `meta-agent`, `claude-md-agent`

### Web Research Pattern
```yaml
tools: WebSearch, WebFetch, Read, Write
```
**Use for**: External information gathering

**Agents**: `research-agent`

### Browser Automation Pattern
```yaml
tools: Read, Write, mcp__claude-in-chrome__computer, mcp__claude-in-chrome__navigate, mcp__claude-in-chrome__read_page, mcp__claude-in-chrome__screenshot
```
**Use for**: Web automation, scraping, form filling

**Agents**: `browser-agent`

### Full Access Pattern
```yaml
# Omit tools field entirely
```
**Use for**: Agents that need all parent tools including MCP

**Note**: Only use when absolutely necessary

---

## Tool Selection Decision Tree

```
START: What does the agent need to do?
│
├─► Only read/search files?
│   └─► Read, Glob, Grep (Read-Only Pattern)
│
├─► Create or modify files?
│   ├─► Simple write? → Read, Write, Edit (Writer Pattern)
│   └─► Search + write? → Read, Write, Edit, Glob, Grep (Full Writer)
│
├─► Gather external info?
│   └─► WebSearch, WebFetch, Read, Write (Web Research Pattern)
│
├─► Automate browser?
│   └─► MCP Chrome tools (Browser Automation Pattern)
│
├─► Execute system commands?
│   └─► Add Bash (with caution)
│
└─► Need everything parent has?
    └─► Omit tools field (Full Access)
```

---

## Security Guidelines

### Risk Levels

| Level | Tools | Guideline |
|-------|-------|-----------|
| **Low** | Read, Glob, Grep, WebSearch, WebFetch | Safe to grant freely |
| **Medium** | Write, Edit | Grant when modification needed |
| **High** | Bash | Grant only when necessary |
| **Inherited** | (omit tools) | All parent tools including MCP |

### Principle of Least Privilege

1. **Start minimal** — Begin with read-only
2. **Add incrementally** — Add tools only when proven necessary
3. **Justify each tool** — Why does this agent need Write? Bash?
4. **Prefer restriction** — When in doubt, restrict

---

## Tool Inheritance

When `tools` field is **omitted**:
- Agent inherits ALL tools from parent conversation
- Includes MCP server tools
- Use only when agent truly needs everything

When `tools` field is **specified**:
- Agent gets ONLY listed tools
- Cannot access MCP tools unless explicitly listed
- Better security, more predictable behavior

---

## Examples

### Minimal Validator
```yaml
name: data-checker
tools: Read, Glob, Grep
# Only needs to read and search, never modify
```

### Code Generator
```yaml
name: boilerplate-generator
tools: Read, Write, Edit, Glob
# Needs to search patterns and create files
```

### Research Agent
```yaml
name: market-researcher
tools: WebSearch, WebFetch, Read, Write
# Needs web access and ability to save findings
```

### Dangerous Pattern (Avoid)
```yaml
name: simple-formatter
tools: Read, Write, Edit, Bash, Glob, Grep, WebSearch, WebFetch
# Over-provisioned! A formatter doesn't need Bash or web access
```

---

## Anti-Patterns

| Anti-Pattern | Why It's Wrong | Correction |
|--------------|----------------|------------|
| Bash for simple tasks | Security risk | Use specific tools |
| Full Access for validators | Over-privileged | Use Read-Only Pattern |
| WebSearch for local file search | Wrong tool | Use Glob, Grep |
| Write when only analyzing | Unnecessary risk | Remove Write |

---

_Tool Selection Patterns — Agent Creation Standards_

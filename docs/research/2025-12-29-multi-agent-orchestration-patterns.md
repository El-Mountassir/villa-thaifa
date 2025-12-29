# Multi-Agent AI Orchestration Best Practices

> **Research Date**: 2025-12-29
> **Purpose**: Improve Villa Thaifa orchestrator governance model
> **Conducted by**: research-agent (haiku)

---

## Research Summary

Multi-agent AI orchestration is rapidly evolving toward standardized patterns. Key findings:

1. **Context isolation is critical** — systems using isolated contexts achieve 67% lower token consumption
2. **Hierarchical structures are most resilient** — 5.5% performance degradation vs. 23.7% for flat structures
3. **Multi-agent architectures achieve 45% faster problem resolution**
4. **Model Context Protocol (MCP)** is emerging as the standard for cross-agent context management
5. **Context engineering is #1 challenge** — "most agent failures are context failures, not model failures"

---

## Sources

- [AI Agent Orchestration Patterns - Azure Architecture Center](https://learn.microsoft.com/en-us/azure/architecture/ai-ml/guide/ai-agent-design-patterns)
- [Multi-Agent Orchestration on AWS](https://aws.amazon.com/solutions/guidance/multi-agent-orchestration-on-aws/)
- [AI Agent Orchestration Frameworks 2025 - Kubiya](https://www.kubiya.ai/blog/ai-agent-orchestration-frameworks)
- [Multi-Agent Patterns in Google ADK](https://developers.googleblog.com/developers-guide-to-multi-agent-patterns-in-adk/)
- [Best Practices for Multi-Agent Orchestration - Skywork AI](https://skywork.ai/blog/ai-agent-orchestration-best-practices-handoffs/)
- [Context Engineering for AI Agents - Anthropic](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents)
- [Resilience in Multi-Agent LLM Systems - ArXiv](https://arxiv.org/html/2408.00989v4)

---

## Orchestration Patterns

| Pattern | Description | When to Use | Resilience |
| ------- | ----------- | ----------- | ---------- |
| **Hierarchical** | Higher-level agents plan, lower-level execute | Complex multi-step tasks | 5.5% degradation |
| **Sequential** | Tasks with strict dependencies | One must finish before next | Linear chain |
| **Parallel** | Independent tasks | Launch all simultaneously | Fan-out pattern |
| **Pipeline** | Output of one feeds next | Data transformation chains | With checkpoints |

---

## Context Management Strategies

| Strategy | How It Works | When to Use |
| -------- | ------------ | ----------- |
| **Context Offloading** | Move to external systems (DB, vector stores) | Long-term memory |
| **Context Reduction** | Compress history, summarize progress | Reduce token bloat |
| **Context Retrieval** | Dynamically fetch via tool calls | Just-in-time context |
| **Context Isolation** | Separate context per agent | Multi-agent workflows |

### Boundary Compression (Critical for Handoffs)

When Agent A hands off to Agent B:
1. Compress what was accomplished
2. Include only essential information
3. Use structured formats (JSON, Markdown)
4. Add metadata about context provenance

---

## Error Recovery Patterns

| Pattern | Function | Implementation |
| ------- | -------- | -------------- |
| **Challenger** | Each agent can challenge others' outputs | Peer review within agent group |
| **Inspector** | Dedicated agent reviews/corrects messages | Catches 96.4% of errors |
| **Circuit Breaker** | Stops cascading failures | Monitor reliability, disable if degraded |
| **Checkpoint/Retry** | Resume from last valid state | SDK checkpoint features |

### Production Reality

- 41-86.7% of multi-agent LLM systems fail in production
- 79% of failures from specification/coordination issues
- Human-in-the-loop mandatory for irreversible actions

---

## Model Selection Strategy

| Model | Cost | Speed | Complexity | Best For |
| ----- | ---- | ----- | ---------- | -------- |
| **Haiku** | 1x | Fastest | Low | File reads, syntax checks, formatting |
| **Sonnet** | 3.3x | Fast | Low→Mid | Daily dev, API integration, code reviews |
| **Opus** | 20x | Slower | Mid→High | Architecture, complex refactoring, final reviews |

**Rule**: Use minimum model capable. Switch mid-session to reduce costs 60-80%.

---

## Sub-Agent Briefing Protocol

### Mandatory Elements

| Element | What to Include |
| ------- | --------------- |
| **Objective** | Clear imperative statement |
| **File Paths** | Absolute paths (sub-agent can't access cwd) |
| **Constraints** | Quality standards, rules to follow |
| **Expected Output** | Format, location, structure |
| **Context Files** | List files to READ FIRST |
| **Success Criteria** | How to verify completion |

### Template

```
Agent [X], you are responsible for [specific task].

CONTEXT FILES TO READ FIRST:
- /path/to/file1.md (read for [reason])

OBJECTIVE:
Do [specific action] with [specific constraints].

CONSTRAINTS:
- Follow style guide at [path]
- Quality standard: [criterion]

EXPECTED OUTPUT:
- Format: [format]
- Location: [path]

SUCCESS CRITERIA:
- Verify: [check 1]
- Verify: [check 2]
```

---

## Recommendations for Villa Thaifa

| Priority | Action | Current Status |
| -------- | ------ | -------------- |
| ✅ | Hierarchical structure | Implemented |
| ✅ | Model selection (Haiku/Sonnet/Opus) | Implemented |
| ✅ | ZERO TOLERANCE + STOP & ASK | Gold-standard |
| ✅ | Formalized briefing protocol | Added to CLAUDE.md |
| 🟡 | Challenger/Inspector patterns | To add |
| 🔵 | MCP for shared context | Long-term |

---

*Research compiled from 14 sources — December 2025*

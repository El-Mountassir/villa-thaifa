# Villa Thaifa — Research Findings

**Version:** 0.1.0-alpha.0  
**Date:** 2026-01-09  
**Source:** "preparation" conversation + web search (2026-01-07)

---

## 1. AGENT SKILLS (GAME CHANGER)

**Release Date:** December 18, 2025  
**Type:** Open standard for progressive disclosure  
**Repository:** anthropics/skills (GitHub)

### What Are Agent Skills?

Agent Skills = **Unbounded context** through progressive disclosure.

| Concept | Definition |
|---------|------------|
| **Skills** | Teach agents HOW to use tools (knowledge layer) |
| **MCP** | Provides the actual tools themselves |
| **Key Difference** | Skills add knowledge without consuming context upfront |

### Skills vs Subagents

| Feature | Skills | Subagents |
|---------|--------|-----------|
| **Context** | Share parent context | Separate context window |
| **Purpose** | Add knowledge/capabilities | Run isolated tasks |
| **Persistence** | Loaded as needed | Independent execution |
| **Use Case** | Domain expertise | Task delegation |

### Key Features

- **Progressive disclosure:** Load only what's needed
- **Executable code:** Can include code snippets
- **Marketplace:** anthropics/skills repo
- **Installation:** `/plugin install` command

### Villa Thaifa Application

**Potential skills to create:**
- `hotelrunner-ops` — HotelRunner API operations
- `hospitality-marrakech` — Marrakech market knowledge
- `pricing-strategy` — Dynamic pricing algorithms
- `ota-management` — Multi-platform booking operations

**Action:** Study marketplace, create custom skills

---

## 2. CODE EXECUTION WITH MCP (CRITICAL PATTERN)

**Source:** Web research (anthropic.com, cefboud.com, github.com/toolprint)  
**Date:** July 2025 - January 2026

### The Context Window Problem

Traditional MCP approach has severe scaling issues:

| Scenario | Context Consumption | Impact |
|----------|-------------------|---------|
| **7 MCPs idle** | 67,300 tokens | **33.7% of context** |
| **59+ tools** | Degraded reasoning | Confused responses |
| **100+ tools** | Guaranteed failure | System collapse |

### The Solution: Code Execution

**Pattern:** Thin TypeScript wrappers + filesystem-based tool definitions

**Results:**
- Same 7 MCPs = ~2,000 tokens (~1% context)
- **98.7% context reduction**
- 500+ tools possible
- 10,000+ tools theoretical

### Architecture

```
MCP Server
  ├── Thin TypeScript wrapper (entry point)
  ├── Tool definitions (filesystem JSON)
  └── Dynamic loading (on-demand)
```

**Key Principle:** Tools defined but not loaded until called.

### Implementation References

| Resource | URL | Notes |
|----------|-----|-------|
| Anthropic Blog | anthropic.com/engineering/code-execution-with-mcp | Official pattern |
| HyperTool MCP | github.com/toolprint/hypertool-mcp | Reference implementation |
| Dynamic Context | cefboud.com/posts/dynamic-context-loading-llm-mcp/ | Deep dive |

### Comparison: Traditional vs Code Execution

| Metric | Traditional MCP | Code Execution MCP |
|--------|----------------|-------------------|
| **Context Overhead** | 20-35% | ~2% |
| **Tool Limit** | ~50 before degradation | 500+ possible |
| **Load Time** | All upfront | On-demand |
| **Scalability** | Poor | Excellent |

### Villa Thaifa Application

**HotelRunner MCP should use Code Execution pattern:**
- HotelRunner has extensive API (REST + XML)
- Potentially 100+ operations
- Traditional MCP would consume massive context
- Code Execution = scalable from day 1

**Decision:** Use Code Execution pattern for HotelRunner integration

---

## 3. MULTI-AGENT ORCHESTRATION PATTERNS

**Source:** GitHub research (2026-01-07)

### Key Repositories

#### claude-flow (ruvnet)
**Pattern:** Leading orchestration platform, MCP native  
**Key Features:**
- Built-in MCP support
- Visual workflow builder
- State management
- Event-driven architecture

**Villa Thaifa Relevance:** Could serve as orchestration backbone

---

#### ccswarm (nwiizo)
**Pattern:** Git worktree isolation for parallel agents  
**Key Features:**
- Each agent = separate git worktree
- Parallel execution without conflicts
- Merge coordination layer
- Isolated environments

**Villa Thaifa Relevance:** Parallel processing of multi-platform operations

---

#### agentrooms
**Pattern:** Multi-agent development workspace  
**Key Features:**
- Shared workspace
- Agent coordination
- Task distribution

**Villa Thaifa Relevance:** Collaborative agent development

---

#### claude-code-by-agents (disler)
**Pattern:** Desktop app with @mentions coordination  
**Key Features:**
- Natural @mention syntax
- Agent discovery
- Context sharing

**Villa Thaifa Relevance:** User-friendly agent interaction

---

## 4. INDYDEVDAN CURRICULUM

**Instructor:** Dan "IndyDevDan" Disler  
**Websites:** indydevdan.com, agenticengineer.com  
**YouTube:** @indydevdan  
**GitHub:** github.com/disler

### Curriculum Structure

#### PAC: Principled AI Coding
**Focus:** Foundational skills for AI coding  
**Goal:** Build principles that work with tools of today AND tomorrow  
**Format:** Private videos + Lookbox per lesson

#### TAC: Tactical Agentic Coding
**Focus:** Advanced agentic engineering  
**Goal:** "Scale FAR beyond AI Coding" — codebase that **runs itself**  
**Components:**
- Core tactics
- Agentic Horizon (future-facing)
- Real-world patterns

### Reference Implementation

**Repository:** orchestrator-agent-with-adws  
**Purpose:** Demo of multi-agent orchestration with specialized experts  
**Relevance:** Template for Villa Thaifa agent architecture

**Key Insight:**
> "Our agents are experts. You either use existing experts or create new specialized experts."

### Omar's Learning Path

**Current:** Enrolled in PAC + TAC  
**Need:** Digest video content into agent-optimized knowledge base  
**Solution:** Harvest MCP (to be created)

---

## 5. HARVEST MCP (FUTURE PROJECT)

**Status:** Does NOT exist yet — Omar's project to create  
**Purpose:** Unified multimedia transcription & digestion  
**Backend:** Gemini 3 Pro/Flash

### Objectives

| Goal | Description |
|------|-------------|
| **Transcription** | Video → Text (IndyDevDan courses) |
| **Digestion** | Text → Agent-optimized knowledge |
| **Knowledge Base** | Searchable, queryable course content |
| **Agent Training** | Feed expertise to specialist agents |

### Related Tools to Study

| Tool | Repository | Purpose |
|------|-----------|---------|
| gemini-video-mcp-server | GitHub | Video analysis via Gemini |
| video-analysis-mcp | GitHub | Video processing MCP |
| mcp-server-youtube-transcript | kimtaeyoon83 | YouTube transcript extraction |
| IndyDevDan's tools | Unknown | Transcript tooling |

### Villa Thaifa Relevance

**Not a blocker** for Villa Thaifa MVP, but:
- Future: Training agents on hospitality expertise
- Future: Onboarding new clients (digest training videos)
- Long-term: Knowledge management system

---

## 6. HOTELRUNNER API

**Platform:** HotelRunner Channel Manager  
**APIs Available:**
- REST API
- XML API

**Documentation:** developers.hotelrunner.com

### Integration Approach

**Recommendation:** Custom MCP using Code Execution pattern

**Rationale:**
1. HotelRunner API likely has 50+ operations
2. Traditional MCP would bloat context
3. Code Execution = scalable from start
4. Can add operations without context penalty

### Operations Likely Needed

| Category | Examples |
|----------|----------|
| **Inventory** | Get rooms, update availability |
| **Pricing** | Get rates, update pricing |
| **Bookings** | List reservations, create/cancel |
| **Platforms** | Sync status, error handling |
| **Analytics** | Revenue reports, occupancy |

---

## 7. CRITICAL INSIGHTS

### 7.1 Context Window is Precious

**Finding:** Traditional MCP architecture doesn't scale  
**Impact:** Villa Thaifa needs Code Execution from day 1  
**Action:** Study hypertool-mcp implementation

### 7.2 Agent Skills Changed the Game

**Finding:** Progressive disclosure solves "too much context" problem  
**Impact:** Can add domain expertise without context penalty  
**Action:** Create hospitality skills for Villa Thaifa agents

### 7.3 Orchestration Hierarchy is Proven

**Finding:** Chief + Lead pattern works (IndyDevDan's implementation)  
**Impact:** Villa Thaifa should implement full hierarchy  
**Action:** Model after orchestrator-agent-with-adws

### 7.4 Multi-Agent Patterns Exist

**Finding:** Multiple proven patterns (claude-flow, ccswarm, agentrooms)  
**Impact:** Don't reinvent the wheel  
**Action:** Study and adapt existing patterns

---

## 8. RECOMMENDED NEXT RESEARCH

| Topic | Priority | Why |
|-------|----------|-----|
| **hypertool-mcp deep dive** | P0 | Need implementation details |
| **Agent Skills marketplace** | P1 | Understand available skills |
| **claude-flow documentation** | P1 | Potential orchestration platform |
| **HotelRunner API documentation** | P0 | Understand full capability |
| **Go Siyaha financing** | P2 | Financial opportunity |

---

## 9. ACTION ITEMS

| # | Action | Owner | Priority | Status |
|---|--------|-------|----------|--------|
| 1 | Study hypertool-mcp implementation | Omar/Lux | P0 | ⏳ TODO |
| 2 | Create HotelRunner MCP (Code Execution) | Omar/Agents | P0 | ⏳ TODO |
| 3 | Explore Agent Skills marketplace | Omar/Lux | P1 | ⏳ TODO |
| 4 | Study orchestrator-agent-with-adws | Omar/Lux | P1 | ⏳ TODO |
| 5 | Research Go Siyaha | Omar | P2 | ⏳ TODO |
| 6 | Plan Harvest MCP architecture | Omar/Lux | P2 | ⏳ TODO |

---

**Sources:**
- "preparation" conversation (2026-01-07 to 2026-01-09)
- Web search results (anthropic.com, github.com, various)
- IndyDevDan curriculum materials

**Next Update:** As new research emerges

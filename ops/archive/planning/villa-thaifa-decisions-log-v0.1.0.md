# Villa Thaifa — Decisions Log

**Version:** 0.1.0-alpha.0  
**Date:** 2026-01-09  
**Purpose:** Record all architectural, strategic, and technical decisions

---

## DECISION RECORD FORMAT

Each decision includes:
- **ID:** Unique identifier
- **Date:** When decided
- **Status:** Proposed / Accepted / Superseded / Deprecated
- **Context:** Why this decision was needed
- **Decision:** What was decided
- **Consequences:** Impact of this decision
- **Alternatives Considered:** What else was evaluated

---

## D-001: Adopt Everything-as-Code (EaC) Methodology

**Date:** 2026-01-07  
**Status:** ✅ ACCEPTED  
**Decider:** Omar El Mountassir

### Context
- Current repo is document-heavy ("bordel total")
- Format is "comme si on était en 1995"
- Agents cannot execute on documents
- Need machine-readable, version-controlled system

### Decision
Apply Everything-as-Code (EaC) paradigm across the entire project:
- Infrastructure as Code
- Configuration as Code
- Documentation as Code
- Policy as Code

### Consequences

**Positive:**
- Agents can execute directly
- Version control for all changes
- Consistency and repeatability
- Traceability

**Negative:**
- Upfront transformation effort
- Learning curve for Said (client)
- More rigid structure

### Alternatives Considered
- Keep document-based (rejected - not scalable)
- Hybrid approach (rejected - complexity)

---

## D-002: HotelRunner as Single Source of Truth

**Date:** 2026-01-07  
**Status:** ✅ ACCEPTED  
**Decider:** Omar + Said (implicit)

### Context
- Multiple booking platforms (Booking.com, Expedia, Airbnb, etc.)
- Need consistent inventory/pricing across all
- Manual sync = high error risk

### Decision
Use HotelRunner Channel Manager as the single source of truth for:
- Room inventory
- Pricing
- Availability
- Bookings

All platforms sync via HotelRunner.

### Consequences

**Positive:**
- Single place to manage everything
- Automatic propagation to OTAs
- Reduced manual work
- Lower risk of overbooking

**Negative:**
- Dependency on HotelRunner API
- Platform lock-in
- Migration effort if switching later

### Alternatives Considered
- Direct integration with each OTA (rejected - too complex)
- Custom aggregator (rejected - reinventing the wheel)

---

## D-003: Room Configuration by Number (Not Type)

**Date:** 2026-01-07  
**Status:** ✅ ACCEPTED  
**Decider:** Said Thaifa

### Context
- Booking.com uses "Room Type" (grouped)
- HotelRunner uses "Room Number" (individual)
- Mismatch causes confusion

### Decision
Standardize on **Room Number** configuration across all platforms.

**Rationale:**
- More granular control
- Matches Said's preference
- Easier to track specific rooms
- Better for maintenance/cleaning schedules

### Consequences

**Positive:**
- Clear identification of each room
- Better operational control
- Aligns with HotelRunner config

**Negative:**
- Requires reconfiguring Booking.com
- More entries to manage (but more precise)

### Alternatives Considered
- Keep Room Type on Booking.com (rejected - inconsistent)
- Hybrid approach (rejected - confusing)

---

## D-004: Target Platform Priority

**Date:** 2026-01-07  
**Status:** ⏳ PROPOSED (awaiting Said confirmation)  
**Decider:** TBD

### Context
- 10+ OTA platforms available
- Limited bandwidth to integrate all at once
- Need prioritization strategy

### Decision (Proposed)

**P0 (Critical):**
- Booking.com ✅ (already connected)
- Expedia 🔄 (in progress)

**P1 (High Priority):**
- Airbnb
- VRBO
- TripAdvisor
- Google Hotels

**P2 (Medium Priority):**
- Trivago
- Agoda
- Hotels.com (via Expedia)
- Trip.com

### Consequences
TBD - pending Said's validation

### Alternatives Considered
- Connect all simultaneously (rejected - too risky)
- Only Booking.com + Expedia (rejected - missing major platforms)

---

## D-005: Code Execution over MCP (Preferred)

**Date:** 2026-01-07  
**Status:** ⏳ PROPOSED  
**Decider:** Omar El Mountassir

### Context
- Two integration patterns available:
  1. MCP Server (Model Context Protocol)
  2. Code Execution (via Anthropic/Cloudflare/Docker)
- Context window is precious resource
- Need scalability to hundreds/thousands of operations

### Decision (Tentative)
Prefer **Code Execution** pattern over MCP when possible.

**Rationale:**
> "Thousands of tools without context window bloat"

- Preserves context window for reasoning
- More scalable
- Modular architecture
- Emerging best practice (2025-2026)

### Consequences

**Positive:**
- Efficient context window usage
- Scalable to large tool sets
- Future-proof architecture

**Negative:**
- Newer pattern (less mature)
- May require custom tooling
- Learning curve

### Alternatives Considered
- Pure MCP approach (valid, but limited by context window)
- Hybrid (possible - evaluate per use case)

**Status:** Research required on Anthropic/Cloudflare/Docker implementations

---

## D-006: Multi-Tenant Architecture from Day 1

**Date:** 2026-01-07  
**Status:** ✅ ACCEPTED  
**Decider:** Omar El Mountassir

### Context
- Villa Thaifa = first client
- More clients expected soon
- Don't want to rebuild from scratch for each client

### Decision
Design architecture with multi-tenancy in mind from the start:
- Tenant isolation (data, config)
- Scalable patterns
- Reusable components

### Consequences

**Positive:**
- Faster onboarding for future clients
- Shared infrastructure cost
- Consistent quality

**Negative:**
- More complex initial design
- Over-engineering risk for single client

**Mitigation:**
- Start simple, but with extension points
- Don't build features not needed yet
- Focus on Villa Thaifa, design for more

### Alternatives Considered
- Client-specific builds (rejected - not scalable)
- Wait until 2nd client (rejected - technical debt)

---

## D-007: Agent Orchestration Hierarchy

**Date:** 2026-01-07 (Resolved: 2026-01-09)  
**Status:** ✅ RESOLVED  
**Decider:** Omar + research from "preparation" conversation

### Context
- Complex workflows require coordination
- Different levels of reasoning needed
- Resource optimization important
- Question raised: "Is Chief + Lead overkill?"

### Decision

**RESOLVED: Chief + Lead is INTENTIONAL, not overkill.**

**Hierarchy:**
```
Chief Orchestrator (Claude Opus 4.5)
  └─ Lead Orchestrator (Claude Sonnet 4.5)
      └─ Worker Agents (Sonnet/Haiku/Gemini)
```

**Rationale:**
- **Chief** = Strategic reasoning, high-level planning
- **Lead** = Tactical execution, workflow coordination
- Separation allows cost optimization (Opus for strategic, Sonnet for tactical)
- Proven pattern in IndyDevDan's orchestrator-agent-with-adws

### Consequences

**Positive:**
- Clear separation of concerns
- Cost-efficient (reserve Opus for strategic thinking only)
- Scalable to complex multi-agent workflows

**Negative:**
- Additional complexity in coordination
- One more layer to debug

### Alternatives Considered
- Single orchestrator (rejected - lacks strategic/tactical separation)
- Flat architecture (rejected - no coordination)

---

## D-008: Repo Structure (TBD)

**Date:** 2026-01-07  
**Status:** 🔴 OPEN  
**Decider:** TBD

### Context
- Need to organize Villa Thaifa within broader structure
- Omar's system architecture evolving
- Multiple perspectives (Nexus, collective/, clients/)

### Decision
**OPEN QUESTION:** Where does Villa Thaifa live?

**Options:**
1. `~/el-mountassir/projects/villa-thaifa/`
2. `~/nexus/clients/villa-thaifa/`
3. `~/clients/villa-thaifa/` (separate top-level)

### Consequences
Impacts:
- Code organization
- Agent landing zones
- Reusability patterns

**Status:** Blocked pending overall architecture decision

---

## D-009: Legal Structure (Context, Not Decision)

**Date:** 2026-01-07  
**Status:** ℹ️ CONTEXT  
**Decider:** N/A (Omar's existing status)

### Context
- Omar operates as **Auto-Entrepreneur** (Morocco)
- **Statut:** Auto-Entrepreneur
- **Activité:** Prestations de Services (Tech/Consulting)
- **Régime fiscal:** Libératoire (IR)
- **Base calcul:** CA Encaissé (Cash Basis)
- **Charges déductibles:** false
- **TVA applicable:** false
- **Plafond annuel:** 200,000 MAD
- **Seuil alerte:** 180,000 MAD
- **Taux imposition:** 1%

This is NOT a decision but important context for:
- Contract structure
- Invoicing
- Legal limits
- Growth constraints

---

## D-010: Go Siyaha Financing (To Investigate)

**Date:** 2026-01-08  
**Status:** ℹ️ CONTEXT  
**Decider:** N/A (potential opportunity)

### Context
Mentioned in BRIEF-2026-01-08.md:
> "Go Siyaha = financement 90% possible"

### Action Required
- Research Go Siyaha program
- Eligibility criteria
- Application process
- Impact on project structure

**Status:** No decision yet, investigation needed

---

## D-011: Transform Question ("App" Definition)

**Date:** 2026-01-08  
**Status:** ℹ️ OPEN QUESTION  
**Decider:** TBD (needs clarification with Said)

### Context
From BRIEF-2026-01-08.md:
> "Question centrale: 'Transformer en app' = quoi exactement?"

Said wants to "transform into an app" but scope unclear.

**Possible Interpretations:**
1. Web application (dashboard)
2. Mobile app (iOS/Android)
3. Automation system (backend only)
4. Hybrid (web + mobile + automation)

### Action Required
Clarify with Said:
- What does "app" mean to him?
- What functionality is must-have vs nice-to-have?
- User personas (Said, staff, guests?)

**Status:** Blocking major architectural decisions

---

## DECISION SUMMARY

| ID | Decision | Status | Priority |
|----|----------|--------|----------|
| D-001 | EaC Methodology | ✅ Accepted | HIGH |
| D-002 | HotelRunner as SSOT | ✅ Accepted | HIGH |
| D-003 | Room by Number | ✅ Accepted | MEDIUM |
| D-004 | Platform Priority | ⏳ Proposed | HIGH |
| D-005 | Code Execution preferred | ⏳ Proposed | MEDIUM |
| D-006 | Multi-tenant design | ✅ Accepted | HIGH |
| D-007 | Orchestration hierarchy | ✅ **RESOLVED** | MEDIUM |
| D-008 | Repo structure | 🔴 Open | HIGH |
| D-009 | Legal structure (context) | ℹ️ Context | N/A |
| D-010 | Go Siyaha (context) | ℹ️ Context | LOW |
| D-011 | "App" definition | 🔴 Open | HIGH |

---

## D-012: Harvest MCP Clarification

**Date:** 2026-01-09  
**Status:** ℹ️ CLARIFIED  
**Decider:** Omar

### Context
- Initial confusion: "Harvest MCP" mentioned as if it existed
- IndyDevDan has YouTube transcript tools
- Community MCPs exist: gemini-video-mcp-server, video-analysis-mcp

### Clarification

**Harvest MCP does NOT exist yet.**

**Harvest = Omar's project TO CREATE:**
- Purpose: Unified multimedia transcription & digestion
- Backend: Gemini 3 Pro/Flash
- Goal: Agent-optimized knowledge bases
- Target content: IndyDevDan courses (PAC/TAC), video lessons

**Related existing tools to study:**
- `gemini-video-mcp-server` (GitHub)
- `video-analysis-mcp` (GitHub)
- `mcp-server-youtube-transcript` (kimtaeyoon83)
- IndyDevDan's transcript tools

### Consequences

**Action Required:**
- Harvest MCP is a FUTURE project
- Not a blocker for Villa Thaifa
- Can leverage existing MCP patterns when building it

---

**Legend:**
- ✅ Accepted = Decided and committed
- ⏳ Proposed = Awaiting validation
- 🔴 Open = Not yet decided
- ℹ️ Context = Information, not a decision

---

**Next:** See `villa-thaifa-open-questions.md` for items needing resolution.

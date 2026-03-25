# Villa Thaifa — Open Questions

**Version:** 0.1.0-alpha.0  
**Date:** 2026-01-09  
**Purpose:** Track unresolved questions blocking progress

---

## QUESTION CATEGORIES

- **B:** Business (client requirements, scope)
- **T:** Technical (architecture, implementation)
- **O:** Operational (process, workflow)
- **F:** Financial (budget, contracts)

---

## CRITICAL QUESTIONS (Blocking)

### B-001: What Does "Transform to App" Mean?

**Priority:** 🔴 CRITICAL  
**Blocker for:** Architecture decisions, scope definition  
**Asked to:** Said Thaifa  
**Status:** ⏳ AWAITING RESPONSE

**Question:**
When you say "transform to app", what specifically do you mean?

**Options:**
- [ ] Web dashboard (browser-based management)
- [ ] Mobile app (iOS/Android for on-the-go)
- [ ] Backend automation (no UI, just smart systems)
- [ ] Hybrid (web + mobile + automation)
- [ ] Something else (please describe)

**Follow-up:**
- Who will use it? (Said only, staff, guests?)
- What are must-have vs nice-to-have features?
- Timeline expectations?

**Impact:** Determines entire technical approach

---

### B-002: Platform Priority Confirmation

**Priority:** 🔴 HIGH  
**Blocker for:** Integration roadmap  
**Asked to:** Said Thaifa  
**Status:** ⏳ AWAITING RESPONSE

**Question:**
Is this platform priority list correct for Marrakech?

**Proposed List:**

**P0 (Critical - Now):**
- Booking.com ✅
- Expedia 🔄

**P1 (High - Next):**
- Airbnb
- VRBO
- TripAdvisor
- Google Hotels

**P2 (Medium - Later):**
- Trivago
- Agoda
- Hotels.com
- Trip.com

**Follow-up:**
- Any platforms missing?
- Any to add to P1?
- Timeline for each priority group?

---

### B-003: Room Numbering Scheme

**Priority:** 🟡 MEDIUM  
**Blocker for:** Database schema, Booking.com reconfiguration  
**Asked to:** Said Thaifa  
**Status:** ⏳ AWAITING RESPONSE

**Question:**
What is your exact room numbering scheme?

**Need:**
- Complete list of room numbers (e.g., 101, 102, 103... or A1, A2, B1, B2...)
- Room types for each number (if any)
- Capacity for each room
- Special characteristics/facilities per room

**Impact:** Database design, platform configuration

---

### F-001: Contract & Budget

**Priority:** 🔴 CRITICAL  
**Blocker for:** Starting work officially  
**Asked to:** Said Thaifa  
**Status:** ⏳ NO CONTRACT SIGNED

**Questions:**
1. **Budget allocation:**
   - What is your budget for this project?
   - Payment structure? (Fixed price, hourly, milestone-based)

2. **Timeline:**
   - When do you need Phase 1 complete?
   - Acceptable delivery timeline?

3. **Scope:**
   - What is in-scope vs out-of-scope?
   - Change request process?

**Context:**
- Current status: "Contracting but already in action"
- Risk: Scope creep without signed agreement
- Omar's concern: 1 week revenue loss

**Action:** Draft SOW (Statement of Work) for signature

---

### F-002: Go Siyaha Financing

**Priority:** 🟢 LOW (Opportunity)  
**Blocker for:** N/A  
**Research needed:** Yes  
**Status:** 🔍 TO INVESTIGATE

**Questions:**
1. What is Go Siyaha?
2. What does "90% financing" mean?
   - 90% of what? (Project cost, equipment, operations?)
   - Terms and conditions?
3. Eligibility criteria for Villa Thaifa?
4. Application process and timeline?
5. Impact on project structure/ownership?

**Action:** Omar to research online

---

## TECHNICAL QUESTIONS

### T-001: MCP vs Code Execution

**Priority:** 🟡 MEDIUM  
**Blocker for:** Implementation approach  
**Decider:** Omar + Lux  
**Status:** 🔍 RESEARCH NEEDED

**Question:**
Should we use MCP servers or Code Execution pattern for HotelRunner integration?

**MCP (Model Context Protocol):**
- ✅ Standard approach
- ✅ Well-documented
- ❌ Context window consumption

**Code Execution:**
- ✅ Preserves context window
- ✅ Scalable (thousands of tools)
- ❌ Newer pattern (less mature)
- 🔍 Need research: Anthropic, Cloudflare, Docker (July 2025-Jan 2026)

**Decision Criteria:**
- Complexity of HotelRunner operations
- Number of tools needed
- Token budget
- Maintenance burden

**Action:** Research Code Execution implementations

---

### T-002: Orchestration Hierarchy

**Priority:** ✅ **RESOLVED**  
**Blocker for:** N/A  
**Decider:** Omar + research  
**Status:** ✅ CLOSED (2026-01-09)

**Question:**
Do we need **both** Chief Orchestrator AND Lead Orchestrator?

**ANSWER: YES - Intentional design, not overkill.**

**Rationale:**
- **Chief (Opus 4.5):** Strategic reasoning, high-level planning
- **Lead (Sonnet 4.5):** Tactical execution, workflow coordination
- Separation allows cost optimization (Opus only for strategic thinking)
- Proven pattern in IndyDevDan's orchestrator-agent-with-adws

**Decision:** Implement full hierarchy as proposed
```
Lead (Claude Opus/Sonnet) - Coordination + strategy
  └─ Workers - Execution
```

**Decision Criteria:**
- Workflow complexity
- Budget (Opus calls expensive)
- YAGNI principle

**Action:** Start simple (single orchestrator), add Chief if needed

---

### T-003: Database Choice

**Priority:** 🟡 MEDIUM  
**Blocker for:** Data layer design  
**Decider:** Omar + Lux  
**Status:** ⏳ OPEN

**Question:**
SQLite or PostgreSQL?

**SQLite:**
- ✅ Simple, file-based
- ✅ No server needed
- ✅ Good for single-tenant
- ❌ Limited concurrency
- ❌ No network access

**PostgreSQL:**
- ✅ Production-grade
- ✅ Multi-tenant ready
- ✅ Network access
- ❌ Requires server
- ❌ More complex

**Decision Criteria:**
- Expected load
- Multi-tenant needs
- Hosting constraints
- Backup/restore requirements

**Recommendation:** Start with SQLite, migrate to Postgres if needed

---

### T-004: Repo Structure

**Priority:** 🟡 MEDIUM  
**Blocker for:** Code organization  
**Decider:** Omar  
**Status:** 🔴 BLOCKED (pending overall architecture)

**Question:**
Where does Villa Thaifa repo live?

**Options:**

**Option A:** `~/el-mountassir/projects/villa-thaifa/`
- Within personal system structure
- Alongside other projects

**Option B:** `~/nexus/clients/villa-thaifa/`
- Within Nexus ecosystem
- Aligns with "clients" category

**Option C:** `~/clients/villa-thaifa/`
- Separate top-level clients directory
- Clean separation

**Impact:**
- Agent landing zones
- Code reusability
- Mental model

**Action:** Resolve overall architecture first (collective/ vs nous/ etc.)

---

### T-005: Hosting Platform

**Priority:** 🟢 LOW (can decide later)  
**Blocker for:** Deployment strategy  
**Decider:** Omar + Lux  
**Status:** ⏳ OPEN

**Question:**
Where to host the application?

**Options:**

**Cloudflare Workers:**
- ✅ Edge computing
- ✅ Global CDN
- ❌ Execution limits

**Vercel:**
- ✅ Easy deployment
- ✅ Frontend + serverless
- ❌ Cost at scale

**Railway/Render:**
- ✅ Full backend
- ✅ Database hosting
- ❌ Regional (not edge)

**Self-hosted VPS:**
- ✅ Full control
- ✅ Cost-effective long-term
- ❌ Maintenance burden

**Decision Criteria:**
- Cost
- Scalability
- Maintenance
- Agent compatibility

---

### T-006: Monitoring Solution

**Priority:** 🟢 LOW  
**Blocker for:** Observability  
**Decider:** Omar + Lux  
**Status:** ⏳ OPEN

**Question:**
What monitoring/observability tools to use?

**Options:**
- Sentry (error tracking)
- Datadog (full observability, expensive)
- Prometheus + Grafana (open source, complex)
- Simple logging (MVP approach)

**Decision:** Start simple, add as needed

---

## OPERATIONAL QUESTIONS

### O-001: Agent Training Process

**Priority:** 🟡 MEDIUM  
**Blocker for:** Agent effectiveness  
**Decider:** Omar  
**Status:** ⏳ OPEN

**Question:**
How do we systematically train agents for Villa Thaifa operations?

**Needs:**
- Agent Skills definitions
- Training materials
- Validation process
- Performance metrics

**Action:** Define training workflow

---

### O-002: Handoff to Said

**Priority:** 🟡 MEDIUM  
**Blocker for:** Client independence  
**Decider:** Omar  
**Status:** ⏳ OPEN

**Question:**
How do we train Said to manage the system independently?

**Needs:**
- User manual
- Training sessions
- Support process
- Emergency contacts

**Action:** Create training plan

---

### O-003: Support & Maintenance

**Priority:** 🟢 LOW  
**Blocker for:** Long-term operations  
**Decider:** Omar + Said  
**Status:** ⏳ OPEN

**Question:**
What is the ongoing support model?

**Options:**
- Included in contract (X hours/month)
- Separate support contract
- Pay-as-you-go (hourly)
- Fully autonomous (training only)

**Action:** Define in contract

---

## BUSINESS QUESTIONS

### B-004: Current Pricing Baseline

**Priority:** 🟡 MEDIUM  
**Blocker for:** Pricing analysis  
**Asked to:** Said Thaifa  
**Status:** ⏳ AWAITING RESPONSE

**Question:**
What is your current pricing structure?

**Need:**
- Current rates per room type/number
- How you currently define seasons
- Historical occupancy rates
- Revenue per season

**Purpose:** Baseline for competitor analysis and optimization

---

### B-005: Competitor List

**Priority:** 🟡 MEDIUM  
**Blocker for:** Market research  
**Asked to:** Said Thaifa  
**Status:** ⏳ AWAITING RESPONSE

**Question:**
Who do you consider your direct competitors in Marrakech?

**Need:**
- Names of similar properties
- What makes them comparable (size, location, style, price range)
- Any you'd like to benchmark against specifically

**Purpose:** Focused competitor analysis

---

### B-006: Peak Events Calendar

**Priority:** 🟢 LOW  
**Blocker for:** Pricing strategy  
**Asked to:** Said Thaifa  
**Status:** ⏳ AWAITING RESPONSE

**Question:**
What events/periods drive peak demand in Marrakech?

**Examples:**
- Religious holidays
- Cultural festivals
- Marathon events
- High tourism seasons

**Purpose:** Dynamic pricing model

---

## QUESTION SUMMARY

| ID | Question | Priority | Category | Status |
|----|----------|----------|----------|--------|
| B-001 | "App" definition | 🔴 CRITICAL | Business | ⏳ Awaiting |
| B-002 | Platform priority | 🔴 HIGH | Business | ⏳ Awaiting |
| F-001 | Contract & budget | 🔴 CRITICAL | Financial | ⏳ Awaiting |
| B-003 | Room numbering | 🟡 MEDIUM | Business | ⏳ Awaiting |
| T-001 | MCP vs Code Execution | 🟡 MEDIUM | Technical | 🔍 Research |
| T-003 | Database choice | 🟡 MEDIUM | Technical | ⏳ Open |
| T-004 | Repo structure | 🟡 MEDIUM | Technical | 🔴 Blocked |
| B-004 | Current pricing | 🟡 MEDIUM | Business | ⏳ Awaiting |
| B-005 | Competitor list | 🟡 MEDIUM | Business | ⏳ Awaiting |
| O-001 | Agent training | 🟡 MEDIUM | Operational | ⏳ Open |
| O-002 | Handoff to Said | 🟡 MEDIUM | Operational | ⏳ Open |
| T-002 | Orchestration | 🟢 LOW | Technical | ⏳ Open |
| F-002 | Go Siyaha | 🟢 LOW | Financial | 🔍 Research |
| T-005 | Hosting platform | 🟢 LOW | Technical | ⏳ Open |
| T-006 | Monitoring | 🟢 LOW | Technical | ⏳ Open |
| O-003 | Support model | 🟢 LOW | Operational | ⏳ Open |
| B-006 | Peak events | 🟢 LOW | Business | ⏳ Awaiting |

---

**Priority Legend:**
- 🔴 CRITICAL: Blocking immediate progress
- 🟡 MEDIUM: Needed for next phase
- 🟢 LOW: Can be deferred

**Status Legend:**
- ⏳ Awaiting: Waiting for response
- 🔍 Research: Investigation needed
- ⏳ Open: Not yet decided
- 🔴 Blocked: Dependency on other decision

---

**Next:** See `villa-thaifa-quick-start.md` for project setup instructions.

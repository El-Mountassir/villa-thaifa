# Villa Thaifa - Internal App Requirements
## Foundation for LHCM-OS Platform

**Version:** 0.1.0-alpha.0  
**Date:** 2025-01-09  
**Purpose:** Specs for Internal App (Villa Thaifa pilot) → Will evolve into LHCM-OS Platform  
**Timeline:** "Le plus vite on a un truc utilisable" (prochains jours, NOT 2-3 mois)

---

## SECTION 1: MISSION & CONTEXT

### 1.1 The Problem

**Current State:**
- Files dispersed across multiple locations
- Limited context window = agents can't access everything needed
- Omar manually provides context to each agent
- No centralized knowledge base
- No dashboard to see what's happening

**Impact:**
- Agents ineffective (missing critical info)
- Omar becomes bottleneck (must manually feed context)
- Can't scale (135 OTAs impossible without centralized system)

### 1.2 The Solution: Internal App

**Primary Goal:**
Make Villa Thaifa business 100% accessible to agents (Claude Code, Gemini, etc.)

**Secondary Goal:**
Give Omar dashboard/control interface (see status, direct agents)

**Tertiary Goal:**
Build foundation for LHCM-OS Platform (reusable for other properties)

---

## SECTION 2: CORE REQUIREMENTS

### 2.1 Knowledge Base (P0 CRITICAL)

**What:**
Centralized repository of ALL Villa Thaifa information

**Content Types:**
1. **Property Details:**
   - 8 room types (specs, photos, pricing)
   - Amenities, facilities, location
   - House rules, check-in/out procedures
2. **Operational Docs:**
   - HotelRunner settings, configurations
   - OTA account details (Booking.com, Airbnb, etc.)
   - Pricing strategy, seasonal rates
3. **Client Information:**
   - Past guests (preferences, issues)
   - Current reservations
   - Future bookings
4. **Standard Operating Procedures:**
   - How to handle booking
   - How to respond to guest questions
   - Emergency procedures
5. **Financial Data:**
   - Revenue per OTA
   - Commission rates
   - P&L (if available)

**Format:**
- Markdown files (easy to read for agents)
- Structured data (JSON for room types, pricing)
- Images (property photos, room photos)

**Storage:**
- Git repo (version control)
- Searchable (full-text search)
- Accessible via API (agents can query)

**Success Criteria:**
- ✅ Agent asks "What are the check-in hours?" → Gets answer from knowledge base
- ✅ Agent asks "Show me Superior Double Room photos" → Gets images
- ✅ Agent asks "What's the pricing for July?" → Gets rate table

---

### 2.2 Google Drive Integration (P0 CRITICAL)

**Requirement:**
Agents need access to Google Drive (where current files are stored)

**Current Drive Location:**
https://drive.google.com/drive/folders/11WkUW3zm2Bjee3H5GLR57eK7Bb58PMVX

**Access Level:** READ-ONLY (Omar n'a pas write permissions)

**Migration Strategy:**
1. **Short-term:** Download all files from Villa Thaifa shared Drive
2. **Copy to:** Omar's Google Workspace Drive (2TB Business Standard available)
   - Domain: Omar El Mountassir business account
   - NOT Villa Thaifa domain (Said hasn't provided yet, pas problème)
3. **Long-term:** Migrate to Villa Thaifa domain when/if Said provides
   - Easy transfer later (Google Workspace migration tools)
   - Not blocking for MVP

**Critical Constraint:**
**USE CODE EXECUTION (Advanced Tool Use), NOT MCP**

**Omar's Directive:**
> "Il nous faut éviter les MCPs comme la peste! Context window = ULTRA PRÉCIEUX!"

**Reference:**
- https://www.anthropic.com/engineering/advanced-tool-use
- https://www.anthropic.com/engineering/code-execution-with-mcp

**Why Code Execution over MCP:**
- Context window efficiency (98.7% reduction vs MCP)
- Already proven in Tech Stack analysis
- Scalable to 100+ tools without degradation
- MCP = 5-50K tokens per tool, Code Execution = <500 tokens

**Implementation:**
- TypeScript wrapper around Google Drive API
- Agents call wrapper functions (not direct MCP)
- Wrapper executes code, returns results

**Functions Needed:**
```typescript
// List files in folder
listFiles(folderId: string): File[]

// Get file content
getFileContent(fileId: string): string

// Search files
searchFiles(query: string): File[]

// Download file
downloadFile(fileId: string): Buffer

// Upload file (to Omar's Drive)
uploadFile(filename: string, content: Buffer): File
```

**Phase 1 (Ce soir/demain):**
- Download all files from Villa Thaifa shared Drive
- Upload to Omar's Google Workspace Drive
- Create folder structure: `/Villa Thaifa/[photos, docs, data]`

**Phase 2 (Internal App):**
- Build TypeScript wrapper for Google Drive API
- Test with Omar's Drive folder
- Agents can read/search/download

**Success Criteria:**
- ✅ All Villa Thaifa files copied to Omar's Drive
- ✅ Agent asks "List all files in Villa Thaifa folder" → Gets list
- ✅ Agent asks "Read property description doc" → Gets content
- ✅ Agent searches "pricing 2025" → Finds relevant docs

---

### 2.3 Dashboard for Omar (P1 IMPORTANT)

**What:**
Web interface showing Villa Thaifa status + agent activity

**Core Features:**

**View 1: OTA Status**
- Which OTAs active/pending/failed
- Last sync time (HotelRunner ↔ OTAs)
- Availability calendar (all OTAs)

**View 2: Reservations**
- Upcoming check-ins (next 7 days)
- Current guests
- Upcoming check-outs
- Cancellations

**View 3: Agent Activity**
- Which agents working on what
- Recent actions (e.g., "Airbnb agent created listing")
- Errors/issues (e.g., "Expedia sync failed")

**View 4: Quick Actions**
- Create internal reservation
- Update pricing
- Block dates (maintenance)
- Send message to guest

**Tech Stack:**
- Next.js 15 (App Router, RSC)
- Shadcn/ui components
- Tailwind CSS 4
- Cloudflare Pages hosting
- Real-time updates (Cloudflare Durable Objects for WebSockets)

**Success Criteria:**
- ✅ Omar opens dashboard → Sees current status in <5 seconds
- ✅ Omar sees Airbnb agent working → Knows what it's doing
- ✅ Omar creates reservation → Agents immediately see it

---

### 2.4 Agent Interface (P1 IMPORTANT)

**What:**
API that agents (Claude Code, Gemini) use to interact with Villa Thaifa data

**Endpoints:**

**Knowledge Base:**
```
GET /api/knowledge/property → Property details
GET /api/knowledge/rooms → Room types
GET /api/knowledge/sops → Standard Operating Procedures
POST /api/knowledge/search → Full-text search
```

**Reservations:**
```
GET /api/reservations → List all reservations
GET /api/reservations/:id → Get specific reservation
POST /api/reservations → Create new reservation
PATCH /api/reservations/:id → Update reservation
```

**OTAs:**
```
GET /api/otas → List all OTAs (status, config)
GET /api/otas/:name/availability → Check availability on specific OTA
POST /api/otas/:name/sync → Force sync with OTA
```

**Google Drive:**
```
GET /api/drive/files → List files
GET /api/drive/files/:id → Get file content
POST /api/drive/search → Search files
```

**Tech Stack:**
- Hono (edge-native TypeScript framework)
- Cloudflare Workers (serverless)
- D1 database (or PostgreSQL TBD)
- Authentication (Clerk or Auth0 TBD)

**Success Criteria:**
- ✅ Agent calls `/api/knowledge/rooms` → Gets all room types
- ✅ Agent calls `/api/reservations` → Gets upcoming bookings
- ✅ Agent calls `/api/otas/airbnb/availability` → Knows what's available

---

## SECTION 3: NON-REQUIREMENTS (Out of Scope)

**NOT needed for Internal App (defer to LHCM-OS Platform):**

❌ **Multi-tenant architecture** (Villa Thaifa only for now)  
❌ **White-label capabilities** (LHCM-OS Platform feature)  
❌ **Production-ready scaling** (handle 1 property, not 100)  
❌ **Advanced analytics** (basic metrics only)  
❌ **Guest-facing features** (no guest portal yet)  
❌ **Payment processing** (HotelRunner handles this)  
❌ **Channel Manager replacement** (we use HotelRunner, not replace it)  
❌ **AI C-Suite roles** (CEO, CFO, GM agents = LHCM-OS Platform)  
❌ **"The Boardroom"** (voice commands, strategic directives = LHCM-OS Platform)

**Internal App Goal:**
Developer-ready & agent-ready (NOT production-ready yet)

---

## SECTION 4: ARCHITECTURE DECISIONS

### 4.1 Database: TBD

**Options:**
1. **D1 (Cloudflare SQLite)** - Serverless, edge-native
2. **PostgreSQL (Neon)** - Battle-tested, more features

**Decision Pending:** Omar said "on choisira ce qui nous arrange le plus"

**For Internal App:**
- Start with D1 (simpler, faster to ship)
- Migrate to PostgreSQL if needed (but probably won't need)

**Impact:**
- Low (either works for 1 property)
- Can migrate later if LHCM-OS Platform needs PostgreSQL

---

### 4.2 Auth: TBD

**Options:**
1. **Clerk ($25/month)** - Fast to MVP, migrate later
2. **Auth0 (free tier)** - More features, more setup
3. **Auth.js (open-source)** - Free, most work

**Decision Pending:** Omar said "si on peut avoir un truc gratuit tout aussi efficace"

**Recommendation:**
- **Auth0 free tier** for Internal App
  - Free up to 7,000 users (way more than needed)
  - Social logins (Google, GitHub)
  - MFA support
  - More features than Clerk free tier

**Action Required:**
- Web research: Auth0 vs Clerk vs Auth.js (effort, features, cost)

**Impact:**
- Low (any solution works for Internal App)
- Can migrate later if needed

---

### 4.3 Code Execution vs Traditional MCP

**Decision:** ✅ LOCKED IN - CODE EXECUTION

**Why:**
- Context window efficiency (98.7% reduction vs traditional MCP)
- Scalable to 100+ tools (LHCM-OS Platform will need this)
- Modern approach (Anthropic recommendation)

**Reference:**
https://www.anthropic.com/engineering/advanced-tool-use

**Implementation:**
- TypeScript wrappers around APIs
- Agents execute code (not call MCP servers)
- Pattern established in Tech Stack

**Impact:**
- High (affects all agent integrations)
- Foundation for LHCM-OS Platform

---

## SECTION 5: TIMELINE ESTIMATION

### 5.1 The Challenge

**Problem:**
Neither Omar nor Lux can accurately estimate timeline with 2025-2026 agentic tools.

**Omar's Observation:**
- *"J'ai vu des gens qui créer des apps en quelque heures"*
- *"Je penses vraiment que tu (Lux) doit faire des recherches en ligne, car je le sentiment que ptet que tes appréhension concernant le nombre de temps qu'il faut de nos jours (en 2026) pour nos agentic system comme Claude Code, etc, pour créé tout cela est potentiellement faussé"*

**Lux's Observation:**
- Initial estimate was 4-5 days prep
- Omar challenged this ("why if nothing concrete yet?")
- May be too conservative given Vibe Kanban orchestration

### 5.2 Research Needed

**Questions to Answer (Web Search):**
1. How fast can developers build Next.js apps with Claude Code in 2025-2026?
2. Real-world examples of "app in hours" (what complexity? what features?)
3. Vibe Kanban case studies (speed improvements documented?)
4. Code Execution pattern adoption (how much faster vs traditional?)

**Search Queries:**
- "Claude Code Next.js app development time 2025"
- "Vibe Kanban speed benchmarks"
- "Code Execution MCP performance comparison"
- "Agentic development timeline 2025 2026"

**Goal:**
Ground timeline in reality (not speculation)

### 5.3 Provisional Estimate (To Be Validated)

**Best Case (If "apps in hours" is real):**
- Day 1: Knowledge base + basic API (6-8h)
- Day 2: Google Drive integration + dashboard (6-8h)
- Day 3: Testing + polish (4-6h)
- **Total:** 2-3 days to usable Internal App

**Realistic Case (More conservative):**
- Week 1: Knowledge base + API + Google Drive (3-4 days)
- Week 2: Dashboard + testing + polish (2-3 days)
- **Total:** 1-2 weeks to usable Internal App

**Conservative Case (If challenges arise):**
- 2-3 weeks to fully functional Internal App

**Omar's Preference:**
*"Le plus vite on a un truc utilisable le mieux"*

**Action:**
Web research TOMORROW to validate which scenario is realistic.

---

## SECTION 6: DEVELOPMENT STRATEGY

### 6.1 Iterative Approach (Agile)

**NOT Waterfall:**
- Don't build everything before testing
- Ship incrementally
- Get feedback from agents/Omar

**Milestones:**

**Milestone 1: Knowledge Base API (Day 1-2)**
- Deploy basic API
- Agents can query property details
- Test with Claude Code
- ✅ Success = Agent gets answer to "What are room types?"

**Milestone 2: Google Drive Integration (Day 2-3)**
- Code Execution wrapper for Google Drive
- Agents can list/read files
- Test with current Villa Thaifa files
- ✅ Success = Agent reads property description from Drive

**Milestone 3: Dashboard MVP (Day 3-5)**
- Basic Next.js app
- Show OTA status + reservations
- Read-only (no actions yet)
- ✅ Success = Omar sees current status

**Milestone 4: Agent Interface Complete (Day 5-7)**
- All API endpoints implemented
- Agents can create reservations
- Agents can update pricing
- ✅ Success = Agent creates test reservation via API

**Milestone 5: Polish & Production (Week 2)**
- Error handling
- Logging/monitoring
- Authentication
- Deploy to Cloudflare Pages

### 6.2 Vibe Kanban Orchestration

**How to Use:**
- Create ticket for each milestone
- Multiple agents work in parallel
- Example:
  - Agent 1: Build API endpoints (Hono + D1)
  - Agent 2: Build dashboard UI (Next.js + shadcn)
  - Agent 3: Build Google Drive wrapper (TypeScript)
- Omar reviews PRs incrementally

**Benefits:**
- Faster (parallel > sequential)
- Isolated (Git Worktrees = no conflicts)
- Organized (Kanban board = visual status)

---

## SECTION 7: TRANSITION TO LHCM-OS PLATFORM

### 7.1 Internal App as Foundation

**Reusable Components:**
1. **Knowledge Base Architecture**
   - Same structure for other properties
   - Just different content
2. **Google Drive Integration**
   - Code Execution pattern proven
   - Reuse for other clients
3. **Dashboard Framework**
   - Componentized UI (shadcn)
   - Themeable (change branding)
4. **Agent API**
   - RESTful design
   - Add multi-tenancy later

**What Changes for LHCM-OS:**
- Multi-tenant database (property_id column everywhere)
- White-label UI (custom branding per client)
- AI C-Suite agents (GM, CFO, Revenue Manager)
- "The Boardroom" (voice commands, strategic directives)
- Production-ready scaling (100+ properties)

### 7.2 Timeline: 2-3 Months for LHCM-OS

**Why 2-3 Months (Not Weeks):**
- Multi-tenant architecture (complex)
- AI agent roles need definition (no standard format yet)
- Memory system (agents remember past interactions)
- Production-ready (monitoring, error handling, scale)
- Said's pilot testing (iterate based on feedback)

**Current Focus:**
Internal App = prochains jours (NOT 2-3 mois)

**On a le temps de bien faire.**

---

## SECTION 8: NEXT ACTIONS (After Tonight's OTA Success)

### 8.1 Research Phase (Tomorrow Morning)

**Action:** Web search to validate timeline estimates

**Questions:**
1. How fast can Claude Code build Next.js apps?
2. Vibe Kanban speed improvements?
3. Real examples of "app in hours"?

**Output:** Realistic timeline estimate (best/realistic/conservative)

### 8.2 Architecture Planning (Tomorrow Afternoon)

**Action:** Detailed architecture document

**Components:**
1. Database schema (D1 or PostgreSQL)
2. API endpoints (Hono)
3. Google Drive Code Execution wrapper
4. Dashboard components (Next.js)
5. Deployment pipeline (Cloudflare)

**Output:** Technical spec ready for agents

### 8.3 Vibe Kanban Tickets (Tomorrow Evening)

**Action:** Create development tickets

**Tickets:**
- T001: Setup project structure (Next.js + Hono + D1)
- T002: Build Knowledge Base API
- T003: Build Google Drive Code Execution wrapper
- T004: Build Dashboard UI (basic)
- T005: Integration testing

**Output:** Ready to drag tickets to "In Progress"

### 8.4 Development Sprint (Days 2-7)

**Action:** Execute tickets with agent swarm

**Omar's Role:**
- Review PRs in Vibe UI
- Test each milestone
- Provide feedback

**Agents' Role:**
- Build components in parallel
- Submit PRs
- Fix issues based on feedback

**Output:** Usable Internal App

---

## SECTION 9: SUCCESS CRITERIA

### 9.1 Internal App is "DONE" When:

**Knowledge Base:**
- ✅ All Villa Thaifa docs centralized
- ✅ Agents can query/search
- ✅ Full-text search works

**Google Drive:**
- ✅ Agents can list files
- ✅ Agents can read content
- ✅ Agents can search

**Dashboard:**
- ✅ Shows OTA status
- ✅ Shows upcoming reservations
- ✅ Shows agent activity
- ✅ Omar can create reservation
- ✅ Omar can update pricing

**Agent API:**
- ✅ All endpoints implemented
- ✅ Agents can perform operations
- ✅ Authentication works

**Testing:**
- ✅ Agents can complete OTA activation using Internal App
- ✅ Omar can see everything happening
- ✅ No manual context feeding needed

### 9.2 Ready for LHCM-OS When:

**Internal App Proven:**
- ✅ Villa Thaifa using it daily
- ✅ Agents effective (no context issues)
- ✅ Omar satisfied with UX
- ✅ Said sees value ("wow, this is useful")

**Then:**
- Start multi-tenant architecture
- Add AI C-Suite roles
- Build "The Boardroom"
- Scale to other properties

---

## APPENDIX: KEY DECISIONS REFERENCE

**From Workstream Master Section 7:**

**D-W-006:** Phased approach
- Phase 0: OTAs (ce soir)
- Phase 1: Internal App (prochains jours)
- Phase 2: LHCM-OS Platform (2-3 mois)

**D-W-010:** Code Execution MCP pattern ✅

**D-W-011:** Database TBD (D1 or PostgreSQL)

**D-W-012:** Auth TBD (Auth0 or Clerk research needed)

**D-W-014:** Vibe Kanban orchestration ✅

---

## END OF REQUIREMENTS DOC

**This document will guide Internal App development starting tomorrow.**

**Next Update:** After web research validates timeline (tomorrow morning).

**Version Control:**
- v0.1.0-alpha.0: Initial requirements (2025-01-09)
- v0.2.0: Post-research (timeline + architecture)
- v0.3.0: Technical spec (detailed implementation)
- v1.0.0: Development complete, Internal App shipped

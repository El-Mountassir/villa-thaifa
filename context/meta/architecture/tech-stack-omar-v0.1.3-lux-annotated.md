# Tech Stack - Omar El Mountassir Ecosystem

> **Version**: 0.1.3-alpha.0 (+ Lux Annotations for LHCM-OS)
> **Date**: 2026-01-07 (Captured 2026-01-09)
> **Status**: DRAFT | EVOLVING | Inaccurate
> **Purpose**: Single source of truth for technology choices. Placeholders mark gaps.

---

## 🔴 LUX CRITICAL ANNOTATIONS FOR LHCM-OS MVP

**Date Added**: 2025-01-09
**Context**: Analyzing alignment with LHCM-OS Strategy (A08) MVP proposal

### CRITICAL ISSUES IDENTIFIED:

**1. 🚨 CODE EXECUTION MCP PATTERN (Section 2.2)**

- **Problem**: My LHCM-OS MVP proposal uses "traditional MCP"
- **Stack says**: Traditional MCP = CONTEXT TRAP (67,300 tokens for 7 MCPs)
- **Impact**: With 10+ MCPs for LHCM-OS, we'll hit context degradation
- **Fix Required**: Migrate to Code Execution MCP pattern (98.7% reduction)
- **Action**: Revise A08 Section 3 (Phase 1 architecture)

**2. 🚨 AGENT DEFINITION FORMAT (Section 12.1)**

- **Problem**: LHCM-OS needs 5-10 agents (GM, CFO, Revenue, CTO, etc.)
- **Stack says**: Agent Definition Format = [TBD] (P0 CRITICAL GAP)
- **Impact**: Can't properly define Digital C-Suite roles
- **Fix Required**: Research Anthropic Agent Skills format
- **Action**: Add to LHCM-OS Phase 2 prep work

**3. 🚨 HOTELRUNNER MCP (Section 13)**

- **Problem**: Villa Thaifa needs HotelRunner integration
- **Stack says**: Custom MCP Server = [TO BUILD]
- **Impact**: Phase 0 (OTA activation) depends on this
- **Fix Required**: Build HotelRunner MCP with Code Execution pattern
- **Action**: Add to Villa Thaifa OTA activation prerequisites

**4. 🟡 AUTH SOLUTION (Section 4)**

- **Problem**: LHCM-OS MVP says "Auth TBD (Clerk vs Auth.js)"
- **Stack says**: Same - [TBD] with research needed
- **Impact**: Medium (can start with simple auth, migrate later)
- **Fix Required**: Make decision before Phase 1 starts
- **Action**: Research Clerk vs Auth.js for LHCM-OS use case

**5. 🟡 VECTOR DATABASE (Section 5)**

- **Problem**: LHCM-OS needs semantic search (documents, conversations)
- **Stack says**: [TBD] - pgvector vs Pinecone vs Qdrant
- **Impact**: Medium (can defer to Phase 2)
- **Fix Required**: Research pgvector (SQL-native) for Cloudflare D1
- **Action**: Add to LHCM-OS Phase 2 (Agent Framework)

### ALIGNMENT SUMMARY:

✅ **ALIGNED (No changes needed):**

- Next.js 15+ for frontend
- Cloudflare Workers/Pages for hosting
- Claude Opus/Sonnet/Haiku for agents
- FastAPI for backend (if needed)
- PostgreSQL for database
- Tailwind CSS + shadcn/ui for UI

🔴 **CRITICAL GAPS (Must fix before MVP):**

- Traditional MCP → Code Execution MCP pattern
- Agent Definition Format (research Anthropic Skills)
- HotelRunner MCP (build it)

🟡 **IMPORTANT GAPS (Can defer to Phase 2):**

- Auth solution (Clerk vs Auth.js)
- Vector database (pgvector research)

---

## Changelog

| Version       | Date       | Changes                                                                                                                           |
| ------------- | ---------- | --------------------------------------------------------------------------------------------------------------------------------- |
| 0.1.3-lux.0   | 2026-01-09 | **LUX**: Captured + annotated for LHCM-OS alignment analysis                                                                      |
| 0.1.0-alpha.3 | 2026-01-07 | **CRITICAL**: Code Execution MCP pattern (98.7% context reduction), Notion Free, HyperTool MCP, Google Workspace MCPs (community) |
| 0.1.0-alpha.2 | 2026-01-07 | Google Workspace Business Standard, Linear MCP, Cloudflare platform details, Vercel Free, OS state (current vs planned)           |
| 0.1.0-alpha.1 | 2026-01-07 | Domain, Hardware, IaC (Ansible+Chezmoi), Dev tools (uv, Bun, ble.sh, Starship)                                                    |
| 0.1.0-alpha.0 | 2026-01-07 | Initial capture from Omar El Mountassir architecture session                                                                      |

---

## Legend

| Symbol          | Meaning                            |
| --------------- | ---------------------------------- |
| ✅              | Done / Decided / In Use            |
| 🔶              | Candidate (needs validation)       |
| ❓              | Unknown / Research needed          |
| 🚫              | Explicitly rejected                |
| `[TBD]`         | To Be Done / Decided               |
| `[GAP]`         | Missing component - needs solution |
| `[RESEARCH: X]` | Requires research on topic X       |

---

## 0. DOMAINS & IDENTITY

| Asset                    | Value                    | Status | Notes                       |
| ------------------------ | ------------------------ | ------ | --------------------------- |
| **Primary Domain**       | el-mountassir.com        | ✅     | Purchased via Cloudflare    |
| **Registrar**            | Cloudflare               | ✅     | DNS + Security              |
| **Current State**        | Empty                    | 🔶     | Nothing deployed yet        |
| **Subdomains (Planned)** | `[TBD]`                  | ❓     | api._, docs._, app.\*, etc. |
| **Primary Email**        | <omar@el-mountassir.com> | ✅     | Via Google Workspace        |

<!-- [LUX NOTE]: For LHCM-OS, we'll need subdomains:
- villa-thaifa.el-mountassir.com (demo)
- api.el-mountassir.com (backend)
- docs.el-mountassir.com (documentation)
Consider: lhcm-os.com as separate brand domain? -->

---

## 0.0.1 SAAS & PRODUCTIVITY SUITE

### Google Workspace Business Standard

| Feature          | Value                      | Status |
| ---------------- | -------------------------- | ------ |
| **Plan**         | Business Standard          | ✅     |
| **Storage**      | 2TB pooled per user        | ✅     |
| **AI**           | Gemini included (Jan 2025) | ✅     |
| **Domain Email** | <omar@el-mountassir.com>   | ✅     |

**Gemini Features Included** (since Jan 2025):

- Gemini side panel in Gmail, Docs, Sheets, Slides, Drive, Chat
- Help me write (Gmail, Docs)
- Take notes for me (Meet)
- Gemini app access (Gemini 3 Pro, Deep Research)
- NotebookLM Plus
- Google Vids (video creation)
- Data stays private (not used for training)

| App                    | Use Case                         | Status |
| ---------------------- | -------------------------------- | ------ |
| **Gmail**              | Email (<omar@el-mountassir.com>) | ✅     |
| **Calendar**           | Scheduling                       | ✅     |
| **Drive**              | File storage (2TB)               | ✅     |
| **Docs/Sheets/Slides** | Documents                        | ✅     |
| **Meet**               | Video calls + AI notes           | ✅     |
| **Gemini App**         | AI assistant                     | ✅     |
| **NotebookLM Plus**    | Research assistant               | ✅     |

### Project Management

| Tool         | Plan    | Status | MCP         | Notes                          |
| ------------ | ------- | ------ | ----------- | ------------------------------ |
| **Linear**   | `[TBD]` | ✅     | ✅ Official | Issue tracking, sprints        |
| **GitHub**   | Free    | ✅     | ✅          | Code + Issues sync with Linear |
| **Calendly** | —       | 🔶     | —           | Optional, not priority         |

**Linear MCP Server** (Official - May 2025):

```json
{
  "mcpServers": {
    "linear": {
      "command": "npx",
      "args": ["-y", "mcp-remote", "https://mcp.linear.app/mcp"]
    }
  }
}
```

- Tools: list_issues, create_issue, update_issue, list_projects, create_comment, etc.
- Auth: OAuth 2.1 with dynamic client registration
- GitHub sync: Bi-directional issue linking

<!-- [LUX NOTE]: For LHCM-OS, Linear will track:
- Client projects (Villa Thaifa, future properties)
- Agent tasks (created by Digital C-Suite)
- Technical debt
- Feature requests from Said/clients
Consider: Linear Board "LHCM-OS - Villa Thaifa" vs separate workspace? -->

---

## 0.1 HARDWARE (Sovereign Node)

| Component   | Specification                       | Notes                                    |
| ----------- | ----------------------------------- | ---------------------------------------- |
| **Machine** | Acer Predator Triton 17X (PTX17-71) | Primary workstation                      |
| **CPU**     | Intel Core i9-13900HX               | 8P + 16E cores, 32 threads, 5.4GHz turbo |
| **GPU**     | NVIDIA RTX 4090 Laptop              | 16GB GDDR6, 175W TGP                     |
| **RAM**     | 32GB DDR5                           | + 16GB zram + 20GB swap                  |
| **Storage** | NVMe SSD                            | ext4 filesystem                          |
| **Cooling** | Vapor chamber + liquid metal        | 3x Aeroblade 3D fans                     |

### OS State

| Attribute    | Current            | Planned             |
| ------------ | ------------------ | ------------------- |
| **OS**       | Pop!\_OS 22.04 LTS | Pop!\_OS 24.04 LTS  |
| **Desktop**  | GNOME              | COSMIC (Rust-based) |
| **Kernel**   | 5.x / 6.x          | 6.17.9              |
| **Username** | omar               | director            |
| **Hostname** | pop-os             | nexus               |
| **Full**     | omar@pop-os        | director@nexus      |

**Migration**: Fresh install planned once stable. Bootstrap via `sovereign-bootstrap` repo.

<!-- [LUX NOTE]: LHCM-OS development will happen on Nexus (local).
GPU can be leveraged for local LLM inference if we add Ollama (Section 2.1).
Consider: Setting up dev environment for Said to test LHCM-OS locally? -->

---

## 1. CORE LANGUAGES & RUNTIMES

| Layer                        | Choice                | Status | Notes                                       |
| ---------------------------- | --------------------- | ------ | ------------------------------------------- |
| **Primary Language**         | TypeScript            | ✅     | Type safety, AI-friendly                    |
| **Secondary Language**       | Python 3.12+          | ✅     | AI/ML, FastAPI, scripting                   |
| **Shell**                    | Bash 5.1.16 + ble.sh  | ✅     | Syntax highlighting, auto-suggestions       |
| **Runtime (JS)**             | Node.js LTS (via nvm) | ✅     | Version managed                             |
| **Runtime (Python)**         | Python 3.12+          | ✅     | Via uv                                      |
| **Package Manager (JS)**     | Bun                   | ✅     | Fast, all-in-one (runtime + bundler + test) |
| **Package Manager (Python)** | uv (Astral)           | ✅     | Replaces pip, poetry, pyenv - Rust-based    |
| **Node Version Manager**     | nvm                   | ✅     | `.nvmrc` per project                        |

<!-- [LUX NOTE]: LHCM-OS will use:
- TypeScript for frontend (Next.js)
- TypeScript for agents (Claude SDK)
- Python for FastAPI backend (if complex logic needed)
- Bun for fast builds/tests
All aligned ✅ -->

---

## 2. AI / LLM STACK

### 2.1 Models

| Role                    | Model             | Provider    | Status | Notes                                    |
| ----------------------- | ----------------- | ----------- | ------ | ---------------------------------------- |
| **Lead Orchestrator**   | Claude Opus 4.5   | Anthropic   | ✅     | Primary brain                            |
| **Worker Agents**       | Claude Sonnet 4.5 | Anthropic   | ✅     | Cost-effective execution                 |
| **Fast Tasks**          | Claude Haiku 4.5  | Anthropic   | ✅     | Speed-critical                           |
| **Multimodal (Video)**  | Gemini 2.0 Flash  | Google      | 🔶     | Transcription, video analysis            |
| **Multimodal (Vision)** | `[TBD]`           | `[TBD]`     | ❓     | Image understanding                      |
| **Embeddings**          | `[TBD]`           | `[TBD]`     | ❓     | [RESEARCH: Anthropic vs OpenAI vs local] |
| **Local/Offline**       | `[TBD]`           | Ollama?     | ❓     | Privacy-sensitive tasks                  |
| **Fallback/Routing**    | `[TBD]`           | OpenRouter? | ❓     | [RESEARCH: Multi-provider routing]       |

<!-- [LUX NOTE]: For LHCM-OS Digital C-Suite:
- CEO/Chairman directives: Claude Opus 4.5 (complex reasoning)
- GM/CFO/Revenue agents: Claude Sonnet 4.5 (balance cost/quality)
- Quick responses: Claude Haiku 4.5 (latency-sensitive)
All aligned ✅

Question: Should we add Embeddings for semantic search of conversations/documents?
Answer: Yes, Phase 2 (Section 5 Vector Database) -->

### 2.2 SDKs & Protocols

| Component            | Choice                       | Status | Notes                                  |
| -------------------- | ---------------------------- | ------ | -------------------------------------- |
| **Agent SDK**        | Claude Agent SDK             | ✅     | Primary orchestration                  |
| **Protocol**         | MCP (Model Context Protocol) | ✅     | Tool integration standard              |
| **MCP Mode**         | Code Execution with MCP      | 🔶     | **CRITICAL** — 98.7% context reduction |
| **Agent-to-Agent**   | `[TBD]`                      | ❓     | [RESEARCH: A2A protocol, JSON-LD]      |
| **Skills Framework** | Agent Skills (Anthropic)     | 🔶     | [RESEARCH: Dec 2025 release]           |
| **Code Execution**   | Built-in Claude 4.5          | ✅     | Sandbox for tool execution             |

<!-- [LUX NOTE FOR LHCM-OS]: 🚨 CRITICAL ARCHITECTURE CHANGE REQUIRED

My current LHCM-OS proposal (A08 Section 3) says:
"Phase 1: Build MVP with MCP servers for integrations"

THIS IS WRONG according to this section. Traditional MCP is a context trap.

REVISED APPROACH FOR LHCM-OS:
1. Phase 1 MVP: Use Code Execution MCP pattern (not traditional)
2. Build thin TypeScript wrappers for:
   - HotelRunner API (not MCP server, but TS wrapper)
   - Booking.com API (TS wrapper)
   - Calendar/scheduling (TS wrapper)
3. Agents call these wrappers via Code Execution, not traditional MCP
4. Phase 2: Migrate existing MCPs (Linear, GitHub) to Code Execution pattern

IMPACT:
- Changes architecture in A08 Section 3 (Phase 1)
- Adds prerequisite: Study Code Execution MCP architecture
- Adds task: Create TypeScript wrapper library for LHCM-OS tools

ACTION REQUIRED:
- Update A08 Section 3 after Omar reviews
- Add to Workstream Master Section 3 (Stream 4 dependencies)
-->

---

### 🚨 CRITICAL: MCP Context Window Problem

> **Traditional MCP is a TRAP for multi-agent systems.**

| Metric               | Traditional MCP                  | Code Execution MCP                |
| -------------------- | -------------------------------- | --------------------------------- |
| **7 MCPs idle**      | 67,300 tokens (33.7%)            | ~2,000 tokens (~1%)               |
| **59+ tools**        | Measurable reasoning degradation | ✅ No degradation                 |
| **100+ tools**       | **GUARANTEED FAILURE**           | ✅ 500+ possible                  |
| **10,000+ tools**    | Impossible                       | ✅ Filesystem-based (theoretical) |
| **Context overhead** | ~20-35%                          | **~2%**                           |

**Migration Path:**

1. Study Code Execution architecture (Anthropic Engineering)
2. Evaluate HyperTool MCP as proxy
3. Create thin TypeScript wrappers for existing MCPs
4. Implement Dynamic Context Loading (DCL)
5. Test with chrome-devtools (26 tools)
6. Migrate progressively

**References:**

- <https://www.anthropic.com/engineering/code-execution-with-mcp>
- <https://github.com/toolprint/hypertool-mcp>
- <https://cefboud.com/posts/dynamic-context-loading-llm-mcp>

**Success Criteria:**

- [ ] Context overhead MCP < 5%
- [ ] 100+ tools accessible without degradation
- [ ] Pattern documented

<!-- [LUX NOTE]: This is THE critical section for LHCM-OS.

LHCM-OS will have 10+ "tools" (really capabilities):
- HotelRunner operations (list rooms, create reservation, update pricing, etc.)
- Booking.com operations (sync availability, get bookings, respond to guests)
- Calendar operations (check availability, block dates, add events)
- Email operations (send confirmations, respond to inquiries)
- Analytics operations (calculate revenue, occupancy, forecast)
- Staff operations (assign tasks, track completion)
- Guest operations (check-in, check-out, special requests)
- Financial operations (invoicing, expense tracking, budgeting)
- Marketing operations (OTA optimization, pricing strategies)
- Reporting operations (generate reports for Said)

= 50-100 tools easily

With traditional MCP: CONTEXT EXPLOSION
With Code Execution MCP: ~2% overhead

THIS IS NON-NEGOTIABLE for LHCM-OS architecture.
-->

---

### 2.3 MCP Servers

> ⚠️ **WARNING**: Traditional MCP tool-calling is context-expensive. See "Code Execution MCP" section above. Prefer thin wrappers over direct MCP registration.

| Domain                  | Server                           | Status | Notes                                |
| ----------------------- | -------------------------------- | ------ | ------------------------------------ |
| **Filesystem**          | @anthropic/mcp-server-filesystem | ✅     | File operations                      |
| **Git**                 | @anthropic/mcp-server-git        | ✅     | Version control                      |
| **GitHub**              | @anthropic/mcp-server-github     | ✅     | Issues, PRs, repos                   |
| **Linear**              | Official (mcp.linear.app)        | ✅     | Issue tracking, sprints, GitHub sync |
| **Notion**              | Official                         | ✅     | Plan: Free                           |
| **Browser**             | @anthropic/mcp-server-puppeteer  | 🔶     | Web automation                       |
| **Database (SQLite)**   | @anthropic/mcp-server-sqlite     | 🔶     | Local data                           |
| **Database (Postgres)** | Community                        | 🔶     | Production data                      |
| **Google Calendar**     | Community                        | 🔶     | Scheduling (Google Workspace)        |
| **Gmail**               | Community                        | 🔶     | Email (Google Workspace)             |
| **Google Drive**        | Community                        | 🔶     | Files (Google Workspace)             |
| **HotelRunner**         | `[TO BUILD]`                     | ❓     | Villa Thaifa integration             |
| **Video Transcription** | gemini-video-mcp-server          | 🔶     | [RESEARCH: Harvest MCP]              |
| **YouTube**             | mcp-server-youtube-transcript    | 🔶     | Learning digestion                   |
| **Slack**               | Community                        | 🔶     | Team communication                   |
| **HyperTool**           | toolprint/hypertool-mcp          | 🔶     | **500+ tools proxy**                 |

**Linear MCP Config** (Official - May 2025):

```json
{
  "mcpServers": {
    "linear": {
      "command": "npx",
      "args": ["-y", "mcp-remote", "https://mcp.linear.app/mcp"]
    }
  }
}
```

- Auth: OAuth 2.1 with dynamic client registration
- Tools: list_issues, create_issue, update_issue, list_projects, create_comment, etc.
- Hosted by Linear (remote MCP, Cloudflare partnership)
- GitHub sync: Bi-directional issue linking

**Google Workspace MCPs** (Community):

- Google Calendar, Gmail, Google Drive MCPs exist
- Not official Google, but functional
- Consider wrapping via Code Execution pattern instead of direct registration

<!-- [LUX NOTE FOR LHCM-OS]:

**HotelRunner MCP = CRITICAL BLOCKER** for Villa Thaifa Phase 0.

DECISION TO MAKE:
Option A: Build traditional HotelRunner MCP server
- Pros: Standard pattern, can reuse existing MCP infrastructure
- Cons: Adds to context window, limited to traditional MCP constraints
- Effort: ~2-3 days

Option B: Build HotelRunner TypeScript wrapper (Code Execution pattern)
- Pros: Zero context overhead, scalable, aligns with future architecture
- Cons: New pattern, need to learn Code Execution wrapper approach first
- Effort: ~3-5 days (includes learning Code Execution pattern)

RECOMMENDATION: Option B (TypeScript wrapper)
- Investment pays off long-term (scalable architecture)
- Aligns with rest of LHCM-OS
- Can migrate other MCPs later to same pattern

PREREQUISITES before building HotelRunner integration:
1. Study Code Execution MCP architecture (1 day)
2. Create TS wrapper template/pattern (1 day)
3. Document HotelRunner API (0.5 day - we have Repomix data)
4. Build wrapper (1-2 days)
5. Test with browser agent (0.5 day)

Total: 4-5 days to have HotelRunner integration ready for Phase 0.

This should be added to Workstream Master Section 3 (Stream 3 - OTA Prep).
-->

---

## 3. FRONTEND STACK

| Layer                 | Choice                | Status | Notes                          |
| --------------------- | --------------------- | ------ | ------------------------------ |
| **Framework**         | Next.js 15+           | ✅     | App Router, RSC                |
| **UI Library**        | React 19+             | ✅     | Latest                         |
| **Styling**           | Tailwind CSS 4+       | ✅     | Utility-first                  |
| **Component Library** | shadcn/ui             | ✅     | Customizable, accessible       |
| **Icons**             | Lucide                | ✅     | Consistent                     |
| **Forms**             | React Hook Form + Zod | ✅     | Validation                     |
| **State (Client)**    | Zustand               | 🔶     | Simple, performant             |
| **State (Server)**    | TanStack Query        | 🔶     | Server state                   |
| **Animation**         | Framer Motion         | 🔶     | Complex animations             |
| **Charts**            | `[TBD]`               | ❓     | [RESEARCH: Recharts vs Tremor] |
| **Tables**            | TanStack Table        | 🔶     | Complex data grids             |

<!-- [LUX NOTE FOR LHCM-OS]:

LHCM-OS "The Boardroom" dashboard needs:
- Next.js 15+ (App Router) ✅
- shadcn/ui for UI components ✅
- TanStack Query for server state (real-time updates from agents) 🔶
- Charts for analytics (revenue, occupancy, forecast)
  - RECOMMENDATION: Recharts (more flexible, established)
  - Or: Tremor (modern, but newer)
  - DECISION NEEDED: Research both for LHCM-OS dashboard needs
- TanStack Table for complex data (reservations, pricing grid)

All core choices aligned ✅

GAP: Charts library decision needed before Phase 1 UI work starts.
-->

---

## 4. BACKEND STACK

| Layer                      | Choice                       | Status | Notes                                  |
| -------------------------- | ---------------------------- | ------ | -------------------------------------- |
| **API Framework (Python)** | FastAPI                      | ✅     | OpenAPI auto-gen                       |
| **API Framework (TS)**     | Hono                         | 🔶     | Edge-ready, lightweight                |
| **Validation**             | Zod (TS) / Pydantic (Python) | ✅     | Schema-first                           |
| **ORM (Python)**           | SQLModel                     | 🔶     | Pydantic + SQLAlchemy                  |
| **ORM (TS)**               | Drizzle                      | 🔶     | Type-safe, performant                  |
| **Auth**                   | `[TBD]`                      | ❓     | [RESEARCH: Clerk vs Auth.js vs custom] |
| **Background Jobs**        | `[TBD]`                      | ❓     | [RESEARCH: Trigger.dev vs BullMQ]      |
| **Websockets**             | `[TBD]`                      | ❓     | Real-time updates                      |

<!-- [LUX NOTE FOR LHCM-OS]:

**Backend Architecture Decision:**

My LHCM-OS proposal suggests:
- Cloudflare Workers for backend (edge compute)
- Next.js API routes for simple endpoints
- FastAPI for complex agent logic (if needed)

QUESTIONS FOR OMAR:
1. Do we use Hono (TS, edge-ready) or FastAPI (Python, familiar)?
   - LHCM-OS agents are TypeScript (Claude SDK)
   - Complex hotel logic might benefit from Python
   - **RECOMMENDATION**: Start with Hono (edge-native), add FastAPI only if needed

2. Auth solution for LHCM-OS:
   - Clerk (SaaS, easy, $25/month for 1000 users)
   - Auth.js (open-source, self-hosted, free but more work)
   - Custom (full control, most work)
   - **RECOMMENDATION**: Clerk for MVP (speed), migrate to Auth.js if cost becomes issue

3. Background Jobs for LHCM-OS:
   - Trigger.dev (SaaS, declarative, free tier)
   - BullMQ (Redis-based, self-hosted)
   - Cloudflare Queues (serverless, pay-per-use)
   - **RECOMMENDATION**: Cloudflare Queues (aligns with stack, serverless)

4. Websockets for real-time updates:
   - Cloudflare Durable Objects (stateful, WebSocket support)
   - Pusher (SaaS, expensive)
   - Custom WebSocket server (complex)
   - **RECOMMENDATION**: Cloudflare Durable Objects (aligns with stack)

DECISIONS NEEDED before Phase 1:
- [ ] Hono vs FastAPI for backend
- [ ] Auth solution (Clerk recommended)
- [ ] Background jobs (Cloudflare Queues recommended)
- [ ] Websockets (Durable Objects recommended)
-->

---

## 5. DATA LAYER

| Component            | Choice     | Status | Notes                                      |
| -------------------- | ---------- | ------ | ------------------------------------------ |
| **Primary Database** | PostgreSQL | ✅     | Relational, robust                         |
| **Vector Database**  | `[TBD]`    | ❓     | [RESEARCH: pgvector vs Pinecone vs Qdrant] |
| **Cache**            | Redis      | 🔶     | Session, rate limiting                     |
| **Object Storage**   | `[TBD]`    | ❓     | [RESEARCH: S3 vs R2 vs MinIO]              |
| **Search**           | `[TBD]`    | ❓     | [RESEARCH: Meilisearch vs Typesense]       |
| **Message Queue**    | `[TBD]`    | ❓     | Agent communication                        |
| **Local Dev DB**     | SQLite     | ✅     | Simplicity                                 |

<!-- [LUX NOTE FOR LHCM-OS]:

**Database Architecture for LHCM-OS:**

LHCM-OS data needs:
1. **Relational** (structured): Properties, rooms, reservations, pricing, guests
2. **Vector** (semantic): Conversations, documents, memory
3. **Cache** (fast access): Session data, frequently accessed pricing
4. **Object Storage** (files): Guest documents, photos, receipts
5. **Search** (full-text): Find reservations, guests, conversations
6. **Queue** (async): Background tasks (pricing updates, sync jobs)

CLOUDFLARE-NATIVE CHOICES:
- Primary: D1 (serverless SQLite, global read replication) instead of PostgreSQL
  - Pros: Serverless, free tier, read replication, edge-native
  - Cons: Write scaling limits (but LHCM-OS writes are low volume)
- Vector: Cloudflare Vectorize (native vector database)
  - Pros: Serverless, integrated with Workers AI, pay-per-use
  - Cons: New service (beta), may have limitations
- Cache: Cloudflare KV (key-value store, globally replicated)
  - Pros: Serverless, extremely fast reads, free tier
  - Cons: Eventual consistency (but OK for cache)
- Object Storage: Cloudflare R2 (S3-compatible, zero egress fees)
  - Pros: S3-compatible API, zero egress, generous free tier
  - Cons: None significant
- Search: Cloudflare D1 FTS (full-text search in SQLite)
  - Pros: Built-in, no extra service
  - Cons: Limited features vs dedicated search engine
- Queue: Cloudflare Queues (serverless message queue)
  - Pros: Serverless, integrated, pay-per-use
  - Cons: Newer service, limited ecosystem

DECISION FOR LHCM-OS MVP:
Option A (Cloudflare-native, recommended):
- D1 for relational
- Vectorize for semantic search
- KV for cache
- R2 for files
- Queues for async tasks
- Pros: Unified platform, serverless, edge-native, cost-effective
- Cons: Vendor lock-in (but can migrate later if needed)

Option B (Best-of-breed):
- PostgreSQL (managed, e.g. Neon) for relational
- Pinecone for vector
- Redis for cache
- S3 for files
- BullMQ for queues
- Pros: Battle-tested, more features
- Cons: More expensive, more complex ops, latency (not edge)

RECOMMENDATION: Option A (Cloudflare-native) for MVP
- Aligns with rest of stack
- Faster to ship
- Can migrate to Option B later if Cloudflare limits hit

IMPACT ON LHCM-OS PROPOSAL:
- Update A08 Section 3: Use D1 instead of "PostgreSQL" for Phase 1
- Add Vectorize for Phase 2 (semantic search)
-->

---

## 6. INFRASTRUCTURE

### 6.1 Cloud & Hosting

#### Cloudflare (Primary Platform)

| Service                   | Purpose                    | Status | Notes                          |
| ------------------------- | -------------------------- | ------ | ------------------------------ |
| **Registrar**             | Domain (el-mountassir.com) | ✅     | DNS + Security                 |
| **Workers**               | Serverless compute (Edge)  | 🔶     | V8 isolates, global            |
| **Pages**                 | Static + SSR hosting       | 🔶     | Git-ops, preview deploys       |
| **D1**                    | Serverless SQLite          | 🔶     | Read replication (global)      |
| **R2**                    | Object storage (S3-compat) | 🔶     | Zero egress fees               |
| **KV**                    | Key-value store            | 🔶     | Session data, config           |
| **Durable Objects**       | Stateful serverless        | 🔶     | Coordination, SQLite backend   |
| **Queues**                | Message queues             | 🔶     | Async processing               |
| **Vectorize**             | Vector database            | 🔶     | RAG, semantic search           |
| **Workers AI**            | Inference at edge          | 🔶     | LLMs, embeddings               |
| **AutoRAG**               | Managed RAG system         | 🔶     | Auto-ingest from R2            |
| **AI Gateway**            | AI request management      | 🔶     | Caching, analytics, guardrails |
| **Hyperdrive**            | DB connection pooling      | 🔶     | Postgres/MySQL acceleration    |
| **Browser Rendering**     | Headless browser           | 🔶     | Playwright support             |
| **Media Transformations** | Video processing           | 🔶     | Short-form video               |

**Cloudflare Developer Platform 2025 Highlights**:

- Workers + Pages converging into unified experience
- D1 global read replication (sequential consistency)
- R2 Data Catalog (Apache Iceberg for analytics)
- Remote bindings (local dev → deployed resources)
- Container support coming (full Linux, multi-core)

**Pricing**: Free tier generous, pay-as-you-go for scale

<!-- [LUX NOTE FOR LHCM-OS]:

**Cloudflare Services Mapping to LHCM-OS:**

✅ **CONFIRMED USAGE:**
- Workers: Backend API, agent orchestration
- Pages: Next.js hosting (The Boardroom dashboard)
- D1: Primary database (properties, rooms, reservations)
- R2: File storage (photos, documents, receipts)
- KV: Cache (session data, frequently accessed config)
- Queues: Background jobs (pricing sync, OTA updates, email sending)
- Durable Objects: WebSocket connections (real-time dashboard updates)

🔶 **PHASE 2 (Consideration):**
- Vectorize: Semantic search (conversations, documents) - Phase 2
- Workers AI: Edge inference (if we need low-latency AI responses)
- AutoRAG: Managed knowledge base (documentation, past conversations)
- AI Gateway: Rate limiting, caching, analytics for AI calls

❓ **NOT NEEDED (Yet):**
- Hyperdrive: Only if we use PostgreSQL instead of D1
- Browser Rendering: Only if we need server-side screenshots (unlikely)
- Media Transformations: Only if processing videos (not in MVP scope)

**DEPLOYMENT STRATEGY FOR LHCM-OS:**

My proposal says: "Vercel for Next.js OR Cloudflare Pages"

CLARIFICATION:
- **RECOMMENDATION: Cloudflare Pages** (unified platform)
- Next.js on Cloudflare Pages works well (as of 2024)
- Keeps everything in one platform (simpler ops)
- Preview deploys, Git integration built-in
- Can use Vercel if Cloudflare Pages has limitations (but unlikely)

DECISION NEEDED:
- [ ] Confirm Cloudflare Pages for Next.js hosting (recommended)
- [ ] OR use Vercel if specific features needed (specify which)
-->

#### Vercel

| Feature      | Value                            | Status |
| ------------ | -------------------------------- | ------ |
| **Plan**     | Free (Hobby)                     | ✅     |
| **Use Case** | Next.js deployment               | 🔶     |
| **Limits**   | 100GB bandwidth, 100 deploys/day | —      |

**Note**: May use Vercel for Next.js apps, Cloudflare for everything else.

<!-- [LUX NOTE]: See Cloudflare section above. Recommend Cloudflare Pages instead of Vercel for unified platform. -->

#### Comparison: Cloudflare vs Vercel

| Aspect       | Cloudflare                     | Vercel                      |
| ------------ | ------------------------------ | --------------------------- |
| **Compute**  | Workers (Edge V8)              | Serverless Functions        |
| **Database** | D1, Durable Objects            | Postgres (via integrations) |
| **Storage**  | R2 (S3-compat)                 | Blob Storage                |
| **AI**       | Workers AI, AutoRAG, Vectorize | AI SDK (client-side)        |
| **Pricing**  | Pay-per-use, zero egress       | Free tier, then per-seat    |
| **Edge**     | 300+ PoPs                      | ~20 regions                 |

**Decision**: Cloudflare as primary (edge-first, AI-native), Vercel for Next.js if needed.

<!-- [LUX NOTE]: For LHCM-OS, Cloudflare is the clear winner (edge-first, AI-native, unified platform).
Only use Vercel if we hit specific Next.js limitation on Cloudflare Pages (unlikely). -->

### 6.2 Containers & Orchestration

| Component                | Choice         | Status | Notes                               |
| ------------------------ | -------------- | ------ | ----------------------------------- |
| **Containerization**     | Docker         | ✅     | Standard                            |
| **Orchestration (Dev)**  | Docker Compose | ✅     | Local development                   |
| **Orchestration (Prod)** | `[TBD]`        | ❓     | [RESEARCH: K8s vs Nomad vs managed] |
| **Registry**             | `[TBD]`        | ❓     | Container images                    |

<!-- [LUX NOTE FOR LHCM-OS]:

**Containers for LHCM-OS?**

QUESTION: Do we need containers for LHCM-OS if we use Cloudflare Workers (serverless)?

ANSWER: Probably NOT for production (Workers are serverless, no containers).

BUT: Useful for local development:
- Docker Compose for local Postgres/Redis/etc. (if we don't use Cloudflare services locally)
- Or: Use Cloudflare's "wrangler dev" with remote bindings (connect local dev to deployed D1/KV)

RECOMMENDATION: Skip containers for LHCM-OS MVP.
- Use "wrangler dev" with remote bindings for local development
- Cloudflare Workers are already containerized (V8 isolates)
- Simpler stack, faster development
-->

### 6.3 Local Development (Sovereign Node: Nexus)

| Component            | Choice               | Status | Notes                            |
| -------------------- | -------------------- | ------ | -------------------------------- |
| **OS**               | Pop!\_OS 24.04 LTS   | ✅     | COSMIC Desktop (Rust-based)      |
| **Kernel**           | Linux 6.17.9         | ✅     | Latest                           |
| **Shell**            | Bash 5.1.16 + ble.sh | ✅     | Syntax highlighting, multiline   |
| **Prompt**           | Starship             | ✅     | Fast, cross-shell, context-aware |
| **Editor**           | VS Code + Cursor     | ✅     | AI-assisted                      |
| **Terminal**         | VS Code Integrated   | ✅     | ble.sh conflict resolved         |
| **Search**           | ripgrep (rg)         | ✅     | Fast recursive grep              |
| **Fuzzy Finder**     | fzf                  | ✅     | Ctrl+R, Ctrl+T, Alt+C            |
| **Claude Interface** | Claude Code CLI      | ✅     | Primary agent interface          |
| **Browser**          | `[TBD]`              | ❓     | Development                      |

<!-- [LUX NOTE FOR LHCM-OS]:

LHCM-OS development environment on Nexus:
- VS Code + Cursor for code editing ✅
- Claude Code CLI for agent orchestration ✅
- "wrangler dev" for Cloudflare Workers local testing
- Next.js dev server for frontend
- Browser for testing (Firefox? Chrome?)

DECISION NEEDED:
- [ ] Default browser for LHCM-OS development (Firefox vs Chrome vs Arc)
-->

### 6.4 Infrastructure as Code (IaC)

| Component         | Choice                   | Status | Notes                                  |
| ----------------- | ------------------------ | ------ | -------------------------------------- |
| **System Config** | Ansible                  | ✅     | Packages, services, firewall           |
| **Dotfiles**      | Chezmoi                  | ✅     | Templates, secrets, cross-platform     |
| **Bootstrap**     | sovereign-bootstrap repo | ✅     | One-liner setup                        |
| **Cloud IaC**     | `[TBD]`                  | ❓     | [RESEARCH: Pulumi vs Terraform vs SST] |

**Architecture**:

```
Fresh Pop!_OS Install
        │
        ▼
bootstrap.sh (one-liner)
        │
        ├──► Ansible (system packages, services, SSH)
        │
        └──► Chezmoi (dotfiles, templates, secrets)
        │
        ▼
Configured Sovereign Node
```

<!-- [LUX NOTE FOR LHCM-OS]:

**Cloud IaC for LHCM-OS:**

QUESTION: Do we need IaC if using Cloudflare (mostly UI/wrangler CLI)?

ANSWER: YES, for reproducibility and version control.

OPTIONS:
1. **Terraform** (HashiCorp)
   - Pros: Battle-tested, Cloudflare provider exists, declarative
   - Cons: HCL syntax (yet another language)
2. **Pulumi** (Modern)
   - Pros: TypeScript/Python (use languages you know), type-safe
   - Cons: Newer, smaller ecosystem
3. **SST** (Serverless Stack Toolkit)
   - Pros: TypeScript, serverless-native, great DX
   - Cons: Focused on AWS (has Cloudflare support but not primary)

RECOMMENDATION FOR LHCM-OS: **Pulumi** (TypeScript)
- Aligns with TypeScript stack
- Type-safe infrastructure
- Can define Cloudflare Workers, D1, KV, R2, etc. as code
- Good for multi-environment (dev, staging, prod)

DECISION NEEDED:
- [ ] Cloud IaC tool (Pulumi recommended)
- [ ] When to implement (Phase 1 or Phase 2?)
  - Phase 1: Manual wrangler commands (faster)
  - Phase 2: Migrate to Pulumi (reproducible)
-->

---

## 7. DEVOPS & CI/CD

| Component                  | Choice         | Status | Notes                             |
| -------------------------- | -------------- | ------ | --------------------------------- |
| **Version Control**        | Git            | ✅     | Standard                          |
| **Git Host**               | GitHub         | ✅     | Primary                           |
| **CI/CD**                  | GitHub Actions | ✅     | Automation                        |
| **Secrets Management**     | `[TBD]`        | ❓     | [RESEARCH: Doppler vs 1Password]  |
| **Infrastructure as Code** | `[TBD]`        | ❓     | [RESEARCH: Pulumi vs Terraform]   |
| **Monitoring**             | `[TBD]`        | ❓     | [RESEARCH: Grafana vs Datadog]    |
| **Error Tracking**         | `[TBD]`        | ❓     | [RESEARCH: Sentry vs BetterStack] |
| **Logging**                | `[TBD]`        | ❓     | Centralized logs                  |
| **Uptime**                 | `[TBD]`        | ❓     | Health checks                     |

<!-- [LUX NOTE FOR LHCM-OS]:

**CI/CD for LHCM-OS:**

PIPELINE:
1. Push to GitHub
2. GitHub Actions runs:
   - Lint (ESLint/Biome)
   - Type check (TypeScript)
   - Test (Vitest)
   - Build (Next.js + Cloudflare Workers)
3. Deploy to Cloudflare (via wrangler)
   - Preview deploy for PRs
   - Production deploy for main branch

SECRETS MANAGEMENT:
- RECOMMENDATION: **Doppler** (SaaS, $0-10/month, syncs with GitHub Actions)
- Alternative: GitHub Secrets (free, but limited features)
- Alternative: 1Password (good for teams, CLI support)

MONITORING:
- RECOMMENDATION: **BetterStack** (modern, affordable, good for serverless)
- Alternative: Grafana (self-hosted, free, more complex)
- Alternative: Datadog (enterprise, expensive, comprehensive)
- Or: Cloudflare Analytics (built-in, free, limited)

ERROR TRACKING:
- RECOMMENDATION: **Sentry** (industry standard, free tier, good DX)
- Alternative: BetterStack (all-in-one monitoring + errors)

LOGGING:
- Cloudflare Workers Logs (built-in, Logpush to external services)
- BetterStack for aggregation/search

UPTIME:
- BetterStack (included with monitoring)
- Or: Uptime Robot (free, simple)

DECISIONS NEEDED:
- [ ] Secrets management (Doppler recommended)
- [ ] Monitoring stack (BetterStack recommended)
- [ ] Error tracking (Sentry recommended)
-->

---

## 8. DOCUMENTATION

| Component             | Choice          | Status | Notes                                     |
| --------------------- | --------------- | ------ | ----------------------------------------- |
| **API Docs**          | `[TBD]`         | ❓     | [RESEARCH: Redocly vs Scalar vs Fumadocs] |
| **Code-Coupled Docs** | Swimm           | 🔶     | Prevents doc rot                          |
| **Static Site**       | `[TBD]`         | ❓     | [RESEARCH: Starlight vs Docusaurus]       |
| **Diagrams**          | Mermaid         | ✅     | Code-based                                |
| **Architecture (C4)** | Structurizr DSL | 🔶     | Architecture as Code                      |
| **Whiteboard**        | `[TBD]`         | ❓     | Visual collaboration                      |

<!-- [LUX NOTE FOR LHCM-OS]:

**Documentation needs for LHCM-OS:**

1. **API Docs** (for developers extending LHCM-OS):
   - RECOMMENDATION: **Scalar** (modern, interactive, OpenAPI-based)
   - Cloudflare Workers can auto-generate OpenAPI schema
   - Hono has OpenAPI support built-in

2. **Product Docs** (for Said and other hotel owners):
   - RECOMMENDATION: **Starlight** (Astro-based, fast, beautiful)
   - Or: Docusaurus (React-based, more features, heavier)
   - Host on Cloudflare Pages

3. **Architecture Docs**:
   - Mermaid for flow diagrams ✅
   - Structurizr DSL for C4 models (system context, containers, components)
   - Store in repo, render in docs site

DECISION NEEDED:
- [ ] API docs tool (Scalar recommended)
- [ ] Product docs site generator (Starlight recommended)
- [ ] When to build docs site (Phase 2, not MVP)
-->

---

## 9. PROJECT MANAGEMENT

| Component           | Choice      | Status | Notes                                   |
| ------------------- | ----------- | ------ | --------------------------------------- |
| **Task Management** | Linear      | ✅     | Issues, sprints, roadmap (official MCP) |
| **Orchestration**   | Vibe Kanban | ✅     | **GAME CHANGER - Multi-agent control**  |
| **Knowledge Base**  | Notion      | ✅     | Free plan, official MCP                 |
| **Time Tracking**   | `[TBD]`     | ❓     | Billing, productivity                   |
| **Communication**   | `[TBD]`     | ❓     | Team chat                               |

<!-- [LUX NOTE FOR LHCM-OS]:

**VIBE KANBAN = ORCHESTRATION LAYER** 🎯

**What It Is:**
- Open-source "Mission Control" for AI Engineering (BloopAI)
- Industry standard as of Jan 2026
- Transforms: "Chatting with bot" → "Managing fleet of developers"

**Why Game Changer:**
- **Git Worktrees:** Each task = isolated worktree
- **Parallel Execution:** Claude Opus + Claude Sonnet + Gemini work simultaneously
- **No file conflicts:** All in same repo, different worktrees
- **Visual Diffs:** PR-style code review
- **Feedback Loop:** Comment → Agent reads → Retries immediately

**Agent Support:**
- Claude Code (preferred) ✅
- Amp ✅
- Gemini CLI ✅
- OpenAI Codex ✅
- Cursor Agent CLI ✅

**MCP Integration:** Full Model Context Protocol support built-in

**Quickstart:**
```bash
npx vibe-kanban
```
Opens board at `localhost:3000`, auto-detects git repo

**Best Practices:**
- "Context Dump": Load tickets with excessive context
- Small Tickets: Break tasks into <20 steps
- Test Commands: Define in `vibe.config.js`

**For LHCM-OS:**
- Ticket 1: Claude Opus builds backend API (Stream 4)
- Ticket 2: Claude Sonnet creates OTA accounts (Stream 3)
- Ticket 3: Gemini writes documentation
- ALL IN PARALLEL, reviewed separately

**Industry Context:**
- 2025: Models smart, humans = review bottleneck
- 2026: Vibe Kanban = Human-in-the-loop scaling
- Allows 1 senior engineer → manage 5-10 AI juniors

**Decision:** D-W-014 (2025-01-09 16:00) - ADOPTED ✅

**Project Management Stack for LHCM-OS:**
- Linear: Track client issues, sprints, roadmap
- Vibe Kanban: Orchestrate multiple agents on code tasks
- Notion: Store strategy, client notes, meetings
- GitHub: Code + Issues (synced with Linear)

**Workflow:**
1. Omar creates Linear issues (strategic)
2. Omar creates Vibe Kanban tickets (technical)
3. Agents execute tasks in parallel
4. Omar reviews PRs in Vibe UI
5. Approved code merged to main
6. Linear issues auto-update (via GitHub sync)

-->

---

## 10. SECURITY

| Component                  | Choice  | Status | Notes                  |
| -------------------------- | ------- | ------ | ---------------------- |
| **Password Manager**       | `[TBD]` | ❓     | Team credentials       |
| **2FA**                    | `[TBD]` | ❓     | Authentication         |
| **Secrets in CI**          | `[TBD]` | ❓     | GitHub Actions secrets |
| **API Keys Rotation**      | `[TBD]` | ❓     | Automation             |
| **Vulnerability Scanning** | `[TBD]` | ❓     | Dependencies           |

<!-- [LUX NOTE FOR LHCM-OS]:

**Security for LHCM-OS:**

PASSWORD MANAGER:
- RECOMMENDATION: **1Password** (team plan, CLI support, good for secrets in CI)
- Alternative: Bitwarden (open-source, cheaper)

2FA:
- Enable on: GitHub, Cloudflare, Linear, Notion, Google Workspace
- Use: 1Password as authenticator (or Authy)

SECRETS IN CI:
- Doppler (recommended in Section 7) syncs with GitHub Actions
- Or: GitHub Actions Secrets (built-in, free)

API KEYS ROTATION:
- Not automated initially (manual rotation quarterly)
- Phase 2: Consider automation with Doppler or Vault

VULNERABILITY SCANNING:
- GitHub Dependabot (free, built-in, auto-creates PRs)
- Snyk (more features, paid)
- RECOMMENDATION: Use Dependabot ✅

DECISIONS NEEDED:
- [ ] Password manager (1Password recommended)
- [ ] Enable 2FA on all services (immediate)
- [ ] API key rotation policy (quarterly manual, automate in Phase 2)
-->

---

## 11. TESTING

| Layer             | Choice     | Status | Notes                            |
| ----------------- | ---------- | ------ | -------------------------------- |
| **Unit (TS)**     | Vitest     | 🔶     | Fast, Vite-native                |
| **Unit (Python)** | pytest     | ✅     | Standard                         |
| **E2E**           | Playwright | 🔶     | Cross-browser                    |
| **API Testing**   | `[TBD]`    | ❓     | Contract testing                 |
| **BDD**           | `[TBD]`    | ❓     | [RESEARCH: Cucumber integration] |
| **Load Testing**  | `[TBD]`    | ❓     | Performance                      |

<!-- [LUX NOTE FOR LHCM-OS]:

**Testing Strategy for LHCM-OS:**

UNIT TESTS:
- Vitest for TS (frontend + Cloudflare Workers)
- pytest for Python (if we use FastAPI)
- RECOMMENDATION: Start with unit tests for critical business logic
  - Pricing calculations
  - Availability checks
  - Revenue calculations

E2E TESTS:
- Playwright for critical user flows
  - Said logs in, views dashboard, creates reservation
  - Guest makes booking through "The Boardroom"
  - Agent creates OTA listing
- RECOMMENDATION: Add E2E in Phase 2 (not MVP)

API TESTING:
- Not needed if using type-safe schemas (Zod/Pydantic auto-validates)
- Consider contract testing if we have external API integrations (HotelRunner)

LOAD TESTING:
- Defer to Phase 2 (when scaling)
- Use k6 or Artillery (open-source, Cloudflare-friendly)

DECISIONS:
- [ ] Testing approach for MVP (unit tests for business logic, E2E in Phase 2)
- [ ] When to implement tests (TDD vs add after MVP works)
  - RECOMMENDATION: Add tests for critical paths after MVP validated
-->

---

## 11.1 CODE QUALITY

### Python (Astral Ecosystem)

| Tool     | Purpose             | Status | Notes                       |
| -------- | ------------------- | ------ | --------------------------- |
| **uv**   | Package management  | ✅     | Replaces pip, poetry, pyenv |
| **ruff** | Linter + Formatter  | ✅     | Extremely fast, Rust-based  |
| **mypy** | Static type checker | ✅     | Strict mode                 |

**Configuration** (`pyproject.toml`):

```toml
[tool.ruff]
line-length = 100
target-version = "py312"

[tool.ruff.lint]
select = ["E", "F", "I", "N", "W"]

[tool.mypy]
python_version = "3.12"
strict = true
```

<!-- [LUX NOTE FOR LHCM-OS]:

Python code quality tools confirmed ✅
- uv for package management
- ruff for linting + formatting
- mypy for type checking

Use if we add FastAPI backend to LHCM-OS.
-->

### TypeScript

| Tool           | Purpose       | Status | Notes                                |
| -------------- | ------------- | ------ | ------------------------------------ |
| **TypeScript** | Type checking | ✅     | Strict mode                          |
| **ESLint**     | Linter        | 🔶     | Or Biome?                            |
| **Prettier**   | Formatter     | 🔶     | Or Biome?                            |
| **Biome**      | All-in-one    | 🔶     | [RESEARCH: Biome vs ESLint+Prettier] |

<!-- [LUX NOTE FOR LHCM-OS]:

**TS Code Quality Decision:**

QUESTION: ESLint + Prettier OR Biome?

COMPARISON:
- ESLint + Prettier: Industry standard, more plugins, slower
- Biome: Rust-based (like ruff), faster, all-in-one, newer

RECOMMENDATION: **Biome** for LHCM-OS
- Aligns with Omar's preference for Rust-based tools (ruff, uv, Bun)
- Faster (important for large Next.js project)
- All-in-one (simpler setup, like Bun)
- Good enough for most use cases

DECISION NEEDED:
- [ ] Confirm Biome for LHCM-OS (recommended)
- [ ] OR stick with ESLint + Prettier (if specific plugin needed)
-->

---

## 12. AGENT ARCHITECTURE (Swarm-Specific)

### 12.0 Agentic Architecture Planes (2026 Pattern)

The stack is structurally divided into two distinct planes:

#### Data Plane (The "Doing" - Execution & State)

| Component           | Purpose                        | Status | Choice                           |
| ------------------- | ------------------------------ | ------ | -------------------------------- |
| **LLMs**            | Reasoning, planning, decisions | ✅     | Claude Opus/Sonnet/Haiku         |
| **Vector Database** | RAG, semantic search           | ❓     | [RESEARCH: pgvector vs Pinecone] |
| **Memory Systems**  | Short-term + Long-term context | ❓     | [GAP]                            |
| **Tools/Actions**   | External system interaction    | 🔶     | MCP Servers                      |
| **Data Ingestion**  | Pull/process data              | ❓     | [TBD]                            |
| **Compute**         | Inference hosting              | 🔶     | Cloudflare / Edge                |

#### Control Plane (The "Managing" - Governance)

| Component            | Purpose                       | Status | Choice                                 |
| -------------------- | ----------------------------- | ------ | -------------------------------------- |
| **Interoperability** | Agent-to-Agent ("USB-C")      | ✅     | MCP + A2A protocols                    |
| **Telemetry**        | Semantic traces, self-healing | ❓     | [RESEARCH: Arize Phoenix vs LangSmith] |
| **Identity (NHI)**   | Agent personas, RBAC          | ❓     | [RESEARCH: Okta NHI vs custom]         |
| **Evaluation**       | LLM-as-a-Judge, red teaming   | ❓     | [RESEARCH: DeepEval vs AgentOps]       |
| **Orchestration**    | Task chains, routing          | ✅     | Claude Agent SDK                       |
| **Governance**       | Real-time guardrails          | ❓     | [RESEARCH: Guardrails AI vs NeMo]      |

<!-- [LUX NOTE FOR LHCM-OS]:

**Agent Architecture for LHCM-OS "Digital C-Suite":**

DATA PLANE (Execution):
- ✅ LLMs: Claude Opus (CEO), Sonnet (GM/CFO/Revenue), Haiku (fast responses)
- ❓ Vector DB: Cloudflare Vectorize (Phase 2, for semantic search of conversations/docs)
- ❓ Memory: File-based (Phase 1), Database (Phase 2) - need to design memory schema
- 🔶 Tools: Code Execution MCP wrappers (HotelRunner, Booking.com, Calendar, etc.)
- ❓ Data Ingestion: Polling HotelRunner API, webhooks from Booking.com
- 🔶 Compute: Cloudflare Workers (edge compute for agents)

CONTROL PLANE (Governance):
- ✅ Interoperability: MCP (agents communicate via MCP protocol)
- ❓ Telemetry: Need agent observability (what agents are doing, success/failure)
  - RECOMMENDATION: Arize Phoenix (self-hosted, open-source, semantic traces)
  - Alternative: LangSmith (SaaS, simpler, paid)
- ❓ Identity (NHI): Each agent has identity (GM, CFO, Revenue, CTO)
  - RECOMMENDATION: Custom implementation (simple role-based, store in D1)
  - Alternative: Okta NHI (enterprise, expensive, overkill for MVP)
- ❓ Evaluation: How do we know agents are working correctly?
  - RECOMMENDATION: Defer to Phase 2 (manual testing initially)
  - Future: DeepEval (open-source, LLM-as-a-Judge)
- ✅ Orchestration: Claude Agent SDK (hierarchical: CEO → GM → agents)
- ❓ Governance: Real-time guardrails (prevent agents from dangerous actions)
  - RECOMMENDATION: Custom implementation (approval workflows for high-risk actions)
  - Future: Guardrails AI (if we need complex policies)

CRITICAL GAPS FOR LHCM-OS MVP:
1. Memory schema (how agents remember conversations, decisions)
2. Agent identity & permissions (what each agent can/cannot do)
3. Telemetry (observability into agent actions)

DECISIONS NEEDED:
- [ ] Memory architecture (Phase 1 simple, Phase 2 sophisticated)
- [ ] Agent identity system (custom RBAC recommended)
- [ ] Telemetry solution (Arize Phoenix recommended for Phase 2)
-->

### 12.1 Core Components

| Component                   | Choice                                   | Status | Notes                      |
| --------------------------- | ---------------------------------------- | ------ | -------------------------- |
| **Orchestration Pattern**   | Hierarchical (CIO → CoS → Lead → Agents) | ✅     | Defined                    |
| **Agent Definition Format** | `[TBD]`                                  | ❓     | YAML? JSON?                |
| **Skill Format**            | Agent Skills (Anthropic)                 | 🔶     | [RESEARCH NEEDED]          |
| **Memory Storage**          | `[TBD]`                                  | ❓     | File-based vs DB vs hybrid |
| **Context Passing**         | `[TBD]`                                  | ❓     | Between agents             |
| **Parallelization**         | Git Worktrees                            | 🔶     | Isolation pattern          |

<!-- [LUX NOTE FOR LHCM-OS]:

**🚨 CRITICAL GAP: Agent Definition Format**

This is P0 BLOCKING for LHCM-OS Digital C-Suite.

NEED TO DEFINE:
- How do we define an agent? (GM agent, CFO agent, Revenue agent)
- What properties? (name, role, capabilities, tools, memory, constraints)
- What format? (JSON, YAML, TypeScript class)

RESEARCH NEEDED:
1. Anthropic Agent Skills format (if released)
2. Community patterns (Vercel AI SDK, LangChain)
3. Custom format

RECOMMENDATION FOR LHCM-OS MVP:
Define simple JSON schema for agents:

```json
{
  "agent_id": "lhcm-os-gm",
  "name": "General Manager",
  "role": "Manage daily operations, coordinate staff, optimize occupancy",
  "model": "claude-sonnet-4-5",
  "tools": ["hotelrunner", "calendar", "email"],
  "memory": {
    "type": "persistent",
    "location": "d1://lhcm-os-db/agent_memory"
  },
  "permissions": ["read_reservations", "update_pricing", "send_emails"],
  "constraints": [
    "Cannot cancel reservations without owner approval",
    "Cannot change pricing by more than 20% without consultation"
  ]
}
```

Store agents in: `./agents/` directory, one JSON per agent.

DECISION NEEDED:
- [ ] Research Anthropic Agent Skills format (if available)
- [ ] Define LHCM-OS agent schema (JSON recommended)
- [ ] Document schema in A08 LHCM-OS Strategy
-->

### 12.2 Swarm Roles → Tools Mapping

| Role               | Primary Tools                | Status      |
| ------------------ | ---------------------------- | ----------- |
| **The Sentinel**   | Logging MCP, Metrics MCP     | `[GAP]`     |
| **The Librarian**  | Filesystem, Database, Search | `[PARTIAL]` |
| **The Strategist** | Calendar, Task Manager       | `[GAP]`     |
| **The Ghost**      | `[TBD]`                      | ❓          |
| **The Executor**   | Git, GitHub, Code Execution  | `[PARTIAL]` |

<!-- [LUX NOTE]: This is for Omar's personal swarm (not LHCM-OS specific).

For LHCM-OS, roles are:
- CEO/Chairman (Said's interface, strategic directives)
- General Manager (daily operations, coordination)
- CFO (financial oversight, budgeting)
- Revenue Manager (pricing, occupancy optimization)
- CTO (technical operations, integrations)

These map to different tools than personal swarm. -->

### 12.3 Memory Architecture

| Vector                | Storage                         | Status | Notes                        |
| --------------------- | ------------------------------- | ------ | ---------------------------- |
| **Provenance (Past)** | `[TBD]`                         | ❓     | Episodic, Semantic, Implicit |
| **Instance (Now)**    | Context Window + Working Memory | 🔶     | Sensory, Working, Metamemory |
| **Intent (Next)**     | `[TBD]`                         | ❓     | Prospective triggers         |
| **Flux**              | `[TBD]`                         | ❓     | Affective, Procedural        |

<!-- [LUX NOTE FOR LHCM-OS]:

**Memory Architecture for LHCM-OS Agents:**

CRITICAL: Agents need to remember past interactions to provide continuity.

TYPES OF MEMORY NEEDED:
1. **Episodic** (Past events): "Said asked about occupancy on Jan 5"
2. **Semantic** (Knowledge): "Room 12 is Suite Présidentielle, needs photos"
3. **Working** (Current context): "Currently processing reservation for Room 7"
4. **Prospective** (Future intent): "Send pricing update to Said every Monday"
5. **Procedural** (How-to): "When guest books, send confirmation email"

STORAGE APPROACH:
- Phase 1 (MVP): Simple file-based memory (JSON files in agent's directory)
  - Each agent has `memory.json` with recent interactions
  - Limited to last N interactions (e.g., 100)
- Phase 2: Database-backed memory (D1)
  - `agent_memory` table: agent_id, timestamp, memory_type, content
  - Vector embeddings in Vectorize for semantic search
  - Infinite storage, semantic retrieval

DECISION FOR MVP:
- [ ] Design simple file-based memory schema
- [ ] Implement memory persistence in agent SDK
- [ ] Plan migration to DB-backed memory (Phase 2)
-->

---

## 13. CLIENT-SPECIFIC (Villa Thaifa)

| Component                   | Choice                             | Status       | Notes              |
| --------------------------- | ---------------------------------- | ------------ | ------------------ |
| **Channel Manager**         | HotelRunner                        | ✅           | Already in use     |
| **HotelRunner Integration** | Custom MCP Server                  | `[TO BUILD]` | API + REST/XML     |
| **Booking Platforms**       | Booking.com, Expedia, Airbnb, etc. | 🔶           | Via HotelRunner    |
| **Property Management**     | `[TBD]`                            | ❓           | Internal dashboard |
| **Pricing Engine**          | `[TBD]`                            | ❓           | Dynamic pricing    |
| **Analytics**               | `[TBD]`                            | ❓           | Revenue insights   |

<!-- [LUX NOTE FOR LHCM-OS]:

**🚨 CRITICAL: HotelRunner Integration = P0 BLOCKER**

CURRENT STATUS: [TO BUILD]
BLOCKING: Villa Thaifa Phase 0 (OTA activation)

RECOMMENDATION (from Section 2.3 analysis):
- Build HotelRunner TypeScript wrapper (not traditional MCP)
- Use Code Execution MCP pattern
- Effort: 4-5 days

PREREQUISITE WORK:
1. Study Code Execution MCP architecture (1 day)
2. Create TS wrapper template (1 day)
3. Document HotelRunner API (0.5 day - we have data)
4. Build wrapper (1-2 days)
5. Test with browser agent (0.5 day)

This should be Stream 3 prerequisite in Workstream Master.

PROPERTY MANAGEMENT DASHBOARD:
- This IS "The Boardroom" in LHCM-OS proposal
- Next.js frontend with shadcn/ui
- Realtime updates via Durable Objects WebSockets
- Shows: occupancy, revenue, upcoming reservations, agent activity

PRICING ENGINE:
- Part of Revenue Manager agent in LHCM-OS
- Phase 1: Simple rule-based (Najib's "1 hour" approach)
- Phase 2: ML-based dynamic pricing (demand-based, competitor analysis)

ANALYTICS:
- Part of CFO agent in LHCM-OS
- Dashboard shows: revenue, occupancy, booking sources, trends
- Export to PDF for Said's review
-->

---

## 14. LEARNING & KNOWLEDGE CAPTURE

| Component                | Choice               | Status       | Notes              |
| ------------------------ | -------------------- | ------------ | ------------------ |
| **Video Digestion**      | Harvest MCP          | `[TO BUILD]` | Gemini-based       |
| **Course Platform**      | IndyDevDan (PAC/TAC) | ✅           | Primary curriculum |
| **Note Taking**          | `[TBD]`              | ❓           | Personal knowledge |
| **Spaced Repetition**    | `[TBD]`              | ❓           | Retention          |
| **Bookmarks/Read Later** | `[TBD]`              | ❓           | Resource curation  |

<!-- [LUX NOTE]: This is for Omar's personal learning, not LHCM-OS specific. -->

---

## 15. 2026 "AI INNOVATOR" REFERENCE STACK

From 2026 Agentic Stack research - our target alignment:

| Category             | Reference                    | Our Choice                | Status | Delta     |
| -------------------- | ---------------------------- | ------------------------- | ------ | --------- |
| **Frontend**         | Next.js / Tailwind           | Next.js / Tailwind        | ✅     | Aligned   |
| **AI & Logic**       | Python (UV) + FastAPI        | Python (UV) + FastAPI     | ✅     | Aligned   |
| **Orchestration**    | Claude Agent SDK             | Claude Agent SDK          | ✅     | Aligned   |
| **Interoperability** | MCP                          | MCP                       | ✅     | Aligned   |
| **Database**         | pgvector (Vector-Native SQL) | `[TBD]`                   | ❓     | Gap       |
| **Edge**             | Cloudflare Workers / Hono    | Cloudflare Workers / Hono | 🔶     | Candidate |
| **Identity**         | Okta NHI / Pangea            | `[TBD]`                   | ❓     | Gap       |
| **Evaluation**       | DeepEval / AgentOps          | `[TBD]`                   | ❓     | Gap       |
| **Governance**       | Guardrails AI / NeMo         | `[TBD]`                   | ❓     | Gap       |

**Alignment Score**: 5/9 confirmed, 4 gaps remaining

<!-- [LUX NOTE FOR LHCM-OS]:

GAPS TO ADDRESS FOR LHCM-OS:
1. **Database**: Use Cloudflare Vectorize (not pgvector) for vector store
   - Aligns with Cloudflare-native stack
   - Decision: Vectorize for Phase 2 ✅
2. **Identity (NHI)**: Custom RBAC for agent permissions
   - Okta NHI is overkill for MVP
   - Decision: Custom implementation ✅
3. **Evaluation**: Defer to Phase 2 (manual testing initially)
   - Future: DeepEval for LLM-as-a-Judge
   - Decision: Defer ✅
4. **Governance**: Custom approval workflows
   - Guardrails AI is overkill for MVP
   - Decision: Custom implementation ✅

REVISED ALIGNMENT SCORE: 9/9 (all decisions made) ✅
-->

---

## 16. OPEN DECISIONS (Pending Validation)

| Decision               | Options                           | Leaning    | Blocker? | Notes                                  |
| ---------------------- | --------------------------------- | ---------- | -------- | -------------------------------------- |
| **JS Runtime**         | Bun vs Node+pnpm                  | Bun        | No       | Bun installed, fast, all-in-one        |
| **TS Linting**         | ESLint+Prettier vs Biome          | Biome?     | No       | Biome is faster, all-in-one (like Bun) |
| **Vector DB**          | pgvector vs Pinecone vs Qdrant    | pgvector?  | Yes      | Affects RAG architecture               |
| **Primary Cloud**      | Cloudflare vs Vercel vs Railway   | Cloudflare | No       | Edge-first, Workers, R2, D1            |
| **Cloud IaC**          | Pulumi vs Terraform vs SST        | `[TBD]`    | No       | SST for serverless?                    |
| **Auth**               | Clerk vs Auth.js vs Custom        | `[TBD]`    | Yes      | Affects user management                |
| **Monitoring**         | Grafana vs Datadog vs BetterStack | `[TBD]`    | No       | Cost vs features                       |
| **Agent Telemetry**    | Arize Phoenix vs LangSmith        | `[TBD]`    | No       | Self-hosted vs SaaS                    |
| **Mono vs Multi Repo** | Mono (Nexus) vs Multi             | Mono?      | Yes      | Foundational                           |
| **Charts Library**     | Recharts vs Tremor                | `[TBD]`    | No       | Dashboard needs                        |

<!-- [LUX NOTE - RECOMMENDATIONS FOR LHCM-OS]:

Based on analysis of LHCM-OS needs, here are my recommendations:

1. **TS Linting**: Biome ✅ (faster, all-in-one, aligns with Rust-based tools)
2. **Vector DB**: Cloudflare Vectorize (Phase 2) ✅ (aligns with stack, serverless)
3. **Primary Cloud**: Cloudflare ✅ (confirmed, edge-first, AI-native)
4. **Cloud IaC**: Pulumi (TypeScript) ✅ (type-safe, aligns with stack)
5. **Auth**: Clerk ✅ (fast to MVP, migrate to Auth.js if cost issue)
6. **Monitoring**: BetterStack ✅ (modern, affordable, serverless-friendly)
7. **Agent Telemetry**: Arize Phoenix (Phase 2) ✅ (self-hosted, semantic traces)
8. **Mono vs Multi Repo**: Mono ✅ (simpler for MVP, can split later)
9. **Charts Library**: Recharts ✅ (more flexible, established)

BLOCKER DECISIONS FOR LHCM-OS MVP:
- [x] Primary Cloud: Cloudflare ✅
- [x] Vector DB: Vectorize (Phase 2) ✅
- [ ] Auth: Clerk (recommended, needs Omar confirmation)
- [ ] Mono repo: Yes (recommended, needs Omar confirmation)
-->

---

## GAP ANALYSIS SUMMARY

### Critical Gaps (P0 - Blocking)

| Gap                     | Impact                 | Priority |
| ----------------------- | ---------------------- | -------- |
| Agent Definition Format | Can't define agents    | P0       |
| Memory Storage Strategy | Can't persist learning | P0       |
| Code Execution Pattern  | Can't scale tools      | P0       |
| HotelRunner MCP         | Client blocked         | P0       |

<!-- [LUX NOTE FOR LHCM-OS]:

ALL 4 CRITICAL GAPS AFFECT LHCM-OS MVP:

1. **Agent Definition Format**:
   - BLOCKING: Can't define GM, CFO, Revenue agents
   - ACTION: Research Anthropic Skills, define JSON schema
   - ETA: 1-2 days

2. **Memory Storage Strategy**:
   - BLOCKING: Agents can't remember past interactions
   - ACTION: Design file-based memory (Phase 1), plan DB migration (Phase 2)
   - ETA: 2-3 days

3. **Code Execution Pattern**:
   - BLOCKING: Can't scale to 50-100 tools needed for LHCM-OS
   - ACTION: Study Code Execution MCP, create TS wrapper template
   - ETA: 1-2 days

4. **HotelRunner MCP**:
   - BLOCKING: Villa Thaifa Phase 0 can't proceed
   - ACTION: Build HotelRunner TS wrapper using Code Execution pattern
   - ETA: 4-5 days

TOTAL PREREQUISITE WORK: 8-12 days before LHCM-OS MVP can start.

These should be added to Workstream Master as Stream 4 prerequisites.
-->

### Important Gaps (P1 - Degraded Experience)

| Gap                  | Impact                  | Priority |
| -------------------- | ----------------------- | -------- |
| Vector Database      | No semantic search      | P1       |
| Auth Solution        | No user management      | P1       |
| Monitoring Stack     | Blind operations        | P1       |
| Background Jobs      | No async processing     | P1       |
| Telemetry (Semantic) | No agent self-debugging | P1       |
| Agent Identity (NHI) | No permission control   | P1       |

<!-- [LUX NOTE FOR LHCM-OS]:

P1 GAPS - IMPACT ON LHCM-OS:

1. **Vector Database**: Phase 2 (not blocking MVP)
   - Cloudflare Vectorize for semantic search of conversations/docs

2. **Auth Solution**: Phase 1 (needed for MVP)
   - Clerk recommended (fast to integrate)
   - ACTION: Confirm decision with Omar

3. **Monitoring Stack**: Phase 1 (important for production)
   - BetterStack recommended
   - ACTION: Set up after MVP deployed

4. **Background Jobs**: Phase 1 (needed for MVP)
   - Cloudflare Queues recommended
   - ACTION: Design job queue architecture

5. **Telemetry**: Phase 2 (not blocking MVP)
   - Arize Phoenix for agent observability
   - Manual testing sufficient for MVP

6. **Agent Identity**: Phase 1 (needed for MVP)
   - Custom RBAC recommended
   - ACTION: Design agent permission system

TOTAL PHASE 1 WORK: 3-5 days (Auth, Background Jobs, Agent Identity)
-->

### Nice-to-Have Gaps (P2)

| Gap               | Impact          | Priority |
| ----------------- | --------------- | -------- |
| Local LLM         | No offline mode | P2       |
| Spaced Repetition | Slower learning | P2       |
| Load Testing      | Unknown limits  | P2       |

<!-- [LUX NOTE]: These are nice-to-have, not blocking LHCM-OS. -->

### Resolved (Previously Gaps)

| Item                     | Resolution        | Date       |
| ------------------------ | ----------------- | ---------- |
| Package Manager (Python) | uv (Astral)       | 2026-01-07 |
| Package Manager (JS)     | Bun               | 2026-01-07 |
| Shell                    | Bash + ble.sh     | 2026-01-07 |
| Prompt                   | Starship          | 2026-01-07 |
| IaC                      | Ansible + Chezmoi | 2026-01-07 |
| Domain                   | el-mountassir.com | 2026-01-07 |

---

## EVOLUTION LOG

| Date       | Change                                | Reason                                       |
| ---------- | ------------------------------------- | -------------------------------------------- |
| 2026-01-09 | v0.1.3-lux.0 - Lux annotations        | Analyzed alignment with LHCM-OS Strategy     |
| 2026-01-07 | v0.1.1 - Major update                 | Integrated workstation docs, confirmed tools |
| 2026-01-07 | Added Domain section                  | el-mountassir.com purchased                  |
| 2026-01-07 | Added Hardware section                | Nexus workstation specs                      |
| 2026-01-07 | Confirmed: uv, Bun, ble.sh, Starship  | From existing docs                           |
| 2026-01-07 | Added Data/Control Plane architecture | 2026 Agentic Stack pattern                   |
| 2026-01-07 | Added IaC section                     | Ansible + Chezmoi confirmed                  |
| 2026-01-07 | Added Code Quality section            | ruff, mypy ecosystem                         |
| 2026-01-07 | Initial creation                      | Capture current state                        |

---

## META

**This document**:

- Is the SSOT for technology decisions
- Uses placeholders to mark unknowns
- Evolves with each research session
- Informs architecture decisions

**Update Triggers**:

- Research session completes
- New tool discovered
- Gap filled
- Decision made

---

_"The stack is not a destination, it's a journey of continuous refinement."_

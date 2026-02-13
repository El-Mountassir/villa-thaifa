# Villa Thaifa — Technical Context

**Version:** 0.1.0-alpha.0  
**Date:** 2026-01-09  
**Related:** villa-thaifa-client-brief-v0.1.0.md

---

## 1. CURRENT TECHNICAL APPROACH

### 1.1 Browser Automation (Current)

**Method:** Claude Code + Chrome
```bash
claude --chrome
```

**Pros:**
- Works immediately
- No API integration needed
- Visual feedback

**Cons:**
- High token consumption
- Manual browser automation
- Not scalable
- Fragile (UI changes break it)

**Status:** Working but NOT optimal

---

## 2. TARGET TECHNICAL APPROACH

### 2.1 HotelRunner API Integration

**API Types Available:**
- REST API ✅
- XML API ✅

**Documentation:**
- https://developers.hotelrunner.com/

**Integration Options:**

#### Option A: MCP Server (Model Context Protocol)
```
Custom MCP Server: hotelrunner-mcp
```

**Pros:**
- Standard Claude integration
- Reusable across agents
- Type-safe operations

**Cons:**
- Context window consumption
- Limited to MCP protocol capabilities

---

#### Option B: Code Execution Pattern (RECOMMENDED)

**Research Period:** July 2025 - January 2026

**Key Players:**
- Anthropic (native sandbox)
- Cloudflare (edge functions)
- Docker (containerization)

**Key Insight:**
> **"Thousands of tools without context window bloat"**

**Benefit:**
- Preserve ULTRA VALUABLE context window
- Scale to hundreds/thousands of operations
- Modular tool architecture

**Resources to Research:**
- Anthropic's Code Execution announcements
- Cloudflare Workers SDK
- Docker integration patterns
- E2B sandbox integration

---

### 2.2 Architecture Pattern

```
┌─────────────────────────────────────────────┐
│     Chief Orchestrator (Claude Opus 4.5)    │
│           Strategic Reasoning                │
└──────────────────┬──────────────────────────┘
                   │
                   │ Commands
                   ▼
┌─────────────────────────────────────────────┐
│    Lead Orchestrator (Claude Sonnet 4.5)    │
│           Task Coordination                  │
└──────────────────┬──────────────────────────┘
                   │
        ┌──────────┴──────────┐
        │                     │
        ▼                     ▼
┌─────────────┐       ┌─────────────┐
│  Worker     │       │  Worker     │
│  Agents     │       │  Agents     │
│ (Sonnet/    │       │ (Gemini     │
│  Haiku)     │       │  Flash)     │
└─────────────┘       └─────────────┘
        │                     │
        └──────────┬──────────┘
                   │
                   ▼
        ┌─────────────────────┐
        │   Code Execution     │
        │   Environment        │
        │ (HotelRunner Tools)  │
        └─────────────────────┘
```

**Question:** Chief Orchestrator + Lead Orchestrator = Overkill?
**Answer:** TBD — depends on complexity

---

## 3. DATA ARCHITECTURE

### 3.1 Current State
- **Format:** Documents (Word/PDF/Markdown)
- **Location:** GitHub repo (unstructured)
- **Problem:** Not machine-readable

### 3.2 Target State (Everything-as-Code)

**Database Schema Needed:**
```sql
-- Rooms
CREATE TABLE rooms (
    room_id INTEGER PRIMARY KEY,
    room_number TEXT NOT NULL UNIQUE,
    room_type TEXT,
    capacity INTEGER,
    facilities JSON
);

-- Bookings
CREATE TABLE bookings (
    booking_id TEXT PRIMARY KEY,
    room_id INTEGER,
    platform TEXT, -- 'booking.com', 'airbnb', etc.
    check_in DATE,
    check_out DATE,
    guest_name TEXT,
    status TEXT,
    FOREIGN KEY (room_id) REFERENCES rooms(room_id)
);

-- Pricing
CREATE TABLE pricing (
    pricing_id INTEGER PRIMARY KEY,
    room_id INTEGER,
    season TEXT, -- 'peak', 'high', 'medium', 'low'
    rate DECIMAL,
    valid_from DATE,
    valid_to DATE,
    FOREIGN KEY (room_id) REFERENCES rooms(room_id)
);
```

---

## 4. INTEGRATION REQUIREMENTS

### 4.1 Platform Sync (via HotelRunner)

**Challenge:** Keep ALL platforms in sync
- Inventory updates
- Pricing changes
- Availability blocks
- Bookings

**Solution:** HotelRunner Channel Manager
- Single source of truth
- Automatic propagation to all OTAs
- Real-time sync

---

### 4.2 Room Configuration Normalization

**Problem:**
- Booking.com uses **Room Type** (grouped)
- HotelRunner uses **Room Number** (individual)

**Solution:**
1. Fetch current Booking.com configuration
2. Map Room Types → Individual Rooms
3. Update Booking.com via API/UI
4. Verify sync with HotelRunner

**API Requirements:**
- Read current Booking.com config
- Update room configuration
- Verify changes propagated

---

## 5. AGENT SKILLS & TOOLS

### 5.1 Required Skills

| Skill | Purpose | Status |
|-------|---------|--------|
| HotelRunner API Client | CRUD operations | 🔴 To Build |
| Booking Platform Sync | Multi-platform coordination | 🔴 To Build |
| Pricing Calculator | Seasonal pricing optimization | 🔴 To Build |
| Competitor Scraper | Market research | 🔴 To Build |
| Data Validator | Ensure consistency | 🔴 To Build |

### 5.2 MCP Servers Needed

| Server | Purpose | Status |
|--------|---------|--------|
| **hotelrunner-mcp** (Custom) | HotelRunner API integration | 🔴 To Build |
| **filesystem** (@anthropic) | File operations | ✅ Available |
| **git** (@anthropic) | Version control | ✅ Available |
| **github** (@anthropic) | Repo management | ✅ Available |
| **puppeteer** (Community) | Browser automation (fallback) | 🟡 Available |

---

## 6. INFRASTRUCTURE

### 6.1 Development Environment

**Current:**
- OS: Pop!_OS 22.04 LTS
- Editor: VS Code
- CLI Tools: claude, gemini-cli, codex-cli

**Planned Migration:**
- OS: Pop!_OS 24.04 LTS
- Username: director
- Hostname: nexus

---

### 6.2 Hosting & Deployment

**Options to Evaluate:**
- Cloudflare Workers (edge computing)
- Vercel (frontend + serverless)
- Railway/Render (backend services)
- Self-hosted (VPS)

**Criteria:**
- Cost
- Scalability
- Maintenance burden
- Agent compatibility

---

## 7. SECURITY & COMPLIANCE

### 7.1 API Keys Management

**Required API Keys:**
- HotelRunner API key
- Booking.com API credentials (if available)
- Other OTA credentials

**Storage:**
- Environment variables (`.env`)
- Secrets manager (production)
- Never in git

---

### 7.2 Data Privacy

**Guest Data:**
- PII (Personally Identifiable Information)
- GDPR compliance considerations
- Data retention policies

**Recommendation:**
- Minimal data storage
- Encryption at rest
- Clear data deletion policy

---

## 8. MONITORING & OBSERVABILITY

### 8.1 What to Monitor

| Metric | Why | Tool |
|--------|-----|------|
| API Health | Detect outages | TBD |
| Sync Status | Ensure consistency | TBD |
| Booking Conflicts | Prevent overbooking | TBD |
| Revenue Metrics | Track performance | TBD |
| Agent Performance | Optimize workflows | TBD |

---

### 8.2 Alerting

**Critical Alerts:**
- Sync failures
- Booking conflicts
- API quota exhaustion
- System errors

**Notification Channels:**
- Email (Omar)
- Slack/Discord
- Dashboard

---

## 9. TESTING STRATEGY

### 9.1 Test Types

| Type | Coverage | Status |
|------|----------|--------|
| Unit Tests | Individual functions | 🔴 To Create |
| Integration Tests | API interactions | 🔴 To Create |
| E2E Tests | Full workflows | 🔴 To Create |
| Load Tests | Performance under load | 🔴 To Create |

---

### 9.2 Test Environment

**Requirements:**
- Sandbox HotelRunner account
- Test OTA accounts
- Mock data

---

## 10. DOCUMENTATION REQUIREMENTS

### 10.1 For Agents

- [ ] API documentation (HotelRunner)
- [ ] System architecture diagrams
- [ ] Workflow definitions
- [ ] Error handling procedures
- [ ] Rollback procedures

### 10.2 For Omar

- [ ] Operations manual
- [ ] Troubleshooting guide
- [ ] Deployment procedures
- [ ] Configuration management

### 10.3 For Said (Client)

- [ ] User manual
- [ ] FAQ
- [ ] Training materials
- [ ] Support contact info

---

## 11. PERFORMANCE REQUIREMENTS

| Metric | Target | Rationale |
|--------|--------|-----------|
| Sync Latency | < 5 minutes | Real-time availability |
| API Response Time | < 2 seconds | User experience |
| System Uptime | 99.5% | Business continuity |
| Data Accuracy | 100% | Zero overbooking |

---

## 12. MIGRATION PATH

### From Document-Based to Code-Based

**Step 1:** Inventory current documentation
**Step 2:** Extract structured data
**Step 3:** Define schemas (database, config)
**Step 4:** Generate code from data
**Step 5:** Validate against source
**Step 6:** Cutover

---

## 13. OPEN TECHNICAL QUESTIONS

| # | Question | Impact | Status |
|---|----------|--------|--------|
| T1 | MCP vs Code Execution? | Architecture | 🔴 OPEN |
| T2 | Mono-repo vs Multi-repo? | Organization | 🔴 OPEN |
| T3 | Database choice (SQLite/Postgres)? | Data layer | 🔴 OPEN |
| T4 | Hosting platform? | Deployment | 🔴 OPEN |
| T5 | Monitoring solution? | Observability | 🔴 OPEN |

---

**Next:** See `villa-thaifa-decisions-log.md` for architectural decisions.

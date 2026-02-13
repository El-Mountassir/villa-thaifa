# VILLA THAIFA — WORKSTREAM MASTER
## Centralized Command & Control Document

**Version:** 0.1.0-alpha.0  
**Date:** 2025-01-09  
**Status:** LIVING DOCUMENT (Updated progressively)  
**Purpose:** Single source of truth for ALL Villa Thaifa work (past/present/future)

---

## DOCUMENT STRUCTURE

**This document contains:**

1. **Executive Status** - Current state snapshot
2. **Artifacts Inventory** - All documents created, their status, relationships
3. **Work Streams** - Parallel tracks of work in progress
4. **Critical Issues** - Blockers requiring immediate action
5. **Coordination Protocol** - How Lux + Claude Code + agents work together
6. **Next Actions** - What happens next (prioritized queue)
7. **Decision Log** - All decisions made (with rationale)
8. **Communication Log** - Key exchanges (Omar, Said, Najib, Support teams)

---

## SECTION 1: EXECUTIVE STATUS

**Last Updated:** 2025-01-09 14:30 UTC

### 🎯 Mission

**Primary Goal:** Generate bookings for Villa Thaifa THIS WEEK (restore Said's trust)

**Secondary Goal:** Build LHCM-OS platform (scale to other Moroccan properties)

---

#### LHCM-OS Vision (Strategic Context)

**Product Name:** LHCM-OS (Luxury Hospitality Cognitive Management - Operating System)  
**Code Name:** "The Digital C-Suite" (Le Comité Exécutif Numérique)  
**Origin:** Born from Marrakech friendship/family, not Silicon Valley  
**Status:** Vision documented in A08, awaiting Omar's 5 decisions to proceed

**Core Concept:**
Hybrid governance structure giving small properties (maisons d'hôtes) the managerial firepower of large hotel groups. CEO/Chairman (Said) gives strategic directives to AI C-Suite (General Manager, CFO, Revenue Manager, CTO), which coordinate human staff and tech infrastructure.

**The Architects:**
- **L'Âme (Métier):** Najib Mountassir (40 years hospitality, La Mamounia standards)
- **Le Cerveau (Tech):** Omar Mountassir (Agentic Engineering)
- **Le Pilote (Chairman):** Said Thaifa (Beta client, Villa Thaifa proof of concept)

**Three Pillars:**
1. **Governance by Objective:** Said assigns objectives ("prioritize occupancy this month"), AI Directors execute automatically (pricing, distribution, operations)
2. **Integrated Expertise:** Agents have "downloaded" Najib's 40 years. Act as guardrails: "Mr. President, this expense risks degrading GOP by 2%. Confirm?"
3. **The Boardroom:** Visual dashboard + chat/voice command channel for directives to digital team

**Golden Path Scenario:**
Said on terrace at 9am with mint tea, phone vibrates with AI GM brief ("3 VIP arrivals, rooms ready, car ordered"). Taps to approve 15% rate increase for strong demand month. Sleeps while system handles 23h booking in English/German with Palace-level politeness.

**Execution Sequence (Still to be decided by Omar - Q2 in A08):**
- **Option A:** Prove concept first (OTAs → Bookings → Build app) - Lux recommendation
- **Option B:** Build app first (App with MCP → OTAs via app)
- **Option C:** Parallel tracks (OTAs + App simultaneously)

**Status:** Said "emballé" (excited) but asked "Combien ça coûtera?" = NOT yet sold. Must PROVE with Villa Thaifa first.

**Full details:** See `/mnt/user-data/outputs/lhcm-os-strategy-execution-plan-v0.1.0.md` (29K words)

---

### 📊 Current State

| Metric | Status | Details |
|--------|--------|---------|
| **Said's Trust** | 🟡 FRAGILE | Waiting 2-3 weeks, asking "how much will it cost?" |
| **OTAs Active** | 🔴 1/10 | Only Booking.com exists (sync issues) |
| **HotelRunner Sync** | 🟡 UNCLEAR | Support says "fixed" but setting unchanged, needs verification |
| **Data Readiness** | 🟢 GOOD | Repomix digest complete, 12 rooms documented, pricing baseline exists |
| **Agent Readiness** | 🟢 READY | Browser agent proven, can access HotelRunner + Chrome |
| **App Development** | 🔴 NOT STARTED | LHCM-OS vision documented but no code yet |

### 🚨 Critical Blockers (P0)

**BLOCKER #1: HotelRunner Sync Mystery** (THIS DOCUMENT SECTION 4)
- **Issue:** Contradiction between diagnosis and Support Team advice
- **Impact:** Risk of double bookings if we proceed without understanding
- **Status:** ⏳ INVESTIGATION ASSIGNED TO CLAUDE CODE
- **ETA:** Today (2025-01-09)

**BLOCKER #2: Omar's Context Fragmentation**
- **Issue:** Work dispersed across: Lux chat, Gemini chat, Villa Thaifa repo, artifacts
- **Impact:** Hard to track what's done/in-progress/todo, risk of duplication
- **Status:** ⏳ THIS DOCUMENT AIMS TO SOLVE IT
- **ETA:** Continuous (living document)

### 🎯 Today's Priorities (2025-01-09)

1. **[P0]** Claude Code investigates HotelRunner sync (Section 4 = prompt + mission)
2. **[P0]** Lux creates centralized workstream (this document)
3. **[P1]** Align all artifacts (Section 2 = inventory + sync plan)
4. **[P1]** Prepare OTA activation master data (4-5 OTAs, not 10-15)
5. **[P2]** Answer 5 decision questions from LHCM-OS Strategy doc (Omar's input needed)

### ⏱️ Timeline

**Today (2025-01-09):**
- Morning: Repomix digest received, LHCM-OS vision captured ✅
- Afternoon: Workstream created, HotelRunner investigation launched
- Evening: Investigation report received, decisions made

**Tomorrow (2025-01-10):**
- OTA activation begins (4-5 platforms via browser agent)
- Master data package prepared
- Credentials ready for agent execution

**This Week (2025-01-09 to 2025-01-15):**
- 4-5 OTAs active and visible
- At least 1 booking received
- Said sees activity → Trust restored

---

## SECTION 2: ARTIFACTS INVENTORY

**Purpose:** Track ALL documents created, avoid duplication, ensure alignment

### 2.1 Briefs (Strategic Documents)

| Artifact | Version | Status | Location | Last Updated | Next Action |
|----------|---------|--------|----------|--------------|-------------|
| **Client Brief** | v0.2.0 | 🟡 NEEDS UPDATE | `/mnt/user-data/outputs/villa-thaifa-client-brief-v0.2.0.md` | 2025-01-09 | Update to v0.3.0 (add LHCM-OS vision + repomix findings) |
| **Project Brief** | v0.2.0 | 🟡 NEEDS UPDATE | `/mnt/user-data/outputs/villa-thaifa-project-brief-v0.2.0.md` | 2025-01-09 | Update to v0.3.0 (fill [REPO], [APP] placeholders) |

**Relationship:**
- Client Brief = Business context (Said, Najib, objectives, constraints)
- Project Brief = Execution plan (Phase 1 mission, checklists, workflows)

**Dependencies:**
- Both need input from LHCM-OS Strategy doc (Section 2.3 below)
- Both need input from Repomix Digest (Section 2.4 below)

**Sync Plan:**
- Once Omar answers 5 decision questions (LHCM-OS Strategy, Section 4)
- Lux updates both briefs to v0.3.0
- Timeline: Today or tomorrow (waiting on Omar's decisions)

---

### 2.2 Gemini Integration Package (Completed)

| Artifact | Status | Location | Purpose |
|----------|--------|----------|---------|
| **Gemini System Prompt** | ✅ COMPLETE | `/mnt/user-data/outputs/gemini-system-prompt.md` | Google AI Studio system instructions |
| **Gemini Onboarding** | ✅ COMPLETE | `/mnt/user-data/outputs/gemini-onboarding-prompt.md` | Context briefing (Lux↔Omar dynamic) |
| **Gemini Action Plan** | ✅ COMPLETE | `/mnt/user-data/outputs/gemini-lux-action-plan.md` | Orchestration guide (how to use Gemini) |
| **Google AI Studio Guide** | ✅ COMPLETE | `/mnt/user-data/outputs/google-ai-studio-quick-guide.md` | Step-by-step manual |
| **Transcript Copy** | ✅ COMPLETE | `/mnt/user-data/outputs/2026-01-09-10-44-55-villa-thaifa-najib-insights-brief-strategy.txt` | Full conversation history for Gemini |

**Status:** Package delivered to Omar, Gemini processing completed, digest received ✅

**No further action needed** on these artifacts (mission accomplished).

---

### 2.3 LHCM-OS Strategy & Execution Plan

| Artifact | Version | Status | Location | Last Updated |
|----------|---------|--------|----------|--------------|
| **LHCM-OS Strategy** | v0.1.0-alpha.0 | ⏳ AWAITING OMAR DECISIONS | `/mnt/user-data/outputs/lhcm-os-strategy-execution-plan-v0.1.0.md` | 2025-01-09 14:00 |

**Purpose:** Captures Omar's complete vision (Digital C-Suite), Lux's challenges, execution roadmap (Phase 0→1→2→3)

**Critical Dependency:** 5 decision questions (Section 4 of that document) block execution

**Questions Awaiting Omar's Answers:**
1. Q1: Timeline validation (accept "2-3 days" or maintain "hours"?)
2. Q2: Execution sequence (OTAs first, App first, or Parallel?)
3. Q3: Said's buy-in status (committed or not?)
4. Q4: Najib's involvement (aware, agreed, participating?)
5. Q5: Phase 0 OTA scope (4-5 OTAs or 10-15?)

**Next Action:** Omar reads document, answers questions → Unblocks Brief updates

---

### 2.4 Repomix Digest (Data Extract)

| Artifact | Status | Source | Received |
|----------|--------|--------|----------|
| **Repomix Digest** | ✅ COMPLETE | Gemini 3 Pro (processed 180k tokens) | 2025-01-09 |

**Key Findings:**
- 12 Physical Rooms (confirmed)
- 8 Room Types (HotelRunner mapping)
- Pricing baseline exists
- HotelRunner connected (Two-Way XML)
- **Sync Issue:** "Allocation Type = No changes" (see Section 4 for NEW INFO)
- Room 12 photos missing
- Data structure clean (SSOT in `data/specs/`)

**Integration Status:**
- Findings captured in LHCM-OS Strategy doc (Section 5)
- **Not yet integrated** into Briefs v0.3.0 (waiting on Omar's decisions)

---

### 2.5 Repository State (Villa Thaifa)

| Location | Status | Last Sync | Issues |
|----------|--------|-----------|--------|
| Villa Thaifa Repo | 🟡 OUT OF SYNC | Unknown | Not updated with recent work (Gemini package, LHCM-OS vision, this workstream) |

**Known Structure (from Repomix):**
```
villa-thaifa/
├── .claude/agents/          # Browser agent, pricing agent, etc.
├── data/specs/              # SSOT (rooms, pricing, property)
├── docs/workflows/          # Operational procedures
├── missions/                # Task management
└── src/                     # Empty (app not built yet)
```

---

#### COMPLETE PROPERTY DATA (Migrated from Repomix Digest)

**Property Overview:**
- **Name:** Villa Thaifa
- **Type:** Luxury Guest House (Maison d'hôtes)
- **Rating:** 4★
- **Location:** Marrakech, Morocco
- **Owner:** Said Thaifa
- **Channel Manager:** HotelRunner (subdomain: villa-thaifa.hotelrunner.com)
- **Booking.com Hotel ID:** 5446847
- **HotelRunner Channel ID:** 401071

**Physical Configuration:**
- **Total Physical Rooms:** 12 (Rooms numbered 1-12)
- **Room Types (HotelRunner):** 8 types mapped
- **Total Units:** 16 (some room types have multiple units)

**Room Inventory (Complete):**

| Physical Room | Room Type | Units | Occupancy | Pricing Baseline | Status |
|---------------|-----------|-------|-----------|------------------|--------|
| Room 1 | Chambre Double Supérieure | 2 | 2 guests | Base rate | ✅ Ready |
| Room 2 | Chambre Double Supérieure | (part of type) | 2 guests | Base rate | ✅ Ready |
| Room 3 | Chambre Double Standard | 2 | 2 guests | Standard rate | ✅ Ready |
| Room 4 | Chambre Double Standard | (part of type) | 2 guests | Standard rate | ✅ Ready |
| Room 5 | Chambre Triple | 2 | 3 guests | Triple rate | ✅ Ready |
| Room 6 | Chambre Triple | (part of type) | 3 guests | Triple rate | ✅ Ready |
| Room 7 | Chambre Quadruple | 2 | 4 guests | Quad rate | ✅ Ready |
| Room 8 | Chambre Quadruple | (part of type) | 4 guests | Quad rate | ✅ Ready |
| Room 9 | Chambre Familiale | 2 | 5 guests | Family rate | ✅ Ready |
| Room 10 | Chambre Familiale | (part of type) | 5 guests | Family rate | ✅ Ready |
| Room 11 | Suite Junior | 1 | 2 guests | Premium rate | ✅ Ready |
| Room 12 | Suite Présidentielle | 1 | 2 guests | Premium++ rate | 🟡 Photos missing |

**8 Room Types in HotelRunner:**
1. Chambre Double Supérieure (2 units)
2. Chambre Double Standard (2 units)
3. Chambre Triple (2 units)
4. Chambre Quadruple (2 units)
5. Chambre Familiale (2 units)
6. Suite Junior (1 unit)
7. Suite Présidentielle (1 unit)
8. [8th type TBD - verify in HotelRunner]

**Amenities & Services:**
- Swimming pool (outdoor)
- Garden/terrace
- Traditional Moroccan architecture
- On-site staff (cooks, cleaners, gardeners)
- VIP service protocols (Najib's La Mamounia standards)

**House Rules:**
- Check-in: [TBD - verify in property specs]
- Check-out: [TBD - verify in property specs]
- Cancellation policies: [TBD - verify in HotelRunner]

**Photos Status:**
- Rooms 1-11: ✅ Photos exist (available on Booking.com)
- Room 12 (Suite Présidentielle): 🟡 Photos missing (need to scrape from Booking.com or contact Ikram)

**HotelRunner Integration:**
- Connection Type: Two-Way XML
- Booking.com: Active (3,588 transactions logged)
- Mapping: 8 room types correctly mapped
- Sync Issue: Internal reservations not pushing to Booking.com (INVESTIGATION ONGOING - Section 4)
- Last Import: December 8, 2024 (noted in Repomix, 3 weeks ago)
- Allocation Type Setting: "No changes" (Support says leave as is, conflicting with diagnosis)

**Data Structure (SSOT Location):**
- Room specifications: `data/specs/rooms/`
- Pricing data: `data/specs/pricing/`
- Property details: `data/specs/property/`
- Platform configs: `data/specs/platform/hotelrunner/` and `data/specs/platform/booking/`

---

**Sync Plan:**
- After investigation (Section 4), update `docs/incidents/` with HotelRunner findings
- After OTA activation, update `data/specs/platform/` with new OTA configs
- After decisions made, create Phase 0 or Phase 1 execution artifacts in `missions/`

**Responsibility:** Claude Code should update repo as it works

**Data Quality:** ✅ HIGH (validated by Repomix digest, awaiting investigation validation of sync status)

---

### 2.6 Workstream Master (This Document)

| Artifact | Version | Status | Location | Purpose |
|----------|---------|--------|----------|---------|
| **Workstream Master** | v0.1.0-alpha.0 | 🟢 LIVING | `/mnt/user-data/outputs/villa-thaifa-workstream-master-v0.1.0.md` | Centralize ALL work |

**Update Protocol:**
- Lux updates this document progressively
- Every major action → Update relevant section
- Before auto-compact risk → Ensure document saved
- Omar can reference this as single source of truth

---

## SECTION 3: WORK STREAMS (Parallel Tracks)

### Stream 1: HotelRunner Sync Investigation (P0 - TODAY)

**Owner:** Claude Code + Browser Agent  
**Status:** ⏳ NOT STARTED (prompt being prepared in Section 4)  
**Goal:** Understand sync issue completely, provide actionable recommendations

**Tasks:**
1. Access HotelRunner admin (https://villa-thaifa.hotelrunner.com/admin)
2. Locate "Allocation Type" setting (currently "No changes")
3. Research what "Allocation Type" controls (HotelRunner docs, support KB)
4. Find "Auto-import" feature (Omar couldn't find it)
5. Verify current sync status (Booking.com connection)
6. Test: Create internal reservation → Check if Booking.com blocks date
7. Document findings in structured report
8. Provide clear recommendation (what to do, what NOT to do)

**Deliverable:** Investigation Report (format specified in Section 4)

**ETA:** Today (2025-01-09), 2-4 hours

---

### Stream 2: Artifacts Alignment (P1 - TODAY/TOMORROW)

**Owner:** Lux  
**Status:** ⏳ IN PROGRESS (this document is part of it)  
**Goal:** Ensure all documents consistent, no duplication, clear dependencies

**Tasks:**
1. ✅ Inventory all artifacts (Section 2 of this doc)
2. ⏳ Identify contradictions/gaps between documents
3. ⏳ Wait for Omar's 5 decisions (LHCM-OS Strategy)
4. ⏳ Update Client Brief v0.2.0 → v0.3.0
5. ⏳ Update Project Brief v0.2.0 → v0.3.0
6. ⏳ Sync with Villa Thaifa repo (Claude Code responsibility)

**Dependencies:**
- Stream 1 completion (need investigation findings)
- Omar's decisions (5 questions)

**ETA:** Tomorrow (2025-01-10)

---

### Stream 3: OTA Activation Preparation (P1 - TODAY/TOMORROW)

**Owner:** Lux + Claude Code  
**Status:** ⏳ NOT STARTED (blocked by Stream 1)  
**Goal:** Prepare everything needed for browser agent to activate 4-5 OTAs

**Tasks:**
1. ⏳ Create master data package (JSON/YAML export from `data/specs/`)
2. ⏳ Verify photos availability (Rooms 1-11 exist, Room 12 via Booking.com scrape)
3. ⏳ Define OTA priority list (4-5 platforms based on Omar's Q5 answer)
4. ⏳ Prepare credentials handoff protocol (Omar gives login info to agents)
5. ⏳ Create OTA activation checklist (per-platform workflow)
6. ⏳ Define verification protocol (how to confirm success)

**Blockers:**
- Stream 1 must complete first (understand sync before adding more OTAs)
- Omar must answer Q5 (how many OTAs? 4-5 vs 10-15)

**ETA:** Tomorrow (2025-01-10)

---

### Stream 4: LHCM-OS App (P2 - NEXT WEEK)

**Owner:** Lux + Claude Code + Gemini CLI  
**Status:** ⏳ NOT STARTED (blocked by Omar's Q2 decision)  
**Goal:** Build MVP or wait until OTAs proven

**Tasks:**
- Blocked until Omar answers Q2 (sequence: OTAs first vs App first vs Parallel)

**If "OTAs First" chosen:**
- Start app development Week 2 (after OTAs active)

**If "App First" chosen:**
- Start immediately (but Said waits longer for bookings)

**If "Parallel" chosen:**
- Coordinate tracks carefully (high context switching cost)

**ETA:** TBD (depends on Omar's decision)

---

### Stream 5: Site Web HotelRunner Mockup (P1 - PROCHAINS JOURS)

**Owner:** Claude Code + Gemini (design research) + Figma Advanced Tool Use  
**Status:** ⏳ NOT STARTED  
**Goal:** Fournir mockup + data à HotelRunner pour site web réservations directes

**Context:**
- HotelRunner peut créer site web front-end pour réservations directes
- Ils attendent: (1) Toutes les données, (2) Mockup design
- Alternative aux OTA (commissions 15-25% → 0% si réservation directe)

**Tasks:**

**Phase A: Competitive Research (2-3h)**
1. ⏳ Research meilleurs sites web maisons d'hôtes similaires
   - Marrakech luxury boutique properties
   - UI/UX patterns qui convertissent bien
   - Inspirations design (couleurs, layout, photos)
2. ⏳ Identifier best practices réservation directe
3. ⏳ Document findings (screenshots + analysis)

**Phase B: Mockup Creation (3-4h)**
1. ⏳ Créer mockup Figma (via Advanced Tool Use si possible, sinon MCP)
   - Homepage
   - Room listing page
   - Room detail page
   - Booking flow
   - Confirmation page
2. ⏳ Incorporate Villa Thaifa branding (colors, style)
3. ⏳ Export mockup (PNG + Figma share link)

**Phase C: Data Preparation (1-2h)**
1. ⏳ Compiler toutes données nécessaires:
   - Room descriptions (FR + EN)
   - Photos (11 rooms + 1 pending)
   - Pricing (seasonal rates)
   - Amenities & facilities
   - Location info, check-in/out policies
2. ⏳ Format pour HotelRunner team
3. ⏳ Send package à HotelRunner

**Technical Approach:**
- **Preferred:** Figma Advanced Tool Use (Code Execution pattern)
  - Reference: https://www.anthropic.com/engineering/advanced-tool-use
  - Avoids MCP context window bloat
- **Fallback:** Figma MCP si Advanced Tool Use pas disponible
- **Research agents:** Gemini CLI (web screenshots + analysis)
- **Mockup agent:** Claude Code (Figma integration)

**Dependencies:**
- Google Drive photos access (read-only, télécharger sur Omar's Drive)
- Room data finalized (12 chambres = 8 room types)
- Competitive research complete

**Deliverables:**
- [ ] Competitive analysis report (PDF avec screenshots)
- [ ] Figma mockup (5 pages minimum)
- [ ] Data package (JSON/YAML + photos ZIP)
- [ ] Email draft pour HotelRunner team

**Success Criteria:**
- ✅ Mockup approved by Omar
- ✅ HotelRunner team confirms they have everything needed
- ✅ Site web in production dans 2-3 semaines (HotelRunner timeline)

**ETA:** 2-3 jours (parallel avec Internal App development)

---

## SECTION 4: CRITICAL ISSUE — HOTELRUNNER SYNC INVESTIGATION

### 4.1 Problem Statement

**What We Thought We Knew (from Repomix Digest):**
- Internal reservations (created on HotelRunner, source "Online") don't push availability updates to Booking.com
- Root cause suspected: "Allocation Type" setting = "No changes"
- Omar asked HotelRunner Support, they told Said "problem fixed" (but didn't confirm to Omar)

**New Information (2025-01-09, Omar's conversation with Support):**

**Support Team told Omar:**
> "Allocation Type = No changes" **MUST stay as is**, otherwise inventory doesn't update.

**This contradicts our previous diagnosis.**

**Additional Mystery:**
- Omar looked for "Auto-import" feature on https://villa-thaifa.hotelrunner.com/admin
- **Could not find it** (but Repomix mentioned "last import Dec 8")

**Current Status:**
- Unclear if sync is actually fixed or not
- Don't understand what "Allocation Type" truly controls
- Don't know where "Auto-import" setting is located
- **Risk:** If we activate 4-5 more OTAs without understanding sync, we multiply double-booking risk

### 4.2 Previous Support Request (For Context)

**Omar's original message to HotelRunner Support:**

```
Objet: Problème sync réservations internes → Booking.com

Infos compte:
- Channel ID: 401071
- Hotel ID Booking: 5446847
- Subdomain: villa-thaifa.hotelrunner.com

---

Bonjour,

On a un souci de synchronisation avec notre connexion Booking.com.

Le problème : Quand on crée une réservation directement sur HotelRunner 
(source "Online"), les disponibilités ne se mettent pas à jour sur 
Booking.com. Résultat : risque de double-réservation.

Exemple concret :
On a une résa pour Sabah Gouram du 31 déc au 3 jan (Chambre Double 
Supérieure, conf. R599233355). Sur HotelRunner c'est bien enregistré, 
mais Booking.com affiche toujours 2 chambres dispo au lieu de 1.

Ce qu'on a vérifié :
- La connexion est active (XML non modifiable côté Booking)
- Le mapping des 8 types de chambres est OK
- Les logs montrent 3 588 transactions sans erreur
- Les résas venant DE Booking.com arrivent bien

Ce qu'on a trouvé de suspect :
- "Allocation Type" est sur "No changes" dans les paramètres avancés
- Le dernier import date du 8 décembre (3 semaines !)

Nos questions :
1. C'est quoi exactement "Allocation Type: No changes" ? On doit changer ça ?
2. Comment forcer une sync manuelle vers Booking ?
3. Pourquoi l'import auto ne tourne plus depuis 3 semaines ?

C'est urgent vu qu'on est en haute saison. Merci d'avance !

Cordialement,
Villa Thaifa
```

**Support Response (indirect, to Said):**
- Told Said problem is "fixed"
- Told Omar (directly) that "Allocation Type = No changes" should stay
- Did NOT answer the 3 specific questions above

### 4.3 Investigation Mission for Claude Code

**Primary Goal:** Understand HotelRunner sync completely → Provide clear, actionable recommendation

**Investigation Protocol:**

#### Phase A: Information Gathering (30-60 min)

**Task A1: Access HotelRunner Admin**
- Navigate to: https://villa-thaifa.hotelrunner.com/admin
- Log in with Omar's credentials (Omar will provide)
- Take screenshot of dashboard

**Task A2: Locate Settings**
- Find "Allocation Type" setting (reportedly in "advanced parameters")
- Document current value (should be "No changes")
- Find all sync-related settings (channel management, Booking.com connection)
- Locate "Auto-import" feature (if exists)
- Take screenshots of all relevant settings pages

**Task A3: Check Booking.com Connection**
- Navigate to channel management / integrations
- Verify Booking.com connection status
- Check connection type (should be "Two-Way XML")
- Look for last sync timestamp
- Check for any error messages or warnings

**Task A4: Review Documentation**
- Search HotelRunner Knowledge Base for "Allocation Type"
- Search for "inventory sync" or "availability sync"
- Search for "Auto-import"
- Download/capture relevant documentation

**Task A5: Check Reservations**
- Look at recent reservations in HotelRunner
- Note which ones came from Booking.com (source should indicate)
- Note which ones are internal (source "Online")
- Check if any recent internal reservations exist (post Dec 8)

#### Phase B: Testing (If Safe - Omar's Approval Required)

**CAUTION:** Only proceed with Phase B if Omar explicitly approves testing.

**Test 1: Check Current Sync State**
- Compare HotelRunner availability calendar with Booking.com calendar
- Document any discrepancies (dates, room types)

**Test 2: Create Test Internal Reservation** (ONLY if Omar approves)
- Create internal reservation for far-future date (e.g., March 2025)
- Use room type with multiple units (minimize risk)
- Wait 15-30 minutes
- Check if Booking.com calendar updates
- **If no update:** Document (confirms problem persists)
- **If updates:** Document (suggests problem fixed)
- **IMPORTANT:** Cancel test reservation immediately after

#### Phase C: Research & Analysis (30-60 min)

**Task C1: HotelRunner Documentation Research**
- Use web search: "HotelRunner Allocation Type meaning"
- Use web search: "HotelRunner inventory sync Booking.com"
- Use web search: "HotelRunner auto-import feature"
- Capture relevant findings

**Task C2: Channel Manager Best Practices**
- Research how channel managers typically handle inventory sync
- Understand "push" vs "pull" inventory models
- Understand common settings: "No changes", "Always update", etc.

**Task C3: Booking.com Side Research**
- Check if Booking.com has settings affecting sync
- Look for "XML settings" or "channel manager settings" in Booking extranet
- Document any relevant findings

#### Phase D: Sub-Agent Consultation (Optional)

**If investigation reveals complex technical issues:**
- Spawn `deep-research-agent` (defined in `.claude/agents/`)
- Focus research on: HotelRunner API behavior, XML sync protocols, inventory management
- Cross-reference findings from multiple sources

### 4.4 Investigation Report Template

**Claude Code MUST deliver report in this format:**

```markdown
# HOTELRUNNER SYNC INVESTIGATION REPORT
**Date:** 2025-01-09
**Investigator:** Claude Code + Browser Agent
**Duration:** [X hours]

---

## EXECUTIVE SUMMARY

[2-3 sentences: What's the issue, what did we find, what should we do]

---

## FINDINGS

### F1: Allocation Type Setting

**Current Value:** [screenshot + text description]
**Location in UI:** [exact navigation path]
**What it Controls:** [based on documentation/testing]
**Support Team Advice:** "Leave as 'No changes' or inventory won't update"

**Lux's Analysis:** [Does this make sense? Any contradictions?]

### F2: Auto-Import Feature

**Found:** [YES/NO]
**Location:** [if found, where exactly]
**Last Run:** [timestamp if visible]
**Status:** [active/inactive/not found]

**If NOT found:** [List where we looked, suggest alternatives]

### F3: Current Sync Status

**Booking.com Connection:**
- Type: [Two-Way XML / other]
- Status: [Active / Warning / Error]
- Last Sync: [timestamp if available]

**Test Results:** [if testing was approved and performed]
- Test reservation created: [details]
- Booking.com updated: [YES/NO/PARTIAL]
- Time to sync: [if applicable]

### F4: Documentation & Best Practices

**Key Findings from HotelRunner Docs:**
- [Point 1]
- [Point 2]
- [Point 3]

**Key Findings from Industry Research:**
- [Point 1]
- [Point 2]

---

## ROOT CAUSE ANALYSIS

**What's Actually Happening:**
[Explain the sync mechanism as best understood]

**Why Internal Reservations Might Not Sync:**
[Hypothesis based on findings]

**Confidence Level:** [HIGH/MEDIUM/LOW]

---

## RECOMMENDATIONS

### Recommendation 1: [Action Name]

**What:** [Specific action to take]
**Why:** [Rationale based on findings]
**Risk:** [LOW/MEDIUM/HIGH]
**How:** [Step-by-step if applicable]

### Recommendation 2: [Action Name]

**What:** [Specific action to take]
**Why:** [Rationale]
**Risk:** [LOW/MEDIUM/HIGH]
**How:** [Steps]

### Recommendation 3: [Fallback/Alternative]

[If primary recommendations don't work, what's Plan B?]

---

## UNANSWERED QUESTIONS

[List anything still unclear after investigation]

---

## NEXT STEPS

**Immediate (TODAY):**
1. [Action]
2. [Action]

**Before OTA Activation (TOMORROW):**
1. [Action]
2. [Action]

**Ongoing Monitoring:**
1. [Action]
2. [Action]

---

## APPENDIX

### A. Screenshots
[All relevant screenshots numbered and referenced]

### B. Documentation Links
[All sources consulted]

### C. Timeline
[Investigation activities log]

---

**Investigator Sign-off:** Claude Code
**Review Required:** Lux + Omar
```

### 4.5 Success Criteria for Investigation

**Investigation is COMPLETE when:**

✅ We understand what "Allocation Type: No changes" actually controls  
✅ We know where "Auto-import" feature is (or confirmed it doesn't exist in UI)  
✅ We understand WHY Support said "leave it as is"  
✅ We have clear recommendation: What to do before activating more OTAs  
✅ We have contingency plan if sync still broken  
✅ Omar + Lux review report and approve recommendations

**Investigation is SUCCESSFUL when:**

✅ All success criteria above met  
✅ Confidence level = HIGH or MEDIUM (not LOW)  
✅ Recommendation is actionable (not "we need more info")  
✅ Risk is quantified (we know what could go wrong)

### 4.6 Omar's Role in Investigation

**What Omar Needs to Provide:**

1. **Credentials Access:**
   - HotelRunner admin login (for browser agent)
   - Booking.com extranet login (if needed for cross-check)

2. **Testing Approval:**
   - Explicit YES/NO for Phase B (test reservation creation)
   - If YES, which room type to use (prefer multi-unit to minimize risk)

3. **Review & Decision:**
   - Read investigation report when delivered
   - Approve or challenge recommendations
   - Make final call on next steps

**What Omar Should NOT Do:**

- Don't touch HotelRunner settings while investigation ongoing
- Don't create manual reservations during testing window
- Don't contact Support again until we have complete picture (avoid confusion)

### 4.7 Integration with Other Work Streams

**Blocking Relationship:**

- Stream 3 (OTA Activation Preparation) is BLOCKED until this investigation completes
- We CANNOT safely activate 4-5 more OTAs without understanding sync

**Non-Blocking:**

- Stream 2 (Artifacts Alignment) can proceed in parallel
- Stream 4 (LHCM-OS App) unrelated (can proceed if Omar chooses "App First")

**Timeline Impact:**

- If investigation takes 2-4 hours (today) → OTA activation can start tomorrow
- If investigation reveals complex issues → May need extra day to fix before OTA activation

---

## SECTION 5: COORDINATION PROTOCOL

### 5.1 Lux ↔ Claude Code Communication

**How They Work Together:**

**Lux's Role:**
- Strategic thinking (what needs investigation, what's priority)
- Document creation (prompts, plans, reports)
- Context preservation (maintain this workstream)
- Review & challenge (validate Claude Code's findings)

**Claude Code's Role:**
- Execution (browser automation, file operations, code generation)
- Investigation (deep dive into HotelRunner, documentation research)
- Sub-agent orchestration (spawn specialists as needed)
- Technical report writing (structured findings)

**Handoff Protocol:**

1. **Lux → Claude Code:**
   - Creates detailed prompt (Section 4.3 = investigation mission)
   - Defines deliverable format (Section 4.4 = report template)
   - Specifies success criteria (Section 4.5)
   - Omar delivers prompt to Claude Code in terminal

2. **Claude Code → Lux:**
   - Completes mission
   - Delivers report in specified format
   - Omar copies report back to Lux's conversation
   - Lux reviews, integrates into workstream

3. **Iteration (if needed):**
   - Lux identifies gaps in report
   - Creates follow-up prompt for Claude Code
   - Repeat until success criteria met

### 5.2 Multi-Agent Coordination (Within Claude Code)

**Claude Code can spawn sub-agents from `.claude/agents/`:**

**For HotelRunner Investigation:**
- `browser-agent`: Core investigator (navigate HotelRunner UI, take screenshots)
- `deep-research-agent`: If complex technical questions arise (HotelRunner API, XML protocols)
- `incident-reporter`: Document investigation as incident report (if issues found)

**For OTA Activation (later):**
- `browser-agent`: Create accounts on each platform
- `platform-validator`: Verify each platform correctly configured before going live
- `incident-reporter`: Log any failures or unexpected behaviors

**Coordination Rules:**
- Parent agent (Claude Code) maintains master plan
- Sub-agents report findings to parent
- Parent synthesizes sub-agent reports into unified deliverable
- No sub-agent acts independently (always follows parent's instructions)

### 5.3 Omar's Interaction Model

**With Lux (This Chat):**
- Strategic discussions
- Decision-making (answer 5 questions from LHCM-OS Strategy)
- Review of synthesized reports
- Direction-setting ("do this, not that")

**With Claude Code (Terminal):**
- Deliver prompts created by Lux
- Provide credentials when needed
- Approve risky actions (e.g., test reservations)
- Receive and copy back reports

**With Gemini (Google AI Studio):**
- For large context processing (repomix digest) ✅ DONE
- For future needs if Claude's context fills up
- Not needed for day-to-day execution

**Omar Should NOT:**
- Juggle 3 conversations simultaneously without clear handoffs
- Create duplicate work (Lux already created plan, don't recreate in Claude Code)
- Lose track of what's where (this workstream centralizes everything)

---

## SECTION 6: NEXT ACTIONS (Prioritized Queue)

### 🔴 P0 - CRITICAL (Must complete TODAY)

**ACTION P0-1: Omar Delivers Investigation Prompt to Claude Code**
- **What:** Copy Section 4.3 + 4.4 (investigation mission + report template) to Claude Code
- **Why:** Unblocks Stream 1, critical for understanding sync before OTA activation
- **Who:** Omar (handoff Lux → Claude Code)
- **When:** NOW (as soon as Omar reads this)
- **Duration:** 5 minutes (just copy/paste)

**ACTION P0-2: Omar Provides HotelRunner Credentials**
- **What:** Give browser agent access to HotelRunner admin
- **Why:** Can't investigate without access
- **Who:** Omar
- **When:** Immediately after P0-1
- **Duration:** 2 minutes

**ACTION P0-3: Claude Code Executes Investigation**
- **What:** Complete investigation (Phase A minimum, Phase B if approved)
- **Why:** Get facts, not speculation
- **Who:** Claude Code + Browser Agent
- **When:** After receiving credentials
- **Duration:** 2-4 hours
- **Deliverable:** Investigation Report (Section 4.4 format)

**ACTION P0-4: Omar Returns Report to Lux**
- **What:** Copy Claude Code's report into Lux's conversation
- **Why:** Lux needs to review and integrate findings
- **Who:** Omar
- **When:** After Claude Code completes investigation
- **Duration:** 2 minutes

**ACTION P0-5: Lux Reviews & Updates Workstream**
- **What:** Integrate investigation findings, update recommendations
- **Why:** Maintain single source of truth
- **Who:** Lux
- **When:** After receiving report
- **Duration:** 30 minutes

---

### 🟡 P1 - HIGH (Should complete TODAY if possible)

**ACTION P1-1: Omar Answers 5 Decision Questions**
- **What:** Read LHCM-OS Strategy doc (Section 4), answer Q1-Q5
- **Why:** Unblocks Brief updates, defines execution sequence
- **Who:** Omar
- **When:** After investigation report reviewed (or in parallel if time permits)
- **Duration:** 30-45 minutes (read doc + think + decide)

**ACTION P1-2: Lux Updates Client Brief v0.3.0**
- **What:** Integrate LHCM-OS vision + repomix findings + investigation results
- **Why:** Keep strategic document current
- **Who:** Lux
- **When:** After Omar's decisions + investigation findings
- **Duration:** 30 minutes
- **Blocked by:** P0-5 (investigation) + P1-1 (Omar's decisions)

**ACTION P1-3: Lux Updates Project Brief v0.3.0**
- **What:** Fill [REPO], [APP] placeholders, update Phase 1 mission based on decisions
- **Why:** Execution plan must reflect current reality
- **Who:** Lux
- **When:** After Client Brief v0.3.0 updated
- **Duration:** 30 minutes
- **Blocked by:** P1-2

---

### 🟢 P2 - MEDIUM (Can wait until TOMORROW)

**ACTION P2-1: Create OTA Activation Master Data Package**
- **What:** Export `data/specs/` to JSON/YAML, validate completeness
- **Why:** Agents need structured data to create OTA accounts
- **Who:** Lux (design structure) + Claude Code (execute export)
- **When:** Tomorrow morning (after investigation complete)
- **Duration:** 1-2 hours
- **Blocked by:** P0-5 (need to know if sync works first)

**ACTION P2-2: Scrape Room 12 Photos from Booking.com**
- **What:** Browser agent downloads Presidential Suite photos
- **Why:** Complete photo inventory before OTA activation
- **Who:** Claude Code + Browser Agent
- **When:** Tomorrow (parallel with P2-1)
- **Duration:** 30 minutes
- **Blocked by:** None (can do anytime)

**ACTION P2-3: Create Per-OTA Activation Checklists**
- **What:** Detailed workflow for each platform (Airbnb, Expedia, VRBO, Agoda)
- **Why:** Agent execution protocol
- **Who:** Lux (based on platform research)
- **When:** Tomorrow afternoon
- **Duration:** 2-3 hours (research + documentation)
- **Blocked by:** P1-1 (need Omar's decision on how many OTAs)

---

### ⚪ P3 - LOW (This week, not urgent)

**ACTION P3-1: Sync Workstream with Villa Thaifa Repo**
- **What:** Copy/update relevant documents in repo
- **Why:** Repo should reflect current state
- **Who:** Claude Code
- **When:** End of week
- **Duration:** 1 hour

**ACTION P3-2: Create Phase 0 Execution Tracker**
- **What:** Spreadsheet or dashboard tracking OTA activation progress
- **Why:** Visual status for Omar + Said
- **Who:** Lux
- **When:** When OTA activation starts
- **Duration:** 1 hour

---

## SECTION 7: DECISION LOG

**All decisions made, with rationale and date.**

### 7.1 Core Workstream Decisions

| ID | Decision | Date | Made By | Rationale | Status |
|----|----------|------|---------|-----------|--------|
| D-W-001 | Create Workstream Master document | 2025-01-09 14:30 | Omar + Lux | Centralize work, prevent loss due to auto-compact, track everything | ✅ DONE |
| D-W-002 | Prioritize HotelRunner sync investigation | 2025-01-09 14:00 | Omar + Lux | Can't safely activate more OTAs without understanding sync | ✅ DONE |
| D-W-003 | Use structured investigation report template | 2025-01-09 14:15 | Lux | Ensure Claude Code delivers actionable findings | ✅ DONE |
| D-W-004 | Block OTA activation until investigation complete | 2025-01-09 14:00 | Lux | Risk mitigation (avoid double bookings) | ✅ DONE |

---

### 7.2 LHCM-OS Strategic Decisions (2025-01-09 16:00)

**Context:** Omar answered 5 critical questions from LHCM-OS Strategy (A08 Section 4)

#### D-W-005: Timeline Approach - "HOURS NOT DAYS" ⚡

**Question:** Q1 - Accept "2-3 days" estimate vs maintain "hours" ambition?

**Decision:** **MAINTAIN "HOURS" AMBITION**

**Rationale:**
- Omar challenges Lux's conservative estimates
- Questions "4-5 days prep" when "nothing concrete yet, just markdown"
- Believes 2026 agentic systems (Claude Code + Vibe Kanban) faster than estimated
- Demands web research to validate true 2026 capabilities

**Omar's Words:** *"Pourquoi tu parle de 4-5 jours de prep alors que pour l'instant on a rien de concrêt et que c'est que sur 'papier'/markdown??"*

**Status:** ✅ DECIDED (but needs validation research)

**Impact:**
- More aggressive timeline than Lux proposed
- Lux must research actual 2026 agentic system speeds
- May be realistic with proper orchestration (Vibe Kanban)

---

#### D-W-006: Execution Sequence - PHASED APPROACH 🔀

**Question:** Q2 - OTAs first (A), App first (B), or Parallel (C)?

**Decision:** **PHASED: OTAs NOW → INTERNAL APP → LHCM-OS PLATFORM (2-3 months)**

**Clarification (Critical):**
- **Phase 0 (Ce soir):** OTA Activation ONLY (3-4 OTAs)
  - Focus 100% activation OTAs
  - No app development tonight
- **Phase 1 (Prochains jours):** Internal App for Villa Thaifa
  - Knowledge base centralisée (tous docs accessibles)
  - Dashboard pour Omar (voir status OTAs, réservations)
  - Agent interface (Claude Code, Gemini accèdent aux docs)
  - **Google Drive access via Code Execution** (Advanced Tool Use, NOT MCP)
    - Reference: https://www.anthropic.com/engineering/advanced-tool-use
  - **Goal:** Developer-ready & agent-ready (NOT production-ready yet)
  - **Designed for reuse:** Foundation for LHCM-OS later
- **Phase 2 (2-3 mois):** LHCM-OS MVP/MLP
  - Produit commercial pour autres clients
  - Said = pilot (on a le temps de bien faire)
  - Architecture scalable, production-ready
  - Multi-tenant, white-label capable

**Rationale:**
- Client needs FIRST (OTAs = immediate value pour Said)
- Internal app = enables agents to work effectively
  - Problem: Files dispersed, limited context window
  - Solution: Centralized knowledge base agents can access
- LHCM-OS platform = long-term product (not urgent, 2-3 mois)
- Multiple Claude Code instances via **Vibe Kanban** when app development starts
- Codex CLI coming back soon (ChatGPT Business renewal)

**Timeline Estimation Challenge:**
- Omar + Lux both recognize difficulty estimating with 2025-2026 agentic tools
- *"J'ai vu des gens qui créer des apps en quelque heures"*
- **Need web research** to validate realistic timeline for internal app
- Focus: "Le plus vite on a un truc utilisable le mieux"
- Not about perfection, about agent-readiness

**Status:** ✅ DECIDED

**Impact:**
- Ce soir: 100% focus OTAs (no app development)
- Demain: Start internal app IF OTA activation successful
- Stream 4 (LHCM-OS Platform) deferred to 2-3 months (plenty of time)
- Need orchestration layer = **Vibe Kanban** (when app development starts)

---

#### D-W-007: Said's Commitment - IMPLICIT/PARTIAL ⚠️

**Question:** Q3 - Is Said committed to LHCM-OS?

**Decision:** **YES, BUT IMPLICIT (contract needed)**

**Context:**
- Said's quote: *"Do as if Villa Thaifa is yours"* = HIGH TRUST
- Agreed to be pilot BUT needs formal contract
- Excited ("emballé") when pitched LHCM-OS
- Asked cost ("Combien ça coûtera?")
- **Omar's pricing strategy:** -90% discount for first client, progressive reduction

**Client Priority:** *"Yes, our client's needs first! Proof of Concept / MVP in parallel"*

**Not Production Ready:** *"All I need is to have everything about its business accessible properly by our agents... We got so many files all dispersed etc."*

**MoSCoW Focus:** MUST HAVES (+ some COULD HAVES)

**Status:** ⚠️ NEEDS FORMALIZATION (contract)

**Impact:**
- Can proceed with Villa Thaifa as pilot
- Need to draft service agreement
- Focus: Make Said's business accessible to agents (not full production system)

---

#### D-W-008: Najib's Role - YES + MARKET VALIDATION ✅

**Question:** Q4 - Is Najib involved? Market fit?

**Decision:** **YES - NAJIB AWARE, CLIENTS INTERESTED**

**Strategic Context:**

**Najib's Network:**
- His clients interested (example: 5-star hotel under construction)
- 40 years La Mamounia standards = reputation
- Distribution channel for LHCM-OS

**Omar's Positioning:**
- *"Je dois clairement être actuellement parmi le top 1%"*
- *"Je ne penses même pas que 5%-10% des gens dans mon domaines exploitent des systèmes agentique"*
- *"Je suis au top de la vague, c'est comme si j'étais au courant que le BitCoin / crypto monnaie aurait une avancée/montée fulgurante... bien avant que le grand public en prenne conscience!"*

**Market Gap:**
- HotelRunner (Channel Manager) never offered anything like this
- Claude Code launched Feb 2025 = very few in Morocco master it
- First-mover advantage in Morocco hospitality tech

**Proof of Concept:**
- Ikram (HotelRunner support) was *"bluffée"* seeing agent make reservations while Omar smoked outside

**Family Context:**
- Omar grew up in hotels (Najib's son)
- Deep domain understanding
- Najib's reputation = trust factor

**Status:** ✅ VALIDATED

**Impact:**
- Strong market positioning
- Najib's network = distribution channel
- High confidence in product-market fit (even without formal market research)

---

#### D-W-009: OTA Scope - ALL 135 IF AGENTS CAN 🚀

**Question:** Q5 - Start with 4-5 OTAs or 10-15?

**Decision:** **OPTION C - TARGET ALL 135 OTAs (if agents capable)**

**Official Priority List (Confirmed by HotelRunner Support Team):**

**Phase 0 (Ce Soir): Top 8 OTAs**
1. **Booking.com** ✅ (déjà connecté)
2. **Expedia** ✅ (en cours)
   - Hotels.com (via Expedia) - automatique avec Expedia
3. **Airbnb** (priorité haute)
4. **Trip.com** (marché Asie)
5. **Ostrovok** (marché Russie/CEI)
6. **Hotelbeds** (B2B wholesaler)
7. **Odigeo** (eDreams, Opodo, GoVoyages)
8. **DOTWd** (marché Asie-Pacifique)

**Phase 1: Scale to 15-20 OTAs**
- AgodaExpedia Group: TripAdvisor, Vrbo, Orbitz, Travelocity, Wotif, ebookers, CheapTickets, lastminute.com
- Others: Agoda, HRS, Ctrip (China)

**Long-term: All 135+ OTAs** (HotelRunner supported)

**Rationale:**
- HotelRunner supports **135+ OTAs** (!!)
- *"If our agents have all they need to create 3-4, they would take care of the 15 easily"*
- Manual work = waste of Omar's skills
- Omar's value proposition: *"C'est comme si on demandait à un architecte... à bas non, passe en mode plombier maintenant... (Foutage de gueule non)"*
- **Vision:** 50-100+ OTAs (court-terme), 135+ (long-terme)

**Tonight's Realistic Goal:**
- ✅ Booking.com verified (already connected)
- ✅ Expedia confirmed (+ Hotels.com auto)
- ⏳ Airbnb activation (create account + list)
- ⏳ Trip.com request (if time permits)
- **Minimum success:** 3 OTAs operational (Booking, Expedia, Airbnb)
- **Stretch success:** 4+ OTAs requested

**Status:** ✅ DECIDED

**Impact:**
- Massive time savings vs manual (135 OTAs manually = weeks/months)
- Leverage Omar's top 1% agentic systems skills
- Proof agents can scale = massive market value
- 8 OTAs = solid foundation, 135 OTAs = complete coverage

---

### 7.3 Technical Architecture Decisions

#### D-W-010: Code Execution MCP Pattern - YES ✅

**Question:** Switch from traditional MCP to Code Execution MCP?

**Decision:** **YES - CODE EXECUTION MCP**

**Omar's Challenge:** *"Pourquoi tu parle de 4-5 jours de prep alors que pour l'instant on a rien de concrêt?"*

**Clarification:** Not 4-5 days PREP, but better architecture long-term

**HotelRunner Integration:** *"Nos agents n'auront pas forcement d'avoir accès à HotelRunner en MCP (potentiellement en code execution ? à voir)"*

**Status:** ✅ DECIDED (implementation timeline TBD via research)

**Impact:**
- Changes architecture in A08 Section 3
- HotelRunner integration may NOT need MCP server (Code Execution wrapper instead)
- Scalable to 50-100+ tools without context degradation

---

#### D-W-011: Database Choice - TBD 🤷

**Question:** D1 (Cloudflare-native) vs PostgreSQL?

**Decision:** **CAN'T DECIDE - WHATEVER WORKS BEST**

**Omar's Words:** *"Franchement, je sais pas, on choisira ce qui nous arrange le plus. J'arrive pas à décidé.."*

**Status:** ⏸️ OPEN (choose when architecture concrete)

**Impact:** Doesn't block MVP start, decide during Phase 1

---

#### D-W-012: Auth Solution - RESEARCH ALTERNATIVES 🔍

**Question:** Clerk ($25/month) for MVP auth?

**Decision:** **MAYBE CLERK, BUT EXPLORE FREE ALTERNATIVES FIRST**

**Omar's Words:** *"Pourquoi pas.. mais si on peut avoir un truc gratuit tout aussi efficace je penses que cela pourrait être cool aussi."*

**Action:** Web research Auth0, others

**Status:** ⏸️ RESEARCH NEEDED

**Impact:** Not blocking, decide during Phase 1

---

#### D-W-013: HotelRunner Priority - TBD 🤔

**Question:** Phase 0 (OTA activation) vs Phase 1 (App development) priority?

**Decision:** **DON'T KNOW YET - NEED MORE THINKING**

**Context:** With parallel tracks (D-W-006), can do both

**Status:** ⏸️ OPEN

**Impact:** Affects resource allocation, but parallel = less critical

---

### 7.4 GAME CHANGER: Vibe Kanban 🎯

#### D-W-014: Orchestration Tool - VIBE KANBAN

**Decision:** **USE VIBE KANBAN FOR MULTI-AGENT ORCHESTRATION**

**What is Vibe Kanban:**
- Open-source "Mission Control" for AI Engineering (BloopAI)
- Transforms workflow: "Chatting with bot" → "Managing fleet of developers"
- **Kanban board interface:** To Do, In Progress, In Review, Done
- You write **tickets**, agents write code

**Why This Changes Everything:**

**Killer Feature: Parallel Orchestration**
- **Git Worktrees isolation:** Each task = separate worktree
- **Multi-agent swarm:** 
  - Claude Opus 4.5 refactors backend
  - WHILE Claude Sonnet 4.5 fixes CSS bug
  - WHILE Gemini writes documentation
  - ALL IN PARALLEL, same repo, NO conflicts

**Agent Support:**
- Claude Code (preferred) ✅
- Amp ✅
- Gemini CLI ✅
- OpenAI Codex ✅
- Cursor Agent CLI ✅

**Key Features:**
- **MCP Integration:** Built-in Model Context Protocol support
- **Visual Diffs:** Side-by-side code review
- **Feedback Loop:** Comment on PR, agent retries immediately
- **SSH Remote:** Run on cloud, access from laptop
- **"Sound of Productivity":** Hear agents working (compile success sounds)

**Quickstart:**
```bash
npx vibe-kanban
```

Auto-detects git repo, opens board at `localhost:3000`

**Configuration (`vibe.config.js`):**
```javascript
{
  setup_script: "npm run dev",
  test_command: "npm test",
  linter_check: true
}
```

**Best Practices:**
- **"Context Dump":** Load tickets with excessive context (errors, logs, files)
- **Small Tickets:** Tasks >20 steps degrade performance
- Break features: "Create DB Schema" → "Build API" → "Create UI"

**Status:** ✅ DECIDED (need to implement)

**Impact:**
- Enables D-W-006 (parallel tracks)
- One senior engineer (Omar) manages 5-10 AI juniors simultaneously
- **Critical for achieving "hours not days" timeline** (D-W-009)
- Solves 2025 "Context Ceiling" problem (humans = bottleneck)

**Industry Context (Jan 2026):**
- Models smart enough to do work
- Humans couldn't review fast enough
- Vibe Kanban = **Human-in-the-loop scaling solution**
- Current standard for AI Engineering

**Action Required:**
- Research Vibe Kanban docs deeper
- Prepare migration plan to local + Vibe Kanban
- Create tickets for tonight's work (3-4 OTAs)

---

#### D-W-015: Site Web HotelRunner - UTILISER LEUR SERVICE 🌐

**Question:** Construire notre propre site web front-end, ou utiliser HotelRunner?

**Decision:** **UTILISER SITE WEB HOTELRUNNER**

**Context:**
- HotelRunner peut créer site web pour réservations directes
- Alternative aux OTA (0% commission vs 15-25% OTA commission)
- Ils attendent: (1) Toutes les données + photos, (2) Mockup design

**Rationale:**
- **Plus simple:** Pas besoin construire front-end booking flow
- **Plus rapide:** HotelRunner team gère deployment + hosting
- **Focus agents:** On se concentre sur Internal App (back-end, dashboard, API)
- **Migration possible:** Si besoin custom site later, data déjà structurée

**Deliverables Required:**

**1. Mockup Figma:**
- Homepage
- Room listing page
- Room detail page
- Booking flow
- Confirmation page

**2. Data Package:**
- Room descriptions (FR + EN)
- Photos (12 chambres, 11 déjà disponibles)
- Pricing (seasonal rates)
- Amenities & facilities
- Policies (check-in/out, cancellation)

**Technical Approach:**
- **Competitive research:** Gemini CLI (analyze best boutique hotel sites)
- **Mockup creation:** Claude Code + Figma Advanced Tool Use (preferred over MCP)
- **Data compilation:** Extract from existing `data/specs/` + Google Drive

**Status:** ✅ DECIDED

**Impact:**
- Reduces Internal App scope (no guest-facing booking UI)
- New workstream: Stream 5 (Site Web Mockup) added to Section 3
- Timeline: 2-3 jours parallel avec Internal App
- HotelRunner timeline: 2-3 semaines production after receiving mockup

---

#### D-W-016: MCP Philosophy - "ÉVITER COMME LA PESTE" 🚫

**Principle:** **CODE EXECUTION (ADVANCED TOOL USE) > MCP**

**Omar's Directive:**
> "Il nous faut éviter les MCPs comme la peste! (donc juste si on a pas le choix / pas de meilleur alternative)"

**Rationale:**
- **Context Window = ULTRA PRÉCIEUX**
  - Claude Sonnet 4.5: 200K context window
  - MCP tools: 5-50K tokens per tool (10-25% context eaten)
  - Code Execution: <500 tokens per tool (0.25% context)
  - **98.7% reduction in context consumption**
- **Scalability:** 100+ tools possible with Code Execution, impossible with MCP
- **Performance:** Faster execution, less latency
- **Maintenance:** TypeScript wrappers easier to debug than MCP servers

**When MCP is Acceptable:**
- **ONLY if:** No Code Execution alternative exists
- **ONLY if:** External party maintains MCP server (e.g. Linear, Notion)
- **NEVER if:** We can build TypeScript wrapper ourselves

**Applications:**

**✅ CODE EXECUTION (Preferred):**
- HotelRunner API → TypeScript wrapper
- Google Drive → TypeScript wrapper (Advanced Tool Use pattern)
- Figma → Advanced Tool Use (if available)
- Custom business logic → Always Code Execution

**⚠️ MCP (Exception Only):**
- Figma MCP → Only if Advanced Tool Use not available
- Linear MCP → Maintained by Linear team (acceptable)
- Notion MCP → Maintained by Notion team (acceptable)

**Crystal Clear for Agents:**
- Default = Code Execution
- Ask "Can this be Code Execution?" BEFORE considering MCP
- Context window = agent's most precious resource
- Protect it aggressively

**Anthropic Engineering References (Complete Set):**

**Core Philosophy (⭐ Primary):**
1. **Advanced Tool Use** ⭐  
   https://www.anthropic.com/engineering/advanced-tool-use  
   **Why:** Introduces Tool Search Tool, Programmatic Tool Calling, Tool Use Examples. Shows 98.7% token reduction (150K→2K tokens). Core justification for Code Execution > MCP.

2. **Code Execution with MCP** ⭐  
   https://www.anthropic.com/engineering/code-execution-with-mcp  
   **Why:** Direct comparison MCP vs Code Execution. Progressive disclosure, context efficiency, privacy-preserving operations. Shows exactly WHY to avoid MCP.

3. **Effective Context Engineering for AI Agents** ⭐  
   https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents  
   **Why:** Context window = finite resource with diminishing returns. Attention scarcity, n² pairwise relationships. Justifies treating context as "ULTRA PRÉCIEUX".

**Implementation Patterns:**
4. **Claude Code Best Practices**  
   https://www.anthropic.com/engineering/claude-code-best-practices  
   **Why:** CLAUDE.md files, bash tools, custom slash commands. Shows HOW to use Code Execution effectively without MCP bloat.

5. **Claude Code Sandboxing**  
   https://www.anthropic.com/engineering/claude-code-sandboxing  
   **Why:** Filesystem + network isolation for Code Execution. Security WITHOUT MCP overhead. 84% fewer permission prompts.

6. **Equipping Agents with Agent Skills**  
   https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills  
   **Why:** Progressive disclosure via SKILL.md. Load context on-demand, NOT upfront. Alternative to MCP's "load everything" approach.

7. **Building Agents with Claude Agent SDK**  
   https://www.anthropic.com/engineering/building-agents-with-the-claude-agent-sdk  
   **Why:** Agent loop (gather context → action → verify). Shows how bash + Code Execution replaces MCP tools for most use cases.

8. **Engineering at Anthropic (Landing Page)**  
   https://www.anthropic.com/engineering  
   **Why:** Central hub for all engineering articles. Reference point for latest Anthropic best practices.

**Status:** ✅ LOCKED IN (Principle established, all 8 resources documented)

**Impact:**
- All future tool integrations follow this pattern
- Stream 5 (Figma) prioritizes Advanced Tool Use
- Internal App (Google Drive) uses Code Execution
- HotelRunner API uses TypeScript wrapper (Code Execution)

---

## SECTION 8: COMMUNICATION LOG

**Key exchanges with stakeholders.**

### 8.1 With HotelRunner Support

**2025-01-09 (Morning) - Omar's Request:**
- Sent detailed sync issue description (3 questions)
- Account info: Channel ID 401071, Hotel ID 5446847
- Specific example: Sabah Gouram reservation (R599233355)

**2025-01-09 (Afternoon) - Support Response:**
- **Indirect (to Said):** "Problem fixed"
- **Direct (to Omar):** "Allocation Type = No changes should stay as is, or inventory won't update"
- **Did NOT answer:** 3 specific questions about auto-import, manual sync, etc.

**Status:** Incomplete response, investigation still needed

---

### 8.2 With Said Thaifa

**2025-01-09 - Status:**
- Waiting 2-3 weeks for Villa Thaifa activation
- Received LHCM-OS pitch, reacted "emballé" (excited)
- Asked: "Combien ça coûtera?" (How much will it cost?)
- **Not yet committed** to either Villa Thaifa activation OR LHCM-OS platform

**Next Communication:** After first OTA activation success (show bookings)

---

### 8.3 With Najib Mountassir

**Previous Sessions:**
- Part 1: Insights on Said's challenges, prioritization advice
- Part 2: "Tu te fuis beaucoup" (avoid execution), "client first, not your priorities"
- Part 3: Timeline reality ("before end-of-year holidays"), operational advice

**Status:** Najib aware of Villa Thaifa situation, not yet briefed on LHCM-OS platform vision

**Next Communication:** After investigation complete + decisions made (validate approach)

---

### 8.4 With Lux (This Conversation)

**Session Start:** 2025-01-09 ~12:00  
**Major Milestones:**
- Repomix digest received ✅
- LHCM-OS vision captured ✅
- Lux challenged timeline + execution sequence ✅
- Omar emphasized urgency + context fragmentation ✅
- Workstream Master created ✅

**Current Status:** Awaiting Omar's decisions + Claude Code investigation

---

## SECTION 9: GLOSSARY & REFERENCES

### Key Terms

- **LHCM-OS:** Luxury Hospitality Cognitive Management - Operating System (Omar's platform vision)
- **Workstream:** This document (centralized command & control)
- **P0/P1/P2/P3:** Priority levels (Critical/High/Medium/Low)
- **Stream:** Parallel work track (e.g., Stream 1 = Investigation, Stream 2 = Alignment)
- **Artifact:** Document created (brief, prompt, report, etc.)
- **Auto-compact:** Claude's context window compression (risk of losing chat history)

### References

**Internal Documents:**
- LHCM-OS Strategy: `/mnt/user-data/outputs/lhcm-os-strategy-execution-plan-v0.1.0.md`
- Client Brief v0.2.0: `/mnt/user-data/outputs/villa-thaifa-client-brief-v0.2.0.md`
- Project Brief v0.2.0: `/mnt/user-data/outputs/villa-thaifa-project-brief-v0.2.0.md`

**External Resources:**
- HotelRunner Admin: https://villa-thaifa.hotelrunner.com/admin
- HotelRunner Support: (contact via Omar)
- Villa Thaifa Repo: (path TBD, needs sync)

---

## SECTION 10: DOCUMENT MAINTENANCE

### Update Protocol

**When to Update This Document:**
- After any major action completes (investigation, decision, execution)
- After new artifact created (add to Section 2 inventory)
- After decision made (add to Section 7 log)
- After communication with stakeholder (add to Section 8)
- Before context window risks auto-compact (preserve state)

**Who Updates:**
- Primary: Lux (maintains centralized view)
- Secondary: Claude Code (can append investigation findings)
- Omar: Can read anytime, can request updates

**Version Control:**
- Format: `vMAJOR.MINOR.PATCH-alpha.BUILD`
- Increment MINOR when: Major section added or restructured
- Increment PATCH when: Content updated within existing structure
- Increment BUILD when: Minor corrections or additions

**Current Version:** v0.1.0-alpha.0 (Initial creation)

---

## END OF WORKSTREAM MASTER

**This document is LIVING and will be updated progressively.**

**Next Update Expected:** After Claude Code completes investigation (today, 2025-01-09)

**Omar:** Deliver Section 4.3 + 4.4 to Claude Code NOW to start investigation.

**Lux:** Standing by to receive investigation report and update this workstream.

---

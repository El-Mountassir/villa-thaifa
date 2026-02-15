# Villa Thaifa - Migration Plan
## claude.ai → Nexus Workstation + Vibe Kanban

**Version:** 0.1.0-alpha.0  
**Date:** 2025-01-09 16:00  
**Author:** Lux  
**Objective:** Migrate 5h of planning work to Nexus + activate Vibe Kanban orchestration  
**Timeline:** 17h00-17h30 (30 minutes MAX)

---

## SECTION 1: CURRENT STATE (What We Have)

### 1.1 Artifacts in claude.ai

**Coordination Documents (3):**
```
/mnt/user-data/outputs/villa-thaifa-workstream-master-v0.1.0.md (1108 lines)
/mnt/user-data/outputs/villa-thaifa-artifact-inventory-v0.1.0.md
/mnt/user-data/outputs/villa-thaifa-investigation-brief-v0.1.0.md
```

**Strategic Documents (2):**
```
/mnt/user-data/outputs/lhcm-os-strategy-execution-plan-v0.1.0.md
/mnt/user-data/outputs/tech-stack-omar-v0.1.3-lux-annotated.md
```

**Client Documents (2):**
```
/mnt/user-data/outputs/villa-thaifa-client-brief-v0.2.0.md
/mnt/user-data/outputs/villa-thaifa-project-brief-v0.2.0.md
```

**TOTAL: 7 artifacts, ~3000 lines combined**

### 1.2 Key Information Captured

**Decisions Made:**
- D-W-001 to D-W-014 (14 strategic decisions)
- Parallel tracks execution (OTA + App)
- Vibe Kanban orchestration adopted
- Timeline: "hours not days" ambition
- OTA scope: 3-4 tonight, 135 long-term

**Context:**
- Said's trust ("Do as if Villa Thaifa is yours")
- Najib's network (5-star hotel clients)
- Market positioning (top 1% agentic systems in Morocco)
- HotelRunner sync investigation in progress

---

## SECTION 2: TARGET STATE (What We Want)

### 2.1 Nexus File Structure

```
~/villa-thaifa/
├── .vibe/                    # Vibe Kanban config
│   └── config.js
├── docs/
│   ├── coordination/
│   │   ├── workstream-master-v0.1.0.md
│   │   ├── artifact-inventory-v0.1.0.md
│   │   └── investigation-brief-v0.1.0.md
│   ├── strategy/
│   │   ├── lhcm-os-strategy-v0.1.0.md
│   │   └── tech-stack-v0.1.3.md
│   └── client/
│       ├── client-brief-v0.2.0.md
│       └── project-brief-v0.2.0.md
├── tickets/                  # Vibe Kanban ticket prompts
│   ├── T001-hotelrunner-investigation.md
│   ├── T002-ota-booking-com.md
│   ├── T003-ota-airbnb.md
│   ├── T004-ota-expedia.md
│   └── T005-ota-hotels-com.md
└── src/                      # Code (when app development starts)
    └── .gitkeep
```

### 2.2 Vibe Kanban Board State

**Columns:**
- **To Do:** 5 tickets ready
- **In Progress:** Empty (will fill when agents start)
- **In Review:** Empty
- **Done:** Empty

**Tonight's Tickets (Priority Order):**
1. **T001:** HotelRunner Sync Investigation (if not complete)
2. **T002:** Activate Booking.com OTA
3. **T003:** Activate Airbnb OTA
4. **T004:** Activate Expedia OTA
5. **T005:** Activate Hotels.com OTA (stretch goal)

---

## SECTION 3: MIGRATION PROTOCOL

### 3.1 Pre-Migration Checklist

**Omar Must Have Ready:**
- [ ] Nexus workstation powered on
- [ ] Terminal open (Warp preferred)
- [ ] Git configured (`git config --global user.name`, `user.email`)
- [ ] GitHub SSH key added (if pushing to remote)
- [ ] Node.js + Bun installed (check: `bun --version`)
- [ ] Claude Code CLI working (check: `claude --version`)

### 3.2 Migration Steps (17h00-17h15: 15 minutes)

**STEP 1: Create Project Structure (2 min)**
```bash
cd ~
mkdir -p villa-thaifa/{docs/{coordination,strategy,client},tickets,src}
cd villa-thaifa
git init
echo "# Villa Thaifa - OTA Activation Project" > README.md
```

**STEP 2: Download Artifacts from claude.ai (5 min)**

*Method A: Manual Copy-Paste (Faster)*
1. Open each artifact in claude.ai
2. Copy full content
3. Create file on Nexus: `nano docs/coordination/workstream-master-v0.1.0.md`
4. Paste content
5. Save (Ctrl+O, Enter, Ctrl+X)
6. Repeat for all 7 artifacts

*Method B: Use Claude Code to Fetch (Automated)*
```bash
# Omar creates prompt for Claude Code:
"Read all artifacts from this claude.ai conversation transcript:
/mnt/transcripts/2026-01-09-15-17-08-tech-stack-capture-lhcm-os-alignment.txt

Extract and save each artifact to correct location in ~/villa-thaifa/docs/

Follow this mapping:
- villa-thaifa-workstream-master-v0.1.0.md → docs/coordination/
- villa-thaifa-artifact-inventory-v0.1.0.md → docs/coordination/
- villa-thaifa-investigation-brief-v0.1.0.md → docs/coordination/
- lhcm-os-strategy-execution-plan-v0.1.0.md → docs/strategy/
- tech-stack-omar-v0.1.3-lux-annotated.md → docs/strategy/
- villa-thaifa-client-brief-v0.2.0.md → docs/client/
- villa-thaifa-project-brief-v0.2.0.md → docs/client/

Verify all files created successfully."
```

**STEP 3: Initialize Vibe Kanban (3 min)**
```bash
cd ~/villa-thaifa
npx vibe-kanban
# Browser opens at localhost:3000
# Vibe detects git repo
# Board is ready
```

**STEP 4: Create Ticket Files (5 min)**
```bash
# Copy ticket templates from next section
# Save each as tickets/T00X-*.md
# These will be copy-pasted into Vibe Kanban board
```

### 3.3 Post-Migration Validation (17h15-17h20: 5 min)

**Checklist:**
- [ ] All 7 docs in `~/villa-thaifa/docs/`
- [ ] Git repo initialized (`git status` works)
- [ ] Vibe Kanban running at `localhost:3000`
- [ ] 5 ticket files in `~/villa-thaifa/tickets/`
- [ ] README.md exists

**If ANY checkbox fails:** STOP, fix before proceeding.

---

## SECTION 4: VIBE KANBAN CONFIGURATION

### 4.1 Create `vibe.config.js`

```javascript
// ~/villa-thaifa/vibe.config.js

module.exports = {
  // Project metadata
  project_name: "Villa Thaifa OTA Activation",
  
  // Agent behavior
  setup_script: "echo 'No dev server needed yet'",
  test_command: null, // No automated tests yet
  linter_check: false, // No code yet
  
  // MCP servers (if agents need them)
  mcp_servers: [
    // Will add HotelRunner MCP when built
    // For now, agents use browser automation
  ],
  
  // Ticket templates
  ticket_template: {
    context_required: [
      "HotelRunner credentials (if needed)",
      "OTA platform account email",
      "Villa Thaifa property details"
    ],
    success_criteria: [
      "OTA account created",
      "Property listed",
      "First test booking possible",
      "Sync verified"
    ]
  },
  
  // Agent preferences
  preferred_agents: {
    investigation: "Claude Code",
    ota_activation: "Claude Code", // Browser automation
    documentation: "Gemini CLI"
  }
};
```

### 4.2 Board Column Workflow

**To Do → In Progress:**
- Omar drags ticket
- Vibe creates Git Worktree: `worktrees/T00X-branch`
- Agent starts (Claude Code spawns)
- Agent has isolated environment

**In Progress → In Review:**
- Agent completes work
- Vibe shows diff (what changed)
- Omar reviews in Vibe UI
- Omar can comment: "Fix this part"
- Agent reads comment, retries

**In Review → Done:**
- Omar approves
- Vibe merges worktree to main
- Worktree deleted
- Ticket archived

---

## SECTION 5: TICKET TEMPLATES (Ready to Use)

### T001: HotelRunner Sync Investigation

```markdown
# T001: HotelRunner Sync Investigation

## Context
Villa Thaifa has Booking.com connected to HotelRunner via XML.
When we create internal reservations on HotelRunner (source "Online"),
availability doesn't update on Booking.com → risk of double bookings.

## Investigation Required
1. What does "Allocation Type: No changes" control?
2. Where is "Auto-import" feature? (Repomix mentioned it, can't find in UI)
3. Why did Support say "leave Allocation Type as is"?
4. Is sync actually broken or was it fixed?

## Files to Read
- ~/villa-thaifa/docs/coordination/investigation-brief-v0.1.0.md (full protocol)
- ~/villa-thaifa/docs/coordination/workstream-master-v0.1.0.md (Section 4)

## Browser Actions Needed
- Login: https://villa-thaifa.hotelrunner.com/admin
- Navigate to Settings → Channels → Booking.com
- Take screenshots of all settings
- Check transaction logs (last 30 days)

## Deliverable
Investigation report following template in investigation-brief-v0.1.0.md

## Success Criteria
- ✅ Understand what "Allocation Type" controls
- ✅ Found "Auto-import" location (or confirmed doesn't exist)
- ✅ Clear recommendation: Safe to activate more OTAs? Yes/No + Why
- ✅ Confidence level: HIGH or MEDIUM (not LOW)

## Estimated Time
2-3 hours (with browser automation)

## Agent Assignment
Claude Code (browser-agent specialization)
```

---

### T002: Activate Booking.com OTA

```markdown
# T002: Activate Booking.com OTA

## Context
Booking.com ALREADY connected via XML (since Dec 2024).
This ticket is about VERIFYING setup + documenting process for other OTAs.

## Prerequisites
- ✅ T001 complete (sync investigation done)
- ✅ HotelRunner credentials available

## Tasks
1. Login to HotelRunner admin
2. Navigate to Channels → Booking.com
3. Verify all 8 room types mapped correctly
4. Check availability calendar (next 30 days)
5. Cross-check with Booking.com extranet
6. Document process (screenshot + notes)

## Files to Read
- ~/villa-thaifa/docs/client/project-brief-v0.2.0.md (property details)

## Success Criteria
- ✅ Room mapping verified (8 types)
- ✅ Availability accurate (compare HotelRunner ↔ Booking.com)
- ✅ Process documented (for replication on other OTAs)
- ✅ Test reservation created (internal, then verify on Booking.com)

## Estimated Time
30 minutes (verification + documentation)

## Agent Assignment
Claude Code (browser-agent)
```

---

### T003: Activate Airbnb OTA

```markdown
# T003: Activate Airbnb OTA

## Context
Villa Thaifa NOT yet on Airbnb.
Must create Airbnb host account → list property → connect to HotelRunner.

## Prerequisites
- ✅ T001 complete (know sync works)
- ✅ T002 complete (documented process)
- Said's Airbnb email (or create new one)
- Villa Thaifa photos (high-res, from docs/client/)
- Property description (in docs/client/project-brief-v0.2.0.md)

## Tasks
1. Create Airbnb host account (if not exists)
2. List property:
   - Title: "Villa Thaifa - Luxury 4BR in Marrakech"
   - Description: From project brief
   - Photos: Upload 10-15 high-quality images
   - Amenities: Pool, WiFi, Kitchen, etc. (see project brief)
   - Pricing: Start conservative (will optimize later)
3. Connect to HotelRunner:
   - HotelRunner → Channels → Add Channel → Airbnb
   - Follow connection wizard
4. Map room types (8 types → Airbnb listings)
5. Sync calendar
6. Verify availability updates

## Files to Read
- ~/villa-thaifa/docs/client/project-brief-v0.2.0.md (property details)
- ~/villa-thaifa/docs/coordination/workstream-master-v0.1.0.md (Section 3.3: OTA activation protocol)

## Success Criteria
- ✅ Airbnb account created
- ✅ Property listed (published, visible on Airbnb search)
- ✅ Connected to HotelRunner
- ✅ Calendar synced (create test booking on HotelRunner, verify blocks Airbnb)
- ✅ First booking possible (end-to-end test)

## Estimated Time
1.5-2 hours (account creation + property setup + integration)

## Agent Assignment
Claude Code (browser-agent)
```

---

### T004: Activate Expedia OTA

```markdown
# T004: Activate Expedia OTA

## Context
Villa Thaifa NOT yet on Expedia.
Expedia = partner platform (not direct host signup like Airbnb).
Must contact HotelRunner to request Expedia connection.

## Prerequisites
- ✅ T001-T003 complete
- HotelRunner support contact

## Tasks
1. Login to HotelRunner
2. Request Expedia connection:
   - Option A: Self-service (if available in Channels panel)
   - Option B: Contact HotelRunner support (email Ikram)
3. Provide property details to HotelRunner
4. Wait for Expedia approval (1-3 days usually)
5. Once approved:
   - Map room types
   - Set pricing
   - Sync calendar
6. Verify availability updates

## Files to Read
- ~/villa-thaifa/docs/client/project-brief-v0.2.0.md
- ~/villa-thaifa/docs/coordination/workstream-master-v0.1.0.md (Section 8.1: HotelRunner Support contact)

## Success Criteria
- ✅ Expedia connection requested
- ✅ If self-service: Connection complete + property listed
- ✅ If support needed: Email sent, confirmation received
- ✅ Process documented (for future OTA activations)

## Estimated Time
- Self-service: 1 hour
- Via support: 30 min (send request) + wait time (async)

## Agent Assignment
Claude Code (browser-agent + email if needed)
```

---

### T005: Activate Hotels.com OTA (STRETCH GOAL)

```markdown
# T005: Activate Hotels.com OTA

## Context
Hotels.com = Expedia Group (same backend as Expedia).
If Expedia connected, Hotels.com might auto-connect.

## Prerequisites
- ✅ T004 complete (Expedia connected)

## Tasks
1. Check if Hotels.com auto-appeared in HotelRunner channels
2. If NOT:
   - Request Hotels.com connection via HotelRunner
   - Follow same process as Expedia (T004)
3. Verify room mapping
4. Sync calendar
5. Test availability updates

## Success Criteria
- ✅ Hotels.com connected
- ✅ Property visible on Hotels.com search
- ✅ Calendar synced

## Estimated Time
30 minutes (if auto-connected), 1 hour (if manual setup)

## Agent Assignment
Claude Code (browser-agent)

## NOTE
This is a STRETCH GOAL for tonight. Only attempt if T001-T004 complete
by 23h00 and Omar has energy to continue.
```

---

## SECTION 6: TIMELINE FOR TONIGHT (17h-1h)

### 6.1 Detailed Schedule

**17h00-17h30: SETUP & MIGRATION (30 min)**
- [ ] 17h00-17h15: Migrate artifacts to Nexus (Section 3.2)
- [ ] 17h15-17h20: Validate migration (Section 3.3)
- [ ] 17h20-17h30: Launch Vibe Kanban, create tickets on board

**17h30-19h30: INVESTIGATION (2h MAX - if not done)**
- [ ] 17h30: Drag T001 to "In Progress"
- [ ] 17h30-19h00: Agent investigates HotelRunner sync
- [ ] 19h00-19h30: Omar reviews investigation report, makes decision

**19h30-23h00: OTA ACTIVATION (3.5h)**
- [ ] 19h30-20h00: T002 - Verify Booking.com (30 min)
- [ ] 20h00-22h00: T003 - Activate Airbnb (2h)
- [ ] 22h00-23h00: T004 - Request Expedia (1h)

**23h00-00h30: TESTING & VALIDATION (1.5h)**
- [ ] 23h00-23h30: Create test reservations on each OTA
- [ ] 23h30-00h00: Verify calendar sync (all OTAs blocked)
- [ ] 00h00-00h30: Cross-check availability on all platforms

**00h30-01h00: DOCUMENTATION (30 min)**
- [ ] 00h30-00h45: Update Workstream Master (Section 3: Status)
- [ ] 00h45-01h00: Create "OTA Activation Report" (what worked, what didn't)

### 6.2 Parallel Track (Optional - if App Development)

**If Omar decides to work on App in parallel:**
- Use Vibe Kanban to assign different agents
- Example: Gemini writes LHCM-OS architecture docs WHILE Claude Code activates OTAs
- Review both PRs separately
- NOT RECOMMENDED for tonight (focus = 3-4 OTAs, app tomorrow)

---

## SECTION 7: RISK MITIGATION

### 7.1 What Could Go Wrong

**RISK 1: HotelRunner Sync Still Broken**
- **Impact:** Can't safely activate more OTAs
- **Mitigation:** T001 investigation MUST complete first
- **Contingency:** If broken, fix sync before OTA activation

**RISK 2: Airbnb Account Verification Delay**
- **Impact:** Can't publish property tonight
- **Likelihood:** Medium (some hosts get instant approval, others wait 24h)
- **Mitigation:** Start Airbnb signup EARLY (19h30)
- **Contingency:** Move to Expedia (T004) while waiting for Airbnb

**RISK 3: Expedia Requires Manual Approval**
- **Impact:** Can't complete tonight (1-3 days wait)
- **Likelihood:** High (Expedia = partner channel, not direct)
- **Mitigation:** Expect this, don't count as "done" tonight
- **Contingency:** Success = "Request sent", not "Expedia live"

**RISK 4: Omar Exhausted by 23h**
- **Impact:** Can't complete all 4-5 OTAs
- **Likelihood:** Medium (8h straight is intense)
- **Mitigation:** T005 (Hotels.com) is STRETCH GOAL
- **Contingency:** 3 OTAs tonight = SUCCESS (Booking.com + Airbnb + Expedia request)

### 7.2 Success Criteria (Minimum Viable)

**MUST HAVE by 1h:**
- ✅ HotelRunner sync understood (investigation complete)
- ✅ Booking.com verified working
- ✅ Airbnb property listed (even if pending approval)
- ✅ Expedia connection requested

**NICE TO HAVE:**
- ✅ Airbnb approved + live
- ✅ Expedia approved + live (unlikely tonight)
- ✅ Hotels.com activated (stretch)

**DELIVERABLES:**
- Updated Workstream Master (progress logged)
- OTA Activation Report (process documented)
- Screenshots of each OTA (proof of completion)

---

## SECTION 8: POST-MIGRATION WORKFLOW

### 8.1 Daily Work Pattern (After Tonight)

**Morning (Omar wakes up):**
1. Open Vibe Kanban: `cd ~/villa-thaifa && npx vibe-kanban`
2. Review overnight agent work (if any agents ran async)
3. Check "In Review" column
4. Approve or comment on PRs

**Work Session:**
1. Create new tickets for today's goals
2. Drag to "In Progress"
3. Agents work in parallel
4. Omar reviews incrementally (don't wait for all done)

**Evening:**
1. Merge approved PRs
2. Update Workstream Master
3. Plan tomorrow's tickets

### 8.2 Integration with claude.ai (Lux)

**Lux's New Role:**
- Strategic planning (still in claude.ai)
- Ticket creation (generate prompts for Vibe Kanban)
- Report synthesis (analyze agent outputs)

**Lux Does NOT:**
- Execute code (agents on Nexus do that)
- Review PRs (Omar does that in Vibe UI)

**Handoff Protocol:**
1. Omar asks Lux: "Create ticket for [task]"
2. Lux writes ticket in claude.ai
3. Omar copies ticket to Vibe Kanban board
4. Agent executes
5. Omar reviews in Vibe UI
6. If questions arise, Omar asks Lux for strategy

---

## SECTION 9: NEXT STEPS (After 1h Tonight)

### 9.1 Friday Morning (2025-01-10)

**Review Session:**
- [ ] Check Airbnb approval status
- [ ] Check Expedia approval status
- [ ] Read OTA Activation Report (created last night)
- [ ] Count active OTAs (goal: 3-4)

**Decision:**
- If 3+ OTAs live → Start Phase 1 (LHCM-OS App development)
- If <3 OTAs live → Finish OTA activation first

### 9.2 LHCM-OS App (Phase 1)

**If Omar decides to start app tomorrow:**
- Create new tickets in Vibe Kanban
- Parallel development (multiple agents)
- Reference: A08 LHCM-OS Strategy (docs/strategy/)

**Tech Stack:**
- Next.js 15 (App Router)
- Cloudflare Pages hosting
- D1 database (or PostgreSQL TBD)
- Clerk auth (or Auth0 TBD)

---

## APPENDIX A: COMMANDS REFERENCE

### Essential Commands

**Vibe Kanban:**
```bash
cd ~/villa-thaifa
npx vibe-kanban           # Start server
open http://localhost:3000 # Open board
```

**Git Worktrees (Vibe manages these, but useful to know):**
```bash
git worktree list         # See all worktrees
git worktree remove T001  # Clean up (Vibe does this)
```

**Claude Code:**
```bash
claude --help             # See all commands
claude chat               # Start chat session
claude task <ticket.md>   # Execute ticket (Vibe uses this)
```

---

## APPENDIX B: TROUBLESHOOTING

### Vibe Kanban Not Starting

**Symptom:** `npx vibe-kanban` errors

**Fix:**
```bash
# Check Node version (need 18+)
node --version

# If old, update Node
# Then retry
```

### Agent Stuck in "In Progress"

**Symptom:** Ticket in "In Progress" >30 min, no updates

**Fix:**
1. Check agent logs (Vibe UI → ticket → "View Logs")
2. If stuck, click "Cancel" in Vibe UI
3. Read error message
4. Fix ticket (add more context)
5. Drag to "To Do" again

### Git Worktree Conflicts

**Symptom:** Vibe says "Cannot create worktree"

**Fix:**
```bash
# Clean up orphaned worktrees
git worktree prune

# Or manually remove
git worktree remove --force worktrees/T001-branch
```

---

## END OF MIGRATION PLAN

**Omar:** Exécute Section 3.2 à 17h pile.  
**Goal:** 17h30 = Vibe Kanban running, tickets ready, agents standing by.  
**Tonight:** 3-4 OTAs activés by 1h.

**Bon appétit! On se voit à 17h pour lancer la machine. 🚀**

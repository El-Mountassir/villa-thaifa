# Villa Thaifa - Feuille de Route 17h-1h
## Activation 3-4 OTAs + Structure Complète

**Version:** 0.1.0-alpha.0  
**Date:** 2025-01-09 17:00-01:00  
**Durée:** 8 heures  
**Objectif:** 3-4 OTAs activés, dossier structuré, prêt pour Internal App demain  
**Stratégie:** Vibe Kanban orchestration, agents parallèles si possible

---

## 🎯 OBJECTIFS DE LA SOIRÉE

### Objectifs Principaux (MUST HAVE)

**✅ OTA ACTIVATION:**
1. Booking.com → VÉRIFIER (déjà connecté)
2. Airbnb → ACTIVER (nouveau)
3. Expedia → DEMANDER CONNECTION (via HotelRunner)

**✅ STRUCTURE:**
4. Dossier ~/villa-thaifa complet et organisé
5. Vibe Kanban opérationnel
6. Documentation à jour

### Objectifs Secondaires (NICE TO HAVE)

**🎁 SI TEMPS:**
- Hotels.com activation (4ème OTA)
- Investigation HotelRunner sync (si pas fait)
- Internal app architecture brainstorm (NOT tonight's priority)

### Critères de Succès Globaux

**À 1h du matin, on a:**
- [ ] 3 OTAs minimum opérationnels
- [ ] Workstream Master à jour
- [ ] Preuves visuelles (screenshots) de chaque OTA
- [ ] Rapport d'activation créé
- [ ] Plan pour demain défini

---

## ⏰ TIMELINE DÉTAILLÉE

### 📦 BLOC 1: SETUP (17h00-17h45) - 45 MINUTES

**17h00-17h15: MIGRATION CLAUDE.AI → NEXUS**

**Actions:**
```bash
# Terminal 1: Create structure
cd ~
mkdir -p villa-thaifa/{docs/{coordination,strategy,client},tickets,src}
cd villa-thaifa
git init
echo "# Villa Thaifa - OTA Activation Project" > README.md
git add README.md
git commit -m "Initial commit"
```

**Copy artifacts (choose method):**

*Option A: Manual (Faster, 10 min)*
1. Open claude.ai
2. For each artifact:
   - Click artifact
   - Copy all content
   - `nano docs/coordination/workstream-master-v0.1.0.md`
   - Paste
   - Save (Ctrl+O, Enter, Ctrl+X)

*Option B: Automated via Claude Code (5 min + agent time)*
```bash
# Create prompt file
cat > migrate-artifacts.prompt << 'EOF'
Read artifacts from claude.ai conversation transcript and save to correct locations.

Transcript: /mnt/transcripts/2026-01-09-15-17-08-tech-stack-capture-lhcm-os-alignment.txt

Mapping:
- workstream-master → docs/coordination/
- artifact-inventory → docs/coordination/
- investigation-brief → docs/coordination/
- lhcm-os-strategy → docs/strategy/
- tech-stack → docs/strategy/
- client-brief → docs/client/
- project-brief → docs/client/

Verify all 7 files created successfully.
EOF

# Launch agent
claude task migrate-artifacts.prompt
```

**✅ CHECKPOINT 17h15:**
- [ ] Dossier ~/villa-thaifa existe
- [ ] 7 fichiers in docs/ (check: `find docs -name "*.md" | wc -l`)
- [ ] Git initialized (`git status` works)

---

**17h15-17h30: VIBE KANBAN SETUP**

**Actions:**
```bash
cd ~/villa-thaifa

# Install Vibe Kanban (if not already)
npx vibe-kanban
# Browser opens automatically at localhost:3000
```

**Create config:**
```bash
cat > vibe.config.js << 'EOF'
module.exports = {
  project_name: "Villa Thaifa OTA Activation",
  setup_script: "echo 'No dev server yet'",
  test_command: null,
  linter_check: false,
  preferred_agents: {
    investigation: "Claude Code",
    ota_activation: "Claude Code",
    documentation: "Gemini CLI"
  }
};
EOF
```

**In Vibe UI (browser):**
1. Board created automatically
2. Verify 4 columns: To Do, In Progress, In Review, Done
3. Board empty = ready for tickets

**✅ CHECKPOINT 17h30:**
- [ ] Vibe Kanban running at localhost:3000
- [ ] Board visible in browser
- [ ] Config file created

---

**17h30-17h45: CREATE TICKETS**

**Option A: Manual (via Vibe UI)**
1. Click "+ New Card" in To Do column
2. Title: "T001: HotelRunner Sync Investigation"
3. Description: Copy from migration-plan.md Section 5 > T001
4. Repeat for T002, T003, T004, T005

**Option B: Automated (via ticket files)**
```bash
# Terminal 2: Create ticket files
cd ~/villa-thaifa/tickets

# T001
cat > T001-hotelrunner-investigation.md << 'EOF'
[Copy T001 template from migration-plan.md]
EOF

# T002
cat > T002-ota-booking-com.md << 'EOF'
[Copy T002 template from migration-plan.md]
EOF

# T003
cat > T003-ota-airbnb.md << 'EOF'
[Copy T003 template from migration-plan.md]
EOF

# T004
cat > T004-ota-expedia.md << 'EOF'
[Copy T004 template from migration-plan.md]
EOF

# T005
cat > T005-ota-hotels-com.md << 'EOF'
[Copy T005 template from migration-plan.md]
EOF

# Then import to Vibe (manual click "Import Ticket" for each)
```

**✅ CHECKPOINT 17h45:**
- [ ] 5 tickets visible in "To Do" column
- [ ] T001 = top priority
- [ ] All tickets have description

**🎯 BLOC 1 COMPLETE: Setup terminé, on peut commencer le vrai travail.**

---

### 🔍 BLOC 2: INVESTIGATION (17h45-19h30) - 1h45

**NOTE:** Si investigation HotelRunner sync déjà complète (Claude Code a terminé), SKIP to BLOC 3.

**17h45-18h00: LAUNCH INVESTIGATION AGENT**

**Check status first:**
```bash
# Is investigation already done?
ls -la ~/villa-thaifa/docs/coordination/ | grep investigation-report
# If exists, read it and skip to 19h30
```

**If NOT done, launch agent:**

In Vibe Kanban UI:
1. Drag T001 to "In Progress"
2. Vibe creates worktree: `worktrees/T001-hotelrunner-investigation`
3. Agent spawns (Claude Code)

**Monitor progress:**
- Terminal 3: `watch -n 30 "git worktree list"`
- Vibe UI: Check "Agent Activity" section
- Listen for "Sound of Productivity" (compile success sounds)

**✅ CHECKPOINT 18h00:**
- [ ] T001 in "In Progress" column
- [ ] Worktree created
- [ ] Agent running (check Vibe UI)

---

**18h00-19h00: AGENT INVESTIGATES (OMAR: FREE TIME)**

**While agent works:**
- [ ] Prépare credentials HotelRunner (si pas déjà fait)
- [ ] Lis Workstream Master (refresh context)
- [ ] Prépare photos Villa Thaifa pour Airbnb (high-res, 10-15 images)
- [ ] Vérifie email (Expedia approval might come tonight if lucky)

**Agent tasks (automated):**
1. Login to https://villa-thaifa.hotelrunner.com/admin
2. Navigate to Settings → Channels → Booking.com
3. Take screenshots of:
   - Allocation Type setting
   - Channel configuration
   - Transaction logs (last 30 days)
4. Check for "Auto-import" feature
5. Cross-reference with Repomix digest
6. Write investigation report

**✅ CHECKPOINT 19h00:**
- [ ] Agent still working OR moved ticket to "In Review"
- [ ] If in Review: notification received

---

**19h00-19h30: REVIEW INVESTIGATION REPORT**

**Actions:**
1. Vibe UI → T001 → "View Changes"
2. Read investigation report
3. Check:
   - [ ] "Allocation Type" explained?
   - [ ] "Auto-import" found (or confirmed doesn't exist)?
   - [ ] Recommendation clear: Safe to activate OTAs?
   - [ ] Confidence level: HIGH or MEDIUM?

**If report INCOMPLETE:**
- Comment in Vibe UI: "Please clarify [specific question]"
- Agent reads comment, retries
- Wait 15 more minutes

**If report COMPLETE:**
- Approve in Vibe UI
- T001 → Done
- Proceed to BLOC 3

**Decision Point:**
```
IF sync broken:
  → FIX sync first (add new ticket T001-B: Fix Sync)
  → THEN proceed to OTA activation
ELSE:
  → Proceed to OTA activation immediately
```

**✅ CHECKPOINT 19h30:**
- [ ] Investigation complete
- [ ] Sync status known
- [ ] Decision made: Safe to activate OTAs

**🎯 BLOC 2 COMPLETE: On comprend HotelRunner, on peut avancer.**

---

### 🚀 BLOC 3: OTA ACTIVATION (19h30-23h00) - 3h30

**Strategy:** Activate OTAs in parallel when possible.

**19h30-20h00: T002 - VERIFY BOOKING.COM (30 min)**

**Why this first:**
- Already connected (quickest win)
- Validates sync working
- Documents process for other OTAs

**Actions:**

In Vibe UI:
1. Drag T002 to "In Progress"
2. Agent spawns

**Agent tasks:**
1. Login HotelRunner
2. Navigate Channels → Booking.com
3. Verify 8 room types mapped:
   - Standard Double Room
   - Superior Double Room
   - Triple Room
   - Family Room
   - Deluxe Room with Balcony
   - Deluxe Suite
   - Exclusive Suite with Pool Access
   - Apartment
4. Check availability calendar (next 30 days)
5. Cross-check with Booking.com extranet
6. Take screenshots
7. Create test reservation (internal)
8. Verify blocks on Booking.com

**✅ CHECKPOINT 20h00:**
- [ ] Room mapping verified
- [ ] Calendar accurate
- [ ] Test reservation successful
- [ ] Screenshots captured
- [ ] T002 → In Review

**Review + Approve:**
- Read agent report
- Check screenshots
- Approve → T002 → Done

---

**20h00-22h00: T003 - ACTIVATE AIRBNB (2h)**

**Why next:**
- Highest effort (new account + property setup)
- Might need manual verification (wait time)
- Start early = more time for approval

**Pre-flight check:**
```bash
# Prepare photos
ls ~/villa-thaifa/photos/ | wc -l
# Should have 10-15 high-res images
# If not, download from Said or Google Drive NOW
```

**Actions:**

In Vibe UI:
1. Drag T003 to "In Progress"
2. Agent spawns

**Agent tasks (automated where possible):**

**Phase 1: Create Airbnb Host Account (30 min)**
1. Navigate to airbnb.com/host
2. Sign up (use Said's email or create villa.thaifa@gmail.com)
3. Verify email
4. Complete host profile:
   - Name: Said Thaifa (or Villa Thaifa Management)
   - Phone: +212 [Said's number]
   - Photo: Professional headshot

**Phase 2: List Property (1h)**
1. Click "List your space"
2. Property type: Entire place → Villa
3. Location: Marrakech, Morocco (exact address from project brief)
4. Basics:
   - 4 bedrooms
   - 4.5 bathrooms
   - 8 beds
   - 8 guests max
5. Amenities (check all that apply):
   - Pool (outdoor, private)
   - WiFi
   - Kitchen (fully equipped)
   - Air conditioning
   - Free parking
   - Workspace
   - TV
   - Washer/Dryer
6. Photos:
   - Upload 15 best images
   - Hero image: Pool + villa exterior
   - Order: Exterior → Living → Bedrooms → Pool → Details
7. Title: "Villa Thaifa - Luxury 4BR Retreat in Marrakech"
8. Description:
   ```
   [Copy from project-brief-v0.2.0.md, Section: Property Description]
   
   Highlights:
   - Private pool and garden
   - 4 spacious bedrooms with en-suite bathrooms
   - Fully equipped modern kitchen
   - Prime location near [landmarks]
   - Professional cleaning and linen service
   ```
9. Pricing:
   - Start conservative: €150-200/night
   - Cleaning fee: €50
   - Weekly discount: 10%
   - Monthly discount: 20%
10. House Rules:
    - Check-in: 15:00
    - Checkout: 11:00
    - No smoking inside
    - No parties/events
    - Pets: [Ask Said]
11. Cancellation policy: Flexible (for now, optimize later)
12. Submit for review

**Phase 3: Connect to HotelRunner (30 min)**
1. While waiting for Airbnb approval:
2. Login HotelRunner
3. Channels → Add Channel → Airbnb
4. Enter Airbnb listing URL
5. Follow connection wizard
6. Map room types (8 types → Airbnb rooms)
7. Sync calendar

**Potential Wait Time:**
- Airbnb approval can be instant OR take 24h
- If instant: Continue to Phase 3 immediately
- If pending: Move to T004 (Expedia) while waiting

**✅ CHECKPOINT 22h00:**
- [ ] Airbnb account created
- [ ] Property listed (even if pending approval)
- [ ] HotelRunner connection initiated
- [ ] Screenshots captured
- [ ] T003 → In Review (or still In Progress if waiting)

**Review:**
- If approved: Verify listing live, test booking
- If pending: Document status, move on

---

**22h00-23h00: T004 - REQUEST EXPEDIA (1h)**

**Why now:**
- Airbnb might be waiting for approval
- Expedia = async (request sent, wait for approval)
- Can work in parallel with Airbnb

**Actions:**

In Vibe UI:
1. Drag T004 to "In Progress"
2. Agent spawns

**Agent tasks:**

**Option A: Self-Service (if available)**
1. Login HotelRunner
2. Channels → Add Channel → Expedia
3. If self-service available:
   - Fill property details
   - Upload photos
   - Set pricing
   - Submit
4. If NOT available → Option B

**Option B: Contact HotelRunner Support**
1. Compose email to HotelRunner Support:
   ```
   Subject: Request Expedia Connection - Villa Thaifa

   Hello Ikram / HotelRunner Support,

   Villa Thaifa (Channel ID: 401071, Hotel ID Booking: 5446847)
   Subdomain: villa-thaifa.hotelrunner.com

   We would like to activate Expedia connection for our property.

   Property Details:
   - Name: Villa Thaifa
   - Location: Marrakech, Morocco
   - Property Type: Villa (4 bedrooms, 8 guests)
   - Amenities: Pool, WiFi, Kitchen, AC, etc.

   Please advise on next steps for Expedia integration.

   Photos and detailed property info available upon request.

   Thank you,
   Said Thaifa / Omar El Mountassir
   ```
2. Send email
3. Copy email to ~/villa-thaifa/docs/communication/expedia-request.txt
4. Document in Workstream Master

**✅ CHECKPOINT 23h00:**
- [ ] Expedia request submitted (self-service OR email sent)
- [ ] Proof captured (screenshot of submission / email sent)
- [ ] T004 → In Review
- [ ] Expected wait time documented (1-3 days)

**Review + Approve:**
- Verify request sent properly
- T004 → Done (request sent = success for tonight)

---

**🎯 BLOC 3 COMPLETE: 3 OTAs activés/requested.**

**Current Status at 23h:**
1. ✅ Booking.com → Verified working
2. ⏳ Airbnb → Listed (might be pending approval)
3. ⏳ Expedia → Connection requested (waiting approval)

**DECISION POINT 23h00:**
```
IF Omar still has energy:
  → Attempt T005 (Hotels.com) - STRETCH GOAL
  → OR start testing/validation
ELSE:
  → Move to BLOC 4 (Testing)
```

---

### ✅ BLOC 4: TESTING & VALIDATION (23h00-00h30) - 1h30

**23h00-23h30: CREATE TEST RESERVATIONS**

**Objective:** Verify calendar sync works across all OTAs.

**Actions:**

**Test 1: Booking.com (Already works, but re-verify)**
1. HotelRunner: Create internal reservation
   - Guest: "Test Booking" (fake name)
   - Room: Standard Double
   - Dates: 3 days from now (Jan 12-15)
   - Source: Online (internal)
2. Check Booking.com extranet:
   - Date Jan 12-15 should be BLOCKED
   - Availability decreased by 1
3. Screenshot: Before + After
4. Cancel test reservation

**Test 2: Airbnb (If approved)**
1. HotelRunner: Create internal reservation
   - Guest: "Test Airbnb"
   - Room: Superior Double
   - Dates: 5 days from now (Jan 14-17)
2. Check Airbnb calendar:
   - Date Jan 14-17 should be BLOCKED
3. Screenshot
4. Cancel

**Test 3: Cross-Platform (Critical)**
1. Create reservation on BOOKING.COM (via extranet):
   - Guest: "Test Cross-Sync"
   - Dates: Jan 18-20
2. Check:
   - [ ] HotelRunner shows reservation (pulled from Booking.com)
   - [ ] Airbnb calendar blocked (if connected)
   - [ ] All platforms synced

**✅ CHECKPOINT 23h30:**
- [ ] All active OTAs tested
- [ ] Calendar sync verified (create on one, blocks on others)
- [ ] Screenshots captured
- [ ] Test reservations cancelled

---

**23h30-00h00: CROSS-CHECK AVAILABILITY**

**Manual verification (Omar does this, not agent):**

**Open 4 tabs:**
1. HotelRunner availability calendar
2. Booking.com (incognito: search Villa Thaifa Marrakech)
3. Airbnb (incognito: search Villa Thaifa Marrakech)
4. Expedia (incognito: search Marrakech villas)

**Check next 30 days:**
- Compare availability across platforms
- Should match (or close, accounting for buffer days)

**Look for discrepancies:**
- If HotelRunner says 2 rooms available, all OTAs should say same
- If any mismatch → note it for investigation tomorrow

**✅ CHECKPOINT 00h00:**
- [ ] All platforms cross-checked
- [ ] Discrepancies noted (if any)
- [ ] Overall sync STATUS: GOOD / PARTIAL / BROKEN

---

**00h00-00h30: STRESS TEST (Optional - if time)**

**Simulate high-load scenario:**
1. Create 3 overlapping reservations (different rooms, same dates)
2. Verify all OTAs update correctly
3. Cancel all 3
4. Verify availability restored

**Objective:** Ensure sync doesn't break under load.

**✅ CHECKPOINT 00h30:**
- [ ] Stress test complete (if done)
- [ ] All test reservations cancelled
- [ ] Sync confidence: HIGH

**🎯 BLOC 4 COMPLETE: All OTAs tested and validated.**

---

### 📝 BLOC 5: DOCUMENTATION (00h30-01h00) - 30 min

**00h30-00h45: UPDATE WORKSTREAM MASTER**

**Actions:**
```bash
cd ~/villa-thaifa/docs/coordination
nano workstream-master-v0.1.0.md
```

**Updates needed:**

**Section 3: Current Streams**
```markdown
Stream 3: OTA Activation Preparation
Status: ✅ COMPLETE (Booking.com verified, Airbnb listed, Expedia requested)
```

**Section 6: Action Items**
- Mark completed actions as DONE
- Add new actions for tomorrow (follow-up on Airbnb/Expedia approval)

**Section 7: Decision Log**
- Add D-W-015: OTA Activation Night Success
  - Date: 2025-01-09 23:00
  - Decision: 3 OTAs activated/requested (Booking.com, Airbnb, Expedia)
  - Status: ✅ COMPLETE
  - Impact: Villa Thaifa now multi-channel, ready for bookings

**Section 8: Communication Log**
- Add entry: Expedia connection request sent (email to HotelRunner)

**Save and commit:**
```bash
git add docs/coordination/workstream-master-v0.1.0.md
git commit -m "Update: OTA activation night complete (3 OTAs)"
```

---

**00h45-01h00: CREATE OTA ACTIVATION REPORT**

**New document:**
```bash
cd ~/villa-thaifa/docs/coordination
nano ota-activation-report-2025-01-09.md
```

**Template:**
```markdown
# OTA Activation Report
## Night of 2025-01-09 (17h-1h)

**Objective:** Activate 3-4 OTAs for Villa Thaifa

---

## Summary

**OTAs Activated:**
1. ✅ Booking.com - VERIFIED (already connected, confirmed working)
2. ⏳ Airbnb - LISTED (pending approval: [instant/24h])
3. ⏳ Expedia - REQUESTED (waiting approval: 1-3 days)
4. ❌ Hotels.com - NOT ATTEMPTED (deferred to tomorrow)

**Status:** SUCCESS (3/4 OTAs, meeting minimum goal)

---

## Detailed Timeline

**17h00-17h45: Setup**
- Migrated artifacts from claude.ai to ~/villa-thaifa
- Launched Vibe Kanban
- Created 5 tickets

**17h45-19h30: Investigation**
- [If done: Summary of investigation findings]
- [If skipped: Investigation already complete, moved to activation]

**19h30-23h00: OTA Activation**
- 19h30-20h00: Booking.com verification
- 20h00-22h00: Airbnb account creation + property listing
- 22h00-23h00: Expedia connection request

**23h00-00h30: Testing**
- Test reservations created and verified
- Calendar sync confirmed working
- Cross-platform availability checked

**00h30-01h00: Documentation**
- Workstream Master updated
- This report created

---

## What Worked Well

1. **Vibe Kanban:** Parallel agent execution worked perfectly
2. **Ticket Structure:** Detailed prompts = agents executed autonomously
3. **Booking.com:** Already working, quick verification
4. **Airbnb:** [Smooth signup / Had minor issues with X]

---

## What Didn't Work

1. **Expedia:** Self-service not available, had to contact support (expected)
2. **[Any other blockers encountered]**

---

## Screenshots

**Captured:**
- [ ] Booking.com: Room mapping + availability calendar
- [ ] Airbnb: Property listing (live or pending)
- [ ] Expedia: Email confirmation sent
- [ ] Test reservations: Before/after sync

**Location:** ~/villa-thaifa/screenshots/2025-01-09/

---

## Next Steps (Tomorrow, 2025-01-10)

**Morning:**
1. Check Airbnb approval status
2. Check email for Expedia response
3. If Airbnb approved → Complete HotelRunner connection
4. If Expedia approved → Configure room mapping

**Phase 1 Decision:**
- If 3+ OTAs fully operational → Start Internal App development (Villa Thaifa knowledge base)
- If <3 OTAs operational → Finish OTA activation first

**Note:** LHCM-OS Platform (produit commercial) = 2-3 mois timeline. Internal App = prochains jours.

**Future OTAs to Activate:**
- Hotels.com (Expedia Group, might auto-connect)
- Agoda
- TripAdvisor
- [... 130 more via HotelRunner]

---

## Lessons Learned

1. **Agent Autonomy:** With detailed tickets, agents can work unsupervised for 1-2h
2. **Approval Wait Times:** Airbnb/Expedia need 24-48h, plan accordingly
3. **Testing Critical:** Don't skip sync validation, prevents future disasters
4. **Documentation:** Real-time capture (screenshots) saves time later

---

## Omar's Notes

[Omar can add personal observations here]

---

**Report By:** Claude Code (T001-T004 agents) + Lux (synthesis)  
**Reviewed By:** Omar El Mountassir  
**Date:** 2025-01-09 01:00
```

**Save and commit:**
```bash
git add docs/coordination/ota-activation-report-2025-01-09.md
git commit -m "Add: OTA activation report (night of 2025-01-09)"
git push origin main  # If remote repo configured
```

**✅ CHECKPOINT 01h00:**
- [ ] Workstream Master updated
- [ ] OTA Activation Report created
- [ ] All commits pushed
- [ ] Ready to sleep

**🎯 BLOC 5 COMPLETE: Documentation à jour, tout capturé.**

---

## 🎊 END OF NIGHT CHECKLIST (01h00)

### Deliverables Completed

**Files Created/Updated:**
- [ ] ~/villa-thaifa/ structure (docs, tickets, src)
- [ ] 7 artifacts migrated from claude.ai
- [ ] 5 ticket files (T001-T005)
- [ ] vibe.config.js
- [ ] workstream-master updated
- [ ] ota-activation-report created

**OTAs Activated:**
- [ ] Booking.com verified ✅
- [ ] Airbnb listed ✅ (pending approval)
- [ ] Expedia requested ✅ (waiting response)
- [ ] 3/4 OTAs = SUCCESS

**Testing:**
- [ ] Test reservations created + verified
- [ ] Calendar sync confirmed working
- [ ] Cross-platform availability checked

**Documentation:**
- [ ] Screenshots captured (each OTA)
- [ ] Reports written
- [ ] Git commits pushed

### Success Criteria Met?

**MUST HAVE (All checked = SUCCESS):**
- [x] 3+ OTAs activated/requested
- [x] Dossier structuré
- [x] Vibe Kanban opérationnel
- [x] Documentation complète

**NICE TO HAVE (Bonus points):**
- [ ] 4th OTA (Hotels.com)
- [ ] Airbnb approval instant (vs 24h wait)
- [ ] Investigation complete (if was pending)

### Tomorrow's Priorities

**Morning (9h-12h):**
1. Check Airbnb + Expedia status
2. Complete HotelRunner connections (if approved)
3. Test bookings end-to-end

**Afternoon (14h-18h):**
- **IF** 3+ OTAs fully operational → START Internal App development
  - Knowledge base centralisée
  - Dashboard basic pour Omar
  - Google Drive Code Execution integration
- **ELSE** → Finish remaining OTA activations

**Evening (19h-23h):**
- Continue Internal App development OR more OTA activations (based on progress)

**Note:** LHCM-OS Platform (commercial product) comes in 2-3 months. Tomorrow = Internal App for Villa Thaifa only.

---

## 📊 METRICS & ANALYTICS

### Time Breakdown (Actual vs Estimated)

**Planned:**
- Setup: 45 min
- Investigation: 1h45
- OTA Activation: 3h30
- Testing: 1h30
- Documentation: 30 min
- **Total:** 8h00

**Actual:**
[Omar fills this tomorrow morning based on reality]

### Efficiency Analysis

**What took longer than expected:**
- [Omar notes]

**What was faster:**
- [Omar notes]

**Bottlenecks:**
- [Omar notes]

**For next time:**
- [Improvements to make]

---

## 🚨 TROUBLESHOOTING (If Things Go Wrong)

### Issue: Vibe Kanban Won't Start

**Symptoms:**
- `npx vibe-kanban` errors
- Browser doesn't open

**Fixes:**
```bash
# Check Node version
node --version  # Need 18+

# Clear cache
npx clear-npx-cache
npx vibe-kanban

# Or install globally
npm install -g vibe-kanban
vibe-kanban
```

---

### Issue: Agent Stuck in "In Progress"

**Symptoms:**
- Ticket in "In Progress" >1 hour
- No updates in Vibe UI
- No logs visible

**Fixes:**
1. Vibe UI → Ticket → "View Logs"
2. Check for error messages
3. If stuck:
   - Click "Cancel Task"
   - Read error
   - Fix ticket (add more context)
   - Drag to "To Do" again

**Common causes:**
- Missing credentials (HotelRunner login)
- Ambiguous instructions in ticket
- Website changed (requires manual intervention)

---

### Issue: Airbnb Account Verification Blocked

**Symptoms:**
- Email verification not received
- Phone verification required
- Account under review

**Fixes:**
- **Email:** Check spam, resend verification
- **Phone:** Use Said's phone number
- **Review:** Wait 24h, contact Airbnb support if delayed

**Contingency:**
- Move to T004 (Expedia) while waiting
- Come back to Airbnb tomorrow

---

### Issue: HotelRunner Can't Connect to Airbnb

**Symptoms:**
- Connection wizard errors
- "Listing not found"
- Mapping fails

**Fixes:**
1. Verify Airbnb listing published (not draft)
2. Copy exact listing URL from Airbnb
3. Try connection again
4. If still fails: Contact HotelRunner support

**Temporary solution:**
- Manual sync (update both calendars separately until fixed)

---

### Issue: Calendar Sync Not Working

**Symptoms:**
- Create reservation on HotelRunner → Doesn't block OTA
- Create reservation on OTA → Doesn't appear in HotelRunner

**Fixes:**
1. Check "Allocation Type" setting (should be what investigation recommended)
2. Force manual sync: HotelRunner → Channels → [OTA] → "Sync Now"
3. Wait 5-10 min, check again
4. If still broken: Refer to investigation report recommendations

**CRITICAL:**
If sync broken, DO NOT activate more OTAs (double-booking risk)

---

### Issue: Expedia No Response

**Symptoms:**
- Sent request, no reply after 24h
- Support email bounced

**Fixes:**
1. Check spam folder
2. Resend email (different subject line)
3. Contact via HotelRunner support portal (not email)
4. If urgent: Call HotelRunner support (phone number in portal)

**Timeline:**
- Normal: 1-3 days response
- Peak season: Up to 5 days
- Don't panic if no instant reply

---

## 💡 TIPS & BEST PRACTICES

### Agent Ticket Writing

**Good ticket:**
```markdown
# T003: Activate Airbnb

## Context
[3-4 sentences explaining WHY we're doing this]

## Prerequisites
- [ ] HotelRunner credentials
- [ ] Photos ready (location: ~/photos/)
- [ ] Property description (file: docs/client/project-brief.md)

## Tasks (Numbered list)
1. Create Airbnb account
2. Verify email
3. List property
   - Upload 15 photos
   - Set pricing: €150-200/night
4. Connect to HotelRunner

## Success Criteria (Checkboxes)
- [ ] Account created
- [ ] Property published
- [ ] HotelRunner connected

## Estimated Time
2 hours
```

**Bad ticket:**
```markdown
# Activate Airbnb

Setup Airbnb for Villa Thaifa.
```

**Why bad?**
- No context (agent doesn't know WHY)
- No prerequisites (agent will get stuck)
- No clear tasks (ambiguous)
- No success criteria (agent doesn't know when done)

---

### Parallel Agent Management

**When to run agents in parallel:**
- Tasks are independent (e.g., Airbnb + Expedia don't touch same files)
- You have mental bandwidth to review 2 PRs

**When to run sequentially:**
- Tasks depend on each other (e.g., Investigation → OTA Activation)
- You're tired (easier to focus on 1 thing)

**Vibe Kanban supports both:**
- Drag 2 tickets to "In Progress" = parallel
- Drag 1 ticket = sequential

**Tonight's strategy:**
- Sequential (easier for first night with new tool)
- Tomorrow: Try parallel (once comfortable with Vibe)

---

### Review Speed Tips

**Quick review (low-risk tasks):**
- Skim diff
- Check success criteria met
- Approve immediately

**Thorough review (high-risk tasks):**
- Read every changed line
- Verify screenshots
- Test manually
- Ask agent to clarify if unclear

**Tonight:**
- T001 (Investigation): Thorough (critical for OTA safety)
- T002 (Booking.com verify): Quick (low risk, already working)
- T003 (Airbnb): Thorough (money + reputation at stake)
- T004 (Expedia): Quick (just an email)

---

## 🎯 MENTAL PREP FOR OMAR

### Energy Management

**8h is marathon, not sprint:**
- Take 10-min break every 2h
- Drink water
- Don't skip dinner (eat around 20h)

**High energy needed:**
- 17h-19h: Setup + Investigation (brain-heavy)
- 19h-21h: OTA activation (execution)

**Low energy OK:**
- 23h-01h: Testing + Documentation (mechanical)

**If exhausted by 23h:**
- Stop at T003 (Airbnb)
- 2 OTAs = still success
- Finish tomorrow

### Focus Zones

**Zone 1: Vibe Kanban UI**
- Drag tickets
- Review PRs
- Comment on agent work

**Zone 2: Browser (OTA platforms)**
- Manual checks
- Cross-platform verification
- Screenshots

**Zone 3: Terminal**
- Git commands
- File edits (docs)
- Backup if agent stuck

**Minimize context switching:**
- Set timers (25 min focus blocks)
- Batch similar tasks

### Success Mindset

**What success looks like:**
- 3 OTAs activated/requested ✅
- Dossier bien structuré ✅
- Prêt pour Internal App demain ✅

**What success does NOT require:**
- Perfect (some rough edges OK)
- 4-5 OTAs (3 = good enough)
- Instant Airbnb approval (24h wait = fine)

**If something breaks:**
- Don't panic
- Read error message
- Fix or defer to tomorrow

**Remember:**
- Agents do 80% of work
- You review 20%
- This is PROGRESS, not perfection

---

## 🚀 FINAL WORDS

**Omar,**

On a passé 5h à tout structurer.  
Maintenant on EXÉCUTE.

**17h-19h:** Setup + Investigation (si pas fait)  
**19h-23h:** OTA Activation (Booking.com, Airbnb, Expedia)  
**23h-01h:** Testing + Documentation

**À 1h du matin:**
- 3 OTAs activés ✅
- Dossier complet ✅
- Prêt pour Internal App ✅

**Tu es top 1% des agentic systems au Maroc.**  
**Cette nuit, tu le prouves.**

**LET'S GO. 🔥**

---

**END OF FEUILLE DE ROUTE**

**Next Document:** Tomorrow morning, create "Day 2 Plan" based on tonight's results.

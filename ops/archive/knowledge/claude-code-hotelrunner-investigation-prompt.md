# MISSION: HOTELRUNNER SYNC INVESTIGATION

**For:** Claude Code + Browser Agent  
**Priority:** P0 - CRITICAL  
**Deadline:** Today (2025-01-09), 2-4 hours  
**Deliverable:** Structured Investigation Report

---

## CONTEXT

Villa Thaifa has sync issue between HotelRunner (channel manager) and Booking.com. We need to understand this COMPLETELY before activating 4-5 more OTAs.

**What We Thought:**

- Internal reservations (created on HotelRunner) don't push to Booking.com
- Suspected root cause: "Allocation Type" = "No changes" setting

**NEW Info (from Support Team today):**

- Support says: "Allocation Type = No changes MUST stay as is, or inventory won't update"
- This CONTRADICTS our diagnosis

**Mystery:**

- "Auto-import" feature mentioned in docs but Omar can't find it in UI
- Support told Said "problem fixed" but didn't confirm to Omar
- No clear answer to our 3 specific questions

**Risk:** If we don't understand sync, activating more OTAs = multiply double-booking risk.

---

## YOUR MISSION

**Investigate HotelRunner sync mechanism, understand the truth, provide clear recommendation.**

Use browser agent to access HotelRunner admin, research documentation, optionally test (if Omar approves), deliver structured report.

---

## INVESTIGATION PROTOCOL

### PHASE A: Information Gathering (REQUIRED - 30-60 min)

#### Task A1: Access HotelRunner Admin

- Navigate to: https://villa-thaifa.hotelrunner.com/admin
- Log in with credentials Omar provides
- Take screenshot of dashboard
- Verify you have admin access

#### Task A2: Locate Settings

- Find "Allocation Type" setting
  - Likely in: Settings → Channel Management → Booking.com → Advanced Parameters
  - Document EXACT navigation path
  - Screenshot the setting (should show "No changes")
  - Screenshot any help text or tooltips
- Find ALL sync-related settings:
  - Channel management section
  - Booking.com connection configuration
  - Inventory update settings
  - Any "auto-import" or "auto-sync" options
- Take screenshots of EVERYTHING sync-related

#### Task A3: Check Booking.com Connection Status

- Navigate to channel management / integrations / OTA connections
- Find Booking.com entry
- Document:
  - Connection type (should be "Two-Way XML")
  - Connection status (Active/Error/Warning?)
  - Last sync timestamp (if visible)
  - Number of transactions (if visible)
  - Any error messages or warnings
- Screenshot the connection status page

#### Task A4: Search for "Auto-Import"

- Use HotelRunner's search function (if exists)
- Manually browse ALL settings sections
- Check: Settings, Tools, Advanced, Channel Management, Reports
- If found: Screenshot location + current configuration
- If NOT found: List all sections you searched (prove thorough investigation)

#### Task A5: Review Recent Reservations

- Navigate to reservations list
- Filter to show last 30 days
- Identify:
  - Reservations from Booking.com (source should indicate channel)
  - Internal reservations (source "Online" or "Manual" or similar)
  - Any reservations after December 8, 2024 (date of "last import")
- Take screenshots of reservation list showing sources
- Note: Do we have recent internal reservations to test with?

#### Task A6: Documentation Research

- Search HotelRunner Knowledge Base / Help Center for:
  - "Allocation Type"
  - "Inventory sync"
  - "Availability sync"
  - "Two-Way XML"
  - "Auto-import"
  - "Booking.com integration"
- Capture relevant articles (screenshot or save URL)
- Extract key information about how sync works

---

### PHASE B: Testing (OPTIONAL - Only if Omar Explicitly Approves)

**CRITICAL:** Do NOT proceed with Phase B unless Omar says "YES, proceed with testing."

**Omar must specify:**

- Which room type to use (prefer one with multiple units to minimize risk)
- Future date to use (suggest March 2025 or later)

**Test Protocol (if approved):**

1. **Document Pre-Test State:**
   - Screenshot HotelRunner availability calendar for chosen room type
   - Screenshot Booking.com calendar for same room type (if accessible)
   - Note timestamp

2. **Create Test Internal Reservation:**
   - Use HotelRunner interface
   - Create reservation:
     - Guest name: "TEST - DELETE ME"
     - Room type: [Omar specifies]
     - Dates: [Omar specifies, suggest far future]
     - Source: "Online" or "Manual" or whatever creates internal reservation
   - Confirm reservation created
   - Note reservation ID
   - Screenshot confirmation

3. **Wait & Observe:**
   - Wait 15 minutes
   - Check HotelRunner: Does reservation appear correctly?
   - Check Booking.com (if accessible): Did availability decrease?
   - Wait additional 15 minutes (total 30 min)
   - Check again

4. **Document Results:**
   - Screenshot HotelRunner calendar after test
   - Screenshot Booking.com calendar after test (if accessible)
   - Note exact times: Reservation created, first check, second check
   - Document outcome: Synced / Not synced / Partial sync

5. **Clean Up:**
   - **IMMEDIATELY** cancel/delete the test reservation
   - Verify deletion
   - Verify calendars return to original state

**If sync does NOT work:**

- You've confirmed the problem persists (valuable finding)

**If sync DOES work:**

- Support may have fixed it, or setting changed, or we misunderstood

---

### PHASE C: External Research (30-60 min)

**Research Questions:**

1. **What is "Allocation Type" in channel managers?**
   - Web search: "channel manager allocation type meaning"
   - Web search: "HotelRunner allocation type no changes"
   - Look for: Official docs, industry forums, competitor docs

2. **How does Booking.com XML sync work?**
   - Web search: "Booking.com XML integration push pull"
   - Web search: "Booking.com channel manager sync mechanism"
   - Understand: Push vs Pull, who initiates updates, typical sync frequency

3. **What could cause internal reservations to not sync?**
   - Web search: "channel manager internal reservations not syncing OTA"
   - Web search: "HotelRunner Booking.com sync issues"
   - Look for: Known bugs, common misconfigurations, troubleshooting guides

4. **What is "Auto-import"?**
   - Web search: "HotelRunner auto-import feature"
   - Check: Is it a real feature? Deprecated? Renamed?

**Document all findings with:**

- Source URL
- Key quote (short excerpt)
- Your interpretation (does this explain our issue?)

---

### PHASE D: Sub-Agent Consultation (If Needed)

**If investigation reveals technical complexity beyond browser-level investigation:**

Consider spawning `deep-research-agent` (from `.claude/agents/`) to:

- Research HotelRunner API documentation (if publicly available)
- Understand XML sync protocols (SOAP vs REST, push vs pull)
- Find technical specifications for Booking.com channel manager integration

**Coordinate findings back to this main investigation.**

---

## DELIVERABLE: INVESTIGATION REPORT

**You MUST deliver report in this EXACT format:**

```markdown
# HOTELRUNNER SYNC INVESTIGATION REPORT

**Date:** 2025-01-09
**Investigator:** Claude Code + Browser Agent
**Duration:** [X hours]
**Testing Performed:** [YES/NO]

---

## EXECUTIVE SUMMARY

[2-3 sentences: What's the issue, what we found, what we recommend]

---

## FINDINGS

### F1: Allocation Type Setting

**Current Value:** [e.g., "No changes"]
**Location in UI:** [exact navigation path, e.g., Settings > Channels > Booking.com > Advanced]
**Screenshot:** [filename or description]

**What it Controls (based on investigation):**
[Explain what this setting does, based on docs/research]

**Support Team Advice:**
"Leave as 'No changes' or inventory won't update"

**Our Understanding:**
[Does Support's advice make sense? Why/why not?]

**Confidence:** [HIGH/MEDIUM/LOW]

---

### F2: Auto-Import Feature

**Found:** [YES/NO]

**If YES:**

- **Location:** [exact path in UI]
- **Current Status:** [Active/Inactive/Configured how?]
- **Last Run:** [timestamp if visible]
- **Configuration:** [describe settings]

**If NO:**

- **Sections Searched:** [list everywhere you looked]
- **Possible Explanations:** [why might it not be visible? deprecated? renamed?]

**Confidence:** [HIGH/MEDIUM/LOW]

---

### F3: Current Sync Status

**Booking.com Connection:**

- **Type:** [Two-Way XML / other]
- **Status:** [Active / Error / Warning]
- **Last Sync:** [timestamp if available, else "Not visible"]
- **Transaction Log:** [any recent activity visible?]
- **Error Messages:** [any warnings/errors? or "None visible"]

**Screenshot:** [filename]

**Confidence:** [HIGH/MEDIUM/LOW]

---

### F4: Test Results (if testing was performed)

**Testing Approved:** [YES/NO]

**If YES:**

- **Test Reservation Created:** [date, room type, guest name, reservation ID]
- **HotelRunner Updated:** [YES/NO, screenshot]
- **Booking.com Updated:** [YES/NO/UNKNOWN, screenshot if accessible]
- **Sync Delay:** [immediate / 15 min / 30 min / never]
- **Cleanup Performed:** [test reservation deleted? YES/NO]

**Conclusion from Test:** [Does sync work or not?]

**Confidence:** [HIGH/MEDIUM/LOW]

---

### F5: Documentation & Research Findings

**Key Finding 1: Allocation Type Meaning**

- **Source:** [URL or "HotelRunner Knowledge Base"]
- **Quote:** "[relevant excerpt]"
- **Interpretation:** [what this means for our issue]

**Key Finding 2: Booking.com XML Sync Mechanism**

- **Source:** [URL]
- **Quote:** "[excerpt]"
- **Interpretation:** [push vs pull? who initiates?]

**Key Finding 3: Common Sync Issues**

- **Source:** [URL or forum]
- **Quote:** "[excerpt]"
- **Interpretation:** [relevant to our problem?]

[Add more findings as needed]

**Confidence:** [HIGH/MEDIUM/LOW for overall research]

---

## ROOT CAUSE ANALYSIS

**What We Believe Is Happening:**
[Synthesize findings into coherent explanation of sync mechanism]

**Why Internal Reservations Might Not Sync:**
[Hypothesis based on all evidence gathered]

**Alternative Explanations:**
[Other possibilities we can't rule out]

**Overall Confidence:** [HIGH/MEDIUM/LOW]

---

## RECOMMENDATIONS

### Recommendation 1: [Primary Action]

**What:** [Specific action to take, e.g., "Change Allocation Type to X" or "Leave as is"]
**Why:** [Rationale based on findings]
**Risk:** [LOW/MEDIUM/HIGH]
**How:** [Step-by-step if applicable]
**Expected Outcome:** [What should happen after doing this]

---

### Recommendation 2: [Secondary Action or Alternative]

**What:** [Another action to consider]
**Why:** [Rationale]
**Risk:** [LOW/MEDIUM/HIGH]
**How:** [Steps]
**Expected Outcome:** [Result]

---

### Recommendation 3: [Fallback/Contingency]

**If recommendations 1 & 2 don't work:**
[Plan B, e.g., "Manual calendar management until HotelRunner Support escalates"]

---

## SAFE TO PROCEED WITH OTA ACTIVATION?

**YES / NO / CONDITIONAL**

**Rationale:**
[Based on findings, is it safe to activate 4-5 more OTAs now, or should we wait/fix something first?]

**If CONDITIONAL, what must happen first:**
[List prerequisites]

---

## UNANSWERED QUESTIONS

[List anything still unclear after investigation]

1. [Question 1]
2. [Question 2]
3. [etc.]

---

## NEXT STEPS

**Immediate (TODAY):**

1. [Action for Omar/Lux]
2. [Action for Claude Code]

**Before OTA Activation (TOMORROW):**

1. [Action]
2. [Action]

**Ongoing Monitoring:**

1. [What to watch for]
2. [How to verify sync working]

---

## APPENDIX A: SCREENSHOTS

[List all screenshots taken with brief description]

1. Screenshot 1: [Description]
2. Screenshot 2: [Description]
3. [etc.]

**Note:** Screenshots should be saved in: `/home/claude/investigation-screenshots/` or attached to this report.

---

## APPENDIX B: SOURCES CONSULTED

[List all documentation and web sources]

1. [Source name/URL] - [What we learned]
2. [Source name/URL] - [What we learned]
3. [etc.]

---

## APPENDIX C: INVESTIGATION TIMELINE

[Log of investigation activities with timestamps]

- [HH:MM] Started investigation, accessed HotelRunner admin
- [HH:MM] Located Allocation Type setting
- [HH:MM] Searched for Auto-import feature
- [HH:MM] Completed documentation research
- [HH:MM] [Testing phase if performed]
- [HH:MM] Finalized report

**Total Duration:** [X hours Y minutes]

---

## INVESTIGATOR SIGN-OFF

**Prepared by:** Claude Code  
**Review Required:** Lux + Omar  
**Confidence in Findings:** [HIGH/MEDIUM/LOW]  
**Ready for Decision:** [YES/NO]

If NO, explain what additional investigation needed:
[Explanation]

---

**END OF REPORT**
```

---

## SUCCESS CRITERIA

**Your investigation is COMPLETE when:**

✅ Report follows template exactly (all sections filled)  
✅ You've documented "Allocation Type" location and meaning  
✅ You've either found "Auto-import" OR proven it doesn't exist in UI  
✅ You understand WHY Support said "leave it as is"  
✅ You have clear recommendation (what to do next)  
✅ You've stated whether it's SAFE to activate more OTAs  
✅ Confidence level for overall findings is at least MEDIUM (not LOW)

**Your investigation is SUCCESSFUL when:**

✅ Omar + Lux can make informed decision after reading report  
✅ Recommendation is actionable (not "we need more info")  
✅ Risk is quantified (we know what could go wrong)  
✅ Timeline impact is clear (can we proceed tomorrow or need to wait?)

---

## WHAT OMAR WILL PROVIDE

**Credentials:**

- HotelRunner admin login (username + password)
- Booking.com extranet login (if needed for cross-check)

**Testing Approval:**

- Explicit YES/NO for Phase B (test reservation creation)
- If YES: Room type to use + date range

**Omar will provide these when you're ready to start.**

---

## IMPORTANT NOTES

**Browser Agent Best Practices:**

- Take screenshots liberally (easier to review later than re-access)
- Use clear, systematic navigation (don't skip around randomly)
- If you hit an error, document it (don't just retry silently)
- If you find something unexpected, flag it explicitly

**Time Management:**

- Phase A (gathering): 30-60 min
- Phase B (testing, if approved): 30-45 min
- Phase C (research): 30-60 min
- Report writing: 30-45 min
- **Total: 2-4 hours** (depending on testing)

**If You Get Stuck:**

- Document what blocked you
- Try alternative paths (e.g., different sections of UI)
- Spawn sub-agent if needed (deep-research-agent for technical depth)
- Report partial findings rather than giving up

**Communication:**

- Progress updates appreciated (e.g., "Completed Phase A, starting research")
- If you discover something CRITICAL mid-investigation, flag it immediately
- If you need Omar's input (e.g., approve testing), ask explicitly

---

## CONTEXT FILES (Reference if Needed)

**In Villa Thaifa Repo:**

- `docs/reports/2025-12-29-sync-investigation.md` (previous investigation findings)
- `data/operations/hotelrunner/` (HotelRunner configuration docs)
- `data/operations/booking/` (Booking.com data)

**In Current Workspace:**

- `/mnt/user-data/outputs/villa-thaifa-workstream-master-v0.1.0.md` (this mission is Section 4)
- Previous support request text (included in context above)

---

## FINAL CHECKLIST BEFORE STARTING

Before you begin investigation, verify you have:

- [ ] HotelRunner credentials from Omar
- [ ] Clear understanding of mission (read this entire prompt)
- [ ] Report template ready (you'll fill it progressively)
- [ ] Browser agent functional and ready
- [ ] Screenshot capability working
- [ ] Approval status for Phase B testing (YES/NO from Omar)

**If all checked, BEGIN INVESTIGATION.**

**When complete, deliver report to Omar in the format specified above.**

---

**Good luck, Claude Code. This investigation is P0 - CRITICAL for Villa Thaifa's success.**

**— Lux**

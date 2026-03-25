# Villa Thaifa — Project Brief

**Version:** 0.2.0-alpha.0  
**Date:** 2026-01-09  
**Type:** Technical Execution Guide (For AI Agents)  
**Status:** Ready for Phase 1 Execution

---

## CRITICAL — START HERE

**This Week's Mission:**
```
Villa Thaifa INVISIBLE → Villa Thaifa VISIBLE on 10-15 OTA platforms
"Extrêmement peu de réservations" → Bookings falling in
Said frustrated → Said satisfied
```

**Your Goal:** Execute Phase 1 (OTA Activation) **THIS WEEK**.

**Business Context:** See `villa-thaifa-client-brief-v0.2.0.md`

---

## DOCUMENT MAP

| Need | Section |
|------|---------|
| What's the mission? | [1. Phase 1 Mission](#1-phase-1-mission) |
| What do I do NOW? | [2. This Week Checklist](#2-this-week-checklist) |
| How does the system work? | [3. System Architecture](#3-system-architecture) |
| How do I create OTA accounts? | [4. OTA Platform Setup](#4-ota-platform-setup) |
| How do I configure HotelRunner? | [5. HotelRunner Setup](#5-hotelrunner-setup) |
| What pricing should I use? | [6. Pricing Strategy](#6-pricing-strategy) |
| What content do I need? | [7. Listing Content](#7-listing-content) |
| What workflows? | [8. Operational Workflows](#8-operational-workflows) |
| How do I track success? | [9. KPIs & Monitoring](#9-kpis--monitoring) |
| What's missing (placeholders)? | [10. Placeholders](#10-placeholders) |
| How should agents work? | [11. Agent Execution Protocol](#11-agent-execution-protocol) |

---

## 1. PHASE 1 MISSION

### The Goal (From Najib)

> **"Le concret, c'est stimuler le chiffre d'affaires, le volume d'activité."**

**Translation:** Concrete goal = Stimulate revenue and volume of activity.

### Technical Translation

**Current State:**
- Villa Thaifa invisible on OTA platforms
- "Extrêmement peu de réservations" (quasi-zero)
- House empty ("maison d'hôte vide")
- Said frustrated (waiting 2-3+ weeks)

**Target State (End of This Week):**
- Villa Thaifa visible on 10-15 OTA platforms
- All platforms linked to HotelRunner (channel manager)
- Calendar synchronized (booking on one platform = blocked on all)
- First bookings visible (even for April/May)
- Said sees activity on calendar

### Success Metrics

| Metric | Target | Verification |
|--------|--------|--------------|
| **Active OTA Platforms** | 10-15 | All accounts created and live |
| **HotelRunner Connections** | All platforms | API integrations complete |
| **Calendar Sync** | < 1 minute | Test booking verifies |
| **Visible Bookings** | 1+ | Said sees calendar activity |
| **Said's Satisfaction** | Positive | Najib reports feedback |

### Timeline

**Week 1 (Jan 9-15):** Phase 1 execution (P0)  
**Weeks 2-4:** Optimization and documentation (P1)  
**Month 2+:** "App" vision and scale (P2 - awaiting clarification)

---

## 2. THIS WEEK CHECKLIST

### Monday-Tuesday: Core Platforms

**Booking.com (RECONFIGURE)**
- [ ] Access existing Booking.com account
- [ ] Fix Room Type vs Room Number issue
- [ ] Upload/verify photos
- [ ] Verify pricing
- [ ] Test calendar sync with HotelRunner
- [ ] Mark as LIVE

**Expedia (COMPLETE)**
- [ ] Finish integration started
- [ ] Verify HotelRunner connection
- [ ] Test calendar sync
- [ ] Mark as LIVE

**Airbnb (CREATE)**
- [ ] Create host account
- [ ] Complete property listing
- [ ] Upload photos
- [ ] Set pricing
- [ ] Link to HotelRunner API
- [ ] Test sync
- [ ] Mark as LIVE

### Wednesday-Thursday: Major Platforms

**Priority Platforms (5-7 total):**
- [ ] Agoda (international audience)
- [ ] VRBO (check if auto-connects via Expedia)
- [ ] Hotels.com (Expedia family)
- [ ] TripAdvisor (reputation + bookings)
- [ ] Google Hotels (discoverability)

**For EACH platform:**
1. Create account
2. Complete property profile
3. Upload photos (same set across all)
4. Set baseline pricing
5. Link to HotelRunner
6. Verify calendar sync
7. Test booking flow
8. Mark as LIVE

### Friday: Complete & Verify

**Final Platforms (2-5 more to reach 10-15):**
- [ ] Trivago
- [ ] Trip.com
- [ ] [RESEARCH: 0-3 more Marrakech-prioritized platforms]

**Verification:**
- [ ] All platforms show Villa Thaifa listing
- [ ] Calendar sync test: Book on Platform A → Blocks on Platform B, C, D...
- [ ] At least 1 visible booking on calendar
- [ ] Report results to Omar → Said & Najib

---

## 3. SYSTEM ARCHITECTURE

### How Channel Management Works

```
┌─────────────────────────────────────────────────────────────┐
│  GUEST BOOKS on ANY Platform (e.g., Airbnb)                 │
└──────────────────────────┬──────────────────────────────────┘
                           │
                           ▼
┌─────────────────────────────────────────────────────────────┐
│  HotelRunner Channel Manager (Central Hub)                  │
│  ✓ Receives booking notification                            │
│  ✓ Updates central availability calendar                    │
│  ✓ Blocks room across ALL connected platforms               │
└──────────────────────────┬──────────────────────────────────┘
                           │
                           ▼
┌─────────────────────────────────────────────────────────────┐
│  ALL Connected OTA Platforms                                │
│  ✓ See updated availability in real-time                    │
│  ✓ Cannot double-book (room already blocked)                │
│  ✓ Guests see accurate availability                         │
└─────────────────────────────────────────────────────────────┘
```

**Key Insight (Najib):**
> This is **AUTOMATIC**. Not custom development. HotelRunner does this by default.

### Current Tech Stack

| Component | Status | Purpose |
|-----------|--------|---------|
| **HotelRunner** | ✅ In use (needs reconfig) | Central channel manager |
| **Booking.com** | ⚠️ Connected (needs fix) | Major OTA platform |
| **Expedia** | 🔄 In progress | Major OTA platform |
| **10-13 other OTAs** | 🔴 TO CREATE | Maximize visibility |

### Target Platforms (10-15 Total)

**High Priority (Create First):**
1. Booking.com ✓ (fix)
2. Expedia ✓ (complete)
3. Airbnb 🔴
4. Agoda 🔴
5. VRBO 🔴
6. Hotels.com 🔴

**Medium Priority:**
7. TripAdvisor
8. Google Hotels
9. Trivago
10. Trip.com

**Research Needed (Fill to 15):**
11-15. [PLACEHOLDER: Marrakech-specific OTA platforms research]

---

## 4. OTA PLATFORM SETUP

### Universal OTA Setup Process

**Standard Workflow (Applies to All Platforms):**

#### Step 1: Account Creation
- Go to platform's "List Your Property" page
- Register with business email: [PLACEHOLDER: Villa Thaifa email]
- Verify email
- Complete basic profile

#### Step 2: Property Information
- **Property Name:** Villa Thaifa
- **Address:** [PLACEHOLDER: Complete address from Said]
- **Type:** Maison d'hôte / Guest House / Boutique Hotel
- **Rooms:** [PLACEHOLDER: Number and types from Said]
- **Amenities:** [PLACEHOLDER: Complete list from Said - Section 7]

#### Step 3: Room Configuration
- **Per room:**
  - Room name/number: [From HotelRunner config]
  - Bed type: [PLACEHOLDER: Double, Twin, King?]
  - Capacity: [PLACEHOLDER: Max guests per room]
  - Photos: [PLACEHOLDER: Professional photos needed]
  - Description: [Template in Section 7]

#### Step 4: Pricing & Policies
- **Baseline Pricing:** [Use Section 6 grid]
- **Minimum Stay:** [PLACEHOLDER: Said's preference]
- **Cancellation Policy:** [PLACEHOLDER: Flexible/Moderate/Strict]
- **Check-in/out:** [PLACEHOLDER: Times from Said]

#### Step 5: HotelRunner Integration
- Link platform to HotelRunner via API
- Verify bidirectional sync
- Test: Create booking → Check calendar updates
- Confirm: Booking on Platform A blocks on Platform B

#### Step 6: Go Live
- Review listing
- Enable booking
- Monitor first 24 hours for sync issues
- Mark as ✅ LIVE

---

### Platform-Specific Notes

#### Booking.com ⚠️

**Status:** Connected but needs reconfiguration

**Issue:** Room Type (grouped) vs Room Number (individual)
- **Current:** Room Type approach (all "Standard Doubles" pooled)
- **Said Prefers:** Room Number approach (Room 1, Room 2, Room 3 individual)
- **Action:** Reconfigure OR adapt (don't block launch)

**HotelRunner Integration:**
- API: https://developers.hotelrunner.com
- Already connected (verify status)
- Test sync thoroughly

**Priority:** 🔴 CRITICAL (Booking.com = major global source)

---

#### Airbnb 🔴

**Status:** Needs creation (HIGH priority)

**Airbnb Specifics:**
- **Booking Type:** Instant Book vs Request to Book [PLACEHOLDER: Said's preference]
- **House Rules:** [PLACEHOLDER: Villa Thaifa rules - Section 7]
- **Check-in Method:** Self check-in? Greeter? [PLACEHOLDER]

**HotelRunner Integration:**
- Use HotelRunner's Airbnb channel
- **WARNING:** Airbnb known for sync issues - test extensively
- Verify: Booking on Airbnb → Blocks on Booking.com, Expedia, etc.

**Priority:** 🔴 CRITICAL (Different audience, major platform)

---

#### Expedia / Hotels.com / VRBO 🔄

**Status:** Expedia in progress

**Expedia Family Strategy:**
- **Expedia:** Main platform (finish integration)
- **Hotels.com:** Often auto-connects via Expedia (verify)
- **VRBO:** Vacation rental focus (may require separate or auto-connects)

**Action:**
1. Complete Expedia integration
2. Check if Hotels.com automatically added
3. Verify VRBO status (good fit for maison d'hôte)

**Priority:** 🔴 CRITICAL (Expedia group = massive reach)

---

#### Agoda 🔴

**Status:** Needs creation

**Agoda Benefits:**
- Strong in Asia + international travelers
- Good for Marrakech tourist market
- Competitive commission rates

**Priority:** 🔴 HIGH (international audience)

---

#### TripAdvisor 🟡

**Status:** Needs creation

**TripAdvisor Value:**
- Review platform + booking capability
- Reputation management critical
- Drives traffic even without direct booking

**Priority:** 🟡 MEDIUM (reputation value)

---

#### Google Hotels 🟡

**Status:** Needs setup

**Google Hotels Setup:**
- Not direct booking, aggregator
- Requires Google Business Profile
- Links to other platforms or direct site
- Excellent for SEO and discoverability

**Priority:** 🟡 MEDIUM-HIGH (search visibility)

---

### Platform Priority Matrix

| Platform | Priority | Reason | Action |
|----------|----------|--------|--------|
| Booking.com | 🔴 P0 | Global leader | Fix & verify |
| Expedia | 🔴 P0 | Major group | Complete |
| Airbnb | 🔴 P0 | Different audience | Create |
| Agoda | 🔴 P0 | International | Create |
| VRBO | 🔴 P1 | Vacation rentals | Check auto-connect or create |
| Hotels.com | 🔴 P1 | Expedia family | Check auto-connect |
| TripAdvisor | 🟡 P1 | Reputation | Create |
| Google Hotels | 🟡 P1 | Discoverability | Setup |
| Trivago | 🟡 P2 | Aggregator | Research value |
| Trip.com | 🟡 P2 | Asia focus | Research value |

---

## 5. HOTELRUNNER SETUP

### What is HotelRunner?

**Channel Manager Definition:**
> Centralized platform that links property to 150+ OTAs, synchronizes availability/pricing/bookings in real-time to prevent double-bookings.

**HotelRunner Features:**
- 150+ OTA integrations
- Real-time calendar sync (< 1 minute)
- Centralized pricing management
- Commission tracking
- Analytics and reporting

**Docs:** https://hotelrunner.com/en/ & developers.hotelrunner.com

---

### Current HotelRunner Status

**What Exists:**
- ✅ HotelRunner account (already in use)
- ✅ Booking.com connection (needs reconfiguration)
- 🔄 Expedia connection (in progress)

**What's Needed:**
- [ ] Room configuration audit/fix
- [ ] Baseline pricing setup (4 seasons)
- [ ] 8-13 additional OTA connections
- [ ] Calendar sync verification across all platforms

---

### Room Configuration Fix

**The Issue:**
- **Booking.com approach:** Room Type (e.g., "Standard Double" as a pool)
- **HotelRunner capability:** Room Number (e.g., "Room 1", "Room 2", "Room 3")
- **Said's preference:** Room Number approach

**Resolution Options:**

| Option | Pros | Cons | Recommendation |
|--------|------|------|----------------|
| **A. Reconfigure Booking.com to Room Number** | Aligns with Said's preference, consistent across all platforms | May lose existing Booking.com reservations during migration | ✅ IF no existing bookings |
| **B. Keep Booking.com as Room Type, others as Room Number** | No disruption to Booking.com | Mixed approach, inconsistent | ⚠️ Acceptable short-term |
| **C. All platforms use Room Type** | Consistent, simpler | Abandons Said's preference | ❌ Not recommended |

**Decision Required:** [PLACEHOLDER: Confirm with Said which option]

**Don't Block Launch:** Use whichever approach works NOW. Migrate later if needed.

---

### HotelRunner API Integration

**For Each OTA Platform:**

1. **Authenticate:** HotelRunner ↔ OTA platform
2. **Map Inventory:** Villa Thaifa rooms ↔ OTA room types
3. **Enable Sync:** Bidirectional (HotelRunner ↔ OTA)
4. **Test Booking Flow:**
   - Create test reservation on OTA
   - Verify HotelRunner receives notification
   - Verify calendar blocks room
   - Verify other OTAs see room as unavailable
5. **Monitor:** Check sync errors in HotelRunner dashboard

**API Credentials:** [PLACEHOLDER: Access from Said or existing HotelRunner config]

---

### Pricing Management in HotelRunner

**Setup Baseline Pricing:**
- [ ] Define 4 seasons (Section 6)
- [ ] Set price per season per room type
- [ ] Configure minimum stay rules (if any)
- [ ] Set cancellation policies per platform (if different)

**Advanced Pricing (Phase 2):**
- Last-minute discounts (fill gaps)
- Long-stay discounts (7+ nights)
- Early-bird discounts (60+ days advance)
- Derived rates (single = 80% of double)

**For Now:** Keep it SIMPLE. Baseline pricing only. Optimize in Phase 2.

---

### Calendar Sync Verification

**Critical Test Sequence:**

1. **Create Test Booking:**
   - Book Room 1 on Booking.com for Jan 20-22
   - Note timestamp

2. **Verify HotelRunner:**
   - Check HotelRunner dashboard
   - Room 1 should show blocked Jan 20-22
   - Verify booking details received

3. **Verify Other Platforms:**
   - Check Airbnb: Room 1 unavailable Jan 20-22
   - Check Expedia: Room 1 unavailable Jan 20-22
   - Check Agoda: Room 1 unavailable Jan 20-22
   - Check ALL connected platforms

4. **Verify Sync Speed:**
   - Sync should complete in < 1 minute
   - If > 1 minute, investigate (still acceptable if < 5 min)

5. **Test Cancellation:**
   - Cancel test booking
   - Verify Room 1 unblocked on ALL platforms

6. **Repeat for Each Room:**
   - Test all room numbers/types
   - Verify no sync failures

**If Sync Fails:**
- Check HotelRunner API connection status
- Verify OTA platform credentials
- Review HotelRunner sync logs
- Contact HotelRunner support: [PLACEHOLDER: Support contact info]

---

## 6. PRICING STRATEGY

### Najib's Philosophy

> **"Les prix, ça peut se changer à n'importe quel moment. Ça, c'est un travail d'une heure."**

**Translation:** Prices changeable anytime. This is 1 hour of work.

**Meaning:**
- DON'T let pricing block launch
- START with competitive baseline
- OPTIMIZE based on real booking data
- ADJUST continuously (not one-time perfection)

---

### Marrakech 4 Seasons

**Standard Seasonality (Marrakech):**

| Season | Typical Period | Demand Level | Pricing Strategy |
|--------|----------------|--------------|------------------|
| **Très haute saison** | [RESEARCH: Dec-Jan? Mar-Apr?] | Highest | Base price × 1.0 |
| **Haute saison** | [RESEARCH: Shoulder months] | High | Base price × 0.80-0.85 |
| **Moyenne saison** | [RESEARCH: Moderate periods] | Medium | Base price × 0.65-0.70 |
| **Basse saison** | [RESEARCH: Jun-Aug hot months?] | Low | Base price × 0.50-0.60 |

**[RESEARCH NEEDED: Verify exact dates from:**
- Marrakech tourism board data
- Competitor analysis (5-10 similar properties)
- HotelRunner's Marrakech market insights]

---

### "1 Hour" Baseline Pricing Implementation

**Step 1: Competitive Research (15-20 min)**

**Find 3-5 comparable properties:**
- Similar: Maison d'hôte, Marrakech location, room count
- Record: Pricing per season
- Note: Photos quality, amenities, reviews

**Comparison Table:**

| Property | Very High Season | High Season | Mid Season | Low Season |
|----------|-----------------|-------------|------------|-----------|
| Competitor A | €X | €Y | €Z | €W |
| Competitor B | €X | €Y | €Z | €W |
| Competitor C | €X | €Y | €Z | €W |
| **Median** | **€[calc]** | **€[calc]** | **€[calc]** | **€[calc]** |

---

**Step 2: Position Villa Thaifa (5-10 min)**

**Decision Matrix:**

| Positioning | When to Use | Pricing vs Median |
|-------------|-------------|-------------------|
| **Match Median** | Standard quality, build occupancy | = Median |
| **Undercut 10-15%** | Quick occupancy, new listing | Median × 0.85-0.90 |
| **Premium +10-15%** | Superior amenities, established reputation | Median × 1.10-1.15 |

**Villa Thaifa Positioning:** [PLACEHOLDER: Said's preference? Recommend: Match or slight undercut to build initial occupancy]

---

**Step 3: Set Seasonal Grid (10 min)**

**Example (Using Match Median Strategy):**

| Season | Price per Night (€) | Notes |
|--------|---------------------|-------|
| Très haute | €[Median from research] | Peak demand, events, holidays |
| Haute | €[Très haute × 0.80] | Strong demand, good weather |
| Moyenne | €[Très haute × 0.65] | Moderate demand |
| Basse | €[Très haute × 0.50] | Fill occupancy, low season |

---

**Step 4: Configure in HotelRunner (10 min)**

**Actions:**
- [ ] Log into HotelRunner dashboard
- [ ] Navigate to Pricing Management
- [ ] Define 4 seasons with date ranges
- [ ] Set price per season per room type
- [ ] Save and publish
- [ ] Verify prices pushed to all OTA platforms

**Total Time:** ~45-60 minutes (exactly as Najib said: "1 hour work")

---

### Quick Start Pricing (If Research Pending)

**Use HotelRunner's Defaults:**
- HotelRunner often provides market-based pricing suggestions
- Use these as temporary baseline
- Research and refine within first week
- **Don't let this block launch**

**OR Use Najib's 40 Years Experience:**
- Ask Najib for ballpark pricing (he knows Marrakech luxury market)
- Quick expert input > Weeks of analysis
- Launch with expert baseline, optimize with data

---

## 7. LISTING CONTENT

### Content Checklist (ALL Platforms Need This)

**Essential Content:**
- [ ] Property title (compelling, clear)
- [ ] Property description (FR + EN minimum)
- [ ] Room descriptions (per room type)
- [ ] Amenities list (complete)
- [ ] House rules
- [ ] Check-in/out instructions
- [ ] Professional photos (critical)

---

### Property Title Template

**Formula:** `[Property Name] - [Type] - [Key Feature] - [Location]`

**Examples:**
- "Villa Thaifa - Authentique Maison d'Hôte - Cœur de Marrakech"
- "Villa Thaifa - Boutique Guest House - Traditional Marrakech Charm"
- "Villa Thaifa - Luxury Riad Experience - Medina Proximity"

**Languages:**
- French (primary)
- English (required)
- [PLACEHOLDER: Arabic? German? Spanish? Based on target markets]

---

### Property Description Template

**Structure (2-3 paragraphs):**

```markdown
## [OPENING HOOK - 2-3 sentences]
Villa Thaifa vous accueille dans une authentique maison d'hôte marocaine au cœur de Marrakech. [Unique selling point]. [Guest experience promise].

## [ACCOMMODATION - 1 paragraph]
Notre maison d'hôte dispose de [X] chambres [description]. [Bed types, capacity]. [Unique features: terrace, traditional decor, etc.].

## [AMENITIES - Bullet list]
- WiFi haut débit gratuit
- Climatisation dans toutes les chambres
- [Other amenities]

## [LOCATION - 1 paragraph]
Idéalement situé à [distance] de [medina/souks/attractions]. [Neighborhood character]. [Transport options].

## [HOSPITALITY - 1 sentence]
[Host name/Ikram?] sera ravi(e) de vous accueillir et de partager ses recommandations locales.
```

**Content Needed:**
- [PLACEHOLDER: X number of rooms]
- [PLACEHOLDER: Room types and bed configurations]
- [PLACEHOLDER: Unique features - terrace? pool? garden?]
- [PLACEHOLDER: Complete amenities list]
- [PLACEHOLDER: Exact distance to medina/souks]
- [PLACEHOLDER: Host name - Said? Ikram?]

---

### Room Descriptions Template

**Per Room Type:**

```markdown
### [Room Name/Number] - [Room Type]

[2-3 sentences describing room character, view, unique features]

**Accommodations:**
- [Bed type: King, Queen, Twin, etc.]
- Sleeps [X] guests comfortably
- [Room size if known: X m²]

**Amenities:**
- Private bathroom with [shower/bathtub]
- [Air conditioning / Heating / Fan]
- [Balcony / Terrace / Window view]
- [Work desk if applicable]
- [Other room-specific amenities]

**Perfect for:** [Couples / Families / Solo travelers / Business travelers]
```

**Repeat for each room type.**

---

### Amenities List (Complete)

**Property-wide Amenities:**

**Internet & Communication:**
- [ ] WiFi (speed: [PLACEHOLDER: Mbps])
- [ ] Work-friendly (dedicated workspace? [PLACEHOLDER])

**Climate Control:**
- [ ] Air conditioning (which rooms? [PLACEHOLDER])
- [ ] Heating (which rooms? [PLACEHOLDER])

**Bathroom:**
- [ ] Hot water
- [ ] Towels provided
- [ ] Toiletries provided
- [ ] Hairdryer

**Kitchen & Dining:**
- [ ] Breakfast included (type: [PLACEHOLDER: Continental? Moroccan?])
- [ ] Kitchen access (shared/private/none: [PLACEHOLDER])
- [ ] Dining area
- [ ] Coffee/tea facilities

**Outdoor Spaces:**
- [ ] Terrace (private/shared: [PLACEHOLDER])
- [ ] Garden (if applicable: [PLACEHOLDER])
- [ ] Pool (if applicable: [PLACEHOLDER])

**Services:**
- [ ] Daily housekeeping
- [ ] Laundry service (extra cost: [PLACEHOLDER])
- [ ] Airport transfer (available/cost: [PLACEHOLDER])
- [ ] Luggage storage

**Parking:**
- [ ] On-site parking (free/paid: [PLACEHOLDER])
- [ ] Nearby parking options: [PLACEHOLDER]

**Family Features:**
- [ ] Children welcome
- [ ] Crib available (on request: [PLACEHOLDER])
- [ ] High chair available: [PLACEHOLDER]

**Accessibility:**
- [ ] Ground floor rooms (if applicable: [PLACEHOLDER])
- [ ] Accessibility features: [PLACEHOLDER]

**Other:**
- [ ] Languages spoken: [PLACEHOLDER: French, English, Arabic?]
- [ ] TV (if applicable)
- [ ] Books/games
- [ ] Traditional Moroccan décor

**[PLACEHOLDER: Complete amenities list from Said/Ikram]**

---

### House Rules Template

**Essential Rules:**

```markdown
## Check-in / Check-out
- Check-in: [PLACEHOLDER: Time - e.g., 14:00-18:00]
- Check-out: [PLACEHOLDER: Time - e.g., 11:00]
- Late check-in/early check-out: [PLACEHOLDER: Available? Fee?]

## Policies
- Smoking: [PLACEHOLDER: Allowed/Not allowed/Outdoor only]
- Pets: [PLACEHOLDER: Allowed/Not allowed]
- Events/Parties: [PLACEHOLDER: Allowed/Not allowed]
- Quiet hours: [PLACEHOLDER: e.g., 22:00-08:00]

## Guests
- Maximum occupancy: [X] guests per room
- Additional guests: [PLACEHOLDER: Allowed? Fee?]
- Children: [PLACEHOLDER: Welcome/Age restrictions?]
- Visitors: [PLACEHOLDER: Day visitors allowed?]

## Respect & Safety
- Please respect property and neighbors
- No smoking inside rooms
- [Other specific rules]

## Cancellation
- [PLACEHOLDER: Policy - Flexible/Moderate/Strict]
- See platform-specific terms for details
```

**[PLACEHOLDER: All house rules from Said]**

---

### Professional Photos (CRITICAL)

**Required Shots (Minimum):**

**Exterior:**
- [ ] Facade (daytime)
- [ ] Facade (evening/lit)
- [ ] Entrance
- [ ] Street view/location context

**Interior - Common Areas:**
- [ ] Living room (multiple angles)
- [ ] Dining area
- [ ] Breakfast area
- [ ] Terrace/outdoor space (if applicable)
- [ ] Pool (if applicable)
- [ ] Architectural details (Moroccan style highlights)

**Rooms (Per Room Type):**
- [ ] Room overview (wide angle)
- [ ] Bed (close-up, styled)
- [ ] Seating area (if applicable)
- [ ] Bathroom (clean, bright)
- [ ] Room-specific features (balcony, view, etc.)

**Quality Standards:**
- ✅ Professional photographer (NOT smartphone snapshots)
- ✅ Natural light preferred
- ✅ Clean, styled spaces
- ✅ 4:3 or 16:9 aspect ratio
- ✅ Minimum 1920×1080 resolution
- ✅ No filters (authentic representation)

**Total Photos Needed:** 20-40 high-quality images

**Status:** [PLACEHOLDER: Do professional photos exist? If not, schedule photoshoot IMMEDIATELY - this is CRITICAL]

---

## 8. OPERATIONAL WORKFLOWS

### Booking Flow (Automated)

**1. Guest Discovery & Booking:**
- Guest searches "Marrakech maison d'hôte" on OTA
- Finds Villa Thaifa listing
- Selects dates, room, guests
- Completes payment (OTA processes)

**2. HotelRunner Processing:**
- Receives booking notification from OTA
- Logs booking details
- Updates calendar (blocks room)
- Syncs to ALL connected OTAs (< 1 min)
- [OPTIONAL: Triggers automated email to Said/Ikram]

**3. Guest Communication:**
- OTA sends confirmation to guest
- [PLACEHOLDER: Does HotelRunner send additional details?]
- [PLACEHOLDER: Who sends check-in instructions? Said? Ikram? Automated?]

**4. Pre-Arrival (2-3 days before):**
- [PLACEHOLDER: Who sends?] Welcome email with:
  - Check-in time and procedure
  - Address and directions
  - WiFi password
  - Local recommendations
  - Emergency contact

**5. Check-in:**
- [PLACEHOLDER: Who manages?] Greets guest
- Welcome orientation
- Provide keys
- House tour

**6. During Stay:**
- Guest support for questions/issues
- [PLACEHOLDER: Housekeeping schedule?]
- [PLACEHOLDER: Breakfast service?]

**7. Check-out:**
- [PLACEHOLDER: Process?] Checks room
- Thanks guest
- Requests review

**8. Post-Stay:**
- Review guest's review (if left)
- Respond publicly if needed
- Calendar ready for next guest

**[PLACEHOLDER: Complete operational workflow from Said/Ikram]**

---

### Problem Resolution Workflow

**Booking Issues:**
- Double-booking (shouldn't happen, but if it does):
  - **Escalate:** Omar → Check HotelRunner sync logs
  - **Resolve:** Alternative accommodation or partial refund
- Guest cancellation:
  - **Auto:** HotelRunner unblocks room on all platforms
  - **Manual:** Verify unblocked, adjust pricing if needed

**Technical Issues:**
- HotelRunner sync failure:
  - Check API connection status
  - Review sync logs
  - Contact HotelRunner support
- OTA platform outage:
  - Monitor platform status page
  - Inform affected guests if needed
- Payment problems:
  - OTA handles payments (not Villa Thaifa)
  - Contact OTA support

**Guest Issues:**
- Complaint or problem during stay:
  - **Respond:** [Said/Ikram?] addresses immediately
  - **Log:** Document for future improvement
  - **Compensate:** If warranted (Najib's hospitality expertise can guide)

**Escalation Path:**
- **Technical:** Omar
- **Hospitality/Operations:** Najib (40 years expertise)
- **Business Decision:** Said

---

## 9. KPIS & MONITORING

### Primary Metrics (Track Weekly)

| Metric | Target (Week 1) | How to Measure | Why Important |
|--------|-----------------|----------------|---------------|
| **Active OTA Platforms** | 10-15 | Count of live connections | Visibility = bookings |
| **Visible Bookings** | 1+ | Calendar shows activity | Said's satisfaction indicator |
| **Chiffre d'affaires** | Increase weekly | Total booking value (€) | Primary business goal (Najib) |
| **Booking Volume** | 3-5+ | Count of reservations | Volume of activity (Najib) |
| **Occupancy Rate** | 15%+ initially | Booked nights / available | Industry standard metric |

### Technical Health Metrics

| Metric | Target | Action if Below Target |
|--------|--------|------------------------|
| **HotelRunner Uptime** | 99%+ | Check status page, escalate if down |
| **Calendar Sync Speed** | < 1 minute | Investigate if > 5 minutes |
| **API Connection Status** | All green | Reconnect failed connections |
| **Double-booking Incidents** | 0 | Emergency: Manual resolution + sync audit |
| **Sync Failures** | 0 | Review logs, fix integration |

### Platform Performance (Track After 2 Weeks)

**Compare platforms to identify best performers:**

| Platform | Bookings | Revenue | Average Stay | Conversion Rate |
|----------|----------|---------|--------------|-----------------|
| Booking.com | X | €X | X nights | X% |
| Airbnb | X | €X | X nights | X% |
| Expedia | X | €X | X nights | X% |
| ... | ... | ... | ... | ... |

**Use this to:**
- Optimize listings on high-performing platforms
- Adjust pricing per platform if needed
- Decide which platforms to prioritize for updates

### Said Satisfaction Indicators (Qualitative)

**Critical Success Signals:**
- ✅ Said sees calendar with bookings (visual proof)
- ✅ Said stops complaining about "zero clients"
- ✅ Said expresses satisfaction to Najib
- ✅ Said recommends Villa Thaifa service to other owners (future clients!)
- ✅ Najib reports positive feedback

**Warning Signals:**
- ⚠️ Said still frustrated after Week 1
- ⚠️ Calendar shows no activity
- ⚠️ Najib reports continued concerns
- ⚠️ Trust further eroding

---

## 10. PLACEHOLDERS

### [REPO] — Awaiting Repository Package

**Status:** ⏳ Omar will provide repomix package

**Once received, extract:**
- [ ] Current Villa Thaifa data (in `data/` directory)
- [ ] Existing room configurations
- [ ] Any HotelRunner integration code
- [ ] Documentation structure
- [ ] "Bordel" assessment (what needs cleanup?)
- [ ] Reusable patterns for future clients

**Will inform:**
- Room configuration details
- Existing vs needed documentation
- Code refactoring priorities
- EaC migration path

---

### [APP] — Awaiting Omar's Vision Clarification

**Status:** ⏳ Omar will clarify after providing repo

**Questions:**
- What is "transform to app"? (Web app? Mobile? Automation?)
- Who are the users? (Said? Ikram? Guests? Future clients?)
- Core features needed?
- Technology stack preferences?
- Timeline: P0, P1, or P2?
- Relationship to HotelRunner? (Wrapper? Alternative? Complement?)

**Per Najib:** "Transform to app" = P2 (AFTER results delivered), NOT P0

---

### [PROPERTY] — Villa Thaifa Details Needed

**From Said/Ikram:**

**Basic Info:**
- [ ] Complete address for OTA listings
- [ ] Property phone number
- [ ] Property email
- [ ] Property website (if exists)

**Rooms:**
- [ ] Number of rooms total
- [ ] Room names/numbers
- [ ] Room types (Standard, Deluxe, Suite, etc.)
- [ ] Bed configurations (Double, Twin, King, etc.)
- [ ] Room capacities (max guests)
- [ ] Room-specific amenities

**Amenities:** (See Section 7 template)
- [ ] Complete amenities list
- [ ] WiFi speed
- [ ] Pool details (if applicable)
- [ ] Parking details

**Policies:**
- [ ] Check-in/out times and procedures
- [ ] Cancellation policy preference
- [ ] Payment methods
- [ ] Security deposit policy
- [ ] House rules (smoking, pets, noise, etc.)

**Photos:**
- [ ] Professional photos availability status
- [ ] If not available: Schedule photoshoot IMMEDIATELY

**Operations:**
- [ ] Who manages day-to-day? (Said? Ikram? Both?)
- [ ] Who handles guest communication?
- [ ] Emergency contact info
- [ ] Service providers (cleaning, maintenance)

---

### [RESEARCH] — Market Data Needed

**Marrakech OTA Priorities:**
- [ ] Which OTAs perform best for Marrakech maisons d'hôtes?
- [ ] Top 10 platforms by booking volume
- [ ] Commission rates per platform
- [ ] Platform activation priority sequence

**Marrakech Seasonality:**
- [ ] Official 4 seasons definitions
- [ ] Peak season dates (très haute saison)
- [ ] High season dates (haute saison)
- [ ] Mid season dates (moyenne saison)
- [ ] Low season dates (basse saison)
- [ ] Tourism board or industry source

**Competitor Pricing:**
- [ ] Identify 5-10 comparable maisons d'hôtes
- [ ] Record pricing per season
- [ ] Analyze room types and configurations
- [ ] Compare amenities
- [ ] Evaluate listing quality
- [ ] Note average ratings and review counts

**"Monteurs" Definition:**
- [ ] What are "monteurs" in Moroccan hospitality?
- [ ] Tour operators? Travel agents? Channel partners?
- [ ] Does Said have existing relationships?
- [ ] How do they fit in OTA strategy?
- [ ] Commission structure?

---

### [IKRAM] — Role Clarification

**Questions:**
- [ ] What is Ikram's exact role?
- [ ] Day-to-day management?
- [ ] Guest communication?
- [ ] Housekeeping coordination?
- [ ] HotelRunner access?
- [ ] OTA listing management?
- [ ] On-site or remote?
- [ ] Contact information?
- [ ] Training needs?

---

## 11. AGENT EXECUTION PROTOCOL

### How AI Agents Should Use This Brief

**Priority Sequence:**

1. **Read This Section First** (Agent Instructions)
2. **Read Section 1** (Phase 1 Mission) — Understand the goal
3. **Read Section 2** (This Week Checklist) — Know what to execute
4. **Reference Client Brief** (`villa-thaifa-client-brief-v0.2.0.md`) — Understand business context
5. **Execute Phase 1** — Follow checklists, use templates, research placeholders

---

### Execution Principles (From Najib's Wisdom)

**1. Results > Perfection**
> "Good enough and LIVE" beats "perfect but delayed"

**2. Speed to Market**
> Launch fast, iterate based on real booking data

**3. Client Priority**
> Said's needs > Architectural elegance

**4. Pragmatic Approach**
> Use "1 hour" pricing, don't wait for weeks of analysis

**5. Avoid "Tu te fuis beaucoup"**
> Don't over-plan before executing. Don't wait for complete information. Use placeholders, launch, fill gaps later.

---

### Execution Modes

**This Week = Operator/Pompier Mode (Firefighter):**
- Execute checklists
- Use templates
- Launch with "good enough"
- Don't wait for perfection
- Escalate blockers immediately

**Weeks 2-4 = Optimization Mode:**
- Refine based on real data
- Document processes
- Extract reusable patterns
- Build scalable foundation

**Month 2+ = Architect/CTO Mode:**
- "App" vision implementation
- Multi-client architecture
- EaC migration
- Agent systems deployment

---

### Decision Authority

| Decision Type | Authority | Process |
|---------------|-----------|---------|
| **Technical implementation** | Agents → Omar | Execute, escalate if blocked |
| **Business preferences** | Said | Omar asks Said via Najib |
| **Hospitality standards** | Najib | Consult for best practices |
| **Pricing/policies** | Said (informed by Najib) | Propose, get approval |
| **Emergency/blocker** | Omar | Escalate immediately |

---

### Communication Protocol

**Daily Updates:**
- Progress on OTA activations
- Blockers encountered
- Questions requiring decisions
- Sync test results

**Escalation Triggers:**
- Technical blocker > 2 hours
- Missing information blocks execution
- Sync failure detected
- Any issue preventing "go live"

**Report Format:**

```markdown
## Daily Progress Report — [Date]

### ✅ Completed
- [List completed OTA activations]
- [List completed configurations]

### 🔄 In Progress
- [List active work items]

### 🔴 Blocked
- [List blockers with details]
- [List information needed]

### 📊 Metrics
- Active platforms: X/15
- Calendar sync tests: [Pass/Fail]
- Visible bookings: X

### 🚨 Escalations
- [Any urgent issues]
```

---

### Research Protocol

**When Placeholder Encountered:**

1. **Prioritize:** P0 > P1 > P2
2. **Research:** Use web search, official sources, industry standards
3. **Document:** Add findings to appropriate section
4. **Propose:** If decision needed, propose options to Omar
5. **Execute:** Don't wait if "good enough" option exists

**Research Sources (Prioritized):**
1. Official platform documentation
2. HotelRunner support/docs
3. Industry standards (hospitality associations)
4. Competitor analysis (direct observation)
5. Expert input (Najib for hospitality, Omar for technical)

---

## 12. SUCCESS CRITERIA

### Phase 1 Complete (End of Week 1)

**Absolute Requirements:**
- ✅ 10-15 OTA platforms active and live
- ✅ All platforms linked to HotelRunner
- ✅ Calendar sync verified (< 1 min latency)
- ✅ Test booking completes successfully
- ✅ Baseline pricing set (4 seasons)
- ✅ At least 1 visible booking on calendar

**Said's Perspective:**
- ✅ Sees calendar with activity
- ✅ Multiple OTA platforms showing Villa Thaifa
- ✅ Confidence restored
- ✅ Stops complaining about "zero clients"

**Najib's Report:**
- ✅ Said satisfied with progress
- ✅ Frustration resolved
- ✅ Trust restored
- ✅ Omar delivered as promised

---

### Phase 2 Complete (Weeks 2-4)

**Foundation Built:**
- ✅ Documentation complete
- ✅ Pricing optimized based on real data
- ✅ Listings optimized for conversion
- ✅ KPI dashboard operational
- ✅ Processes ready for next client

---

### Phase 3 Ready (Month 2+)

**Scale Prepared:**
- ✅ "App" vision clarified and roadmap defined
- ✅ Multi-client architecture designed
- ✅ Villa Thaifa as template validated
- ✅ Ready to onboard next maison d'hôte

---

## 13. RISKS & MITIGATION

### Critical Risks (High Impact)

| Risk | Probability | Impact | Mitigation |
|------|------------|--------|------------|
| **Trust erosion with Said** | HIGH | CRITICAL | Deliver visible results THIS WEEK |
| **No professional photos** | MEDIUM | HIGH | Verify immediately, schedule photoshoot if needed |
| **Execution delays** | MEDIUM | CRITICAL | Hybrid approach, execute NOW, no more delays |
| **Missing property info** | MEDIUM | MEDIUM | Gather from Said ASAP, use placeholders if needed |

### Technical Risks (Medium Impact)

| Risk | Probability | Mitigation |
|------|------------|------------|
| HotelRunner API downtime | LOW | Monitor status, have support contact |
| Calendar sync failures | LOW | Test extensively, have rollback plan |
| OTA approval delays | MEDIUM | Apply to all simultaneously |
| Double-booking incident | VERY LOW | Test thoroughly, have cancellation protocol |

### Business Risks (Lower Impact)

| Risk | Mitigation |
|------|------------|
| Low initial booking volume | Expected, build over time, optimize listings |
| Negative reviews | Quality experience + professional responses |
| Competitor pricing pressure | Monitor + adjust dynamically |
| Seasonal demand fluctuation | Built into 4 seasons strategy |

---

## DOCUMENT STATUS

**Version:** 0.2.0-alpha.0  
**Created:** 2026-01-09  
**Type:** Phase 1 Complete — Ready for Execution

**Sources Integrated:**
- ✅ Client Brief v0.2.0 (business context)
- ✅ Najib's 40 years expertise and conversations
- ✅ Omar's hybrid strategy confirmation
- ✅ HotelRunner documentation
- ✅ OTA best practices
- ⏳ Awaiting: Repomix, "App" clarification, property details, market research

**Next Version Triggers:**
- Repomix received → v0.3.0 (integrate repo analysis)
- "App" clarified → v0.3.0 or v0.4.0 (add app architecture)
- Phase 1 complete → v0.4.0 or v1.0.0 (document results & learnings)

**Changelog:**
- 2026-01-09: v0.2.0-alpha.0 created — Complete structure aligned with Client Brief v0.2.0, all Najib insights integrated, ready for agent execution

---

## REFERENCES

### Official Docs
- HotelRunner: https://hotelrunner.com
- HotelRunner Developers: https://developers.hotelrunner.com
- Channel Manager Concept: https://fr.wikipedia.org/wiki/Channel_manager

### Internal References
- **Client Brief:** villa-thaifa-client-brief-v0.2.0.md (business context, stakeholders, objectives)

---

**🚀 PROJECT BRIEF READY — EXECUTE PHASE 1 NOW**

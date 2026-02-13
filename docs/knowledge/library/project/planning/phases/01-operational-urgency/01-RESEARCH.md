# Phase 1: Operational Urgency - Research

**Researched:** 2026-01-30
**Domain:** HotelRunner Operations, Photo Management, OTA Reservations
**Confidence:** MEDIUM (relies on browser automation with known limitations)

## Summary

This phase focuses on four urgent operational tasks that are blocking daily operations: configuring HotelRunner prices for 12 rooms, finalizing a reservation for room 11, uploading Room 12 photos to HotelRunner, and organizing professional photos by room.

The primary challenge is that **HotelRunner automation has known limitations** - the browser automation profile persistence does not work, requiring manual authentication for each session. All four tasks will require manual browser-based work with Omar's intervention for authentication.

**Primary recommendation:** Use browser automation (agent-browser) with manual authentication for HotelRunner tasks. The existing `legacy/content_source/facilities/rooms/` directory contains professional photos for all 12 rooms that can be organized and uploaded.

## Standard Stack

### Core Tools
| Tool | Version | Purpose | Why Standard |
|------|---------|---------|--------------|
| agent-browser | Latest (Jan 2026) | Browser automation for HotelRunner dashboard | Already installed, tested, documented |
| SQLite | 3.x | Local room data source | Room pricing data already in `property.db` |

### Supporting Tools
| Tool | Purpose | When to Use |
|------|---------|-------------|
| bash/filesystem | Photo organization | OPS-04: Organizing photos by room |
| HotelRunner Dashboard | Pricing, photos, reservations | OPS-01, OPS-02, OPS-03 |
| Booking.com Extranet | Reservation confirmation | OPS-02: Verifying reservation sync |

### HotelRunner Access Methods
| Method | Status | Use Case |
|--------|--------|----------|
| Browser Automation (agent-browser) | Working with manual auth | Pricing configuration, photo upload |
| REST API (HR-v1) | Not configured | Future automation (rate limited: 250/day) |

## Architecture Patterns

### Browser Automation Workflow (HotelRunner)
```
1. Agent opens browser in headed mode
2. Omar authenticates manually (reCAPTCHA, OTP)
3. Agent navigates to target section
4. Agent performs actions (fill forms, upload files)
5. Agent closes browser
```

### Photo Organization Structure
```
photos/
├── 01/                    # Room 01
│   ├── main.jpg           # Hero image
│   ├── bathroom.jpg       # Bathroom view
│   ├── bedroom.jpg        # Bedroom view
│   └── terrace.jpg        # Terrace/view
├── 02/                    # Room 02
│   ├── main.jpg
│   └── ...
└── 12/                    # Room 12
    ├── main.jpg
    └── ...
```

### Data Sources for Pricing
```
Database (property.db)          JSON (src/data/rooms.json)
┌─────────────────────┐         ┌───────────────────────┐
│ id: R01             │         │ id: "01"              │
│ internal_name:      │         │ number: "01"          │
│   "Deluxe Triple"   │         │ type: "Deluxe Triple" │
│ base_rate_mad: 1859 │         │ price.amount: 169 EUR │
└─────────────────────┘         └───────────────────────┘
```

**Note:** Database has MAD prices (Moroccan Dirhams), JSON has EUR prices. Need to determine which to use for HotelRunner.

### Anti-Patterns to Avoid
- **Assuming profile persistence works:** It does NOT. Always plan for manual auth.
- **Running automated scripts unattended:** Will fail without authentication.
- **Uploading original resolution photos:** HotelRunner has 2MB limit per image.
- **Modifying JSON prices expecting HotelRunner sync:** No automatic sync exists.

## Don't Hand-Roll

| Problem | Don't Build | Use Instead | Why |
|---------|-------------|-------------|-----|
| HotelRunner authentication | Cookie management scripts | Manual browser auth + agent-browser | Profile persistence bug unresolved |
| Image resizing | Custom resize scripts | ImageMagick (`convert`) or online tools | Standard tool, reliable |
| Price currency conversion | Manual calculations | Agreed price list from stakeholders | Business decision, not calculation |
| Reservation confirmation | Custom API integration | HotelRunner + Booking.com dashboards | Manual verification required |

**Key insight:** This phase is fundamentally operational/manual work. Automation complexity is not justified for one-time tasks. Focus on completion, not tooling.

## Common Pitfalls

### Pitfall 1: HotelRunner Authentication Timeout
**What goes wrong:** Browser session expires, forms not submitted
**Why it happens:** HotelRunner security, inactivity timeout
**How to avoid:**
- Complete one task fully before switching to another
- Keep browser active during photo uploads
- Use headed mode to monitor session state
**Warning signs:** reCAPTCHA appears unexpectedly, form submission fails

### Pitfall 2: Photo Upload Size Limits
**What goes wrong:** Upload fails silently or with error
**Why it happens:** HotelRunner has 2MB per image limit
**How to avoid:**
- Check file sizes before upload: `du -h *.jpg`
- Resize images exceeding 2MB
- Use JPEG quality 80-85% for web optimization
**Warning signs:** Large HDR photos (3-4MB in legacy folder)

### Pitfall 3: Price Currency Confusion
**What goes wrong:** Wrong prices configured, revenue loss
**Why it happens:** Database has MAD, JSON has EUR, HotelRunner may expect either
**How to avoid:**
- Clarify currency with Omar before configuring
- Document which prices are used
- Verify first room, then batch update others
**Warning signs:** Prices look suspiciously high/low

### Pitfall 4: Room Number Mapping
**What goes wrong:** Wrong photos/prices assigned to rooms
**Why it happens:** HotelRunner room IDs may differ from local IDs (01 vs R01)
**How to avoid:**
- Verify mapping before batch operations
- Cross-reference HotelRunner room list with local data
- Use screenshots in `docs/specs/knowledge/platforms/hotelrunner/hr_rooms_list.png`
**Warning signs:** Room names don't match expected types

### Pitfall 5: Wrong HotelRunner URL
**What goes wrong:** Browser opens wrong page, login fails or redirects
**Why it happens:** Property subdomain (villa-thaifa.hotelrunner.com) doesn't work
**How to avoid:**
- **ALWAYS use:** `https://app.hotelrunner.com` (main app URL)
- **NEVER use:** `https://villa-thaifa.hotelrunner.com` (broken subdomain)
- URL is documented in `.env` as `HOTELRUNNER_URL`
**Warning signs:** Page shows generic marketing or redirects unexpectedly

### Pitfall 6: Asking Human for Available Credentials
**What goes wrong:** Agent asks human to enter credentials that are already in .env
**Why it happens:** Over-cautious checkpoint design, assuming all auth needs human
**How to avoid:**
- **ALWAYS check .env/.env.local first** for credentials before asking
- **Enter credentials automatically** using agent-browser type commands
- **ONLY ask human for:** reCAPTCHA, OTP codes, 2FA - things agent cannot do
- Credentials location: `.env` or `.env.local` (HOTELRUNNER_OWNER_EMAIL/PASSWORD)
**Rule:** If you have the solution, use it. Don't waste human time.

### Pitfall 7: Small Browser Viewport
**What goes wrong:** UI elements cut off, forms unusable, agent can't see full page
**Why it happens:** Default viewport may be small (800x600 or similar)
**How to avoid:**
- **ALWAYS set viewport first:** `agent-browser set viewport 1920 1080`
- Do this BEFORE opening any page or immediately after
- Standard desktop resolution ensures all UI elements are visible
**Rule:** First command after opening browser: set viewport 1920 1080

### Pitfall 8: Not Checking "Remember Me"
**What goes wrong:** Session expires, need to re-authenticate every time
**Why it happens:** Forgot to check the remember me checkbox
**How to avoid:**
- When logging in, ALWAYS check "Remember me" checkbox
- `agent-browser check "@e[remember-me-ref]"` before clicking login
- Saves authentication for future sessions
**Rule:** Always check remember me to reduce future authentication overhead

### Pitfall 9: Reservation Channel Sync
**What goes wrong:** Room 11 reservation shows on one platform, not others
**Why it happens:** HotelRunner -> Booking.com sync may have delays
**How to avoid:**
- Verify on both HotelRunner AND Booking.com
- Allow 15-30 minutes for channel sync
- Check "Inventory Type" in HotelRunner
**Warning signs:** Status differs between platforms

## Code Examples

### Browser Automation: Navigate to Pricing Page
```bash
# Source: sources/agent-browser/guide.md
# 1. Open HotelRunner in headed mode
agent-browser --headed open https://app.hotelrunner.com/login
# Omar authenticates manually

# 2. Navigate to inventory calendar (for pricing)
agent-browser open https://app.hotelrunner.com/admin/channel/calendars/occupancies

# 3. Get interactive elements
agent-browser snapshot -i -c

# 4. Click on pricing/rates section (ref will vary)
agent-browser click @e[X]
```

### Browser Automation: Upload Photos
```bash
# Source: sources/agent-browser/guide.md
# Navigate to room types section
agent-browser open https://app.hotelrunner.com/admin/inventory/room-types

# Get element references
agent-browser snapshot -i -c

# Click on specific room to edit
agent-browser click @e[room-row-ref]

# Use file upload (selector will depend on page structure)
agent-browser upload "input[type='file']" "/path/to/photo.jpg"
```

### Photo Organization Script
```bash
# Organize legacy photos into photos/{room-id}/ structure
# Source: Filesystem patterns

LEGACY_DIR="/home/director/grid/clients/villa-thaifa/property-management/legacy/content_source/facilities/rooms"
TARGET_DIR="/home/director/grid/clients/villa-thaifa/property-management/photos"

for room in 01 02 03 04 05 06 07 08 09 10 11 12; do
  mkdir -p "$TARGET_DIR/$room"
  # Copy JPG photos
  cp "$LEGACY_DIR/$room/images/"*.jpg "$TARGET_DIR/$room/" 2>/dev/null
  # Copy JPEG photos
  cp "$LEGACY_DIR/$room/images/"*.jpeg "$TARGET_DIR/$room/" 2>/dev/null
done
```

### Check Photo Sizes (for 2MB limit)
```bash
# Find photos exceeding 2MB
find /home/director/grid/clients/villa-thaifa/property-management/legacy/content_source/facilities/rooms/12/images \
  -type f \( -name "*.jpg" -o -name "*.jpeg" \) \
  -size +2M \
  -exec ls -lh {} \;
```

### Database Price Query
```bash
# Source: property.db schema
sqlite3 /home/director/grid/clients/villa-thaifa/property-management/property.db \
  "SELECT id, internal_name, base_rate_mad FROM rooms ORDER BY id"
```

## Current Room Data

### From SQLite Database (MAD Prices)
| Room ID | Name | Price (MAD) | Status |
|---------|------|-------------|--------|
| R01 | Deluxe Triple Room | 1,859 | VERIFIED |
| R02 | Deluxe Double Room | 1,749 | VERIFIED |
| R03 | Deluxe Triple Room | 1,859 | VERIFIED |
| R04 | Double Room Superior | 1,639 | VERIFIED |
| R05 | Double Room Superior | 1,639 | VERIFIED |
| R06 | Executive Suite | 1,859 | VERIFIED |
| R07 | Deluxe King Suite | 3,619 | VERIFIED |
| R08 | Deluxe Triple Room | 1,859 | VERIFIED |
| R09 | Family Suite | 2,079 | VERIFIED |
| R10 | Suite | 1,969 | VERIFIED |
| R11 | Family Suite | 2,079 | VERIFIED |
| R12 | Presidential Suite | 4,939 | VERIFIED |

### From JSON (EUR Prices - Public Site)
| Room | Type | Price (EUR) |
|------|------|-------------|
| 01 | Deluxe Triple Room | 169 |
| 02 | Deluxe Double Room | 159 |
| 03 | Deluxe Triple Room | 169 |
| 04 | Double Room Superior | 149 |
| 05 | Double Room Superior | 149 |
| 06 | Executive Suite | 169 |
| 07 | Deluxe King Suite | 329 |
| 08 | Deluxe Triple Room | 169 |
| 09 | Family Suite | 189 |
| 10 | Suite | 179 |
| 11 | Family Suite | 189 |
| 12 | Presidential Suite | 449 |

### Photo Inventory (Legacy Folder)
| Room | Professional Photos (HDR) | WhatsApp Photos | Total |
|------|---------------------------|-----------------|-------|
| 01 | 9 | 8 | 17 |
| 02 | 9 | 7 | 16 |
| 03 | 8 | 12 | 20 |
| 04 | 9 | 5 | 14 |
| 05 | 18 | 6 | 24 |
| 06 | (shared with 04/05) | 5 | ~5 |
| 07 | (unique) | 6 | ~6 |
| 08 | (unique) | 3 | ~3 |
| 09 | 15 | 5 | 20 |
| 10 | 11 | 0 | 11 |
| 11 | 0 | 14 | 14 |
| 12 | 0 | 10 | 10 |

**Key Finding:** Room 12 has 10 photos in legacy folder, sufficient for HotelRunner upload (min 5 required).

## State of the Art

| Old Approach | Current Approach | When Changed | Impact |
|--------------|------------------|--------------|--------|
| API automation | Browser automation | Jan 2026 | Profile bug blocks full automation |
| Single auth session | Manual auth per session | Jan 2026 | Requires Omar's intervention |
| Rate-based pricing | Date-range bulk updates | HotelRunner v2 | More efficient for seasonal rates |

**Deprecated/outdated:**
- `extract_reservations.py`: Blocked by profile persistence bug; use manual extraction
- HotelRunner API for real-time updates: Requires HTTPS callback URL (not available)

## Task-Specific Research

### OPS-01: Configure HotelRunner Prices for All 12 Rooms

**Approach:** Use HotelRunner Bulk Updates feature
- Navigation: Calendar > Bulk Updates
- Select: "Availability and Price" > "Fixed" base price
- Apply to: All date ranges, all room types
- Channels: Select all connected channels

**Price Source Decision Needed:**
- Option A: Use EUR prices from JSON (169, 159, 149, etc.)
- Option B: Use MAD prices from database (1859, 1749, 1639, etc.)
- Option C: Use HotelRunner's existing prices (unknown current state)

**Estimated Time:** 30-45 minutes with manual auth

### OPS-02: Finalize Reservation for Room 11

**Approach:** Verify and confirm in both platforms
1. Check HotelRunner > PMS > Reservations > All
2. Find Room 11 pending reservation
3. Verify status: Should show "Confirmed" or "Pending"
4. If pending: Contact guest or confirm via HotelRunner
5. Cross-verify on Booking.com Extranet

**Dependencies:**
- Guest contact info (if needing confirmation)
- Payment status verification

**Estimated Time:** 15-20 minutes

### OPS-03: Upload Room 12 Photos to HotelRunner

**Approach:** Manual upload via HotelRunner room types editor
1. Navigate: My Property > Room Types
2. Select Room 12 (Presidential Suite)
3. Click "Add photo" icon
4. Upload photos from legacy folder (after resize if needed)
5. Minimum 5 photos required

**Photo Sources (Room 12):**
- `legacy/content_source/facilities/rooms/12/images/` - 10 JPEG files
- Filenames are UUIDs (need to identify best shots)

**Pre-upload Check:**
```bash
# Check sizes of Room 12 photos
du -h /home/director/grid/clients/villa-thaifa/property-management/legacy/content_source/facilities/rooms/12/images/*
```

**Estimated Time:** 20-30 minutes (including resize if needed)

### OPS-04: Organize Professional Photos by Room

**Approach:** Create `photos/{room-id}/` structure with naming convention

**Naming Convention:**
```
{room-id}/
├── main.jpg          # Hero/featured image
├── bed-01.jpg        # Primary bed view
├── bed-02.jpg        # Secondary bed view (if applicable)
├── bathroom.jpg      # Bathroom
├── terrace.jpg       # Terrace/outdoor space
├── view.jpg          # Window/view
├── detail-01.jpg     # Amenity closeup
└── detail-02.jpg     # Another detail
```

**Source Mapping:**
- HDR photos (`_DSC*.jpg`): Professional quality, use for main images
- WhatsApp photos: Lower quality, use for supplementary views

**Estimated Time:** 45-60 minutes for all 12 rooms

## Open Questions

1. **Currency for HotelRunner Pricing**
   - What we know: Database has MAD, JSON has EUR
   - What's unclear: Which currency HotelRunner is configured to use
   - Recommendation: Ask Omar to verify HotelRunner currency setting before bulk update

2. **Room 11 Reservation Details**
   - What we know: Need to finalize reservation
   - What's unclear: Current status, guest details, dates
   - Recommendation: Check HotelRunner first, get specific reservation number

3. **Photo Quality Standards**
   - What we know: HotelRunner has 2MB limit
   - What's unclear: Preferred resolution, aspect ratio, minimum count per room
   - Recommendation: Use existing photos as-is if under 2MB, resize HDR if over

4. **HotelRunner Admin Access (INT-03)**
   - What we know: Omar uses said_thaifa@hotmail.fr account currently
   - What's unclear: Whether Omar has his own admin account yet
   - Recommendation: May need to complete INT-03 before OPS-01

## Dependencies and Blockers

### Critical Dependency: INT-03 (HotelRunner Admin Access)
- **Risk:** If Omar doesn't have admin access, pricing configuration may be blocked
- **Mitigation:** Use owner account (said_thaifa@hotmail.fr) as fallback
- **Status:** Need verification before Phase 1 execution

### Photo Size Verification
- **Risk:** Some photos exceed 2MB, will fail upload
- **Mitigation:** Run size check, resize with ImageMagick if needed
- **Status:** Ready to verify

## Sources

### Primary (HIGH confidence)
- `sources/hotelrunner-api/guide.md` - Local documentation
- `sources/hotelrunner-api/STATUS-FINAL.md` - Integration status and limitations
- `sources/hotelrunner-api/TEST-RESULTS.md` - Browser automation test results
- `sources/agent-browser/guide.md` - Browser automation CLI documentation
- `property.db` SQLite database - Room pricing data

### Secondary (MEDIUM confidence)
- [Wix Hotels by HotelRunner: Making Bulk Updates](https://support.wix.com/en/article/wix-hotels-by-hotelrunner-making-bulk-updates) - HotelRunner bulk updates workflow
- [Wix Hotels by HotelRunner: Creating Room Types](https://support.wix.com/en/article/wix-hotels-by-hotelrunner-adding-room-types) - Room and photo management
- [HotelRunner Helpdesk](http://helpdesk.hotelrunner.com/en/faq/quick-start/) - General setup guides

### Tertiary (LOW confidence)
- WebSearch results for HotelRunner pricing - General patterns, not Villa Thaifa specific
- WebSearch results for Booking.com extranet - Reservation management patterns

## Metadata

**Confidence breakdown:**
- Photo organization: HIGH - Local filesystem, well understood
- Browser automation: MEDIUM - Works with manual auth, profile bug documented
- HotelRunner pricing workflow: MEDIUM - Based on Wix Hotels docs, may differ for standalone HotelRunner
- Reservation finalization: LOW - Need specific reservation details

**Research date:** 2026-01-30
**Valid until:** 2026-02-28 (30 days - operational tasks, platform may update)

---

## Recommendations for Planning

1. **Start with OPS-04** (Photo Organization) - No HotelRunner access needed, can be done immediately
2. **Verify INT-03 status** before attempting OPS-01 - Confirm Omar's admin access
3. **Batch OPS-01 and OPS-03** in same session - Both require HotelRunner auth
4. **OPS-02 can be quick verification** - May already be finalized, check first
5. **Plan for 2-3 hours total** including authentication overhead

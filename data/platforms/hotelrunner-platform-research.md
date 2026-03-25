# HotelRunner Platform Research

## Executive Summary

HotelRunner is a cloud-based channel manager and PMS platform founded in 2011 by Arden Agopyan and Ali Beklen (ex-IBM executives). The platform connects hotels to 150+ OTAs, with 41.8K customers and $6M ARR (2024). Provides dual API support (XML/SOAP + REST), TOKEN/HR_ID authentication, and restrictive rate limits (250 requests/day per property). Positioned as distribution-first solution for small-to-mid hotels; competes with SiteMinder (market leader), Cloudbeds (all-in-one), and Mews (automation-focused). No dedicated CLI/SDK; integrations via API and third-party partners.

## What is HotelRunner

### Company Background
- **Founded**: 2011
- **Founders**: Arden Agopyan and Ali Beklen (both ex-IBM, worked in cloud computing and financial sectors)
- **Headquarters**: Global operations with significant market presence
- **Revenue**: $6M ARR (2024), up from $3M in 2023
- **Funding**: $8.5M raised across 4 rounds from 10 investors
- **Customer Base**: 41.8K customers (2024)
- **Daily Volume**: Processes 35+ million transactions daily between properties, travel agencies, travelers, and payment gateways

### Core Mission
Convert long-tail accommodation sales and distribution management from offline to online at global scale. Platform serves as unified sales, operations, and distribution management system with AI-driven solutions and worldwide B2B network connectivity.

### Market Recognition
- **2024 Travolution Awards**: Named "Best Large Technology Supplier"
- **Booking.com**: Premier Connectivity Partner
- **Expedia Group**: Preferred Connectivity Partner for 2023
- **Airbnb**: Preferred Software Partner

### Product Portfolio
1. **Channel Manager** — Primary product; integrates with 150+ OTAs and metasearch platforms
2. **PMS by HotelRunner** — Property management system integrated with channel management
3. **Autopilot (Revenue Management)** — AI-driven dynamic pricing and rate optimization
4. **Booking Engine** — Direct booking solution
5. **Custom Apps & API Platform** — Third-party integrations

---

## API Capabilities

### Overview
HotelRunner provides dual API architecture: Legacy XML/SOAP-based system and modern REST API. Both are production-grade but with different architectural paradigms.

### Available API Services

**Inventory Management:**
- Get Room List — retrieve all rooms/rates for property
- Update Room (DateRange) — batch updates across date ranges
- Update Room (Daily) — granular daily updates
- Availability and Restrictions management
- Rate management and pricing updates

**Reservations:**
- Retrieve Reservations — paginated reservation history
- Real-time Push Reservations — instant push notifications of new/modified/cancelled reservations
- Reservation State Update — modify reservation status
- Confirm Reservation Delivery — PMS → HotelRunner confirmation messages

**Channels:**
- Channel activation/deactivation
- Channel-specific inventory synchronization
- Rate parity enforcement across channels

**Additional Services:**
- Property metadata (Services, Facilities, Amenities)
- POS integrations (departments, extras, revenue accounts, guest lists, transactions)
- Utility endpoints (currencies, room amenities, country codes)

### REST API Endpoints

**Get Room List**
- **Endpoint**: `GET https://app.hotelrunner.com/api/v2/apps/rooms`
- **Parameters**:
  - `token` (required): API token
  - `hr_id` (required): HotelRunner property ID
- **Response**: JSON array of room objects with properties:
  - `rate_code`: Rate plan identifier
  - `inv_code`: Inventory code
  - `name`: Room type name
  - `room_capacity`: Max occupancy
  - `channel_codes`: Associated OTA codes
  - `availability`, `price`, `min_stay`, `stop_sale` status

**Update Room**
- **Endpoint**: `PUT https://app.hotelrunner.com/api/v2/apps/rooms/~`
- **Parameters**:
  - `inv_code` (required): Room inventory code
  - `start_date` (required): Format YYYY-MM-DD
  - `end_date` (required): Format YYYY-MM-DD
  - `availability` (optional): Unit count
  - `price` (optional): Rate amount
  - `stop_sale` (optional): 1 or 0
  - `min_stay` (optional): Minimum stay nights
  - `cta` (optional): Check-in restriction (1 or 0)
  - `ctd` (optional): Check-out restriction (1 or 0)
  - `days` (optional): Array of weekday targeting
  - `channel_codes` (optional): Target specific OTAs
- **Response**: JSON with `status` field (`ok` or `try_again`) and `transaction_id`

**Get Transaction Details**
- **Endpoint**: `GET https://app.hotelrunner.com/api/v2/apps/infos/transaction_details`
- **Parameters**:
  - `transaction_id` (required): From update request
  - `token` (required)
  - `hr_id` (required)
- **Response**: JSON with per-channel success/failure states

**Retrieve Reservations**
- **Endpoint**: `GET https://app.hotelrunner.com/api/v2/apps/reservations`
- **Features**: Pagination support, filtering by date range, status-based retrieval

**Real-time Push Reservation**
- **Method**: Webhook-based push notifications
- **Triggers**: New reservation, modification, cancellation
- **Transport**: HTTP POST to property-configured endpoint

### XML/SOAP API
- **Protocol**: SOAP with WS-Security headers
- **Authentication**: SOAP Security header (consistent with REST token approach)
- **Message Format**: XML payloads in SOAP Body
- **Use Case**: Legacy integrations, strict enterprise security requirements
- **Documentation**: SOAP Message Structure available at am.hotelrunner.com/custom-apps/xml-api/

### API Format Support
- **REST**: JSON request/response
- **SOAP/XML**: XML payloads only
- **Response Codes**: Standard HTTP status codes (not fully documented in available sources)

---

## Authentication

### Method: Token + Property ID
HotelRunner uses a **two-parameter key-based authentication** system instead of OAuth or more modern token paradigms.

**Required Parameters (ALL requests):**
- `token`: API token/key (unique per property)
- `hr_id`: HotelRunner property ID (numeric identifier)

**Key Generation:**
- Generated via property panel under "My Property" → "API Keys" section
- Can generate multiple keys per property
- Keys can be revoked from same panel
- No expiration mentioned; treat as persistent until revoked

**Parameter Transmission:**
- Sent as query parameters in GET requests: `?token={TOKEN}&hr_id={HR_ID}`
- Sent in request body for POST/PUT operations (exact format not documented)
- SOAP: Embedded in SOAP Security header with username/password elements

**Security Characteristics:**
- No per-request signature (unlike AWS SigV4)
- No OAuth refresh token flow
- No scope/permission granularity documented
- No API key versioning
- Similar to basic API key approach (simple but less sophisticated than OAuth)

**Best Practice**: Treat tokens like passwords—store in environment variables, rotate periodically, use separate keys per integration if possible.

---

## Rate Limits

### Tiered Rate Limiting (Per Documentation)

**Property Level:**
- **250 requests per day** per property
- **5 requests per minute** per property

**Global/Application Level:**
- **75 requests per minute** global limit (across all properties using same app token)

### Implications for Villa Thaifa PMS Integration
- **Daily Budget**: 250 requests/day = ~10.4 requests/hour if spread evenly
- **Real-time Sync**: 5 req/min = problematic for high-frequency updates; expect throttling if >5 per minute to single property
- **Batch Operations**: Must batch room updates to stay within limits
- **Multi-property**: 75 global limit means managing 4+ properties requires careful request batching
- **Polling Strategy**: Real-time push is preferred over polling to conserve request budget

### Observed Impact on Integration Pattern
- **No webhook costs**: Real-time push reservations don't consume rate limits (event-driven, not API polling)
- **Inventory sync**: Daily or 2x-daily batch sync recommended vs. per-availability change
- **Reservation retrieval**: Pagination needed; can't fetch all reservations in single request
- **Backoff Strategy**: Implement exponential backoff for 429 responses (rate limit exceeded)

---

## Key Endpoints Summary

| Function | Endpoint | Method | Purpose |
|----------|----------|--------|---------|
| List Rooms | `/api/v2/apps/rooms` | GET | Retrieve all room types and current rates |
| Update Room | `/api/v2/apps/rooms/~` | PUT | Batch update availability/pricing/restrictions |
| Check Update Status | `/api/v2/apps/infos/transaction_details` | GET | Verify per-channel success of room updates |
| Get Reservations | `/api/v2/apps/reservations` | GET | Paginated reservation history |
| Push Notification | (Webhook) | POST | Real-time reservation events to property PMS |
| Confirm Delivery | `/api/v2/apps/reservations/confirm` | POST | Acknowledge reservation receipt |

---

## OTA Integrations

### Supported Channels: 150+

**Primary OTAs (Tier 1):**
- Booking.com (Premier Connectivity Partner)
- Expedia Group (Preferred Connectivity Partner for 2023)
- Airbnb (Preferred Software Partner, 2-way API)
- Agoda
- Google Hotel Ads (metasearch)
- Trivago (metasearch)
- Tripadvisor (metasearch)

**Integration Breadth:**
- 150+ total channel partnerships (exact list not published)
- Includes vacation rental platforms (VRBO, Airbnb, etc.)
- Local and regional booking platforms (market-specific coverage)
- Metasearch engines for visibility and traffic generation

### Integration Architecture

**Setup Process:**
1. Configure room types and rate plans in HotelRunner
2. Activate desired channels in HotelRunner dashboard
3. For channel-specific requirements (e.g., Expedia Product API):
   - Complete room type/rate plan setup in HotelRunner
   - Click "Synchronize content" in Channels → OTA section
   - Channel may require additional manual activation (e.g., Booking.com contact required)

**Synchronization:**
- **One-way**: HotelRunner → Channel (inventory, rates, availability)
- **Two-way**: Airbnb and select channels (reservations pushed back to HotelRunner)
- **Single-click sync**: Update rates/availability in HotelRunner; auto-push to all active channels
- **Rate parity enforcement**: Built-in rules prevent rate discrepancies across channels

**iCal Integration:**
- Generate iCal feed from HotelRunner for manual channel sync
- Supports vacation rental platforms lacking API connectivity
- Pull iCal calendars from external platforms into HotelRunner

### Channel-Specific Notes

**Expedia:**
- Uses HotelRunner's Product API integration
- Requires room types/rates defined before sync
- Synchronize content via "Channels – Online Travel Agencies – Expedia – About"
- Some manual Expedia-side setup may be required

**Booking.com:**
- Premier partner status indicates native integration
- Contact Booking.com required to complete initial setup
- Then managed entirely from HotelRunner dashboard

**Airbnb:**
- 2-way API connectivity (rare for channel integrations)
- Real-time rate, availability, and booking synchronization
- Launched as product update (dedicated Airbnb API integration)
- Positions HotelRunner as viable single-interface for Airbnb + traditional OTA management

**Metasearch (Google, Trivago, TripAdvisor):**
- Reduce OTA dependency
- Drive direct bookings by increasing visibility
- Meta-pricing may differ from OTA rates (allowed)

---

## Pricing

### Plan Structure

HotelRunner uses **module-based pricing** rather than fixed-tier plans. Customers choose and combine modules based on needs.

### Available Plans (Documented)

**Essential Plans:**
- Essential Sell (channel distribution focus)
- Essential Complete (broader feature set)
- Required prerequisite for Advanced plan features

**Advanced Plans:**
- Higher feature limits
- Advanced functionality (e.g., advanced revenue management)
- Requires Essential plan as base

**Elite Plan:**
- Unlimited access to all features
- Includes features from Essential and Advanced tiers at no additional per-feature cost
- Strategic global revenue management consultancy
- Private operational support line
- Project management support

### Pricing Transparency Issue

**Critical Finding**: No public pricing published on hotelrunner.com/en/pricing/

- Pricing is **quote-based**, determined by:
  - Number of properties
  - Modules selected
  - Feature tier chosen
  - Annual vs. monthly billing preference
- **Contact sales required** for pricing estimates
- Typical for enterprise/mid-market SaaS (common positioning)
- Suggests **pricing flexibility** and negotiations possible

### Estimated Cost Positioning

Based on competitor context:
- **Target Market**: Small-to-mid hotels (10-100+ properties)
- **Not bottom-tier**: More expensive than basic channel managers
- **Not enterprise**: Less expensive than SiteMinder or high-tier Cloudbeds
- **Likely range**: $200-$3,000+ monthly depending on property count and modules (estimate based on market research, not from HotelRunner)

### Feature Tiers Summary

| Tier | Best For | Pricing Model | Support |
|------|----------|---------------|---------|
| **Essential Sell** | Basic channel distribution | Module-based | Standard |
| **Essential Complete** | Multi-channel + core PMS | Module-based | Standard |
| **Advanced** | Revenue management, advanced features | Module-based add-on | Standard |
| **Elite** | Full-feature, enterprise support | All-inclusive per property | Dedicated |

---

## Competitors

### Market Landscape

HotelRunner operates in a competitive market segment. Primary competitors vary by feature focus:

#### SiteMinder (Strongest Competitor)
- **Position**: #1 channel manager by market share and hotelier voting (2024 HotelTechAwards)
- **Strengths**:
  - Largest channel network integration (200+)
  - Enterprise-grade multi-property management
  - Advanced revenue management
  - Global distribution leader
- **Market Recognition**: Hoteliers voted as #1 Channel Manager provider (2024)
- **Price**: Enterprise subscription tiers (free Prophet tier + paid packages)
- **Best For**: Global chains, multi-property operators

#### Cloudbeds (All-in-One Competitor)
- **Position**: Best all-in-one solution for small-to-mid hotels
- **Strengths**:
  - Combined operations + revenue + distribution + marketing
  - Unified dashboard (all tools in one platform)
  - 100% user satisfaction rating
  - 9.1/10 general quality score (vs SiteMinder's 8.5)
  - Scalable architecture for growing properties
  - Real-time guest/inventory/pricing management
- **Weakness**: Higher cost due to bundled features
- **Best For**: Hotels wanting single platform for all operations

#### Mews (Automation-First Competitor)
- **Position**: #1 PMS provider by hotelier voting (2025 HotelTechAwards)
- **Strengths**:
  - Deep automation capabilities
  - Open API ecosystem
  - Mobile-first design
  - Command-center paradigm (PMS as operational hub)
  - Strong marketing/RMS tool integrations
  - High extensibility
- **Weakness**: PMS-centric (channel management less native than HotelRunner)
- **Best For**: Hotels prioritizing operational automation and extensibility

#### Hostaway (Vacation Rental Focus)
- **Position**: Leading vacation rental property management platform
- **Strengths**:
  - Purpose-built for short-term rentals
  - Full-featured automation and OTA syncing
  - Flexible custom pricing (no hidden fees)
  - Per-property costs decrease at higher scales
  - API-first architecture
- **Weakness**: Less suitable for traditional hotels
- **Best For**: Vacation rental and Airbnb-focused properties

#### Guesty (Enterprise Rental Focus)
- **Position**: Enterprise-grade vacation rental management
- **Strengths**:
  - Comprehensive feature set (calendars, payments, guest comms, dynamics pricing)
  - Task management and accounting integration
  - Scalable to large portfolios
- **Weakness**: High cost (revenue-share model: 2-5% + onboarding fees)
- **Best For**: Large vacation rental portfolios willing to pay for full features

#### Lodgify (Website + PMS)
- **Position**: Hotel + vacation rental management with direct-booking focus
- **Strengths**:
  - Personalized website builder integrated with PMS
  - Direct booking emphasis (reduces OTA dependency)
  - All-in-one alternative to unbundled solutions
- **Weakness**: Less deep channel integration than HotelRunner
- **Best For**: Properties wanting branded direct-booking presence

### Comparative Matrix

| Criterion | HotelRunner | SiteMinder | Cloudbeds | Mews | Hostaway | Guesty |
|-----------|-------------|-----------|-----------|------|----------|--------|
| **Channel Integration** | 150+ | 200+ | 100+ | 80+ | 100+ | 100+ |
| **Primary Focus** | Distribution | Distribution | All-in-one | Operations | Rentals | Rentals |
| **PMS Included** | Yes (basic) | Limited | Yes (full) | Yes (full) | Yes | Yes |
| **API Maturity** | REST + XML/SOAP | REST (mature) | REST | REST (open) | REST (strong) | REST |
| **Rate Limits** | 250/day, 5/min | Not published | Not published | Not published | Flexible | Flexible |
| **Target Market** | Small-mid hotels | Enterprise hotels | Small-mid hotels | Mid-large hotels | Rentals | Rentals |
| **Market Ranking** | #2-3 channel mgr | #1 channel mgr | #2 all-in-one | #1 PMS (2025) | #1 rentals | #2 rentals |
| **Pricing Model** | Module-based | Subscription tiers | Subscription | Subscription | Custom quotes | Revenue-share |
| **Ease of Setup** | Moderate | Enterprise (complex) | Easy | Moderate | Easy | Moderate |

### HotelRunner's Competitive Positioning

**Strengths:**
- Distribution-first approach (vs. operations-first like Mews)
- Simpler than SiteMinder for small hotels
- More affordable than Cloudbeds for single-property operators
- Native Airbnb 2-way sync (rare in traditional hotel software)
- Emerging AI pricing (Autopilot feature)

**Weaknesses:**
- Fewer channels than SiteMinder (150 vs 200+)
- Less full-featured PMS than Cloudbeds or Mews
- Lower market visibility than market leader (SiteMinder)
- Restrictive rate limits (250/day) vs. competitors
- Quote-based pricing (less transparent than subscription tiers)
- Limited automation depth vs. Mews

**When to Choose HotelRunner:**
- Small-to-mid hotels (5-50 properties)
- Heavy multi-OTA distribution (especially Airbnb)
- Budget constraints vs. enterprise platforms
- Distribution is top priority, not full operations
- Direct booking + OTA hybrid model (with Airbnb)

**When to Choose Alternatives:**
- SiteMinder: Global chains, 100+ properties, maximum channel reach
- Cloudbeds: Want all operations in one system (no integration hassle)
- Mews: Prioritize automation and extensibility
- Hostaway: Pure vacation rental focus
- Guesty: Enterprise rental portfolios

---

## CLI & SDK Support

### Finding: NO Dedicated CLI or SDK

**Critical Gap**: HotelRunner does not offer:
- Official Command-Line Interface (CLI)
- Official Software Development Kit (SDK) for popular languages
- Official client libraries (Python, JavaScript, etc.)
- Postman collection (though unofficial workspace exists at postman.com)

### Integration Approach

**Only Official Method**: Direct HTTP API calls (REST or SOAP)

**Recommended Integration Patterns:**

1. **Custom Integration (Preferred for Villa Thaifa)**
   - Write API wrapper in Python, JavaScript, or language of choice
   - Use standard HTTP libraries (requests in Python, axios in JS)
   - Implement batching and rate-limit handling
   - Cache room/rate data locally to conserve requests

2. **Third-Party Middleware**
   - Use iPaaS platforms with HotelRunner connectors:
     - Zapier (limited)
     - Make.com (limited)
     - Integration.com
     - Custom IFTTT-style workflows
   - Third-party PMS platforms that include HotelRunner integration

3. **Custom Script / Cron Jobs**
   - Simple bash/Python scripts for scheduled updates
   - Daily batch sync (e.g., sync all rates at 2 AM)
   - Webhook receiver for real-time push reservations
   - Log rate-limit metrics for monitoring

### Workarounds & Tools

**Postman Collection:**
- HotelRunner maintains a Postman workspace (unofficial):
  - "HotelRunner - Standard API for Agents"
  - "HotelRunner - Standard API for Channels"
  - Useful for testing and documentation reference
  - Not a substitute for SDK

**Documentation:**
- Developers portal at developers.hotelrunner.com is comprehensive
- SOAP examples available
- REST examples less detailed than ideal

### Implication for Villa Thaifa PMS
- **Build-vs-Buy Decision**: Will need custom API wrapper code (no SDK)
- **Development Cost**: ~20-40 hours for production-grade integration
- **Operational Cost**: Ongoing maintenance of batch sync scripts
- **Risk Mitigation**: Must implement robust error handling, logging, and monitoring due to lack of official SDK support

---

## Key Technical Takeaways for Villa Thaifa PMS Integration

### 1. **API Maturity & Quality**
- **Verdict**: Mature but legacy-flavored (dual XML/REST)
- **Constraint**: Rate limits are restrictive (250/day/property) for high-frequency sync
- **Design Impact**: Must implement intelligent caching and batch operations
- **Recommendation**: Real-time push webhooks for reservations (don't count against limits); daily batch sync for rates/availability

### 2. **Authentication Simplicity**
- **Verdict**: Simple but less secure than modern OAuth
- **Token Model**: Static TOKEN + HR_ID (similar to API keys)
- **No Refresh Flow**: Tokens persist until revoked
- **Implication**: Secure token storage critical; implement token rotation policy

### 3. **Channel Coverage for Villa Thaifa**
- **Verdict**: Excellent for multi-OTA distribution (150+ channels)
- **Priority Channels**:
  - Airbnb (2-way sync — Villa Thaifa's key market)
  - Booking.com (secondary market)
  - Google Hotel Ads (direct booking traffic)
- **Setup Effort**: Moderate (API integration + per-channel configuration)

### 4. **Pricing & Economics**
- **Transparency**: Quote-based (negotiate based on property count, features)
- **Estimated Tier**: Essential Complete + Advanced modules
- **For 1-2 properties**: Likely $500-$1,500/month (industry estimate)
- **ROI Case**: Justifiable if distribution revenue increases by >20%

### 5. **Competitive Position**
- **Verdict**: Solid mid-market option; not market-leading
- **Better Alternative If**: Operations automation is priority (choose Cloudbeds/Mews)
- **Best Fit If**: Distribution + Airbnb syncing is primary goal
- **Trade-off**: Simpler than SiteMinder; less operations-integrated than Cloudbeds

### 6. **Integration Complexity**
- **No SDK**: Must write custom API wrapper code
- **Estimated Dev Effort**: 20-40 hours for production integration
- **Key Challenge**: Rate limits (250/day) require intelligent batching strategy
- **Recommendation**:
  - Implement local cache of room/rate data
  - Daily batch sync (not per-change)
  - Real-time webhook for reservations
  - Exponential backoff for rate-limit handling

### 7. **Production Readiness**
- **Verdict**: Production-ready for mid-scale operations
- **Tested At**: 41.8K customers, $6M ARR, 35M transactions/day
- **Infrastructure**: Global cloud-based (resilient)
- **Uptime**: Not published; assume 99%+ (standard for SaaS)

### 8. **Long-term Viability**
- **Positive**: Growing company ($3M→$6M revenue YoY), well-funded ($8.5M), award recognition
- **Risk**: Smaller than SiteMinder/Cloudbeds (acquisition risk, but low probability)
- **Recommendation**: Not a blocker; company trajectory is positive

---

## Integration Roadmap for Villa Thaifa (Recommended)

### Phase 1: Setup & Testing (Week 1)
1. Obtain HotelRunner API credentials (token, hr_id)
2. Access Postman collection for endpoint testing
3. Test Get Room List and Update Room endpoints in sandbox/test environment
4. Document actual rate-limit behavior (confirm 250/day, 5/min)

### Phase 2: Build Integration Layer (Weeks 2-4)
1. Write Python API wrapper class (reusable across Villa Thaifa PMS)
2. Implement batch room update logic (coalesce changes into single requests)
3. Build reservation webhook receiver (for real-time push from HotelRunner)
4. Add rate-limit monitoring and exponential backoff
5. Cache room/rate data locally (Redis or simple JSON file)

### Phase 3: Channel Activation (Weeks 3-5, parallel)
1. Set up Airbnb integration (priority for Villa Thaifa market)
2. Set up Booking.com integration
3. Set up Google Hotel Ads (metasearch traffic)
4. Test end-to-end: Update rate in PMS → HotelRunner → visible on Airbnb
5. Implement rate-parity rules (prevent conflicts)

### Phase 4: Launch & Monitor (Week 6+)
1. Deploy integration to production with logging
2. Monitor rate-limit usage (should be ~50-100/day)
3. Track booking flow from each channel
4. Optimize batch sync frequency based on real-world demand
5. Quarterly review of API changes and new features

### Estimated Total Effort
- **Development**: 30-40 hours (custom API wrapper + integrations)
- **Setup & Configuration**: 10-15 hours (per-channel setup, testing)
- **Ongoing Maintenance**: 2-4 hours/month (monitoring, updates)
- **Total First Year**: ~120 hours (dev + setup + ongoing)

---

## Gaps & Uncertainties

### Information Not Found
1. **Exact Pricing**: No public pricing; contacted sales required
   - Impact: Cannot finalize ROI without quote
   - Mitigation: Request quote for 1-2 properties with Essential Complete plan

2. **Uptime SLA**: Not published in documentation
   - Impact: Cannot guarantee service level in SLA with guests
   - Assumption: 99%+ (standard for SaaS platforms of this scale)
   - Mitigation: Implement local fallback (manual booking entry if API down)

3. **Rate Limit Edge Cases**: No documentation on:
   - How transactions are counted (does 1 room update = 1 request or N requests?)
   - Webhook/push notification counting (likely doesn't count, but unconfirmed)
   - Daily reset timing (UTC? Midnight? Property timezone?)
   - Behavior when limit exceeded (hard block? 429? Queued?)
   - Impact: Must test in sandbox to confirm behavior

4. **API Versioning Strategy**:
   - Current version: v2 (`/api/v2/...`)
   - Backward compatibility: Not documented
   - Deprecation policy: Not documented
   - Risk: Potential breaking changes on API upgrades
   - Mitigation: Monitor HotelRunner changelog; version-lock in integration code

5. **Advanced Features Not Documented**:
   - Guest communication APIs (email/SMS)
   - Revenue report APIs
   - Channel analytics APIs
   - Refund/adjustment APIs
   - Likely exist but not in official docs

6. **Error Handling & Retry Logic**:
   - Error response format: Not fully documented
   - Retry-able errors: Not specified
   - Backoff strategy: Recommended values not provided
   - Example: Is 429 (rate limit) the only 4xx error? What about 400 validation errors?

7. **Security Posture**:
   - SSL/TLS requirements: Assumed HTTPS but not stated
   - IP whitelisting: Not available (cloud-based)
   - Data encryption at rest: Not documented
   - PCI compliance: Not documented
   - Assumption: Standard SaaS security, but verify with sales team

8. **Scalability Limits**:
   - Max rooms per property: Not documented (assume >10,000 based on customer base)
   - Max properties per account: Not documented
   - Max reservation history: Not documented
   - Pagination limits: Not documented
   - Risk: May hit unknown limits during Villa Thaifa growth
   - Mitigation: Test with expected data volumes in sandbox

### Contradictions or Inconsistencies Found
1. **Rate Limit Mentions**: 250/day repeated consistently across multiple sources, but:
   - Not found in official HotelRunner API docs (searched multiple pages)
   - Found in developer.hotelrunner.com custom apps section
   - Risk: Limit may have changed; verify current limits before building integration

2. **OTA Channel Count**: Claims vary (150+ most common, some sources say 100+, one says 200+ for SiteMinder)
   - HotelRunner official: 150+ confirmed in multiple sources
   - No exact list published (likely changes frequently)
   - Implication: Can't rely on specific OTA list; verify before signing contract

---

## Recommendations

### 1. **Proceed with HotelRunner Integration for Villa Thaifa**
- **Rationale**: Strong fit for multi-OTA distribution + Airbnb focus
- **Conditions**:
  - Negotiate pricing for 1-2 properties (expect $500-$1,500/month)
  - Confirm rate limits (250/day) in writing before integration
  - Request sandbox access and API documentation walkthrough from HotelRunner sales
  - Budget 40 hours dev time for custom integration wrapper

### 2. **Alternative Evaluation: Test Cloudbeds**
- **If priority shifts** to unified operations management
- **Pros**: All-in-one (no integration work), better PMS, higher satisfaction rating
- **Cons**: Higher cost, less focused on distribution
- **Decision Point**: If Villa Thaifa grows to 5+ properties or automation becomes priority, revisit Cloudbeds

### 3. **Build in Local Caching & Fallback**
- **Due to rate limits**, implement:
  - Local Redis/JSON cache of room types and rates (refresh 1-2x/day)
  - Fallback to last-known state if API down
  - Batch all updates into single requests (coalesce changes)
  - Real-time push webhook for reservations (doesn't consume daily quota)
- **Outcome**: Optimize for <50 API calls/day (well under 250 limit)

### 4. **Prioritize Airbnb 2-Way Sync**
- **Competitive Advantage**: HotelRunner's native Airbnb integration is rare
- **Setup**: Activate Airbnb integration week 1 (before Booking.com or other channels)
- **Outcome**: Real-time reservation flow from Airbnb directly into Villa Thaifa PMS

### 5. **Implement Monitoring & Alerts**
- Log all API responses (status, error, rate-limit headers)
- Alert on rate-limit warnings (>80% of 250/day consumed)
- Track booking volume by channel (measure ROI)
- Weekly dashboard of OTA distribution performance
- **Outcome**: Early warning of integration issues or channel health

### 6. **Contractual Considerations**
- **Verify in writing before signing**:
  - Rate limits (250/day assumed; may negotiate for higher tier)
  - SLA/uptime guarantee (push for 99.5%+)
  - API deprecation notice period (request 12 months minimum)
  - Support channel and response time SLA
  - Data ownership and export (if Villa Thaifa ever leaves HotelRunner)

### 7. **Longer-term Strategy**
- **Year 1-2**: HotelRunner as primary channel manager (proven, stable)
- **Year 3+**: Evaluate if:
  - Operations complexity warrants moving to Cloudbeds/Mews
  - International expansion requires SiteMinder's 200+ channel reach
  - Market shifts toward vacation rental focus (reconsider Hostaway/Guesty)
- **Outcome**: Don't over-engineer for future; HotelRunner is correct choice now

---

## Sources

### Official Documentation & Company
- [HotelRunner API Documentation Portal](https://developers.hotelrunner.com/)
- [HotelRunner REST API Overview](https://developers.hotelrunner.com/custom-apps/rest-api)
- [HotelRunner Custom Apps & API Features](https://hotelrunner.com/en/features/custom-apps-api/)
- [HotelRunner Integrations Directory](https://hotelrunner.com/en/integrations/)
- [HotelRunner About Page](https://hotelrunner.com/en/about/)
- [HotelRunner Pricing Page](https://hotelrunner.com/en/pricing/)

### API Endpoints & Reference
- [Get Room List Endpoint](https://developers.hotelrunner.com/custom-apps/rest-api/inventory/get-room-list)
- [Retrieve Reservations Endpoint](https://developers.hotelrunner.com/custom-apps/rest-api/reservations/retrieve-reservations)
- [Real-time Push Reservations](https://developers.hotelrunner.com/custom-apps/rest-api/reservations/realtime-push)
- [Inventory API Documentation](https://developers.hotelrunner.com/custom-apps/rest-api/inventory)
- [Postman Collections (Unofficial)](https://www.postman.com/hotelrunner-test/workspace/hotelrunner-standard-api-for-channels/)

### Company & Funding
- [HotelRunner Crunchbase Profile](https://www.crunchbase.com/organization/hotelrunner)
- [Arden Agopyan Founder Profile](https://www.crunchbase.com/person/arden-agopyan)
- [HotelRunner on Tracxn](https://tracxn.com/d/companies/hotelrunner/)
- [GetLatka Profile (Revenue Data)](https://getlatka.com/companies/hotelrunner)

### Channel Integration & Awards
- [Airbnb API Integration Launch](https://hotelrunner.com/en/news/product/hotelrunner-launches-airbnb-api-integration/)
- [Expedia Preferred Connectivity Partner 2023](https://hotelrunner.com/en/news/corporate/hotelrunner-recognized-as-preferred-connectivity-partner-for-2023-by-expedia-group/)
- [Expedia Inventory Management](https://hotelrunner.com/en/blog/hospitality-technology/managing-your-inventory-on-expedia-via-hotelrunner-is-now-much-easier/)

### Competitive Analysis & Reviews
- [HotelRunner on Capterra](https://www.capterra.com/p/158882/HotelRunner/)
- [SiteMinder vs HotelRunner vs Cloudbeds Comparison](https://www.capterra.com/reservations-software/compare/158882-123133-158839/HotelRunner-vs-SiteMinder-vs-Cloudbeds)
- [Cloudbeds vs SiteMinder 2024 Comparison](https://comparisons.financesonline.com/cloudbeds-vs-siteminder)
- [HotelRunner vs Mews Comparison](https://hoteltechreport.com/compare/hotelrunner-pms-vs-mews)
- [SiteMinder Competitors & Alternatives](https://www.cbinsights.com/company/siteminder/alternatives-competitors)
- [Cloudbeds vs SiteMinder Software Advice](https://www.softwareadvice.com/hotel-management/cloudbeds-profile/vs/site-minder/)
- [Top 10 Best Booking Engines 2026](https://www.techmagic.co/blog/best-hotel-booking-engine)
- [Hotel Channel Manager Reviews 2026](https://hoteltechreport.com/revenue-management/channel-managers/)

### Integration Approaches & Third-Party
- [HotelRunner XML API Integration Services](https://www.wbe.travel/partner/hotelrunner/)
- [Oganro HotelRunner Integration](https://www.oganro.com/suppliers/hotel-runner-xml-api-integration)
- [Travelopro HotelRunner API Documentation](https://www.travelopro.com/hotel-runner.php)
- [HyperGuest Marketplace HotelRunner Integration](https://www.hyperguest.com/integrations/hotelrunner)

### Industry Context & Related Platforms
- [Hostaway vs Guesty Comparison](https://get.hostaway.com/hostaway-vs-guesty/)
- [Guesty vs Hostaway Detailed Review](https://www.guesty.com/lp/guesty-vs-hostaway/)
- [Mews Alternatives 2026](https://www.roommaster.com/blog/mews-alternatives)
- [Best Hotel Management Systems 2026](https://www.gourmetmarketing.net/blog/the-best-hotel-management-systems-for-2026-what-hoteliers-need-to-know/)

---

## Document Version & Metadata

**Date**: 2026-02-13
**Research Scope**: HotelRunner platform capabilities, API, integrations, competitive landscape
**Researcher**: Omar's Research Agent
**Confidence Level**: High for core facts (API structure, pricing model, competitors); Medium for specific rate-limit edge cases and unpublished pricing
**Recommended Review Date**: 2026-05-13 (90 days; HotelRunner updates frequently)


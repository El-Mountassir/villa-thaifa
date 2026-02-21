# Stakeholders — Villa Thaifa

> Unified stakeholder reference: profiles, contacts, decisions, and team structure.

## Overview

> **Quick Reference** for project stakeholders
> **Last Updated**: 2026-01-24
> **Read Time**: < 2 minutes

---

## 🎯 Project Overview

**Mission**: Digital transformation of Villa Thaifa from manual operations to optimized, automated systems
**Type**: Consulting / AI-First Workforce
**Timeline**: Dec 2025 → Ongoing
**Phase**: 1 - Stabilization & Cleanup

---

## 👥 Stakeholders

### 1. Client - Said Thaifa

**Role**: Owner & Operator of Villa Thaifa

| Field                 | Value                                                    |
| --------------------- | -------------------------------------------------------- |
| **Contact**           | <said_thaifa@hotmail.fr> / +212 661-134194 (WhatsApp ⭐) |
| **Age**               | 78 years                                                 |
| **Property**          | Villa Thaifa (12 rooms, 4★, Palmeraie Marrakech)         |
| **Platform Accounts** | HotelRunner, Booking.com (Owner access)                  |

**Key Facts**:

- 🏆 Booking.com rating: 9.3/10 ("Wonderful")
- 🎯 Business: Fully manual, everything memorized
- 💡 Goal: Reduce operational burden, optimize revenue
- 🚨 **Communication**: ALWAYS use vouvoiement (formal French), WhatsApp preferred
- 📅 Active client since December 2025

**⚠️ Critical Rule for Agents**: Scout → Report → Questions → Action
(Never ask for info without first reporting what you've discovered)

**📄 Detailed Profile**: [`data/admin/client/PROFILE.md`](../../data/admin/client/PROFILE.md)

---

### 2. Consultant - Omar El Mountassir

**Role**: CEO & Project Leader

| Field                 | Value                                                        |
| --------------------- | ------------------------------------------------------------ |
| **Contact**           | <omar@el-mountassir.com>                                     |
| **Responsibilities**  | Strategy, team leadership, client relations, final approvals |
| **Team**              | 17 AI agents + Claude (CTO)                                  |
| **Platform Accounts** | HotelRunner, Booking.com (Admin access)                      |

**Key Facts**:

- 🎯 Philosophy: "AI-First" - Agents are co-workers, not tools
- 🔐 Manages admin accounts for security & traceability
- ✅ Must approve all critical operations (pricing, platforms, client comm)
- 📊 Data-driven, systematic, documented decision-making

**📄 Detailed Profile**: [`profiles/OMAR-EL-MOUNTASSIR.md`](./profiles/OMAR-EL-MOUNTASSIR.md)

---

### 3. Technical Team - AI Agents

**CTO/Architect**: Claude (successive instances)
**Workforce**: 17 specialized AI agents

| Category    | Count | Function                              |
| ----------- | ----- | ------------------------------------- |
| Operations  | 4     | Pricing, reservations, calendar, sync |
| Technical   | 4     | Validation, browser, security, audits |
| Meta        | 7     | Research, reporting, documentation    |
| Hospitality | 2     | Guest communication, translation      |

**📄 Team Structure**: [`TEAM.md`](./TEAM.md)

---

## 🔗 Relationship Structure

```
Said Thaifa (Client/Owner)
    ↓ Mandate
Omar El Mountassir (Consultant/CEO)
    ↓ Leadership
Claude (CTO/Architect)
    ↓ Management
17 AI Agents (Specialized Workforce)
```

---

## ⚡ Decision Hierarchy

| Type                                   | Process                                                     |
| -------------------------------------- | ----------------------------------------------------------- |
| **Strategic** (Vision, Budget, Exit)   | Omar recommends → Said decides → Omar executes              |
| **Operational** (Pricing, OTAs, Setup) | Agents analyze → Claude validates → Omar approves → Execute |
| **Technical** (Architecture, Tools)    | Claude proposes → Omar validates → Execute                  |

---

## 🚨 Critical Rules for AI Agents

### Platform Operations

**ALWAYS** get Omar approval before:

- ❗ Modifying pricing, availability, or reservations
- ❗ Communicating with Said Thaifa
- ❗ Making budget or timeline decisions
- ❗ Executing platform changes

### Account Usage

- ✅ **USE**: Omar's admin accounts (<<omar@el-mountassir.com>)>
- ❌ **NEVER USE**: Said's owner accounts (unless explicit Omar approval)

### Platform Credentials

**Location**: `.env.local` (project root)
**Structure reference**: `.env.example`

**Quick access:**

1. Read `.env.local` file
2. Extract needed credentials (HOTELRUNNER*ADMIN\*\*, BOOKING*ADMIN\*\*)
3. Use admin accounts by default
4. Handle OTP/reCAPTCHA (request from Omar)

**⚠️ Security**: Never log, output, or store credentials. Read on demand only.

**📖 Full Guide**: [`../operations/CREDENTIALS.md`](../operations/CREDENTIALS.md)

### Communication with Said

**Required Protocol**:

1. ✅ Vouvoiement obligatoire (formal "vous")
2. ✅ WhatsApp preferred channel
3. ✅ Scout → Report → Questions → Action
4. ❌ NEVER ask questions without reporting findings first

### Emergency Protocol

If critical issue (platform bug, lost reservation, pricing error):

1. **STOP** all operations
2. **DOCUMENT** incident immediately
3. **NOTIFY** Omar
4. **WAIT** for instructions

---

## 📋 Quick Decision Guide for Agents

**Can Proceed Autonomously**:

- ✅ Research & analysis
- ✅ Documentation updates
- ✅ Non-critical bug fixes
- ✅ Internal reports

**Must Get Omar Approval**:

- ❗ All platform operations
- ❗ Client communications
- ❗ Financial decisions
- ❗ Timeline changes

---

## 📚 Documentation Map

| Need                | Document                                                                                |
| ------------------- | --------------------------------------------------------------------------------------- |
| **Who is Said?**    | [`data/admin/client/PROFILE.md`](../../data/admin/client/PROFILE.md) (detailed profile) |
| **Who is Omar?**    | [`profiles/OMAR-EL-MOUNTASSIR.md`](./profiles/OMAR-EL-MOUNTASSIR.md) (detailed profile) |
| **Team structure?** | [`TEAM.md`](./TEAM.md) (17 AI agents)                                                   |
| **What to do?**     | [`../../ROADMAP.md`](../../ROADMAP.md) (project plan)                                   |
| **Current tasks?**  | [`../../tasks/active.md`](../../tasks/active.md) (active work)                          |
| **How to work?**    | [`../project/standards/agents/`](../project/standards/agents/) (protocols)              |
| **Navigate docs?**  | [`INDEX.md`](./INDEX.md) (documentation index)                                          |

---

## ✅ Before Starting Any Task

**Checklist for AI Agents**:

1. ☐ Read this document (STAKEHOLDERS.md)?
2. ☐ Understand my role in the hierarchy?
3. ☐ Know if I need Omar approval?
4. ☐ Using correct accounts (admin vs owner)?
5. ☐ Respecting communication protocol with Said?
6. ☐ Ready to document my work?

**If ANY answer is NO → STOP and read the relevant documentation**

---

## 📞 Emergency Contacts

- **Omar El Mountassir**: +212 643 39 04 09 (Phone & WhatsApp) / <omar@el-mountassir.com>
- **Said Thaifa**: +212 661-134194 (Phone & WhatsApp) / <said_thaifa@hotmail.fr>

---

_Single Source of Truth for stakeholder relationships_
_For detailed profiles, see [`profiles/`](./profiles/) directory_
_Last updated: 2026-01-24 by Omar El Mountassir_

---

## Contact Information

- **Relation**: New potential client (high-ticket)

## Primary

| Field    | Value                    |
| -------- | ------------------------ |
| Name     | Said Thaifa              |
| Age      | 78 years                 |
| WhatsApp | +212 661-134194          |
| Email    | <said_thaifa@hotmail.fr> |
| Email    | <saidthaifa@gmail.com>   |

### Spoken Languages

| Language | Level  |
| -------- | ------ |
| Arabic   | Native |
| French   | Fluent |
| English  | Basic  |
| Dutch    | Fluent |

## Secondary

| Field | Value                           |
| ----- | ------------------------------- |
| Name  | Nezha Thaifa                    |
| Role  | Co-manager / Wife of Mr. Said   |
| Note  | Warm welcome, hearty breakfasts |

> **Reputation**: Appreciated for her hospitality, contributing to a relaxed and comfortable atmosphere for travelers. Reviews mention a "family-like" atmosphere.

## Property

| Field | Value              |
| ----- | ------------------ |
| Name  | Villa Thaifa       |
| Type  | Guest house        |
| City  | Marrakech, Morocco |
| Rooms | 12                 |

> Source: Booking.com property profile

---

## Notes

- Formal communication
- Senior client — respect without rigidity
- Said and Nezha co-manage the Villa together

### Communication Channels

> **SYSTEM PROMPT**: To be strictly followed for any interaction with Said Thaifa.
> **Last updated**: 2026-01-24
> **Priority**: P1 (critical)

---

## 📞 Channels

| Channel      | Usage       | Details                                        |
| ------------ | ----------- | ---------------------------------------------- |
| **WhatsApp** | **PRIMARY** | "Action-Reaction" Channel (See protocol below) |
| Email        | Secondary   | For monthly / official reports                 |
| Phone        | Emergency   | +212 661-134194                                |
| In person    | Rare        | Strategic meetings                             |

---

## 📝 Templates (Reports)

### Weekly Report (Internal/Email)

```markdown
## Week of [DATE]

### ✅ Accomplished

- TODO

### 🔄 In progress

- TODO

### ⚠️ Issues

- TODO

### 📅 Next week

- TODO
```

---

## 🎯 INTERACTION PROTOCOL (WhatsApp - "Dutch First")

### 1. CONTEXT & ROLE

You act as **"Omar El Mountassir" (Hybrid Agentic Workforce)** for the client Said Thaifa (owner of Villa Thaifa, 78 years old, 9.3/10 rating).

**Your goal**: Act as a **"Digital Steward"**. You handle the technical complexity (HotelRunner, Booking) to provide him with peace of mind.

### 2. GOLDEN RULES

#### Rule #1: "Dutch First" with Mirror Validation

The language for interacting with Said is **Dutch**, but Omar must validate the content.
You must **IMPERATIVELY** generate each response in two distinct blocks:

1. 🇳🇱 **MESSAGE TO SEND (Dutch)**: The final optimized message, ready to be copy-pasted for Said.
2. 🇫🇷 **VALIDATION (French)**: The exact translation or substantial summary so Omar can unambiguously validate the action.

> **Security clause**: If Said asks a complex strategic question in French, you may answer in French for clarity, then conclude in Dutch.

#### Rule #2: "Action-Reaction" Structure

Never say "I will do it". Say "**It's done**".

- ❌ **Bad**: "Ik zal kijken..." (I'll look into it...)
- ✅ **Good**: "Genoteerd, ik ben ermee bezig." (Noted, I'm on it.)
- ✅ **Excellent**: "Missie voltooid ✅. Data geblokkeerd." (Mission accomplished. Dates blocked.)

#### Rule #3: Visual & Compact

- Use bullet points.
- Use Emojis: ✅ (Gedaan), 🔒 (Geblokkeerd), 💶 (Prijs).
- **Bold** for dates and prices.

#### Rule #4: Error Management (S.A.P)

- **Situatie**: "De data stonden nog open."
- **Actie**: "Ik heb dit handmatig geblokkeerd."
- **Plan**: "Ik neem contact op met support."

### 3. RESPONSE TEMPLATES

**SCENARIO A: Block / Close Dates**

> **🇳🇱 MESSAGE**
> "Salam Si Said,
> Missie voltooid ✅.
> Ik heb Kamer 4 geblokkeerd voor de gevraagde data:
> 📅 **Van 08 maart tot 12 maart**
> Geen risico meer op dubbele boekingen.
> Fijne dag! 🙏"

**SCENARIO B: Pricing**

> **🇳🇱 MESSAGE**
> "Het is geregeld Si Said.
> Update uitgevoerd:
> 🏠 **Presidentiële Suite**
> 💶 Nieuw tarief: **€ 449**
> Direct gesynchroniseerd. Alles is in orde! 👍"

**SCENARIO C: Reception / Acknowledgment**

> **🇳🇱 MESSAGE**
> "Goed ontvangen Si Said! 🙏
> Ik download de bestanden en ga er direct mee aan de slag."

---

## 5. TONE & STYLE

- **Greeting**: "Salam Si Said" or "Goedendag Si Said".
- **Closing**: "Mijn vriend", "Fijne avond", "Tot uw dienst".
- **Key vocabulary**: `Missie voltooid`, `Alles is in orde`, `Geen zorgen`.

---

**Tags**: `protocol` `communication` `dutch` `client`

---

## Profiles

### Said Thaifa — Owner

> **Quick Reference**: See [../STAKEHOLDERS.md](../STAKEHOLDERS.md) for overview
> **Related**: [OMAR-EL-MOUNTASSIR.md](./OMAR-EL-MOUNTASSIR.md) (Consultant profile)
> **Last Updated**: 2026-01-24 (Refactored from legacy/archive_v1/admin/client/PROFILE.md)

---

## Document Status

| Field                 | Value                                   |
| --------------------- | --------------------------------------- |
| **Client Status**     | Active - Digital Transformation Project |
| **Project Phase**     | Phase 1 - Stabilization & Cleanup       |
| **Priority**          | HIGH                                    |
| **Created**           | 2025-12-19                              |
| **Last Major Update** | 2025-12-20                              |
| **Refactored**        | 2026-01-24                              |

---

## 1. Executive Snapshot

### Key KPIs

| Metric                 | Value                               | Note                            |
| ---------------------- | ----------------------------------- | ------------------------------- |
| **Rooms**              | 12                                  | 8 types on Booking.com          |
| **Booking Rating**     | 9.3/10 (80 reviews)                 | "Wonderful"                     |
| **Booking Commission** | 25%                                 | High (standard = 15%)           |
| **PMS**                | None                                | Everything in Mr. Thaifa's head |
| **Channel Manager**    | HotelRunner                         | Active since 2025-12            |
| **OTAs**               | Booking ✅ / Airbnb ⏳ / Expedia ⏳ | Setup in progress               |

### Detailed Booking.com Scores

| Category            | Score | Level       |
| ------------------- | ----- | ----------- |
| **Staff**           | 9.7   | Exceptional |
| **Cleanliness**     | 9.4   | Excellent   |
| **Comfort**         | 9.4   | Excellent   |
| **Facilities**      | 9.3   | Excellent   |
| **Value for money** | 8.9   | Very good   |
| **WiFi**            | 8.8   | Very good   |
| **Location**        | 8.2   | Good        |
| **Breakfast**       | 10    | Perfect     |

> **Major strength**: Staff rated 9.7/10 and perfect breakfast 10/10

### Current Operational Status

| Metric                            | Value      |
| --------------------------------- | ---------- |
| **Confirmed reservations**        | 11         |
| **Expected revenue**              | €8,008.85  |
| **Peak occupancy (Dec 29-31)**    | 50% (6/12) |
| **Prices configured HotelRunner** | 0/9 types  |
| **Active promotions Booking**     | 5 (10-15%) |

→ See `data/` for operational details

---

## 2. Contact & Communication

### 2.1 Primary Contact

| Field        | Value                    |
| ------------ | ------------------------ |
| **Name**     | Said Thaifa              |
| **Age**      | 78 years                 |
| **Email**    | <said_thaifa@hotmail.fr> |
| **Email**    | <saidthaifa@gmail.com>   |
| **Phone**    | +212 661-134194          |
| **WhatsApp** | +212 661-134194          |

**Professional background**:

- Owner and host of Villa Thaifa (with his wife Nezha)
- CEO / Real estate agent in Marrakech
- Specialties: sales, purchases, seasonal rentals
- Reputation: warm welcome, making clients feel "at home"

### 2.2 Communication Protocol

| Rule         | Detail                                                      |
| ------------ | ----------------------------------------------------------- |
| **Tone**     | Formal & Direct ("Action-Reaction")                         |
| **Language** | **DUTCH FIRST**                                             |
| **Format**   | Dual output (NL for him, FR for Omar)                       |
| **Standard** | 👉 [COMMUNICATION.md](../knowledge/client/COMMUNICATION.md) |

### 2.3 Communication Pattern

```text
1. SCOUT    → Explore, verify feasibility
2. REPORT   → Keep the client informed of discoveries
3. QUESTIONS → Ask for missing info (with context)
4. ACTION   → Execute when everything is clear
```

> **Golden rule**: Never ask for info without first reporting what was discovered.

→ See `docs/lessons-learned.md` for documented patterns

---

## 3. Property

### 3.1 General Information

| Field          | Value                                         |
| -------------- | --------------------------------------------- |
| **Name**       | Villa Thaifa (sometimes "Villa Thaifa & SPA") |
| **Type**       | Boutique guest house / B&B (4★)               |
| **Address**    | Route de Fès, Km 12                           |
| **Area**       | Palmeraie / Ouled Jelal (12-14 km center)     |
| **City**       | Marrakech, Morocco                            |
| **Rooms**      | 12                                            |
| **Renovation** | Recently renovated                            |

### 3.2 Facilities & Services

| Category       | Details                                                 |
| -------------- | ------------------------------------------------------- |
| **Relaxation** | Infinity pool (open year-round), garden, solarium       |
| **Wellness**   | Spa/Hammam, massages (surcharge)                        |
| **Restaurant** | "Thaifa's restaurant" — Moroccan cuisine                |
| **Cuisine**    | Moroccan (halal, vegetarian) — "Best tagine in Morocco" |
| **Rooms**      | Air conditioning, heating, satellite TV, Wi-Fi, terrace |
| **Services**   | Free parking, airport shuttle, car rental               |
| **Security**   | 24/7, CCTV, safe, alarm                                 |
| **Languages**  | Arabic, English, French, Dutch                          |

### Breakfast (Score 10/10)

| Attribute | Value                                                            |
| --------- | ---------------------------------------------------------------- |
| **Price** | MAD 160.90/person                                                |
| **Hours** | 08:30 - 11:00                                                    |
| **Type**  | Continental, Halal                                               |
| **Menu**  | Pastries, bread, pancakes, eggs, cheese, local specialties, jams |

### 3.3 Positioning & Reputation

| Aspect             | Value                                                           |
| ------------------ | --------------------------------------------------------------- |
| **Price range**    | 160-600 €/night (depending on type)                             |
| **Reputation**     | Very good (9.3/10 Booking)                                      |
| **Strengths**      | Quiet, gardens, infinity pool, warm welcome ("feeling at home") |
| **Location asset** | Quiet and peaceful, away from city noise (14 km from center)    |

→ See `data/rooms/rooms.md` for room details and pricing

---

## 4. Business Context

### 4.1 Confirmed Facts ✅

| Fact                | Detail                                          |
| ------------------- | ----------------------------------------------- |
| **Current PMS**     | None — Everything happens in Mr. Thaifa's head  |
| **Channel Manager** | HotelRunner (active since Dec 2025)             |
| **Booking.com**     | In place (25% commission)                       |
| **Airbnb**          | Awaiting setup                                  |
| **Expedia Partner** | Awaiting setup                                  |
| **Client Rating**   | 9.3/10 on Booking — Excellent                   |
| **Staffing**        | Difficulty finding qualified employees (luxury) |
| **Promotions**      | 5 active (10-15%) — Audit performed Dec 20      |

### 4.2 Key Questions for Meeting ⏳ (Monday, Dec 22, 10am)

**Needs to prioritize:**

| #   | Potential need                                             | Priority to validate |
| --- | ---------------------------------------------------------- | -------------------- |
| 1   | Management of booking platforms (Booking, Airbnb, Expedia) | ❓                   |
| 2   | Increase occupancy rate                                    | ❓                   |
| 3   | Stabilize pricing grid / adapt to competition              | ❓                   |
| 4   | Top SEO for "Villa Thaifa"                                 | ❓                   |
| 5   | Quality website                                            | ❓                   |
| 6   | Dynamic pricing (season, occupancy, competition)           | ❓                   |
| 7   | Property Management System (PMS)                           | ❓                   |

**Other questions:**

| Question            | Expected answer       |
| ------------------- | --------------------- |
| Approximate budget? | To be determined      |
| Desired timeline?   | "As soon as possible" |
| Long-term vision?   | Keep / Sell / Rent?   |

### 4.3 Main Pain Points

| Pain                  | Impact                                                  | Potential solution                  |
| --------------------- | ------------------------------------------------------- | ----------------------------------- |
| **Recruitment**       | Hard to find qualified employees for luxury positioning | Training? School partnerships?      |
| **Positioning**       | Ambition to truly position as luxury (evidence: 9.3/10) | Premium pricing + communication     |
| **Manual management** | Everything in Mr. Thaifa's head                         | PMS adapted for small structure     |
| **OTA Dependency**    | 100% Booking.com currently                              | Diversify (Airbnb, Expedia, direct) |
| **High commission**   | 25% Booking (vs 15% standard)                           | Negotiate medium-term               |

### 4.4 Identified Opportunities

**Short term (Q1 2026):**

| Opportunity                      | Impact            | Effort | Priority |
| -------------------------------- | ----------------- | ------ | -------- |
| Configure HotelRunner pricing    | Immediate revenue | Low    | 🔴 P0    |
| Setup Airbnb/Expedia             | Diversification   | Medium | 🟠 P1    |
| Adapted PMS (Hotelogix or other) | Efficiency        | Medium | 🟠 P1    |
| Reporting automation             | Visibility        | Low    | 🟢 P2    |

**Long term (2026+):**

| Opportunity                        | Note                                 |
| ---------------------------------- | ------------------------------------ |
| Website + Direct booking engine    | Via HotelRunner? Source code access? |
| Jisr l'Mokawala (Go Siyaha portal) | Brief prepared — investigate P3      |
| Direct sale without middleman      | Mr. Thaifa "is tired of managing"    |
| Lease to a competent company       | Alternative to selling               |

---

## 5. Competitive Analysis

### 5.1 Palmeraie Market

| Segment          | Price/night | Typical Rating | Characteristics                 |
| ---------------- | ----------- | -------------- | ------------------------------- |
| **Standard**     | 80-150€     | 8.0-8.5        | Basic B&B, few services         |
| **Premium**      | 150-280€    | 8.5-9.0        | Pool, spa, restaurant           |
| **Luxury**       | 280-500€    | 9.0+           | Suites, exclusive experience    |
| **Ultra-luxury** | 500€+       | 9.5+           | Private villas, dedicated staff |

### 5.2 Villa Thaifa Positioning

| Criterion    | Villa Thaifa          | Position          |
| ------------ | --------------------- | ----------------- |
| **Price**    | 160-600€              | Premium → Luxury  |
| **Rating**   | 9.3/10                | Top 10% Palmeraie |
| **Rooms**    | 12                    | Medium size       |
| **Services** | Pool, spa, restaurant | Full premium      |

**Competitive advantage:** Exceptional rating (9.3) + quiet Palmeraie positioning

→ Detailed benchmark: research in progress

---

## 6. Financial Baseline

### 6.1 Revenue Models

| Occupancy rate | Nights/year | Gross Revenue | After commission (25%) |
| -------------- | ----------- | ------------- | ---------------------- |
| **50%**        | 2,190       | ~€438,000     | ~€328,500              |
| **70%**        | 3,066       | ~€613,200     | ~€459,900              |
| **90%**        | 3,942       | ~€788,400     | ~€591,300              |

_Base: 12 rooms × 365 days × average price ~200€_

### 6.2 Commission Impact

| OTA                      | Commission | On €100 gross | Net  |
| ------------------------ | ---------- | ------------- | ---- |
| **Booking.com current**  | 25%        | -€25          | €75  |
| **Booking.com standard** | 15%        | -€15          | €85  |
| **Airbnb**               | ~15%       | -€15          | €85  |
| **Direct**               | 0%         | €0            | €100 |

**Opportunity:** Reduce Booking dependency + negotiate commission

### 6.3 RevPAR Objectives

| KPI           | Current     | Target Q1 2026 | Target 2026 |
| ------------- | ----------- | -------------- | ----------- |
| **Occupancy** | ~50% (peak) | 60%            | 70%         |
| **ADR**       | ~€200       | €220           | €250        |
| **RevPAR**    | ~€100       | €132           | €175        |

---

## 7. Technical Stack

### 7.1 Current State

| Component           | Solution              | Status                     |
| ------------------- | --------------------- | -------------------------- |
| **PMS**             | None (manual)         | ❌ Critical                |
| **Channel Manager** | HotelRunner           | ✅ Active                  |
| **Primary OTA**     | Booking.com           | ✅ Active (25% commission) |
| **Secondary OTAs**  | Airbnb, Expedia       | ⏳ Pending                 |
| **Website**         | Non-existent or basic | ❓ To verify               |
| **Booking engine**  | None                  | ⏳ HotelRunner?            |

### 7.2 Constraints & Challenges

- No tech training for Mr. Thaifa (78 years old)
- Need simple, intuitive solution
- No dedicated IT staff
- Budget to be defined

### 7.3 Proposed Integrations

| Solution                      | Function                           | Priority           |
| ----------------------------- | ---------------------------------- | ------------------ |
| **Hotelogix** (or equivalent) | PMS adapted for small structure    | P1                 |
| **HotelRunner**               | Channel Manager + Booking engine   | P0 (in progress)   |
| **Jisr l'Mokawala**           | Direct bookings (GO Siyaha portal) | P3 (investigation) |

---

## 8. Risks & Mitigation

| Risk                       | Probability | Impact | Mitigation                 |
| -------------------------- | ----------- | ------ | -------------------------- |
| **Booking.com dependency** | High        | High   | Diversify OTAs + direct    |
| **Qualified staffing**     | High        | Medium | Training partnerships      |
| **Tech adoption**          | Medium      | Medium | Simple solutions, training |
| **Seasonality**            | High        | Medium | Dynamic pricing, events    |
| **Owner fatigue**          | Medium      | High   | Gradual delegation         |

---

## 9. Success Metrics

### 9.1 KPIs to Establish at Meeting

| KPI                   | Baseline | 6-month target | How to measure                |
| --------------------- | -------- | -------------- | ----------------------------- |
| Average commission    | 25%      | 20%            | Negotiation + diversification |
| % direct bookings     | 0%       | 10%            | Booking engine + SEO          |
| Annual occupancy rate | ~50%     | 60%            | HotelRunner reports           |
| Booking rating        | 9.3/10   | Maintain >9.0  | Booking dashboard             |
| Staff turnover        | ❓       | Reduce         | Define with Mr. Thaifa        |

### 9.2 Mission Success Criteria

| Criterion       | Definition                                    |
| --------------- | --------------------------------------------- |
| **Operational** | All reservations assigned, pricing configured |
| **Technical**   | HotelRunner functional, OTAs synchronized     |
| **Strategic**   | 2026 plan validated, budget approved          |
| **Relational**  | Mr. Thaifa's trust established                |

---

## 10. Engagement & Timeline

### 10.1 History

| Date       | Event                               | Status         |
| ---------- | ----------------------------------- | -------------- |
| 2025-12-19 | First contact                       | ✅ Done        |
| 2025-12-20 | Audit promotions + pricing strategy | ✅ Done        |
| 2025-12-20 | Setup HotelRunner (partial)         | ⏳ In progress |

### 10.2 Next Steps

| Date               | Event                         | Objective                        |
| ------------------ | ----------------------------- | -------------------------------- |
| **2025-12-22 10h** | Discovery meeting Mr. Thaifa  | Validate needs, budget, timeline |
| 2025-12-22 PM      | Document decisions            | Update PROFILE.md                |
| 2025-12-23-24      | Commercial proposal           | Create quote                     |
| 2025-12-25-28      | Assign reservations           | 10 rooms to assign               |
| 2026-01            | Jisr l'Mokawala investigation | Feasibility                      |

### 10.3 Proposed Milestones

| Milestone               | Target date  | Deliverables                          |
| ----------------------- | ------------ | ------------------------------------- |
| **M1: Complete setup**  | Dec 31, 2025 | HotelRunner configured, active prices |
| **M2: Diversification** | Jan 31, 2026 | Airbnb + Expedia active               |
| **M3: PMS**             | Feb 28, 2026 | PMS solution chosen + deployed        |
| **M4: Direct booking**  | Mar 31, 2026 | Booking engine + basic SEO            |

---

## 11. Strategic Opportunities (Long Term)

### Vision 2026+

| Scenario         | Description                      | Probability |
| ---------------- | -------------------------------- | ----------- |
| **Optimization** | Mr. Thaifa keeps it, we optimize | High        |
| **Delegation**   | Lease to competent company       | Medium      |
| **Exit**         | Direct sale (without middleman)  | Low         |

### Growth Levers

1. **Direct bookings** — Reduce OTA commission
2. **Upselling** — Spa, transport, excursions
3. **Events** — Weddings, corporate retreats
4. **Loyalty** — Returning customer program

---

## 12. References

### 12.1 Linked Documents

| Folder                         | Content                |
| ------------------------------ | ---------------------- |
| `data/communication/whatsapp/` | Ready-to-send messages |
| `archive/2025/Q4/`             | Archives and history   |

### 12.2 Operational State (SSOT)

| File                               | Content                             |
| ---------------------------------- | ----------------------------------- |
| `data/rooms/rooms.md`        | Rooms, pricing, HotelRunner mapping |
| `data/bookings/reservations/reservations.md` | Confirmed reservations              |
| `data/finance/rates.json` | Active promotions                   |

### 12.3 Documentation

| File                      | Content                             |
| ------------------------- | ----------------------------------- |
| `docs/lessons-learned.md` | 3 documented communication patterns |
| `CLAUDE.md`               | AI agents instructions              |

### 12.4 Industry Resources

- [Hotelogix - 8 Must-Have PMS Reports](https://blog.hotelogix.com/hotel-reservation-report/)
- [Villa Palmeraie Marrakech - Booking.com](https://www.booking.com/hotel/ma/villa-palmeraie-marrakech-marrakech1.html)
- [Villa Al Assala Palmeraie - Booking.com](https://www.booking.com/hotel/ma/villa-al-assala-palmeraie.html)

---

## Industry Glossary

| Term                | Definition                                                     |
| ------------------- | -------------------------------------------------------------- |
| **PMS**             | Property Management System — Hotel management software         |
| **OTA**             | Online Travel Agency — Platforms like Booking, Airbnb, Expedia |
| **Channel Manager** | Tool synchronizing availability across all OTAs                |
| **ADR**             | Average Daily Rate — Average revenue per paid occupied room    |
| **RevPAR**          | Revenue Per Available Room                                     |
| **SSOT**            | Single Source of Truth                                         |

---

## Internal Notes

```text
[2025-12-19] Client folder created. Monday meeting to be confirmed.
[2025-12-20] Profile optimization v1 via /elevate.
[2025-12-20] Profile reorganization v2 — 12-section structure.
             Backup: .backup/PROFILE-2025-12-20-v2-before-reorg.md
```

---

## See Also

- [../STAKEHOLDERS.md](../STAKEHOLDERS.md) - Quick reference for all stakeholders
- [OMAR-EL-MOUNTASSIR.md](./OMAR-EL-MOUNTASSIR.md) - Consultant profile
- [../INDEX.md](../INDEX.md) - Documentation navigation guide

---

_Detailed client profile - Part of docs/leadership/profiles/_
_Original: legacy/archive_v1/admin/client/PROFILE.md (2025-12-20)_
_Refactored: 2026-01-24 - Moved to new structure, cross-references added_

### Omar El Mountassir — Admin/Consultant

> **Role**: CEO & Leader - Villa Thaifa Digital Transformation Project
> **Last Updated**: 2026-01-24

---

## 🎯 Overview

**Name**: Omar El Mountassir
**Role**: Digital Transformation Consultant & Project Leader
**Client**: Said Thaifa (Villa Thaifa owner)
**Project Start**: December 2025
**Project Type**: Digital Transformation & Operational Optimization

---

## 📧 Contact Information

| Field     | Value                           |
| --------- | ------------------------------- |
| **Email** | <omar@el-mountassir.com>        |
| **Role**  | CEO, Strategist, Project Leader |

---

## 👔 Professional Role

### Primary Responsibilities

1. **Strategic Leadership**
   - Overall project vision and direction
   - Client relationship management with Said Thaifa
   - Budget and timeline approval
   - Final decision authority on all deliverables

2. **Team Management**
   - Leadership of 17 specialized AI agents
   - Claude (CTO/Architect) supervision
   - Agent performance monitoring
   - Workflow optimization

3. **Client Interface**
   - Main point of contact with Said Thaifa
   - Requirements gathering and validation
   - Progress reporting
   - Decision approval and implementation

4. **Quality Assurance**
   - Review and validation of all platform operations
   - Security and compliance oversight
   - Documentation standards enforcement
   - Deliverable quality control

---

## 🏗️ Project Context

### Mission

Transform Villa Thaifa's operations from fully manual (everything in Said's head) to digitally optimized with:

- Professional PMS (Property Management System)
- Multi-channel distribution (Booking, Airbnb, Expedia)
- Automated pricing and revenue optimization
- Reduced operational burden on 78-year-old owner

### Approach

**Philosophy**: "AI-First"

- AI agents are co-workers, not tools
- Autonomous execution with human supervision
- Systematic documentation and handovers
- Continuous improvement through agent collaboration

**Methodology**: Scout → Report → Questions → Action

- Never ask questions without first reporting findings
- Always provide context before requesting information
- Validate before executing
- Document everything

---

## 🔐 Platform Access

### Admin Accounts (Primary Use)

**HotelRunner**:

- Email: <omar@el-mountassir.com>
- Role: Admin/Manager
- Purpose: Daily operations, configuration, management

**Booking.com**:

- Email: <omar@el-mountassir.com>
- Role: Admin/Manager
- Purpose: Property management, updates, analytics

### Owner Accounts (Reference Only)

**Said Thaifa's Accounts**:

- HotelRunner: <said_thaifa@hotmail.fr>
- Booking.com: <said_thaifa@hotmail.fr>

**⚠️ CRITICAL**: Use Said's accounts ONLY with explicit approval from Omar

---

## 🎯 Decision Authority

### Decision Hierarchy

**Strategic Decisions** (Vision, Budget, Exit Strategy):

```
Omar analyzes & recommends → Said decides → Omar executes
```

**Operational Decisions** (Pricing, OTAs, Setup):

```
AI agents analyze → Claude validates → Omar approves → (Said informed) → Execute
```

**Technical Decisions** (Architecture, Stack, Tools):

```
Claude proposes → Omar validates → Execute autonomously
```

### Approval Requirements

**Omar Must Approve**:

- ✅ All platform operations (pricing, reservations, availability)
- ✅ Client communications (Said Thaifa)
- ✅ Budget allocations
- ✅ Timeline changes
- ✅ Vendor selection (PMS, tools, services)

**Omar Can Delegate** (to Claude/Agents):

- ✅ Research and analysis
- ✅ Documentation
- ✅ Technical implementation
- ✅ Reporting and monitoring
- ✅ Non-critical automation

**Omar Does NOT Handle** (Said's Domain):

- ❌ Guest relations (direct)
- ❌ On-site operations
- ❌ Staff management
- ❌ Final strategic vision

---

## 🤝 Relationship with Said Thaifa

### Communication Protocol

**Tone**: Professional, respectful, consultative
**Method**: WhatsApp preferred (Said's preference)
**Pattern**: Scout → Report → Questions → Action

**Golden Rule**: Always report findings BEFORE asking for additional information

### Roles Clarity

| Aspect         | Said (Client) | Omar (Consultant) |
| -------------- | ------------- | ----------------- |
| **Ownership**  | 100%          | 0% (consultant)   |
| **Vision**     | Decides       | Advises           |
| **Execution**  | Delegates     | Manages           |
| **Operations** | Informs       | Implements        |
| **Budget**     | Approves      | Proposes          |
| **Success**    | Benefits      | Delivers          |

---

## 🚀 Project Objectives & KPIs

### Short Term (Q1 2026)

- ✅ HotelRunner fully configured with accurate pricing
- ✅ Airbnb and Expedia channels active
- ✅ PMS selected and implemented
- ✅ Commission reduced from 25% to 20%
- ✅ Operational burden reduced 50%

### Medium Term (2026)

- ✅ 70% occupancy rate achieved
- ✅ 10% direct bookings (bypass OTAs)
- ✅ Dynamic pricing implemented
- ✅ Stable qualified staff in place
- ✅ Automated reporting systems

### Long Term (Beyond 2026)

Support Said's chosen path:

- **Option A**: Delegation to professional management company
- **Option B**: Direct sale (no intermediary)
- **Option C**: Continued optimization with tech support

### Success Metrics

| KPI                    | Baseline    | Target        |
| ---------------------- | ----------- | ------------- |
| **Operational Load**   | 100% manual | -50%          |
| **Revenue**            | Current     | +20%          |
| **OTA Commission**     | 25%         | 20%           |
| **Booking.com Rating** | 9.3/10      | Maintain 9.0+ |
| **Direct Bookings**    | 0%          | 10%           |
| **Occupancy Rate**     | ~50%        | 70%           |

---

## 🛠️ Technical Leadership

### Team Structure

**Under Omar's Leadership**:

1. **Claude** (CTO/Architect)
   - Technical architecture
   - Agent coordination
   - System design

2. **17 AI Agents** (Specialized Workforce)
   - 4 Operations agents
   - 4 Technical agents
   - 7 Meta agents
   - 2 Hospitality agents

**Reference**: [`docs/leadership/TEAM.md`](../TEAM.md)

### Workflow Management

- **Daily**: Agent outputs review
- **Weekly**: Progress sync with Claude
- **Bi-weekly**: Client update to Said
- **Monthly**: KPI review and adjustment

---

## 📋 Current Project Phase

**Phase**: 1 - Stabilization & Cleanup
**Status**: Active
**Focus**:

- Rescue and migrate data
- Fix platform configurations
- Establish baseline systems
- Create solid documentation foundation

**Roadmap**: [`ROADMAP.md`](../../ROADMAP.md)
**Active Tasks**: [`tasks/active.md`](../../tasks/active.md)

---

## 🔒 Security & Compliance

### Access Control

**Omar's Responsibility**:

- Secure credential management
- Platform access governance
- Agent permission levels
- Data privacy compliance

**Never Share**:

- ❌ Platform passwords
- ❌ API keys
- ❌ Client personal data
- ❌ Financial information

### Audit Trail

All operations must be:

- ✅ Documented in git commits
- ✅ Logged in appropriate tools
- ✅ Reviewable by Omar
- ✅ Traceable to specific agent/action

---

## 📚 Work Style & Preferences

### Decision Making

- **Data-driven**: Prefer metrics over opinions
- **Systematic**: Process > ad-hoc solutions
- **Documented**: Everything must be written
- **Validated**: Double-check before execution

### Communication Style

- **Concise**: Clear, to the point
- **Structured**: Organized information
- **Actionable**: Always include next steps
- **Transparent**: No surprises

### Quality Standards

- **Excellence**: Aim for 9.0+ quality (like Said's rating)
- **Reliability**: Systems must work consistently
- **Maintainability**: Future agents can understand
- **Scalability**: Can grow with business

---

## 🎓 Learning & Adaptation

### Continuous Improvement

Omar expects:

- Regular agent performance reviews
- Process optimization suggestions
- Technology updates consideration
- Best practices research

### Feedback Loops

- Agents report findings and blockers
- Claude proposes architecture improvements
- Omar validates and approves changes
- Documentation updated accordingly

---

## 🚨 For AI Agents: Working with Omar

### What Omar Expects

1. **Autonomous Execution**
   - Don't ask for every small decision
   - Use judgment within your domain
   - But validate critical operations

2. **Clear Communication**
   - Summary upfront, details after
   - Highlight blockers immediately
   - Propose solutions, not just problems

3. **Documented Work**
   - Git commits for all changes
   - Handovers when switching context
   - Decisions logged with rationale

4. **Quality Focus**
   - Double-check before executing
   - Test when possible
   - Never guess - research or ask

### When to Escalate to Omar

**Always Escalate**:

- ❗ Platform operations (pricing, availability, reservations)
- ❗ Client communication with Said
- ❗ Budget/financial decisions
- ❗ Timeline changes
- ❗ Critical errors or incidents

**Can Proceed Autonomously**:

- ✅ Research and analysis
- ✅ Documentation updates
- ✅ Internal tool usage
- ✅ Non-critical bug fixes

### Communication Format

**Good**:

```
Subject: [Agent-Name] Brief summary of topic

Context: What led to this situation
Finding: What was discovered
Recommendation: Proposed action
Request: What you need from Omar

Next: What happens after approval
```

**Bad**:

```
"Hey, what should I do about X?"
(No context, no research, no proposal)
```

---

## 📞 Contact & Availability

**Email**: <omar@el-mountassir.com>

**Response Time**:

- Critical issues: Within 2 hours
- Standard requests: Within 24 hours
- Research/analysis: As appropriate

**Escalation Path**:

1. Agent identifies issue
2. Claude (CTO) reviews
3. Omar decides
4. Execution proceeds

---

## 🔗 Related Documentation

| Document                                | Purpose                                        |
| --------------------------------------- | ---------------------------------------------- |
| [`STAKEHOLDERS.md`](../STAKEHOLDERS.md) | Overview of all stakeholders and relationships |
| [`SAID-THAIFA.md`](./SAID-THAIFA.md)    | Detailed client profile                        |
| [`TEAM.md`](../TEAM.md)                 | AI agent team structure                        |
| [`ROADMAP.md`](../../ROADMAP.md)        | Project roadmap and milestones                 |

---

_Profile created: 2026-01-24_
_Last updated: 2026-01-24_
_Document owner: Omar El Mountassir_

---

## Detailed Client Profile

> **Status:** Lead (RDV planifié)
> **Priority:** HIGH
> **Next:** RDV découverte — Lundi 22 décembre 2025, 10h (Done)
> **Created:** 2025-12-19
> **Last Updated:** 2025-12-20

---

## 1. Executive Snapshot

### Key KPIs

| Metric                 | Value                               | Note                            |
| ---------------------- | ----------------------------------- | ------------------------------- |
| **Rooms**              | 12                                  | 8 types on Booking.com          |
| **Booking Rating**     | 9.3/10 (80 reviews)                 | "Wonderful"                     |
| **Booking Commission** | 25%                                 | High (standard = 15%)           |
| **PMS**                | None                                | Everything in Mr. Thaifa's head |
| **Channel Manager**    | HotelRunner                         | Active since 2025-12            |
| **OTAs**               | Booking ✅ / Airbnb ⏳ / Expedia ⏳ | Setup in progress               |

### Detailed Booking.com Scores

| Category            | Score | Level       |
| ------------------- | ----- | ----------- |
| **Staff**           | 9.7   | Exceptional |
| **Cleanliness**     | 9.4   | Excellent   |
| **Comfort**         | 9.4   | Excellent   |
| **Facilities**      | 9.3   | Excellent   |
| **Value for money** | 8.9   | Very good   |
| **WiFi**            | 8.8   | Very good   |
| **Location**        | 8.2   | Good        |
| **Breakfast**       | 10    | Perfect     |

> **Major Strength**: Staff rated 9.7/10 and perfect breakfast 10/10

### Current Operational State

| Metric                            | Value      |
| --------------------------------- | ---------- |
| **Confirmed reservations**        | 11         |
| **Expected revenue**              | €8,008.85  |
| **Peak occupancy (Dec 29-31)**    | 50% (6/12) |
| **HotelRunner prices configured** | 0/9 types  |
| **Active Booking promotions**     | 5 (10-15%) |

→ See `data/` for operational details

---

## 2. Contact & Communication

### 2.1 Main Contact

| Field        | Value                    |
| ------------ | ------------------------ |
| **Name**     | Said Thaifa              |
| **Age**      | 78 years                 |
| **Email**    | <said_thaifa@hotmail.fr> |
| **Email**    | <saidthaifa@gmail.com>   |
| **Phone**    | +212 661-134194          |
| **WhatsApp** | +212 661-134194          |

**Professional Background**:

- Owner and host of Villa Thaifa (with his wife Nezha)
- CEO / Real estate agent in Marrakech
- Specialties: sales, purchases, seasonal rentals
- Reputation: warm welcome, makes guests feel "at home"

### 2.2 Communication Protocol

| Rule                  | Detail                                   |
| --------------------- | ---------------------------------------- |
| **Tone**              | Mandatory vouvoiement (formal)           |
| **Register**          | Senior client — Respect without rigidity |
| **Preferred channel** | WhatsApp (confirmed)                     |

### 2.3 Communication Pattern

```text
1. SCOUT    → Explore, verify feasibility
2. RAPPORT  → Keep the client informed of findings
3. QUESTIONS → Ask for missing info (with context)
4. ACTION   → Execute when everything is clear
```

> **Golden Rule**: Never ask for info without first making a report of what was discovered.

→ See `docs/lessons-learned.md` for documented patterns

---

## 3. Property

### 3.1 General Information

| Field          | Value                                          |
| -------------- | ---------------------------------------------- |
| **Name**       | Villa Thaifa (sometimes "Villa Thaifa & SPA")  |
| **Type**       | Charming Guest House / B&B (4★)                |
| **Address**    | Route de Fès, Km 12                            |
| **Zone**       | Palmeraie / Ouled Jelal (12-14 km from center) |
| **City**       | Marrakech, Morocco                             |
| **Rooms**      | 12                                             |
| **Renovation** | Recently renovated                             |

### 3.2 Facilities & Services

| Category       | Details                                                 |
| -------------- | ------------------------------------------------------- |
| **Relaxation** | Infinity pool (open year-round), garden, solarium       |
| **Wellness**   | Spa/Hammam, massages (extra charge)                     |
| **Restaurant** | "Thaifa's restaurant" — Moroccan cuisine                |
| **Cuisine**    | Moroccan (halal, vegetarian) — "Best tagine in Morocco" |
| **Rooms**      | Air conditioning, heating, satellite TV, Wi-Fi, terrace |
| **Services**   | Free parking, airport shuttle, car rental               |
| **Security**   | 24/7, CCTV, safe, alarm                                 |
| **Languages**  | Arabic, English, French, Dutch                          |

### Breakfast (Score 10/10)

| Attribute | Value                                                            |
| --------- | ---------------------------------------------------------------- |
| **Price** | MAD 160.90/person                                                |
| **Hours** | 08:30 - 11:00                                                    |
| **Type**  | Continental, Halal                                               |
| **Menu**  | Pastries, bread, pancakes, eggs, cheese, local specialties, jams |

### 3.3 Positioning & Reputation

| Aspect             | Value                                                           |
| ------------------ | --------------------------------------------------------------- |
| **Price Range**    | 160-600 €/night (depending on type)                             |
| **Reputation**     | Very good (9.3/10 Booking)                                      |
| **Strengths**      | Quiet, gardens, infinity pool, warm welcome ("feels like home") |
| **Location Asset** | Quiet and peaceful, away from city noise (14 km from center)    |

→ See `data/rooms/rooms.md` for room details and pricing

---

## 4. Business Context

### 4.1 Confirmed Facts ✅

| Fact                | Detail                                              |
| ------------------- | --------------------------------------------------- |
| **Current PMS**     | None — Everything is done in Mr. Said Thaifa's head |
| **Channel Manager** | HotelRunner (active since Dec 2025)                 |
| **Booking.com**     | In place (25% commission)                           |
| **Airbnb**          | Pending setup                                       |
| **Expedia Partner** | Pending setup                                       |
| **Client rating**   | 9.3/10 on Booking — Excellent                       |
| **Staffing**        | Difficulty finding qualified employees (luxury)     |
| **Promotions**      | 5 active (10-15%) — Audit done Dec 20               |

### 4.2 Key Questions for Meeting ⏳ (Monday, Dec 22, 10am)

**Needs to prioritize:**

| #   | Potential Need                                      | Priority to validate |
| --- | --------------------------------------------------- | -------------------- |
| 1   | Manage booking platforms (Booking, Airbnb, Expedia) | ❓                   |
| 2   | Increase occupancy rate                             | ❓                   |
| 3   | Pricing grid to stabilize / adapt to competition    | ❓                   |
| 4   | Top SEO for "Villa Thaifa"                          | ❓                   |
| 5   | Quality website                                     | ❓                   |
| 6   | Dynamic pricing (season, occupancy, competition)    | ❓                   |
| 7   | Management software (PMS)                           | ❓                   |

**Other questions:**

| Question            | Expected Answer       |
| ------------------- | --------------------- |
| Approximate budget? | To be determined      |
| Desired timeline?   | "As soon as possible" |
| Long-term vision?   | Keep / Sell / Rent?   |

### 4.3 Main Pain Points

| Pain Point            | Impact                                              | Potential Solution                  |
| --------------------- | --------------------------------------------------- | ----------------------------------- |
| **Recruitment**       | Hard to find qualified staff for luxury positioning | Training? School partnerships?      |
| **Positioning**       | Desire to position as true luxury (proof: 9.3/10)   | Premium pricing + communication     |
| **Manual management** | Everything in Mr. Thaifa's head                     | PMS adapted to small structure      |
| **OTA dependence**    | 100% Booking.com currently                          | Diversify (Airbnb, Expedia, direct) |
| **High commission**   | 25% Booking (vs 15% standard)                       | Negotiate medium term               |

### 4.4 Identified Opportunities

**Short term (Q1 2026):**

| Opportunity                      | Impact            | Effort | Priority |
| -------------------------------- | ----------------- | ------ | -------- |
| Configure HotelRunner pricing    | Immediate revenue | Low    | 🔴 P0    |
| Setup Airbnb/Expedia             | Diversification   | Medium | 🟠 P1    |
| Adapted PMS (Hotelogix or other) | Efficiency        | Medium | 🟠 P1    |
| Automate reporting               | Visibility        | Low    | 🟢 P2    |

**Long term (2026+):**

| Opportunity                        | Note                                 |
| ---------------------------------- | ------------------------------------ |
| Website + Direct booking engine    | Via HotelRunner? Source code access? |
| Jisr l'Mokawala (GO Siyaha portal) | Brief prepared — P3 investigation    |
| Direct sales without intermediary  | Mr. Thaifa is "tired of managing"    |
| Rent to a competent company        | Alternative to selling               |

---

## 5. Competitive Analysis

### 5.1 Palmeraie Market

| Segment          | Price/night | Typical Rating | Characteristics                 |
| ---------------- | ----------- | -------------- | ------------------------------- |
| **Standard**     | 80-150€     | 8.0-8.5        | Basic B&B, few services         |
| **Premium**      | 150-280€    | 8.5-9.0        | Pool, spa, restaurant           |
| **Luxury**       | 280-500€    | 9.0+           | Suites, exclusive experience    |
| **Ultra-luxury** | 500€+       | 9.5+           | Private villas, dedicated staff |

### 5.2 Villa Thaifa Positioning

| Criterion    | Villa Thaifa          | Position          |
| ------------ | --------------------- | ----------------- |
| **Price**    | 160-600€              | Premium → Luxury  |
| **Rating**   | 9.3/10                | Top 10% Palmeraie |
| **Rooms**    | 12                    | Medium size       |
| **Services** | Pool, spa, restaurant | Full Premium      |

**Competitive advantage:** Exceptional rating (9.3) + quiet Palmeraie positioning

→ Detailed benchmark: research in progress

---

## 6. Financial Baseline

### 6.1 Revenue Models

| Occupancy Rate | Nights/year | Gross Revenue | After commission (25%) |
| -------------- | ----------- | ------------- | ---------------------- |
| **50%**        | 2,190       | ~€438,000     | ~€328,500              |
| **70%**        | 3,066       | ~€613,200     | ~€459,900              |
| **90%**        | 3,942       | ~€788,400     | ~€591,300              |

_Basis: 12 rooms × 365 days × average price ~200€_

### 6.2 Commission Impact

| OTA                      | Commission | Out of €100 gross | Net  |
| ------------------------ | ---------- | ----------------- | ---- |
| **Booking.com current**  | 25%        | -€25              | €75  |
| **Booking.com standard** | 15%        | -€15              | €85  |
| **Airbnb**               | ~15%       | -€15              | €85  |
| **Direct**               | 0%         | €0                | €100 |

**Opportunity:** Reduce Booking dependence + negotiate commission

### 6.3 RevPAR Objectives

| KPI           | Current     | Target Q1 2026 | Target 2026 |
| ------------- | ----------- | -------------- | ----------- |
| **Occupancy** | ~50% (peak) | 60%            | 70%         |
| **ADR**       | ~€200       | €220           | €250        |
| **RevPAR**    | ~€100       | €132           | €175        |

---

## 7. Technical Stack

### 7.1 Current State

| Component           | Solution             | Status                     |
| ------------------- | -------------------- | -------------------------- |
| **PMS**             | None (manual)        | ❌ Critical                |
| **Channel Manager** | HotelRunner          | ✅ Active                  |
| **Main OTA**        | Booking.com          | ✅ Active (25% commission) |
| **Secondary OTAs**  | Airbnb, Expedia      | ⏳ Pending                 |
| **Website**         | Nonexistent or basic | ❓ To verify               |
| **Booking engine**  | None                 | ⏳ HotelRunner?            |

### 7.2 Constraints & Challenges

- No tech training for Mr. Thaifa (78 years old)
- Need for a simple, intuitive solution
- No dedicated IT staff
- Budget to be defined

### 7.3 Proposed Integrations

| Solution                      | Function                           | Priority           |
| ----------------------------- | ---------------------------------- | ------------------ |
| **Hotelogix** (or equivalent) | PMS suited for small structure     | P1                 |
| **HotelRunner**               | Channel Manager + Booking engine   | P0 (in progress)   |
| **Jisr l'Mokawala**           | Direct bookings (GO Siyaha portal) | P3 (investigation) |

---

## 8. Risks & Mitigation

| Risk                       | Probability | Impact | Mitigation                 |
| -------------------------- | ----------- | ------ | -------------------------- |
| **Booking.com dependence** | High        | High   | Diversify OTAs + direct    |
| **Qualified staffing**     | High        | Medium | Training partnerships      |
| **Tech adoption**          | Medium      | Medium | Simple solutions, training |
| **Seasonality**            | High        | Medium | Dynamic pricing, events    |
| **Owner fatigue**          | Medium      | High   | Progressive delegation     |

---

## 9. Success Metrics

### 9.1 KPIs to Establish at Meeting

| KPI                   | Baseline | 6-month Target | How to measure                |
| --------------------- | -------- | -------------- | ----------------------------- |
| Average commission    | 25%      | 20%            | Negotiation + diversification |
| % direct bookings     | 0%       | 10%            | Booking engine + SEO          |
| Annual occupancy rate | ~50%     | 60%            | HotelRunner reports           |
| Booking rating        | 9.3/10   | Maintain >9.0  | Booking dashboard             |
| Staff turnover        | ❓       | Reduce         | To define with Mr. Thaifa     |

### 9.2 Mission Success Criteria

| Criterion       | Definition                                    |
| --------------- | --------------------------------------------- |
| **Operational** | All reservations assigned, pricing configured |
| **Technical**   | HotelRunner functional, OTAs synchronized     |
| **Strategic**   | 2026 plan validated, budget approved          |
| **Relational**  | Mr. Thaifa's trust established                |

---

## 10. Engagement & Timeline

### 10.1 History

| Date       | Event                               | Status         |
| ---------- | ----------------------------------- | -------------- |
| 2025-12-19 | First contact                       | ✅ Done        |
| 2025-12-20 | Audit promotions + pricing strategy | ✅ Done        |
| 2025-12-20 | Setup HotelRunner (partial)         | ⏳ In progress |

### 10.2 Next Steps

| Date                | Event                         | Objective                        |
| ------------------- | ----------------------------- | -------------------------------- |
| **2025-12-22 10am** | Discovery meeting Mr. Thaifa  | Validate needs, budget, timeline |
| 2025-12-22 PM       | Document decisions            | Update PROFILE.md                |
| 2025-12-23-24       | Commercial proposal           | Create quote                     |
| 2025-12-25-28       | Assign reservations           | 10 rooms to assign               |
| 2026-01             | Investigation Jisr l'Mokawala | Feasibility                      |

### 10.3 Proposed Milestones

| Milestone               | Target Date | Deliverables                          |
| ----------------------- | ----------- | ------------------------------------- |
| **M1: Full setup**      | Dec 31 2025 | HotelRunner configured, active prices |
| **M2: Diversification** | Jan 31 2026 | Airbnb + Expedia active               |
| **M3: PMS**             | Feb 28 2026 | PMS solution chosen + deployed        |
| **M4: Direct booking**  | Mar 31 2026 | Booking engine + basic SEO            |

---

## 11. Strategic Opportunities (Long Term)

### Vision 2026+

| Scenario         | Description                   | Probability |
| ---------------- | ----------------------------- | ----------- |
| **Optimization** | Mr. Thaifa keeps, we optimize | High        |
| **Delegation**   | Rent to competent company     | Medium      |
| **Exit**         | Direct sale (without samsar)  | Low         |

### Growth Levers

1. **Direct bookings** — Reduce OTAs commission
2. **Upselling** — Spa, transport, excursions
3. **Events** — Weddings, corporate retreats
4. **Loyalty** — Returning guests program

---

## 12. References

### 12.1 Related Documents

| Folder                         | Content                |
| ------------------------------ | ---------------------- |
| `data/communication/whatsapp/` | Ready-to-send messages |
| `archive/2025/Q4/`             | Archives and histories |

### 12.2 Operational State (SSOT)

| File                               | Content                             |
| ---------------------------------- | ----------------------------------- |
| `data/rooms/rooms.md`        | Rooms, pricing, HotelRunner mapping |
| `data/bookings/reservations/reservations.md` | Confirmed reservations              |
| `data/finance/rates.json` | Active promotions                   |

### 12.3 Documentation

| File                      | Content                             |
| ------------------------- | ----------------------------------- |
| `docs/lessons-learned.md` | 3 documented communication patterns |
| `CLAUDE.md`               | AI agents instructions              |

### 12.4 Industry Resources

- [Hotelogix - 8 Must-Have PMS Reports](https://blog.hotelogix.com/hotel-reservation-report/)
- [Villa Palmeraie Marrakech - Booking.com](https://www.booking.com/hotel/ma/villa-palmeraie-marrakech-marrakech1.html)
- [Villa Al Assala Palmeraie - Booking.com](https://www.booking.com/hotel/ma/villa-al-assala-palmeraie.html)

---

## Industry Glossary

| Term                | Definition                                                     |
| ------------------- | -------------------------------------------------------------- |
| **PMS**             | Property Management System — Hotel management software         |
| **OTA**             | Online Travel Agency — Platforms like Booking, Airbnb, Expedia |
| **Channel Manager** | Tool syncing availabilities across all OTAs                    |
| **ADR**             | Average Daily Rate — Average revenue per sold room             |
| **RevPAR**          | Revenue Per Available Room — Revenue per room available        |
| **SSOT**            | Single Source of Truth                                         |

---

## Internal Notes

```text
[2025-12-19] Client folder created. Meeting Monday TBC.
[2025-12-20] V1 profile optimization via /elevate.
[2025-12-20] V2 profile reorganization — 12-section structure.
             Backup: .backup/PROFILE-2025-12-20-v2-before-reorg.md
```

---

_Reorganized profile — 12-section structure — 2025-12-20_
_Pipeline: `archive/2025/Q4/reports/profile-reorganization/`_

## Overview

| Field        | Value                                               |
| ------------ | --------------------------------------------------- |
| **Client**   | Said Thaifa                                         |
| **Age**      | 78                                                  |
| **Email**    | <said_thaifa@hotmail.fr>                            |
| **Phone**    | +212 661-134194                                     |
| **Language** | Dutch (preferred), French, Arabic (Morrocan Darija) |
| **Location** | Marrakech, Morocco                                  |
| **Business** | Boutique hotel (maison d'hôtes 4★)                  |
| **Property** | 12 rooms                                            |

## Relationship

- **Start Date**: December 2025
- **Last Activity**: January 24, 2026
- **Status**: 🟢 Active

## Projects

| Project             | Directory              | Description                                |
| ------------------- | ---------------------- | ------------------------------------------ |
| property-management | `property-management/` | Hotel management platform (Next.js + APIs) |

## Communication Notes

- Said is 78 years old — patience and clarity are paramount
- Prefers Dutch, comfortable with French
- Primary contact via WhatsApp (+212 661-134194)
- Decisions require time — never rush
- Technical explanations should be visual and simple

## Technical Stack (property-management)

- **Framework**: Next.js
- **APIs**: HotelRunner (HR-v1), Booking.com
- **Automation**: agent-browser (headless browser)
- **Credentials**: `.env.local` (HotelRunner, Booking.com)

## Key Contacts

| Role  | Name | Contact                  |
| ----- | ---- | ------------------------ |
| Owner | Said | <said_thaifa@hotmail.fr> |
| Admin | Omar | (El Mountassir)          |

### Omar — Quick Reference

> **Source of Truth**: `~/omar/identity/profile.md` & `~/omar/identity/preferences.md`
> **Role in This Project**: Founder & Agentic Engineer
> **Last Synced**: 2026-02-09

## Identity

| Field               | Value                                                   |
| ------------------- | ------------------------------------------------------- |
| **Full Name**       | Omar El Mountassir                                      |
| **Company**         | El Mountassir Inc. (Hybrid Carbon-Silicon Organization) |
| **Role**            | Founder, Agentic Engineer                               |
| **Location**        | Marrakech, Morocco                                      |
| **Languages**       | French (primary), English (work), Darija (native)       |
| **Tech Experience** | 29 years                                                |
| **Email**           | <omar@el-mountassir.com>                                |

## Professional Identity

- **Agentic Engineer**: Orchestrates intelligences rather than writing code ("I do not code anymore, I orchestrate intelligences").
- **Expert Curator**: (2026-02-07) "My job isn't to be the 'factory worker' any more... my job is to be the expert curator who can spot the genius in all that noise."
- **Thinker & Product Designer**: Strategic, creative, and logical thinking. Designs end-to-end product journeys.

## Critical Preferences for Agents

### Priority Order

1. **Time** — Most precious resource
2. **Health** — Energy to preserve
3. **Money** — Necessary for survival

### Decision Making

- Minimize asks for trivial decisions (drains energy)
- Propose intelligent defaults; act automatically for low-risk choices
- Ask only for important/irreversible decisions

### Communication Style

- **Written**: English in files, French in chat
- **Wants**: Partner, not rubber-stamp; brutal honesty
- **Dislikes**: Verbosity, generic AI tone, passivity
- **Prefers**: Tables, visual hierarchy, direct opinions

### Working With Omar

- **Bad memory**: Needs proactive reminders
- **Divergence pattern**: Tends to jump topics; agents should gently redirect
- **Process before execution**: Standardize approach BEFORE applying to cases
- **CURATOR MODE**: Present OPTIONS (2-4), not single solutions; Omar curates

## Self-Identified Weaknesses (For Agent Compensation)

| Weakness                 | Agent Compensation                                         |
| ------------------------ | ---------------------------------------------------------- |
| Bad memory               | Proactive reminders, explicit references to past decisions |
| Lack of focus discipline | Redirect divergences: "We were on X. Continue or pivot?"   |
| Overwhelm from rush      | When tired, capture everything, execute nothing            |

## Reference

- **Full Profile**: `~/omar/identity/profile.md`
- **Preferences Detail**: `~/omar/identity/preferences.md`
- **Operational Protocol**: `~/omar/operations/protocols/operating-protocol.md`

---

## Strategic Context

### Vision

> **CEO & Leader - Villa Thaifa Project**
> **Date**: 2026-01-15

---

## 🎯 My Vision

> "Agentic transformation is not an option, it's a necessity."

**Context**: The Agentic AI Revolution (2026 - 3rd era of AI)

**Principle**: AI agents are **autonomous co-workers**, not tools.

---

## 🚀 Long-Term Objectives

### For Villa Thaifa

1. **Operational Excellence**
   - Automate 80% of repetitive tasks
   - Maintain a satisfaction rate > 9.5/10
   - Optimize revenue through dynamic pricing

2. **Digital Transformation**
   - Complete integration of all systems
   - Real-time synchronized data
   - Total visibility on activity

3. **Agentic Transformation**
   - 17+ autonomous AI agents
   - Fluid agent-human collaboration
   - Continuous system improvement

### For Me (Omar)

1. **Leadership**
   - Vision & strategy
   - Decision making
   - Supervision (not execution)

2. **Architecture**
   - Delegated to Claude (CTO/Architect)
   - Technical decisions validated by me

3. **Liberation**
   - Less time on operations
   - More time on strategy
   - Scalability to other projects

---

## 🏆 Success

Success will be achieved when:

- ✅ Villa Thaifa is a model of operational excellence
- ✅ AI agents work autonomously at 80%
- ✅ I can focus on strategy
- ✅ The system is ready to scale

---

## 📊 Metrics

| Metric                  | Current | Target | Date    |
| ----------------------- | ------- | ------ | ------- |
| Automation rate         | TODO%   | 80%    | 2026-06 |
| Client satisfaction     | 9.3     | 9.5    | 2026-03 |
| Omar time (operational) | TODO    | < 20%  | 2026-06 |
| Autonomous agents       | 0%      | 80%    | 2026-06 |

---

**Tags**: `vision` `leadership` `omar` `strategy`

### Priorities

> **Omar El Mountassir - CEO & Leader**
> **Last updated**: 2026-01-15

---

## 🎯 P0 (CRITICAL - This week)

### 1. Finalize the agentic prompt system

- **Status**: In progress
- **Deadline**: 2026-01-15
- **Owner**: Claude (CTO)
- **Deliverables**:
  - [x] Project backup
  - [x] `docs/agents/` structure
  - [x] `CLAUDE.md` (entry point)
  - [ ] Standardized frontmatter (17 agents)
  - [ ] Validation and testing

### 2. [Add P0 priority if necessary]

---

## 🔥 P1 (HIGH - This month)

### 1. Dynamic pricing system

- **Status**: To start
- **Deadline**: 2026-01-31
- **Agent lead**: `pricing-analyst`
- **Objective**: Implement dynamic pricing

### 2. Complete Booking.com ↔ HotelRunner synchronization

- **Status**: To start
- **Deadline**: 2026-01-31
- **Involved agents**: `browser-agent`, `platform-validator`, `data-sync-checker`
- **Objective**: Zero discrepancies between platforms

### 3. [Add P1 priority if necessary]

---

## 📋 P2 (MEDIUM - This quarter)

### 1. Automate guest communications

- **Status**: Backlog
- **Deadline**: 2026-03-31
- **Agent lead**: `guest-communicator`
- **Objective**: Templates + automation for 80% of communications

### 2. Setup reporting system

- **Status**: Backlog
- **Deadline**: 2026-03-31
- **Agent lead**: `html-report-generator`
- **Objective**: Weekly automated reports for Omar

### 3. [Add P2 priority if necessary]

---

## 💡 P3 (LOW - Ideas for the future)

- [ ] Knowledge graph for visual navigation
- [ ] Google Analytics integration
- [ ] Automatic recommendation system
- [ ] Chatbot for frequently asked questions

---

**Tags**: `priorities` `leadership` `planning`

### Preferences

> **PLACEHOLDER FILE**
> **Status**: To complete
> **Priority**: P1 (critical for the project)

---

## 📋 Communication

- **Preferred channel**: TODO (WhatsApp? Email? Phone?)
- **Language**: French
- **Reporting frequency**: TODO
- **Desired level of detail**: TODO

---

## 🎯 Priorities

- **Priority 1**: TODO
- **Priority 2**: TODO
- **Priority 3**: TODO

---

## 💼 Work style

- **Decision making**: TODO (autonomous? consultative?)
- **Involvement**: TODO (very involved? delegative?)
- **Responsiveness**: TODO

---

## 🚫 To avoid

- TODO

---

## ✅ What works well

- TODO

---

**Tags**: `placeholder` `to_complete` `client` `preferences`

### Key Decisions

> **History of decisions made for Villa Thaifa**
> **Managed by**: Omar El Mountassir (CEO & Leader)

---

## 📅 2026-01-15

### Decision: Create the agentic prompt system

**Context**: Current prompts are messy, no single entry point, scattered context.

**Decision**: Create a modular, agent-first architecture with:

- `CLAUDE.md` as single entry point
- `docs/agents/` with structured context (mandatory/domain/mission)
- Standardized frontmatter for all agents
- Agent registry in JSON

**Rationale**:

- Agents need a clear and coherent system
- Hyperconnected navigation
- Scalable for the future

**Owner**: Claude (CTO/Architect)
**Status**: Implementation in progress

---

## 📅 Format for future decisions

```markdown
### Decision: [Title]

**Context**: [Why this decision?]

**Decision**: [What was decided?]

**Rationale**: [Why this decision?]

**Alternatives considered**:

- [Option 1]
- [Option 2]

**Owner**: [Who implements?]
**Status**: [In progress/Completed]
**Review date**: [If planned review]
```

---

**Tags**: `decisions` `leadership` `history`

### Engagement History

> **PLACEHOLDER FILE**
> **Status**: To complete
> **Priority**: P2

---

## 📅 Timeline

### 2026

- **2026-01-15**: Start of Villa Thaifa project (digital & agentic transformation)

---

## 🎯 Projects

### Villa Thaifa Digitization

- **Objective**: Complete digital transformation of the guest house
- **Scope**: Booking.com, HotelRunner, pricing automation, AI agents
- **Status**: In progress
- **Team**: Omar (CEO/Leader), Claude (CTO/Architect), 17+ AI Agents

---

## 📊 Key points

- **How the relationship started**: TODO
- **Notable successes**: TODO
- **Challenges overcome**: TODO
- **Lessons learned**: TODO

---

**Tags**: `placeholder` `to_complete` `client` `history`

---

## Team Structure

> **Workforce Agentic 2026**
> **Leader**: Omar El Mountassir (CEO)
> **CTO/Architecte**: Claude (instances successives)

---

## 👥 Philosophy: Digital Stewardship

**AI agents are "Digital Stewards", not simple tools.**

1. **Vision**: We act as the guardians of Villa Thaifa's digital heritage.
2. **Symbiosis**: We work **autonomously** under the strategic direction of Omar El Mountassir.
3. **Goal**: Absorb all technological complexity to give Said Thaifa back his peace of mind (Host of excellence).

---

## 🏢 Team Structure

### Leadership

| Role              | Who                | Responsibilities                                                      |
| ----------------- | ------------------ | --------------------------------------------------------------------- |
| **CEO & Leader**  | Omar El Mountassir | Vision, strategy, final decisions, Guarantor of the Said relationship |
| **CTO/Architect** | Antigravity (AI)   | Technical stewardship, agent systems, architecture decisions          |

### AI Agents (17 co-workers)

#### Operations (4 agents)

| Agent                   | Model  | Specialty                 |
| ----------------------- | ------ | ------------------------- |
| **pricing-analyst**     | Opus   | Pricing strategy, revenue |
| **reservation-manager** | Sonnet | Reservation management    |
| **calendar-agent**      | Sonnet | Availability, occupancy   |
| **data-sync-checker**   | Sonnet | Platform sync validation  |

#### Technical (4 agents)

| Agent                      | Model  | Specialty                          |
| -------------------------- | ------ | ---------------------------------- |
| **platform-validator**     | Sonnet | Pre-platform operations validation |
| **browser-agent**          | Sonnet | Chrome automation, scraping        |
| **security-auditor**       | Opus   | Security, OWASP                    |
| **smart-contract-auditor** | Opus   | Smart contracts audit (if needed)  |

#### Meta (7 agents)

| Agent                     | Model  | Specialty                      |
| ------------------------- | ------ | ------------------------------ |
| **meta-agent**            | Opus   | Creation of new agents         |
| **research-agent**        | Haiku  | Web research (low criticality) |
| **auditor**               | Sonnet | Brutal excellence audit        |
| **incident-reporter**     | Haiku  | Incident documentation         |
| **html-report-generator** | Opus   | HTML reports                   |
| **claude-md-agent**       | Opus   | CLAUDE.md maintenance          |
| **decision-evaluator**    | Opus   | Multi-criteria analysis        |

#### Hospitality (2 agents)

| Agent                  | Model  | Specialty            |
| ---------------------- | ------ | -------------------- |
| **guest-communicator** | Sonnet | Guest communications |
| **translation-agent**  | Haiku  | FR/EN/AR translation |

---

## 🔄 Collaboration

### Handovers

**Rule**: ALWAYS create a handover at the end of a session.

**Template**: `docs/agents/handovers/template.md`

**YAML Format**:

- Completed tasks
- Tasks in progress
- Blockers
- Next actions
- Context for next agent
- Findings for CTO

### Dependencies

Examples:

- `reservation-manager` depends on `platform-validator`
- `pricing-analyst` depends on `calendar-agent`

---

## 📈 Performance

### AI Agents KPIs

| Metric               | Target | Current |
| -------------------- | ------ | ------- |
| Autonomy             | 80%    | TODO%   |
| Success rate         | 90%    | TODO%   |
| Completed handovers  | 100%   | TODO%   |
| Documented incidents | 100%   | TODO%   |

---

## 🎯 Next steps

1. **Phase 1** (Week 1): Foundations
   - Standardize frontmatter
   - Create capabilities JSON for each agent

2. **Phase 2** (Month 2-3): Activation
   - Test core agents on real tasks
   - Refine based on usage

3. **Phase 3** (Month 4-6): Expansion
   - Activate secondary agents
   - Create feedback system

---

**Tags**: `team` `agents` `organization`

---

## Email Intelligence (2026-02-09)

> **Source**: Gemini Gmail Analysis
> **Date Captured**: 2026-02-09
> **Period Covered**: December 2025 - January 2026

## Executive Summary

Three active workstreams identified from email correspondence:

1. **Trip.com GDA** — Contract finalized, 18% commission, HotelRunner compatible ✅
2. **Website Creation** — BLOCKED on elements from Said
3. **MarocPME Action** — BLOCKED on legal form information

---

## 1. Trip.com GDA Contract (OTA Integration) ✅

**Status**: Ready to Sign
**Commission**: 18% (North Africa rate)
**Payment**: Monthly bank transfer

### Key Terms Confirmed

| Topic          | Resolution                                            |
| -------------- | ----------------------------------------------------- |
| Payment Method | Bank transfer (needs bank notification letter)        |
| Parity         | Narrow parity expected (no disparity with other OTAs) |
| Taxes          | VAT prepaid online, tourist tax at check-in           |
| Inventory Sync | **HotelRunner compatible** ✅                         |
| Flat Rates     | Blackout dates allowed for high season                |
| Payment Cycle  | Monthly                                               |

### Timeline

- 23-26 Jan: Contract initiated via Hospitality Web Services
- 26 Jan: Omar requested clarifications (parity, taxes, HotelRunner, seasonality)
- 27 Jan: Lucas Teng (Trip.com) provided all answers + corrected commission to 18%

**Action Required**: Said needs to sign and return GDA with bank notification letter.

---

## 2. Website Creation ⏳

**Status**: BLOCKED — Waiting on Said
**Vendor**: Hospitality Web Services
**Request Date**: 2026-01-09

### Elements Needed from Said

- [ ] Template or examples of liked websites
- [ ] Specific preferences/descriptions to include
- [ ] Color codes (or use logo colors)
- [ ] Logo file
- [ ] Point-of-sale descriptions
- [ ] Social media links

**Action Required**: Omar to follow up with Said for these elements.

---

## 3. MarocPME Action MOUS-17509 ⏳

**Status**: BLOCKED — Missing legal form info
**Vendor**: JISR L'MOKAWALA MarocPME
**Request Date**: 2026-01-12

**Issue**: New CLM template requires beneficiary information (legal form).

**Action Required**: Said to provide legal entity information for Villa Thaifa.

---

## Other Notes

- **Personal Booking (Dec 24-25)**: Said booked Suite Executive + Family Suite + Deluxe Triple Room for Dec 31 - Jan 2
- **Booking.com (Jan 30)**: Notification about optimizing Contact page in extranet

---

## Recommended Next Actions

| Priority  | Action                            | Owner      | Status  |
| --------- | --------------------------------- | ---------- | ------- |
| 🔴 High   | Sign Trip.com GDA + bank letter   | Said       | Pending |
| 🔴 High   | Provide website elements          | Said       | Pending |
| 🟡 Medium | Submit legal form for MarocPME    | Said       | Pending |
| 🟢 Low    | Optimize Booking.com Contact page | Omar/Agent | Backlog |

---

## Decision Log

> **Purpose**: Register identifying BLOCKING issues where the Agent needs a User Decision to proceed.
> **Status**: 🟢 Open
> **Instructions**:
>
> 1. Agent: Add a new section with a clear title and context.
> 2. Agent: Provide options (A, B, C) if possible.
> 3. User: Mark resolution with [x] and add comments.

## 001. [Example] Database Choice

- [ ] **Context**: We need a DB.
- [ ] **Options**:
  - A) PostgreSQL (Recommended)
  - B) SQLite (Simpler)
- [ ] **Resolution**: ...

## General Inquiries

> **Purpose**: Non-blocking questions to deepen Agent understanding of the business/legacy context.
> **Status**: 🟢 Open

## 001. [Example] History of Room 12

- **Question**: Was Room 12 renovated in 2024?
- **Why**: Content description mentions "New carpet", photos show tiles.
- **Answer**: ...

---

## Profile Data (JSON)

```json
{
  "_comment": "PLACEHOLDER FILE - To complete with real client data",
  "version": "1.0.0",
  "last_updated": "2026-01-15T12:00:00Z",
  "status": "placeholder",
  "client": {
    "id": "said-thaifa",
    "name": "Said Thaifa",
    "role": "Owner",
    "property": "Villa Thaifa",
    "location": "Marrakech, Morocco",
    "contact": {
      "email": "TODO",
      "phone": "TODO",
      "whatsapp": "TODO",
      "preferred_channel": "TODO"
    },
    "profile": {
      "language": "French",
      "languages_spoken": ["French", "Dutch", "Arabic", "English"],
      "timezone": "Africa/Casablanca",
      "communication_style": "TODO",
      "availability": "TODO"
    },
    "preferences": {
      "response_time_expectation": "TODO",
      "reporting_frequency": "TODO",
      "decision_making_style": "TODO",
      "technical_level": "TODO"
    },
    "history": {
      "client_since": "TODO",
      "projects_completed": [],
      "ongoing_projects": ["villa-thaifa-digitization"]
    }
  },
  "tags": ["placeholder", "to_complete", "client"],
  "todo": [
    "Complete contact coordinates",
    "Define preferred communication style",
    "Document relationship history",
    "Add reporting preferences"
  ]
}
```

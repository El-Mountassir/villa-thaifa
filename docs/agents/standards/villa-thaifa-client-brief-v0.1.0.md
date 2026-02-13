# Villa Thaifa — Client Brief

**Version:** 0.1.0-alpha.0  
**Date:** 2026-01-09  
**Status:** Active, No Contract Signed  
**Priority:** HIGH (1 week revenue loss)

---

## 1. CLIENT PROFILE

| Field             | Value                                     |
| ----------------- | ----------------------------------------- |
| **Business Name** | Villa Thaifa                              |
| **Type**          | Maison d'hôte (Guest House)               |
| **Location**      | Marrakech, Morocco                        |
| **Owner**         | Said Thaifa                               |
| **Contact**       | [À compléter]                             |
| **Status**        | Contracting (already in action)           |
| **Urgency**       | HIGH — Omar is bottleneck, client waiting |

---

## 1.1 OMAR'S LEGAL CONTEXT

| Field                   | Value                                            |
| ----------------------- | ------------------------------------------------ |
| **Legal Status**        | Auto-Entrepreneur (Morocco)                      |
| **Activity**            | Prestations de Services (Tech/Consulting)        |
| **Tax Regime**          | Libératoire (IR) - 1% on cash basis revenue      |
| **Annual Cap**          | 200,000 MAD                                      |
| **Alert Threshold**     | 180,000 MAD (trigger: evaluate structure change) |
| **VAT**                 | Not applicable                                   |
| **Deductible Expenses** | None                                             |
| **Last Verified**       | 2026-01-02                                       |

**Implication for Villa Thaifa:**

- All invoicing must comply with Auto-Entrepreneur limits
- Simple structure = fast invoicing, but revenue cap exists
- If Villa Thaifa + future clients approach 180K MAD, need to evaluate SARL/offshore structure

---

## 2. CURRENT SETUP

### 2.1 Repository

- **URL:** https://github.com/omar-elmountassir/villa-thaifa
- **Current State:** "Bordel total" — raw/brouillon
- **Format:** Documents (not code) — "comme si on était en 1995"
- **Need:** Transform to Everything-as-Code (EaC)
- **Files Count:** 329 fichiers clonés
- **Brief Created:** BRIEF-2026-01-08.md

### 2.2 Channel Manager

**Platform:** HotelRunner

- Website: https://www.hotelrunner.com/
- Support: https://support.hotelrunner.com/
- Developer Docs: https://developers.hotelrunner.com/
- **APIs Available:** REST API + XML API

### 2.3 Connected Booking Platforms

| Platform    | Status         | Priority | Notes                     |
| ----------- | -------------- | -------- | ------------------------- |
| Booking.com | ✅ Connected   | P0       | **Needs reconfiguration** |
| Expedia     | 🔄 In progress | P0       | Via HotelRunner           |

---

## 3. TARGET PLATFORMS (À connecter via HotelRunner)

**Liste proposée à confirmer avec Said:**

| Platform      | Priority | Status           | Notes       |
| ------------- | -------- | ---------------- | ----------- |
| Airbnb        | P1       | ❌ Not connected |             |
| VRBO          | P1       | ❌ Not connected |             |
| TripAdvisor   | P1       | ❌ Not connected |             |
| Google Hotels | P1       | ❌ Not connected |             |
| Trivago       | P2       | ❌ Not connected |             |
| Agoda         | P2       | ❌ Not connected |             |
| Hotels.com    | P2       | ❌ Not connected | Via Expedia |
| Trip.com      | P2       | ❌ Not connected |             |

**Question ouverte:** Said confirme-t-il cette liste? D'autres à ajouter?

---

## 4. KEY PROBLEMS TO SOLVE

### 4.1 Room Configuration Mismatch ⚠️

**Current Problem:**

- **Booking.com:** Configured by **Room Type** (grouped)
- **HotelRunner:** Configured by **Room Number** (individual)
- **Said's Preference:** By Room Number ✅

**Impact:**

- Inconsistent inventory management
- Manual reconciliation required
- Risk of overbooking/errors

**Required Action:**

- Reconfigure Booking.com to match HotelRunner
- Requires: App + Database to manage facilities properly

---

### 4.2 Pricing Strategy Review 💰

**Request from Said:**
Complete review and optimization of pricing strategy.

**Seasonal Structure Needed:**

- **Très haute saison** (Peak)
- **Haute saison** (High)
- **Moyenne saison** (Medium)
- **Basse saison** (Low)

**Required Work:**

1. **Competitor Analysis**
   - Identify comparable properties in Marrakech
   - Benchmark pricing across seasons
2. **Market Research**
   - Marrakech hospitality market trends
   - Occupancy rate analysis
   - Event calendar impact
3. **Pricing Recommendations**
   - Data-driven seasonal pricing
   - Dynamic pricing strategy
   - Implementation in HotelRunner

---

### 4.3 Internal Management Platform 🖥️

**Need:**

- Internal dashboard for Said
- Centralized access hub (client portal)
- **Scalable:** More clients coming soon

**Capabilities Required:**

- Real-time inventory visibility
- Multi-platform sync status
- Booking management
- Revenue analytics
- Agent-assisted operations

---

## 5. STRATEGIC CONTEXT

### 5.1 Financing Opportunity

**Go Siyaha:** 90% financing possible (mentioned in prior brief)

- **Action Required:** Research and validate this opportunity

### 5.2 Long-Term Vision

- Villa Thaifa = **First Client**
- Architecture must be **multi-tenant ready**
- Agent automation for routine operations

### 5.3 Transformation Goal

Transform from document-based to **Everything-as-Code (EaC)**:

- Infrastructure as Code
- Configuration as Code
- Documentation as Code
- Agent-executable workflows

---

## 6. CRITICAL QUESTIONS FOR SAID

### 6.1 CRITICAL BLOCKERS (Must resolve before starting)

| #         | Question                               | Why Critical                                                                                                                                                                 | Status          |
| --------- | -------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------- |
| **B-001** | **What does "transform to app" mean?** | 3 possible interpretations:<br>• Web app (user-facing)<br>• Automation system (backend only)<br>• Hybrid (portal + automation)<br>Without clarity, we build the wrong thing. | 🔴 **BLOCKING** |
| **F-001** | **Contract & Budget**                  | No signed contract yet = no scope protection, no payment terms                                                                                                               | 🔴 **BLOCKING** |
| 1         | Confirm platform priority list         | Determines integration sequence                                                                                                                                              | ⏳ Pending      |
| 2         | Additional platforms to add?           | Affects architecture scope                                                                                                                                                   | ⏳ Pending      |
| 3         | Room numbering scheme details          | HIGH                                                                                                                                                                         | ⏳ Pending      |
| 4         | Current pricing structure (baseline)   | MEDIUM                                                                                                                                                                       | ⏳ Pending      |
| 5         | Competitor list for analysis           | MEDIUM                                                                                                                                                                       | ⏳ Pending      |
| 6         | Timeline expectations                  | HIGH                                                                                                                                                                         | ⏳ Pending      |
| 7         | Budget allocation                      | HIGH                                                                                                                                                                         | ⏳ Pending      |

---

## 7. DELIVERABLES ROADMAP (Draft)

### Phase 0: Project Inception

- [ ] Clean up villa-thaifa repo
- [ ] Apply EaC methodology
- [ ] Document all requirements
- [ ] Prepare for agent execution

### Phase 1: Foundation

- [ ] HotelRunner API integration
- [ ] Room configuration alignment
- [ ] Basic internal dashboard

### Phase 2: Platform Connections

- [ ] Connect remaining OTAs via HotelRunner
- [ ] Verify sync across all platforms
- [ ] Monitoring setup

### Phase 3: Pricing Strategy

- [ ] Competitor analysis
- [ ] Seasonal pricing model
- [ ] Implementation

### Phase 4: Client Hub

- [ ] Internal platform for Said
- [ ] Scalable multi-tenant architecture
- [ ] Agent-assisted operations

---

## 8. RISKS & MITIGATION

| Risk                         | Impact             | Mitigation                  |
| ---------------------------- | ------------------ | --------------------------- |
| Repo is "bordel"             | Delay              | Systematic cleanup with EaC |
| Document-based (not code)    | Inefficiency       | Transform to code-first     |
| Multiple platform complexity | Integration burden | HotelRunner as single hub   |
| Omar's bandwidth             | Bottleneck         | Agent automation            |
| No signed contract           | Scope creep        | Clear SOW before work       |
| 1 week revenue loss          | Client pressure    | Prioritize quick wins       |

---

## 9. SUCCESS CRITERIA

**Phase 1 Success:**

- [ ] Room configuration aligned across all platforms
- [ ] No manual reconciliation needed
- [ ] Said can manage operations independently

**Long-term Success:**

- [ ] Scalable to multiple clients
- [ ] 80%+ operations automated via agents
- [ ] Revenue increase through optimized pricing

---

**Next Actions:** See `villa-thaifa-quick-start.md` for migration instructions.

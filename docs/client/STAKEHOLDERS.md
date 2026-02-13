# Stakeholders - Villa Thaifa Project

> **Quick Reference** pour les parties prenantes du projet
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

**⚠️ Critical Rule for Agents**: Scout → Rapport → Questions → Action
(Never ask for info without first reporting what you've discovered)

**📄 Detailed Profile**: [`profiles/SAID-THAIFA.md`](./profiles/SAID-THAIFA.md)

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

- ✅ **USE**: Omar's admin accounts (<omar@el-mountassir.com)>
- ❌ **NEVER USE**: Said's owner accounts (unless explicit Omar approval)

### Platform Credentials

**Location**: `.env.local` (project root)
**Structure reference**: `.env.example`

**Quick access:**

1. Read `.env.local` file
2. Extract needed credentials (HOTELRUNNER*ADMIN*_, BOOKING*ADMIN*_)
3. Use admin accounts by default
4. Handle OTP/reCAPTCHA (request from Omar)

**⚠️ Security**: Never log, output, or store credentials. Read on demand only.

**📖 Full Guide**: [`../operations/CREDENTIALS.md`](../operations/CREDENTIALS.md)

### Communication with Said

**Required Protocol**:

1. ✅ Vouvoiement obligatoire (formal "vous")
2. ✅ WhatsApp preferred channel
3. ✅ Scout → Rapport → Questions → Action
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
| **Who is Said?**    | [`profiles/SAID-THAIFA.md`](./profiles/SAID-THAIFA.md) (detailed profile)               |
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

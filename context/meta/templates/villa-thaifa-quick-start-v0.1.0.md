# Villa Thaifa — Quick Start Guide

**Version:** 0.1.0-alpha.0  
**Date:** 2026-01-09  
**Purpose:** Guide Omar through creating the new Villa Thaifa project and importing context

---

## PHASE 3: MIGRATION (You + Lux)

This guide walks you through migrating Villa Thaifa content into a dedicated Claude.ai Project.

---

## STEP 1: CREATE NEW PROJECT

### 1.1 In Claude.ai Interface

1. Navigate to Projects (left sidebar)
2. Click **"New Project"**
3. **Project Name:** `Villa Thaifa`
4. **Description (optional):**
   ```
   Client project: Villa Thaifa maison d'hôte (Marrakech)
   Owner: Said Thaifa
   Focus: HotelRunner integration, multi-platform booking management
   ```
5. Click **"Create"**

---

## STEP 2: UPLOAD ARTIFACTS

### 2.1 Files to Upload

You have **5 core artifacts** from this extraction:

| File | Purpose |
|------|---------|
| `villa-thaifa-client-brief-v0.1.0.md` | Complete client profile & requirements |
| `villa-thaifa-technical-context-v0.1.0.md` | Technical architecture & approach |
| `villa-thaifa-decisions-log-v0.1.0.md` | All architectural decisions |
| `villa-thaifa-open-questions-v0.1.0.md` | Unresolved questions & blockers |
| `villa-thaifa-quick-start.md` | This guide |

### 2.2 Upload Process

1. Open the new **Villa Thaifa** project
2. Start a new conversation
3. Click the **📎 (paperclip)** icon to attach files
4. Upload all 5 files
5. Add this message:

```
Salut Lux,

Je viens de migrer le contexte Villa Thaifa dans ce project dédié.

Voici les 5 artifacts qui consolident tout ce qu'on sait:
1. Client Brief - Profil complet de Said Thaifa et Villa Thaifa
2. Technical Context - Architecture, HotelRunner, intégrations
3. Decisions Log - Toutes les décisions prises
4. Open Questions - Ce qui reste à clarifier
5. Quick Start - Ce guide

Prochaine étape: On attaque les questions critiques (B-001, B-002, F-001).

Prêt?
```

---

## STEP 3: CONFIGURE PROJECT CONTEXT

### 3.1 Set Project Instructions (Optional but Recommended)

In the Project settings, you can add custom instructions:

```markdown
# Villa Thaifa Project Context

**Client:** Said Thaifa  
**Business:** Maison d'hôte, Marrakech  
**Focus:** Multi-platform booking management via HotelRunner

## Key Constraints
- No signed contract yet (in negotiation)
- 1 week revenue loss already occurred
- Everything-as-Code (EaC) methodology
- Multi-tenant architecture (future clients coming)

## Priority Questions
1. Define "transform to app" scope (B-001)
2. Confirm platform priority list (B-002)
3. Finalize contract & budget (F-001)

## Technical Approach
- HotelRunner as single source of truth
- Code Execution preferred over MCP (context window)
- Room configuration by number (not type)

## Resources
All context consolidated in uploaded artifacts.
```

---

## STEP 4: VALIDATE CONTEXT

### 4.1 Test Lux's Understanding

Send this message to Lux:

```
Lux, quiz rapide pour vérifier que tu as le contexte:

1. Quel est le problème principal avec Booking.com?
2. Quelles sont les 3 questions critiques bloquantes?
3. Quelle est la différence entre MCP et Code Execution?

Réponds sans consulter les fichiers (juste mémoire).
```

**Expected Result:**
Lux should be able to answer from the uploaded context.

---

## STEP 5: NEXT ACTIONS

### 5.1 Immediate (Today/Tomorrow)

**Action 1:** Draft message to Said Thaifa

Use Lux to help draft a message covering:
- Confirm platform priority list (B-002)
- Clarify "app" scope (B-001)
- Request room numbering details (B-003)
- Discuss contract/budget (F-001)

**Action 2:** Research Go Siyaha

Ask Lux to research:
```
Lux, recherche en ligne: Go Siyaha financement Maroc.

Questions:
1. C'est quoi exactement?
2. 90% financement = 90% de quoi?
3. Éligibilité pour Villa Thaifa?
4. Process et timeline?
```

---

### 5.2 Short-term (This Week)

**Technical Research:**
- [ ] Code Execution implementations (Anthropic, Cloudflare, Docker)
- [ ] HotelRunner API capabilities (REST + XML)
- [ ] Competitor analysis methodology

**Planning:**
- [ ] Draft Statement of Work (SOW) for Said
- [ ] Define Phase 1 deliverables clearly
- [ ] Estimate timeline & budget

---

### 5.3 Medium-term (2-4 Weeks)

**Architecture:**
- [ ] Finalize repo structure (pending overall el-mountassir/ architecture)
- [ ] Design database schema
- [ ] Define agent workflows

**Implementation:**
- [ ] Build HotelRunner integration (MCP or Code Execution)
- [ ] Create internal dashboard (MVP)
- [ ] Test multi-platform sync

---

## STEP 6: MAINTAIN PROJECT KNOWLEDGE

### 6.1 Update Artifacts as You Progress

As decisions are made and questions are answered:

1. **Update Decisions Log:**
   - Change status from "Proposed" to "Accepted"
   - Add new decisions as they emerge

2. **Update Open Questions:**
   - Mark resolved questions
   - Add new questions as they arise

3. **Update Client Brief:**
   - Add contract details once signed
   - Update timelines
   - Track deliverables

### 6.2 Versioning

When making significant updates:
- Increment version: v0.1.0 → v0.2.0
- Keep changelog in each file
- Date all updates

---

## STEP 7: COORDINATE WITH MAIN PROJECT

### 7.1 Link to el-mountassir/ Structure

Once Omar decides on overall architecture (collective/ vs nous/, repo structure), update:

```markdown
# In Villa Thaifa Project

**Location in Overall Structure:**
`~/el-mountassir/projects/villa-thaifa/`
(or wherever it ends up)

**Related Projects:**
- `collective/` or `nous/` (shared knowledge)
- `nexus/` (if that becomes the umbrella)
```

---

## TROUBLESHOOTING

### Issue: Lux Can't Find Context

**Symptom:** Lux asks questions already answered in artifacts

**Solution:**
1. Verify files were uploaded successfully
2. Ask Lux to read a specific file: "Lux, lis villa-thaifa-client-brief-v0.1.0.md"
3. If persistent, re-upload files

---

### Issue: Context Window Full

**Symptom:** Can't upload more files or conversation is slow

**Solution:**
1. Start a new conversation within the project
2. Upload only the most relevant 2-3 artifacts
3. Reference others by name when needed

---

### Issue: Conflicting Information

**Symptom:** Artifacts say different things

**Solution:**
1. Identify the conflict
2. Check version numbers and dates
3. Update the newer artifact to resolve
4. Increment version number

---

## SUCCESS CRITERIA

You'll know the migration was successful when:

✅ Lux can answer questions about Villa Thaifa without re-explaining  
✅ All critical context is preserved in artifacts  
✅ New conversations in this project "just work" with context  
✅ No need to re-upload files for each conversation  

---

## FINAL CHECKLIST

Before considering migration complete:

- [ ] New "Villa Thaifa" project created in Claude.ai
- [ ] All 5 artifacts uploaded
- [ ] Lux validated context (quiz passed)
- [ ] First message sent outlining next steps
- [ ] This project isolated from main el-mountassir/ conversations

---

## WHAT'S NEXT?

### Immediate Priority: The 3 Critical Questions

Work with Lux to:

1. **Draft message to Said** (B-001, B-002, F-001)
2. **Research Go Siyaha** (F-002)
3. **Research Code Execution** (T-001)

Once you have answers to the critical questions:

4. **Finalize SOW (Statement of Work)**
5. **Sign contract**
6. **Begin Phase 1 implementation**

---

## CONTACT LUX

In the Villa Thaifa project, you can say:

```
Lux, on commence par quoi?
```

And Lux will guide you through the critical path based on:
- Open questions status
- Decisions made
- Current blockers

---

**Project Status:** Ready to begin  
**Blocker Status:** 3 critical questions (B-001, B-002, F-001)  
**Next Milestone:** Contract signature  

---

*"Petit à petit, l'oiseau fait son nid"* 🐦

---

**End of Quick Start Guide**

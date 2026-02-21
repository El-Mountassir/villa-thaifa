# Lessons Learned — Villa Thaifa

> This file documents errors and learnings to prevent repetition.
> To be consulted by future AI agents and humans working on this project.

---

## [2025-12-19] Client Communication: Scout → Report → Action Pattern

### The mistake

Sent a message to Said asking for info (guest name, rate, number of adults) WITHOUT first reporting what we had discovered as a scout.

**Context**: Booking mission for room 11 on HotelRunner. We successfully connected, verified availability, prepared the form — but asked the client for info without first communicating the good news.

**Impact**: Client receives questions without context → impression that we don't have the situation under control.

### What should have been done

```text
1. SCOUT    → Explore the platform, verify feasibility
2. REPORT   → Keep Omar informed of discoveries, then determine if Omar (who serves as a bridge between our AI team and clients) should pass the information along or keep it internal
3. QUESTIONS → Ask for missing info (with context)
4. ACTION   → Execute once everything is clear
```

### Correct pattern

| Phase         | Action                  | Example                                    |
| ------------- | ----------------------- | ------------------------------------------ |
| **Scout**     | Explore as a scout      | Connect, verify availability               |
| **Report**    | Inform the client       | "Good news, the room is available"         |
| **Questions** | Ask for what is missing | "To finalize, I need..."                   |
| **Action**    | Execute                 | Create the reservation                     |

### Client communication checklist

Before sending a message to Omar, verify:

- [ ] Do I have ALL the **context** to understand the situation?
- [ ] Have I informed Omar of what I **discovered**?
- [ ] Does Omar have the **context** to understand my questions?
- [ ] Does my message show that we **have the situation under control**?
- [ ] Have I shown **empathy** (putting myself in his place)?

### Corrective message sent

After realizing the mistake, a follow-up message was sent:

```
Actually Omar, I should have started with this:

Good news — we successfully connected to HotelRunner and room 11
(family suite) is AVAILABLE for the 2 nights!

The reservation form is ready, I just need the info I asked for
in my previous message.

[Entity name]
```

### Lesson learned

> **Never assume the client knows what we know.**
> Always report before asking for actions/info.
> Client empathy = putting yourself in their place and imagining what they receive.

---

## [2025-12-19] Communication Tone: Adapt Register to Context

### The mistake

Messages drafted with too informal/casual a tone ("tu", casual style) for a client aged 60+ in a professional context.

**Problematic example**:

```
Actually Said, I should have started with this...
```

**What should have been written**:

```
Monsieur Thaifa,

Please accept my apologies, I should have started by informing you that...
```

### Factors to consider

| Factor       | Impact on register              |
| ------------ | ------------------------------- |
| Relationship | New client → formal             |
| Culture      | Morocco → respect for elders    |
| Stakes       | High-ticket → professionalism   |

### Correct register for this client

- Formal register ("vous/vouvoiement") mandatory
- Respect without corporate rigidity
- Never use: "Salut", "tu", casual abbreviations

### Adaptation by channel (WhatsApp)

| Situation                      | Approach                              |
| ------------------------------ | ------------------------------------- |
| **First message of the day**   | Greeting + signature                  |
| **Follow-up (same thread)**    | Direct, fluid, no repeated greeting   |
| **Important/formal message**   | Greeting + signature                  |

**Fluid example (follow-up message)**:

```
My apologies, I should have started with this:
Good news — [content]
```

**No need for**: "Monsieur Thaifa" + "Cordialement, Omar" on EVERY message.

### Pre-send checklist for client messages

- [ ] Did I use the formal register (vouvoiement)?
- [ ] Is the tone adapted to the client's age and status?
- [ ] Is there an appropriate courtesy phrase?
- [ ] Is the message structured professionally?

### Lesson learned

> **Always adapt communication register to the client's context.**
> When in doubt, choose the more formal register.
> A too-formal message is rarely poorly received; a too-casual one can be.

---

## [2025-12-20] Client Deliverables: Ready-to-Use Files

### The mistake

Created a `.md` file with the WhatsApp message containing metadata, explanation sections, and context — when Omar needed a `.txt` file ready to copy-paste directly.

**What was done**:

```
draft-message-rapport-reservations.md  ← Markdown with metadata
```

**What was expected**:

```
2025-12-20-message-rapport-reservations.txt  ← Plain text ready to copy
```

### Impact

- Omar must manually extract the message from the markdown file
- Wasted time
- Unnecessary friction in the workflow

### What should have been done

When preparing a client deliverable (message, email, document):

| Type                  | Format           | Naming                            |
| --------------------- | ---------------- | --------------------------------- |
| WhatsApp/SMS message  | `.txt`           | `YYYY-MM-DD-message-[subject].txt` |
| Email                 | `.txt` or `.eml` | `YYYY-MM-DD-email-[subject].txt`  |
| Report/Document       | `.pdf`           | `report-[subject]-YYYY-MM-DD.pdf` |
| Internal notes        | `.md`            | Free                              |

### Deliverable structure

```
communication/
├── whatsapp/
│   ├── 2025-12-20-message-rapport-reservations.txt  ← Ready to copy
│   └── draft-*.md                                    ← Drafts/notes
│
projects/[project]/
└── deliverables/
    └── report-[subject]-YYYY-MM-DD.pdf               ← Final PDF
```

### Pre-creation checklist for client deliverables

- [ ] Is the file **directly usable** without extraction?
- [ ] Is the format appropriate for use (`.txt` to copy, `.pdf` to send)?
- [ ] Does the naming include the **date** and **subject**?
- [ ] Is the file in the **correct folder** (deliverables/, whatsapp/)?

### Lesson learned

> **A client deliverable must be ready to use, not a working document.**
> Always ask: "Can Omar use this file immediately without manipulation?"
> If no → wrong format or wrong structure.

---

## [2025-12-22] Date Confusion: Always Verify the Year

### The mistake

Dates mentioned without an explicit year, creating confusion between 2024 and 2025. Particularly problematic during year transitions (December → January).

### Impact

- Misunderstanding of deadlines
- Risk of incorrect planning
- Confusion in reservation history

### What must be done

| Situation                          | Action                         |
| ---------------------------------- | ------------------------------ |
| Client mentions "December 20th"    | Ask/confirm the year           |
| Date near New Year                 | Double-check the year          |
| Reservation for "January"          | Clarify 2025 or 2026           |

**Verification pattern**:

- Always specify the full year (e.g., "December 20, 2025")
- Check the year when a client mentions only month/day
- Extra attention near year transitions (Dec → Jan)

### Lesson learned

> **Always verify the year.** "December 20th" could be 2024 or 2025.
> Never assume — always make it explicit.

---

## Template for future lessons

```markdown
## [YYYY-MM-DD] Short title

### The mistake

[Factual description of what happened]

### Impact

[Consequences of the mistake]

### What should have been done

[The correct approach]

### Lesson learned

[Generalizable principle]
```

## [2025-12-23] Room Structure Feedback from Said

**What happened**: After state-management restructuring, presented data to Said. He requested room-centric view instead of type-grouped.

**Why it matters**: Client's daily operations reference rooms by number. Our structure should match his workflow.

**Root cause**: Technical structure was based on data normalization (group by type) rather than user's mental model (individual rooms).

**Action taken**: Restructured to individual room files + facilities model.

**Future prevention**:

- Always validate data structure with primary user before finalizing
- Ask: "How do you talk about these entities in daily work?"
- Client-facing data should use client's vocabulary (ubiquitous language)

**Pattern recognized**: Client-Centric Data Modeling (documented in `shared/memory/patterns.md`)

---

## [2025-12-28] Commission Economics — CRITICAL for all instances

### Business Context

| Channel                    | Commission | On €1000   |
| -------------------------- | ---------- | ---------- |
| Booking.com                | **25%**    | Net: €750  |
| Expedia, etc.              | ~15-25%    | Variable   |
| Direct (phone, email)      | **0%**     | Net: €1000 |

### Why this is HUGE

```
Direct reservation = +33% net margin vs Booking.com
```

**Villa Thaifa will connect 20+ platforms** → The commission impact is MASSIVE.

### Implication for AI Agents

> **Mr. Thaifa prefers direct reservations when possible.**
> This is NOT just a personal preference — it is a rational economic decision.
> Even for clients who are not friends/family.

**ALWAYS UNDERSTAND**:

- "Direct" reservation on HotelRunner = client contacted directly = 0% commission
- Reservation via Booking/Expedia = 25% commission lost
- When Mr. Thaifa says "direct reservation" → it is to save on commissions

### Lesson learned

> **Booking platforms are an ACQUISITION channel, not the goal.**
> The goal is to maximize net revenue — direct reservations contribute to this.

---

## [2025-12-28] Tunnel Vision — Room 5 "Sync Bug" Case

### The mistake (Tunnel Vision)

An AI instance saw:

- Room 5 reserved on HotelRunner (Benchekroum)
- But not visible on Booking.com

**Hasty conclusion**: "SYNC BUG! P0! URGENT INVESTIGATION!"

### What was missed (ZOOM OUT)

The real question should have been:

> "Is this reservation SUPPOSED to be on Booking.com?"

**Probable answer**: No. It is a direct reservation.

- Direct reservations are created on HotelRunner only
- They are NOT automatically synchronized to Booking.com
- Dates must be manually blocked on Booking.com

### The real problem

This is not a "sync bug" — it is:

1. A knowledge gap about how the platforms work
2. An undocumented workflow for direct reservations

### Anti-Tunnel Vision Pattern

Before creating a "bug investigation" mission, ALWAYS ask:

```
1. Is this a bug or a behavior I don't understand?
2. Have I ZOOMED OUT on the business context?
3. Have I verified the basic assumptions?
```

### Related documentation

- Full strategy: `docs/strategic/2025-12-28-platform-mastery-strategy.md`
- Skill: `.claude/skills/tunnel-vision-prevention/`

---

## [2025-12-28] Platform Knowledge Gap

### Finding

Neither AI agents nor Omar fully understand:

- HotelRunner (Channel Manager)
- Booking.com Extranet
- The room mapping between the two
- Synchronization flows

### Risk

Without this understanding:

- Possible reservation errors
- Misunderstood sync issues
- Tunnel vision on "bugs" that are not bugs

### Plan

A "Platform Mastery" project is documented in:
`docs/strategic/2025-12-28-platform-mastery-strategy.md`

### Lesson learned

> **Before operating on a platform, make sure you understand it.**
> If you don't understand → document the gap and plan the learning.

---

## [2025-12-28] HotelRunner — Price Adjustment Workflow

### Discovery

To modify the price during a manual reservation on HotelRunner:

### Path

```
Reservations > New reservation > 2. Select room type
```

### Steps

1. Select the room type (e.g., "Double Superior Room")
2. Click on the **"Number of rooms"** dropdown
3. Select the number of rooms (e.g., 1)
4. Once selected → a **"Price adjustment"** link appears
5. Click "Price adjustment"
6. A pop-up menu opens allowing you to modify the price

### Use cases

- Direct reservations with negotiated rate
- Special promos not configured in the system
- Friends/family rates

### Lesson learned

> **The price is not directly editable in the field.**
> You must go through "Price adjustment" which appears AFTER selecting the number of rooms.

---

## [2025-12-28] Chrome Extension — Issues with HotelRunner

### Observed problem

The Claude in Chrome extension frequently loses connection with HotelRunner tabs. Tabs "detach" after a few interactions.

### Impact

- Reservation automation is difficult
- Requires frequently recreating tabs
- Sometimes impossible to complete a task automatically

### Current workaround

- Provide detailed manual instructions to Omar
- Omar executes manually while AI guides

### Future investigation

- Check if it is an extension permissions issue
- Test with other browsers
- Explore HotelRunner API as an alternative

---

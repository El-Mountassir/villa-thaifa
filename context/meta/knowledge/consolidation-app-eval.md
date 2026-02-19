# Prompt Evaluation: Villa Thaifa Consolidation + App

**Score: 2.8/10** (Critical)

| Dimension     | Score  | Notes                                                                                                 |
| ------------- | ------ | ----------------------------------------------------------------------------------------------------- |
| Clarity       | 2/10   | Stream of consciousness. 10+ topics interleaved. No structure.                                        |
| Completeness  | 3/10   | Good raw material but key info missing: what data exists, what app type, what Said needs specifically |
| Actionability | 3.5/10 | Asks for investigation + plan mode — that part is clear. But scope is unbounded.                      |

## Diagnosed Issues

1. **Brain dump** — 10+ concerns mixed together (data dispersal, app type, GitHub repos, YAML files, HotelRunner, OTAs, credit limits, Said's access)
2. **Scope creep** — One prompt tries to solve: data consolidation + app development + PRD/SRS + deployment + GitHub cleanup + credit management
3. **Missing context** — What data exists where? What does Said actually need day-to-day? What's HotelRunner's role exactly?
4. **Contradictions** — "I haven't told you everything" + "investigate so you know everything" = impossible without Omar's input
5. **No deliverable defined** — What does "done" look like?

## Extracted Workstreams (7 distinct problems)

| #   | Workstream                                                         | Type          | Priority                     |
| --- | ------------------------------------------------------------------ | ------------- | ---------------------------- |
| W1  | Data audit: map ALL villa-thaifa data across all locations/formats | Investigation | P0 — must happen first       |
| W2  | Data consolidation: centralize into single SSOT                    | Execution     | P0 — depends on W1           |
| W3  | App definition: what type, what features, for whom                 | Discovery/PRD | P1 — needs Omar + Said input |
| W4  | App development: PRD → SRS → Architecture → Code                   | Development   | P1 — depends on W3           |
| W5  | GitHub cleanup: resolve 2 repos, fresh start                       | DevOps        | P1 — quick win               |
| W6  | HotelRunner/OTA sync: channel manager integration                  | Integration   | P2 — depends on W2+W4        |
| W7  | Claude credit management: delegation to Gemini/Kilo                | Meta/Process  | Separate concern             |

## Rewrite (Structured)

### Phase 1: Investigation (agents, no Omar input needed)

> **Goal**: Map the complete state of villa-thaifa data.
>
> **Tasks**:
>
> 1. Audit ~/villa-thaifa/ — full tree, all file types, DB schema + row counts
> 2. Audit ~/omar/ for any villa-thaifa scattered content
> 3. Check both GitHub repos (El-Mountassir/villa-thaifa-property-management + omar-elmountassir/villa-thaifa) — what's in each, last activity, differences
> 4. Inventory all data formats: YAML, SQLite, MD, JSON, etc.
> 5. Identify gaps: what data SHOULD exist but doesn't
>
> **Output**: Single audit report file with findings.

### Phase 2: Discovery (needs Omar's answers)

> **Questions to resolve before planning**:
>
> 1. What does Said need to DO daily? (view bookings? edit prices? create OTA listings?)
> 2. What's HotelRunner's current role — is it the channel manager you already use?
> 3. Is the app mainly a CRUD dashboard for property data, or does it need booking management too?
> 4. Vercel deployment — is this a web app Said accesses via browser?
> 5. What data is currently ONLY in Said's head (not captured anywhere)?

### Phase 3: Plan Mode (after Phase 1+2)

> Enter plan mode with full context to produce:
>
> - PRD (Product Requirements Document)
> - SRS (Software Requirements Specification)
> - Architecture decision
> - Phased implementation plan
> - New GitHub repo setup (private, clean start)

### Separate: Credit Management

> Persist a rule about Gemini/Kilo delegation for cost control. Not part of villa-thaifa work.

## Recommendation

Execute Phase 1 immediately (agent investigation). Then ask Omar the Phase 2 questions. Then enter plan mode.

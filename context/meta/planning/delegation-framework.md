# Multi-Model Delegation Framework

**Version**: 2.0 (Villa Thaifa PMS)
**Last Updated**: 2026-02-13
**Applies To**: All complex multi-phase projects requiring orchestration + delegation

---

## Design Principle

**Route by TASK COMPLEXITY, not model name.** Models ship every 1-2 months — the routing logic stays, the model filling each slot changes. This framework is version-agnostic.

---

## CLI Arsenal (4 tools, each has strengths)

| CLI             | Provider       | Access                  | Best For                                            | Install                     |
| --------------- | -------------- | ----------------------- | --------------------------------------------------- | --------------------------- |
| **Claude Code** | Anthropic      | Max plan (Omar)         | Orchestration, code quality, architecture           | Already installed           |
| **Codex CLI**   | OpenAI         | ChatGPT Business (Omar) | Reliability, code review, structured output (JSONL) | ✅ v0.101.0 installed       |
| **Gemini CLI**  | Google         | Free tier (1000 RPD)    | Bulk research, large context (1M), web grounding    | ✅ v0.28.2 installed        |
| **Kilo CLI**    | Multi-provider | Free (GLM-5)            | 500+ models, parallel execution, cost-free bulk     | Already installed (v1.0.13) |

---

## Task Complexity → Model Routing Matrix

Route tasks by what they NEED, not by model name. Current best model per slot (update when new models ship):

| Task Type                   | Complexity  | Capability Needed       | Current Best Model    | CLI         | Why                                 |
| --------------------------- | ----------- | ----------------------- | --------------------- | ----------- | ----------------------------------- |
| File exploration, search    | Low         | Speed, cheap            | Claude Haiku 4.5      | Claude Code | 10x cheaper, 90% capability         |
| Translation, formatting     | Low         | Accuracy, cheap         | Gemini 2.5 Flash-Lite | Gemini CLI  | $0.10/1M input, free tier           |
| Component code (UI)         | Medium      | Code quality            | Claude Sonnet 4.5     | Claude Code | Best quality-to-cost, 77% SWE-bench |
| API integration code        | Medium-High | Reliability             | Codex (GPT-5.3)       | Codex CLI   | "Never breaks codebases" reputation |
| Full-page implementation    | Medium      | Code quality + speed    | Claude Sonnet 4.5     | Claude Code | $0.08/task, fastest execution       |
| Frontend/UI prototyping     | Medium      | UI understanding        | Gemini 3 Pro          | Gemini/Kilo | WebDev Arena leader                 |
| Document drafting (PRD/SRS) | Medium      | Long context, synthesis | Gemini 2.5 Pro        | Gemini CLI  | 1M context, $1.25/1M input          |
| Code review                 | Medium-High | Judgment, reliability   | Codex (GPT-5.3)       | Codex CLI   | Strong review + JSONL output        |
| Architecture decisions      | High        | Deep reasoning          | Claude Opus 4.6       | Claude Code | 81% SWE-bench, adaptive thinking    |
| Complex debugging           | High        | Multi-file reasoning    | Claude Opus 4.6       | Claude Code | 1M context, sustained agentic       |
| Full-repo refactoring       | High        | Large context           | Gemini 2.5 Pro        | Gemini CLI  | 1M tokens, context caching          |
| Algorithmic reasoning       | High        | Chain-of-thought        | DeepSeek R1           | Kilo CLI    | o1-level at 95% less cost           |
| Bulk mechanical transforms  | Any         | Throughput, free        | GLM-5 (free)          | Kilo CLI    | Zero cost, parallel execution       |

---

## Model Strength Matrix (what each excels at)

| Strength     | Claude Opus | Sonnet | Haiku | Codex (GPT-5.3) | Gemini Pro | Gemini Flash | DeepSeek R1 |
| ------------ | :---------: | :----: | :---: | :-------------: | :--------: | :----------: | :---------: |
| Architecture |     +++     |   ++   |   +   |       ++        |     ++     |      +       |      +      |
| Code quality |     +++     |  +++   |  ++   |       +++       |     ++     |      +       |     ++      |
| Speed        |      +      |  +++   |  +++  |       ++        |     ++     |     +++      |      +      |
| Cost         |      +      |   ++   |  +++  |  ++ (flat sub)  |     ++     |     +++      |     +++     |
| Long context |     +++     |   ++   |   +   |       ++        |    +++     |      ++      |      +      |
| Reliability  |     ++      |   ++   |   +   |       +++       |     ++     |      +       |     ++      |
| UI/Frontend  |     ++      |   ++   |   +   |       ++        |    +++     |      ++      |      +      |
| Reasoning    |     +++     |   ++   |   +   |       ++        |     ++     |      +       |     +++     |

---

## Cost Comparison (per 1M tokens, Feb 2026)

| Model             | Input    | Output   | Effective Daily Cost | Notes                        |
| ----------------- | -------- | -------- | -------------------- | ---------------------------- |
| Claude Opus 4.6   | $5.00    | $25.00   | ~$10                 | Reserve for orchestration    |
| Claude Sonnet 4.5 | $3.00    | $15.00   | ~$10                 | Workhorse for code           |
| Claude Haiku 4.5  | ~$0.25   | ~$1.25   | <$1                  | Exploration only, NOT code   |
| Codex (GPT-5.3)   | Flat sub | Flat sub | $0 marginal          | Included in ChatGPT Business |
| Gemini 2.5 Pro    | $1.25    | $10.00   | ~$6                  | Long-context champion        |
| Gemini 2.5 Flash  | $0.30    | $2.50    | ~$2                  | Good balance                 |
| Gemini Flash-Lite | $0.10    | $0.40    | <$1                  | Bulk processing              |
| DeepSeek R1       | $0.12    | $0.20    | <$1                  | Algorithmic reasoning        |
| GLM-5 (via Kilo)  | FREE     | FREE     | $0                   | Bulk mechanical work         |

---

## Per-Phase Delegation (Villa Thaifa PMS)

| Phase           | Orchestrator | Code Writing | Documents        | Bulk/Mechanical  | Review      |
| --------------- | ------------ | ------------ | ---------------- | ---------------- | ----------- |
| 0: Foundation   | Opus (5%)    | Sonnet (60%) | Gemini Pro (20%) | Kilo/GLM-5 (15%) | Codex       |
| 1: Documents    | Opus (10%)   | —            | Gemini Pro (70%) | Flash-Lite (10%) | Codex (10%) |
| 2: MVP          | Opus (10%)   | Sonnet (65%) | —                | Flash-Lite (10%) | Codex (15%) |
| 3: Reservations | Opus (15%)   | Sonnet (50%) | Gemini Pro (10%) | —                | Codex (25%) |
| 4: Full Feature | Opus (10%)   | Sonnet (45%) | Gemini Pro (15%) | Flash-Lite (10%) | Codex (20%) |

---

## Hard Rules (persist for all future instances)

```
1. Opus = orchestration + architecture ONLY. Never write code in Opus context.
2. Code writing = Sonnet 4.5+ minimum. NEVER Haiku for code (too low quality).
3. Haiku = exploration, file search, quick lookups ONLY.
4. Documents (PRD/SRS/research) = Gemini 2.5 Pro (1M context, cheaper).
5. Code review = Codex CLI (reliability strength, flat cost).
6. Bulk mechanical = Kilo/GLM-5 (free) or Gemini Flash-Lite ($0.10/1M).
7. Never read >50 lines of code in Opus context — delegate to Sonnet agent.
8. Always tell Kilo to write output to FILES, not stdout.
9. When model X ships: test on 3 tasks → update matrix → persist.
```

---

## Adaptive Update Protocol

When a new model ships (Sonnet 5, DeepSeek V4, Gemini 4, etc.):

1. Add it to the research brief at `~/omar/knowledge/research/ai/llm-delegation-strategy-2026.md`
2. Test on 3 representative tasks from current project
3. Update the routing matrix if it outperforms current slot holder
4. Persist the change in the delegation skill at `~/.claude/skills/`

**Upcoming to watch**:

- Claude Sonnet 5 (expected soon) → likely replaces Sonnet 4.5 in all code slots
- DeepSeek V4 (expected Feb 17, 2026) → may challenge Claude for code generation
- Gemini 3 Pro GA → pricing + performance finalization

---

## Villa Thaifa Specific Delegation Decisions

### Phase 0: Foundation

- **Scaffold**: Sonnet agent (standard Next.js setup, low risk)
- **Schema design**: Sonnet agent (from existing property.db + rooms.yaml)
- **Seed script**: Sonnet agent (straightforward data transform)
- **Review**: Codex (validate schema quality, catch migration issues)

### Phase 1: Documents (12 files)

- **PRD (French)**: Gemini 2.5 Pro (1M context, can read all existing docs, cheap)
- **SRS**: Gemini 2.5 Pro (synthesis from PRD + existing pages)
- **DB_SCHEMA.md**: Sonnet agent (technical writing from SQL)
- **API_SPEC.md**: Sonnet agent (from HotelRunner research brief)
- **CHANNEL_MAPPING.md**: Sonnet agent (structured data, 5 OTAs)
- **ARCHITECTURE.md**: Omar (orchestrator) — requires integration judgment
- **Review all docs**: Codex (consistency check across 12 files)

### Phase 2: MVP (7 deliverables)

- **Room list + card**: Sonnet agent (standard CRUD UI)
- **Room detail + edit**: Sonnet agent (form with Zod validation)
- **Pricing table**: Sonnet agent (bulk edit + currency API)
- **French strings**: Gemini Flash-Lite (translation extraction, cheap)
- **Review**: Codex (code quality before merge)
- **NextAuth + Vercel setup**: Omar (config-level, requires credentials)

### Phase 3: Reservations (5 deliverables)

- **Reservation list + detail**: Sonnet agent (CRUD pages)
- **Calendar view**: Sonnet agent (FullCalendar.js integration)
- **HotelRunner API client**: Codex CLI (reliability-critical, live system, rate limits)
- **Review API client**: Codex (safety validation: idempotent, error handling, caching)
- **Live testing**: Omar (real credentials, production monitoring)

### Phase 4: Full Feature (6 deliverables)

- **HotelRunner push API**: Codex CLI (bidirectional sync, highest risk)
- **Revenue/occupancy reports**: Sonnet agent (Recharts integration)
- **Email templates**: Sonnet agent (French templates + Resend)
- **Seasonal pricing logic**: Gemini 2.5 Pro (research + implementation spec)
- **Full code review**: Codex (safety-critical before go-live)
- **Dry-run approval**: Omar (final go/no-go decision)

---

## Research Produced (persist for future sessions)

- `~/omar/knowledge/research/ai/llm-delegation-strategy-2026.md` — Full model comparison
- `~/omar/knowledge/research/ai/gemini-claude-orchestration-guide.md` — CLI integration patterns
- `~/omar/knowledge/research/ai/codex-cli-evaluation.md` — Codex CLI capabilities

---

## Testing Requirements Before Execution

| Test | Tool       | Task                          | Pass Criteria                                  | Status           |
| ---- | ---------- | ----------------------------- | ---------------------------------------------- | ---------------- |
| 1    | Codex CLI  | Code review on existing file  | Returns JSONL output, catches issues           | ⏳ PENDING       |
| 2    | Gemini CLI | Draft 1-page spec from 3 docs | 1M context handles all inputs, coherent output | ⏳ PENDING       |
| 3    | Kilo/GLM-5 | Bulk file rename (10 files)   | Writes to files, not stdout, zero cost         | SKIPPED (proven) |

---

_This framework is version-agnostic. Update the MODEL names in the matrix, but keep the ROUTING LOGIC unchanged._

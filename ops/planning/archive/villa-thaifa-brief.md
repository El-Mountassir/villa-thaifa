# Villa Thaifa Brief

## Metadata

— Session 2026-01-08 (12 PM - 2 PM)

## Current State

| Aspect       | Status                                                                                                                                                                |
| ------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Contract** | ❌ NONE — Urgent formalization required                                                                                                                               |
| **Phase**    | 1 (Cleanup & Foundation) — In progress                                                                                                                                |
| **Repo**     | 329 files, poorly structured - a complete refactoring is mandatory, building an app with db, frontend, backend etc. // Draw inspiration from / reuse IndyDevDan demos |
| **App Code** | ❌ NON-EXISTENT — Doc/ops system only                                                                                                                                 |

---

## Past Lessons (To Remember)

1. **Scout → Report → Questions → Action** — Always report findings BEFORE asking for information
2. **Formal tone with Mr. Thaifa** — Respectful addressing ("vous"), respect for elders is mandatory
3. **Ready-to-use deliverables** — `.txt` for WhatsApp, no `.md` with metadata
4. **Commission savings** — Direct = 0%, Booking = 25% lost (MASSIVE impact)
5. **Anti Tunnel Vision** — Zoom out before calling it a "bug"
6. **94% confidence rule** — If < 94% confidence → STOP & ASK Omar

---

## What is Missing to "Transform into an App"

### Option A: Management Web App

```sh
villa-thaifa-app/
├── frontend/          # React/Next.js dashboard
│   ├── reservations/  # Calendar view
│   ├── pricing/       # Pricing management
│   └── reports/       # Analytics
├── backend/           # Node/Python API
│   ├── hotelrunner/   # API integration (create an MCP for our agents??)
│   ├── booking/       # Booking.com sync (do they have an MCP for our agents??)
│   └── .../           # Sync all other platforms (do they have an MCP for our agents??)
└── mobile/            # PWA or React Native ## NOT A PRIORITY !!
```

### Option B: Automation-First (More realistic short-term)

```sh
Keep current structure + add:
├── scripts/
│   ├── sync-hotelrunner.py    # API automation
│   ├── daily-report.py        # Auto reports
│   └── notification-bot.py    # WhatsApp/Telegram
└── infra/
    └── cron/                   # Scheduled tasks
```

### Option C: Hybrid (Recommended)

1. **Short-term**: Automation scripts on top of the existing structure
2. **Medium-term**: Simple web dashboard (Streamlit/Gradio)
3. **Long-term**: Full app with backend API

---

## Priorities Tomorrow 12 PM

### P0 — Strategic Decisions

1. **App or Automation first?** (Option A/B/C)
2. **Mr. Thaifa's Contract** — When?
3. **Go Siyaha** — 90% funding — Investigate?

### P1 — Technical

1. **HotelRunner API** — Request status with Ikram?
2. **Tech stack** — If app: Next.js? Python? Other?
3. **IndyDevDan curriculum** — What to use?

### P2 — Organization

1. **Link el-mountassir → villa-thaifa** — How to integrate?
2. **Vibe Kanban** — For mission management?

---

## Open Questions

1. "Transform into an app" = what exactly?
   [x] Custom web dashboard for Mr. Thaifa and for us (Omar + AI agents)
   [?] Backend automation scripts? Why not see if we can combine everything

2. What is the realistic timeline?
   [x] This week (Proof of Concept / Minimum Viable Product / Minimum Lovable Product / fast prototype)

3. HotelRunner API — Reply from Ikram?
   [x] Yes, access granted https://developers.hotelrunner.com/

---

## Resources

### Available Resources

| Resource                | Location    | Usage                      |
| ----------------------- | ----------- | -------------------------- |
| IndyDevDan curriculum   | To locate   | Agent patterns             |
| Vibe Kanban             | To activate | Project management         |
| Core Four               | ops/        | Model/Context/Prompt/Tools |
| docs/lessons-learned.md | This repo   | Mistakes to avoid          |

---

## North Star

> **One M-Shaped Generalist + AI agents = full management of 10+ hotel properties.**

Villa Thaifa = first template property.

---

_Prepared by Claude Code — 2026-01-08 01:30_

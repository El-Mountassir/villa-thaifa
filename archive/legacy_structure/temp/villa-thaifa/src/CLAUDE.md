# Source Code — CLAUDE.md

> **Domain**: Villa Thaifa application code
> **Parent context**: `../CLAUDE.md` (inherits all project rules)

---

## Directory Structure

```
src/
├── apps/           # Full applications
│   ├── dashboard/  # Management dashboard (future)
│   ├── api/        # Backend API (future)
│   └── automation/ # Automation scripts (future)
├── packages/       # Shared libraries
└── tools/          # CLI tools, utilities
```

---

## Development Rules

| Rule            | Description                                      |
| --------------- | ------------------------------------------------ |
| **EaC Pattern** | Everything as Code — Docs, Config, Infra, Agents |
| **Type Safety** | Prefer TypeScript where applicable               |
| **Monorepo**    | Shared packages in `packages/`                   |

---

## App Structure (Future)

Each app in `apps/` should have:

```
apps/{app-name}/
├── CLAUDE.md       # App-specific context
├── src/            # Source code
├── tests/          # Test files
└── README.md       # App documentation
```

---

## Currently Empty

This directory is prepared for future development:

- Dashboard for M. Thaifa
- API for integrations
- Automation for HotelRunner/Booking.com

---

_Hierarchical context for src/_

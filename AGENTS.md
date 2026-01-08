# AGENTS.md — Villa Thaifa

> Standard multi-agent documentation for any AI assistant.
> Based on [GitHub best practices (2025)](https://github.blog/ai-and-ml/github-copilot/how-to-write-a-great-agents-md-lessons-from-over-2500-repositories/).

---

## Project Overview

## [Project Overview](project/OVERVIEW.md) @project/OVERVIEW.md

## Commands

| Command                | Purpose                |
| ---------------------- | ---------------------- |
| `tree -a --dirsfirst`  | View project structure |
| `git status`           | Check working tree     |
| `pandoc + wkhtmltopdf` | Generate PDF reports   |

### PDF Generation

```bash
# Markdown → HTML → PDF
pandoc rapport.md -o /tmp/temp.html --standalone --self-contained --css=docs/templates/report-style.css
wkhtmltopdf --enable-local-file-access --page-size A4 --margin-top 12mm --margin-bottom 12mm /tmp/temp.html output.pdf
```

---

## Project Structure

[project/STRUCTURE.md](project/STRUCTURE.md)

---

## Conventions

### File Naming

| Type        | Pattern                            | Example                               |
| ----------- | ---------------------------------- | ------------------------------------- |
| Dated files | `YYYY-MM-DD-description.md`        | `2025-12-22-hws-introduction.md`      |
| Reports     | `rapport-{subject}-YYYY-MM-DD.pdf` | `rapport-reservations-2025-12-20.pdf` |
| Messages    | `YYYY-MM-DD-message-{subject}.txt` | `2025-12-22-reservation-akram.txt`    |

### Markdown Style

- **Headers**: ATX style (`#`, `##`, `###`)
- **Lists**: Dashes (`-`) for unordered
- **Tables**: For structured data (always)
- **Code blocks**: Triple backticks with language
- **Emphasis**: `**bold**` for critical info

---

## Git Workflow

### Commit Format

```
type(scope): description

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude Opus 4.5 <noreply@anthropic.com>
```

### Types

| Type       | Usage                     |
| ---------- | ------------------------- |
| `feat`     | New feature or capability |
| `fix`      | Bug fix                   |
| `docs`     | Documentation changes     |
| `chore`    | Maintenance, cleanup      |
| `refactor` | Code restructuring        |

---

## Boundaries

### ✅ Always Do

- Read `docs/lessons-learned.md` before client actions
- Use **vouvoiement** with M. Thaifa (formal French)
- Backup before modifying important files (`cp file.md file.md.backup-YYYY-MM-DD`)
- Verify details before platform operations (room numbers, dates, prices)
- Use exact system values (never calculate/approximate)

### ⚠️ Ask First

- Modifying `data/specs/` files destructively
- Deleting any file
- Sending messages to client
- Platform operations (HotelRunner, Booking.com)
- Creating reservations

### 🚫 Never Do

- Commit credentials in plain text
- Use client account (M. Thaifa) on platforms — use Admin Omar
- Guess room numbers or prices
- Rush without checkpoints (PACE CONTROL)
- Skip the SCOUT → REPORT → QUESTIONS → ACTION pattern

---

## Key Rules

READ [ai/rules/README.md](ai/rules/README.md)

## Key References

| File                           | Purpose                                  |
| ------------------------------ | ---------------------------------------- |
| `CLAUDE.md`                    | Claude-specific rules and context        |
| `data/specs/platform/rules.md` | Platform safety rules (4 CRITICAL)       |
| `.env` / `.env.example`        | Platform credentials (READ .env.example) |
| `docs/lessons-learned.md`      | Past errors (READ BEFORE CLIENT ACTIONS) |

---

## Platform-Specific Notes

### HotelRunner

- Channel manager for OTA distribution
- Contact: Ikram (HWS Support) — see `data/admin/client/CONTACT.md`
- API status: Pending (Ikram checking with technical team)

### Booking.com

- Primary OTA channel (25% commission)
- Promotions managed via Extranet
- Use Admin Omar account, not client account

---

_AGENTS.md v2.0.0 — Updated for v5 structure (EaC + Agentic AI)_

# Browser Agent — Villa Thaifa Project Context

> Loaded dynamically by the generic browser-agent when operating in this project.
> This file contains ALL Villa-Thaifa-specific platform rules, extraction protocols, and safety requirements.

---

## Platform Rules (Zero Tolerance)

**Source**: `context/meta/knowledge/rules.md`

Before any platform operation involving HotelRunner or Booking.com, read and comply with all rules in
`/home/director/villa-thaifa/context/meta/knowledge/rules.md`.

### Trust-Based Action Rule

- Confidence < 90% → **STOP EVERYTHING and ASK Omar**
- Applies to: platform clicks, room/rate changes, guest actions, irreversible submissions

### Dates/Details Verification Rule

Before executing any booking or change, repeat all key details to Omar and wait for explicit "yes":

```
"I will create: Room X, from DD to DD/MM, name: Y, price: Z"
```

Details to confirm: dates, room number, guest name, exact price.

### Use Exact System Values

- **NEVER calculate or approximate** — copy the exact value from the platform (e.g., "4,512.21 MAD" not "~4500 DH")

### Pre-Execution Checklist

- [ ] Confidence > 90%?
- [ ] Details repeated to Omar?
- [ ] Exact values (not calculated)?
- [ ] Data files not modified destructively?

If any answer is NO → **STOP** and adjust.

---

## HotelRunner

**Reference guides** (read before any HotelRunner operation):

- `.agents/hotelrunner/EXTRACTION-GUIDE.md` — field-by-field extraction protocol
- `.agents/hotelrunner/SETUP.md` — platform setup and configuration
- `.agents/hotelrunner/guide.md` — general operational guide

Key safety rule: A mistake on HotelRunner can affect live guest reservations. Zero tolerance.

---

## Booking.com

**Reference**: `.agents/booking/capabilities.json`

Read `.agents/booking/capabilities.json` before any Booking.com operation to understand
platform-specific capabilities and constraints.

---

## Expedia Partner Central

**Protocol**: `~/omar/knowledge/research/business/expedia-extraction-protocol.md`

Before any Expedia Partner Central extraction, READ the protocol at that path and follow it exactly.

**Key rule — EXHAUSTIVE CAPTURE**: Every field, every value, checked AND unchecked, filled AND empty. No exceptions. Data will be reused for future properties beyond Villa Thaifa.

---

## OTA Extractions (General)

When extracting data from any OTA (Online Travel Agency) platform:

- Capture ALL fields exhaustively — checked and unchecked, yes and no, filled and empty
- Data will be reused for future properties; completeness is critical

---

## Screenshot Storage

Archive screenshots to: `~/.claude/data/browser-agent/screenshots/YYYY-MM-DD/`

Naming convention: descriptive, underscore-separated, lowercase (e.g., `hotelrunner_room_rates_2026-02-21.png`).

Never delete screenshots. This is a preservation requirement.

---

## Data Files Protection

Before any destructive modification of data files (`data/`):

| Action type               | Required confirmation |
| ------------------------- | --------------------- |
| Overwrite existing data   | MANDATORY ASK         |
| Replace values (not add)  | MANDATORY ASK         |
| Delete/remove information | MANDATORY ASK         |
| Change counters/metrics   | MANDATORY ASK         |
| Add NEW data alongside    | OK to proceed         |

Process: READ current data → IDENTIFY what exists vs what is new → ADD new data WITHOUT deleting existing → if modification necessary, STOP and ASK Omar.

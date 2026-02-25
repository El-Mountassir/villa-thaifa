# Platform Operations Rules — Villa Thaifa

> **CRITICAL**: These rules apply to ANY operation on HotelRunner, Booking.com, or other platforms.
> Zero tolerance — A mistake can affect guest reservations.

---

## ⚠️ Trust-Based Action Rule

> **If confidence < 90% → STOP EVERYTHING and ASK Omar.**

### Concerned Contexts

| Context              | Examples                           |
| -------------------- | ---------------------------------- |
| Platform operations  | Clicks on HotelRunner, Booking.com |
| Room/rate changes    | Room selection, rate adjustments   |
| Guest actions        | Bookings, cancellations            |
| Irreversible actions | Submissions, confirmations         |

### Process

```text
1. PAUSE before clicking/submitting
2. VERIFY against documentation (data/rooms/rooms.md, etc.)
3. If uncertain → STOP → ASK → Wait for confirmation
4. NEVER guess or assume on platform operations
```

**Context**: Added 2025-12-22 after Room 11 near-miss.

---

## ⚠️ Dates/Details Verification Rule

> **ALWAYS repeat key details to Omar BEFORE executing.**

| Detail          | Action                                         |
| --------------- | ---------------------------------------------- |
| **Dates**       | Repeat "From X to Y" and wait for confirmation |
| **Room number** | Confirm "Room X" explicitly                    |
| **Guest name**  | Spell the name                                 |
| **Price**       | Announce total before submission               |

### Booking process

```text
1. ANALYZE the request carefully
2. REPEAT: "I will create: Room X, from DD to DD/MM, name: Y, price: Z"
3. WAIT for a "yes" or a correction
4. THEN execute
```

**Context**: Added 2025-12-22 after date error ("25 to 27" instead of "24 to 27").

---

## ⚠️ Use Exact System Values

> **NEVER calculate/approximate — use the EXACT value from the platform.**

| ❌ Wrong             | ✅ Correct                        |
| -------------------- | --------------------------------- |
| "4500 DH (3 × 1500)" | "4,512.21 MAD" (from HotelRunner) |
| "~280€"              | "280.00 €" (exact)                |

**Rule**: Always copy the final total from HotelRunner/Booking.com. Systems may add fees, taxes, or rounding.

---

## ⛔ Data Files Protection

> **FULL STOP required before any destructive modification of data/specs files.**

| Action type               | Required confirmation |
| ------------------------- | --------------------- |
| Overwrite existing data   | ✅ MANDATORY ASK      |
| Replace values (not add)  | ✅ MANDATORY ASK      |
| Delete/remove information | ✅ MANDATORY ASK      |
| Change counters/metrics   | ✅ MANDATORY ASK      |
| Add NEW data alongside    | ❌ OK to proceed      |

### Update data process

```text
1. READ current data carefully
2. IDENTIFY what exists vs what is new
3. ADD new data WITHOUT deleting existing
4. If modification necessary → STOP → ASK OMAR
```

### Example (rooms.md)

- ❌ WRONG: "Room types: 9" → "Room types: 8" (data destroyed)
- ✅ RIGHT: Add "Room types (Booking.com): 8" next to existing

> **Justification**: Data files = SSOT. Different platforms may have different data.

---

## Pre-Execution Checklist

Before any platform action:

- [ ] Confidence > 90%?
- [ ] Details repeated to Omar?
- [ ] Exact values (not calculated)?
- [ ] Data files not modified destructively?

If any answer is NO → **STOP** and adjust.

---

<i>Platform Operations Rules v0.1.0-alpha.0 — Zero Tolerance</i>

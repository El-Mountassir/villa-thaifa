# Example: Validation Agent (Yellow)

> **Role Type**: Validation
> **Color**: Yellow
> **Semantic**: Gatekeeper, checks, warnings, caution

---

## Example Agent: platform-validator

```yaml
---
name: platform-validator
description: Platform data validator. Validates all inputs before HotelRunner/Booking.com operations. Use BEFORE any platform submission to prevent costly errors.
tools: Read, Glob, Grep
color: yellow
model: sonnet
permissionMode: plan
---

# Purpose

A gatekeeper agent that validates all data before platform operations. Ensures confidence thresholds are met, data is exact (never calculated), and explicit confirmation is obtained before execution proceeds.

## Instructions

- **NEVER execute** — Validation and confirmation only
- **ALWAYS read source files** — Verify data accuracy from specs
- **REQUIRE exact values** — Reject any calculated or approximated data
- **BLOCK if any check fails** — No partial passes

## Workflow

1. Receive operation request with proposed data
2. Read relevant spec files (rooms, pricing, reservations)
3. Validate each data point against specs
4. Run platform checklist (confidence, exactness, completeness)
5. Generate validation report
6. If ALL PASS: Format confirmation request
7. If ANY FAIL: List failures with remediation steps

## Report

[Validation checklist with PASS/FAIL status for each check]
```

---

## Why This Works

| Aspect | Value | Rationale |
|--------|-------|-----------|
| **Color** | yellow | Validation/caution role |
| **Model** | sonnet | Structured validation needs moderate capability |
| **Tools** | Read, Glob, Grep | Read-only — validators never modify |
| **permissionMode** | plan | Extra safety — read-only mode |
| **Description** | "Use BEFORE any platform submission" | Clear gatekeeper trigger |

---

## Other Validation Agent Examples

- `data-checker` — Validates data integrity
- `security-validator` — Checks for security issues
- `format-validator` — Validates file formats

---

## Key Pattern: Gatekeeper

Validation agents follow the **Gatekeeper Pattern**:

1. **Trigger**: "Use BEFORE any [action]"
2. **Tools**: Read-only (never Write, Edit, Bash)
3. **Permission**: `plan` mode for extra safety
4. **Output**: PASS/FAIL with clear reasons
5. **No execution**: Only validates, never acts

---

_Example: Validation Agent — Agent Creation Standards_

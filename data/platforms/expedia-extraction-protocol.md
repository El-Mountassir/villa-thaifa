# Expedia Partner Central — Extraction Protocol

**Purpose**: Standard operating procedure for extracting data from Expedia Partner Central onboarding wizard. Applies to Villa Thaifa AND all future properties.

---

## Core Rule: EXHAUSTIVE CAPTURE

**Every field, every value, every state — no exceptions.**

This means:
- Checked AND unchecked checkboxes
- Selected AND unselected radio buttons
- Filled AND empty text inputs
- Dropdown values AND all available options
- Yes/No answers — capture BOTH states explicitly
- Default values vs user-set values (note which is which when possible)

**Why**: Properties evolve. Future properties will need the same data. A "No" today is a potential "Yes" tomorrow. Omitting unchecked fields makes the extraction useless for comparison, auditing, and onboarding new properties.

---

## Extraction Format

Each step gets its own file: `expedia-step{N}-extraction.md`

### Header (mandatory)
```markdown
# Expedia Partner Central — Step {N} Extraction

**Property**: {name} (htid={id})
**Step**: {N} of 12
**Title**: {step title}
**URL**: {full URL}
**Extracted**: {YYYY-MM-DD}
**Note**: READ ONLY — no form values were modified during extraction
```

### Body
- One section per module/subsection on the page
- Tables for form fields: `| Field | Value | State |`
- State column: `Checked`, `Unchecked`, `Selected`, `Not selected`, `Empty`, `Default`
- Screenshots: take at least 1 per major section for verification

### Footer
```markdown
## Extraction Summary
- Total fields: {N}
- Filled/checked: {N}
- Empty/unchecked: {N}
- Modules: {list}
```

---

## Safety Rules

1. **READ ONLY** — never click save, submit, or modify any field
2. **Navigation only** — step tabs, scroll, accordion expand
3. **If unsure about a button** — describe it, don't click it
4. **If login required** — STOP and report, don't guess credentials
5. **Screenshot before leaving each step** — proof of state

---

## Multi-Property Pattern

When extracting for a new property, use the same file naming:
`expedia-step{N}-extraction-{property-slug}.md`

This enables side-by-side comparison between properties.

---

_Protocol version: 1.0 | Created: 2026-02-21_

# Environment Files — Rules for AI Agents

> **CRITICAL**: These rules apply to ALL operations on `.secrets/.env` and `.env.example`

---

## 🔴 FORBIDDEN ACTIONS

### On `.secrets/.env` (REAL credentials)

- **NEVER** delete passwords or credentials
- **NEVER** replace real values with placeholders like "example_password_here"
- **NEVER** modify existing credential values without EXPLICIT Omar request
- **NEVER** comment out active credential lines

**PENALTY**: These actions destroy access to production systems

---

## ✅ ALLOWED ACTIONS

### On `.secrets/.env`

- Add NEW variables (if they follow the existing structure)
- Improve documentation/comments (without touching values)
- Reorganize sections (without touching values)
- Fix typos in comments

### On `.env.example`

- Replace placeholders with better examples
- Add missing sections to match `.secrets/.env` structure
- Improve documentation
- Fix formatting/alignment

---

## 🔒 SIGNATURE REQUIRED

Any modification to `.secrets/.env` credential **VALUES** requires:

1. **Explicit request** from Omar El Mountassir
2. **Digital signature** (confirmation message)
3. **Documentation** in commit message

**Example**:

```
Omar: "Delete the EXPEDIA_ADMIN_PASSWORD from .secrets/.env"
Agent: "I need your explicit signature to delete this credential.
       This will break Expedia access. Confirm?"
Omar: "I confirm, delete it."
Agent: [Proceeds with deletion + documents in commit]
```

---

## 📋 VALIDATION CHECKLIST

Before modifying `.secrets/.env`:

- [ ] Am I preserving ALL existing credential values?
- [ ] Am I ONLY adding documentation, NOT changing values?
- [ ] Is this a NEW variable (not modifying existing)?
- [ ] Did Omar explicitly request this change?

If ANY answer is "NO" → STOP and ask Omar

---

## 🚨 EMERGENCY

If you accidentally delete/modify a credential:

1. **IMMEDIATELY** admit the mistake to Omar
2. **DO NOT** try to fix it yourself
3. **PROVIDE** the git history so Omar can restore
4. **DOCUMENT** the incident in docs/incidents/

---

**Version**: 1.0
**Created**: 2026-01-24
**Owner**: Omar El Mountassir
**Enforcement**: Mandatory for ALL AI agents

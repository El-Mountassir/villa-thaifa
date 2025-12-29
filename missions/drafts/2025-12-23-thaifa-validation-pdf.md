# Mission: Villa Thaifa Validation PDF for Said

```yaml
# Core Metadata
mission_id: 2025-12-23-thaifa-validation-pdf
type: STANDARD
status: DRAFT
priority: P3

# Assignment
assigned_to: Claude Code
created: 2025-12-23
assigned:
claimed_at:
claimed_by:
completed:
archived:

# Source tracking
source_session: "Thaifa session 2025-12-23"
source_insight: "Said needs formal document to review/validate room structure"

# Verification (Updated by /mission complete)
verification:
  self_reviewed: false
  gates_passed: "0/7"
  blocking_issues: []
  last_verified:
```

---

## Context

Create professional PDF report for M. Said Thaifa to:
1. Review proposed room structure
2. Validate/correct information
3. Provide missing details
4. Sign approval

**Language**: French (formal register - vouvoiement)

**Dependencies**: M1, M2, M3 must be complete

---

## Objectives

- [ ] Design PDF template in French (formal)
- [ ] Generate room fiches for all 12 rooms
- [ ] Include facilities overview
- [ ] List missing information for Said to complete
- [ ] Include signature section for validation

---

## Success Criteria

| #   | Criterion                                    | Status | Evidence |
| --- | -------------------------------------------- | ------ | -------- |
| 1   | PDF template designed                        | ⬜     |          |
| 2   | All 12 rooms have fiches                     | ⬜     |          |
| 3   | Facilities section included                  | ⬜     |          |
| 4   | Missing info section clearly marked          | ⬜     |          |
| 5   | Signature/validation section present         | ⬜     |          |
| 6   | PDF generated and saved                      | ⬜     |          |

---

## Constraints

- Language: French only
- Tone: Formal (vouvoiement)
- Format: PDF (generated from markdown via pandoc or similar)
- Client name: M. Said Thaifa
- Omar can sign on Said's behalf if authorized

---

## Specification

### PDF Structure

```
RAPPORT DE VALIDATION — VILLA THAIFA
Configuration des Chambres et Installations

═══════════════════════════════════════

TABLE DES MATIÈRES
1. Synthèse Exécutive
2. Structure Proposée
3. Chambres (1-12) — Fiches Individuelles
4. Installations (Spa, Piscine, Jardin, Hall)
5. Informations Manquantes
6. Signature de Validation

═══════════════════════════════════════

[Per-room fiche template]

CHAMBRE X — [Type Name]

📊 Informations de Base
   • Numéro: X
   • Type: [Type]
   • Lits: [Beds]
   • Capacité: X personnes

❓ À Valider / Compléter
   ☐ Surface totale: _____ m²
   ☐ Vue: [ ] Jardin  [ ] Piscine  [ ] Autre: _____
   ☐ Étage: _____
   ☐ Caractéristiques uniques: _________________

✓ Prix
   • Marge nette cible: XXX€
   • Prix Booking.com: XXX€

═══════════════════════════════════════

VALIDATION

Date: _______________

Signature M. Said Thaifa:


_______________________

Validé par Omar El Mountassir:
☐ Oui  ☐ Non

Date: _______________  Signature: _________________
```

---

## Execution Log

> Append-only. Add entries as work progresses.

### 2025-12-23

- 19:45 - Mission created in drafts/ directory

---

## Deviations

[Document any differences from original spec. What changed and why.]

---

## Lessons Learned

[What to do differently next time. Patterns to extract. Rules to add.]

---

## Quality Gates (Pre-Archive)

- [ ] All success criteria have evidence
- [ ] All requirements validated
- [ ] All tasks completed
- [ ] Execution log is complete
- [ ] Deviations documented
- [ ] Lessons learned captured
- [ ] Files in correct archive location

---

_Mission created from template v0.3.0 (verification-enhanced)_

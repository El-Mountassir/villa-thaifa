# Pattern Extraction

**Date**: 2025-12-20
**Objective**: Transformer les observations en principes réutilisables

---

## Extracted Patterns

### Pattern 1: Commission Impact Formula

| Attribute | Value |
|-----------|-------|
| **Observed In** | Internal docs, Mews, Cvent, XOTELS |
| **Formula** | `Net = Prix_Affiché × (1 - Discount%) × (1 - Commission%)` |
| **Underlying Principle** | Les discounts et commissions se composent multiplicativement, pas additivement |
| **Generalization Test** | Applicable à tout OTA avec commission? → **YES** |
| **Confidence** | **HIGH** |

**Example**:
```
Prix affiché: 200€
Discount: 40%
Commission Booking: 25%

Net = 200 × 0.60 × 0.75 = 90€ (pas 200 - 40% - 25% = 70€)
```

**Reusable insight**: Toujours calculer l'impact composé, jamais additif.

---

### Pattern 2: Industry Discount Ceiling

| Attribute | Value |
|-----------|-------|
| **Observed In** | Mews, Cvent, XOTELS, Prostay |
| **Rule** | 10-25% = range optimal pour OTAs à haute commission |
| **Underlying Principle** | Au-delà de 25%, le rate dilution et l'érosion de marge dépassent les bénéfices de volume |
| **Generalization Test** | Applicable à autres OTAs? → **YES** (Expedia, Hotels.com, etc.) |
| **Confidence** | **HIGH** |

**Decision matrix**:

| Discount | Commission 15% | Commission 25% | Recommendation |
|----------|---------------|----------------|----------------|
| 10% | 76.5% retained | 67.5% retained | ✅ Safe |
| 20% | 68% retained | 60% retained | ✅ Acceptable |
| 30% | 59.5% retained | 52.5% retained | ⚠️ Caution |
| 40% | 51% retained | 45% retained | ❌ Avoid |

---

### Pattern 3: Execution Verification Method

| Attribute | Value |
|-----------|-------|
| **Observed In** | Execution log Villa Thaifa |
| **Method** | Plan → Execute → Log → Verify Checklist |
| **Underlying Principle** | La documentation systématique permet la vérification post-hoc |
| **Generalization Test** | Applicable à autres tâches critiques? → **YES** |
| **Confidence** | **HIGH** |

**Checklist template**:
```markdown
## Post-Execution Verification
- [ ] Toutes les actions planifiées exécutées
- [ ] Aucune action non planifiée effectuée
- [ ] État final vérifié visuellement
- [ ] Documentation mise à jour
```

---

### Pattern 4: Highest-Discount-Wins (Booking.com Specific)

| Attribute | Value |
|-----------|-------|
| **Observed In** | Booking.com official documentation |
| **Rule** | Quand plusieurs promotions sont actives, seule la plus élevée s'applique |
| **Underlying Principle** | Booking.com protège contre le stacking excessif |
| **Generalization Test** | Applicable à autres OTAs? → **PARTIAL** (varie par plateforme) |
| **Confidence** | **HIGH** (pour Booking.com uniquement) |

**Implication**: Avoir plusieurs petites promos (10%, 15%, 20%) n'est pas plus risqué qu'une seule grande promo. Le risque est dans la PLUS HAUTE promo active.

---

## Anti-Patterns Identified

### Anti-Pattern 1: Assumption Creep

| Attribute | Value |
|-----------|-------|
| **Observed** | Utilisation de 120€ comme marge universelle |
| **Problem** | Documenté seulement pour 2/12 chambres, appliqué partout |
| **Why it's bad** | Conclusions techniquement correctes mais exemples trompeurs |
| **Alternative** | Toujours utiliser les valeurs spécifiques documentées |

---

### Anti-Pattern 2: Example Conflation

| Attribute | Value |
|-----------|-------|
| **Observed** | Exemple 200€ (Deluxe Triple) pour illustrer marge 120€ (Double Superior) |
| **Problem** | Mélange de room types crée confusion |
| **Why it's bad** | Lecteur peut mal interpréter les calculs |
| **Alternative** | Un exemple par room type, ou utiliser des variables génériques |

---

### Anti-Pattern 3: Stacking Myth Propagation

| Attribute | Value |
|-----------|-------|
| **Observed** | Claim "40% + 10% géociblé = 50%" dans rapport |
| **Problem** | Booking.com ne permet pas ce cumul |
| **Why it's bad** | Risque surévalué, décisions potentiellement sous-optimales |
| **Alternative** | Vérifier les policies officielles avant de calculer des cumuls |

---

## Patterns Summary

| Pattern | Confidence | Reusability |
|---------|------------|-------------|
| Commission Impact Formula | HIGH | Universal |
| Industry Discount Ceiling | HIGH | OTA-wide |
| Execution Verification Method | HIGH | Universal |
| Highest-Discount-Wins | HIGH | Booking.com only |

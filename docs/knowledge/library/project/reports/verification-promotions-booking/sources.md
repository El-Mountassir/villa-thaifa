# Source Triangulation

**Date**: 2025-12-20
**Objective**: Valider les claims sur les promotions Booking.com avec des sources multiples

---

## Sources

### Source 1: Documents Internes Villa Thaifa

- **Type**: Internal Documentation
- **Files**: `execution-log-booking.md`, `plan-promotions-booking.md`, `rapport-promotions-msaid.md`
- **Key Claims**:
  - 40%+ promotions = marge nette négative vs objectif 120€
  - Formule: `Net = Prix × (1 - Discount) × 0.75`
  - Les promotions "cumulent" créant des risques de stacking
- **Evidence Quality**: **Strong** (math vérifiable, logs détaillés)
- **Potential Bias**: Optimisme sur l'universalité de la marge 120€

---

### Source 2: Industry Research (Mews, Cvent, XOTELS)

- **URLs**:
  - https://www.mews.com/en/blog/hotel-pricing-strategies
  - https://www.cvent.com/en/blog/hospitality/hotel-pricing-strategies
  - https://www.xotels.com/en/revenue-management/ota-revenue-management-advice
- **Type**: Practitioner / Official Documentation
- **Key Claims**:
  - 10-25% = range de discount normal pour OTAs
  - 25-40% = réservé aux last-minute sur canaux directs uniquement
  - 40%+ = rate dilution risk, "guests get conditioned to wait for discounts"
  - Maximum stackable sur Booking.com = 20%
- **Evidence Quality**: **Strong** (consensus multi-sources, practitioners reconnus)
- **Potential Bias**: Focus sur best practices, pas sur cas spécifiques Maroc

---

### Source 3: Booking.com Official Documentation (via Zeevou, Rentals United)

- **URLs**:
  - https://zeevou.com/blog/booking-com-promotions/
  - https://rentalsunited.com/blog/booking-com-opportunities/
- **Type**: Official / Authoritative
- **Key Claims**:
  - **Promotions NE CUMULENT PAS** — seul le discount le plus élevé s'applique
  - "If you have multiple active promotions, the highest discount will be offered"
  - "Deep deals are never stackable with other pricing offers"
  - Max combined discount = 20% pour overlapping audiences
- **Evidence Quality**: **Strong** (policy Booking.com officielle)
- **Potential Bias**: Aucun — documentation factuelle

---

## Convergence Analysis

| Pattern | Source 1 (Interne) | Source 2 (Industry) | Source 3 (Booking) | Confidence |
|---------|-------------------|---------------------|-------------------|------------|
| 40%+ discount est excessif | ✅ AGREE | ✅ AGREE | N/A | **HIGH** |
| Math commission 25% | ✅ AGREE | ✅ AGREE | ✅ AGREE | **HIGH** |
| Formule Net = Prix×(1-D)×0.75 | ✅ AGREE | ✅ AGREE | ✅ AGREE | **HIGH** |
| Promotions cumulent (stacking) | ✅ AGREE | ⚠️ PARTIAL | ❌ **DISAGREE** | **LOW** |
| 120€ margin est universel | ASSUMED | GAP | GAP | **LOW** |
| 10-15% post-fix = optimal | ✅ AGREE | ✅ AGREE | ✅ AGREE | **HIGH** |

---

## Decision Points (Disagreements)

### 1. Stacking / Cumul des promotions

| Position | Source | Evidence |
|----------|--------|----------|
| "Promotions cumulent" | Interne | Exemple: 40% + 10% = 50% |
| "Highest discount wins" | Booking.com | Official policy documentation |

**Resolution**: Booking.com documentation est **authoritative**. Les promotions **NE CUMULENT PAS**. Le claim interne était incorrect.

**Impact**: Le risque de stacking était surévalué. Cependant, les promotions individuelles de 40%+ restent destructrices même sans cumul.

---

### 2. Universalité de la marge 120€

| Position | Source | Evidence |
|----------|--------|----------|
| "120€ = marge cible" | Interne | Documenté pour chambres 4&5 uniquement |
| Variable par chambre | Interne (grille) | 120€ à 450€ selon type |

**Resolution**: La marge 120€ n'est **pas universelle**. Les calculs auraient dû utiliser les marges spécifiques par chambre.

**Impact**: Les conclusions restent valides (40%+ EST destructeur pour TOUTES les marges documentées), mais la précision des exemples est questionnable.

---

## Source Quality Summary

| Source | Reliability | Relevance | Recency |
|--------|-------------|-----------|---------|
| Internal Docs | High | High | Current |
| Mews/Cvent/XOTELS | High | High | 2024-2025 |
| Booking.com (Zeevou) | High | High | 2024-2025 |

**Overall triangulation confidence**: **HIGH** for main claims, **LOW** for stacking claim

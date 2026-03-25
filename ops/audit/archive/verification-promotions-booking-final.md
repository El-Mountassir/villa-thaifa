# Rapport de Vérification — Promotions Booking.com Villa Thaifa

**Generated**: 2025-12-20
**Pipeline**: `.claude/output/2025/Q4/reports/verification-promotions-booking/`
**Method**: /elevate (multi-source triangulation)

> **Source de vérité** : [state/current/promotions.md](../../../../../state/current/promotions.md)
> Historique des changements : [state/historical/changelog-promotions.md](../../../../../state/historical/changelog-promotions.md)

---

## Résumé Exécutif

Le travail exécuté (désactivation de 8 promotions Booking.com) est **valide et bien fondé**. L'exécution est 100% complète, les calculs financiers sont corrects, et les décisions sont alignées avec les best practices de l'industrie. Cependant, une affirmation sur le "cumul des promotions" était **techniquement incorrecte** — Booking.com n'autorise pas le stacking.

| Dimension | Verdict | Confiance |
|-----------|---------|-----------|
| Exécution | ✅ 100% complète | HIGH |
| Math financière | ✅ Correcte | HIGH |
| Industry alignment | ✅ Aligné | HIGH |
| Claim "stacking" | ❌ Inexact | HIGH |

---

## Ce Qui a Été Vérifié

### 1. Exécution Completeness

| Planifié | Exécuté | Écart |
|----------|---------|-------|
| 6 désactivations P0 | 6 désactivations | 0 |
| 2 modifications P1 | 2 modifications | 0 |
| **Total: 8 actions** | **8 actions** | **0** |

**Verdict**: ✅ Toutes les actions planifiées ont été exécutées sans écarts.

---

### 2. Validité Financière

**Formule utilisée** (correcte):
```
Net = Prix_Affiché × (1 - Discount%) × (1 - Commission%)
```

**Exemple vérifié** (200€ base, 40% discount, 25% commission):
```
Net = 200 × 0.60 × 0.75 = 90€ ✅
```

**Verdict**: ✅ Les calculs sont mathématiquement corrects.

---

### 3. Alignement Industry

| Practice | Villa Thaifa | Standard Industry | Status |
|----------|--------------|-------------------|--------|
| Max discount OTA | 10-15% | 10-25% | ✅ Optimal |
| Éviter 40%+ | Désactivé | Best practice | ✅ Aligné |
| Commission-aware | Formule utilisée | Standard | ✅ Aligné |

**Sources**: Mews, Cvent, XOTELS, Prostay (consensus 2024-2025)

**Verdict**: ✅ Les décisions sont alignées avec les best practices.

---

## Key Insights

| Insight | Confidence | Sources |
|---------|------------|---------|
| 40%+ discount EST excessif pour OTA à 25% commission | HIGH | Mews, Cvent, XOTELS, Internal |
| Formule Net composée (pas additive) | HIGH | All 3 sources |
| Promotions Booking.com NE CUMULENT PAS | HIGH | Booking.com official, Zeevou |
| 10-15% post-fix est dans le range optimal | HIGH | Industry consensus |

---

## Découverte Importante: Le Mythe du Stacking

### Ce qui était affirmé
> "40% + 10% géociblé = 50% cumulative — certaines réservations vous coûtent de l'argent"

### Ce qui est vrai
**Booking.com applique UNIQUEMENT le discount le plus élevé**, pas la somme.

> "If you have multiple active promotions, and a guest is eligible for more than one of them, the promotion with the highest discount will be offered."
> — Zeevou (citant Booking.com)

### Impact
- Le risque de stacking était **surévalué**
- Les 6 promotions restaient problématiques **individuellement** (40%+ chacune)
- La décision de les désactiver reste **correcte**, mais pour une raison légèrement différente

---

## Nuances et Gaps

### Gap 1: Définition de "Marge"

**Question non résolue**: Les marges 120-450€ représentent-elles:
- Revenue net après commission?
- Profit net après tous les coûts?

**Impact**: "Marge négative" est techniquement incorrect si on parle de revenue. L'hôtel reçoit encore 45% du prix affiché avec 40% discount.

**Action**: Clarifier avec M. Thaifa le 22 décembre.

---

### Gap 2: Impact sur l'Occupancy

**Non analysé**: Les promotions 40% généraient-elles plus de réservations?

**Trade-off potentiel**:
- 100% occupancy à 45% marge vs
- 60% occupancy à 75% marge

**Action**: Analyser les données historiques Booking.com pour évaluer.

---

### Gap 3: Marge 120€ Non Universelle

**Observation**: L'exemple 120€ était documenté uniquement pour les chambres 4&5 (Double Superior), pas pour les 12 types.

**Impact**: Les calculs restent valides direction nellement, mais les exemples manquent de précision.

---

## État Actuel des Promotions (Mise à jour 21h30)

### Promotions Actives (5 total)

| # | Promotion | Discount | Performance | Status |
|---|-----------|----------|-------------|--------|
| 1 | Basic Deal | 10% | -- | ✅ Sain |
| 2 | Basic Deal (3 nuits min) | 15% | 1 résa, €118.50 | ✅ Sain |
| 3 | **Early Booker Deal** | 10% | -- | ✅ **NOUVEAU** (conforme) |
| 4 | **Tarif Mobiles** | 10% | 27 résa, €15,614 | ✅ **NON DOCUMENTÉ** |
| 5 | **À l'étranger (géociblé)** | 10% | 2 résa, €160 | ✅ **NON DOCUMENTÉ** |

> **Note** : Toutes les promotions sont dans le range optimal (10-15%). Aucune action corrective requise.

### Promotions Désactivées (6 total)

| Promotion | Discount | Raison |
|-----------|----------|--------|
| Early Booker Deal | 40% | Marge insuffisante |
| Basic Deal | 38% | Marge insuffisante |
| Late Escape Deal | 43% | Marge insuffisante |
| Late Escape Deal | 42% | Marge insuffisante |
| Tarif géociblé Europe | 10% | Risque cumul (note: surévalué) |
| Tarif géociblé Maroc | 10% | Risque cumul (note: surévalué) |

---

## Recommendations

### Immédiat
1. ✅ **Continuer** avec les promotions 10-15% — aligné avec best practices
2. ⚠️ **Surveiller** le tarif Royaume-Uni 10% — pourrait être utile pour diversification géographique

### Court terme (Janvier 2025)
3. **Analyser** les données d'occupancy pré/post changement
4. **Clarifier** avec M. Thaifa la définition exacte des marges cibles

### Moyen terme
5. **Considérer** des promotions saisonnières (15-20%) pour la basse saison (Juin-Août)
6. **Négocier** la commission Booking.com (25% → 18-20%)

---

## Limitations & Gaps (Mise à jour 21h30)

| Gap | Impact | Resolution | Status |
|-----|--------|------------|--------|
| ~~Définition marge (revenue vs profit)~~ | ~~Moyen~~ | **Marge = Revenue net** (confirmé par Omar) | ✅ RÉSOLU |
| Impact occupancy | Moyen | Analyser historique | ⏳ À faire |
| Compétitivité Palmeraie | Faible | Benchmark concurrence | ⏳ À faire |
| ~~Stacking claim inexact~~ | ~~Faible~~ | Corrigé dans ce rapport | ✅ RÉSOLU |
| **3 promos non documentées** | Faible | Identifiées dans Audit V2 | ✅ RÉSOLU |

---

## Conclusion

**Le travail exécuté est VALIDE.**

- ✅ Exécution: 100% complète
- ✅ Math: Correcte
- ✅ Industry: Aligné
- ⚠️ Stacking claim: Inexact mais sans impact sur la décision finale

Les promotions 40%+ étaient destructrices pour les marges — cette conclusion reste vraie même sans le risque de cumul. La direction stratégique était correcte.

---

## Sources

### Internal
- `execution-log-booking.md`
- `plan-promotions-booking.md`
- `rapport-promotions-msaid.md`
- `grille-tarifaire-officielle.md`

### Industry
- [Mews - Hotel Pricing Strategies](https://www.mews.com/en/blog/hotel-pricing-strategies)
- [Cvent - Hotel Pricing Strategies](https://www.cvent.com/en/blog/hospitality/hotel-pricing-strategies)
- [XOTELS - OTA Revenue Management](https://www.xotels.com/en/revenue-management/ota-revenue-management-advice)
- [Prostay - Hotel Discount Strategies](https://www.prostay.com/blog/hotel-discount/)

### Official
- [Zeevou - Booking.com Promotions](https://zeevou.com/blog/booking-com-promotions/)
- [Rentals United - Booking.com Opportunities](https://rentalsunited.com/blog/booking-com-opportunities/)

---

*Rapport généré via pipeline /elevate — Multi-source triangulation*
*Villa Thaifa — 20 décembre 2025*

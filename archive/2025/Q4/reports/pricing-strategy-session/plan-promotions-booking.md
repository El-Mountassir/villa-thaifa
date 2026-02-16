# Plan d'Action — Promotions Booking.com

**Date** : 20 décembre 2025
**Statut** : ✅ EXÉCUTÉ (voir liens ci-dessous)
**Hotel ID** : 5446847

> **Sources de vérité** :
> - État AVANT exécution : [state/baseline/promotions-2025-12-20.md](../../../../../state/baseline/promotions-2025-12-20.md)
> - État APRÈS exécution : [state/current/promotions.md](../../../../../state/current/promotions.md)
> - Log d'exécution : [state/execution/2025-12-20/promotions.md](../../../../../state/execution/2025-12-20/promotions.md)

---

## État Initial (Baseline 20 déc 2025)

| # | Promotion | Réduction | Période séjour | Performance | Action |
|---|-----------|-----------|----------------|-------------|--------|
| 1 | Basic Deal | 30% | 8 déc 2025 → 30 nov 2026 | -- | 🟡 P1 : Réduire à **10%** |
| 2 | Basic Deal | 33% | 8 déc 2025 → 30 nov 2026 | 1 résa, 10 nuits, €118.50 | 🟡 P1 : Réduire à **15%** |
| 3 | Basic Deal | **38%** | 8 déc 2025 → 30 nov 2026 | 3 résa, 9 nuits, €102.92 | 🔴 P0 : **DÉSACTIVER** |
| 4 | Tarif géociblé Europe | **10%** | Toujours active | -- | 🔴 P0 : **DÉSACTIVER** |
| 5 | Tarif géociblé Maroc | **10%** | Toujours active | -- | 🔴 P0 : **DÉSACTIVER** |
| 6 | Early Booker Deal | **40%** | 8 déc 2025 → 30 nov 2026 | -- | 🔴 P0 : **DÉSACTIVER** |
| 7 | Late Escape Deal | **43%** | 1 oct 2025 → 7 jan 2026 | -- | 🔴 P0 : **DÉSACTIVER** |
| 8 | Late Escape Deal | **42%** | 1 oct 2025 → 7 jan 2026 | -- | 🔴 P0 : **DÉSACTIVER** |

---

## Résumé des Actions

### 🔴 P0 — Désactivations Immédiates (6 promos)

| Promotion | Réduction | Pourquoi désactiver |
|-----------|-----------|---------------------|
| Early Booker Deal | 40% | Marge nette < 0 après commission 25% |
| Basic Deal | 38% | Marge nette < 0 après commission 25% |
| Late Escape Deal | 43% | Réduction destructrice |
| Late Escape Deal | 42% | Réduction destructrice |
| Tarif géociblé Europe | 10% | Cumul avec autres promos = destruction |
| Tarif géociblé Maroc | 10% | Cumul avec autres promos = destruction |

### 🟡 P1 — Réductions (2 promos)

| Promotion | Avant | Après | Pourquoi |
|-----------|-------|-------|----------|
| Basic Deal (3 nuits min) | 33% | **15%** | Préserver marge minimale |
| Basic Deal (Standard) | 30% | **10%** | Préserver marge minimale |

---

## Impact Financier (Exemple chambre 200€)

| Scénario | Prix client | Commission 25% | Net Villa | vs Objectif 120€ |
|----------|-------------|----------------|-----------|------------------|
| Sans promo | 200€ | -50€ | **150€** | +30€ ✅ |
| Avec Early Booker 40% | 120€ | -30€ | **90€** | -30€ ❌ |
| Avec Basic Deal 38% | 124€ | -31€ | **93€** | -27€ ❌ |
| Avec Late Escape 43% | 114€ | -28.5€ | **85.5€** | -34.5€ ❌ |

---

## Espace Décision Omar

### Question 1 : Valider les désactivations P0 ?

> **Les 6 promotions P0 détruisent la marge. Elles doivent être désactivées.**

- [ ] ✅ OUI — Désactiver les 6 promos P0
- [ ] ❌ NON — Attendre / Discuter

### Question 2 : Valider les réductions P1 ?

> **Les 2 Basic Deals restants doivent être réduits pour préserver la marge.**

- [ ] ✅ OUI — Réduire à 15% et 10%
- [ ] ❌ NON — Autres pourcentages ? (préciser)

### Question 3 : Procéder maintenant ?

- [ ] ✅ OUI — Exécuter maintenant
- [ ] ⏸️ ATTENDRE — Reporter à plus tard

---

## Méthode d'Exécution (si validé)

Pour chaque promo :

1. **Cliquer** sur le nom de la promo
2. **Screenshot** de l'état avant
3. **Désactiver** ou modifier le pourcentage
4. **Screenshot** de confirmation
5. **Logger** dans `execution-log-booking.md`

---

## Notes

- Ces promos ont été configurées par l'ancien gestionnaire
- La commission Booking.com de 25% est élevée (standard = 15%)
- Les tarifs géociblés peuvent se CUMULER avec les autres promos

---

_Document créé le 20 décembre 2025_
_En attente de validation Omar_

# Audit Promotions Booking.com — Villa Thaifa

**Date** : 20 décembre 2025
**Mise à jour** : 20 décembre 2025, 21h30
**Hotel ID** : 5446847
**Statut** : ✅ EXÉCUTÉ + AUDIT V2

> **Source de vérité** : [state/current/promotions.md](../../../../../state/current/promotions.md)
> Baseline avant audit : [state/baseline/promotions-2025-12-20.md](../../../../../state/baseline/promotions-2025-12-20.md)

---

## Résumé Exécutif (MISE À JOUR)

| Indicateur             | Avant (Audit Initial) | Après (État Actuel) |
| ---------------------- | --------------------- | ------------------- |
| Promotions actives     | **8**                 | **5**               |
| Réduction maximale     | **43%**               | **15%**             |
| Commission Booking.com | **25%**               | **25%**             |
| Impact combiné max     | **~58%**              | **~35%** ✅         |

### Changement Net

- **6 promotions désactivées** (P0)
- **2 promotions réduites** (P1)
- **3 nouvelles promotions** identifiées (non documentées initialement)

---

## État Actuel des Promotions (20 déc 2025, 21h)

### Promotions Actives (5 total)

| #   | Promotion                | Réduction | Période réservable         | Dates séjour              | Performance                 | Status               |
| --- | ------------------------ | --------- | -------------------------- | ------------------------- | --------------------------- | -------------------- |
| 1   | Basic Deal               | **10%**   | 8 déc 2025 - Aujourd'hui   | 8 déc 2025 → 30 nov 2026  | --                          | ✅ Optimal           |
| 2   | Basic Deal (3 nuits min) | **15%**   | 8 déc 2025 - Aujourd'hui   | 8 déc 2025 → 30 nov 2026  | 1 résa, 10 nuits, €118.50   | ✅ Optimal           |
| 3   | Early Booker Deal        | **10%**   | 20 déc 2025 - Aujourd'hui  | 20 déc 2025 → 30 nov 2026 | --                          | ✅ **NOUVEAU**       |
| 4   | Tarif Mobiles            | **10%**   | 22 sept 2025 - Aujourd'hui | Toujours active           | 27 résa, 122 nuits, €15,614 | ✅ **NON DOCUMENTÉ** |
| 5   | À l'étranger (géociblé)  | **10%**   | 8 déc 2025 - Aujourd'hui   | Toujours active           | 2 résa, 5 nuits, €160.16    | ✅ **NON DOCUMENTÉ** |

### Analyse des Nouvelles Promotions

| Promotion             | Discount | Dans range optimal? | Conformité stratégie | Action                   |
| --------------------- | -------- | ------------------- | -------------------- | ------------------------ |
| Early Booker Deal 10% | 10%      | ✅ Oui (10-25%)     | ✅ Conforme          | Conserver                |
| Tarif Mobiles 10%     | 10%      | ✅ Oui (10-25%)     | ✅ Conforme          | Conserver (€15K revenus) |
| À l'étranger 10%      | 10%      | ✅ Oui (10-25%)     | ✅ Conforme          | Conserver                |

**Note importante** : Booking.com **NE CUMULE PAS** les promotions — seul le discount le plus élevé s'applique.

### Promotions Désactivées (6 total)

| Promotion             | Réduction | Date désactivation | Raison                   |
| --------------------- | --------- | ------------------ | ------------------------ |
| Early Booker Deal     | ~~40%~~   | 20 déc 2025        | Marge destructrice       |
| Basic Deal            | ~~38%~~   | 20 déc 2025        | Marge destructrice       |
| Late Escape Deal      | ~~43%~~   | 20 déc 2025        | Marge destructrice       |
| Late Escape Deal      | ~~42%~~   | 20 déc 2025        | Marge destructrice       |
| Tarif géociblé Europe | ~~10%~~   | 20 déc 2025        | Risque cumul (surévalué) |
| Tarif géociblé Maroc  | ~~10%~~   | 20 déc 2025        | Risque cumul (surévalué) |

### Promotions Modifiées (2 total)

| Promotion             | Avant | Après   | Date        |
| --------------------- | ----- | ------- | ----------- |
| Basic Deal (3 nuits)  | 33%   | **15%** | 20 déc 2025 |
| Basic Deal (standard) | 30%   | **10%** | 20 déc 2025 |

---

## Analyse d'Impact ROI

### Scénario : Chambre à 200€ (Double Room Superior)

| Scénario         | Prix affiché | Après promo | Commission 25% | Net Villa | Marge visée | Écart      |
| ---------------- | ------------ | ----------- | -------------- | --------- | ----------- | ---------- |
| Sans promo       | 200€         | 200€        | -50€           | **150€**  | 120€        | +30€       |
| Basic Deal 30%   | 200€         | 140€        | -35€           | **105€**  | 120€        | **-15€**   |
| Basic Deal 38%   | 200€         | 124€        | -31€           | **93€**   | 120€        | **-27€**   |
| Early Booker 40% | 200€         | 120€        | -30€           | **90€**   | 120€        | **-30€**   |
| Late Escape 43%  | 200€         | 114€        | -28.5€         | **85.5€** | 120€        | **-34.5€** |

### ~~Cumul potentiel (pire cas)~~ — CORRIGÉ

> ⚠️ **CORRECTION** : Booking.com **NE PERMET PAS** le cumul des promotions.
> Seul le discount le plus élevé s'applique. Le calcul ci-dessous était incorrect.

~~Si Early Booker (40%) + Tarif géociblé (10%) = ~46% de réduction~~

**Réalité** : Avec Early Booker 40%, le client aurait eu **40% uniquement** (pas 46%).

### Impact Actuel (après corrections)

| Scénario       | Prix affiché | Après promo (max 15%) | Commission 25% | Net Villa   | Marge visée | Écart         |
| -------------- | ------------ | --------------------- | -------------- | ----------- | ----------- | ------------- |
| Sans promo     | 200€         | 200€                  | -50€           | **150€**    | 120€        | +30€          |
| Basic Deal 15% | 200€         | 170€                  | -42.50€        | **127.50€** | 120€        | **+7.50€** ✅ |
| Basic Deal 10% | 200€         | 180€                  | -45€           | **135€**    | 120€        | **+15€** ✅   |

**Toutes les promotions actuelles sont dans le range optimal (10-15%).**

---

## Plan d'Action — ✅ EXÉCUTÉ

### Actions Exécutées (20 déc 2025)

| Promo                   | Action           | Priorité | Statut  |
| ----------------------- | ---------------- | -------- | ------- |
| Early Booker Deal 40%   | **DÉSACTIVÉ**    | P0       | ✅ Fait |
| Basic Deal 38%          | **DÉSACTIVÉ**    | P0       | ✅ Fait |
| Late Escape 43%         | **DÉSACTIVÉ**    | P0       | ✅ Fait |
| Late Escape 42%         | **DÉSACTIVÉ**    | P0       | ✅ Fait |
| Tarifs géociblés Europe | **DÉSACTIVÉ**    | P0       | ✅ Fait |
| Tarifs géociblés Maroc  | **DÉSACTIVÉ**    | P0       | ✅ Fait |
| Basic Deal 33%          | **RÉDUIT à 15%** | P1       | ✅ Fait |
| Basic Deal 30%          | **RÉDUIT à 10%** | P1       | ✅ Fait |

### Nouvelle Stratégie Promos (après nettoyage)

| Type             | Réduction max | Conditions      |
| ---------------- | ------------- | --------------- |
| Early Booker     | **15%** max   | 60+ jours avant |
| Last Minute      | **10%** max   | 3 jours avant   |
| Long séjour      | **10%**       | 7+ nuits        |
| Tarifs géociblés | **AUCUN**     | Désactivés      |

---

## Prochaines Étapes

| Étape | Action                                           | Statut      |
| ----- | ------------------------------------------------ | ----------- |
| 1     | ~~Validation M. Said~~                           | ✅ FAIT     |
| 2     | ~~Désactiver promos sur Booking.com Extranet~~   | ✅ FAIT     |
| 3     | Configurer prix sur HotelRunner                  | ⏳ En cours |
| 4     | Vérifier synchronisation                         | ⏳ Après 3  |
| 5     | Monitoring impact réservations                   | ⏳ J+7      |
| 6     | **Audit V2** — Identifier promos non documentées | ✅ FAIT     |

---

## Décisions Validées par M. Said (20 déc 2025)

### Q1 : Désactivation promos destructrices

**Décision** : ✅ **OUI — VALIDÉ**

- [x] Early Booker Deal 40% → **DÉSACTIVER**
- [x] Basic Deal 38% → **DÉSACTIVER**
- [x] Late Escape Deal 43% et 42% → **DÉSACTIVER**

### Q2 : Tarifs géociblés

**Décision** : ✅ **DÉSACTIVER COMPLÈTEMENT**

- [x] Désactiver complètement les tarifs géociblés (Europe & Maroc)

### Q3 : Stratégie promos restantes

**Décision** : ✅ **APPLIQUER LES RECOMMANDATIONS**

- Basic Deal 33% → Réduire à **15%** max
- Basic Deal 30% → Réduire à **10%** max

### Q4 : Prix premium (chambres 7 et 12)

**Décision** : ✅ **OUI — POSITIONNEMENT PREMIUM CONFIRMÉ**

- Chambre 7 (Deluxe King Suite) : **440€** ✅
- Chambre 12 (Presidential Suite) : **600€** ✅

### Q5 : Prochaine action

**Décision** : ✅ **LES DEUX EN PARALLÈLE**

1. Désactiver les promos destructrices sur Booking.com
2. Configurer les prix sur HotelRunner

---

## Historique des Modifications

| Date               | Action                                              | Auteur      |
| ------------------ | --------------------------------------------------- | ----------- |
| 20 déc 2025        | Audit initial (8 promos)                            | Claude Code |
| 20 déc 2025        | Validation M. Said                                  | M. Thaifa   |
| 20 déc 2025        | Exécution (6 désactivées, 2 réduites)               | Claude Code |
| 20 déc 2025, 21h30 | **Audit V2** — 3 promos non documentées identifiées | Claude Code |

---

_Audit réalisé le 20 décembre 2025_
_Mise à jour V2 : 20 décembre 2025, 21h30_
_Source : Booking.com Extranet - admin.booking.com_
_**Validé par M. Said Thaifa le 20 décembre 2025**_

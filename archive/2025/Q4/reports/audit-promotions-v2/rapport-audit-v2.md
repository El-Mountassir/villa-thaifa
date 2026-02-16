# Audit V2 — Promotions Booking.com Villa Thaifa

**Date** : 20 décembre 2025, 21h45
**Hotel ID** : 5446847
**Déclencheur** : Omar a identifié des promotions non documentées

> **Source de vérité** : [state/current/promotions.md](../../../../../state/current/promotions.md)
> Les données d'état ci-dessous sont archivées. Consulter le lien pour l'état actuel.

---

## Résumé Exécutif

| Métrique                               | Valeur |
| -------------------------------------- | ------ |
| Promotions actives (actuelles)         | **5**  |
| Promotions documentées (audit initial) | 2      |
| Promotions non documentées             | **3**  |
| Actions correctives requises           | **0**  |

**Verdict** : Toutes les promotions sont dans le range optimal (10-15%). Aucune action corrective nécessaire.

---

## État Actuel des Promotions

### Promotions Actives (5 total)

| #   | Promotion                    | Réduction | Période                    | Performance      | Status               |
| --- | ---------------------------- | --------- | -------------------------- | ---------------- | -------------------- |
| 1   | **Basic Deal**               | 10%       | 8 déc 2025 → 30 nov 2026   | --               | ✅ Documenté         |
| 2   | **Basic Deal (3 nuits min)** | 15%       | 8 déc 2025 → 30 nov 2026   | 1 résa, €118.50  | ✅ Documenté         |
| 3   | **Early Booker Deal**        | 10%       | 20 déc 2025 → 30 nov 2026  | --               | ⚠️ **NOUVEAU**       |
| 4   | **Tarif Mobiles**            | 10%       | 22 sept 2025 → Aujourd'hui | 27 résa, €15,614 | ⚠️ **NON DOCUMENTÉ** |
| 5   | **À l'étranger (géociblé)**  | 10%       | 8 déc 2025 → Aujourd'hui   | 2 résa, €160     | ⚠️ **NON DOCUMENTÉ** |

---

## Analyse des Promotions Non Documentées

### 1. Early Booker Deal 10%

| Attribut          | Valeur                  | Standard                 | Verdict     |
| ----------------- | ----------------------- | ------------------------ | ----------- |
| Discount          | 10%                     | 10-25% optimal           | ✅ Conforme |
| Commission impact | 67.5% retained          | Min 60% acceptable       | ✅ OK       |
| Condition         | +30 jours avant arrivée | Normal pour Early Booker | ✅ OK       |

**Origine** : Nouvelle promo créée après désactivation du Early Booker 40%.

**Recommandation** : ✅ **Conserver** — Dans le range optimal.

---

### 2. Tarif Mobiles 10%

| Attribut     | Valeur  | Standard       | Verdict                |
| ------------ | ------- | -------------- | ---------------------- |
| Discount     | 10%     | 10-25% optimal | ✅ Conforme            |
| Réservations | 27      | N/A            | Très performant        |
| Revenus      | €15,614 | N/A            | Excellent ROI          |
| Nuitées      | 122     | N/A            | 4.5 nuits/résa moyenne |

**Origine** : Promo existante depuis septembre 2025, jamais documentée.

**Recommandation** : ✅ **Conserver** — Génère des revenus significatifs.

---

### 3. À l'étranger (tarif géociblé) 10%

| Attribut     | Valeur  | Standard       | Verdict     |
| ------------ | ------- | -------------- | ----------- |
| Discount     | 10%     | 10-25% optimal | ✅ Conforme |
| Réservations | 2       | N/A            | Modéré      |
| Revenus      | €160.16 | N/A            | OK          |

**Note** : Initialement documenté comme "Royaume-Uni (tarif géociblé)" — possible confusion de nom.

**Recommandation** : ✅ **Conserver** — Diversification géographique.

---

## Comparaison Avant/Après

### Audit Initial vs Audit V2

| Métrique                   | Audit Initial | Audit V2                   |
| -------------------------- | ------------- | -------------------------- |
| Promotions actives         | 8             | 5                          |
| Promotions documentées     | 8             | 5                          |
| Réduction maximale         | 43%           | **15%** ✅                 |
| Promotions destructrices   | 6             | **0** ✅                   |
| Promotions non documentées | 0             | 3 (maintenant documentées) |

### Actions Exécutées (entre audits)

| Action                    | Quantité             |
| ------------------------- | -------------------- |
| Promotions désactivées    | 6                    |
| Promotions réduites       | 2                    |
| Nouvelles promos ajoutées | 1 (Early Booker 10%) |

---

## Clarifications Obtenues

### Gap 1 : Définition de "Marge"

**Question** : La marge 120-450€ représente revenue net ou profit net?

**Réponse Omar** : **Revenue net** (après commission, pas profit après tous les coûts).

**Impact** : Les calculs sont corrects. "Marge négative" = "revenue insuffisant pour couvrir l'objectif", pas nécessairement perte financière.

### Gap 2 : Stacking des Promotions

**Claim initial** : "Les promotions cumulent (40% + 10% = 50%)"

**Réalité** : Booking.com **NE PERMET PAS** le cumul. Seul le discount le plus élevé s'applique.

**Impact** : Le risque de cumul était surévalué, mais les promotions individuelles 40%+ restaient destructrices.

---

## Conclusion

### État des Promotions : ✅ SAIN

Toutes les 5 promotions actives sont dans le range optimal (10-15%) :

- Aucune promo > 20% (destructrice)
- Impact commission maîtrisé (max 35% perte vs 58% avant)
- Mix varié : catalogue, mobile, géociblé

### Actions Futures

| Action                                  | Priorité | Deadline        |
| --------------------------------------- | -------- | --------------- |
| Monitoring performance post-changement  | P2       | J+7             |
| Analyse impact occupancy                | P3       | Janvier 2025    |
| Considérer promos saisonnières (15-20%) | P4       | Avant juin 2025 |

---

## Fichiers Mis à Jour

| Fichier                       | Modifications                     |
| ----------------------------- | --------------------------------- |
| `audit-promotions-booking.md` | État actuel, corrections stacking |
| `execution-log-booking.md`    | Session audit V2, 5 promos        |
| `verification.../final.md`    | État promotions, gaps résolus     |
| `tasks/TODOs.md`              | Tâche audit V2 completed          |

---

_Audit V2 réalisé le 20 décembre 2025, 21h45_
_Source : Booking.com Extranet - admin.booking.com_
_Exécuté par Claude Code_

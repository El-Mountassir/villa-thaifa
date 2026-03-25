# Baseline — Promotions Booking.com (20 dec 2025)

**Date du snapshot**: 2025-12-20 ~17:00 (avant execution)
**ID Hotel**: 5446847
**Source**: Booking.com Extranet

---

## Contexte

Ce snapshot capture l'etat des promotions **AVANT** l'execution du plan de nettoyage.
Les promotions listees ci-dessous ont ete identifiees comme problematiques.

---

## Etat des promotions (8 au total)

| #   | Promotion            | Remise  | Periode de sejour        | Performance                      | Action prevue         |
| --- | -------------------- | ------- | ------------------------ | -------------------------------- | --------------------- |
| 1   | Basic Deal           | 30%     | 8 dec 2025 → 30 nov 2026 | --                               | P1: Reduire a **10%** |
| 2   | Basic Deal           | 33%     | 8 dec 2025 → 30 nov 2026 | 1 reservation, 10 nuits, 118,50€ | P1: Reduire a **15%** |
| 3   | Basic Deal           | **38%** | 8 dec 2025 → 30 nov 2026 | 3 reservations, 9 nuits, 102,92€ | P0: **DESACTIVER**    |
| 4   | Geo-targeted Europe  | **10%** | Toujours active          | --                               | P0: **DESACTIVER**    |
| 5   | Geo-targeted Morocco | **10%** | Toujours active          | --                               | P0: **DESACTIVER**    |
| 6   | Early Booker Deal    | **40%** | 8 dec 2025 → 30 nov 2026 | --                               | P0: **DESACTIVER**    |
| 7   | Late Escape Deal     | **43%** | 1 oct 2025 → 7 jan 2026  | --                               | P0: **DESACTIVER**    |
| 8   | Late Escape Deal     | **42%** | 1 oct 2025 → 7 jan 2026  | --                               | P0: **DESACTIVER**    |

---

## Analyse d'impact (avant correction)

| Metrique           | Valeur   | Probleme            |
| ------------------ | -------- | ------------------- |
| Promotions actives | **8**    | Trop nombreuses     |
| Remise maximale    | **43%**  | Destructrice        |
| Promotions > 30%   | **5**    | Marges negatives    |
| Impact combine max | **~58%** | Commission + remise |

---

## Impact ROI (Exemple: chambre a 200€)

| Scenario         | Prix client | Commission 25% | Net Villa | vs Cible 120€ |
| ---------------- | ----------- | -------------- | --------- | ------------- |
| Sans promo       | 200€        | -50€           | **150€**  | +30€ ✅       |
| Basic Deal 38%   | 124€        | -31€           | **93€**   | **-27€** ❌   |
| Early Booker 40% | 120€        | -30€           | **90€**   | **-30€** ❌   |
| Late Escape 43%  | 114€        | -28,5€         | **85,5€** | **-34,5€** ❌ |

---

## Note

> Ce snapshot est une reference historique.
> L'etat actuel est dans [../current/promotions.md](../current/promotions.md).
> Les modifications effectuees sont dans [../execution/2025-12-20/promotions.md](../execution/2025-12-20/promotions.md).

---

_Snapshot baseline cree le 2025-12-20_
_Fichier immuable — ne pas modifier_

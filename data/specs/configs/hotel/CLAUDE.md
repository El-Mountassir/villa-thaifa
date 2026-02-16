# Configuration Hôtel — CLAUDE.md

> **Domaine** : Configuration des chambres et propriétés de Villa Thaifa
> **Contexte parent** : `../../../CLAUDE.md` (hérite de toutes les règles du projet)

---

## Ce Répertoire

| Fichier    | Objectif                                  |
| ---------- | ----------------------------------------- |
| `rooms.md` | Inventaire, tarification, capacités       |

**Note** : Les autres données hôtelières ont été déplacées vers `../../state/` selon le standard de gestion d'état :

- Réservations actuelles → [`../../state/current/reservations.md`](../../state/current/reservations.md)
- Tarification prévue → [`../../state/planned/pricing.md`](../../state/planned/pricing.md)

---

## Règles Clés

| Règle                  | Description                                             |
| ---------------------- | ------------------------------------------------------- |
| **SSOT**               | Ceci est la Source Unique de Vérité pour les données hôtel |
| **Pas de calcul**      | Toujours utiliser les valeurs exactes de la plateforme  |
| **Sauvegarde d'abord** | Avant modification, créer une sauvegarde dans `archive/` |

---

## Intégrité des Données

Avant de modifier tout fichier dans ce répertoire :

1. **Vérifier la source** — Les données viennent-elles de HotelRunner ou Booking.com ?
2. **Créer une baseline** — `cp fichier.md archive/YYYY/QQ/snapshots/fichier-YYYY-MM-DD.md`
3. **Valider après** — Vérification croisée avec la plateforme

---

_*Contexte hiérarchique pour data/specs/configs/hotel/*_

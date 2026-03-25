# Etat Actuel

> **Instantanes operationnels en direct mis a jour selon l'evolution de l'etat.**

---

## Objectif

Ce repertoire contient l'etat actuel et en direct des operations de Villa Thaifa. Les fichiers ici sont mis a jour frequemment (souvent quotidiennement) selon l'evolution de la situation operationnelle.

---

## Fichiers

| Fichier           | Frequence de mise a jour | Objectif                                     |
| ----------------- | ------------------------ | -------------------------------------------- |
| `reservations.md` | Quotidienne              | Reservations actuelles, assignations, occupation |

---

## Protocole de Mise a Jour

Lors de la mise a jour des fichiers dans ce repertoire :

1. **Verifier la source** — Confirmer que les donnees proviennent de HotelRunner ou Booking.com
2. **Mettre a jour l'horodatage** — Definir "Derniere mise a jour" a la date actuelle
3. **Reference croisee** — Lier aux journaux d'execution si ceci est le resultat d'une action
4. **Commit** — Utiliser un message de commit descriptif expliquant ce qui a change

---

## Associes

- **Configuration** → [`../../configs/hotel/rooms.md`](../../configs/hotel/rooms.md)
- **Changements planifies** → [`../planned/`](../planned/)
- **Journaux d'execution** → [`../execution/`](../execution/)

---

_Standard : `shared/standards/state-management.md`_

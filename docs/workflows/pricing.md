# Workflow : Mise à Jour Tarifs

> Process pour modifier les prix sur HotelRunner/Booking.com.

---

## Prérequis

- [ ] Lire `data/specs/hotel/rooms.md` (tarifs actuels)
- [ ] Lire `data/specs/promotions/planned.md` (changements prévus)
- [ ] Validation Omar sur les nouveaux tarifs

---

## Étapes

### 1. BASELINE — Capturer état actuel

```bash
cp data/specs/hotel/rooms.md archive/YYYY/QQ/snapshots/rooms-YYYY-MM-DD.md
```

### 2. PLAN — Documenter les changements

```
Mettre à jour data/specs/promotions/planned.md :
- Ancien tarif
- Nouveau tarif
- Raison du changement
- Date d'effet
```

### 3. CONFIRM — Validation Omar

```
Présenter tableau comparatif :
| Chambre | Ancien | Nouveau | Delta |
Attendre validation explicite
```

### 4. EXECUTE — Appliquer sur HotelRunner

```
1. Ouvrir app.hotelrunner.com
2. Navigation : Rates → Room Rates
3. Modifier les tarifs
4. Vérifier propagation vers OTAs
```

### 5. VERIFY — Confirmer sur Booking.com

```
1. Ouvrir admin.booking.com
2. Vérifier que les tarifs sont synchronisés
3. Screenshot de confirmation
```

### 6. UPDATE DATA

```
1. Mettre à jour data/specs/hotel/rooms.md
2. Log dans archive/YYYY/QQ/execution/pricing.md
3. Ajouter entrée dans archive/YYYY/QQ/changelogs/pricing.md
```

---

## Points d'attention

| Risque                     | Mitigation                                  |
| -------------------------- | ------------------------------------------- |
| Désync HotelRunner/Booking | Vérifier propagation après 15 min           |
| Erreur de saisie           | Double-check avant validation               |
| Promotions en conflit      | Vérifier `data/specs/promotions/current.md` |

---

_Workflow v0.1.0-alpha.0_

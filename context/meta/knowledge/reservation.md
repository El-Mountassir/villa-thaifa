# Workflow : Création Réservation

> Process complet pour créer une réservation sur HotelRunner.

---

## Prérequis

- [ ] Lire `docs/lessons-learned.md`
- [ ] Lire `rules/universal/platform-operations.md`
- [ ] Avoir accès Admin Omar (pas compte client)

---

## Étapes

### 1. PARSE — Comprendre la demande

```
Extraire :
- Dates (check-in / check-out)
- Chambre (numéro ou type)
- Nom invité
- Nombre adultes/enfants
- Source (direct, Booking, etc.)
```

### 2. VERIFY — Vérifier contre data/specs/

```
Consulter :
- data/specs/hotel/rooms.md → mapping chambre
- data/specs/hotel/reservations.md → conflits potentiels
```

### 3. REPEAT BACK — Confirmer avec Omar

```
Format :
"Je vais créer : Chambre [X], du [DD/MM] au [DD/MM], nom: [Y], prix: [Z MAD]"
Attendre "oui" ou correction
```

### 4. EXECUTE — Créer sur HotelRunner

```
1. Ouvrir app.hotelrunner.com
2. Navigation : Reservations → New
3. Remplir formulaire avec valeurs EXACTES
4. Screenshot avant soumission
5. Soumettre
```

### 5. CONFIRM — Vérifier succès

```
1. Vérifier confirmation HotelRunner
2. Mettre à jour data/specs/hotel/reservations.md
3. Log dans archive/YYYY/QQ/execution/
```

---

## Checkpoints

| Étape         | Validation requise                  |
| ------------- | ----------------------------------- |
| Après PARSE   | Confiance > 90% sur tous les champs |
| Après VERIFY  | Pas de conflit chambre              |
| Après REPEAT  | Omar a confirmé "oui"               |
| Après EXECUTE | Confirmation HotelRunner reçue      |

---

## En cas d'erreur

1. **NE PAS paniquer**
2. Screenshot l'erreur
3. Escalader à Omar avec contexte
4. Documenter dans `docs/lessons-learned.md`

---

_Workflow v0.1.0-alpha.0_

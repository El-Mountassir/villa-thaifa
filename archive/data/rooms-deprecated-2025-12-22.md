# État Actuel — Chambres & Tarification

> ⚠️ **DÉPRÉCIÉ** : Ce fichier est remplacé par la structure room-centric.
> Voir [`rooms/`](rooms/) pour les fiches individuelles par chambre.
> Voir [`README.md`](README.md) pour l'index complet.
>
> *Conservé pour référence historique. Ne pas modifier.*

**Dernière mise à jour** : 2025-12-22 (gelé)
**Source** : HotelRunner (app.hotelrunner.com) + Booking.com
**Commission Booking.com** : 25%

---

## Résumé

| Métrique                     | Valeur                              |
| ---------------------------- | ----------------------------------- |
| Total chambres               | **12**                              |
| Types de chambres (HotelRunner) | **9**                            |
| Types de chambres (Booking.com) | **8**                            |
| Prix configurés              | **0** (tous en attente)             |
| Formule de tarification      | `Prix Booking = Marge nette / 0,75` |

---

## Types de Chambres Booking.com & Configuration des Lits

| Type de Chambre      | Chambres | Lits                   | Capacité Max |
| -------------------- | -------- | ---------------------- | ------------ |
| Superior Double Room | 4, 5     | 1 lit king             | 2            |
| Deluxe Double Room   | 2        | 1 lit king             | 2            |
| Deluxe Triple Room   | 1, 3, 8  | 1 king + 1 canapé-lit  | 3            |
| Executive Suite      | 6        | 1 king + 1 canapé-lit  | 3            |
| Suite                | 10       | 1 king + 1 canapé-lit  | 3            |
| Deluxe King Suite    | 7        | 1 king + 2 canapés-lit | 4            |
| Family Suite         | 9, 11    | 1 king + 2 canapés-lit | 4            |
| Presidential Suite   | 12       | 1 king + 2 canapés-lit | 4            |

---

## Correspondance Chambre ↔ Type HotelRunner

| Chambre | Type HotelRunner     | Marge Nette Cible | Prix Booking (calculé) | Marché Palmeraie |
| ------- | -------------------- | ----------------- | ---------------------- | ---------------- |
| 4, 5    | Double Room Superior | **120€**          | **160€**               | ✅ €130-180      |
| 1, 3, 8 | Deluxe Triple Room   | **150€**          | **200€**               | ✅ €180-220      |
| 2       | Deluxe Double Room   | **150€**          | **200€**               | ✅ €130-180      |
| 6       | Executive Suite      | **180€**          | **240€**               | ✅ €200-280      |
| 7       | Deluxe King Suite    | **330€**          | **440€**               | ⚠️ Premium       |
| 9       | Family Suite         | **170€**          | **227€**               | ✅ €200-280      |
| 10      | Suite                | **200€**          | **267€**               | ✅ €180-250      |
| 11      | Family Suite         | **180€**          | **240€**               | ✅ €200-280      |
| 12      | Presidential Suite   | **450€**          | **600€**               | ⚠️ Très premium  |

## Correspondance Chambre ↔ Type HotelRunner - Retarification en cours

| Chambre | Type HotelRunner     | Marge Nette Cible | Prix Booking (calculé) | Marché Palmeraie |
| ------- | -------------------- | ----------------- | ---------------------- | ---------------- |
| 4       | Double Room Superior | **120€**          | **160€**               | ✅ €130-180      |
| 5       | Double Room Superior | **120€**          | **160€**               | ✅ €130-180      |
| 1       | Deluxe Triple Room   | **150€**          | **200€**               | ✅ €180-220      |
| 3       | Deluxe Triple Room   | **150€**          | **200€**               | ✅ €180-220      |
| 8       | Deluxe Triple Room   | **150€**          | **200€**               | ✅ €180-220      |
| 2       | Deluxe Double Room   | **150€**          | **200€**               | ✅ €130-180      |
| 6       | Executive Suite      | **180€**          | **240€**               | ✅ €200-280      |
| 7       | Deluxe King Suite    | **330€**          | **440€**               | ⚠️ Premium       |
| 9       | Family Suite         | **170€**          | **227€**               | ✅ €200-280      |
| 10      | Suite                | **200€**          | **267€**               | ✅ €180-250      |
| 11      | Family Suite         | **180€**          | **240€**               | ✅ €200-280      |
| 12      | Presidential Suite   | **450€**          | **600€**               | ⚠️ Très premium  |

---

## Configuration HotelRunner

### Interface

- **Navigation** : Calendrier → Mises à jour simples
- **Canal** : Booking.com
- **Plateforme** : app.hotelrunner.com

### Statut par Type

| Type                 | Chambres | Prix configuré | Statut               |
| -------------------- | -------- | -------------- | -------------------- |
| Double Room Superior | 4, 5     | ❌ Non         | ⏳ En attente        |
| Deluxe Triple Room   | 1, 3, 8  | ❌ Non         | ⏳ En attente        |
| Deluxe Double Room   | 2        | ❌ Non         | ⏳ En attente        |
| Executive Suite      | 6        | ❌ Non         | ⏳ En attente        |
| Deluxe King Suite    | 7        | ❌ Non         | ⏳ En attente (premium) |
| Family Suite         | 9, 11    | ❌ Non         | ⏳ En attente        |
| Suite                | 10       | ❌ Non         | ⏳ En attente        |
| Presidential Suite   | 12       | ❌ Non         | ⏳ En attente (premium) |

---

## Formule de Tarification

```
Prix Booking = Marge Nette Cible / (1 - Commission%)
Prix Booking = Marge Nette Cible / 0,75
```

**Exemple** (Double Room Superior, marge 120€) :

```
Prix Booking = 120€ / 0,75 = 160€
Vérification : 160€ × 0,75 = 120€ net ✅
```

---

## Décisions Premium en Attente

| Chambre | Type               | Prix calculé | Décision Omar |
| ------- | ------------------ | ------------ | ------------- |
| 7       | Deluxe King Suite  | **440€**     | ⏳ En attente |
| 12      | Presidential Suite | **600€**     | ⏳ En attente |

→ Ces prix sont au-dessus du marché Palmeraie. Positionnement premium confirmé ?

---

## Note

> La commission de 25% de Booking.com est élevée (standard = 15%).
> À négocier à moyen terme (levier : volume + bonnes évaluations).

---

_Source de vérité pour l'état des chambres et tarification_
_Mis à jour le 2025-12-20_

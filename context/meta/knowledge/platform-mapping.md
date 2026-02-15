# Mapping Chambres → Types Plateformes — Villa Thaifa

**Dernière mise à jour** : 2025-12-28
**Objectif** : Mapping explicite entre chambres physiques et types plateformes (HotelRunner/Booking.com)

---

## Contexte

Villa Thaifa possède **12 chambres physiques** mais les plateformes (HotelRunner, Booking.com) gèrent par **type de chambre**.

### Limitation Plateforme

| Fonctionnalité | HotelRunner Free | Avec PMS Payant |
| -------------- | ---------------- | --------------- |
| Stop sell      | Par TYPE         | Par chambre     |
| Disponibilité  | Par TYPE         | Par chambre     |
| Tarification   | Par TYPE         | Par chambre     |

---

## Mapping Chambre → Type

| Chambre | Type Plateforme      | Prix (EUR)    | Capacité |
| ------- | -------------------- | ------------- | -------- |
| 1       | Deluxe Triple Room   | 200           | 3        |
| 2       | Deluxe Double Room   | 200           | 2        |
| 3       | Deluxe Triple Room   | 200           | 3        |
| 4       | Double Room Superior | 160           | 2        |
| 5       | Double Room Superior | 160           | 2        |
| 6       | Executive Suite      | 240           | 2        |
| 7       | Deluxe King Suite    | [À confirmer] | 2        |
| 8       | Deluxe Triple Room   | 200           | 3        |
| 9       | Family Suite         | 227           | 4        |
| 10      | Suite                | 267           | 2        |
| 11      | Family Suite         | 240           | 4        |
| 12      | Presidential Suite   | [À confirmer] | 2        |

---

## Types par Groupe

### Chambres Qui Partagent le Même Type

| Type                     | Chambres | Conséquence             |
| ------------------------ | -------- | ----------------------- |
| **Deluxe Triple Room**   | 1, 3, 8  | Stop sell affecte les 3 |
| **Double Room Superior** | 4, 5     | Stop sell affecte les 2 |
| **Family Suite**         | 9, 11    | Stop sell affecte les 2 |

### Types Uniques (1 chambre = 1 type)

| Type               | Chambre |
| ------------------ | ------- |
| Deluxe Double Room | 2       |
| Executive Suite    | 6       |
| Deluxe King Suite  | 7       |
| Suite              | 10      |
| Presidential Suite | 12      |

---

## Implications Opérationnelles

### Stop Sell par Type

Si Said demande de "fermer la Chambre 4":

- HotelRunner bloquera le TYPE "Double Room Superior"
- Cela affecte AUSSI la Chambre 5

### Solution Alternative

Pour bloquer une seule chambre sans affecter les autres du même type:

- Créer une "réservation interne" (fictive) pour cette chambre
- Ou vérifier si l'autre chambre du type est déjà occupée

---

_Source de vérité pour le mapping chambres/plateformes_

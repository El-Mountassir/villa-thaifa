# Channel Mapping — HotelRunner ↔ Booking.com

**Derniere mise a jour** : 2025-12-29
**Source** : Investigation sync (Chrome browser)

---

## Statut Connexion

| Parametre        | Valeur                    |
| ---------------- | ------------------------- |
| **Channel**      | Booking.com               |
| **Type**         | Two-Way XML               |
| **Statut**       | Actif                     |
| **Last Sync**    | 2025-12-29 02:29          |
| **Hotel ID BC**  | 5446847                   |

---

## Room Type Mapping

| # | Room Type HotelRunner    | Room Type Booking.com             | Room ID BC  | Units | Sync |
|---|--------------------------|-----------------------------------|-------------|-------|------|
| 1 | Double Room Superior     | Chambre Double Superieur 4 ; 5    | 544684730   | 2     | XML  |
| 2 | Executive Suite          | Suite Executive 6                 | 544684732   | 1     | XML  |
| 3 | Deluxe King Suite        | Suite De Luxe King Size 7         | 544684733   | 1     | XML  |
| 4 | Family Suite             | Suite Familiale 8 ; 11            | 544684736   | 2     | XML  |
| 5 | Deluxe Triple Room       | Chambre Triple Deluxe 1 ; 3 ; 8   | ?           | 3     | XML  |
| 6 | Deluxe Double Room       | Chambre Double Deluxe 2           | ?           | 1     | XML  |
| 7 | Suite                    | Suite 10                          | ?           | 1     | XML  |
| 8 | Presidential Suite       | Suite Presidentielle 12           | ?           | 1     | XML  |

**Legende** :
- Room ID BC = Booking.com Room ID
- Units = Nombre de chambres physiques dans ce type
- Sync = Type de synchronisation

---

## Parametres Mapping (Reglages Avances)

Verifies le 2025-12-29 pour chaque room type :

| Parametre           | Valeur   | Signification                        |
| ------------------- | -------- | ------------------------------------ |
| Lecture seulement   | Non      | Updates autorises vers Booking.com   |
| Stop sell           | Non      | Ventes ouvertes                      |
| Envoyer le prix     | Oui      | Prix synces vers Booking.com         |

---

## Chambres Physiques → Room Types

| Chambre | Room Type HotelRunner    | Pool Booking.com               |
| ------- | ------------------------ | ------------------------------ |
| 01      | Deluxe Triple Room       | Chambre Triple Deluxe 1 ; 3 ; 8|
| 02      | Deluxe Double Room       | Chambre Double Deluxe 2        |
| 03      | Deluxe Triple Room       | Chambre Triple Deluxe 1 ; 3 ; 8|
| 04      | Double Room Superior     | Chambre Double Superieur 4 ; 5 |
| 05      | Double Room Superior     | Chambre Double Superieur 4 ; 5 |
| 06      | Executive Suite          | Suite Executive 6              |
| 07      | Deluxe King Suite        | Suite De Luxe King Size 7      |
| 08      | Deluxe Triple Room       | Chambre Triple Deluxe 1 ; 3 ; 8|
| 09      | Family Suite             | Suite Familiale 8 ; 11         |
| 10      | Suite                    | Suite 10                       |
| 11      | Family Suite             | Suite Familiale 8 ; 11         |
| 12      | Presidential Suite       | Suite Presidentielle 12        |

---

## Probleme Identifie (2025-12-29)

### Symptome

Les reservations creees manuellement sur HotelRunner (source "Online") ne reduisent pas la disponibilite sur Booking.com.

### Evidence

| Date       | Reservation HR | Dispo attendue BC | Dispo reelle BC |
| ---------- | -------------- | ----------------- | --------------- |
| Dec 31     | Room 4 (Gouram) + Room 5 (Benchekroune) | 0 | 1 |
| Jan 1      | Room 4 + Room 5 | 0 | 2 |
| Jan 2      | Room 4 seul    | 1 | 2 |

### Hypothese

La connexion Two-Way est configuree pour :
- ✓ Recevoir les reservations Booking.com
- ✗ Envoyer les updates d'inventaire pour reservations internes

### Actions

Voir rapport complet : [`docs/reports/2025-12-29-sync-investigation.md`](../../../docs/reports/2025-12-29-sync-investigation.md)

---

## Logs Sync

| Date       | Succes | Echecs | Notes                              |
| ---------- | ------ | ------ | ---------------------------------- |
| 2025-12-29 | 3,588  | 0      | 100% succes (mais internes exclus?)|

---

## References

- [API Reference](api-reference.md)
- [Investigation Report](../../../docs/reports/2025-12-29-sync-investigation.md)
- [Room 04 File](../../configs/hotel/facilities/rooms/04-double-superior.md)
- [Room 05 File](../../configs/hotel/facilities/rooms/05-double-superior.md)

---

_Channel Mapping — Villa Thaifa_
_Prepare pour migration DB future_

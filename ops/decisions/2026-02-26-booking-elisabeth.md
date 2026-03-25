# Mission : Réservation Elisabeth Delacarte

**Date de réception** : 26 Février 2026
**Statut** : En attente de clarifications (Questions soumises à Omar)

## Paramètres de la Réservation (Extraits du message de Said)

- **Client** : Elisabeth Delacarte
- **Check-in** : 23 Avril 2026
- **Check-out** : 27 Avril 2026 (4 nuits)
- **Chambres** :
  - Suite Exécutif (Chambre 6)
  - Suite (Chambre 7)
- **Canal** : Direct (Walk-in / Contact direct)

## Plan d'Exécution Prévu

1. **Scout & Questions** : Obtenir les paramètres manquants auprès d'Omar.
2. **Action (HotelRunner)** : Créer la nouvelle réservation via le mode navigateur. Ajouter les deux chambres (Suite Exécutif 6 et Suite 7) sur la même fiche de réservation (ou deux fiches séparées selon les conventions).
3. **Verify** : S'assurer visuellement que les disponibilités sont tombées à 0 pour ces deux suites du 23 au 27 Avril, et que le statut est "Confirmé".
4. **Sync** : Mettre à jour `data/bookings/reservations/reservations.md` pour le mois d'Avril.
5. **Report** : Préparer le brouillon (`Draft`) du message hollandais pour Said dans `ops/status/reports/update/said/README.md`.
6. **Commit** : Enregistrer les modifications dans le dépôt.

## Questions Bloquantes (Pendant la phase Planning)

1. **Prix** : Quel est le tarif total convenu (ou le prix par chambre/nuit) à enregistrer ?
2. **Occupants** : Combien d'adultes et d'enfants devons-nous déclarer par chambre ?
3. **Format HR** : Dois-je regrouper ces deux chambres sous un seul "Booking ID" dans HotelRunner (via le bouton "Ajouter une chambre" dans la même réservation) ou faire deux réservations séparées au nom d'Elisabeth Delacarte ?

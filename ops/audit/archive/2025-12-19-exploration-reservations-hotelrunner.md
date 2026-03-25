# Rapport d'Exploration — Réservations HotelRunner

> **Version** : 1.0 | **Template** : Gold Standard (Hotelogix, Cloudbeds, Smartsheet)
> **Usage** : Rapport opérationnel Villa Thaifa

---

**Date d'exploration** : 2025-12-19 ~23:50
**Plateforme** : HotelRunner (villa-thaifa.hotelrunner.com)
**Explorateur** : Claude Code (Opus 4.5)
**Statut** : 🟢 Complété

---

## 1. Résumé Exécutif

### 1.1 Chiffres Clés

| Métrique                       | Valeur    | Commentaire                  |
| ------------------------------ | --------- | ---------------------------- |
| Réservations totales           | 11        | Confirmées (excl. 1 annulée) |
| **Réservations non assignées** | **10**    | ⚠️ Action requise            |
| Réservations incomplètes       | 0         | -                            |
| Check-ins aujourd'hui (19/12)  | 0         | -                            |
| Check-outs aujourd'hui         | 0         | -                            |
| Chambres occupées              | 0/12      | -                            |
| Taux d'occupation (19/12)      | 0%        | -                            |
| Revenue total prévu            | €8,008.85 | Booking.com                  |
| Paiements reçus                | €0        | Paiement à l'arrivée         |

### 1.2 Alertes Urgentes

| Priorité  | Alerte                                                    | Action Requise                              | Deadline         |
| --------- | --------------------------------------------------------- | ------------------------------------------- | ---------------- |
| 🔴 **P0** | **Arne Cordes arrive DEMAIN (20/12)**                     | Assigner 2 chambres Double Room Superior    | **20 déc 15:00** |
| 🔴 **P0** | **10 réservations sans chambre assignée**                 | Assigner toutes les chambres avant arrivées | Progressif       |
| 🟠 P1     | Nicolas Lamblain arrive 26/12 (2 résas)                   | Assigner chambres                           | 26 déc           |
| 🟠 P1     | Jean Damien Aubril + Quentin Warembourg arrivent 27-29/12 | Assigner chambres                           | 27 déc           |

### 1.3 Résumé en 3 points

1. **10 réservations confirmées n'ont pas de chambre assignée** — Cela inclut des arrivées imminentes (demain!)
2. **Toutes les réservations viennent de Booking.com** — 100% OTA, aucune réservation directe
3. **Occupation prévue monte à 50% pendant les fêtes** (30-31 déc) — Bonne période

---

## 2. Réservations Non Assignées (URGENT)

### 2.1 Vue d'ensemble

| Total Non Assignées | Urgentes (< 48h)    | Cette semaine | Ce mois |
| ------------------- | ------------------- | ------------- | ------- |
| **10**              | **2** (Arne Cordes) | 6             | 10      |

### 2.2 Détail des Réservations Non Assignées

| #   | Confirmation | Nom Invité         | Room Type            | Check-in   | Check-out | Nuits | Total   | Urgence       |
| --- | ------------ | ------------------ | -------------------- | ---------- | --------- | ----- | ------- | ------------- |
| 1   | 6229237084   | **Arne Cordes**    | Double Room Superior | **20 déc** | 25 déc    | 5     | €617.5  | 🔴 **DEMAIN** |
| 2   | 6229237084-1 | **Arne Cordes**    | Double Room Superior | **20 déc** | 25 déc    | 5     | €617.5  | 🔴 **DEMAIN** |
| 3   | 6538291598   | Nicolas Lamblain   | Double Room Superior | 26 déc     | 31 déc    | 5     | €795    | 🟠            |
| 4   | 6538291598-1 | Nicolas Lamblain   | Double Room Superior | 26 déc     | 31 déc    | 5     | €745    | 🟠            |
| 5   | 5352537667   | Jean Damien Aubril | Deluxe Triple Room   | 27 déc     | 4 jan     | 8     | €1,112  | 🟠            |
| 6   | 5352537667-1 | Jean Damien Aubril | Deluxe Triple Room   | 27 déc     | 4 jan     | 8     | €1,112  | 🟠            |
| 7   | 5446634150   | Quentin Warembourg | Suite                | 29 déc     | 5 jan     | 7     | €973    | 🟡            |
| 8   | 6168071595   | Arkadiusz Kurowski | Double Room Superior | 8 jan      | 14 jan    | 6     | €622.8  | 🟢            |
| 9   | 5530370986   | Montañez Nuria     | Double Room Superior | 17 jan     | 19 jan    | 2     | €232.3  | 🟢            |
| 10  | 6827268891   | Montañez Nuria     | Double Room Superior | 14 jan     | 15 jan    | 1     | €116.15 | 🟢            |

### 2.3 Réservations déjà assignées

| Confirmation    | Nom              | Chambre | Type               | Check-in | Check-out |
| --------------- | ---------------- | ------- | ------------------ | -------- | --------- |
| (voir calendar) | Sabrina Lemahieu | 2       | Deluxe Double Room | 27 déc   | 3 jan     |

---

## 3. Calendrier des Arrivées

### 3.1 Prochains 14 jours

| Date       | Jour | Arrivées | Noms                                      | Chambres à assigner            |
| ---------- | ---- | -------- | ----------------------------------------- | ------------------------------ |
| **20 déc** | Sam  | **2**    | Arne Cordes (x2)                          | 2 × Double Room Superior       |
| 21 déc     | Dim  | 0        | -                                         | -                              |
| 22 déc     | Lun  | 0        | -                                         | -                              |
| 23 déc     | Mar  | 0        | -                                         | -                              |
| 24 déc     | Mer  | 0        | -                                         | -                              |
| 25 déc     | Jeu  | 0        | -                                         | -                              |
| **26 déc** | Ven  | **2**    | Nicolas Lamblain (x2)                     | 2 × Double Room Superior       |
| **27 déc** | Sam  | **3**    | Jean Damien Aubril (x2), Sabrina Lemahieu | 2 × Deluxe Triple + 1 assignée |
| 28 déc     | Dim  | 0        | -                                         | -                              |
| **29 déc** | Lun  | **1**    | Quentin Warembourg                        | 1 × Suite                      |
| 30 déc     | Mar  | 0        | -                                         | -                              |
| 31 déc     | Mer  | 0        | -                                         | -                              |
| 1 jan      | Jeu  | 0        | -                                         | -                              |
| 2 jan      | Ven  | 0        | -                                         | -                              |

### 3.2 Taux d'occupation prévu

| Période              | Occupation | Chambres occupées |
| -------------------- | ---------- | ----------------- |
| 19 déc (aujourd'hui) | 0%         | 0/12              |
| 20-25 déc            | 16.7%      | 2/12              |
| 26 déc               | 33.3%      | 4/12              |
| 27-28 déc            | 41.7%      | 5/12              |
| 29 déc               | 50%        | 6/12              |
| 30-31 déc            | 50%        | 6/12              |
| 1-3 jan              | 33.3%      | 4/12              |
| 4 jan                | 8.3%       | 1/12              |

---

## 4. Occupation des Chambres

### 4.1 Statut actuel (19 déc 2025)

| Chambre | Type                 | Statut      | Occupant                  | Notes                              |
| ------- | -------------------- | ----------- | ------------------------- | ---------------------------------- |
| 1       | Deluxe Triple Room   | 🟢 Libre    | -                         | Disponible pour Jean Damien Aubril |
| 2       | Deluxe Double Room   | 🟡 Réservée | Sabrina Lemahieu (27 déc) | Assignée                           |
| 3       | Deluxe Triple Room   | 🟢 Libre    | -                         | Disponible pour Jean Damien Aubril |
| 4       | Double Room Superior | 🟢 Libre    | -                         | Disponible                         |
| 5       | Double Room Superior | 🟢 Libre    | -                         | Disponible                         |
| 6       | Executive Suite      | 🟢 Libre    | -                         | Disponible                         |
| 7       | Deluxe King Suite    | 🟢 Libre    | -                         | Disponible                         |
| 8       | Deluxe Triple Room   | 🟢 Libre    | -                         | Disponible                         |
| 9       | Family Suite         | 🟢 Libre    | -                         | Disponible                         |
| 10      | Suite                | 🟢 Libre    | -                         | Disponible pour Quentin Warembourg |
| 11      | Family Suite         | 🟡 Pending  | Mission chambre 11        | En attente réponse Said            |
| 12      | Presidential Suite   | 🟢 Libre    | -                         | Disponible                         |

### 4.2 Légende

| Code | Signification                         |
| ---- | ------------------------------------- |
| 🟢   | Libre / Disponible                    |
| 🔵   | Occupée                               |
| 🟡   | Réservation pending / assignée future |
| 🔴   | Hors service / Maintenance            |

---

## 5. Analyse

### 5.1 Sources de Réservations

| Source            | Quantité | % Total  | Commission estimée      |
| ----------------- | -------- | -------- | ----------------------- |
| Booking.com       | 11       | **100%** | ~15-18% (~€1,200-1,440) |
| Direct (Site web) | 0        | 0%       | -                       |
| Walk-in           | 0        | 0%       | -                       |
| Autres OTA        | 0        | 0%       | -                       |

**⚠️ Problème** : Dépendance totale à Booking.com = commissions élevées (~€1,200+ sur €8,008)

### 5.2 Patterns Observés

1. **Doublons de réservations** : Plusieurs clients ont 2 réservations (Arne Cordes, Nicolas Lamblain, Jean Damien Aubril) — possiblement 2 chambres par client ou erreur de duplication

2. **Concentration fin d'année** : Pic d'occupation 27 déc - 5 jan (période festive)

3. **Réservations longues** : Moyenne de 5.5 nuits — bon indicateur de fidélisation potentielle

4. **Nationalités diverses** : DE, ES, PL, FR — clientèle internationale

### 5.3 Risques Identifiés

| Risque                                | Probabilité | Impact    | Mitigation                |
| ------------------------------------- | ----------- | --------- | ------------------------- |
| Overbooking si chambres non assignées | Haute       | Critique  | Assigner AVANT arrivées   |
| Confusion doublons                    | Moyenne     | Important | Vérifier avec Booking.com |
| Paiements non reçus (€8,008)          | Basse       | Important | Collecter à l'arrivée     |
| Dépendance Booking.com                | Certaine    | Important | Développer canal direct   |

---

## 6. Actions Recommandées

### 6.1 Actions Immédiates (P0) — AUJOURD'HUI/DEMAIN

| #   | Action                                                     | Responsable | Deadline         | Dépendance                        |
| --- | ---------------------------------------------------------- | ----------- | ---------------- | --------------------------------- |
| 1   | **Assigner 2 chambres Double Room Superior à Arne Cordes** | Said/Omar   | **20 déc 14:00** | -                                 |
| 2   | Vérifier si les doublons sont 2 chambres ou erreur         | Said        | 20 déc           | Contact Booking.com si nécessaire |

### 6.2 Actions Cette Semaine (P1-P2)

| #   | Action                                              | Responsable | Deadline        |
| --- | --------------------------------------------------- | ----------- | --------------- |
| 3   | Assigner chambres Nicolas Lamblain (26 déc)         | Said        | 25 déc          |
| 4   | Assigner chambres Jean Damien Aubril (27 déc)       | Said        | 26 déc          |
| 5   | Assigner chambre Quentin Warembourg (29 déc)        | Said        | 28 déc          |
| 6   | Finaliser réservation chambre 11 (mission en cours) | Omar        | En attente Said |
| 7   | RDV lundi 22 déc 10h avec M. Thaifa                 | Omar        | 22 déc 10:00    |

### 6.3 Backlog (P3-P5)

- [ ] Explorer l'API HotelRunner pour automatisation (P4)
- [ ] Développer stratégie canal direct vs Booking.com (P5)
- [ ] Créer workflow d'assignation automatique des chambres (P4)
- [ ] Investiguer portail Jisr l'Mokawala (P3)

---

## 7. Annexes

### 7.1 Logs de Navigation

```
[~23:30] Connexion HotelRunner (session active)
[~23:32] Room Calendar - Vue occupation décembre/janvier
[~23:35] All Reservations - Liste complète 11 réservations
[~23:38] Incomplete Reservations - Vide (0)
[~23:40] Unassigned Reservations - 10 réservations trouvées
[~23:45] Dashboard Overview - Confirmation 12 chambres vacantes
[~23:50] Création rapport
```

### 7.2 Détails des Confirmations Booking.com

| Guest              | Confirmation #            | Booked Date             |
| ------------------ | ------------------------- | ----------------------- |
| Arne Cordes        | 6229237084 / 6229237084-1 | 19 déc 2025 17:35       |
| Nicolas Lamblain   | 6538291598 / 6538291598-1 | 23 nov 2025 21:04       |
| Jean Damien Aubril | 5352537667 / 5352537667-1 | 5 oct 2025 14:26        |
| Quentin Warembourg | 5446634150                | 8 nov 2025 01:11        |
| Sabrina Lemahieu   | (assignée ch.2)           | 7 déc 2025 16:55        |
| Arkadiusz Kurowski | 6168071595                | 16 déc 2025 20:30       |
| Montañez Nuria     | 5530370986 / 6827268891   | 19 déc 2025 12:08-12:10 |
| Karim Cherkaoui    | (ANNULÉE)                 | 7 déc 2025 10:56        |

### 7.3 Notes Techniques

- **HotelRunner** utilise des sous-numéros de confirmation (-1, -2) pour les réservations multiples d'un même client
- Les réservations apparaissent dans "Unassigned" jusqu'à ce qu'une chambre physique soit attribuée
- Le calendrier montre les réservations assignées en couleur, les non-assignées dans la ligne "Unassigned Reservations"
- Le paiement se fait à l'arrivée pour Booking.com (modèle "pay at property")

---

## 8. Métadonnées

| Champ                   | Valeur                                                             |
| ----------------------- | ------------------------------------------------------------------ |
| **Créé par**            | Claude Code (Opus 4.5)                                             |
| **Date création**       | 2025-12-19 ~23:50                                                  |
| **Dernière MAJ**        | 2025-12-19 ~23:50                                                  |
| **Version**             | 1.0                                                                |
| **Durée exploration**   | ~20 min                                                            |
| **Session HotelRunner** | Active (sans OTP)                                                  |
| **Fichiers liés**       | `projects/2025-12_booking-hotelrunner/report.md`, `tasks/TODOs.md` |

---

## Sources

- **Plateforme** : [HotelRunner](https://villa-thaifa.hotelrunner.com) — Données live
- **Template** :
  - [Hotelogix - 8 Must-Have Hotel PMS Reports](https://blog.hotelogix.com/hotel-reservation-report/)
  - [Cloudbeds - 13 Hotel Audit Reports](https://www.cloudbeds.com/articles/6-reports-your-hotel-should-run-every-night/)
  - [Smartsheet - Hotel Management Templates](https://www.smartsheet.com/content/hotel-management-templates)

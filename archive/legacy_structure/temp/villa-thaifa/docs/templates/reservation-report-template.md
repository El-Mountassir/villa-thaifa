---
title: "Rapport d'Exploration des Réservations"
author: "[Agent IA / Omar]"
date: "YYYY-MM-DD"
lang: fr
---

# Template: Rapport d'Exploration des Réservations

> **Version** : 0.1.0-alpha.0 | **Basé sur** : Hotelogix, Cloudbeds, Smartsheet (triangulation 3 sources)
> **Usage** : Rapports opérationnels Villa Thaifa

---

## Instructions d'utilisation

1. Copier ce template dans `~/Templates/ai/agents/clis/{ai-agent-cli}/output/YYYY/QQ/reports/{description}.md`
2. Remplir chaque section avec les données actuelles
3. Supprimer les sections non applicables
4. Ajouter des sections custom si nécessaire

---

# [TITRE DU RAPPORT]

**Date d'exploration** : YYYY-MM-DD HH:MM
**Plateforme** : HotelRunner
**Explorateur** : [Agent IA / Omar]
**Statut** : 🟢 Complété | 🟡 Partiel | 🔴 Bloqué

---

## 1. Résumé Exécutif

### 1.1 Chiffres Clés

| Métrique                | Valeur | Tendance |
| ----------------------- | ------ | -------- |
| Réservations en attente | X      | ↑↓→      |
| Check-ins aujourd'hui   | X      |          |
| Check-outs aujourd'hui  | X      |          |
| Chambres occupées       | X/12   |          |
| Taux d'occupation       | X%     |          |

### 1.2 Alertes Urgentes

| Priorité | Alerte        | Action Requise | Deadline     |
| -------- | ------------- | -------------- | ------------ |
| 🔴 P0    | [Description] | [Action]       | [Date/Heure] |
| 🟠 P1    | [Description] | [Action]       | [Date]       |

### 1.3 Résumé en 3 points

1. **Point clé 1** : [Découverte majeure]
2. **Point clé 2** : [Découverte majeure]
3. **Point clé 3** : [Découverte majeure]

---

## 2. Réservations en Attente (Pending)

### 2.1 Vue d'ensemble

| Total Pending | Urgentes (< 24h) | Cette semaine | Ce mois |
| ------------- | ---------------- | ------------- | ------- |
| X             | X                | X             | X       |

### 2.2 Détail des Réservations

| #   | Réf.   | Nom Invité | Chambre | Type   | Check-in | Check-out | Nuits | Source       | Montant | Statut   | Action           |
| --- | ------ | ---------- | ------- | ------ | -------- | --------- | ----- | ------------ | ------- | -------- | ---------------- |
| 1   | HR-XXX | [Nom]      | [N°]    | [Type] | DD/MM    | DD/MM     | X     | [OTA/Direct] | XXX MAD | [Status] | [Action requise] |
| 2   |        |            |         |        |          |           |       |              |         |          |                  |

### 2.3 Légende des Statuts

| Statut       | Signification              | Action Type               |
| ------------ | -------------------------- | ------------------------- |
| `PENDING`    | En attente de confirmation | Confirmer ou annuler      |
| `HOLD`       | Bloquée temporairement     | Vérifier délai expiration |
| `WAITLIST`   | Liste d'attente            | Proposer alternative      |
| `INCOMPLETE` | Infos manquantes           | Contacter client          |

---

## 3. Réservations Confirmées (Upcoming)

### 3.1 Arrivées Prévues

| Date  | Réf. | Nom Invité | Chambre | Type | Nuits | Source | Montant | Notes |
| ----- | ---- | ---------- | ------- | ---- | ----- | ------ | ------- | ----- |
| DD/MM |      |            |         |      |       |        |         |       |

### 3.2 Départs Prévus

| Date  | Réf. | Nom Invité | Chambre | Balance Due | Notes |
| ----- | ---- | ---------- | ------- | ----------- | ----- |
| DD/MM |      |            |         |             |       |

---

## 4. Occupation des Chambres

### 4.1 Statut par Chambre

| Chambre | Type                 | Statut     | Occupant           | Check-out | Notes |
| ------- | -------------------- | ---------- | ------------------ | --------- | ----- |
| 1       | Triple Deluxe        | 🟢 Libre   | -                  | -         |       |
| 2       | Double Deluxe        | 🔵 Occupée | [Nom]              | DD/MM     |       |
| 3       | Triple Deluxe        | 🟢 Libre   | -                  | -         |       |
| 4       | Double Supérieure    | 🟡 Pending | [Nom?]             | DD/MM     |       |
| 5       | Double Supérieure    | 🟢 Libre   | -                  | -         |       |
| 6       | Suite Exécutive      | 🟢 Libre   | -                  | -         |       |
| 7       | Suite King           | 🟢 Libre   | -                  | -         |       |
| 8       | Triple Deluxe        | 🟢 Libre   | -                  | -         |       |
| 9       | Suite Familiale      | 🟢 Libre   | -                  | -         |       |
| 10      | Suite                | 🟢 Libre   | -                  | -         |       |
| 11      | Suite Familiale      | 🟡 Pending | [Mission actuelle] | 21/12     |       |
| 12      | Suite Présidentielle | 🟢 Libre   | -                  | -         |       |

### 4.2 Légende

| Code | Signification              |
| ---- | -------------------------- |
| 🟢   | Libre / Disponible         |
| 🔵   | Occupée                    |
| 🟡   | Réservation pending        |
| 🔴   | Hors service / Maintenance |
| ⚪   | Bloquée (house use)        |

---

## 5. Analyse

### 5.1 Sources de Réservations

| Source           | Quantité | % Total | Tendance |
| ---------------- | -------- | ------- | -------- |
| Direct (Walk-in) | X        | X%      |          |
| Site Web         | X        | X%      |          |
| Booking.com      | X        | X%      |          |
| Expedia          | X        | X%      |          |
| Autres OTA       | X        | X%      |          |

### 5.2 Patterns Observés

- **Pattern 1** : [Description et implications]
- **Pattern 2** : [Description et implications]

### 5.3 Risques Identifiés

| Risque     | Probabilité         | Impact                    | Mitigation |
| ---------- | ------------------- | ------------------------- | ---------- |
| [Risque 1] | Haute/Moyenne/Basse | Critique/Important/Mineur | [Action]   |

---

## 6. Actions Recommandées

### 6.1 Actions Immédiates (P0-P1)

| #   | Action   | Responsable | Deadline | Dépendance |
| --- | -------- | ----------- | -------- | ---------- |
| 1   | [Action] | [Qui]       | [Quand]  | [Blocage?] |

### 6.2 Actions Cette Semaine (P2-P3)

| #   | Action   | Responsable | Deadline |
| --- | -------- | ----------- | -------- |
| 1   | [Action] | [Qui]       | [Quand]  |

### 6.3 Backlog (P4-P5)

- [ ] [Action future 1]
- [ ] [Action future 2]

---

## 7. Annexes

### 7.1 Logs de Navigation

```
[HH:MM] Action effectuée
[HH:MM] Page visitée
[HH:MM] Donnée extraite
```

### 7.2 Screenshots

> Référencer les screenshots capturés si pertinent
> Format: `assets/screenshots/YYYY-MM-DD-description.png`

### 7.3 Notes Techniques

- [Observations sur la plateforme]
- [Bugs ou comportements inattendus]
- [Suggestions d'amélioration]

---

## 8. Métadonnées

| Champ                 | Valeur                   |
| --------------------- | ------------------------ |
| **Créé par**          | [Agent/Omar]             |
| **Date création**     | YYYY-MM-DD HH:MM         |
| **Dernière MAJ**      | YYYY-MM-DD HH:MM         |
| **Version**           | 1.0                      |
| **Durée exploration** | X min                    |
| **Fichiers liés**     | [Liens vers autres docs] |

---

## Sources du Template

- [Hotelogix - 8 Must-Have Hotel PMS Reports](https://blog.hotelogix.com/hotel-reservation-report/)
- [Cloudbeds - 13 Hotel Audit Reports](https://www.cloudbeds.com/articles/6-reports-your-hotel-should-run-every-night/)
- [Smartsheet - Hotel Management Templates](https://www.smartsheet.com/content/hotel-management-templates)
- [DashThis - The Perfect Hotel Report](https://dashthis.com/blog/the-perfect-hotel-report/)

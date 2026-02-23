<!-- Security: Credentials redacted 2026-02-22. Original contained plaintext credentials for HotelRunner. -->
# Rapport Session Stratégie Tarifaire — 20 décembre 2025

**Date** : 20 décembre 2025
**Participants** : Omar El Mountassir, M. Said Thaifa (présent), Claude Code
**Statut** : EN COURS

> **Sources de vérité** :
> - Chambres & Pricing : [state/current/rooms.md](../../../../../state/current/rooms.md)
> - Prix planifiés : [state/planned/pricing.md](../../../../../state/planned/pricing.md)
> - Promotions : [state/current/promotions.md](../../../../../state/current/promotions.md)

---

## Résumé Exécutif

| Objectif                                 | Statut                        |
| ---------------------------------------- | ----------------------------- |
| Accès HotelRunner                        | ✅ Confirmé                   |
| Assignation Arne Cordes (chambres 4 & 5) | ✅ Fait                       |
| Interface modification prix localisée    | ✅ Calendar → Simple Updates  |
| Plan de pricing calculé                  | ✅ Voir section Prix          |
| Accès Booking.com Extranet               | ✅ Confirmé                   |
| Audit promotions Booking.com             | ✅ **CATASTROPHE IDENTIFIÉE** |

---

## 1. Accomplissements

### 1.1 Réservation Arne Cordes

| Réservation | Chambre | Dates     | Nuits | Total  |
| ----------- | ------- | --------- | ----- | ------ |
| #1          | **4**   | 20-25 déc | 5     | €617.5 |
| #2          | **5**   | 20-25 déc | 5     | €617.5 |

**Total combiné** : €1,235 | Canal : Booking.com

### 1.2 Mapping Chambres ↔ Types (Confirmé)

| N° Chambre | Type HotelRunner     | Marge nette visée |
| ---------- | -------------------- | ----------------- |
| 4, 5       | Double Room Superior | **120€**          |
| 1, 3, 8    | Deluxe Triple Room   | **150€**          |
| 2          | Deluxe Double Room   | **150€**          |
| 6          | Executive Suite      | **180€**          |
| 7          | Deluxe King Suite    | **330€**          |
| 9          | Family Suite         | **170€**          |
| 10         | Suite                | **200€**          |
| 11         | Family Suite         | **180€**          |
| 12         | Presidential Suite   | **450€**          |

### 1.3 Prix Booking.com Calculés (Commission 25%)

**Formule** : `Prix Booking = Marge nette / 0.75`

| Chambre | Type                 | Marge nette | Prix Booking (min) | Marché Palmeraie |
| ------- | -------------------- | ----------- | ------------------ | ---------------- |
| 4, 5    | Double Room Superior | 120€        | **160€**           | ✅ €130-180      |
| 1, 3, 8 | Deluxe Triple Room   | 150€        | **200€**           | ✅ €180-220      |
| 2       | Deluxe Double Room   | 150€        | **200€**           | ✅ €130-180      |
| 6       | Executive Suite      | 180€        | **240€**           | ✅ €200-280      |
| 7       | Deluxe King Suite    | 330€        | **440€**           | ⚠️ Premium       |
| 9       | Family Suite         | 170€        | **227€**           | ✅ €200-280      |
| 10      | Suite                | 200€        | **267€**           | ✅ €180-250      |
| 11      | Family Suite         | 180€        | **240€**           | ✅ €200-280      |
| 12      | Presidential Suite   | 450€        | **600€**           | ⚠️ Très premium  |

---

## 2. AUDIT PROMOTIONS — CATASTROPHE CONFIRMÉE

> **Détail complet** : `audit-promotions-booking.md`

### 2.1 Promotions Actives (8 identifiées)

| Promotion             | Réduction | Période       | Statut    |
| --------------------- | --------- | ------------- | --------- |
| Basic Deal            | **30%**   | → 30 nov 2026 | PERMANENT |
| Basic Deal            | **33%**   | → 30 nov 2026 | PERMANENT |
| Basic Deal            | **38%**   | → 30 nov 2026 | PERMANENT |
| Early Booker Deal     | **40%**   | → 30 nov 2026 | PERMANENT |
| Late Escape Deal      | **43%**   | → 7 jan 2026  | Actif     |
| Late Escape Deal      | **42%**   | → 7 jan 2026  | Actif     |
| Tarif géociblé Europe | **10%**   | Toujours      | PERMANENT |
| Tarif géociblé Maroc  | **10%**   | Toujours      | PERMANENT |

### 2.2 Impact ROI (exemple 200€)

| Scénario         | Net Villa | Marge visée | Écart      |
| ---------------- | --------- | ----------- | ---------- |
| Sans promo       | 150€      | 120€        | +30€       |
| Basic Deal 38%   | **93€**   | 120€        | **-27€**   |
| Early Booker 40% | **90€**   | 120€        | **-30€**   |
| Late Escape 43%  | **85.5€** | 120€        | **-34.5€** |

### 2.3 Recommandation Urgente

| Promo                 | Action                       |
| --------------------- | ---------------------------- |
| Early Booker 40%      | **DÉSACTIVER IMMÉDIATEMENT** |
| Basic Deal 38%        | **DÉSACTIVER**               |
| Late Escape 43% & 42% | **DÉSACTIVER**               |
| Basic Deal 30-33%     | Réduire à 10-15% max         |
| Tarifs géociblés      | Évaluer (désactiver ou 5%)   |

---

## 3. Prochaines Étapes

| Priorité | Tâche                               | Statut                       |
| -------- | ----------------------------------- | ---------------------------- |
| ✅       | Accéder à Booking.com Extranet      | FAIT                         |
| ✅       | Auditer promotions actives          | FAIT (8 promos, catastrophe) |
| 🔴 P0    | **Désactiver promos destructrices** | En attente validation        |
| 🔴 P0    | Configurer prix HotelRunner         | En attente validation        |
| 🟠 P1    | Vérifier synchro Booking.com        | Après config prix            |
| 🟠 P1    | Mettre à jour credentials.md        | À faire                      |

---

## 4. Credentials Validés

| Plateforme  | Email                    | Password            | Statut   |
| ----------- | ------------------------ | ------------------- | -------- |
| HotelRunner | `said_thaifa@hotmail.fr` | `[REDACTED]`   | ✅ Testé |
| Booking.com | `said_thaifa@hotmail.fr` | -- (session active) | ✅ Testé |

---

## 5. Recherche Effectuée

### 5.1 Revenue Management

- KPIs : ADR, RevPAR, Occupancy Rate (cible 65%+)
- Saisonnalité : Peak (100%), Shoulder (-15%), Low (-40%)

### 5.2 Marché Palmeraie Marrakech

- Budget : €40-85/nuit
- Mid-range : €130-220/nuit
- Boutique villa (segment Villa Thaifa) : €180-280/nuit
- High season : Octobre-Avril

### 5.3 Booking.com

- Commission standard : 15% (Villa Thaifa paie 25% — élevé !)
- Genius : gratuit mais -10% sur prix affiché
- **Promotions stackent** : Risque de cumuls destructeurs

---

## 6. Fichiers de Référence

| Fichier                                                           | Contenu                            |
| ----------------------------------------------------------------- | ---------------------------------- |
| `audit-promotions-booking.md`                                     | **Audit complet des 8 promotions** |
| `~/.claude/plans/eventual-hatching-koala.md`                      | Plan détaillé approuvé             |
| `.claude/output/.../hotelrunner-demo/rapport-demo-20-dec-2025.md` | Rapport démo HotelRunner           |
| `projects/2025-12_booking-hotelrunner/report.md`                  | Mapping chambres original          |

---

## 7. DÉCISIONS URGENTES — Réponse Omar/M. Said

> **Instructions** : Répondre directement dans ce fichier sous chaque question.

### 7.1 Désactivation des promotions destructrices

**Confirmez-vous la désactivation IMMÉDIATE de :**

- [ ] Early Booker Deal **40%**
- [ ] Basic Deal **38%**
- [ ] Late Escape Deal **43%** et **42%**

**Réponse** :

```
[OUI / NON / PRÉCISER]
```

### 7.2 Stratégie promos restantes

**Pour les Basic Deal 30% et 33%, que faire ?**

| Option | Description                          |
| ------ | ------------------------------------ |
| A      | Désactiver complètement (zéro promo) |
| B      | Réduire à 15% max                    |
| C      | Réduire à 10% max                    |
| D      | Garder (justifier)                   |

**Réponse** :

```
[ÉCRIRE ICI]
```

### 7.3 Tarifs géociblés (Europe & Maroc, 10%)

| Option | Description             |
| ------ | ----------------------- |
| A      | Désactiver complètement |
| B      | Réduire à 5%            |
| C      | Garder à 10%            |

**Réponse** :

```
[ÉCRIRE ICI]
```

### 7.4 Prix premium (chambres 7 et 12)

**Les chambres 7 (440€) et 12 (600€) sont au-dessus du marché. Confirmer ?**

| Option | Description                        |
| ------ | ---------------------------------- |
| A      | Oui, positionnement premium assumé |
| B      | Non, ajuster vers le marché        |

**Réponse** :

```
[ÉCRIRE ICI]
```

### 7.5 Prochaine action

**Qu'est-ce qu'on fait MAINTENANT ?**

| Option | Description                                         |
| ------ | --------------------------------------------------- |
| A      | Désactiver les promos destructrices sur Booking.com |
| B      | Configurer les prix sur HotelRunner d'abord         |
| C      | Les deux en parallèle                               |

**Réponse** :

```
[ÉCRIRE ICI]
```

---

## 8. Notes de Session

### 8.1 Contexte M. Said

- Présent pendant la session
- L'ancien gestionnaire a causé des problèmes de pricing
- Objectif : Maximiser le ROI, reprendre le contrôle

### 8.2 Commission Booking.com

- 25% est élevé (standard = 15%)
- À négocier à moyen terme (levier : volume + bonnes notes)

---

_Rapport généré automatiquement — Session du 20 décembre 2025_
_Espace de réponse prévu pour Omar_

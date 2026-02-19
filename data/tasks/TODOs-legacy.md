# Tâches — Villa Thaifa

> Dernière mise à jour : 2025-12-20 21:45

---

## Système de Prioritisation

**Approche hybride** : MoSCoW (importance) + Eisenhower (urgence)

### Matrice de priorité

|                         | **URGENT**                       | **NON URGENT**                  |
| ----------------------- | -------------------------------- | ------------------------------- |
| **MUST** (Critique)     | 🔴 P0 — Faire MAINTENANT         | 🟠 P1 — Planifier cette semaine |
| **SHOULD** (Important)  | 🟡 P2 — Faire aujourd'hui/demain | 🟢 P3 — Planifier ce mois       |
| **COULD** (Souhaitable) | 🔵 P4 — Si temps disponible      | ⚪ P5 — Backlog                 |
| **WON'T** (Exclu)       | ❌ Hors scope                    | ❌ Hors scope                   |

### Légende

| Priorité | Signification             | Délai              |
| -------- | ------------------------- | ------------------ |
| 🔴 P0    | Critique + Urgent         | Immédiat           |
| 🟠 P1    | Critique + Non urgent     | Cette semaine      |
| 🟡 P2    | Important + Urgent        | Aujourd'hui/demain |
| 🟢 P3    | Important + Non urgent    | Ce mois            |
| 🔵 P4    | Nice-to-have + Urgent     | Si temps           |
| ⚪ P5    | Nice-to-have + Non urgent | Backlog            |

---

## Tâches en cours

### 🔴 P0 — Critique + Urgent

- [ ] **⚠️ MÉTA-WORKFLOW : Configurer instances Claude pour fichiers, pas chat**

  - **Problème** : Questions, issues, infos importantes restent dans le chat éphémère
  - **Impact** : Omar ne peut pas gérer/suivre proprement
  - **Solution** : Toute info valuable → fichier (pas chat)
  - **Fichiers cibles** :
    - Questions → `.claude/output/.../questions-pending.md`
    - Issues → `.claude/output/.../blocages.md`
    - Décisions en attente → dans les rapports avec espace réponse
  - **Action** : Mettre à jour `CLAUDE.md` avec cette règle
  - Voir : `.claude/output/2025/Q4/reports/pricing-strategy-session/rapport-session-20-dec-2025.md`

- [ ] **Configurer prix HotelRunner** — Session pricing en cours

  - Interface : Calendar → Simple Updates
  - Prix calculés : voir rapport session
  - **En attente** : validation Omar des prix premium (7, 12)

- [x] ~~**Accéder à Booking.com Extranet** — Audit promotions~~ ✅ FAIT

  - URL : `admin.booking.com`
  - **Exécuté le 20 déc 2025**
  - 6 promotions désactivées (P0)
  - 2 promotions réduites (P1)
  - Voir : `.claude/output/2025/Q4/reports/pricing-strategy-session/execution-log-booking.md`

- [x] ~~**⚠️ URGENT : Assigner chambres Arne Cordes**~~ ✅ FAIT

  - Chambres 4 et 5 assignées (20-25 déc, 5 nuits)
  - Total : €1,235

- [ ] **Finaliser réservation chambre 11** — En attente réponse de M. Thaifa
  - Dates : 19→21 décembre 2025 (2 nuitées)
  - Chambre : Suite familiale (n°11)
  - Infos manquantes : nom invité, tarif, nb adultes
  - Bloqueur : réponse client

### 🟠 P1 — Critique + Non urgent

- [ ] **Assigner chambres Nicolas Lamblain** — Arrivée 26 déc

  - 2 réservations Double Room Superior
  - Confirmations : 6538291598 / 6538291598-1
  - Deadline : 25 déc

- [ ] **Assigner chambres Jean Damien Aubril** — Arrivée 27 déc

  - 2 réservations Deluxe Triple Room
  - Confirmations : 5352537667 / 5352537667-1
  - Chambres suggérées : 1, 3 ou 8
  - Deadline : 26 déc

- [ ] **Assigner chambre Quentin Warembourg** — Arrivée 29 déc
  - 1 réservation Suite (Booking.com)
  - Confirmation : 5446634150
  - Chambre suggérée : 10 (Suite)
  - Dates : 29 déc → **5 jan** (7 nuits)
  - Deadline assignation : 28 déc
  - **✅ VÉRIFIÉ 2025-12-20** :
    - Réservation confirmée depuis le 8 nov 2025
    - Total : €973 | Commission Booking : €262,71
    - HotelRunner : Payment Total €0 | Mode : Hotel Collect
    - Booking.com : Statut **OK** | Paiement par Booking.com / Virement bancaire
    - Cancellation policy : Flexible – 5 days (**limite : 24 déc**)
    - 2 adultes, 0 enfant | Bed & breakfast
  - ⚠️ **Voir tâche P2** : Décision requise avant 24 déc

### 🟡 P2 — Important + Urgent

- [x] ~~**⚠️ DEADLINE 24 DÉC : Décision Quentin Warembourg**~~ ✅ **RÉSOLU**

  - **Contexte initial** : M. Said inquiet car "pas de nouvelles" du client
  - **Investigation 2025-12-20** :
    - HotelRunner : Statut "Reservation", Hotel Collect, €0 reçu
    - Booking.com : Statut "OK", Paiements par Booking.com (virement prévu 1er fév 2026)
  - **✅ SIGNAUX POSITIFS TROUVÉS** :
    - Client a demandé infos navette aéroport → **prévoit vraiment venir**
    - Heure d'arrivée précisée : 21h-22h
    - Réservation depuis 6 semaines (8 nov 2025)
    - Paiement garanti par Booking.com
  - **Décision** : Réservation légitime, contacter client pour navette

- [x] ~~**📩 Répondre à Quentin Warembourg : Navette aéroport**~~ ✅ **ENVOYÉ**
  - **Demande client** : Intéressé par service navette aéroport
  - **Message envoyé** : 2025-12-20 ~18h via Booking.com
  - **Note** : Version raccourcie (manque tarifs). Tarif 200 MAD à communiquer si client confirme
  - **Brouillon** : `.claude/output/2025/Q4/drafts/message-quentin-navette.md`
  - **En attente** : Réponse client (numéro de vol, heure d'atterrissage)

### 🟢 P3 — Important + Non urgent

- [ ] **Préparer brief structuré pour futurs agents** — Documentation workflow HotelRunner
- [ ] **Investiguer portail Jisr l'Mokawala** — Go Siyaha / Maroc PME
- [ ] **RDV lundi 22 déc 10h** — Première rencontre officielle avec M. Thaifa

### 🔵 P4 — Nice-to-have

- [ ] **Explorer l'API HotelRunner** — Pour automatisation future
- [ ] **Créer template de rapport de mission** — Réutilisable pour autres clients

### ⚪ P5 — Backlog

- [ ] **Développer agent IA pour gestion réservations** — Projet à long terme
- [ ] **Réduire dépendance Booking.com** — Stratégie canaux directs

---

## Tâches terminées

### 2025-12-20

- [x] **Audit V2 Promotions Booking.com** ✅
  - 3 promotions non documentées identifiées
  - Early Booker Deal 10% (NOUVEAU)
  - Tarif Mobiles 10% (€15,614 revenus)
  - À l'étranger (géociblé) 10%
  - Toutes conformes à la stratégie (10-15% optimal)
  - 4 fichiers mis à jour
- [x] **Exécuter plan promotions Booking.com** ✅
  - 6 promotions P0 désactivées (40%, 38%, 43%, 42%, 10% Europe, 10% Maroc)
  - 2 promotions P1 réduites (33%→15%, 30%→10%)
  - Fichier log : `execution-log-booking.md`
- [x] Assigner Arne Cordes chambres 4 et 5 ✅
- [x] Localiser interface modification prix (Calendar → Simple Updates) ✅
- [x] Calculer prix Booking.com (formule: marge/0.75) ✅
- [x] Créer rapport session pricing ✅
- [x] Documenter mapping chambres ↔ types ✅
- [x] Investiguer réservation Quentin Warembourg (Suite 10, 29 déc - 5 jan) ✅
  - Résultat : Réservation légitime, Paiements par Booking.com
  - Signaux positifs : demande navette, heure d'arrivée précisée (21h-22h)
- [x] Créer brouillon message navette pour Quentin Warembourg ✅
  - Fichier : `.claude/output/2025/Q4/drafts/message-quentin-navette.md`
- [x] Documenter service transport ✅
  - Fichier : `docs/services-transport.md`
- [x] Envoyer message navette à Quentin Warembourg ✅
  - Via Booking.com (réservation 5446634150)
  - Version raccourcie envoyée (session interrompue)
  - En attente réponse client

### 2025-12-19

- [x] Se connecter à HotelRunner ✅
- [x] Corriger credentials dans la doc ✅
- [x] Vérifier disponibilité chambre 11 ✅
- [x] Créer rapport de mission ✅
- [x] Créer fichier lessons-learned.md ✅
- [x] Documenter erreur communication (pattern Scout→Rapport→Action) ✅
- [x] Documenter erreur ton/registre (vouvoiement + fluidité WhatsApp) ✅
- [x] Restructurer dossiers (`communication/` → racine) ✅
- [x] Créer `CLAUDE.md` (corrigé : racine, pas `.claude/`) ✅
- [x] Ajouter workflow TODOs.md dans CLAUDE.md ✅
- [x] Documenter erreur emplacement CLAUDE.md (patterns.md global) ✅
- [x] Refonte structure dossiers (plan + sources research) ✅
- [x] Créer `admin/`, `assets/`, `projects/` ✅
- [x] Migrer fichiers vers nouvelle structure ✅
- [x] Créer template client global (`~/Documents/templates/client/`) ✅
- [x] Mettre à jour CLAUDE.md avec nouveaux chemins ✅
- [x] Créer template rapport gold standard (`docs/templates/`) ✅
- [x] Explorer réservations HotelRunner ✅
- [x] Identifier 10 réservations non assignées ✅
- [x] Créer rapport exploration (`governance/inbox/ai/reports/`) ✅

---

## Bloqueurs actuels

| Bloqueur                | Impact                          | Dépendance               | Action                |
| ----------------------- | ------------------------------- | ------------------------ | --------------------- |
| Réponse M. Thaifa       | Impossible finaliser résa ch.11 | Client                   | Attendre              |
| ~~Accès Booking.com~~   | ~~Impossible auditer promos~~   | ~~Omar autorise~~        | ✅ RÉSOLU 20/12       |
| Validation prix premium | Config HotelRunner bloquée      | Omar répond dans rapport | Répondre dans fichier |

---

## Notes

### Contexte client

- **Client** : Said Thaifa (+60 ans)
- **Établissement** : Villa Thaifa (maison d'hôtes, Marrakech)
- **Relation** : Nouveau client potentiel (high-ticket)
- **Communication** : Formelle, respectueuse, vouvoiement obligatoire

### Prochaine échéance

- **Lundi 22 décembre 2025, 10h** — RDV avec M. Thaifa

---

## Sources — Système de prioritisation

- [Highberg - Comparison of prioritization methods](https://highberg.com/insights/a-comparison-of-prioritization-methods)
- [Medium - MoSCoW vs Eisenhower](https://medium.com/@nowacki.lukasz/moscow-method-vs-eisenhower-matrix-prioritization-of-tasks-in-the-project-372f8553c12a)
- [Product School - 9 Prioritization Frameworks](https://productschool.com/blog/product-fundamentals/ultimate-guide-product-prioritization)

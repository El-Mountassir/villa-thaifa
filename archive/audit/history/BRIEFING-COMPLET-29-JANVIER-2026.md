# 📋 BRIEFING COMPLET — 29 JANVIER 2026

> **Pour** : Omar El Mountassir + Futures Instances Claude
> **Date** : 29 janvier 2026 (matin)
> **Session précédente** : 28 janvier 2026 22h30
> **Objectif** : Reprendre EXACTEMENT où on s'est arrêté

---

## 🚨 URGENT — P0 (À FAIRE AUJOURD'HUI)

### 1. Demande Client — Anniversaire 30 Personnes (14-17 Mai 2026)

**STATUS** : ⏳ En attente réponses Said
**DEADLINE** : 30 janvier 2026 (envoi proposition client)
**REVENU POTENTIEL** : 7 000 - 10 000 €

#### Actions Immédiates (Aujourd'hui 29 Janvier)

**OMAR (Matin)** :
1. [ ] Envoyer message WhatsApp à Said
   - **Fichier** : `tmp/MESSAGE-POUR-SAID.txt`
   - **Canal** : WhatsApp +212 661-134194
   - **Action** : Copier-coller le message
2. [ ] Attendre réponses Said (JSON du formulaire)

**SAID (Journée)** :
1. [ ] Lire message Omar
2. [ ] Ouvrir `tmp/2026-01-28-demande-anniversaire-30-personnes.html`
3. [ ] Vérifier HotelRunner : 12 chambres libres 14-17 mai 2026 ?
4. [ ] Remplir formulaire (9 questions)
5. [ ] Exporter JSON (bouton dans formulaire)
6. [ ] Envoyer JSON + coordonnées client à Omar

**CLAUDE (Après réception JSON)** :
1. [ ] Lire JSON de Said
2. [ ] Rédiger réponse client professionnelle
3. [ ] Soumettre à validation Omar/Said
4. [ ] Finaliser message WhatsApp pour client

**📂 Fichiers à consulter** :
- `workstream/active/2026-01-28-demande-client-anniversaire-30-personnes.md` (détails complets)
- `tmp/MESSAGE-POUR-SAID.txt` (message à envoyer)
- `tmp/2026-01-28-demande-anniversaire-30-personnes.html` (formulaire Said)
- `data/communication/client-requests/2026-01-28-anniversaire-30-personnes.md` (tracking)

---

## 🟠 PRIORITÉ HAUTE — P1 (Cette Semaine)

### 2. Investigation Room Type vs Room Number (En Cours)

**STATUS** : 🟡 Recherche en cours
**RISQUE** : Perte reviews Booking.com si mauvaise manipulation
**FICHIER** : `docs/project/plans/2026-01-13-room-mapping-investigation.md`

#### Sous-tâches :
- [ ] Rechercher risques renommage Booking.com (reviews/ID)
- [ ] Backup complet room content & photos
- [ ] Décider approche (renommer ou garder mapping actuel)

**⚠️ ATTENTION** : Ne rien toucher sur Booking.com avant validation Omar + recherche complète.

---

### 3. Machine-Ready Prep (Architecture)

**STATUS** : 📋 Planifié
**OBJECTIF** : Définir stack technique complet

#### Sous-tâches :
- [ ] Définir Tech Stack
  - Frontend : Next.js 16 ✅ (déjà en place)
  - Backend : Fastify ? Hono ? tRPC ?
  - Database : PostgreSQL ? Supabase ? PlanetScale ?
  - ORM : Prisma ? Drizzle ?
- [ ] Structure de données OTA (Booking.com, HotelRunner, Expedia)
- [ ] Schéma base de données (réservations, pricing, inventory)

**📂 Fichier à créer** : `docs/architecture/tech-stack-decision.md`

---

## 🟢 PRIORITÉ MOYENNE — P2 (Ce Mois)

### 4. Établir Scoring System

**STATUS** : 📋 Planifié
**FICHIER** : `systems/scoring-system.json` (à créer)
**OBJECTIF** : Système de notation pour clients, réservations, performances

#### Critères à définir :
- Score client (fiabilité, récurrence)
- Score chambre (revenue, occupation)
- Score saisonnier (demande, pricing)

---

### 5. Requirements Hierarchy (PRD/SRS)

**STATUS** : 📋 Planifié
**DOSSIER** : `docs/project/requirements/` (à créer)

#### Structure proposée :
```
docs/project/requirements/
├── PRD-001-platform-overview.md
├── SRS-001-reservation-system.md
├── SRS-002-pricing-engine.md
└── SRS-003-channel-manager-integration.md
```

---

### 6. Quality Audit (Documentation)

**STATUS** : 📋 Planifié
**OBJECTIF** : Relire et améliorer tous les docs existants

#### Documents à auditer :
- [ ] `AGENTS.md` (routing)
- [ ] `CLAUDE.md` (context)
- [ ] `GEMINI.md` (brain)
- [ ] `docs/leadership/` (stakeholders, vision, priorities)
- [ ] `docs/project/standards/` (code of conduct, protocols)

---

## 📊 BACKLOG — P3 (Futur)

### 7. Intégrations OTA

**STATUS** : ⏳ En attente setup HotelRunner complet

#### Plateformes :
- [x] Booking.com (actif, 25% commission)
- [ ] Airbnb (compte à créer)
- [ ] Expedia (compte existe, à configurer)

**Bloqueur** : HotelRunner doit être configuré complètement d'abord.

---

### 8. Site Web & Booking Engine

**STATUS** : 📋 Futur (Q2 2026 ?)

#### Options :
- HotelRunner Booking Engine (inclus dans abonnement ?)
- Site custom Next.js + Stripe
- Plateforme tierce (Hotelogix, etc.)

---

### 9. PMS (Property Management System)

**STATUS** : 📋 Investigation future

#### Options évaluées :
- Hotelogix
- Cloudbeds
- Custom build (Next.js + PostgreSQL)

**Décision** : Attendre fin Phase 1 avant de choisir.

---

## 🗂️ STRUCTURE WORKSTREAM

```
workstream/
├── active/
│   └── 2026-01-28-demande-client-anniversaire-30-personnes.md ← P0 URGENT
├── review/
│   └── (vide actuellement)
├── backlog/
│   ├── tech-stack-definition.md (à créer)
│   ├── scoring-system.md (à créer)
│   ├── requirements-hierarchy.md (à créer)
│   └── room-mapping-investigation.md (en cours)
└── done/
    └── 2026-01-24-extend-pricing-2026.md ✅
    └── 2026-01-13-update-hotelrunner-pricing.md ✅
```

---

## 📁 FICHIERS CRÉÉS SESSION PRÉCÉDENTE (28 JANVIER)

| Fichier | Chemin | Usage |
|---------|--------|-------|
| **Formulaire HTML** | `tmp/2026-01-28-demande-anniversaire-30-personnes.html` | Said : remplir + exporter |
| **Message Said** | `tmp/MESSAGE-POUR-SAID.txt` | Omar : envoyer WhatsApp |
| **Politique événements** | `docs/knowledge/villa-thaifa/policies/events-privatization.md` | Référence permanente |
| **Suivi client** | `data/communication/client-requests/2026-01-28-anniversaire-30-personnes.md` | Historique |
| **Workstream actif** | `workstream/active/2026-01-28-demande-client-anniversaire-30-personnes.md` | Tracking complet |
| **Ce briefing** | `BRIEFING-COMPLET-29-JANVIER-2026.md` | Résumé général |

---

## 🎯 CHECKLIST OMAR (Aujourd'hui Matin)

### Immédiat (10 minutes)
- [ ] Lire ce document (BRIEFING-COMPLET-29-JANVIER-2026.md)
- [ ] Lire `tmp/MESSAGE-POUR-SAID.txt`
- [ ] Envoyer message WhatsApp à Said
- [ ] Vérifier si Said a répondu

### En Journée
- [ ] Attendre JSON de Said
- [ ] Dès réception → Transférer à Claude
- [ ] Valider réponse client préparée par Claude
- [ ] S'assurer que Said envoie au client avant 30 janvier

---

## 🤖 CHECKLIST FUTURES INSTANCES CLAUDE

### Au démarrage d'une nouvelle session :

1. **Lire en priorité** :
   - [ ] Ce document (`BRIEFING-COMPLET-29-JANVIER-2026.md`)
   - [ ] `workstream/active/` (tous les fichiers)
   - [ ] `tasks/active.md`

2. **Vérifier statuts** :
   - [ ] JSON de Said reçu ?
   - [ ] Réponse client envoyée ?
   - [ ] Deadline 30 janvier respectée ?

3. **Actions selon statut** :
   - Si JSON reçu → Rédiger réponse client (priorité absolue)
   - Si pas de JSON → Relancer Omar
   - Si deadline dépassée → Escalader + proposer solution

4. **Rappels automatiques** :
   - Toujours lire `workstream/active/` au début de session
   - Vérifier deadlines
   - Proposer next steps si Omar demande "Quoi faire ?"

---

## 🔔 RAPPELS IMPORTANTS

### Politique Créée (Nouvelle)
**Privatisation événements** :
- Tarif : 2 000 €/nuit (hors prestations)
- Capacité : 37 adultes max (12 chambres)
- Document : `docs/knowledge/villa-thaifa/policies/events-privatization.md`

### Credentials
- **HotelRunner** : Compte OWNER (Said) utilisé car compte ADMIN (Omar) n'existe pas encore
- **Booking.com** : Compte ADMIN (Omar) disponible
- **Expedia** : Compte existe (2FA SMS à Omar)

### Limitations Connues
- **agent-browser** : Profile persistence bug (re-auth manuelle requise)
- **Chrome automation** : Extension peut se déconnecter (vérifier connexion avant usage)

---

## 📞 CONTACTS

- **Said Thaifa** : +212 661-134194 (WhatsApp)
- **Omar El Mountassir** : omar@el-mountassir.com / +212 643-390409
- **Client anniversaire** : Coordonnées à récupérer via Said

---

## 🗓️ TIMELINE CRITIQUE

| Date | Événement | Responsable | Status |
|------|-----------|-------------|--------|
| **28 jan 20:16** | Réception demande client | Client → Said | ✅ |
| **28 jan 22:30** | Analyse + docs créés | Claude + Omar | ✅ |
| **29 jan matin** | Envoi message à Said | Omar | ⏳ |
| **29 jan journée** | Réponses Said (JSON) | Said | ⏳ |
| **29 jan soir** | Rédaction réponse client | Claude | ⏳ |
| **30 jan matin** | Envoi au client | Said | ⏳ |
| **31 jan - 2 fév** | Réponse client attendue | Client | ⏳ |

---

## 💡 CONSEILS POUR FUTURES INSTANCES

### Ton & Communication
- **Client** : Professionnel, formel, accueillant
- **Said** : Formel, vouvoiement, direct (néerlandais préféré mais français OK)
- **Omar** : Collaboratif, technique

### Erreurs à Éviter
- ❌ Ne PAS modifier Booking.com sans backup complet
- ❌ Ne PAS promettre au client sans confirmation Said
- ❌ Ne PAS utiliser compte OWNER (Said) sans demander
- ❌ Ne PAS oublier de clarifier "une seule villa" au client

### Best Practices
- ✅ Toujours documenter dans `workstream/`
- ✅ Toujours créer backup avant modification
- ✅ Toujours demander validation Omar pour décisions importantes
- ✅ Toujours capturer les learnings (politique événements créée = exemple)

---

## 🎓 LEARNINGS SESSION PRÉCÉDENTE

### Ce qui a bien fonctionné
1. **Formulaire HTML interactif** : Excellent outil pour collecter infos structurées
2. **Documentation politique événements** : Maintenant réutilisable
3. **Analyse capacité** : Calculs précis (37 adultes max)
4. **Workflow clair** : Said → JSON → Claude → Client

### Ce qui n'a pas fonctionné
1. **Chrome automation** : Extension déconnectée (limitation technique)
2. **Disponibilités HotelRunner** : Non vérifiées automatiquement

### Améliorations futures
1. Alternative à agent-browser (Playwright ? Puppeteer ?)
2. Script de vérification disponibilités HotelRunner
3. Template réponse client événements

---

## 📊 MÉTRIQUES PROJET

### Documentation
- **Fichiers totaux** : ~150+
- **Fichiers créés session 28 jan** : 6
- **Workstream actif** : 1 item (P0)
- **Backlog** : ~15 items (P1-P3)

### Financier
- **Revenu potentiel demande en cours** : 7 000 - 10 000 €
- **Pricing configuré** : ✅ Jan-Fév 2026
- **Channels actifs** : 1 (Booking.com)
- **Channels à activer** : 2 (Airbnb, Expedia)

### Technique
- **Stack Frontend** : ✅ Next.js 16
- **Stack Backend** : ⏳ À définir
- **Database** : ⏳ À définir
- **Tests** : ❌ Pas encore

---

## 🚀 PROCHAINE SESSION SUGGÉRÉE

### Si JSON de Said reçu :
1. Lire JSON
2. Rédiger réponse client (2 versions : français + néerlandais si besoin)
3. Soumettre à validation
4. Préparer message WhatsApp final

### Si JSON pas encore reçu :
1. Relancer Omar
2. Vérifier si message envoyé à Said
3. Proposer alternative (appel téléphonique ?)

### Autres tâches prioritaires :
1. Room mapping investigation (P1)
2. Tech stack decision (P1)
3. Scoring system (P2)

---

## ✅ VALIDATION BRIEFING

**Ce document contient** :
- ✅ Demande client urgente (P0)
- ✅ Toutes les tâches en cours (P1-P3)
- ✅ Fichiers créés session précédente
- ✅ Checklist Omar (aujourd'hui)
- ✅ Checklist futures instances Claude
- ✅ Timeline critique
- ✅ Learnings & best practices
- ✅ Contacts & credentials
- ✅ Rappels importants

**Prêt pour reprise immédiate** : ✅ OUI

---

## 📝 NOTES FINALES

**Session précédente (28 janvier 22:30)** :
- Durée : ~2h30
- Documents créés : 6 fichiers
- Status : Bloqué sur réponses Said
- Prochaine action : Omar envoie message à Said

**Pour aujourd'hui (29 janvier)** :
- Priorité absolue : Recevoir JSON de Said
- Deadline critique : 30 janvier (envoi client)
- Revenu potentiel : 7 000 - 10 000 €

**Message clé** :
> "Ne rien laisser tomber. Toutes les infos sont capturées. Tout est prêt pour reprendre exactement où on s'est arrêté."

---

_Document vivant — Mise à jour quotidienne recommandée_
_Créé le 2026-01-28 22:45 par Claude_
_Pour : Omar El Mountassir + Futures Instances Claude_
_Prochaine revue : 2026-01-29 matin (après envoi message Said)_

---

**🎯 ACTION IMMÉDIATE : Omar, envoyez le message à Said (`tmp/MESSAGE-POUR-SAID.txt`) dès que possible !**

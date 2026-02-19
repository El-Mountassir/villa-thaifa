# Stakeholders — Villa Thaifa

> Unified stakeholder reference: profiles, contacts, decisions, and team structure.

## Overview

> **Quick Reference** pour les parties prenantes du projet
> **Last Updated**: 2026-01-24
> **Read Time**: < 2 minutes

---

## 🎯 Project Overview

**Mission**: Digital transformation of Villa Thaifa from manual operations to optimized, automated systems
**Type**: Consulting / AI-First Workforce
**Timeline**: Dec 2025 → Ongoing
**Phase**: 1 - Stabilization & Cleanup

---

## 👥 Stakeholders

### 1. Client - Said Thaifa

**Role**: Owner & Operator of Villa Thaifa

| Field                 | Value                                                    |
| --------------------- | -------------------------------------------------------- |
| **Contact**           | <said_thaifa@hotmail.fr> / +212 661-134194 (WhatsApp ⭐) |
| **Age**               | 78 years                                                 |
| **Property**          | Villa Thaifa (12 rooms, 4★, Palmeraie Marrakech)         |
| **Platform Accounts** | HotelRunner, Booking.com (Owner access)                  |

**Key Facts**:

- 🏆 Booking.com rating: 9.3/10 ("Wonderful")
- 🎯 Business: Fully manual, everything memorized
- 💡 Goal: Reduce operational burden, optimize revenue
- 🚨 **Communication**: ALWAYS use vouvoiement (formal French), WhatsApp preferred
- 📅 Active client since December 2025

**⚠️ Critical Rule for Agents**: Scout → Rapport → Questions → Action
(Never ask for info without first reporting what you've discovered)

**📄 Detailed Profile**: [`data/admin/client/PROFILE.md`](../../data/admin/client/PROFILE.md)

---

### 2. Consultant - Omar El Mountassir

**Role**: CEO & Project Leader

| Field                 | Value                                                        |
| --------------------- | ------------------------------------------------------------ |
| **Contact**           | <omar@el-mountassir.com>                                     |
| **Responsibilities**  | Strategy, team leadership, client relations, final approvals |
| **Team**              | 17 AI agents + Claude (CTO)                                  |
| **Platform Accounts** | HotelRunner, Booking.com (Admin access)                      |

**Key Facts**:

- 🎯 Philosophy: "AI-First" - Agents are co-workers, not tools
- 🔐 Manages admin accounts for security & traceability
- ✅ Must approve all critical operations (pricing, platforms, client comm)
- 📊 Data-driven, systematic, documented decision-making

**📄 Detailed Profile**: [`profiles/OMAR-EL-MOUNTASSIR.md`](./profiles/OMAR-EL-MOUNTASSIR.md)

---

### 3. Technical Team - AI Agents

**CTO/Architect**: Claude (successive instances)
**Workforce**: 17 specialized AI agents

| Category    | Count | Function                              |
| ----------- | ----- | ------------------------------------- |
| Operations  | 4     | Pricing, reservations, calendar, sync |
| Technical   | 4     | Validation, browser, security, audits |
| Meta        | 7     | Research, reporting, documentation    |
| Hospitality | 2     | Guest communication, translation      |

**📄 Team Structure**: [`TEAM.md`](./TEAM.md)

---

## 🔗 Relationship Structure

```
Said Thaifa (Client/Owner)
    ↓ Mandate
Omar El Mountassir (Consultant/CEO)
    ↓ Leadership
Claude (CTO/Architect)
    ↓ Management
17 AI Agents (Specialized Workforce)
```

---

## ⚡ Decision Hierarchy

| Type                                   | Process                                                     |
| -------------------------------------- | ----------------------------------------------------------- |
| **Strategic** (Vision, Budget, Exit)   | Omar recommends → Said decides → Omar executes              |
| **Operational** (Pricing, OTAs, Setup) | Agents analyze → Claude validates → Omar approves → Execute |
| **Technical** (Architecture, Tools)    | Claude proposes → Omar validates → Execute                  |

---

## 🚨 Critical Rules for AI Agents

### Platform Operations

**ALWAYS** get Omar approval before:

- ❗ Modifying pricing, availability, or reservations
- ❗ Communicating with Said Thaifa
- ❗ Making budget or timeline decisions
- ❗ Executing platform changes

### Account Usage

- ✅ **USE**: Omar's admin accounts (<omar@el-mountassir.com)>
- ❌ **NEVER USE**: Said's owner accounts (unless explicit Omar approval)

### Platform Credentials

**Location**: `.env.local` (project root)
**Structure reference**: `.env.example`

**Quick access:**

1. Read `.env.local` file
2. Extract needed credentials (HOTELRUNNER*ADMIN*_, BOOKING*ADMIN*_)
3. Use admin accounts by default
4. Handle OTP/reCAPTCHA (request from Omar)

**⚠️ Security**: Never log, output, or store credentials. Read on demand only.

**📖 Full Guide**: [`../operations/CREDENTIALS.md`](../operations/CREDENTIALS.md)

### Communication with Said

**Required Protocol**:

1. ✅ Vouvoiement obligatoire (formal "vous")
2. ✅ WhatsApp preferred channel
3. ✅ Scout → Rapport → Questions → Action
4. ❌ NEVER ask questions without reporting findings first

### Emergency Protocol

If critical issue (platform bug, lost reservation, pricing error):

1. **STOP** all operations
2. **DOCUMENT** incident immediately
3. **NOTIFY** Omar
4. **WAIT** for instructions

---

## 📋 Quick Decision Guide for Agents

**Can Proceed Autonomously**:

- ✅ Research & analysis
- ✅ Documentation updates
- ✅ Non-critical bug fixes
- ✅ Internal reports

**Must Get Omar Approval**:

- ❗ All platform operations
- ❗ Client communications
- ❗ Financial decisions
- ❗ Timeline changes

---

## 📚 Documentation Map

| Need                | Document                                                                                |
| ------------------- | --------------------------------------------------------------------------------------- |
| **Who is Said?**    | [`data/admin/client/PROFILE.md`](../../data/admin/client/PROFILE.md) (detailed profile) |
| **Who is Omar?**    | [`profiles/OMAR-EL-MOUNTASSIR.md`](./profiles/OMAR-EL-MOUNTASSIR.md) (detailed profile) |
| **Team structure?** | [`TEAM.md`](./TEAM.md) (17 AI agents)                                                   |
| **What to do?**     | [`../../ROADMAP.md`](../../ROADMAP.md) (project plan)                                   |
| **Current tasks?**  | [`../../tasks/active.md`](../../tasks/active.md) (active work)                          |
| **How to work?**    | [`../project/standards/agents/`](../project/standards/agents/) (protocols)              |
| **Navigate docs?**  | [`INDEX.md`](./INDEX.md) (documentation index)                                          |

---

## ✅ Before Starting Any Task

**Checklist for AI Agents**:

1. ☐ Read this document (STAKEHOLDERS.md)?
2. ☐ Understand my role in the hierarchy?
3. ☐ Know if I need Omar approval?
4. ☐ Using correct accounts (admin vs owner)?
5. ☐ Respecting communication protocol with Said?
6. ☐ Ready to document my work?

**If ANY answer is NO → STOP and read the relevant documentation**

---

## 📞 Emergency Contacts

- **Omar El Mountassir**: +212 643 39 04 09 (Phone & WhatsApp) / <omar@el-mountassir.com>
- **Said Thaifa**: +212 661-134194 (Phone & WhatsApp) / <said_thaifa@hotmail.fr>

---

_Single Source of Truth for stakeholder relationships_
_For detailed profiles, see [`profiles/`](./profiles/) directory_
_Last updated: 2026-01-24 by Omar El Mountassir_

---

## Contact Information

- **Relation** : Nouveau client potentiel (high-ticket)

## Principal

| Champ    | Valeur                   |
| -------- | ------------------------ |
| Nom      | Said Thaifa              |
| Âge      | 78 ans                   |
| WhatsApp | +212 661-134194          |
| Email    | <said_thaifa@hotmail.fr> |
| Email    | <saidthaifa@gmail.com>   |

### Langues Parlées

| Langue      | Niveau  |
| ----------- | ------- |
| Arabe       | Natif   |
| Français    | Courant |
| Anglais     | Basique |
| Néerlandais | Courant |

## Secondaire

| Champ | Valeur                                       |
| ----- | -------------------------------------------- |
| Nom   | Nezha Thaifa                                 |
| Rôle  | Co-gérante / Épouse de M. Said               |
| Note  | Accueil chaleureux, petits-déjeuners copieux |

> **Réputation** : Appréciée pour son hospitalité, contribuant à une ambiance détendue et confortable pour les voyageurs. Reviews mentionnent une atmosphère "comme en famille".

## Établissement

| Champ    | Valeur           |
| -------- | ---------------- |
| Nom      | Villa Thaifa     |
| Type     | Maison d'hôtes   |
| Ville    | Marrakech, Maroc |
| Chambres | 12               |

> Source: Booking.com profil établissement

---

## Notes

- Communication formelle
- Client senior — respect sans rigidité
- Said et Nezha gèrent ensemble la Villa

### Communication Channels

> **PROMPT SYSTÈME** : À respecter impérativement pour toute interaction avec Said Thaifa.
> **Dernière mise à jour** : 2026-01-24
> **Priorité**: P1 (critique)

---

## 📞 Canaux

| Canal        | Usage         | Détails                                             |
| ------------ | ------------- | --------------------------------------------------- |
| **WhatsApp** | **PRINCIPAL** | Canal "Action-Réaction" (Voir protocole ci-dessous) |
| Email        | Secondaire    | Pour les rapports mensuels / officiels              |
| Téléphone    | Urgence       | +212 661-134194                                     |
| En face      | Rare          | Réunions stratégiques                               |

---

## 📝 Templates (Rapports)

### Rapport Hebdomadaire (Interne/Email)

```markdown
## Semaine du [DATE]

### ✅ Accompli

- TODO

### 🔄 En cours

- TODO

### ⚠️ Problèmes

- TODO

### 📅 Semaine prochaine

- TODO
```

---

## 🎯 PROTOCOLE D'INTERACTION (WhatsApp - "Dutch First")

### 1. CONTEXTE & RÔLE

Tu agis en tant que **"Omar El Mountassir" (Workforce Agentic Hybride)** pour le client Said Thaifa (propriétaire de la Villa Thaifa, 78 ans, établissement 9.3/10).

**Ton but** : Agir comme un **"Intendant Numérique"**. Tu gères la complexité technique (HotelRunner, Booking) pour lui offrir la tranquillité d'esprit.

### 2. RÈGLES D'OR

#### Règle #1 : "Dutch First" avec Validation Miroir

La langue d'interaction avec Said est le **Néerlandais**, mais Omar doit valider le contenu.
Tu dois **IMPÉRATIVEMENT** générer chaque réponse en deux blocs distincts :

1.  🇳🇱 **MESSAGE À ENVOYER (Néerlandais)** : Le message final, optimisé, prêt à être copié-collé pour Said.
2.  🇫🇷 **VALIDATION (Français)** : La traduction exacte ou le résumé substantiel pour qu'Omar puisse valider l'action sans ambiguïté.

> **Clause de sécurité** : Si Said pose une question stratégique complexe en Français, tu peux répondre en Français pour la clarté, puis conclure en Néerlandais.

#### Règle #2 : La structure "Action-Réaction"

Ne jamais dire "Je vais le faire". Dire "**C'est fait**".

- ❌ **Mauvais** : "Ik zal kijken..." (Je vais regarder...)
- ✅ **Bon** : "Genoteerd, ik ben ermee bezig." (Noté, en cours.)
- ✅ **Excellent** : "Missie voltooid ✅. Data geblokkeerd." (Mission accomplie.)

#### Règle #3 : Visuel & Compact

- Utilise des listes à puces.
- Utilise des Emojis : ✅ (Gedaan), 🔒 (Geblokkeerd), 💶 (Prijs).
- **Gras** pour les dates et prix.

#### Règle #4 : Gestion de l'Erreur (S.A.P)

- **Situatie**: "De data stonden nog open."
- **Actie**: "Ik heb dit handmatig geblokkeerd."
- **Plan**: "Ik neem contact op met support."

### 3. MODÈLES DE RÉPONSES (TEMPLATES)

**SCÉNARIO A : Blocage / Fermeture**

> **🇳🇱 MESSAGE**
> "Salam Si Said,
> Missie voltooid ✅.
> Ik heb Kamer 4 geblokkeerd voor de gevraagde data:
> 📅 **Van 08 maart tot 12 maart**
> Geen risico meer op dubbele boekingen.
> Fijne dag! 🙏"

**SCÉNARIO B : Prix**

> **🇳🇱 MESSAGE**
> "Het is geregeld Si Said.
> Update uitgevoerd:
> 🏠 **Presidentiële Suite**
> 💶 Nieuw tarief: **€ 449**
> Direct gesynchroniseerd. Alles is in orde! 👍"

**SCÉNARIO C : Réception**

> **🇳🇱 MESSAGE**
> "Goed ontvangen Si Said! 🙏
> Ik download de bestanden en ga er direct mee aan de slag."

---

## 5. TONALITÉ & STYLE

- **Salutation** : "Salam Si Said" ou "Goedendag Si Said".
- **Clôture** : "Mijn vriend", "Fijne avond", "Tot uw dienst".
- **Vocabulaire clé** : `Missie voltooid`, `Alles is in orde`, `Geen zorgen`.

---

**Tags**: `protocol` `communication` `dutch` `client`

---

## Profiles

### Said Thaifa — Owner

> **Quick Reference**: See [../STAKEHOLDERS.md](../STAKEHOLDERS.md) for overview
> **Related**: [OMAR-EL-MOUNTASSIR.md](./OMAR-EL-MOUNTASSIR.md) (Consultant profile)
> **Last Updated**: 2026-01-24 (Refactored from legacy/archive_v1/admin/client/PROFILE.md)

---

## Document Status

| Field                 | Value                                   |
| --------------------- | --------------------------------------- |
| **Client Status**     | Active - Digital Transformation Project |
| **Project Phase**     | Phase 1 - Stabilization & Cleanup       |
| **Priority**          | HIGH                                    |
| **Created**           | 2025-12-19                              |
| **Last Major Update** | 2025-12-20                              |
| **Refactored**        | 2026-01-24                              |

---

## 1. Snapshot Exécutif

### KPIs Clés

| Métrique               | Valeur                              | Note                           |
| ---------------------- | ----------------------------------- | ------------------------------ |
| **Chambres**           | 12                                  | 8 types sur Booking.com        |
| **Note Booking**       | 9.3/10 (80 avis)                    | "Wonderful"                    |
| **Commission Booking** | 25%                                 | Élevée (standard = 15%)        |
| **PMS**                | Aucun                               | Tout dans la tête de M. Thaifa |
| **Channel Manager**    | HotelRunner                         | Actif depuis 2025-12           |
| **OTAs**               | Booking ✅ / Airbnb ⏳ / Expedia ⏳ | En cours de setup              |

### Scores Détaillés Booking.com

| Catégorie                | Score | Niveau       |
| ------------------------ | ----- | ------------ |
| **Staff**                | 9.7   | Exceptionnel |
| **Propreté**             | 9.4   | Excellent    |
| **Confort**              | 9.4   | Excellent    |
| **Équipements**          | 9.3   | Excellent    |
| **Rapport qualité/prix** | 8.9   | Très bon     |
| **WiFi**                 | 8.8   | Très bon     |
| **Localisation**         | 8.2   | Bon          |
| **Petit-déjeuner**       | 10    | Parfait      |

> **Point fort majeur** : Staff noté 9.7/10 et petit-déjeuner parfait 10/10

### État Opérationnel Actuel

| Métrique                        | Valeur     |
| ------------------------------- | ---------- |
| **Réservations confirmées**     | 11         |
| **Revenue prévu**               | €8,008.85  |
| **Occupation peak (29-31 déc)** | 50% (6/12) |
| **Prix configurés HotelRunner** | 0/9 types  |
| **Promotions actives Booking**  | 5 (10-15%) |

→ Voir `data/specs/` pour détails opérationnels

---

## 2. Contact & Communication

### 2.1 Contact Principal

| Champ         | Valeur                   |
| ------------- | ------------------------ |
| **Nom**       | Said Thaifa              |
| **Âge**       | 78 ans                   |
| **Email**     | <said_thaifa@hotmail.fr> |
| **Email**     | <saidthaifa@gmail.com>   |
| **Téléphone** | +212 661-134194          |
| **WhatsApp**  | +212 661-134194          |

**Background professionnel** :

- Propriétaire et hôte de Villa Thaifa (avec son épouse Nezha)
- CEO / Agent immobilier à Marrakech
- Spécialités : ventes, achats, locations saisonnières
- Réputation : accueil chaleureux, fait que les clients se sentent "comme chez eux"

### 2.2 Protocole de Communication

| Règle        | Détail                                                      |
| ------------ | ----------------------------------------------------------- |
| **Ton**      | Formel & Direct ("Action-Réaction")                         |
| **Langue**   | **DUTCH FIRST** (Néerlandais)                               |
| **Format**   | Double sortie (NL pour lui, FR pour Omar)                   |
| **Standard** | 👉 [COMMUNICATION.md](../knowledge/client/COMMUNICATION.md) |

### 2.3 Pattern de Communication

```text
1. SCOUT    → Explorer, vérifier la faisabilité
2. RAPPORT  → Tenir le client informé des découvertes
3. QUESTIONS → Demander les infos manquantes (avec contexte)
4. ACTION   → Exécuter quand tout est clair
```

> **Règle d'or** : Ne jamais demander des infos sans d'abord faire un rapport de ce qu'on a découvert.

→ Voir `docs/lessons-learned.md` pour les patterns documentés

---

## 3. Établissement

### 3.1 Informations Générales

| Champ          | Valeur                                      |
| -------------- | ------------------------------------------- |
| **Nom**        | Villa Thaifa (parfois "Villa Thaifa & SPA") |
| **Type**       | Maison d'hôtes de charme / B&B (4★)         |
| **Adresse**    | Route de Fès, Km 12                         |
| **Zone**       | Palmeraie / Ouled Jelal (12-14 km centre)   |
| **Ville**      | Marrakech, Maroc                            |
| **Chambres**   | 12                                          |
| **Rénovation** | Récemment rénovée                           |

### 3.2 Équipements & Services

| Catégorie      | Détails                                                    |
| -------------- | ---------------------------------------------------------- |
| **Détente**    | Piscine infinity (ouverte toute l'année), jardin, solarium |
| **Bien-être**  | Spa/Hammam, massages (supplément)                          |
| **Restaurant** | "Thaifa's restaurant" — Cuisine marocaine                  |
| **Cuisine**    | Marocaine (halal, végétarien) — "Best tagine in Morocco"   |
| **Chambres**   | Climatisation, chauffage, TV satellite, Wi-Fi, terrasse    |
| **Services**   | Parking gratuit, navette aéroport, location voiture        |
| **Sécurité**   | 24h/24, CCTV, coffre-fort, alarme                          |
| **Langues**    | Arabe, Anglais, Français, Néerlandais                      |

### Petit-déjeuner (Score 10/10)

| Attribut     | Valeur                                                                         |
| ------------ | ------------------------------------------------------------------------------ |
| **Prix**     | MAD 160.90/personne                                                            |
| **Horaires** | 08:30 - 11:00                                                                  |
| **Type**     | Continental, Halal                                                             |
| **Menu**     | Viennoiseries, pain, pancakes, oeufs, fromage, spécialités locales, confitures |

### 3.3 Positionnement & Réputation

| Aspect                 | Valeur                                                                  |
| ---------------------- | ----------------------------------------------------------------------- |
| **Gamme tarifaire**    | 160-600 €/nuit (selon type)                                             |
| **Réputation**         | Très bonne (9.3/10 Booking)                                             |
| **Points forts**       | Calme, jardins, piscine infinity, accueil chaleureux ("comme chez soi") |
| **Atout localisation** | Calme et paisible, loin du bruit de la ville (14 km du centre)          |

→ Voir `data/specs/hotel/rooms.md` pour le détail des chambres et pricing

---

## 4. Contexte Business

### 4.1 Faits Confirmés ✅

| Fait                | Détail                                              |
| ------------------- | --------------------------------------------------- |
| **PMS actuel**      | Aucun — Tout se fait dans la tête de M. Said Thaifa |
| **Channel Manager** | HotelRunner (actif depuis déc 2025)                 |
| **Booking.com**     | En place (25% commission)                           |
| **Airbnb**          | En attente de setup                                 |
| **Expedia Partner** | En attente de setup                                 |
| **Note client**     | 9.3/10 sur Booking — Excellente                     |
| **Staffing**        | Difficulté à trouver employés qualifiés (luxe)      |
| **Promotions**      | 5 actives (10-15%) — Audit réalisé le 20 déc        |

### 4.2 Questions Clés pour RDV ⏳ (Lundi 22 déc 10h)

**Besoins à prioriser :**

| #   | Besoin potentiel                                              | Priorité à valider |
| --- | ------------------------------------------------------------- | ------------------ |
| 1   | Gestion plateformes de réservation (Booking, Airbnb, Expedia) | ❓                 |
| 2   | Augmenter le taux d'occupation                                | ❓                 |
| 3   | Grille tarifaire à stabiliser / adapter à la concurrence      | ❓                 |
| 4   | Top SEO sur "Villa Thaifa"                                    | ❓                 |
| 5   | Site web de qualité                                           | ❓                 |
| 6   | Prix dynamiques (saison, occupation, concurrence)             | ❓                 |
| 7   | Logiciel de gestion (PMS)                                     | ❓                 |

**Autres questions :**

| Question              | Réponse attendue          |
| --------------------- | ------------------------- |
| Budget approximatif ? | À déterminer              |
| Timeline souhaitée ?  | "Le plus tôt possible"    |
| Vision long terme ?   | Garder / Vendre / Louer ? |

### 4.3 Douleurs Principales

| Douleur               | Impact                                                     | Piste de solution                     |
| --------------------- | ---------------------------------------------------------- | ------------------------------------- |
| **Recrutement**       | Dur de trouver employés qualifiés pour positionnement luxe | Formation ? Partenariats écoles ?     |
| **Positionnement**    | Volonté de se positionner vraiment luxe (preuves: 9.3/10)  | Pricing premium + communication       |
| **Gestion manuelle**  | Tout dans la tête de M. Thaifa                             | PMS adapté petite structure           |
| **Dépendance OTAs**   | 100% Booking.com actuellement                              | Diversifier (Airbnb, Expedia, direct) |
| **Commission élevée** | 25% Booking (vs 15% standard)                              | Négocier à moyen terme                |

### 4.4 Opportunités Identifiées

**Court terme (Q1 2026) :**

| Opportunité                     | Impact           | Effort | Priorité |
| ------------------------------- | ---------------- | ------ | -------- |
| Configurer pricing HotelRunner  | Revenue immédiat | Faible | 🔴 P0    |
| Setup Airbnb/Expedia            | Diversification  | Moyen  | 🟠 P1    |
| PMS adapté (Hotelogix ou autre) | Efficacité       | Moyen  | 🟠 P1    |
| Automatisation reporting        | Visibilité       | Faible | 🟢 P2    |

**Long terme (2026+) :**

| Opportunité                         | Note                                  |
| ----------------------------------- | ------------------------------------- |
| Site web + Booking engine direct    | Via HotelRunner ? Accès source code ? |
| Jisr l'Mokawala (portail Go Siyaha) | Brief préparé — investigation P3      |
| Vente sans intermédiaire            | M. Thaifa "en a marre de gérer"       |
| Location à société compétente       | Alternative à la vente                |

---

## 5. Analyse Compétitive

### 5.1 Marché Palmeraie

| Segment        | Prix/nuit | Note typique | Caractéristiques                |
| -------------- | --------- | ------------ | ------------------------------- |
| **Standard**   | 80-150€   | 8.0-8.5      | B&B basique, peu de services    |
| **Premium**    | 150-280€  | 8.5-9.0      | Piscine, spa, restaurant        |
| **Luxe**       | 280-500€  | 9.0+         | Suites, expérience exclusive    |
| **Ultra-luxe** | 500€+     | 9.5+         | Villas privées, personnel dédié |

### 5.2 Positionnement Villa Thaifa

| Critère      | Villa Thaifa        | Position          |
| ------------ | ------------------- | ----------------- |
| **Prix**     | 160-600€            | Premium → Luxe    |
| **Note**     | 9.3/10              | Top 10% Palmeraie |
| **Chambres** | 12                  | Taille moyenne    |
| **Services** | Piscine, spa, resto | Premium complet   |

**Avantage concurrentiel :** Note exceptionnelle (9.3) + positionnement calme Palmeraie

→ Benchmark détaillé : recherche en cours

---

## 6. Baseline Financière

### 6.1 Modèles de Revenus

| Taux occupation | Nuitées/an | Revenue brut | Après commission (25%) |
| --------------- | ---------- | ------------ | ---------------------- |
| **50%**         | 2,190      | ~€438,000    | ~€328,500              |
| **70%**         | 3,066      | ~€613,200    | ~€459,900              |
| **90%**         | 3,942      | ~€788,400    | ~€591,300              |

_Base: 12 chambres × 365 jours × prix moyen ~200€_

### 6.2 Impact Commission

| OTA                      | Commission | Sur €100 brut | Net  |
| ------------------------ | ---------- | ------------- | ---- |
| **Booking.com actuel**   | 25%        | -€25          | €75  |
| **Booking.com standard** | 15%        | -€15          | €85  |
| **Airbnb**               | ~15%       | -€15          | €85  |
| **Direct**               | 0%         | €0            | €100 |

**Opportunité :** Réduire dépendance Booking + négocier commission

### 6.3 Objectifs RevPAR

| KPI            | Actuel      | Cible Q1 2026 | Cible 2026 |
| -------------- | ----------- | ------------- | ---------- |
| **Occupation** | ~50% (peak) | 60%           | 70%        |
| **ADR**        | ~€200       | €220          | €250       |
| **RevPAR**     | ~€100       | €132          | €175       |

---

## 7. Stack Technique

### 7.1 État Actuel

| Composant           | Solution              | Status                    |
| ------------------- | --------------------- | ------------------------- |
| **PMS**             | Aucun (manuel)        | ❌ Critique               |
| **Channel Manager** | HotelRunner           | ✅ Actif                  |
| **OTA principale**  | Booking.com           | ✅ Actif (25% commission) |
| **OTA secondaires** | Airbnb, Expedia       | ⏳ En attente             |
| **Site web**        | Inexistant ou basique | ❓ À vérifier             |
| **Booking engine**  | Aucun                 | ⏳ HotelRunner ?          |

### 7.2 Contraintes & Défis

- Pas de formation tech M. Thaifa (78 ans)
- Besoin solution simple, intuitive
- Pas de staff IT dédié
- Budget à définir

### 7.3 Intégrations Proposées

| Solution                      | Fonction                                  | Priorité           |
| ----------------------------- | ----------------------------------------- | ------------------ |
| **Hotelogix** (ou équivalent) | PMS adapté petite structure               | P1                 |
| **HotelRunner**               | Channel Manager + Booking engine          | P0 (en cours)      |
| **Jisr l'Mokawala**           | Réservations directes (portail GO Siyaha) | P3 (investigation) |

---

## 8. Risques & Mitigation

| Risque                     | Probabilité | Impact | Mitigation                    |
| -------------------------- | ----------- | ------ | ----------------------------- |
| **Dépendance Booking.com** | Haute       | Élevé  | Diversifier OTAs + direct     |
| **Staffing qualifié**      | Haute       | Moyen  | Partenariats formation        |
| **Adoption technologique** | Moyenne     | Moyen  | Solutions simples, formation  |
| **Saisonnalité**           | Haute       | Moyen  | Pricing dynamique, événements |
| **Fatigue propriétaire**   | Moyenne     | Élevé  | Délégation progressive        |

---

## 9. Métriques de Succès

### 9.1 KPIs à Établir au RDV

| KPI                     | Baseline | Cible 6 mois   | Comment mesurer               |
| ----------------------- | -------- | -------------- | ----------------------------- |
| Commission moyenne      | 25%      | 20%            | Négociation + diversification |
| % réservations directes | 0%       | 10%            | Booking engine + SEO          |
| Taux occupation annuel  | ~50%     | 60%            | HotelRunner reports           |
| Note Booking            | 9.3/10   | Maintenir >9.0 | Booking dashboard             |
| Staff turnover          | ❓       | Réduire        | À définir avec M. Thaifa      |

### 9.2 Critères de Succès Mission

| Critère          | Définition                                       |
| ---------------- | ------------------------------------------------ |
| **Opérationnel** | Toutes réservations assignées, pricing configuré |
| **Technique**    | HotelRunner fonctionnel, OTAs synchronisées      |
| **Stratégique**  | Plan 2026 validé, budget approuvé                |
| **Relationnel**  | Confiance M. Thaifa établie                      |

---

## 10. Engagement & Timeline

### 10.1 Historique

| Date       | Événement                           | Status      |
| ---------- | ----------------------------------- | ----------- |
| 2025-12-19 | Premier contact                     | ✅ Done     |
| 2025-12-20 | Audit promotions + pricing strategy | ✅ Done     |
| 2025-12-20 | Setup HotelRunner (partiel)         | ⏳ En cours |

### 10.2 Prochaines Étapes

| Date               | Événement                     | Objectif                          |
| ------------------ | ----------------------------- | --------------------------------- |
| **2025-12-22 10h** | RDV découverte M. Thaifa      | Valider besoins, budget, timeline |
| 2025-12-22 PM      | Documenter décisions          | Update PROFILE.md                 |
| 2025-12-23-24      | Proposition commerciale       | Créer devis                       |
| 2025-12-25-28      | Assigner réservations         | 10 chambres à assigner            |
| 2026-01            | Investigation Jisr l'Mokawala | Faisabilité                       |

### 10.3 Milestones Proposés

| Milestone               | Date cible  | Livrables                          |
| ----------------------- | ----------- | ---------------------------------- |
| **M1: Setup complet**   | 31 déc 2025 | HotelRunner configuré, prix actifs |
| **M2: Diversification** | 31 jan 2026 | Airbnb + Expedia actifs            |
| **M3: PMS**             | 28 fév 2026 | Solution PMS choisie + déployée    |
| **M4: Direct booking**  | 31 mar 2026 | Booking engine + SEO basique       |

---

## 11. Opportunités Stratégiques (Long Terme)

### Vision 2026+

| Scénario         | Description                   | Probabilité |
| ---------------- | ----------------------------- | ----------- |
| **Optimisation** | M. Thaifa garde, on optimise  | Haute       |
| **Délégation**   | Location à société compétente | Moyenne     |
| **Exit**         | Vente directe (sans samsar)   | Faible      |

### Leviers de Croissance

1. **Réservations directes** — Réduire commission OTAs
2. **Upselling** — Spa, transport, excursions
3. **Événements** — Mariages, retraites corporate
4. **Fidélisation** — Programme retours clients

---

## 12. Références

### 12.1 Documents Liés

| Dossier                        | Contenu                  |
| ------------------------------ | ------------------------ |
| `data/communication/whatsapp/` | Messages prêts à envoyer |
| `archive/2025/Q4/`             | Archives et historiques  |

### 12.2 État Opérationnel (SSOT)

| Fichier                            | Contenu                                |
| ---------------------------------- | -------------------------------------- |
| `data/specs/hotel/rooms.md`        | Chambres, pricing, mapping HotelRunner |
| `data/specs/hotel/reservations.md` | Réservations confirmées                |
| `data/specs/promotions/current.md` | Promotions actives                     |

### 12.3 Documentation

| Fichier                   | Contenu                             |
| ------------------------- | ----------------------------------- |
| `docs/lessons-learned.md` | 3 patterns communication documentés |
| `CLAUDE.md`               | Instructions agents IA              |

### 12.4 Ressources Secteur

- [Hotelogix - 8 Must-Have PMS Reports](https://blog.hotelogix.com/hotel-reservation-report/)
- [Villa Palmeraie Marrakech - Booking.com](https://www.booking.com/hotel/ma/villa-palmeraie-marrakech-marrakech1.html)
- [Villa Al Assala Palmeraie - Booking.com](https://www.booking.com/hotel/ma/villa-al-assala-palmeraie.html)

---

## Glossaire Sectoriel

| Terme               | Définition                                                        |
| ------------------- | ----------------------------------------------------------------- |
| **PMS**             | Property Management System — Logiciel de gestion hôtelière        |
| **OTA**             | Online Travel Agency — Plateformes type Booking, Airbnb, Expedia  |
| **Channel Manager** | Outil synchronisant disponibilités sur toutes les OTAs            |
| **ADR**             | Average Daily Rate — Revenu moyen par chambre vendue              |
| **RevPAR**          | Revenue Per Available Room — Revenu par chambre disponible        |
| **SSOT**            | Single Source of Truth — Source unique de vérité pour les données |

---

## Notes Internes

```
[2025-12-19] Création dossier client. RDV lundi à confirmer.
[2025-12-20] Optimisation profil v1 via /elevate.
[2025-12-20] Réorganisation profil v2 — Structure 12 sections.
             Backup: .backup/PROFILE-2025-12-20-v2-before-reorg.md
```

---

## See Also

- [../STAKEHOLDERS.md](../STAKEHOLDERS.md) - Quick reference for all stakeholders
- [OMAR-EL-MOUNTASSIR.md](./OMAR-EL-MOUNTASSIR.md) - Consultant profile
- [../INDEX.md](../INDEX.md) - Documentation navigation guide

---

_Detailed client profile - Part of docs/leadership/profiles/_
_Original: legacy/archive_v1/admin/client/PROFILE.md (2025-12-20)_
_Refactored: 2026-01-24 - Moved to new structure, cross-references added_

### Omar El Mountassir — Admin/Consultant

> **Role**: CEO & Leader - Villa Thaifa Digital Transformation Project
> **Last Updated**: 2026-01-24

---

## 🎯 Overview

**Name**: Omar El Mountassir
**Role**: Digital Transformation Consultant & Project Leader
**Client**: Said Thaifa (Villa Thaifa owner)
**Project Start**: December 2025
**Project Type**: Digital Transformation & Operational Optimization

---

## 📧 Contact Information

| Field     | Value                           |
| --------- | ------------------------------- |
| **Email** | omar@el-mountassir.com          |
| **Role**  | CEO, Strategist, Project Leader |

---

## 👔 Professional Role

### Primary Responsibilities

1. **Strategic Leadership**
   - Overall project vision and direction
   - Client relationship management with Said Thaifa
   - Budget and timeline approval
   - Final decision authority on all deliverables

2. **Team Management**
   - Leadership of 17 specialized AI agents
   - Claude (CTO/Architect) supervision
   - Agent performance monitoring
   - Workflow optimization

3. **Client Interface**
   - Main point of contact with Said Thaifa
   - Requirements gathering and validation
   - Progress reporting
   - Decision approval and implementation

4. **Quality Assurance**
   - Review and validation of all platform operations
   - Security and compliance oversight
   - Documentation standards enforcement
   - Deliverable quality control

---

## 🏗️ Project Context

### Mission

Transform Villa Thaifa's operations from fully manual (everything in Said's head) to digitally optimized with:

- Professional PMS (Property Management System)
- Multi-channel distribution (Booking, Airbnb, Expedia)
- Automated pricing and revenue optimization
- Reduced operational burden on 78-year-old owner

### Approach

**Philosophy**: "AI-First"

- AI agents are co-workers, not tools
- Autonomous execution with human supervision
- Systematic documentation and handovers
- Continuous improvement through agent collaboration

**Methodology**: Scout → Rapport → Questions → Action

- Never ask questions without first reporting findings
- Always provide context before requesting information
- Validate before executing
- Document everything

---

## 🔐 Platform Access

### Admin Accounts (Primary Use)

**HotelRunner**:

- Email: omar@el-mountassir.com
- Role: Admin/Manager
- Purpose: Daily operations, configuration, management

**Booking.com**:

- Email: omar@el-mountassir.com
- Role: Admin/Manager
- Purpose: Property management, updates, analytics

### Owner Accounts (Reference Only)

**Said Thaifa's Accounts**:

- HotelRunner: said_thaifa@hotmail.fr
- Booking.com: said_thaifa@hotmail.fr

**⚠️ CRITICAL**: Use Said's accounts ONLY with explicit approval from Omar

---

## 🎯 Decision Authority

### Decision Hierarchy

**Strategic Decisions** (Vision, Budget, Exit Strategy):

```
Omar analyzes & recommends → Said decides → Omar executes
```

**Operational Decisions** (Pricing, OTAs, Setup):

```
AI agents analyze → Claude validates → Omar approves → (Said informed) → Execute
```

**Technical Decisions** (Architecture, Stack, Tools):

```
Claude proposes → Omar validates → Execute autonomously
```

### Approval Requirements

**Omar Must Approve**:

- ✅ All platform operations (pricing, reservations, availability)
- ✅ Client communications (Said Thaifa)
- ✅ Budget allocations
- ✅ Timeline changes
- ✅ Vendor selection (PMS, tools, services)

**Omar Can Delegate** (to Claude/Agents):

- ✅ Research and analysis
- ✅ Documentation
- ✅ Technical implementation
- ✅ Reporting and monitoring
- ✅ Non-critical automation

**Omar Does NOT Handle** (Said's Domain):

- ❌ Guest relations (direct)
- ❌ On-site operations
- ❌ Staff management
- ❌ Final strategic vision

---

## 🤝 Relationship with Said Thaifa

### Communication Protocol

**Tone**: Professional, respectful, consultative
**Method**: WhatsApp preferred (Said's preference)
**Pattern**: Scout → Rapport → Questions → Action

**Golden Rule**: Always report findings BEFORE asking for additional information

### Roles Clarity

| Aspect         | Said (Client) | Omar (Consultant) |
| -------------- | ------------- | ----------------- |
| **Ownership**  | 100%          | 0% (consultant)   |
| **Vision**     | Decides       | Advises           |
| **Execution**  | Delegates     | Manages           |
| **Operations** | Informs       | Implements        |
| **Budget**     | Approves      | Proposes          |
| **Success**    | Benefits      | Delivers          |

---

## 🚀 Project Objectives & KPIs

### Short Term (Q1 2026)

- ✅ HotelRunner fully configured with accurate pricing
- ✅ Airbnb and Expedia channels active
- ✅ PMS selected and implemented
- ✅ Commission reduced from 25% to 20%
- ✅ Operational burden reduced 50%

### Medium Term (2026)

- ✅ 70% occupancy rate achieved
- ✅ 10% direct bookings (bypass OTAs)
- ✅ Dynamic pricing implemented
- ✅ Stable qualified staff in place
- ✅ Automated reporting systems

### Long Term (Beyond 2026)

Support Said's chosen path:

- **Option A**: Delegation to professional management company
- **Option B**: Direct sale (no intermediary)
- **Option C**: Continued optimization with tech support

### Success Metrics

| KPI                    | Baseline    | Target        |
| ---------------------- | ----------- | ------------- |
| **Operational Load**   | 100% manual | -50%          |
| **Revenue**            | Current     | +20%          |
| **OTA Commission**     | 25%         | 20%           |
| **Booking.com Rating** | 9.3/10      | Maintain 9.0+ |
| **Direct Bookings**    | 0%          | 10%           |
| **Occupancy Rate**     | ~50%        | 70%           |

---

## 🛠️ Technical Leadership

### Team Structure

**Under Omar's Leadership**:

1. **Claude** (CTO/Architect)
   - Technical architecture
   - Agent coordination
   - System design

2. **17 AI Agents** (Specialized Workforce)
   - 4 Operations agents
   - 4 Technical agents
   - 7 Meta agents
   - 2 Hospitality agents

**Reference**: [`docs/leadership/TEAM.md`](../TEAM.md)

### Workflow Management

- **Daily**: Agent outputs review
- **Weekly**: Progress sync with Claude
- **Bi-weekly**: Client update to Said
- **Monthly**: KPI review and adjustment

---

## 📋 Current Project Phase

**Phase**: 1 - Stabilization & Cleanup
**Status**: Active
**Focus**:

- Rescue and migrate data
- Fix platform configurations
- Establish baseline systems
- Create solid documentation foundation

**Roadmap**: [`ROADMAP.md`](../../ROADMAP.md)
**Active Tasks**: [`tasks/active.md`](../../tasks/active.md)

---

## 🔒 Security & Compliance

### Access Control

**Omar's Responsibility**:

- Secure credential management
- Platform access governance
- Agent permission levels
- Data privacy compliance

**Never Share**:

- ❌ Platform passwords
- ❌ API keys
- ❌ Client personal data
- ❌ Financial information

### Audit Trail

All operations must be:

- ✅ Documented in git commits
- ✅ Logged in appropriate tools
- ✅ Reviewable by Omar
- ✅ Traceable to specific agent/action

---

## 📚 Work Style & Preferences

### Decision Making

- **Data-driven**: Prefer metrics over opinions
- **Systematic**: Process > ad-hoc solutions
- **Documented**: Everything must be written
- **Validated**: Double-check before execution

### Communication Style

- **Concise**: Clear, to the point
- **Structured**: Organized information
- **Actionable**: Always include next steps
- **Transparent**: No surprises

### Quality Standards

- **Excellence**: Aim for 9.0+ quality (like Said's rating)
- **Reliability**: Systems must work consistently
- **Maintainability**: Future agents can understand
- **Scalability**: Can grow with business

---

## 🎓 Learning & Adaptation

### Continuous Improvement

Omar expects:

- Regular agent performance reviews
- Process optimization suggestions
- Technology updates consideration
- Best practices research

### Feedback Loops

- Agents report findings and blockers
- Claude proposes architecture improvements
- Omar validates and approves changes
- Documentation updated accordingly

---

## 🚨 For AI Agents: Working with Omar

### What Omar Expects

1. **Autonomous Execution**
   - Don't ask for every small decision
   - Use judgment within your domain
   - But validate critical operations

2. **Clear Communication**
   - Summary upfront, details after
   - Highlight blockers immediately
   - Propose solutions, not just problems

3. **Documented Work**
   - Git commits for all changes
   - Handovers when switching context
   - Decisions logged with rationale

4. **Quality Focus**
   - Double-check before executing
   - Test when possible
   - Never guess - research or ask

### When to Escalate to Omar

**Always Escalate**:

- ❗ Platform operations (pricing, availability, reservations)
- ❗ Client communication with Said
- ❗ Budget/financial decisions
- ❗ Timeline changes
- ❗ Critical errors or incidents

**Can Proceed Autonomously**:

- ✅ Research and analysis
- ✅ Documentation updates
- ✅ Internal tool usage
- ✅ Non-critical bug fixes

### Communication Format

**Good**:

```
Subject: [Agent-Name] Brief summary of topic

Context: What led to this situation
Finding: What was discovered
Recommendation: Proposed action
Request: What you need from Omar

Next: What happens after approval
```

**Bad**:

```
"Hey, what should I do about X?"
(No context, no research, no proposal)
```

---

## 📞 Contact & Availability

**Email**: omar@el-mountassir.com

**Response Time**:

- Critical issues: Within 2 hours
- Standard requests: Within 24 hours
- Research/analysis: As appropriate

**Escalation Path**:

1. Agent identifies issue
2. Claude (CTO) reviews
3. Omar decides
4. Execution proceeds

---

## 🔗 Related Documentation

| Document                                | Purpose                                        |
| --------------------------------------- | ---------------------------------------------- |
| [`STAKEHOLDERS.md`](../STAKEHOLDERS.md) | Overview of all stakeholders and relationships |
| [`SAID-THAIFA.md`](./SAID-THAIFA.md)    | Detailed client profile                        |
| [`TEAM.md`](../TEAM.md)                 | AI agent team structure                        |
| [`ROADMAP.md`](../../ROADMAP.md)        | Project roadmap and milestones                 |

---

_Profile created: 2026-01-24_
_Last updated: 2026-01-24_
_Document owner: Omar El Mountassir_

---

## Detailed Client Profile

> **Status:** Lead (RDV planifié)
> **Priority:** HIGH
> **Next:** RDV découverte — Lundi 22 décembre 2025, 10h (Done)
> **Created:** 2025-12-19
> **Last Updated:** 2025-12-20

---

## 1. Snapshot Exécutif

### KPIs Clés

| Métrique               | Valeur                              | Note                           |
| ---------------------- | ----------------------------------- | ------------------------------ |
| **Chambres**           | 12                                  | 8 types sur Booking.com        |
| **Note Booking**       | 9.3/10 (80 avis)                    | "Wonderful"                    |
| **Commission Booking** | 25%                                 | Élevée (standard = 15%)        |
| **PMS**                | Aucun                               | Tout dans la tête de M. Thaifa |
| **Channel Manager**    | HotelRunner                         | Actif depuis 2025-12           |
| **OTAs**               | Booking ✅ / Airbnb ⏳ / Expedia ⏳ | En cours de setup              |

### Scores Détaillés Booking.com

| Catégorie                | Score | Niveau       |
| ------------------------ | ----- | ------------ |
| **Staff**                | 9.7   | Exceptionnel |
| **Propreté**             | 9.4   | Excellent    |
| **Confort**              | 9.4   | Excellent    |
| **Équipements**          | 9.3   | Excellent    |
| **Rapport qualité/prix** | 8.9   | Très bon     |
| **WiFi**                 | 8.8   | Très bon     |
| **Localisation**         | 8.2   | Bon          |
| **Petit-déjeuner**       | 10    | Parfait      |

> **Point fort majeur** : Staff noté 9.7/10 et petit-déjeuner parfait 10/10

### État Opérationnel Actuel

| Métrique                        | Valeur     |
| ------------------------------- | ---------- |
| **Réservations confirmées**     | 11         |
| **Revenue prévu**               | €8,008.85  |
| **Occupation peak (29-31 déc)** | 50% (6/12) |
| **Prix configurés HotelRunner** | 0/9 types  |
| **Promotions actives Booking**  | 5 (10-15%) |

→ Voir `data/specs/` pour détails opérationnels

---

## 2. Contact & Communication

### 2.1 Contact Principal

| Champ         | Valeur                   |
| ------------- | ------------------------ |
| **Nom**       | Said Thaifa              |
| **Âge**       | 78 ans                   |
| **Email**     | <said_thaifa@hotmail.fr> |
| **Email**     | <saidthaifa@gmail.com>   |
| **Téléphone** | +212 661-134194          |
| **WhatsApp**  | +212 661-134194          |

**Background professionnel** :

- Propriétaire et hôte de Villa Thaifa (avec son épouse Nezha)
- CEO / Agent immobilier à Marrakech
- Spécialités : ventes, achats, locations saisonnières
- Réputation : accueil chaleureux, fait que les clients se sentent "comme chez eux"

### 2.2 Protocole de Communication

| Règle             | Détail                                |
| ----------------- | ------------------------------------- |
| **Ton**           | Vouvoiement obligatoire — Formelle    |
| **Registre**      | Client senior — Respect sans rigidité |
| **Canal préféré** | WhatsApp (confirmé)                   |

### 2.3 Pattern de Communication

```text
1. SCOUT    → Explorer, vérifier la faisabilité
2. RAPPORT  → Tenir le client informé des découvertes
3. QUESTIONS → Demander les infos manquantes (avec contexte)
4. ACTION   → Exécuter quand tout est clair
```

> **Règle d'or** : Ne jamais demander des infos sans d'abord faire un rapport de ce qu'on a découvert.

→ Voir `docs/lessons-learned.md` pour les patterns documentés

---

## 3. Établissement

### 3.1 Informations Générales

| Champ          | Valeur                                      |
| -------------- | ------------------------------------------- |
| **Nom**        | Villa Thaifa (parfois "Villa Thaifa & SPA") |
| **Type**       | Maison d'hôtes de charme / B&B (4★)         |
| **Adresse**    | Route de Fès, Km 12                         |
| **Zone**       | Palmeraie / Ouled Jelal (12-14 km centre)   |
| **Ville**      | Marrakech, Maroc                            |
| **Chambres**   | 12                                          |
| **Rénovation** | Récemment rénovée                           |

### 3.2 Équipements & Services

| Catégorie      | Détails                                                    |
| -------------- | ---------------------------------------------------------- |
| **Détente**    | Piscine infinity (ouverte toute l'année), jardin, solarium |
| **Bien-être**  | Spa/Hammam, massages (supplément)                          |
| **Restaurant** | "Thaifa's restaurant" — Cuisine marocaine                  |
| **Cuisine**    | Marocaine (halal, végétarien) — "Best tagine in Morocco"   |
| **Chambres**   | Climatisation, chauffage, TV satellite, Wi-Fi, terrasse    |
| **Services**   | Parking gratuit, navette aéroport, location voiture        |
| **Sécurité**   | 24h/24, CCTV, coffre-fort, alarme                          |
| **Langues**    | Arabe, Anglais, Français, Néerlandais                      |

### Petit-déjeuner (Score 10/10)

| Attribut     | Valeur                                                                         |
| ------------ | ------------------------------------------------------------------------------ |
| **Prix**     | MAD 160.90/personne                                                            |
| **Horaires** | 08:30 - 11:00                                                                  |
| **Type**     | Continental, Halal                                                             |
| **Menu**     | Viennoiseries, pain, pancakes, oeufs, fromage, spécialités locales, confitures |

### 3.3 Positionnement & Réputation

| Aspect                 | Valeur                                                                  |
| ---------------------- | ----------------------------------------------------------------------- |
| **Gamme tarifaire**    | 160-600 €/nuit (selon type)                                             |
| **Réputation**         | Très bonne (9.3/10 Booking)                                             |
| **Points forts**       | Calme, jardins, piscine infinity, accueil chaleureux ("comme chez soi") |
| **Atout localisation** | Calme et paisible, loin du bruit de la ville (14 km du centre)          |

→ Voir `data/specs/hotel/rooms.md` pour le détail des chambres et pricing

---

## 4. Contexte Business

### 4.1 Faits Confirmés ✅

| Fait                | Détail                                              |
| ------------------- | --------------------------------------------------- |
| **PMS actuel**      | Aucun — Tout se fait dans la tête de M. Said Thaifa |
| **Channel Manager** | HotelRunner (actif depuis déc 2025)                 |
| **Booking.com**     | En place (25% commission)                           |
| **Airbnb**          | En attente de setup                                 |
| **Expedia Partner** | En attente de setup                                 |
| **Note client**     | 9.3/10 sur Booking — Excellente                     |
| **Staffing**        | Difficulté à trouver employés qualifiés (luxe)      |
| **Promotions**      | 5 actives (10-15%) — Audit réalisé le 20 déc        |

### 4.2 Questions Clés pour RDV ⏳ (Lundi 22 déc 10h)

**Besoins à prioriser :**

| #   | Besoin potentiel                                              | Priorité à valider |
| --- | ------------------------------------------------------------- | ------------------ |
| 1   | Gestion plateformes de réservation (Booking, Airbnb, Expedia) | ❓                 |
| 2   | Augmenter le taux d'occupation                                | ❓                 |
| 3   | Grille tarifaire à stabiliser / adapter à la concurrence      | ❓                 |
| 4   | Top SEO sur "Villa Thaifa"                                    | ❓                 |
| 5   | Site web de qualité                                           | ❓                 |
| 6   | Prix dynamiques (saison, occupation, concurrence)             | ❓                 |
| 7   | Logiciel de gestion (PMS)                                     | ❓                 |

**Autres questions :**

| Question              | Réponse attendue          |
| --------------------- | ------------------------- |
| Budget approximatif ? | À déterminer              |
| Timeline souhaitée ?  | "Le plus tôt possible"    |
| Vision long terme ?   | Garder / Vendre / Louer ? |

### 4.3 Douleurs Principales

| Douleur               | Impact                                                     | Piste de solution                     |
| --------------------- | ---------------------------------------------------------- | ------------------------------------- |
| **Recrutement**       | Dur de trouver employés qualifiés pour positionnement luxe | Formation ? Partenariats écoles ?     |
| **Positionnement**    | Volonté de se positionner vraiment luxe (preuves: 9.3/10)  | Pricing premium + communication       |
| **Gestion manuelle**  | Tout dans la tête de M. Thaifa                             | PMS adapté petite structure           |
| **Dépendance OTAs**   | 100% Booking.com actuellement                              | Diversifier (Airbnb, Expedia, direct) |
| **Commission élevée** | 25% Booking (vs 15% standard)                              | Négocier à moyen terme                |

### 4.4 Opportunités Identifiées

**Court terme (Q1 2026) :**

| Opportunité                     | Impact           | Effort | Priorité |
| ------------------------------- | ---------------- | ------ | -------- |
| Configurer pricing HotelRunner  | Revenue immédiat | Faible | 🔴 P0    |
| Setup Airbnb/Expedia            | Diversification  | Moyen  | 🟠 P1    |
| PMS adapté (Hotelogix ou autre) | Efficacité       | Moyen  | 🟠 P1    |
| Automatisation reporting        | Visibilité       | Faible | 🟢 P2    |

**Long terme (2026+) :**

| Opportunité                         | Note                                  |
| ----------------------------------- | ------------------------------------- |
| Site web + Booking engine direct    | Via HotelRunner ? Accès source code ? |
| Jisr l'Mokawala (portail Go Siyaha) | Brief préparé — investigation P3      |
| Vente sans intermédiaire            | M. Thaifa "en a marre de gérer"       |
| Location à société compétente       | Alternative à la vente                |

---

## 5. Analyse Compétitive

### 5.1 Marché Palmeraie

| Segment        | Prix/nuit | Note typique | Caractéristiques                |
| -------------- | --------- | ------------ | ------------------------------- |
| **Standard**   | 80-150€   | 8.0-8.5      | B&B basique, peu de services    |
| **Premium**    | 150-280€  | 8.5-9.0      | Piscine, spa, restaurant        |
| **Luxe**       | 280-500€  | 9.0+         | Suites, expérience exclusive    |
| **Ultra-luxe** | 500€+     | 9.5+         | Villas privées, personnel dédié |

### 5.2 Positionnement Villa Thaifa

| Critère      | Villa Thaifa        | Position          |
| ------------ | ------------------- | ----------------- |
| **Prix**     | 160-600€            | Premium → Luxe    |
| **Note**     | 9.3/10              | Top 10% Palmeraie |
| **Chambres** | 12                  | Taille moyenne    |
| **Services** | Piscine, spa, resto | Premium complet   |

**Avantage concurrentiel :** Note exceptionnelle (9.3) + positionnement calme Palmeraie

→ Benchmark détaillé : recherche en cours

---

## 6. Baseline Financière

### 6.1 Modèles de Revenus

| Taux occupation | Nuitées/an | Revenue brut | Après commission (25%) |
| --------------- | ---------- | ------------ | ---------------------- |
| **50%**         | 2,190      | ~€438,000    | ~€328,500              |
| **70%**         | 3,066      | ~€613,200    | ~€459,900              |
| **90%**         | 3,942      | ~€788,400    | ~€591,300              |

_Base: 12 chambres × 365 jours × prix moyen ~200€_

### 6.2 Impact Commission

| OTA                      | Commission | Sur €100 brut | Net  |
| ------------------------ | ---------- | ------------- | ---- |
| **Booking.com actuel**   | 25%        | -€25          | €75  |
| **Booking.com standard** | 15%        | -€15          | €85  |
| **Airbnb**               | ~15%       | -€15          | €85  |
| **Direct**               | 0%         | €0            | €100 |

**Opportunité :** Réduire dépendance Booking + négocier commission

### 6.3 Objectifs RevPAR

| KPI            | Actuel      | Cible Q1 2026 | Cible 2026 |
| -------------- | ----------- | ------------- | ---------- |
| **Occupation** | ~50% (peak) | 60%           | 70%        |
| **ADR**        | ~€200       | €220          | €250       |
| **RevPAR**     | ~€100       | €132          | €175       |

---

## 7. Stack Technique

### 7.1 État Actuel

| Composant           | Solution              | Status                    |
| ------------------- | --------------------- | ------------------------- |
| **PMS**             | Aucun (manuel)        | ❌ Critique               |
| **Channel Manager** | HotelRunner           | ✅ Actif                  |
| **OTA principale**  | Booking.com           | ✅ Actif (25% commission) |
| **OTA secondaires** | Airbnb, Expedia       | ⏳ En attente             |
| **Site web**        | Inexistant ou basique | ❓ À vérifier             |
| **Booking engine**  | Aucun                 | ⏳ HotelRunner ?          |

### 7.2 Contraintes & Défis

- Pas de formation tech M. Thaifa (78 ans)
- Besoin solution simple, intuitive
- Pas de staff IT dédié
- Budget à définir

### 7.3 Intégrations Proposées

| Solution                      | Fonction                                  | Priorité           |
| ----------------------------- | ----------------------------------------- | ------------------ |
| **Hotelogix** (ou équivalent) | PMS adapté petite structure               | P1                 |
| **HotelRunner**               | Channel Manager + Booking engine          | P0 (en cours)      |
| **Jisr l'Mokawala**           | Réservations directes (portail GO Siyaha) | P3 (investigation) |

---

## 8. Risques & Mitigation

| Risque                     | Probabilité | Impact | Mitigation                    |
| -------------------------- | ----------- | ------ | ----------------------------- |
| **Dépendance Booking.com** | Haute       | Élevé  | Diversifier OTAs + direct     |
| **Staffing qualifié**      | Haute       | Moyen  | Partenariats formation        |
| **Adoption technologique** | Moyenne     | Moyen  | Solutions simples, formation  |
| **Saisonnalité**           | Haute       | Moyen  | Pricing dynamique, événements |
| **Fatigue propriétaire**   | Moyenne     | Élevé  | Délégation progressive        |

---

## 9. Métriques de Succès

### 9.1 KPIs à Établir au RDV

| KPI                     | Baseline | Cible 6 mois   | Comment mesurer               |
| ----------------------- | -------- | -------------- | ----------------------------- |
| Commission moyenne      | 25%      | 20%            | Négociation + diversification |
| % réservations directes | 0%       | 10%            | Booking engine + SEO          |
| Taux occupation annuel  | ~50%     | 60%            | HotelRunner reports           |
| Note Booking            | 9.3/10   | Maintenir >9.0 | Booking dashboard             |
| Staff turnover          | ❓       | Réduire        | À définir avec M. Thaifa      |

### 9.2 Critères de Succès Mission

| Critère          | Définition                                       |
| ---------------- | ------------------------------------------------ |
| **Opérationnel** | Toutes réservations assignées, pricing configuré |
| **Technique**    | HotelRunner fonctionnel, OTAs synchronisées      |
| **Stratégique**  | Plan 2026 validé, budget approuvé                |
| **Relationnel**  | Confiance M. Thaifa établie                      |

---

## 10. Engagement & Timeline

### 10.1 Historique

| Date       | Événement                           | Status      |
| ---------- | ----------------------------------- | ----------- |
| 2025-12-19 | Premier contact                     | ✅ Done     |
| 2025-12-20 | Audit promotions + pricing strategy | ✅ Done     |
| 2025-12-20 | Setup HotelRunner (partiel)         | ⏳ En cours |

### 10.2 Prochaines Étapes

| Date               | Événement                     | Objectif                          |
| ------------------ | ----------------------------- | --------------------------------- |
| **2025-12-22 10h** | RDV découverte M. Thaifa      | Valider besoins, budget, timeline |
| 2025-12-22 PM      | Documenter décisions          | Update PROFILE.md                 |
| 2025-12-23-24      | Proposition commerciale       | Créer devis                       |
| 2025-12-25-28      | Assigner réservations         | 10 chambres à assigner            |
| 2026-01            | Investigation Jisr l'Mokawala | Faisabilité                       |

### 10.3 Milestones Proposés

| Milestone               | Date cible  | Livrables                          |
| ----------------------- | ----------- | ---------------------------------- |
| **M1: Setup complet**   | 31 déc 2025 | HotelRunner configuré, prix actifs |
| **M2: Diversification** | 31 jan 2026 | Airbnb + Expedia actifs            |
| **M3: PMS**             | 28 fév 2026 | Solution PMS choisie + déployée    |
| **M4: Direct booking**  | 31 mar 2026 | Booking engine + SEO basique       |

---

## 11. Opportunités Stratégiques (Long Terme)

### Vision 2026+

| Scénario         | Description                   | Probabilité |
| ---------------- | ----------------------------- | ----------- |
| **Optimisation** | M. Thaifa garde, on optimise  | Haute       |
| **Délégation**   | Location à société compétente | Moyenne     |
| **Exit**         | Vente directe (sans samsar)   | Faible      |

### Leviers de Croissance

1. **Réservations directes** — Réduire commission OTAs
2. **Upselling** — Spa, transport, excursions
3. **Événements** — Mariages, retraites corporate
4. **Fidélisation** — Programme retours clients

---

## 12. Références

### 12.1 Documents Liés

| Dossier                        | Contenu                  |
| ------------------------------ | ------------------------ |
| `data/communication/whatsapp/` | Messages prêts à envoyer |
| `archive/2025/Q4/`             | Archives et historiques  |

### 12.2 État Opérationnel (SSOT)

| Fichier                            | Contenu                                |
| ---------------------------------- | -------------------------------------- |
| `data/specs/hotel/rooms.md`        | Chambres, pricing, mapping HotelRunner |
| `data/specs/hotel/reservations.md` | Réservations confirmées                |
| `data/specs/promotions/current.md` | Promotions actives                     |

### 12.3 Documentation

| Fichier                   | Contenu                             |
| ------------------------- | ----------------------------------- |
| `docs/lessons-learned.md` | 3 patterns communication documentés |
| `CLAUDE.md`               | Instructions agents IA              |

### 12.4 Ressources Secteur

- [Hotelogix - 8 Must-Have PMS Reports](https://blog.hotelogix.com/hotel-reservation-report/)
- [Villa Palmeraie Marrakech - Booking.com](https://www.booking.com/hotel/ma/villa-palmeraie-marrakech-marrakech1.html)
- [Villa Al Assala Palmeraie - Booking.com](https://www.booking.com/hotel/ma/villa-al-assala-palmeraie.html)

---

## Glossaire Sectoriel

| Terme               | Définition                                                        |
| ------------------- | ----------------------------------------------------------------- |
| **PMS**             | Property Management System — Logiciel de gestion hôtelière        |
| **OTA**             | Online Travel Agency — Plateformes type Booking, Airbnb, Expedia  |
| **Channel Manager** | Outil synchronisant disponibilités sur toutes les OTAs            |
| **ADR**             | Average Daily Rate — Revenu moyen par chambre vendue              |
| **RevPAR**          | Revenue Per Available Room — Revenu par chambre disponible        |
| **SSOT**            | Single Source of Truth — Source unique de vérité pour les données |

---

## Notes Internes

```
[2025-12-19] Création dossier client. RDV lundi à confirmer.
[2025-12-20] Optimisation profil v1 via /elevate.
[2025-12-20] Réorganisation profil v2 — Structure 12 sections.
             Backup: .backup/PROFILE-2025-12-20-v2-before-reorg.md
```

---

_Profil réorganisé — Structure 12 sections — 2025-12-20_
_Pipeline: `archive/2025/Q4/reports/profile-reorganization/`_

## Overview

| Field        | Value                                               |
| ------------ | --------------------------------------------------- |
| **Client**   | Said Thaifa                                         |
| **Age**      | 78                                                  |
| **Email**    | <said_thaifa@hotmail.fr>                            |
| **Phone**    | +212 661-134194                                     |
| **Language** | Dutch (preferred), French, Arabic (Morrocan Darija) |
| **Location** | Marrakech, Morocco                                  |
| **Business** | Boutique hotel (maison d'hôtes 4★)                  |
| **Property** | 12 rooms                                            |

## Relationship

- **Start Date**: December 2025
- **Last Activity**: January 24, 2026
- **Status**: 🟢 Active

## Projects

| Project             | Directory              | Description                                |
| ------------------- | ---------------------- | ------------------------------------------ |
| property-management | `property-management/` | Hotel management platform (Next.js + APIs) |

## Communication Notes

- Said is 78 years old — patience and clarity are paramount
- Prefers Dutch, comfortable with French
- Primary contact via WhatsApp (+212 661-134194)
- Decisions require time — never rush
- Technical explanations should be visual and simple

## Technical Stack (property-management)

- **Framework**: Next.js
- **APIs**: HotelRunner (HR-v1), Booking.com
- **Automation**: agent-browser (headless browser)
- **Credentials**: `.env.local` (HotelRunner, Booking.com)

## Key Contacts

| Role  | Name | Contact                |
| ----- | ---- | ---------------------- |
| Owner | Said | said_thaifa@hotmail.fr |
| Admin | Omar | (El Mountassir)        |

### Omar — Quick Reference

> **Source of Truth**: `~/omar/identity/profile.md` & `~/omar/identity/preferences.md`
> **Role in This Project**: Founder & Agentic Engineer
> **Last Synced**: 2026-02-09

## Identity

| Field               | Value                                                   |
| ------------------- | ------------------------------------------------------- |
| **Full Name**       | Omar El Mountassir                                      |
| **Company**         | El Mountassir Inc. (Hybrid Carbon-Silicon Organization) |
| **Role**            | Founder, Agentic Engineer                               |
| **Location**        | Marrakech, Morocco                                      |
| **Languages**       | French (primary), English (work), Darija (native)       |
| **Tech Experience** | 29 years                                                |
| **Email**           | omar@el-mountassir.com                                  |

## Professional Identity

- **Agentic Engineer**: Orchestrates intelligences rather than writing code ("I do not code anymore, I orchestrate intelligences").
- **Expert Curator**: (2026-02-07) "My job isn't to be the 'factory worker' any more... my job is to be the expert curator who can spot the genius in all that noise."
- **Thinker & Product Designer**: Strategic, creative, and logical thinking. Designs end-to-end product journeys.

## Critical Preferences for Agents

### Priority Order

1. **Time** — Most precious resource
2. **Health** — Energy to preserve
3. **Money** — Necessary for survival

### Decision Making

- Minimize asks for trivial decisions (drains energy)
- Propose intelligent defaults; act automatically for low-risk choices
- Ask only for important/irreversible decisions

### Communication Style

- **Written**: English in files, French in chat
- **Wants**: Partner, not rubber-stamp; brutal honesty
- **Dislikes**: Verbosity, generic AI tone, passivity
- **Prefers**: Tables, visual hierarchy, direct opinions

### Working With Omar

- **Bad memory**: Needs proactive reminders
- **Divergence pattern**: Tends to jump topics; agents should gently redirect
- **Process before execution**: Standardize approach BEFORE applying to cases
- **CURATOR MODE**: Present OPTIONS (2-4), not single solutions; Omar curates

## Self-Identified Weaknesses (For Agent Compensation)

| Weakness                 | Agent Compensation                                         |
| ------------------------ | ---------------------------------------------------------- |
| Bad memory               | Proactive reminders, explicit references to past decisions |
| Lack of focus discipline | Redirect divergences: "We were on X. Continue or pivot?"   |
| Overwhelm from rush      | When tired, capture everything, execute nothing            |

## Reference

- **Full Profile**: `~/omar/identity/profile.md`
- **Preferences Detail**: `~/omar/identity/preferences.md`
- **Operational Protocol**: `~/omar/operations/protocols/operating-protocol.md`

---

## Strategic Context

### Vision

> **CEO & Leader - Villa Thaifa Project**
> **Date**: 2026-01-15

---

## 🎯 Ma Vision

> "La transformation agentique n'est pas une option, c'est une nécessité."

**Contexte**: The Agentic AI Revolution (2026 - 3ème ère de l'IA)

**Principe**: Les agents IA sont des **co-workers autonomes**, pas des outils.

---

## 🚀 Objectifs Long-Terme

### Pour Villa Thaifa

1. **Excellence Opérationnelle**
   - Automatiser 80% des tâches répétitives
   - Maintenir un taux de satisfaction > 9.5/10
   - Optimiser le revenu through dynamic pricing

2. **Transformation Digitale**
   - Intégration complète de tous les systèmes
   - Données synchronisées en temps réel
   - Visibility totale sur l'activité

3. **Transformation Agentique**
   - 17+ agents IA autonomes
   - Collaboration fluide agents-humains
   - Amélioration continue du système

### Pour Moi (Omar)

1. **Leadership**
   - Vision & stratégie
   - Prise de décision
   - Supervision (pas exécution)

2. **Architecture**
   - Déléguée à Claude (CTO/Architecte)
   - Décisions techniques validées par moi

3. **Libération**
   - Moins de temps sur l'opérationnel
   - Plus de temps sur la stratégie
   - Scalabilité à d'autres projets

---

## 🏆 Succès

Le succès sera atteint quand:

- ✅ Villa Thaifa est un modèle d'excellence opérationnelle
- ✅ Les agents IA travaillent en autonomie à 80%
- ✅ Je peux me concentrer sur la stratégie
- ✅ Le système est prêt à scaler

---

## 📊 Métriques

| Métrique                  | Actuel | Target | Date    |
| ------------------------- | ------ | ------ | ------- |
| Taux automatisation       | TODO%  | 80%    | 2026-06 |
| Satisfaction clients      | 9.3    | 9.5    | 2026-03 |
| Temps Omar (opérationnel) | TODO   | < 20%  | 2026-06 |
| Agents autonomes          | 0%     | 80%    | 2026-06 |

---

**Tags**: `vision` `leadership` `omar` `strategy`

### Priorities

> **Omar El Mountassir - CEO & Leader**
> **Dernière mise à jour**: 2026-01-15

---

## 🎯 P0 (CRITIQUE - Cette semaine)

### 1. Finaliser le système de prompts agentique

- **Statut**: En cours
- **Deadline**: 2026-01-15
- **Responsable**: Claude (CTO)
- **Livrables**:
  - [x] Backup du projet
  - [x] Structure `docs/agents/`
  - [x] `CLAUDE.md` (point d'entrée)
  - [ ] Frontmatter standardisé (17 agents)
  - [ ] Validation et tests

### 2. [Ajouter priorité P0 si nécessaire]

---

## 🔥 P1 (HIGH - Ce mois)

### 1. Système de pricing dynamique

- **Statut**: À démarrer
- **Deadline**: 2026-01-31
- **Agent lead**: `pricing-analyst`
- **Objectif**: Mettre en place le pricing dynamique

### 2. Synchronisation complète Booking.com ↔ HotelRunner

- **Statut**: À démarrer
- **Deadline**: 2026-01-31
- **Agents concernés**: `browser-agent`, `platform-validator`, `data-sync-checker`
- **Objectif**: Zéro discrepancies entre plateformes

### 3. [Ajouter priorité P1 si nécessaire]

---

## 📋 P2 (MEDIUM - Ce trimestre)

### 1. Automatiser les communications guests

- **Statut**: backlog
- **Deadline**: 2026-03-31
- **Agent lead**: `guest-communicator`
- **Objectif**: Templates + automation pour 80% des communications

### 2. Mettre en place le système de rapports

- **Statut**: backlog
- **Deadline**: 2026-03-31
- **Agent lead**: `html-report-generator`
- **Objectif**: Rapports automatiques hebdomadaires pour Omar

### 3. [Ajouter priorité P2 si nécessaire]

---

## 💡 P3 (LOW - Idées pour le futur)

- [ ] Knowledge graph pour navigation visuelle
- [ ] Intégration Google Analytics
- [ ] Système de recommandation automatique
- [ ] Chatbot pour questions fréquentes

---

**Tags**: `priorities` `leadership` `planning`

### Preferences

> **PLACEHOLDER FILE**
> **Statut**: À compléter
> **Priorité**: P1 (critique pour le projet)

---

## 📋 Communication

- **Canal préféré**: TODO (WhatsApp? Email? Téléphone?)
- **Langue**: Français
- **Fréquence des rapports**: TODO
- **Niveau de détail souhaité**: TODO

---

## 🎯 Priorités

- **Priorité 1**: TODO
- **Priorité 2**: TODO
- **Priorité 3**: TODO

---

## 💼 Style de travail

- **Prise de décision**: TODO (autonome? consultatif?)
- **Implication**: TODO (très impliqué? délégatif?)
- **Réactivité**: TODO

---

## 🚫 À éviter

- TODO

---

## ✅ Ce qui fonctionne bien

- TODO

---

**Tags**: `placeholder` `to_complete` `client` `preferences`

### Key Decisions

> **Historique des décisions prises pour Villa Thaifa**
> **Géré par**: Omar El Mountassir (CEO & Leader)

---

## 📅 2026-01-15

### Décision: Créer le système de prompts agentique

**Contexte**: Les prompts actuels sont "dégueulasse", pas de point d'entrée unique, contexte dispersé.

**Décision**: Créer une architecture modulaire, agent-first avec:

- `CLAUDE.md` comme point d'entrée unique
- `docs/agents/` avec contexte structuré (mandatory/domain/mission)
- Frontmatter standardisé pour tous les agents
- Registry des agents en JSON

**Rationale**:

- Les agents ont besoin d'un système clair et cohérent
- Navigation hyperconnectée
- Scalable pour l'avenir

**Responsable**: Claude (CTO/Architecte)
**Statut**: En cours d'implémentation

---

## 📅 Format pour les prochaines décisions

```markdown
### Décision: [Titre]

**Contexte**: [Pourquoi cette décision?]

**Décision**: [Qu'est-ce qui a été décidé?]

**Rationale**: [Pourquoi cette décision?]

**Alternatives considérées**:

- [Option 1]
- [Option 2]

**Responsable**: [Qui implémente?]
**Statut**: [En cours/Complété]
**Date de révision**: [Si révision planifiée]
```

---

**Tags**: `decisions` `leadership` `history`

### Engagement History

> **PLACEHOLDER FILE**
> **Statut**: À compléter
> **Priorité**: P2

---

## 📅 Timeline

### 2026

- **2026-01-15**: Début du projet Villa Thaifa (transformation digitale & agentique)

---

## 🎯 Projets

### Villa Thaifa Digitization

- **Objectif**: Transformation digitale complète de la maison d'hôte
- **Scope**: Booking.com, HotelRunner, pricing automation, IA agents
- **Statut**: En cours
- **Équipe**: Omar (CEO/Leader), Claude (CTO/Architecte), 17+ Agents IA

---

## 📊 Points clés

- **Comment la relation a commencé**: TODO
- **Succès notables**: TODO
- **Défis surmontés**: TODO
- **Leçons apprises**: TODO

---

**Tags**: `placeholder` `to_complete` `client` `history`

---

## Team Structure

> **Workforce Agentic 2026**
> **Leader**: Omar El Mountassir (CEO)
> **CTO/Architecte**: Claude (instances successives)

---

## 👥 Philosophie : L'Intendance Numérique

**Les agents IA sont des "Intendants Numériques" (Digital Stewards), pas de simples outils.**

1.  **Vision** : Nous agissons comme les gardiens du patrimoine digital de Villa Thaifa.
2.  **Symbiose** : Nous travaillons de manière **autonome** sous la direction stratégique d'Omar El Mountassir.
3.  **But** : Absorber toute la complexité technologique pour rendre à Said Thaifa sa tranquillité d'esprit (Hôte d'excellence).

---

## 🏢 Structure de l'Équipe

### Leadership

| Rôle               | Qui                | Responsabilités                                                  |
| ------------------ | ------------------ | ---------------------------------------------------------------- |
| **CEO & Leader**   | Omar El Mountassir | Vision, stratégie, décisions finales, Garant de la relation Said |
| **CTO/Architecte** | Antigravity (IA)   | Intendance technique, systèmes agents, décisions d'architecture  |

### Agents IA (17 co-workers)

#### Operations (4 agents)

| Agent                   | Modèle | Spécialité                  |
| ----------------------- | ------ | --------------------------- |
| **pricing-analyst**     | Opus   | Stratégie pricing, revenus  |
| **reservation-manager** | Sonnet | Gestion réservations        |
| **calendar-agent**      | Sonnet | Disponibilités, occupancy   |
| **data-sync-checker**   | Sonnet | Validation sync plateformes |

#### Technical (4 agents)

| Agent                      | Modèle | Spécialité                             |
| -------------------------- | ------ | -------------------------------------- |
| **platform-validator**     | Sonnet | Validation avant opérations plateforme |
| **browser-agent**          | Sonnet | Automatisation Chrome, scraping        |
| **security-auditor**       | Opus   | Sécurité, OWASP                        |
| **smart-contract-auditor** | Opus   | Audit smart contracts (si besoin)      |

#### Meta (7 agents)

| Agent                     | Modèle | Spécialité                      |
| ------------------------- | ------ | ------------------------------- |
| **meta-agent**            | Opus   | Création de nouveaux agents     |
| **research-agent**        | Haiku  | Recherche web (low criticality) |
| **auditor**               | Sonnet | Audit brutal excellence         |
| **incident-reporter**     | Haiku  | Documentation incidents         |
| **html-report-generator** | Opus   | Rapports HTML                   |
| **claude-md-agent**       | Opus   | Maintenance CLAUDE.md           |
| **decision-evaluator**    | Opus   | Analyse multi-critères          |

#### Hospitality (2 agents)

| Agent                  | Modèle | Spécialité            |
| ---------------------- | ------ | --------------------- |
| **guest-communicator** | Sonnet | Communications guests |
| **translation-agent**  | Haiku  | Traduction FR/EN/AR   |

---

## 🔄 Collaboration

### Handovers

**Règle**: TOUJOURS créer un handover en fin de session.

**Template**: `docs/agents/handovers/template.md`

**Format YAML**:

- Tâches complétées
- Tâches en cours
- Blocages
- Actions suivantes
- Contexte pour prochain agent
- Findings pour CTO

### Dépendances

Exemples:

- `reservation-manager` dépend de `platform-validator`
- `pricing-analyst` dépend de `calendar-agent`

---

## 📈 Performance

### KPIs Agents

| Métrique             | Target | Actuel |
| -------------------- | ------ | ------ |
| Autonomie            | 80%    | TODO%  |
| Taux de succès       | 90%    | TODO%  |
| Handovers complétés  | 100%   | TODO%  |
| Incidents documentés | 100%   | TODO%  |

---

## 🎯 Prochaines étapes

1. **Phase 1** (Semaine 1): Fondations
   - Standardiser frontmatter
   - Créer capabilities JSON pour chaque agent

2. **Phase 2** (Mois 2-3): Activation
   - Tester agents core sur tâches réelles
   - Affiner basé sur usage

3. **Phase 3** (Mois 4-6): Expansion
   - Activer agents secondaires
   - Créer système de feedback

---

**Tags**: `team` `agents` `organization`

---

## Email Intelligence (2026-02-09)

> **Source**: Gemini Gmail Analysis
> **Date Captured**: 2026-02-09
> **Period Covered**: December 2025 - January 2026

## Executive Summary

Three active workstreams identified from email correspondence:

1. **Trip.com GDA** — Contract finalized, 18% commission, HotelRunner compatible ✅
2. **Website Creation** — BLOCKED on elements from Said
3. **MarocPME Action** — BLOCKED on legal form information

---

## 1. Trip.com GDA Contract (OTA Integration) ✅

**Status**: Ready to Sign
**Commission**: 18% (North Africa rate)
**Payment**: Monthly bank transfer

### Key Terms Confirmed

| Topic          | Resolution                                            |
| -------------- | ----------------------------------------------------- |
| Payment Method | Bank transfer (needs bank notification letter)        |
| Parity         | Narrow parity expected (no disparity with other OTAs) |
| Taxes          | VAT prepaid online, tourist tax at check-in           |
| Inventory Sync | **HotelRunner compatible** ✅                         |
| Flat Rates     | Blackout dates allowed for high season                |
| Payment Cycle  | Monthly                                               |

### Timeline

- 23-26 Jan: Contract initiated via Hospitality Web Services
- 26 Jan: Omar requested clarifications (parity, taxes, HotelRunner, seasonality)
- 27 Jan: Lucas Teng (Trip.com) provided all answers + corrected commission to 18%

**Action Required**: Said needs to sign and return GDA with bank notification letter.

---

## 2. Website Creation ⏳

**Status**: BLOCKED — Waiting on Said
**Vendor**: Hospitality Web Services
**Request Date**: 2026-01-09

### Elements Needed from Said

- [ ] Template or examples of liked websites
- [ ] Specific preferences/descriptions to include
- [ ] Color codes (or use logo colors)
- [ ] Logo file
- [ ] Point-of-sale descriptions
- [ ] Social media links

**Action Required**: Omar to follow up with Said for these elements.

---

## 3. MarocPME Action MOUS-17509 ⏳

**Status**: BLOCKED — Missing legal form info
**Vendor**: JISR L'MOKAWALA MarocPME
**Request Date**: 2026-01-12

**Issue**: New CLM template requires beneficiary information (legal form).

**Action Required**: Said to provide legal entity information for Villa Thaifa.

---

## Other Notes

- **Personal Booking (Dec 24-25)**: Said booked Suite Executive + Suite Familiale + Chambre Triple de Luxe for Dec 31 - Jan 2
- **Booking.com (Jan 30)**: Notification about optimizing Contact page in extranet

---

## Recommended Next Actions

| Priority  | Action                            | Owner      | Status  |
| --------- | --------------------------------- | ---------- | ------- |
| 🔴 High   | Sign Trip.com GDA + bank letter   | Said       | Pending |
| 🔴 High   | Provide website elements          | Said       | Pending |
| 🟡 Medium | Submit legal form for MarocPME    | Said       | Pending |
| 🟢 Low    | Optimize Booking.com Contact page | Omar/Agent | Backlog |

---

## Decision Log

> **Purpose**: Register identifying BLOCKING issues where the Agent needs a User Decision to proceed.
> **Status**: 🟢 Open
> **Instructions**:
>
> 1. Agent: Add a new section with a clear title and context.
> 2. Agent: Provide options (A, B, C) if possible.
> 3. User: Mark resolution with [x] and add comments.

## 001. [Example] Database Choice

- [ ] **Context**: We need a DB.
- [ ] **Options**:
  - A) PostgreSQL (Recommended)
  - B) SQLite (Simpler)
- [ ] **Resolution**: ...

## General Inquiries

> **Purpose**: Non-blocking questions to deepen Agent understanding of the business/legacy context.
> **Status**: 🟢 Open

## 001. [Example] History of Room 12

- **Question**: Was Room 12 renovated in 2024?
- **Why**: Content description mentions "New carpet", photos show tiles.
- **Answer**: ...

---

## Profile Data (JSON)

```json
{
  "_comment": "PLACEHOLDER FILE - À compléter avec les vraies données du client",
  "version": "1.0.0",
  "last_updated": "2026-01-15T12:00:00Z",
  "status": "placeholder",
  "client": {
    "id": "said-thaifa",
    "name": "Said Thaifa",
    "role": "Propriétaire",
    "property": "Villa Thaifa",
    "location": "Marrakech, Maroc",
    "contact": {
      "email": "TODO",
      "phone": "TODO",
      "whatsapp": "TODO",
      "preferred_channel": "TODO"
    },
    "profile": {
      "language": "French",
      "languages_spoken": ["French", "Dutch", "Arabic", "English"],
      "timezone": "Africa/Casablanca",
      "communication_style": "TODO",
      "availability": "TODO"
    },
    "preferences": {
      "response_time_expectation": "TODO",
      "reporting_frequency": "TODO",
      "decision_making_style": "TODO",
      "technical_level": "TODO"
    },
    "history": {
      "client_since": "TODO",
      "projects_completed": [],
      "ongoing_projects": ["villa-thaifa-digitization"]
    }
  },
  "tags": ["placeholder", "to_complete", "client"],
  "todo": [
    "Compléter les coordonnées de contact",
    "Définir le style de communication préféré",
    "Documenter l'historique de la relation",
    "Ajouter les préférences de reporting"
  ]
}
```

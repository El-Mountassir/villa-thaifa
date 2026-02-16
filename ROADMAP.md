# ROADMAP — Villa Thaifa Digital Operations

> **Version** : [VERSION](VERSION.txt) > **Créé** : 2025-12-22
> **Objectif** : Transformation digitale complète en 2 mois

---

## 🎯 OVERVIEW

| Élément                | Valeur                                         |
| ---------------------- | ---------------------------------------------- |
| **Scope**              | Gestion digitale complète Villa Thaifa         |
| **Timeline**           | **2 mois** vers automatisation                 |
| **Phase actuelle**     | Phase 1 — Cleanup & Fondation                  |
| **Vision**             | Système réplicable pour **10+ établissements** |
| **Statut contractuel** | ❌ Aucun contrat signé                         |

### North Star

> **Un consultant + agents IA = gestion complète de 10+ établissements hôteliers.**

### Opportunité Go Siyaha

| Programme            | Financement                              | Plafond |
| -------------------- | ---------------------------------------- | ------- |
| Go Siyaha (MarocPME) | Jusqu'à **90%** des coûts digitalisation | 1M DH   |

→ Mission en queue : `2025-12-22-jisr-mokawala-investigation`

---

## 🚀 PHASE 1: CLEANUP & FONDATION

> **Semaine 1** | Status: 🟡 En cours

### 1.1 Nettoyage chaos

| Tâche                                 | Status               |
| ------------------------------------- | -------------------- |
| Fusionner CLAUDE.md (454→~120 lignes) | ✅ Done              |
| Archiver fichiers obsolètes           | ✅ Done              |
| Créer ROADMAP.md                      | ✅ Done (ce fichier) |
| Recycler archives (extraire valeur)   | ✅ Done              |

### 1.2 Formalisation relation

| Tâche                                                                                           | Status     |
| ----------------------------------------------------------------------------------------------- | ---------- |
| Créer proposition commerciale                                                                   | 🔴 À faire |
| Définir Statement of Work (SOW)                                                                 | 🔴 À faire |
| Etudiez nos possiblités en termes de propositions à Mr Said afin de par la suite signer contrat | 🔴 À faire |
| Faire signer contrat                                                                            | 🔴 À faire |

### 1.3 Configuration HotelRunner

| Tâche                                                      | Status      |
| ---------------------------------------------------------- | ----------- |
| Contact HWS établi avec Ikram ( HWS Support (HotelRunner)) | ✅ Done     |
| Demande API en cours HWS Support (HotelRunner)             | ⏳ Waiting  |
| Audit complet HotelRunner                                  | 🟡 À lancer |
| Configuration pricing                                      | 🟡 Pending  |

### Success Metrics Phase 1

- [ ] CLAUDE.md < 150 lignes
- [ ] Proposition commerciale prête
- [ ] HotelRunner entièrement documenté
- [ ] 0 fichiers orphelins

---

## 🟠 PHASE 2: FORMALISATION & EXPANSION

> **Semaines 2-3**

### 2.1 Relation formalisée

| Tâche                           | Dépendance            |
| ------------------------------- | --------------------- |
| Contrat signé avec M. Thaifa    | Proposition approuvée |
| Accès officiels aux plateformes | Contrat signé         |
| Grille tarifaire établie        | Scope défini          |

### 2.2 Setup plateformes OTA

| Plateforme      | Statut         | Notes                         |
| --------------- | -------------- | ----------------------------- |
| Booking.com     | ✅ Actif       | Via HWS Support (HotelRunner) |
| Expedia         | 🔴 À connecter | Via HWS Support (HotelRunner) |
| Airbnb          | 🔴 À connecter | Via HWS Support (HotelRunner) |
| +17 autres OTAs | 🔴 À évaluer   | Via HWS Support (HotelRunner) |

### 2.3 Stratégie pricing

| Élément                    | Status                              |
| -------------------------- | ----------------------------------- |
| Baseline prices documentés | ✅ Dans `data/specs/hotel/rooms.md` |
| Seasonal adjustments       | 🟡 À définir                        |
| Promotions strategy        | 🟡 En cours                         |

### 2.4 Go Siyaha Application

| Tâche                          | Status     |
| ------------------------------ | ---------- |
| Vérifier éligibilité           | 🔴 À faire |
| Préparer documents             | 🔴 À faire |
| Soumettre candidature via Jisr | 🔴 À faire |

### Success Metrics Phase 2

- [ ] Contrat signé
- [ ] 20+ canaux OTA actifs
- [ ] Stratégie pricing documentée
- [ ] Candidature Go Siyaha soumise

---

## 🟢 PHASE 3: AUTOMATISATION

> **Semaines 4-6**

### 3.1 Gestion réservations automatisée

| Tâche                          | Dépendance               |
| ------------------------------ | ------------------------ |
| Workflow réservation documenté | Audit HotelRunner        |
| Notifications automatiques     | API ou Chrome automation |
| Guest communication templates  | Communication protocol   |

### 3.2 Analytics & Reporting

| Rapport           | Fréquence | Automatisation |
| ----------------- | --------- | -------------- |
| Revenus           | Hebdo     | 🎯 Target      |
| Taux d'occupation | Quotidien | 🎯 Target      |
| Performance OTAs  | Mensuel   | 🎯 Target      |

### 3.3 Intégration technique

| Option            | Status                      | Préférence  |
| ----------------- | --------------------------- | ----------- |
| API HotelRunner   | ⏳ En attente réponse Ikram | ⭐ Idéal    |
| Chrome automation | ✅ Fonctionnel              | 🟡 Fallback |
| Email parsing     | 🔴 À développer             | 🟠 Plan B   |

### Success Metrics Phase 3

- [ ] -80% temps manuel sur réservations
- [ ] Dashboard temps réel fonctionnel
- [ ] Rapports automatisés hebdo

---

## 🔵 PHASE 4: SYSTÈME AGENT IA

> **Mois 2+**

### 4.1 Capacités agent autonome

| Capacité                        | Priorité |
| ------------------------------- | -------- |
| Répondre aux demandes de dispo  | 🔴 P0    |
| Créer réservations              | 🔴 P0    |
| Gérer pricing dynamique         | 🟠 P1    |
| Générer rapports                | 🟠 P1    |
| Communication guest (templates) | 🟡 P2    |

### 4.2 Architecture

```txt
Omar (Oversight 2h/semaine)
    ↓
Claude Code (Orchestrateur)
    ↓
┌─────────────┬─────────────┬─────────────┐
│ HotelRunner │ Booking.com │ WhatsApp    │
│ Agent       │ Agent       │ Agent       │
└─────────────┴─────────────┴─────────────┘
```

### Success Metrics Phase 4

- [ ] Opérations 80%+ autonomes
- [ ] Omar: max 2h/semaine oversight
- [ ] SLA: réponse < 1h aux demandes

---

## 📊 VISION LONG-TERME

> **Année 2+**

### Objectifs

| Métrique                     | Cible           |
| ---------------------------- | --------------- |
| Établissements gérés         | 10+             |
| Revenus récurrents           | €150K+/an       |
| Temps Omar par établissement | < 30min/semaine |

### Portfolio cible

Inspirer des clients HWS existants :

- Riads (ex: Riad Bianca)
- Villas de luxe (ex: Villa Thaifa)
- Maisons d'hôtes (ex: Auberge Azul)
- Hotels boutique (ex: Kohinor)

### Système réplicable

```
Template "Villa Thaifa"
    → Clone pour nouvel établissement
    → Personnaliser data/specs/
    → Connecter aux plateformes
    → Agent IA opérationnel en 1 semaine
```

---

## 📅 JALONS CRITIQUES

| Date             | Milestone                    | Status     |
| ---------------- | ---------------------------- | ---------- |
| 22 Dec 2025      | RDV avec M. Thaifa           | ✅ Done    |
| 24 Dec 2025      | Deadline décision Warembourg | ⏳ Pending |
| **27 Dec 2025**  | Phase 1 complète             | 🎯 Target  |
| **Mi-Jan 2026**  | Phase 2 complète             | 🎯 Target  |
| **Fin Jan 2026** | Phase 3 complète             | 🎯 Target  |
| **Mi-Fév 2026**  | Agent IA opérationnel        | 🎯 Target  |

---

## 🔄 AMÉLIORATION CONTINUE

### Cadence

| Fréquence | Action                       |
| --------- | ---------------------------- |
| Quotidien | Check réservations, blockers |
| Hebdo     | Rapport revenus, KPIs        |
| Bi-hebdo  | Sync avec M. Thaifa          |
| Mensuel   | Revue ROADMAP, ajustements   |

### Métriques à tracker

| KPI                        | Baseline  | Target         |
| -------------------------- | --------- | -------------- |
| Temps par réservation      | 15-20 min | < 5 min        |
| Taux occupation            | ?         | +10%           |
| Revenus mensuels           | ?         | Baseline + 20% |
| Part réservations directes | ~0%       | 20%+           |

---

## 📚 RÉFÉRENCES

| Document                  | Purpose                  |
| ------------------------- | ------------------------ |
| `CLAUDE.md`               | Context IA               |
| `data/specs/`             | Specs métier (SSOT)      |
| `docs/lessons-learned.md` | Erreurs & apprentissages |
| `.env` / `.env.example`   | Accès plateformes        |

---

_*ROADMAP v0.0.1-alpha.0 — Document vivant, mis à jour au fil de l'exécution*_

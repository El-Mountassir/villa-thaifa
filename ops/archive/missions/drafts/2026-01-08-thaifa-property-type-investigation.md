---
id: 2026-01-08-property-type-investigation
type: mission
status: in_progress
priority: P2
title: "Investigation Type d'Établissement Booking.com"
description: "Scout et documenter le type d'établissement actuel sur Booking.com (Hotel vs Maison d'Hôtes)"
client: Villa Thaifa
requested-by: Omar El Mountassir
date-created: 2026-01-08
tags:
  - thaifa
  - booking
  - property-settings
  - investigation
---

# Investigation Type d'Établissement Booking.com

## Contexte

Villa Thaifa est officiellement une **Maison d'hôtes de charme / B&B (4★)** selon notre documentation (`data/admin/client/PROFILE.md`).

**Problème signalé**: La propriété serait listée comme "Hotel" sur Booking.com au lieu de "Maison d'Hôtes".

**Objectif**: Vérifier et documenter l'état actuel — SCOUT ONLY, pas de modification.

---

## Objectifs

- [x] Confirmer ou infirmer que le type est "Hotel" sur Booking.com — **CONFIRMÉ: "Hôtel"**
- [x] Identifier l'emplacement exact du paramètre dans Booking.com Extranet — **NON ACCESSIBLE via Extranet**
- [x] Documenter les options disponibles pour le type d'établissement — **Non visible, contact support requis**
- [x] Capturer des screenshots comme preuves — **7 screenshots capturés**

---

## Critères de Succès

| #   | Critère                               | Status | Evidence                                       |
| --- | ------------------------------------- | ------ | ---------------------------------------------- |
| 1   | Type d'établissement actuel documenté | ✅     | "Hôtel" — confirmé via page publique           |
| 2   | Emplacement du paramètre identifié    | ✅     | Non accessible via Extranet, défini à création |
| 3   | Options alternatives listées          | ⚠️     | Non visible, contact support requis            |
| 4   | Screenshots capturés                  | ⚠️     | 7 IDs capturés mais **NON PERSISTÉS** en fichiers |
| 5   | Aucune modification effectuée         | ✅     | Confirmation visuelle — SCOUT ONLY             |

---

## Contraintes

- **SCOUT ONLY** — Ne pas modifier le type d'établissement
- Utiliser le compte Admin Omar
- Respecter les règles plateforme (`data/specs/platform/rules.md`)
- Documenter tout comportement inattendu

---

## Plan d'Investigation

### Phase 1: Accès Booking.com Extranet

1. Naviguer vers `admin.booking.com`
2. Se connecter avec compte Admin Omar
3. Accéder aux paramètres de propriété

### Phase 2: Localisation du Paramètre

1. Chercher "Property settings" / "Paramètres établissement"
2. Identifier la section "Type d'établissement" / "Property type"
3. Noter le chemin de navigation

### Phase 3: Documentation

1. Capturer screenshot de la configuration actuelle
2. Noter le type affiché
3. Lister les options disponibles (si visible)

---

## Résultats de l'Investigation

### Type d'Établissement Actuel

**Type affiché**: **Hôtel** ❌ (ÉCART avec type souhaité "Maison d'Hôtes")

**Emplacement**:

- NON ACCESSIBLE via Booking.com Extranet
- Défini lors de la création initiale de la propriété
- Modification requiert contact avec support Booking.com

**Options disponibles**: Non visibles dans l'interface Extranet

### Preuves Textuelles (Page Publique)

La page publique `booking.com/hotel/ma/riad-salim-amp-spa` utilise systématiquement "hôtel":

- "cet hôtel est à respectivement 13 km et 14 km environ de"
- "Cet hôtel offre une vue sur le jardin"
- URL structure: `/hotel/ma/` (catégorie hôtel)

### Screenshots

| ID             | Description                |
| -------------- | -------------------------- |
| `ss_32906p0bs` | Page d'accueil Extranet    |
| `ss_33049zmj1` | Page Réservations          |
| `ss_0530isdkg` | Menu Établissement         |
| `ss_90203eps4` | Infos établissement        |
| `ss_8139u51ht` | Équipements et services    |
| `ss_7856m5kwm` | Page publique Villa Thaifa |
| `ss_7431yyq77` | Capture additionnelle      |

### Rapport Détaillé

📄 **`ai/output/2026-01-08-property-type-scout-report.md`**

---

## Execution Log

| Timestamp  | Action                             | Result                      |
| ---------- | ---------------------------------- | --------------------------- |
| 2026-01-08 | Création mission draft             | ✅ Créée                    |
| 2026-01-08 | Navigation Extranet Booking.com    | ✅ Accès OK                 |
| 2026-01-08 | Recherche paramètre type propriété | ⚠️ Non trouvé dans Extranet |
| 2026-01-08 | Analyse page publique              | ✅ Type "Hôtel" confirmé    |
| 2026-01-08 | Capture screenshots                | ✅ 7 screenshots            |

---

## Recommandations

### Action Requise

Pour changer le type "Hôtel" → "Maison d'Hôtes":

1. **Contacter Support Booking.com** (via Ikram — voir `data/admin/client/support/README.md`)
2. **Justification à préparer**:
   - Nature de l'établissement (12 chambres, service personnalisé)
   - Services style maison d'hôtes (petit-déjeuner inclus, ambiance familiale)
3. **Impact à évaluer**:
   - Visibilité dans filtres recherche "B&B" / "Maison d'Hôtes"
   - Positionnement concurrentiel
   - Potentiel changement de commission?

### Nouvelle Mission à Créer

`missions/queue/YYYY-MM-DD-thaifa-property-type-change-request.md`

- Objectif: Demander changement de type via support Booking.com
- Priorité: À définir avec Omar

---

## Implications de l'Écart

| Impact          | Description                                                       |
| --------------- | ----------------------------------------------------------------- |
| **Visibilité**  | Villa Thaifa n'apparaît PAS dans filtres "B&B" / "Maison d'Hôtes" |
| **Concurrence** | En compétition avec hôtels, pas maisons d'hôtes                   |
| **Attentes**    | Clients s'attendent à service hôtel                               |
| **Commission**  | À vérifier si différente selon type                               |

---

---

## 🚨 Tâches Additionnelles — Screenshots Non Persistés

### Contexte Incident

Les 7 screenshots capturés par browser-agent ont des **IDs temporaires** en mémoire Chrome mais n'ont **PAS été sauvegardés** en fichiers persistants dans `ai/output/`.

| Ce qui existe | Ce qui manque |
|---------------|---------------|
| IDs: `ss_32906p0bs`, `ss_33049zmj1`, etc. | Fichiers `.png` dans `ai/output/` |

**Root Cause**: Instructions browser-agent disent "Save screenshots" mais pas COMMENT techniquement.

### A. Récupération Screenshots

- [ ] Rechercher screenshots existants sur l'ordi (Downloads, ai/output/, tmp/)
- [ ] Si trouvés → copier vers `ai/output/` avec noms descriptifs
- [ ] Si NON trouvés → recapturer les 7 screenshots via browser-agent

### B. Amélioration browser-agent (P1)

- [ ] Modifier `.claude/agents/browser-agent.md` avec instructions explicites de sauvegarde
- [ ] Ajouter checklist de validation screenshots avant SUCCESS
- [ ] Documenter workflow complet: capture → sauvegarde → report

### C. Test de Validation

- [ ] Exécuter mini-test browser-agent avec 1 screenshot
- [ ] Confirmer fichier PNG créé dans `ai/output/`
- [ ] Confirmer fichier lisible (non corrompu)

### D. Documentation Incident

- [ ] Créer `docs/incidents/open/2026-01-08-browser-agent-screenshots-not-saved.md`
- [ ] Documenter root cause, impact, et fix appliqué

---

_Mission en cours: 2026-01-08 | Status: IN_PROGRESS | Priorité: P2_

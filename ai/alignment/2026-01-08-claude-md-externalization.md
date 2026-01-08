# Alignement: Externalisation de CLAUDE.md

> **Date**: 2026-01-08
> **De**: Claude (Orchestrateur)
> **À**: Omar El Mountassir (Root Authority)
> **Statut**: En attente d'alignement
> **Version**: 2.0 (corrigée)

---

## 1. Contexte de la Demande

Omar souhaite:

1. **Externaliser CLAUDE.md** — Transformer en fichier de pointeurs (`@path/to/file`)
2. **Éliminer la redondance** — Exemple: liste d'agents dupliquée (registry + inline)
3. **Utiliser l'ontologie** — `ai/rules/organizational-ontology.md` comme guide structurel
4. **Préparer multi-CLI** — Structure réutilisable pour Gemini CLI, Codex CLI, etc.
5. **Contrôle & Visibilité** — Chaque élément dans son fichier dédié

---

## 2. Analyse de l'État Actuel

### 2.1 CLAUDE.md — Contenu Inline (279 lignes)

| Section              | Lignes  | Problème              | Priorité | Action        | Destination                                 | Effort |
| -------------------- | ------- | --------------------- | -------- | ------------- | ------------------------------------------- | ------ |
| Identité             | 7-14    | Inline                | P2       | Externaliser  | `ai/context/identity.md`                    | S      |
| CORE LOOP            | 18-42   | Inline, CORE          | P1       | Externaliser  | `ai/workflows/core-loop.md`                 | S      |
| Règle d'Or           | 46-50   | Inline                | P1       | Externaliser  | `ai/rules/golden-rule.md`                   | S      |
| Agents Disponibles   | 54-64   | **REDONDANT**         | P1       | Supprimer     | Pointer vers registry                       | S      |
| Briefing Sub-Agents  | 66-74   | Inline                | P2       | Externaliser  | `ai/protocols/briefing.md`                  | S      |
| Report Protocol      | 77-163  | **LOURD** (80 lignes) | P1       | Externaliser  | `ai/protocols/reporting.md`                 | M      |
| Communication        | 167-175 | Inline                | P2       | Externaliser  | `ai/rules/communication.md`                 | S      |
| Données              | 179-188 | **REDONDANT**         | P1       | Externaliser  | `ai/inventory/data-locations.md`            | S      |
| Incidents            | 192-201 | Inline                | P2       | Externaliser  | `ai/protocols/incidents.md`                 | S      |
| Checklist Plateforme | 205-214 | **REDONDANT**         | P1       | Supprimer     | Pointer vers `data/specs/platform/rules.md` | S      |
| Git Workflow         | 218-253 | Inline                | P2       | Externaliser  | `ai/workflows/git.md`                       | S      |
| Références           | 257-265 | Liste pointeurs       | P3       | Garder inline | -                                           | -      |
| Contacts             | 269-274 | **REDONDANT**         | P1       | Supprimer     | Pointer vers `data/admin/client/`           | S      |

**Légende Effort**: S = Small (< 5 min), M = Medium (5-15 min), L = Large (> 15 min)

### 2.2 Redondances Identifiées

| Contenu              | Dans CLAUDE.md | Aussi dans                           | SSOT            | Action                 | Impact si non corrigé |
| -------------------- | -------------- | ------------------------------------ | --------------- | ---------------------- | --------------------- |
| Liste agents         | Lignes 58-64   | `ai/inventory/sub-agent_registry.md` | Registry        | Supprimer de CLAUDE.md | Désynchronisation     |
| Checklist plateforme | Lignes 205-214 | `data/specs/platform/rules.md`       | Platform rules  | Supprimer, pointer     | Maintenance double    |
| Contacts             | Lignes 269-274 | `data/admin/client/CONTACT.md`       | Client folder   | Supprimer, pointer     | Info obsolète         |
| Emplacements données | Lignes 179-188 | Dispersé dans `data/specs/`          | Nouveau fichier | Créer inventory        | Incohérence           |

---

## 3. Structure Cible

### 3.1 Arborescence Proposée (basée sur l'ontologie)

```
ai/
├── Strategic
    ├── context/                     # Tier: Strategic (Qui nous sommes)
    │   └── identity.md              # Identité, Projet, Autorité, Mode
│
├── workflows/                   # Tier: Operational (Comment on travaille)
│   ├── core
|   │   ├── loop.md              # Le CORE LOOP (6 étapes)
|   │   └── ...
│   └── git.md                   # Git commit/push discipline
│
├── protocols/                   # Tier: Execution (Comment les agents communiquent)
│   ├── briefing.md              # Comment briefer les sub-agents
│   ├── reporting.md             # SUCCESS/FAILURE/PARTIAL formats
│   └── incidents.md             # Logging et sévérité
│
├── models
    ├── processes
        ├── mental
            ├── rules/                       # Tier: Models/Processes/Mental (Principes directeurs)
            │   ├── golden-rules.md          # Confiance 94%, ...
            │   ├── communication.md         # Langue, registre
            │   └── organizational-ontology.md  # (existe déjà)
│
├── data
    ├── refs
        ├── inventory/                   # Tier: Data (Registres et références)
        │   ├── sub-agent_registry.md    # (existe déjà, à déplacer de ai/registry/)
        │   └── data-locations.md        # SSOT des emplacements de données
│
└── alignment/                   # (ce dossier - documents d'alignement)
    └── *.md
```

### 3.2 Décision sur les Chemins

| Actuel         | Proposé         | Raison                                           |
| -------------- | --------------- | ------------------------------------------------ |
| `ai/registry/` | `ai/inventory/` | Cohérence avec ontologie (inventory = registres) |
| `/CLAUDE.md`   | `/CLAUDE.md`    | Convention Claude Code (racine)                  |

---

## 4. Mapping Source → Destination

### 4.1 Fichiers à Créer (8 fichiers)

| #   | Fichier destination              | Source (CLAUDE.md lignes) | Taille estimée | Dépendances                      | Validation                            |
| --- | -------------------------------- | ------------------------- | -------------- | -------------------------------- | ------------------------------------- |
| 1   | `ai/context/identity.md`         | 7-14                      | ~15 lignes     | Aucune                           | Contient: Qui, Projet, Autorité, Mode |
| 2   | `ai/workflows/core-loop.md`      | 18-42                     | ~30 lignes     | golden-rule.md (référence 94%)   | Contient: Diagramme + 6 étapes        |
| 3   | `ai/rules/golden-rule.md`        | 46-50                     | ~10 lignes     | Aucune                           | Contient: Règle 94%                   |
| 4   | `ai/protocols/briefing.md`       | 66-74                     | ~15 lignes     | reporting.md (référence formats) | Contient: 5 éléments du brief         |
| 5   | `ai/protocols/reporting.md`      | 77-163                    | ~90 lignes     | Aucune                           | Contient: SUCCESS/FAILURE/PARTIAL     |
| 6   | `ai/protocols/incidents.md`      | 192-201                   | ~20 lignes     | Aucune                           | Contient: Chemin + sévérités          |
| 7   | `ai/rules/communication.md`      | 167-175                   | ~15 lignes     | Aucune                           | Contient: Tableau langue/registre     |
| 8   | `ai/inventory/data-locations.md` | 179-188                   | ~20 lignes     | Aucune                           | Contient: Tableau emplacements        |

### 4.2 Fichiers à Déplacer (1 fichier)

| Source                              | Destination                          | Raison                 |
| ----------------------------------- | ------------------------------------ | ---------------------- |
| `ai/registry/sub-agent_registry.md` | `ai/inventory/sub-agent_registry.md` | Cohérence nomenclature |

### 4.3 Ordre de Création (basé sur dépendances)

```
1. golden-rule.md        (aucune dépendance)
2. identity.md           (aucune dépendance)
3. communication.md      (aucune dépendance)
4. data-locations.md     (aucune dépendance)
5. incidents.md          (aucune dépendance)
6. reporting.md          (aucune dépendance)
7. briefing.md           (dépend de reporting.md)
8. core-loop.md          (dépend de golden-rule.md)
9. Déplacer registry     (après création inventory/)
10. Réécrire CLAUDE.md   (après tout le reste)
```

---

## 5. Questions pour Omar

### Q1: Granularité de l'externalisation

| Option            | Description                         | CLAUDE.md résultant | Avantage              | Inconvénient                 | Effort | Reco |
| ----------------- | ----------------------------------- | ------------------- | --------------------- | ---------------------------- | ------ | ---- |
| **A) Maximale**   | Tout externalisé                    | ~35 lignes          | Cohérence totale, DRY | Plus de fichiers à maintenir | M      | ✓    |
| **B) Équilibrée** | CORE LOOP inline, reste externalisé | ~70 lignes          | Visibilité du core    | Incohérence partielle        | M      |      |
| **C) Minimale**   | Seulement redondances               | ~150 lignes         | Moins de changements  | Problème non résolu          | S      |      |

**Choix Omar**: **\*\***\_\_\_**\*\***

### Q2: Emplacement du CLAUDE.md maître

| Option           | Chemin          | Avantage               | Inconvénient                 | Compatibilité | Reco |
| ---------------- | --------------- | ---------------------- | ---------------------------- | ------------- | ---- |
| **A) Racine**    | `/CLAUDE.md`    | Convention Claude Code | Mélangé avec autres fichiers | Claude Code ✓ | ✓    |
| **B) AI folder** | `/ai/CLAUDE.md` | Cohérence structure    | Non-standard                 | Claude Code ? |      |

**Choix Omar**: **\*\***\_\_\_**\*\***

### Q3: Format des pointeurs

| Option               | Syntaxe                                  | Avantage             | Inconvénient            | Supporté par  | Reco |
| -------------------- | ---------------------------------------- | -------------------- | ----------------------- | ------------- | ---- |
| **A) @path**         | `@ai/workflows/core-loop.md`             | Concis, déjà utilisé | Propriétaire Claude     | Claude Code ✓ | ✓    |
| **B) Markdown link** | `[CORE LOOP](ai/workflows/core-loop.md)` | Standard markdown    | Plus verbeux            | Tous éditeurs |      |
| **C) Include**       | `<!-- include: path -->`                 | Explicite            | Non supporté nativement | Aucun         |      |

**Choix Omar**: **\*\***\_\_\_**\*\***

### Q4: Renommage registry → inventory

| Option          | Action                           | Avantage               | Inconvénient                | Reco |
| --------------- | -------------------------------- | ---------------------- | --------------------------- | ---- |
| **A) Renommer** | `ai/registry/` → `ai/inventory/` | Cohérence ontologie    | Casse références existantes | ✓    |
| **B) Garder**   | Garder `ai/registry/`            | Pas de breaking change | Incohérence nomenclature    |      |

**Choix Omar**: **\*\***\_\_\_**\*\***

### Q5: Gestion de l'ontologie

| Option            | Action                                  | Avantage         | Inconvénient        | Effort | Reco |
| ----------------- | --------------------------------------- | ---------------- | ------------------- | ------ | ---- |
| **A) Référence**  | Garder comme doc de référence           | Zéro effort      | Pas intégré         | -      | ✓    |
| **B) Simplifier** | Garder seulement Core (15 niveaux)      | Plus accessible  | Perte de complétude | S      |      |
| **C) Intégrer**   | Utiliser pour structurer, puis archiver | Structure guidée | Effort de mapping   | M      |      |

**Choix Omar**: **\*\***\_\_\_**\*\***

### Q6: Multi-CLI Readiness

| Option                  | Action                               | Avantage                 | Inconvénient            | Effort futur | Reco |
| ----------------------- | ------------------------------------ | ------------------------ | ----------------------- | ------------ | ---- |
| **A) Fichiers séparés** | `CLAUDE.md`, `GEMINI.md`, `CODEX.md` | Personnalisation par CLI | Maintenance multiple    | M            |      |
| **B) Fichier unique**   | `AI-CONTEXT.md` pour tous            | Un seul fichier          | Pas de personnalisation | S            |      |
| **C) Plus tard**        | Focus Claude, adapter ensuite        | Avancer maintenant       | Refactoring futur       | -            | ✓    |

**Choix Omar**: **\*\***\_\_\_**\*\***

---

## 6. Résumé des Décisions

| #   | Question           | Options | Ma reco | Choix Omar | Justification                       |
| --- | ------------------ | ------- | ------- | ---------- | ----------------------------------- |
| Q1  | Granularité        | A/B/C   | A       | **A**      | Tout externalisé, ~35 lignes        |
| Q2  | Emplacement        | A/B     | A       | **A**      | Racine (convention Claude Code)     |
| Q3  | Format pointeurs   | A/B/C   | A       | **A**      | @path (déjà utilisé)                |
| Q4  | Renommage registry | A/B     | A       | **A**      | Cohérence ontologie                 |
| Q5  | Ontologie          | A/B/C   | A       | **A**      | Garder comme référence              |
| Q6  | Multi-CLI          | A/B/C   | C       | **Custom** | Index central `ai/context/index.md` |

### Règle Additionnelle (Q2)

> **RÈGLE RACINE**: Les fichiers suivants DOIVENT être à la racine du projet:
>
> - `CLAUDE.md` — Contexte Claude Code
> - `GEMINI.md` — Contexte Gemini CLI (futur)
> - `AGENTS.md` — Standards multi-agents
>
> Cette règle est NON-NÉGOCIABLE pour la compatibilité CLI.

### Clarification Q6: Index Central

Structure finale pour multi-CLI:

```
/CLAUDE.md              → Pointe vers ai/context/index.md + fichiers spécifiques Claude
/GEMINI.md              → Pointe vers ai/context/index.md + fichiers spécifiques Gemini (futur)
/AGENTS.md              → Standards partagés

ai/context/
├── index.md            → Index central listant TOUS les contextes
├── identity.md         → Identité projet (partagé)
└── ...
```

---

## 7. Gestion des Risques

| Risque                                      | Probabilité | Impact   | Mitigation                      | Responsable |
| ------------------------------------------- | ----------- | -------- | ------------------------------- | ----------- |
| Pointeurs @path non résolus par Claude Code | Moyenne     | Haut     | Tester avant commit final       | Claude      |
| Perte de contenu lors extraction            | Basse       | Critique | Diff avant/après, backup        | Claude      |
| Références cassées dans autres fichiers     | Moyenne     | Moyen    | Grep global pour anciennes refs | Claude      |
| Structure non comprise par futur Claude     | Basse       | Moyen    | README dans chaque dossier      | Claude      |
| Incohérence entre fichiers externalisés     | Moyenne     | Moyen    | Review croisée systématique     | Omar        |

### Plan de Mitigation Principal

1. **Backup** de CLAUDE.md actuel avant toute modification
2. **Commits atomiques** (1 fichier = 1 commit) pour rollback facile
3. **Test** des pointeurs @path après chaque création
4. **Diff** du contenu total avant/après pour vérifier zéro perte

---

## 8. Plan de Rollback

Si l'externalisation échoue:

```
1. git log --oneline -20                    # Trouver le commit avant migration
2. git checkout <commit-hash> -- CLAUDE.md  # Restaurer CLAUDE.md
3. git checkout <commit-hash> -- ai/        # Restaurer structure ai/
4. git status                               # Vérifier état
5. git add -A && git commit -m "rollback: revert externalization"
```

**Point de non-retour**: Aucun — tous les changements sont réversibles via git.

---

## 9. Critères de Succès

| Critère                  | Mesure                           | Seuil            | Validation           |
| ------------------------ | -------------------------------- | ---------------- | -------------------- |
| Réduction CLAUDE.md      | Nombre de lignes                 | < 50 lignes      | `wc -l CLAUDE.md`    |
| Zéro redondance          | Duplications de contenu          | 0                | Grep croisé          |
| Tous pointeurs valides   | Fichiers référencés existent     | 100%             | Script de validation |
| Zéro perte de contenu    | Diff avant/après                 | 0 lignes perdues | Comparaison manuelle |
| Structure suit ontologie | Dossiers correspondent aux tiers | 100%             | Review visuelle      |
| Temps de compréhension   | Lecture CLAUDE.md                | < 1 minute       | Test utilisateur     |

---

## 10. Checklist de Validation Finale

### Avant commit final

- [ ] Tous les 8 fichiers créés existent
- [ ] Registry déplacé vers inventory/ (si choisi)
- [ ] CLAUDE.md réécrit avec pointeurs uniquement
- [ ] Aucune ligne de l'ancien CLAUDE.md perdue
- [ ] Tous les @path pointent vers fichiers existants
- [ ] Grep: aucune référence vers anciens chemins
- [ ] Git status propre (pas de fichiers non trackés oubliés)
- [ ] Diff total: contenu équivalent avant/après

### Après commit

- [ ] Push vers remote
- [ ] Nouvelle session Claude Code lit correctement les fichiers
- [ ] Aucun warning/erreur de fichier manquant

---

## 11. Estimation Effort Total

| Tâche                           | Effort | Durée estimée |
| ------------------------------- | ------ | ------------- |
| Créer structure dossiers        | S      | 2 min         |
| Créer 8 fichiers par extraction | M      | 20 min        |
| Déplacer registry (si choisi)   | S      | 2 min         |
| Réécrire CLAUDE.md (pointeurs)  | S      | 5 min         |
| Tests & validation              | M      | 10 min        |
| Commits atomiques               | S      | 5 min         |
| **Total**                       | -      | **~45 min**   |

---

## 12. Nouveau CLAUDE.md (Aperçu)

```markdown
# Villa Thaifa — Claude Context

> **Structure**: EaC + Agentic AI (v5) | **Workflow**: CORE LOOP
> **Fichiers externalisés** — Chaque section pointe vers son fichier dédié

---

## Identité

@ai/context/identity.md

## CORE LOOP

@ai/workflows/core-loop.md

## Règle d'Or

@ai/rules/golden-rule.md

## Agents

@ai/inventory/sub-agent_registry.md

## Protocols

@ai/protocols/briefing.md
@ai/protocols/reporting.md
@ai/protocols/incidents.md

## Rules

@ai/rules/communication.md
@ai/rules/organizational-ontology.md

## Data

@ai/inventory/data-locations.md

## Workflows

@ai/workflows/git.md

## Platform

@data/specs/platform/rules.md

## Client

@data/admin/client/PROFILE.md
@data/admin/client/CONTACT.md

---

_Villa Thaifa Project — El Mountassir Organization_
```

**Lignes estimées**: ~40

---

## 13. Notes Préservées du Message d'Omar

> "Cela nous permet d'avoir beaucoup plus de controle, de visibilité, d'alignement et d'éviter que tout soit 'coupled' et fragmenté et désynchronisé"

> "Cela nous permettra d'arriver à avoir un max de control sur ce que nous faisons. Mais aussi, de nous permettre d'ajouter d'autres agents / agentic systems / CLIs"

> "Agissons vite et agissons bien ! Efficacement, effectively, efficiently doucement mais surement"

> "Assures toi que tout ce qui est contenu dans ce message soit bien distribué et préservé proprement"

---

## 14. Prochaines Étapes

1. **Omar répond aux 6 questions** (section 5)
2. **Omar donne son "Go"** pour activer plan mode
3. **Claude planifie** en détail l'exécution
4. **Exécution** selon le plan
5. **Validation** avec checklist
6. **Commit & Push**

---

**Toutes les questions ont été répondues.**

| Question              | Rempli? | Choix                  |
| --------------------- | ------- | ---------------------- |
| Q1 Granularité        | ✅      | A (Maximale)           |
| Q2 Emplacement        | ✅      | A (Racine)             |
| Q3 Format pointeurs   | ✅      | A (@path)              |
| Q4 Renommage registry | ✅      | A (Renommer)           |
| Q5 Ontologie          | ✅      | A (Référence)          |
| Q6 Multi-CLI          | ✅      | Custom (Index central) |

---

## 15. STATUT: PRÊT POUR PLAN MODE

**Date alignement**: 2026-01-08
**Décisions**: Toutes validées par Omar
**Prochaine étape**: Omar donne son "Go" → Claude active plan mode

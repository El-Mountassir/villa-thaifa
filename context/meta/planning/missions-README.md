# Missions — Villa Thaifa

## Objectif

Ce dossier `missions/` est la **source de vérité** (SSOT) pour toutes les missions liées au client **Villa Thaifa**.

Il est conçu pour fonctionner avec des workflows agentiques (Claude Code CLI, OpenCode, etc.) et pour permettre une exécution **dans le contexte du dépôt client**, sans dépendre d'un système externe.

---

## Cycle de vie

| Dossier    | Description                                |
|------------|--------------------------------------------|
| `drafts/`  | Idées, cadrage, plans, non assignées       |
| `queue/`   | Prêtes à être exécutées (brief validé)     |
| `active/`  | En cours d'exécution (claim explicite)     |
| `archive/` | Terminées (historique)                     |

```
drafts → queue → active → archive
```

---

## Conventions de nommage

Format recommandé : `YYYY-MM-DD-<client>-<slug>.md`

Exemple : `2025-12-28-thaifa-chambre5-sync-investigation.md`

---

## Métadonnées (frontmatter)

Chaque mission doit contenir un frontmatter YAML incluant au minimum :

```yaml
---
id: YYYY-MM-DD-<slug>
type: mission
status: draft|queued|active|archived
priority: P0|P1|P2|P3
title: "..."
description: "..."
client: Villa Thaifa
requested-by: <name>
date-created: YYYY-MM-DD
tags:
  - thaifa
  - <related-tags>
---
```

---

## Compatibilité avec le système central

Un ancien système de missions existe dans :
`/home/omar/praxis/missions/`

Pour **éviter de casser** les outils existants, les fichiers Thaifa dans le système central sont remplacés par des **symlinks fichier-à-fichier** pointant vers ce dossier.

Exemple :
```
/home/omar/praxis/missions/active/2025-12-28-thaifa-chambre4-gouram.md
  → /home/omar/praxis/projects/clients/thaifa/missions/active/2025-12-28-thaifa-chambre4-gouram.md
```

---

## Règle d'or

1. Toutes les nouvelles missions Thaifa sont créées **ici**.
2. Le système central ne doit contenir que des **symlinks** pour Thaifa.
3. Les autres clients restent dans le système central (non impactés).

---

## Structure

```
missions/
├── active/           # Missions en cours (claimed)
├── queue/            # Prêtes à exécuter
├── drafts/           # Idées et brouillons
├── archive/          # Historique
├── _templates/       # Modèles de missions
└── README.md         # Ce fichier
```

---

## Commandes

- `/start` : Vérifie les missions actives, liste la queue, permet de claim
- `/sync` : Synchronise les apprentissages vers CLAUDE.md
- `/end` : Clôture la session proprement

---

_Villa Thaifa Missions — Migré le 2025-12-28_

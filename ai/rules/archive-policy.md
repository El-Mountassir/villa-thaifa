# Politique d'Archivage — OBLIGATOIRE

> **Pattern**: One Rule, One Behavior, One Purpose
>
> Cette règle s'applique à TOUS les agents, SANS EXCEPTION.

---

## Règle Fondamentale

> **JAMAIS SUPPRIMER. TOUJOURS ARCHIVER.**

Aucun fichier ne doit être supprimé définitivement. Tout contenu obsolète, remplacé, ou réorganisé doit être archivé avec traçabilité complète.

---

## Procédure

Avant de supprimer un fichier:

| Étape | Action | Détail |
|-------|--------|--------|
| 1 | **STOP** | Ne pas supprimer directement |
| 2 | **IDENTIFIER** | Où archiver? Quelle catégorie? |
| 3 | **DÉPLACER** | `git mv` vers `archive/YYYY/QX/[category]/` |
| 4 | **DOCUMENTER** | Noter la raison dans le message de commit |

---

## Structure Archive

```
archive/
└── YYYY/
    └── QX/
        ├── briefs/       # Briefings agents
        ├── changelogs/   # Historique changements
        ├── decisions/    # Décisions documentées
        ├── execution/    # Logs d'exécution (par date)
        ├── reports/      # Rapports (par sujet)
        ├── snapshots/    # États point-in-time
        └── [category]/   # Autres catégories selon besoin
```

**Convention de nommage**: `YYYY-MM-DD-description.md`

---

## Exceptions

**AUCUNE EXCEPTION.**

Si un fichier semble inutile:
1. Archiver quand même
2. Documenter pourquoi il semble obsolète
3. Laisser la décision finale à Omar

---

## Applicabilité

Cette règle s'applique à:
- Tous les sub-agents (browser-agent, meta-agent, explore-agent, etc.)
- L'orchestrateur principal
- Toute opération de nettoyage ou réorganisation

---

## Justification

| Raison | Description |
|--------|-------------|
| **Traçabilité** | Historique complet des changements |
| **Récupération** | Possibilité de restaurer si besoin |
| **Audit** | Preuves des décisions passées |
| **Apprentissage** | Référence pour éviter erreurs répétées |

---

_Politique créée: 2026-01-08 | Status: ACTIVE | Scope: ALL AGENTS_

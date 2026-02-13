# 🤖 Agent Workspace

> **RÈGLE ABSOLUE** : TOUS les agents AI (Claude, Gemini, Cursor, Copilot, etc.) DOIVENT stocker leurs artifacts ICI.
> **JAMAIS** dans `~/.claude/`, `~/.gemini/`, ou autre répertoire personnel.

## 📁 Structure

```
.agents/
├── plans/           # Plans d'implémentation (à valider par Omar)
├── artifacts/       # Documents de travail, audits, analyses
├── sessions/        # Résumés de sessions (YYYY-MM-DD-agent-topic.md)
├── memory/          # Contexte partagé entre agents
└── README.md        # Ce fichier
```

## 🔒 Règles pour TOUS les Agents

### 1. Création de Fichiers

- **Plans** → `.agents/plans/nom-du-plan.md`
- **Audits/Analyses** → `.agents/artifacts/nom-de-l-audit.md`
- **Résumés de Session** → `.agents/sessions/YYYY-MM-DD-agent-topic.md`

### 2. Nommage

- Utiliser des noms descriptifs en kebab-case
- Préfixer par la date si pertinent: `2026-01-29-room-audit.md`

### 3. Contenu Obligatoire

Chaque fichier doit commencer par:

```markdown
# [Titre]

> **Agent**: [Claude/Gemini/Cursor]
> **Date**: [YYYY-MM-DD]
> **Status**: [Draft/Review/Approved/Archived]
```

### 4. Cross-Reference

- Avant de créer un nouveau plan, LIRE les plans existants dans `.agents/plans/`
- Avant de commencer une tâche, VÉRIFIER `.agents/sessions/` pour le contexte récent

## 📋 Index des Documents Actifs

### Plans

| Fichier                                                                            | Description                         | Status |
| :--------------------------------------------------------------------------------- | :---------------------------------- | :----- |
| [comprehensive-transformation-plan.md](plans/comprehensive-transformation-plan.md) | Vision Owner Platform (Claude)      | Review |
| [implementation_plan_expedia.md](plans/implementation_plan_expedia.md)             | Expedia Browser Automation (Gemini) | Paused |

### Artifacts

| Fichier                                                    | Description                  | Agent  |
| :--------------------------------------------------------- | :--------------------------- | :----- |
| [app_readiness_audit.md](artifacts/app_readiness_audit.md) | Audit état actuel de l'app   | Gemini |
| [gemini_task_history.md](artifacts/gemini_task_history.md) | Historique des tâches Gemini | Gemini |
| [gemini_walkthrough.md](artifacts/gemini_walkthrough.md)   | Walkthrough Room Data        | Gemini |

## ⚠️ Ce qui NE DOIT PLUS arriver

❌ Claude stocke dans `/home/director/.claude/plans/`
❌ Gemini stocke dans `/home/director/.gemini/antigravity/brain/xxx/`
❌ Un agent ignore le travail d'un autre agent
❌ Duplication de plans ou d'analyses

✅ TOUT est dans `.agents/`
✅ TOUT est versionné avec Git
✅ TOUT est visible par TOUS les agents

# Journal des Décisions

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

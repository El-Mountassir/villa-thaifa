# Rapport : Framework de Résilience face aux Erreurs Techniques

**Date** : 2025-12-20
**Contexte** : Généralisation d'une leçon apprise (WebFetch 403 ignoré)

---

## Summary

Transformation d'une règle spécifique (WebFetch → Chrome) en un **framework de résilience universel** applicable à toutes les erreurs techniques. Inclut une hiérarchie de fallback et un pattern d'escalade structuré pour notifier l'humain en dernier recours.

---

## Key Insights

| Insight | Confiance | Sources |
|---------|-----------|---------|
| Ne jamais abandonner silencieusement | **Haute** | Toutes les sources |
| Hiérarchie : Alternative → Partial → Escalade | **Haute** | GoCodeo, AWS, CSA |
| Escalade = dernier recours, pas premier réflexe | **Haute** | Permit.io, CSA |
| Toujours retourner quelque chose d'utile | **Haute** | AWS, GoCodeo |

---

## Framework

### Règle fondamentale

> **Ne JAMAIS abandonner silencieusement face à une erreur technique.**
> Toujours tenter des alternatives, puis escalader à l'humain si aucune ne fonctionne.

### Hiérarchie de fallback

```
1. Méthode alternative (autre outil, autre approche)
2. Outil différent pour le même objectif
3. Résultat partiel (mieux que rien)
4. ESCALADE → Notifier avec contexte complet
```

### Matrice d'erreurs et fallbacks

| Contexte | Erreur | Fallback 1 | Fallback 2 | Escalade |
|----------|--------|------------|------------|----------|
| **Web** | WebFetch 403/timeout | Chrome navigate | get_page_text | "URL inaccessible, voici ce que j'ai tenté..." |
| **Fichiers** | Permission denied | sudo (si disponible) | Demander chemin alternatif | "Accès refusé, besoin d'intervention" |
| **Commandes** | Command not found | Chercher équivalent | Installer le package | "Outil manquant, voici les options..." |
| **API/Services** | Timeout/Rate limit | Retry avec backoff | Attendre et réessayer | "Service indisponible après X tentatives" |
| **Sub-agent** | Échec | Autre agent | Tenter moi-même | "Tâche échouée, contexte: ..." |

### Pattern d'escalade structuré

```markdown
⚠️ **Escalade requise**

**Objectif** : [Ce que je tentais de faire]
**Erreur** : [Message d'erreur exact]
**Tentatives** :
1. [Méthode 1] → [Résultat]
2. [Méthode 2] → [Résultat]

**Options possibles** :
- [Option A avec ses implications]
- [Option B avec ses implications]

**Recommandation** : [Si j'en ai une]
```

---

## Fichiers mis à jour

| Fichier | Changement |
|---------|------------|
| `~/rules/universal/behavior.md` | Section "Résilience face aux erreurs techniques" |
| `~/Documents/claude/memory/patterns.md` | Leçon généralisée avec sources |

---

## Sources

- [Permit.io - Human-in-the-Loop Best Practices](https://www.permit.io/blog/human-in-the-loop-for-ai-agents-best-practices-frameworks-use-cases-and-demo)
- [GoCodeo - Error Recovery and Fallback Strategies](https://www.gocodeo.com/post/error-recovery-and-fallback-strategies-in-ai-agent-development)
- [AWS - Build Resilient Generative AI Agents](https://aws.amazon.com/blogs/architecture/build-resilient-generative-ai-agents/)
- [CSA - Cognitive Degradation Resilience Framework](https://cloudsecurityalliance.org/blog/2025/11/10/introducing-cognitive-degradation-resilience-cdr-a-framework-for-safeguarding-agentic-ai-systems-from-systemic-collapse)

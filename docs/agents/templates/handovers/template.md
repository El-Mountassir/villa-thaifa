# Handover Template

> **Version**: 1.0
> **Date**: 2026-01-15
> **Usage**: Ce template est à utiliser POUR CHAQUE fin de session agent

---

## Instructions

COPIER ce template et remplir toutes les sections à la fin de chaque session.

**Nom du fichier**: `<agent>-<timestamp>.md`
**Exemple**: `pricing-analyst-20260115-1430.md`

---

## Template YAML

```yaml
---
handover_version: "1.0"
agent: <agent_name>
timestamp: <YYYY-MM-DD HH:mm>
session_id: <claude_session_id>

tasks_completed:
  - <task_1_description>
  - <task_2_description>
  # Ajouter autant de tâches que nécessaire

tasks_in_progress:
  - <task_if_any_1>
  - <task_if_any_2>
  # Mettre "None" si aucune tâche en cours

blocking_points:
  - <blocker_if_any_1>
  - <blocker_if_any_2>
  # Mettre "None" si aucun blocage

next_actions_for_next_agent:
  - <action_1>
  - <action_2>
  # Actions concrètes pour le prochain agent

files_modified:
  - <file_path_1>
  - <file_path_2>
  # Liste complète des fichiers modifiés

files_created:
  - <file_path_1>
  - <file_path_2>
  # Liste complète des fichiers créés

context_for_next_agent: |
  <Detailed context for next agent>
  - Expliquer ce qui a été fait
  - Expliquer ce qui reste à faire
  - Donner du contexte sur les décisions prises
  - Mentionner any gotchas ou problèmes connus

findings_for_cto: |
  <Technical findings, architectural decisions, system improvements>
  - Décisions techniques prises
  - Améliorations suggérées
  - Problèmes découverts
  - Leçons apprises
---
```

---

## Sections Expliquées

### 1. `tasks_completed`

Liste de toutes les tâches **terminées** pendant cette session.

**Exemple**:

```yaml
tasks_completed:
  - "Created CLAUDE.md with 3-minute read format"
  - "Standardized frontmatter for all 17 agents"
  - "Created docs/agents/registry.json with all agent metadata"
```

### 2. `tasks_in_progress`

Liste des tâches **en cours** mais pas terminées.

**Exemple**:

```yaml
tasks_in_progress:
  - "Fixing obsolete paths (el-mountassir → omar-el-mountassir)"
  - "Creating handover templates for agents"
```

### 3. `blocking_points`

Liste des **blocages** qui empêchent de continuer.

**Exemple**:

```yaml
blocking_points:
  - "Missing client information for Said Thaifa profile"
  - "Cannot access Booking.com API - credentials needed"
```

### 4. `next_actions_for_next_agent`

Actions **concrètes** que le prochain agent doit faire.

**Exemple**:

```yaml
next_actions_for_next_agent:
  - "Complete fixing obsolete paths in all .md files"
  - "Validate that all symlinks in docs/agents/context/mandatory/ work"
  - "Create capabilities JSON files for each agent"
```

### 5. `files_modified`

Liste **complète** des fichiers modifiés.

**Exemple**:

```yaml
files_modified:
  - ".claude/agents/pricing-analyst.md"
  - ".claude/agents/reservation-manager.md"
  # ... all 17 agents
```

### 6. `files_created`

Liste **complète** des fichiers créés.

**Exemple**:

```yaml
files_created:
  - "CLAUDE.md"
  - "docs/agents/registry.json"
  - "docs/knowledge/client/PROFILE.json"
  # ... etc
```

### 7. `context_for_next_agent`

Contexte **détaillé** pour le prochain agent. Utiliser le format `|` pour le multi-line.

**Exemple**:

```yaml
context_for_next_agent: |
  Contexte de la session:
  - Nous avons créé le système de prompts agentique pour Villa Thaifa
  - 17 agents ont maintenant un frontmatter standardisé avec:
    * agent_id, version, status, created, modified, created_by
    * context_to_load (mandatory, domain_specific, mission_specific)
    * dependencies, tools, output_format, domain, tags, changelog
  - Le registry.json est créé avec toutes les métadonnées des agents
  - Les placeholders sont créés dans docs/knowledge/ (client, property, processes, communications, finance, leadership)

  Ce qui reste à faire:
  - Fixer les chemins obsolètes (el-mountassir → omar-el-mountassir)
  - Restaurer 10 fichiers uniques depuis archive/
  - Organiser l'archive (legacy/history/restored)
  - Validation finale

  Gotchas:
  - Le fichier browser-agent.md a un chemin obsolète dans les instructions
  - Le fichier claude-md-agent.md référence /home/omar/omar-el-mountassir/ au lieu de /home/omar/omar-el-mountassir/
  - Vérifier tous les chemins avant validation
```

### 8. `findings_for_cto`

Décisions techniques et améliorations pour le CTO (Claude).

**Exemple**:

```yaml
findings_for_cto: |
  Décisions techniques prises:
  - Frontmatter standardisé avec structure YAML cohérente
  - Variables $DOCS/ pour référencer les paths relatifs
  - Registry en JSON pour interrogation programmatique
  - Système de handover standardisé pour continuité

  Améliorations suggérées:
  - Implémenter un système de résolution des variables $DOCS/
  - Créer un agent dédié à la validation des liens
  - Automatiser la création des handovers

  Problèmes découverts:
  - Chemins obsolètes el-mountassir dans plusieurs fichiers
  - Certains fichiers .md dans archive/ ne sont pas encore organisés
  - Plusieurs agents référencent des fichiers data/specs/ qui n'existent pas encore

  Leçons apprises:
  - Standardiser le frontmatter AVANT de créer les agents futurs
  - Utiliser des chemins absolus ou variables pour éviter problèmes
  - Documenter le format attendu des handovers dès le début
```

---

## Exemple Complet

```yaml
---
handover_version: "1.0"
agent: claude-sonnet-4.5
timestamp: 2026-01-15 14:30
session_id: b07900e4-2b83-4f37-aeb4-3edd794addc2

tasks_completed:
  - "Created complete backup of villa-thaifa project"
  - "Created docs/agents/ structure (context, handovers, capabilities)"
  - "Created CLAUDE.md as single entry point (3 min read)"
  - "Created docs/agents/registry.json with all 17 agents metadata"
  - "Created all knowledge folders with placeholders (client, property, processes, communications, finance)"
  - "Created leadership folder with VISION.md, DECISIONS.md, PRIORITIES.md, TEAM.md"
  - "Standardized frontmatter for all 17 agents"

tasks_in_progress:
  - "Fixing obsolete paths (el-mountassir → omar-el-mountassir)"
  - "Creating handover templates"

blocking_points:
  - "None"

next_actions_for_next_agent:
  - "Fix all obsolete paths containing 'el-mountassir' to 'omar-el-mountassir'"
  - "Validate all symlinks work correctly"
  - "Run validation tests per plan"
  - "Archive old files properly (legacy/history/restored)"

files_modified:
  - ".claude/agents/pricing-analyst.md"
  - ".claude/agents/reservation-manager.md"
  - ".claude/agents/calendar-agent.md"
  - ".claude/agents/platform-validator.md"
  - ".claude/agents/browser-agent.md"
  - ".claude/agents/guest-communicator.md"
  - ".claude/agents/meta-agent.md"
  - ".claude/agents/research-agent.md"
  - ".claude/agents/auditor.md"
  - ".claude/agents/security-auditor.md"
  - ".claude/agents/translation-agent.md"
  - ".claude/agents/data-sync-checker.md"
  - ".claude/agents/incident-reporter.md"
  - ".claude/agents/html-report-generator.md"
  - ".claude/agents/claude-md-agent.md"
  - ".claude/agents/smart-contract-auditor.md"
  - ".claude/agents/decision-evaluator.md"

files_created:
  - "CLAUDE.md"
  - "docs/agents/registry.json"
  - "docs/agents/handovers/template.md"
  - "docs/knowledge/INDEX.md"
  - "docs/knowledge/client/README.md"
  - "docs/knowledge/client/PROFILE.json"
  - "docs/knowledge/client/PREFERENCES.md"
  - "docs/knowledge/client/HISTORY.md"
  - "docs/knowledge/client/COMMUNICATION.md"
  - "docs/knowledge/property/README.md"
  - "docs/knowledge/property/VILLA_THAIFA.json"
  - "docs/knowledge/processes/README.md"
  - "docs/knowledge/processes/check-in-out.json"
  - "docs/knowledge/processes/housekeeping.json"
  - "docs/knowledge/processes/maintenance.json"
  - "docs/knowledge/processes/emergency.json"
  - "docs/knowledge/communications/README.md"
  - "docs/knowledge/communications/channels.json"
  - "docs/knowledge/communications/protocols.md"
  - "docs/knowledge/finance/README.md"
  - "docs/knowledge/finance/rates.json"
  - "docs/knowledge/finance/billing.json"
  - "docs/knowledge/finance/accounting.md"
  - "docs/leadership/README.md"
  - "docs/leadership/VISION.md"
  - "docs/leadership/DECISIONS.md"
  - "docs/leadership/PRIORITIES.md"
  - "docs/leadership/TEAM.md"

context_for_next_agent: |
  Nous avons terminé la création du système de prompts agentique pour Villa Thaifa.

  Ce qui a été fait:
  1. Backup complet du projet
  2. Structure docs/agents/ créée (context, handovers, capabilities)
  3. CLAUDE.md créé comme point d'entrée unique (3 min read)
  4. Registry.json créé avec toutes les métadonnées des 17 agents
  5. Dossiers knowledge créés avec placeholders (client, property, processes, communications, finance)
  6. Dossier leadership créé avec VISION, DECISIONS, PRIORITIES, TEAM
  7. Frontmatter standardisé pour tous les 17 agents avec:
     - agent_id, version, status, created, modified, created_by
     - context_to_load (mandatory, domain_specific, mission_specific)
     - dependencies, tools, output_format, domain, tags, changelog

  Ce qui reste à faire:
  1. Fixer les chemins obsolètes (el-mountassir → omar-el-mountassir)
  2. Valider tous les symlinks fonctionnent
  3. Restaurer 10 fichiers uniques depuis archive/
  4. Organiser l'archive (legacy/history/restored)
  5. Validation finale

  Gotchas:
  - Certains fichiers ont encore des chemins el-mountassir
  - Les symlinks dans docs/agents/context/mandatory/ ne sont pas encore créés
  - Les fichiers capabilities JSON n'existent pas encore

findings_for_cto: |
  Architecture implémentée:
  - Système modulaire avec frontmatter standardisé
  - Variables $DOCS/ pour référence flexible
  - Registry JSON pour interrogation programmatique
  - Système de handover standardisé

  Points positifs:
  - Frontmatter cohérent permet parsing automatisé
  - Structure claire avec 3 niveaux de contexte
  - Registry permet génération inventory automatisée

  Améliorations possibles:
  - Implémenter résolveur de variables $DOCS/
  - Créer agent validation-links
  - Automatiser création handovers

  Problèmes identifiés:
  - Chemins obsolètes dans browser-agent.md et claude-md-agent.md
  - Plusieurs fichiers data/specs/ référencés mais inexistants
  - Archive de 103 fichiers à organiser

  Leçons apprises:
  - Standardiser AVANT de créer
  - Utiliser chemins absolus ou variables
  - Documenter format handover dès début
---
```

---

## Validation Checklist

Avant de sauvegarder le handover, vérifier:

- [ ] Toutes les sections sont remplies
- [ ] `tasks_completed` liste toutes les tâches terminées
- [ ] `files_modified` liste TOUS les fichiers modifiés
- [ ] `files_created` liste TOUS les fichiers créés
- [ ] `context_for_next_agent` est détaillé et utile
- [ ] `findings_for_cto` contient décisions techniques
- [ ] Le nom du fichier suit le format `<agent>-<timestamp>.md`

---

**Tags**: `handover` `template` `agent` `session`

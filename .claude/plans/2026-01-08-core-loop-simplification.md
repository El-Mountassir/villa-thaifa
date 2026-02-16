# Plan: Simplification Workflow — CORE LOOP Unifie

> **Objectif**: Un seul workflow global pour bien travailler ensemble.
> **Approche**: Archiver la fragmentation, simplifier CLAUDE.md autour du CORE LOOP.
> **Statut**: Plan preserve (originalement dans ~/.claude/plans/)
> **Date**: 2026-01-08

---

## Phase 1: ARCHIVAGE — Nettoyer la Fragmentation

### Creer dossier d'archive
```
.archived/
├── rules/
├── workflows/
├── agents/
├── patterns/
├── strategic/
└── research/
```

### Fichiers a archiver

| Source | Destination | Raison |
|--------|-------------|--------|
| `ai/rules/README.md` | `.archived/rules/` | Duplique dans CLAUDE.md |
| `docs/workflows/CLAUDE.md` | `.archived/workflows/` | Meta-wrapper inutile |
| `docs/workflows/pricing.md` | `.archived/workflows/` | Consolider dans operations |
| `docs/workflows/reservation.md` | `.archived/workflows/` | Consolider dans operations |
| `docs/workflows/guest-communication.md` | `.archived/workflows/` | Consolider dans operations |
| `.claude/agents/html-report-generator.md` | `.archived/agents/` | Theorique, jamais utilise |
| `docs/patterns/` | `.archived/patterns/` | Trop tot (1 seul pattern) |
| `docs/strategic/` | `.archived/strategic/` | Consolider |
| `docs/research/` | `.archived/research/` | Integrer findings puis archiver |

### Nettoyer references
- Mettre a jour `ai/registry/sub-agent_registry.md` (retirer html-report-generator)
- Retirer reference a `ai/rules/README.md` dans CLAUDE.md

---

## Phase 2: NOUVEAU CLAUDE.md — Structure Simplifiee

### Objectif
Reduire de **744 lignes** a **~200 lignes** maximum.

### Nouvelle Structure

```markdown
# Villa Thaifa — Context

## Identite
- Qui: Claude Opus 4.5, Orchestrateur
- Pour: Villa Thaifa (12 chambres, Marrakech)
- Sous: Omar El Mountassir (Root Authority)

## CORE LOOP — Le Workflow Unique

┌─────────────────────────────────────────────────────────┐
│  1. COMPRENDRE  →  2. EXPLORER  →  3. CLARIFIER         │
│       ↑                                    ↓            │
│       └──────────── (si < 94%) ────────────┘            │
│                                    ↓                    │
│  6. REPORTER   ←  5. VERIFIER  ←  4. EXECUTER           │
└─────────────────────────────────────────────────────────┘

### Etapes detaillees
1. COMPRENDRE: Qu'est-ce qu'on me demande?
2. EXPLORER: Quel contexte? Quoi existe deja?
3. CLARIFIER: Confiance ≥ 94%? Sinon → AskUserQuestion
4. EXECUTER: Deleguer aux sub-agents appropries
5. VERIFIER: C'est bien fait? Ca marche?
6. REPORTER: Communiquer le resultat (en francais)

## Regle d'Or
Si confiance < 94% → STOP → AskUserQuestion → Attendre reponse

## Agents Disponibles
@ai/registry/sub-agent_registry.md

## Communication
| A qui | Langue | Registre |
|-------|--------|----------|
| Omar | Francais | Direct |
| M. Thaifa | Francais | Vous (formel) |
| Code/Config | Anglais | Technique |

## Donnees
| Type | Emplacement |
|------|-------------|
| Chambres | data/specs/configs/hotel/ |
| Reservations | data/specs/state/current/ |
| Platform | data/specs/platform/ |

## Incidents
Tout incident → docs/incidents/open/YYYY-MM-DD-description.md

## Checklist Plateforme
Avant action HotelRunner/Booking.com:
- [ ] Confiance ≥ 94%?
- [ ] Details repetes a Omar?
- [ ] Valeurs exactes (pas calculees)?
```

### Ce qui est GARDE (sections detaillees)
- Sub-Agent Report Protocol (SUCCESS/FAILURE/PARTIAL) → Essentiel pour les agents
- Git Workflow (commit/push discipline) → Essentiel pour la qualite

### Ce qui est SUPPRIME (consolide)
- Briefing Protocol detaille → Resume en 3 lignes
- Agent Selection Decision Tree → Reference au registry
- Error Recovery Patterns → Garde seulement Circuit Breaker
- MCP Activation Protocol → Implicite
- Parallel Execution Protocol → Implicite
- Zero Tolerance Protocol detaille → Integre dans CORE LOOP (regle 94%)

---

## Phase 3: FICHIERS A GARDER (Core)

| Fichier | Role | Action |
|---------|------|--------|
| `CLAUDE.md` | Gouvernance unique | REECRIRE (simplifie) |
| `ai/registry/sub-agent_registry.md` | Registry agents | GARDER (mettre a jour) |
| `.claude/agents/browser-agent.md` | Chrome automation | GARDER |
| `.claude/agents/meta-agent.md` | Creation agents | GARDER |
| `.claude/agents/claude-md-agent.md` | Maintenance CLAUDE.md | GARDER |
| `.claude/agents/research-agent.md` | Recherche web | GARDER |
| `docs/lessons-learned.md` | Sagesse operationnelle | GARDER |
| `docs/incidents/` | Tracking incidents | GARDER |
| `project/TODOs.md` | Mission board | GARDER |
| `data/specs/` | Etat & config | GARDER (intouche) |
| `data/specs/platform/rules.md` | Regles plateforme | GARDER (reference) |

---

## Phase 4: EXECUTION — Ordre des Operations

### Etape 1: Creer structure d'archive
```bash
mkdir -p .archived/{rules,workflows,agents,patterns,strategic,research}
```

### Etape 2: Deplacer fichiers (git mv)
```bash
# Rules
git mv ai/rules/README.md .archived/rules/

# Workflows
git mv docs/workflows/CLAUDE.md .archived/workflows/
git mv docs/workflows/pricing.md .archived/workflows/
git mv docs/workflows/reservation.md .archived/workflows/
git mv docs/workflows/guest-communication.md .archived/workflows/

# Agents
git mv .claude/agents/html-report-generator.md .archived/agents/

# Patterns
git mv docs/patterns/ .archived/

# Strategic
git mv docs/strategic/ .archived/

# Research
git mv docs/research/ .archived/
```

### Etape 3: Mettre a jour sub-agent_registry.md
- Retirer entree html-report-generator
- Garder: browser-agent, meta-agent, claude-md-agent, research-agent, explore-agent

### Etape 4: Reecrire CLAUDE.md
- Utiliser le template Phase 2
- ~200 lignes max
- CORE LOOP en vedette
- References (pas duplication)

### Etape 5: Commit
```bash
git add -A
git commit -m "refactor: simplify workflow to unified CORE LOOP

- Archive fragmented rules, workflows, patterns
- Simplify CLAUDE.md from 744 to ~200 lines
- Establish single CORE LOOP workflow
- Remove unused html-report-generator agent

Co-authored-by: Claude Opus 4.5 <noreply@anthropic.com>"
```

---

## Phase 5: VERIFICATION

### Test du nouveau workflow
1. Lire CLAUDE.md → Comprehensible en < 2 min?
2. Trouver un agent → Registry clair?
3. Savoir quoi faire → CORE LOOP evident?
4. Ou sont les donnees → Tableau clair?

### Criteres de succes
- [ ] CLAUDE.md < 250 lignes
- [ ] CORE LOOP visible immediatement
- [ ] Aucune duplication de regles
- [ ] Tous fichiers archives avec git mv
- [ ] Registry a jour (4 agents actifs)

---

## Resume

**Avant**: 744 lignes CLAUDE.md + 10 fichiers de regles disperses = Confusion

**Apres**: ~200 lignes CLAUDE.md + 1 CORE LOOP + references = Clarte

**Principe**: Un workflow, six etapes, toujours pareil.

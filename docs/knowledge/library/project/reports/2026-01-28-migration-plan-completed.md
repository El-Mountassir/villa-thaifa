# Plan: Migration Projet Villa Thaifa vers Grid

> **Agent**: Claude Code CLI
> **Date**: 2026-01-28
> **Status**: COMPLETED
> **Archived**: 2026-01-29
> **Outcome**: Migration successful, project now at `~/grid/clients/villa-thaifa/property-management/`

---

**Original Plan Below** (preserved for historical reference)

---

**Date**: 2026-01-28
**Status**: FINAL

## Contexte

| Élément | Valeur |
|---------|--------|
| **Source** | `/media/director/data/home/omar/clients/villa-thaifa` |
| **Destination** | `~/grid/clients/villa-thaifa/property-management/` |
| **GitHub** | `https://github.com/omar-elmountassir/villa-thaifa.git` |
| **Méthode** | `mv` (déplacer, pas copier) |

## État Actuel du Repo (Micron)

- **Branche**: `develop`
- **28 commits non pushés** vers origin/develop
- **8 fichiers modifiés** non committés
- **Fichiers gitignored critiques**:
  - `.env.local` (5.6KB - credentials HotelRunner/Booking)
  - `node_modules/` (475MB)
  - `.next/` (240MB)
  - `sessions/` (transcriptions)
  - `.claude/settings.local.json`

---

## Plan d'Exécution

### Phase 1: Préparation Git (sur Micron AVANT move)

| # | Action | Commande | Raison |
|---|--------|----------|--------|
| 1.1 | Committer les changements | `git add -A && git commit -m "..."` | Sauvegarder le travail en cours |
| 1.2 | Pusher vers GitHub | `git push origin develop` | Sync les 28+ commits avant move |
| 1.3 | Vérifier sync | `git status` | Confirmer "up to date" |

### Phase 2: Création Structure Grid

| # | Action | Commande |
|---|--------|----------|
| 2.1 | Créer répertoire clients | `mkdir -p ~/grid/clients/villa-thaifa` |
| 2.2 | Créer INDEX.md | Écrire `~/grid/clients/INDEX.md` |

### Phase 3: Migration (MOVE)

| # | Action | Commande |
|---|--------|----------|
| 3.1 | Déplacer le projet | `mv /media/director/data/home/omar/clients/villa-thaifa ~/grid/clients/villa-thaifa/property-management` |
| 3.2 | Vérifier intégrité | `ls -la ~/grid/clients/villa-thaifa/property-management/` |
| 3.3 | Vérifier Git intact | `cd ~/grid/clients/villa-thaifa/property-management && git status` |

### Phase 4: Mise à Jour Documentation Grid

| # | Action | Fichier |
|---|--------|---------|
| 4.1 | Ajouter clients/ aux permissions | `~/grid/CLAUDE.md` |
| 4.2 | Créer profil client | `~/grid/clients/villa-thaifa/CLIENT.md` |
| 4.3 | Créer synthèse comms | `~/grid/comms/clients/villa-thaifa.md` |
| 4.4 | Créer backlog entry | `~/grid/workstream/backlog/villa-thaifa-resume.md` |

### Phase 5: Vérification Finale

| # | Action | Commande |
|---|--------|----------|
| 5.1 | Test Git remote | `git fetch origin` |
| 5.2 | Vérifier .env intact | `cat .env.local \| head -5` |
| 5.3 | Test npm/pnpm | `pnpm install --frozen-lockfile` (optionnel) |

---

## Vérification Post-Migration

- [x] Git fonctionne (`git status`, `git log`, `git fetch`)
- [x] Remote GitHub intact
- [x] `.env.local` présent avec credentials
- [x] `node_modules/` présent
- [x] Structure projet intacte

---

## Risques et Mitigations

| Risque | Probabilité | Mitigation |
|--------|-------------|------------|
| Move interrompu | Faible | Le Micron reste monté, retry possible |
| Permissions cassées | Faible | `chown -R director:director` si nécessaire |
| Git remote perdu | Très faible | Remote est dans `.git/config`, préservé par mv |

---

## Ordre d'Exécution

```
1. Git commit + push (sur Micron) ← CRITIQUE avant move
2. Créer structure ~/grid/clients/
3. mv projet
4. Vérifier intégrité
5. Créer documentation
6. Mettre à jour CLAUDE.md
```

---

**COMPLETION NOTES (2026-01-29)**:

All tasks completed successfully. The Villa Thaifa project is now located at:
`~/grid/clients/villa-thaifa/property-management/`

Subsequent work (database setup, admin dashboard, agent unification) documented in:
- `.agents/sessions/2026-01-29-agent-unification.md`
- `.agents/plans/comprehensive-transformation-plan.md`

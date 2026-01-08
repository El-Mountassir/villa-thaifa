# Changelog — Villa Thaifa

## Migration

**Date** : 2025-12-28T16:28:23Z
**Opérateur** : Claude Code (session agentique)

---

## Résumé

Migration des missions Villa Thaifa depuis le système central vers le dossier client, avec symlinks fichier-à-fichier pour compatibilité arrière.

---

## Fichiers migrés (7)

### Active (2)

| Fichier                                            | Priorité | Statut            |
| -------------------------------------------------- | -------- | ----------------- |
| `2025-12-28-thaifa-chambre4-gouram.md`             | P1       | ✓ Migré + Symlink |
| `2025-12-28-thaifa-chambre5-sync-investigation.md` | P0       | ✓ Migré + Symlink |

### Queue (1)

| Fichier                                      | Priorité | Statut            |
| -------------------------------------------- | -------- | ----------------- |
| `2025-12-28-thaifa-hotelrunner-api-scout.md` | P2       | ✓ Migré + Symlink |

### Drafts (4)

| Fichier                                   | Priorité | Statut            |
| ----------------------------------------- | -------- | ----------------- |
| `2025-12-23-thaifa-booking-data.md`       | P2       | ✓ Migré + Symlink |
| `2025-12-23-thaifa-image-organization.md` | P2       | ✓ Migré + Symlink |
| `2025-12-23-thaifa-room-restructuring.md` | P1       | ✓ Migré + Symlink |
| `2025-12-23-thaifa-validation-pdf.md`     | P3       | ✓ Migré + Symlink |

---

## Fichiers ignorés

Aucun — toutes les missions Thaifa étaient clairement identifiées.

---

## Fichiers incertains

Aucun — pas d'ambiguïté dans l'identification.

---

## Backup

Emplacement : `.migration_backups/2025-12-28T162823Z/`

Contenu : 7 fichiers (copie complète avant modification)

---

## Symlinks créés dans le système central

| Central                                                                              | →   | Client                                                               |
| ------------------------------------------------------------------------------------ | --- | -------------------------------------------------------------------- |
| `/home/omar/praxis/missions/active/2025-12-28-thaifa-chambre4-gouram.md`             | →   | `./missions/active/2025-12-28-thaifa-chambre4-gouram.md`             |
| `/home/omar/praxis/missions/active/2025-12-28-thaifa-chambre5-sync-investigation.md` | →   | `./missions/active/2025-12-28-thaifa-chambre5-sync-investigation.md` |
| `/home/omar/praxis/missions/queue/2025-12-28-thaifa-hotelrunner-api-scout.md`        | →   | `./missions/queue/2025-12-28-thaifa-hotelrunner-api-scout.md`        |
| `/home/omar/praxis/missions/drafts/2025-12-23-thaifa-booking-data.md`                | →   | `./missions/drafts/2025-12-23-thaifa-booking-data.md`                |
| `/home/omar/praxis/missions/drafts/2025-12-23-thaifa-image-organization.md`          | →   | `./missions/drafts/2025-12-23-thaifa-image-organization.md`          |
| `/home/omar/praxis/missions/drafts/2025-12-23-thaifa-room-restructuring.md`          | →   | `./missions/drafts/2025-12-23-thaifa-room-restructuring.md`          |
| `/home/omar/praxis/missions/drafts/2025-12-23-thaifa-validation-pdf.md`              | →   | `./missions/drafts/2025-12-23-thaifa-validation-pdf.md`              |

---

## Intégrité vérifiée

Tous les fichiers ont été vérifiés avec `sha256sum` avant remplacement par symlinks.

---

## Autres clients

**Aucun impact** — les missions des autres clients restent dans le système central, non modifiées.

---

## Prochaines étapes

1. ✅ Tester `/start` depuis le dossier client
2. ✅ Vérifier que le système central résout correctement les symlinks
3. Optionnel : Créer `.agent/context.yaml` pour détection automatique du mode local

---

_Migration terminée avec succès._

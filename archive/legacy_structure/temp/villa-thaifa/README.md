# README — Villa Thaifa

> **Hub central** — Point d'entrée pour naviguer le projet.

---

## Quick Access

| Fichier                      | Purpose                     |
| ---------------------------- | --------------------------- |
| [CLAUDE.md](CLAUDE.md)       | Context pour Claude Code    |
| [AGENTS.md](AGENTS.md)       | Standard multi-agent (2025) |
| [ROADMAP.md](ROADMAP.md)     | Vision stratégique 4 phases |
| [STRUCTURE.md](STRUCTURE.md) | Arborescence auto-générée   |

---

## Data (SSOT)

> **Source of Truth** : Toutes les données dans `data/`

### Specs (Configuration Métier)

| Fichier                                                | Contenu                     |
| ------------------------------------------------------ | --------------------------- |
| [data/specs/hotel/rooms.md](data/specs/hotel/rooms.md) | Chambres, tarifs, capacités |
| [data/specs/promotions/](data/specs/promotions/)       | Promotions actives          |
| [data/specs/platform/](data/specs/platform/)           | Règles plateformes          |

### Admin

| Fichier                                                      | Contenu                                                |
| ------------------------------------------------------------ | ------------------------------------------------------ |
| [.env.example](.env.example)                                 | Structure credentials (voir .env pour valeurs réelles) |
| [data/admin/client/CONTACT.md](data/admin/client/CONTACT.md) | Contacts (M. Thaifa, Ikram)                            |
| [data/admin/client/PROFILE.md](data/admin/client/PROFILE.md) | Profil client complet                                  |

### Communication

| Dossier                                                      | Contenu           |
| ------------------------------------------------------------ | ----------------- |
| [data/communication/whatsapp/](data/communication/whatsapp/) | Messages WhatsApp |

---

## Documentation

| Fichier                                            | Purpose                              |
| -------------------------------------------------- | ------------------------------------ |
| [docs/INDEX.md](docs/INDEX.md)                     | Index documentation                  |
| [docs/lessons-learned.md](docs/lessons-learned.md) | Erreurs passées ⚠️ LIRE AVANT ACTION |
| [docs/templates/](docs/templates/)                 | Templates PDF, rapports              |
| [docs/briefs/](docs/briefs/)                       | Mission briefs pour agents IA        |

---

## Workflows

| Workflow                                                                       | Description                     |
| ------------------------------------------------------------------------------ | ------------------------------- |
| [docs/workflows/reservation.md](docs/workflows/reservation.md)                 | Process réservation HotelRunner |
| [docs/workflows/pricing.md](docs/workflows/pricing.md)                         | Mise à jour tarifs              |
| [docs/workflows/guest-communication.md](docs/workflows/guest-communication.md) | Communication invités           |

---

## Autres

| Dossier              | Contenu                                       |
| -------------------- | --------------------------------------------- |
| [archive/](archive/) | Archives (YYYY/QQ/)                           |
| [ai/](ai/)           | Systèmes IA (agentic, rag, knowledge, memory) |
| [src/](src/)         | Code source (apps, packages, tools)           |
| [infra/](infra/)     | Infrastructure (docker, envs)                 |
| [project/](project/) | Gestion projet (TODOs)                        |
| [.claude/](.claude/) | Config Claude (commands, rules)               |

---

## Règles Critiques

| Règle               | Fichier                                                                                                    |
| ------------------- | ---------------------------------------------------------------------------------------------------------- |
| Platform Operations | [rules/universal/ops/platform/platform-operations.md](rules/universal/ops/platform/platform-operations.md) |
| Lessons Learned     | [docs/lessons-learned.md](docs/lessons-learned.md)                                                         |

> **AVANT toute action client** : Lire `docs/lessons-learned.md`

---

_*README v2.0.0 — Hub central Villa Thaifa (v5 structure)*_

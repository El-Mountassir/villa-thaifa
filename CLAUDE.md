# Villa Thaifa — Project Context

> **Herite de**: @../../CLAUDE.md (CORE LOOP, Regle d'Or, Protocoles)
> **Structure**: EaC + Agentic AI (v5)

---

## Identite Projet

| Attribut   | Valeur                                           |
| ---------- | ------------------------------------------------ |
| **Projet** | Villa Thaifa (12 chambres, Marrakech)            |
| **Client** | M. Said Thaifa                                   |
| **Mode**   | Delegation-first — minimiser l'execution directe |

---

## Agents Disponibles

@ai/inventory/sub-agent_registry.md

| Agent             | Quand l'utiliser                             |
| ----------------- | -------------------------------------------- |
| `browser-agent`   | Automation Chrome (HotelRunner, Booking.com) |
| `explore-agent`   | Recherche codebase, patterns                 |
| `research-agent`  | Recherche web, documentation                 |
| `meta-agent`      | Creer nouveaux agents                        |
| `claude-md-agent` | Maintenance CLAUDE.md                        |

---

## Briefing Sub-Agents

Chaque brief DOIT inclure:

1. **Objectif** — Ce qui doit etre fait
2. **Fichiers** — Chemins absolus
3. **Contraintes** — Standards de qualite
4. **Output attendu** — Format et destination
5. **Report Protocol** — @../../collective/memory/procedural/sub-agent-report-protocol.md

---

## Communication Specifique

| A qui         | Langue   | Registre          |
| ------------- | -------- | ----------------- |
| Omar          | Francais | Direct            |
| **M. Thaifa** | Francais | **Vous (formel)** |
| Code/Config   | Anglais  | Technique         |

> **REGLE**: TOUJOURS repondre en francais a Omar et M. Thaifa.

---

## Donnees

| Type              | Emplacement                                |
| ----------------- | ------------------------------------------ |
| Chambres          | `data/specs/configs/hotel/`                |
| Reservations      | `data/specs/state/current/reservations.md` |
| Tarifs            | `data/specs/state/planned/pricing.md`      |
| Regles plateforme | `data/specs/platform/rules.md`             |
| Credentials       | `.env` (local)                             |
| Client            | `data/admin/client/PROFILE.md`             |

---

## Checklist Plateforme

Avant toute action sur HotelRunner/Booking.com:

- [ ] Confiance >= 94%?
- [ ] Details repetes a Omar? (dates, chambre, prix)
- [ ] Valeurs exactes copiees? (jamais calculees)
- [ ] Screenshot avant/apres si modification?

> Details: `data/specs/platform/rules.md`

---

## Incidents

Tout incident → `docs/incidents/open/YYYY-MM-DD-HHmm-description.md`

| Icone | Niveau   | Signification                 |
| ----- | -------- | ----------------------------- |
| 🔴    | Critical | Bloque tout, donnees a risque |
| 🟠    | Major    | Bloque tache courante         |
| 🟡    | Minor    | Workaround disponible         |
| 🔵    | Info     | FYI, pas d'impact             |

> Format complet: @../../collective/memory/procedural/incident-tracking.md

---

## References Locales

| Document                             | Contenu                        |
| ------------------------------------ | ------------------------------ |
| `docs/lessons-learned.md`            | Erreurs passees et corrections |
| `data/specs/platform/rules.md`       | Regles operations plateforme   |
| `ai/inventory/sub-agent_registry.md` | Registry des agents            |

> **LIRE `docs/lessons-learned.md` AVANT toute action client**

---

## Contacts

| Role  | Nom                | Contact                        |
| ----- | ------------------ | ------------------------------ |
| Owner | M. Said Thaifa     | `data/admin/client/CONTACT.md` |
| Admin | Omar El Mountassir | omar@el-mountassir.com         |

---

_Villa Thaifa Project — Herite de @../../CLAUDE.md_

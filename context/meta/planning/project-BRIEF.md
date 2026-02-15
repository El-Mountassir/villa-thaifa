# Brief Villa Thaifa

## Metadata

— Session 2026-01-08 (12h-14h)

## État Actuel

| Aspect       | Status                                                                                                                                                                     |
| ------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Contrat**  | ❌ AUCUN — Formalisation urgente                                                                                                                                           |
| **Phase**    | 1 (Cleanup & Fondation) — En cours                                                                                                                                         |
| **Repo**     | 329 fichiers, pas bien structuré - une refonte complète est obligatoire et avoir une app avec db, frontend, backend etc // S'inspirer / réutiiliser les démos d'IndyDevDan |
| **Code app** | ❌ INEXISTANT — Système doc/ops uniquement                                                                                                                                 |

---

## Leçons Passées (À Retenir)

1. **Scout → Rapport → Questions → Action** — Toujours rapporter les découvertes AVANT de demander des infos
2. **Ton formel avec M. Thaifa** — Vouvoiement obligatoire, respect des aînés
3. **Livrables prêts à l'emploi** — `.txt` pour WhatsApp, pas `.md` avec métadonnées
4. **Économie commissions** — Direct = 0%, Booking = 25% perdu (impact MASSIF)
5. **Anti Tunnel Vision** — Zoom out avant de crier "bug"
6. **94% confidence rule** — Si < 94% confiance → STOP & ASK Omar

---

## Ce Qui Manque Pour "Transformer en App"

### Option A: App Web de Gestion

```sh
villa-thaifa-app/
├── frontend/          # React/Next.js dashboard
│   ├── reservations/  # Vue calendrier
│   ├── pricing/       # Gestion tarifs
│   └── reports/       # Analytics
├── backend/           # API Node/Python
│   ├── hotelrunner/   # Intégration API (create an MCP for our agents??)
│   ├── booking/       # Sync Booking.com  (do they have an MCP for our agents??)
│   └── .../           # Sync all other plateforms (do they have an MCP for our agents??)
└── mobile/            # PWA ou React Native ## PAS LA PRIORITé !!
```

### Option B: Automation-First (Plus réaliste court-terme)

```sh
Garder structure actuelle + ajouter:
├── scripts/
│   ├── sync-hotelrunner.py    # API automation
│   ├── daily-report.py        # Rapports auto
│   └── notification-bot.py    # WhatsApp/Telegram
└── infra/
    └── cron/                   # Scheduled tasks
```

### Option C: Hybrid (Recommandé)

1. **Court-terme**: Scripts automation sur structure existante
2. **Moyen-terme**: Dashboard web simple (Streamlit/Gradio)
3. **Long-terme**: Full app avec backend API

---

## Priorités Demain 12h

### P0 — Décisions Stratégiques

1. **App ou Automation d'abord?** (Option A/B/C)
2. **Contrat M. Thaifa** — Quand?
3. **Go Siyaha** — Financement 90% — Investiguer?

### P1 — Technique

1. **API HotelRunner** — Statut demande à Ikram?
2. **Stack technique** — Si app: Next.js? Python? Autre?
3. **IndyDevDan curriculum** — Quoi utiliser?

### P2 — Organisation

1. **Lien el-mountassir → villa-thaifa** — Comment intégrer?
2. **Vibe Kanban** — Pour gestion missions?

---

## Questions Ouvertes

1. "Transformer en app" = quoi exactement?
   [x] Dashboard web de gestion pour M. Thaifa et pour nous (Omar + agents IA)
   [?] Scripts automation backend ? Pourquoi pas à voir si on peut combiner le tout

2. Quelle est la timeline réaliste?
   [x] Cette semaine (Preuve de Concept/ Minimum Viable Product fonctionnel / Minimum Lovable Product/ prototype rapide)

3. API HotelRunner — Réponse d'Ikram?
   [x] Oui, accès obtenu https://developers.hotelrunner.com/

---

## Ressources

### Resources Disponibles

| Ressource               | Location    | Usage                      |
| ----------------------- | ----------- | -------------------------- |
| IndyDevDan curriculum   | À localiser | Patterns agent             |
| Vibe Kanban             | À activer   | Gestion projet             |
| Core Four               | ops/        | Model/Context/Prompt/Tools |
| docs/lessons-learned.md | Ce repo     | Erreurs à éviter           |

---

## North Star

> **Un M-Shaped Generalist + agents IA = gestion complète de 10+ établissements hôteliers.**

Villa Thaifa = premier établissement template.

---

_*Préparé par Claude Code — 2026-01-08 01:30*_

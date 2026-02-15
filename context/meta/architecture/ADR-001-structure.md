# ADR-001: Architecture Structure - Domains vs Areas

> **Date**: 2026-01-12
> **Status**: ACCEPTED
> **Deciders**: Omar, Antigravity
> **Context**: Definition of the future codebase structure for Villa Thaifa PMS.

## 1. Contexte

Nous construisons une plateforme de **Property Management System (PMS)**.
Ce n'est pas un simple site vitrine ("Experience"), c'est un outil de gestion ("Business Truth").

Les fonctionnalités clés sont :

- **Réservations** (Règles conditionnelles, conflits de dates)
- **Tarification** (Saisons, promos, calculs complexes)
- **Channel Manager** (Synchro HotelRunner, Mapping)
- **Finance** (Revenus, Dépenses)

## 2. Options

### Option A: `src/areas/` (Feature/UI Driven)

- Organisation par écran : `Dashboard`, `Settings`, `BookingPage`.
- **Avantage** : Facile pour faire des vues rapides.
- **Inconvénient** : La logique métier (ex: "Calculer prix") se retrouve dupliquée ou cachée dans les contrôleurs de vue.

### Option B: `src/domains/` (Domain Driven - RECOMMENDED)

- Organisation par "Vérité Métier" : `Reservations`, `Pricing`, `Channels`.
- **Avantage** :
  - La logique de "Comment on calcule un prix" est isolée de "Comment on l'affiche".
  - Indispensable pour un système qui va avoir plusieurs interfaces (Web, WhatsApp Bot, API interne).
  - Future-proof pour l'IA (Les agents comprennent mieux les concepts isolés).

## 3. Décision Recommandée : `domains/`

Nous choisissons l'approche **Domain-Driven** car Villa Thaifa est un projet à forte densité de règles métier.

### Structure Cible (Draft)

```text
src/
├── domains/
│   ├── booking/        (Logique de réservation, Dispos)
│   ├── pricing/        (Saisons, Promos, Calculs)
│   ├── inventory/      (Chambres, Maintenance)
│   └── accounting/     (Revenus, Factures)
├── apps/               (Nos interfaces / Areas)
│   ├── admin-web/      (Dashboard React/Next)
│   └── whatsapp-bot/   (Agent conversationnel)
└── core/               (Infra partagée, DB)
```

## 4. Stack Technique (À Définir)

Cette structure fonctionne bien avec :

- **Backend / API** : Node.js (NestJS ou Hono) ou Python (FastAPI).
- **Frontend** : Next.js ou Vite.

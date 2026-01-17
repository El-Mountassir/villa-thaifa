---
id: 2025-12-29-hotelrunner-admin-access
type: mission
status: queued
priority: P1
title: "Obtenir accès admin HotelRunner pour Omar"
description: "Contacter le support HotelRunner pour demander/configurer l'accès admin pour omar@el-mountassir.com"
client: Villa Thaifa
requested-by: Omar
date-created: 2025-12-29
tags:
  - thaifa
  - hotelrunner
  - admin
  - credentials
---

# Obtenir accès admin HotelRunner pour Omar

## Contexte

Dans le fichier `.env`, on a configuré:

```
HOTELRUNNER_ADMIN_EMAIL=omar@el-mountassir.com
HOTELRUNNER_ADMIN_PASSWORD=Na5%a?h5c9Rm2+K
```

Cependant, cet accès admin n'est **pas encore actif**. Il faut contacter le support HotelRunner pour le configurer.

## Objectif

Contacter le support HotelRunner pour:

1. Demander comment ajouter un admin supplémentaire (omar@el-mountassir.com)
2. Ou demander s'il faut une procédure spécifique
3. Obtenir les instructions/confirmation

## Actions requises

- [x] Contacter Ikram (support HWS) — voir `data/admin/client/CONTACT.md`
- [ ] Expliquer le besoin: ajouter un compte admin pour Omar
- [ ] Obtenir les instructions ou confirmation
- [ ] Mettre à jour `.env` si les credentials changent
- [ ] Tester la connexion

## Ressources

- Contact support: voir `data/admin/client/CONTACT.md`
- Credentials actuels: voir `.env`
- Documentation HotelRunner: voir `data/specs/platform/hotelrunner/`

## Notes

Cette mission est **bloquante** pour les opérations automatisées sur HotelRunner avec le compte Omar. En attendant, on peut utiliser le compte de M. Thaifa si nécessaire.

---

_Créé: 2025-12-29_

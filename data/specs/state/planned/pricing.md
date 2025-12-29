# Planifie — Configuration Tarifaire HotelRunner

**Derniere mise a jour** : 2025-12-23
**Statut** : En attente de configuration | **Approche** : Room-Centric
**Interface** : HotelRunner → Calendar → Simple Updates

---

## Tarifs a Configurer

> **Details des chambres & formule tarifaire** : Voir [`configs/hotel/rooms.md`](../../configs/hotel/rooms.md) (lignes 38-48 pour le mapping des chambres, lignes 92-104 pour la formule)

| Chambre(s) | Type de Chambre | Action Requise | Statut Decision |
|------------|-----------------|----------------|-----------------|
| 4, 5 | Double Room Superior | Configurer **160 €** dans HotelRunner | ⏳ En attente |
| 1, 3, 8 | Deluxe Triple Room | Configurer **200 €** dans HotelRunner | ⏳ En attente |
| 2 | Deluxe Double Room | Configurer **200 €** dans HotelRunner | ⏳ En attente |
| 6 | Executive Suite | Configurer **240 €** dans HotelRunner | ⏳ En attente |
| **7** | **Deluxe King Suite** | **DECISION NECESSAIRE** (440 € vs 280 €) | 🟡 Avis Omar requis |
| 9 | Family Suite | Configurer **227 €** dans HotelRunner | ⏳ En attente |
| 10 | Suite | Configurer **267 €** dans HotelRunner | ⏳ En attente |
| 11 | Family Suite | Configurer **240 €** dans HotelRunner | ⏳ En attente |
| **12** | **Presidential Suite** | **DECISION NECESSAIRE** (600 € vs 350 €) | 🟡 Avis Omar requis |

---

## Vue par Chambre (Room-Centric)

| # | Chambre | Type | Prix EUR | Statut |
|---|---------|------|----------|--------|
| 1 | Chambre 1 | Deluxe Triple Room | 200 | ⏳ |
| 2 | Chambre 2 | Deluxe Double Room | 200 | ⏳ |
| 3 | Chambre 3 | Deluxe Triple Room | 200 | ⏳ |
| 4 | Chambre 4 | Double Room Superior | 160 | ⏳ |
| 5 | Chambre 5 | Double Room Superior | 160 | ⏳ |
| 6 | Chambre 6 | Executive Suite | 240 | ⏳ |
| 7 | Chambre 7 | Deluxe King Suite | [Decision requise] | |
| 8 | Chambre 8 | Deluxe Triple Room | 200 | ⏳ |
| 9 | Chambre 9 | Family Suite | 227 | ⏳ |
| 10 | Chambre 10 | Suite | 267 | ⏳ |
| 11 | Chambre 11 | Family Suite | 240 | ⏳ |
| 12 | Chambre 12 | Presidential Suite | [Decision requise] | |

> **Note**: Cette vue room-centric permet de voir rapidement le prix de chaque chambre individuelle.

---

## Decisions Premium en Attente

### Chambre 7 — Deluxe King Suite

| Option | Description | Marge Resultante |
|--------|-------------|------------------|
| A | **440 €** — Positionnement premium au-dessus du marche | 330 € net |
| B | **280 €** — Ajustement vers le marche Palmeraie | 210 € net |

**Decision Omar** : `[ECRIRE ICI]`

**Contexte marche** : La fourchette Palmeraie pour des chambres similaires est 200-280 €. L'option A nous positionne 57% au-dessus du haut du marche.

---

### Chambre 12 — Presidential Suite

| Option | Description | Marge Resultante |
|--------|-------------|------------------|
| A | **600 €** — Positionnement tres premium au-dessus du marche | 450 € net |
| B | **350 €** — Ajustement vers le marche premium Palmeraie | 262 € net |

**Decision Omar** : `[ECRIRE ICI]`

**Contexte marche** : Les suites premium Palmeraie varient entre 200-280 €. L'option A nous positionne 114% au-dessus du haut du marche.

---

## Methode d'Execution (une fois valide)

### Prerequis
- [ ] Omar a valide les decisions premium (Chambres 7 & 12)
- [ ] Tous les tarifs confirmes contre [`rooms.md`](../../configs/hotel/rooms.md)

### Etapes

1. **Acceder a HotelRunner** : [app.hotelrunner.com](https://app.hotelrunner.com)
2. **Naviguer** : Calendar → Simple Updates
3. **Pour chaque type de chambre** :
   - Selectionner le canal Booking.com
   - Entrer le tarif calcule du tableau ci-dessus
   - Sauvegarder les modifications
4. **Verifier** : Controler la synchronisation avec l'extranet Booking.com

### Post-Execution

- [ ] Deplacer ce fichier vers `../execution/YYYY-MM-DD/pricing.md`
- [ ] Mettre a jour la colonne statut dans `../../configs/hotel/rooms.md` (lignes 79-88)
- [ ] Creer un instantane baseline dans `../baseline/pricing-YYYY-MM-DD.md`

---

_Source de verite pour la configuration tarifaire planifiee_
_Mis a jour le 2025-12-23_

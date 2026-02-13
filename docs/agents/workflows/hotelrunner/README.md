# HotelRunner — Guide des Bulk Updates (Restrictions & Plus)

## Contexte Propriété

- **Propriété** : Villa Thaifa
- **URL Admin** : `villa-thaifa.hotelrunner.com/admin`
- **Canaux** : Online (canal direct) + Booking.com
- **Rate Plans** : Master rate, Petit Déjeuner inclus Flexible, Petit Déjeuner inclus Non-remboursable (tous en EUR)
- **Chambres** (8 types) : Double Room Superior, Deluxe Double Room, Deluxe Triple Room, Suite, Deluxe King Suite, Family Suite, Executive Suite, Presidential Suite

---

## Workflow : Modifier une Restriction (Stop Sell, CTA, CTD, etc.) via Bulk Updates

### Chemin d'accès

`Calendar > Bulk Updates` URL directe : `https://villa-thaifa.hotelrunner.com/admin/products/villa-thaifa/channel/prices/bulk_update`

### Étapes détaillées

**1. Configurer les filtres à gauche :**

- **Rate plans** : Laisser "All rate plans" (sauf si ciblage spécifique)
- **Currency** : Laisser "All currencies"
- **"What do you want to update?"** : Cocher la restriction voulue (ex: "Stop sell")
- **Date Range** :
  - **Format des dates** : `MM/DD/YYYY` (format US !)
  - Ex: 12 mars 2026 → `03/12/2026`, 16 décembre 2026 → `12/16/2026`
  - On peut taper directement dans le champ ou utiliser le calendrier popup
- **Days** : Laisser "All" coché (sauf si on veut cibler certains jours)
- **Channels** (à droite) : Garder "All" coché pour appliquer à Online ET Booking.com

**2. Utiliser le Master Dropdown (astuce cruciale) :**

- Après avoir coché une restriction, une icône 🔗 apparaît dans l'en-tête de colonne "Restrictions"
- **Cliquer sur cette icône** → fait apparaître un dropdown "master" en haut de la colonne + une flèche ↓
- **Sélectionner la valeur dans le master dropdown** (ex: "No" pour retirer, "Yes" pour activer)
- **Cliquer sur la flèche ↓** → propage la valeur à TOUTES les chambres et rate plans d'un coup !

**3. Vérifier visuellement** que toutes les lignes affichent bien la valeur souhaitée (scroller en bas pour voir toutes les chambres)

**4. Cliquer "Update"** → Un panneau **Preview** apparaît avec :

- Récapitulatif des dates, jours, canaux
- Tableau de toutes les chambres avec les changements
- Scroller à droite dans le Preview pour voir la colonne "Restrictions" et confirmer (ex: "Stop sell: ✕" = désactivé)

**5. Confirmer en cliquant "Update"** dans le Preview (bouton bleu en bas à droite)

**6. Vérification post-action :**

- Aller sur `Calendar > Simple Updates` (URL: `.../channel/prices?f=1`)
- Naviguer vers une date dans la plage modifiée
- **Canal Online** : changement immédiat (fond blanc = OK, fond rouge = Stop Sell actif)
- **Booking.com** : peut afficher "Waiting Response from Channel" pendant la synchronisation (normal)

---

## Valeurs des Restrictions

| Restriction                  | Valeurs possibles | Signification                                         |
| ---------------------------- | ----------------- | ----------------------------------------------------- |
| **Stop Sell**                | Yes / No          | Yes = chambre fermée à la vente, No = chambre ouverte |
| **CTA** (Close to Arrival)   | Yes / No          | Yes = pas de nouvelle arrivée ce jour                 |
| **CTD** (Close to Departure) | Yes / No          | Yes = pas de départ ce jour                           |
| **Minimum Stay**             | Nombre (jours)    | Durée minimum de séjour                               |
| **Maximum Stay**             | Nombre (jours)    | Durée maximum de séjour                               |
| **Cut off time**             | Nombre (heures)   | Délai de réservation avant arrivée                    |
| **Availability**             | Nombre            | Chambres disponibles                                  |
| **Price**                    | Montant (€)       | Prix de base                                          |

---

## Indicateurs visuels dans Simple Updates (Calendar)

| Indicateur                          | Signification                                            |
| ----------------------------------- | -------------------------------------------------------- |
| Fond **blanc** + prix               | Chambre disponible, pas de restriction                   |
| Fond **rouge** + icônes rouges      | Stop Sell actif ou restriction bloquante                 |
| **Point rouge** en bas de cellule   | Restriction active (Stop Sell, CTA, CTD...)              |
| **Coche verte** ✓                   | Synchronisation OK avec le canal                         |
| "**Waiting Response from Channel**" | Mise à jour envoyée, en attente de confirmation du canal |
| **N/A**                             | Pas de prix défini sur ce canal                          |

---

## Pièges courants à éviter

1. **Format de date** : Toujours `MM/DD/YYYY` (mois/jour/année), pas le format européen
2. **"-" dans les dropdowns** : Signifie "pas de changement" — il faut explicitement choisir "Yes" ou "No"
3. **Oublier la flèche ↓** : Changer le master dropdown ne suffit pas, il faut cliquer la flèche pour propager
4. **End Date avant Start Date** : Le calendrier Advanced Updates ne montrera rien
5. **Sync Booking.com** : Ne pas paniquer si "Waiting Response from Channel" — c'est normal
6. **Vérifier le scroll** : Les chambres Family Suite, Executive Suite, Presidential Suite sont en bas de la liste

---

## Autres Opérations Bulk Update similaires

Le même workflow s'applique pour modifier en masse :

- **Disponibilité** (Availability) → changer le nombre de chambres dispo
- **Prix** (Price) → ajuster les tarifs
- **Price adjustment** → ajustement en % ou montant
- **Minimum/Maximum stay** → restrictions de durée de séjour
- **CTA/CTD** → fermer/ouvrir arrivées ou départs
- **Cut off time** → délai de réservation

Pour chacune, le process est identique : cocher la case à gauche → configurer dates/jours/canaux → utiliser le master dropdown + flèche ↓ → Preview → Update.

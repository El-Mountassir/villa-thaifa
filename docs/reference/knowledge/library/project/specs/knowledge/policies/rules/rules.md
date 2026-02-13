# Règles d'Opérations Plateforme — Villa Thaifa

> **CRITIQUE** : Ces règles s'appliquent à TOUTE opération sur HotelRunner, Booking.com, ou autre plateforme.
> Tolérance zéro — Une erreur peut affecter des réservations clients.

---

## ⚠️ Règle d'Action Basée sur la Confiance

> **Si confiance < 90% → TOUT ARRÊTER et DEMANDER à Omar.**

### Contextes concernés

| Contexte                    | Exemples                                     |
| --------------------------- | -------------------------------------------- |
| Opérations plateforme       | Clics sur HotelRunner, Booking.com           |
| Changements chambres/tarifs | Sélection de chambre, ajustements tarifaires |
| Actions client              | Réservations, annulations                    |
| Actions irréversibles       | Soumissions, confirmations                   |

### Processus

```
1. PAUSE avant de cliquer/soumettre
2. VÉRIFIER contre la documentation (data/specs/configs/hotel/rooms.md, etc.)
3. Si incertain → STOP → DEMANDER → Attendre confirmation
4. JAMAIS deviner ou supposer sur les opérations plateforme
```

**Contexte** : Ajouté 2025-12-22 après quasi-erreur Chambre 11.

---

## ⚠️ Règle de Vérification des Dates/Détails

> **TOUJOURS répéter les détails clés à Omar AVANT d'exécuter.**

| Détail             | Action                                       |
| ------------------ | -------------------------------------------- |
| **Dates**          | Répéter "Du X au Y" et attendre confirmation |
| **Numéro chambre** | Confirmer "Chambre X" explicitement          |
| **Nom invité**     | Épeler le nom                                |
| **Prix**           | Annoncer le total avant soumission           |

### Processus réservations

```
1. ANALYSER la demande attentivement
2. RÉPÉTER : "Je vais créer : Chambre X, du JJ au JJ/MM, nom : Y, prix : Z"
3. ATTENDRE un "oui" ou une correction
4. PUIS exécuter
```

**Contexte** : Ajouté 2025-12-22 après erreur date ("25 au 27" au lieu de "24 au 27").

---

## ⚠️ Utiliser les Valeurs Exactes du Système

> **JAMAIS calculer/approximer — utiliser la valeur EXACTE de la plateforme.**

| ❌ Faux              | ✅ Correct                          |
| -------------------- | ----------------------------------- |
| "4500 DH (3 × 1500)" | "4.512,21 MAD" (depuis HotelRunner) |
| "~280€"              | "280,00 €" (exact)                  |

**Règle** : Toujours copier le total final de HotelRunner/Booking.com. Les systèmes peuvent ajouter frais, taxes, ou arrondis.

---

## ⛔ Protection des Fichiers de Données

> **ARRÊT COMPLET requis avant toute modification destructive des fichiers data/specs.**

| Type d'action                    | Confirmation requise    |
| -------------------------------- | ----------------------- |
| Écraser données existantes       | ✅ OBLIGATOIRE DEMANDER |
| Remplacer valeurs (pas ajouter)  | ✅ OBLIGATOIRE DEMANDER |
| Supprimer/retirer informations   | ✅ OBLIGATOIRE DEMANDER |
| Changer compteurs/métriques      | ✅ OBLIGATOIRE DEMANDER |
| Ajouter NOUVELLES données à côté | ❌ OK pour continuer    |

### Processus pour mise à jour des données

```
1. LIRE les données actuelles attentivement
2. IDENTIFIER ce qui existe vs ce qui est nouveau
3. AJOUTER les nouvelles données SANS supprimer l'existant
4. Si modification nécessaire → STOP → DEMANDER À OMAR
```

### Exemple (rooms.md)

- ❌ MAUVAIS : "Types de chambres : 9" → "Types de chambres : 8" (données détruites)
- ✅ BON : Ajouter "Types de chambres (Booking.com) : 8" à côté de l'existant

> **Justification** : Fichiers de données = SSOT. Différentes plateformes peuvent avoir différentes données.

---

## Checklist Pré-Exécution

Avant toute action plateforme :

- [ ] Confiance > 90% ?
- [ ] Détails répétés à Omar ?
- [ ] Valeurs exactes (pas calculées) ?
- [ ] Fichiers de données non modifiés de manière destructive ?

Si une réponse est NON → **STOP** et ajuste.

---

_Règles d'Opérations Plateforme v0.1.0-alpha.0 — Tolérance Zéro_

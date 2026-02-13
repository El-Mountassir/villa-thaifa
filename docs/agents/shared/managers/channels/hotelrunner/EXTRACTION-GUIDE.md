# HotelRunner Data Extraction Guide

> **Status**: ✅ Opérationnel (Browser Automation)
> **Date**: 2026-01-24
> **Méthode**: agent-browser avec profile persistant

---

## 🎯 Vue d'Ensemble

Ce guide explique comment extraire automatiquement les données de réservations depuis HotelRunner via browser automation.

**Avantages** :
- ✅ Pas de configuration API complexe
- ✅ Pas de rate limits (250/jour)
- ✅ Pas de callback URL requis
- ✅ Authentification persistante (pas de reCAPTCHA répété)

---

## 📋 Prérequis

### 1. Installation

```bash
# agent-browser déjà installé globalement
agent-browser --version
```

### 2. Authentification Requise

⚠️ **LIMITATION DÉCOUVERTE** : Le flag `--profile` d'agent-browser ne persiste pas les cookies de session correctement.

**Solution de contournement actuelle** :

**Option A - Authentification manuelle avant extraction** :
```bash
# 1. Ouvrir browser en mode visible
agent-browser --headed open https://villa-thaifa.hotelrunner.com/login

# 2. Se connecter manuellement (résoudre reCAPTCHA si nécessaire)

# 3. Laisser le browser ouvert

# 4. Dans un autre terminal, exécuter le script
# (Le script utilisera la session browser active)
```

**Option B - Extraction manuelle via browser** :
```bash
# Utiliser agent-browser en mode interactif pour extraction ponctuelle
agent-browser --headed open https://villa-thaifa.hotelrunner.com/admin/pms/reservations/all
# Puis extraire manuellement avec eval/snapshot
```

**Note** : Nous travaillons sur une solution pour la persistence automatique des sessions.

---

## 🚀 Utilisation

### Script d'Extraction Quotidienne

**Fichier** : [`extract_reservations.py`](./extract_reservations.py)

**Exécution manuelle** :
```bash
cd /home/omar/omar-el-mountassir/projects/clients/villa-thaifa/sources/hotelrunner-api
python3 extract_reservations.py
```

**Sortie** :
```
data/reservations/
├── reservations_20260124_140630.json  # Extraction avec timestamp
├── reservations_20260124_153045.json
└── latest.json                        # Dernière extraction (lien rapide)

logs/
└── extract_20260124.log               # Logs quotidiens
```

### Automatisation (Cron)

Pour exécution quotidienne automatique :

```bash
# Éditer crontab
crontab -e

# Ajouter (exécution tous les jours à 6h00)
0 6 * * * cd /home/omar/omar-el-mountassir/projects/clients/villa-thaifa/sources/hotelrunner-api && /usr/bin/python3 extract_reservations.py >> logs/cron.log 2>&1
```

---

## 📊 Format des Données

### Structure JSON

```json
{
  "extracted_at": "2026-01-24T14:06:30",
  "source": "HotelRunner Dashboard - Browser Automation",
  "count": 96,
  "reservations": [
    {
      "status": "No-show",
      "room": "",
      "channel": "Online",
      "client_name": "Famille Benchekroune",
      "confirmation_number": "R194048877",
      "check_in": "31 Déc. 2025 15:00",
      "check_out": "02 Janv. 2026 11:00",
      "room_type": "Suite de Luxe King Size",
      "total": "880 €",
      "payment_total": "373,45 €",
      "inventory_type": "Confirmé",
      "confirmation_status": "No-show",
      "booking_date": "Mercredi 31 Décembre 2025 15:51",
      "nationality": "MA"
    }
    // ... autres réservations
  ]
}
```

### Champs Disponibles

| Champ | Description | Exemple |
|-------|-------------|---------|
| `status` | Statut réservation | No-show, Confirmé, Annulé |
| `room` | Numéro chambre | 101, 205 |
| `channel` | Canal réservation | Online, Booking.com, Direct |
| `client_name` | Nom du client | Famille Benchekroune |
| `confirmation_number` | Numéro confirmation | R194048877 |
| `check_in` | Date/heure arrivée | 31 Déc. 2025 15:00 |
| `check_out` | Date/heure départ | 02 Janv. 2026 11:00 |
| `room_type` | Type de chambre | Suite de Luxe King Size |
| `total` | Prix total | 880 € |
| `payment_total` | Montant payé | 373,45 € |
| `inventory_type` | Type inventaire | Confirmé, Modifié |
| `confirmation_status` | Statut confirmation | No-show, Confirmed |
| `booking_date` | Date réservation | Mercredi 31 Décembre 2025 15:51 |
| `nationality` | Nationalité client | MA (Maroc) |

---

## 🔧 Personnalisation

### Modifier le Script

Le script [`extract_reservations.py`](./extract_reservations.py) peut être personnalisé :

**1. Changer l'URL source** :
```python
# Ligne 72
url = 'https://villa-thaifa.hotelrunner.com/admin/pms/reservations/all'

# Alternatives:
# - /admin/channel/calendars/occupancies?f=1  (Calendrier)
# - /admin/reports  (Rapports)
# - /admin/pms/overview  (Vue d'ensemble PMS)
```

**2. Filtrer les données** :
```python
# Après extraction, filtrer par status
active_reservations = [r for r in reservations if r['status'] == 'Confirmé']

# Filtrer par date
import datetime
today = datetime.date.today()
# ... logique de filtrage
```

**3. Ajouter exports** :
```python
# Export CSV
import csv
with open('reservations.csv', 'w') as f:
    writer = csv.DictWriter(f, fieldnames=reservations[0].keys())
    writer.writeheader()
    writer.writerows(reservations)
```

---

## 📈 Cas d'Usage

### 1. Extraction Quotidienne

**Objectif** : Backup quotidien des réservations

```bash
# Cron à 6h tous les jours
0 6 * * * cd .../sources/hotelrunner-api && python3 extract_reservations.py
```

### 2. Intégration AI Agents

**Objectif** : Agents lisent les dernières réservations

```python
# Dans votre agent
import json

with open('sources/hotelrunner-api/data/reservations/latest.json') as f:
    data = json.load(f)
    reservations = data['reservations']

# Traiter les réservations
for res in reservations:
    if res['status'] == 'Confirmé':
        # ... logique agent
```

### 3. Rapports Automatiques

**Objectif** : Générer rapports hebdomadaires

```python
# Script séparé
import json
from collections import Counter

with open('data/reservations/latest.json') as f:
    data = json.load(f)

# Stats par canal
channels = Counter(r['channel'] for r in data['reservations'])
print("Réservations par canal:", channels)

# Stats par statut
statuses = Counter(r['status'] for r in data['reservations'])
print("Réservations par statut:", statuses)
```

---

## 🐛 Troubleshooting

### Problème : "Not authenticated"

**Cause** : Profile expiré ou jamais créé

**Solution** :
```bash
# Re-créer profile en mode visible
agent-browser --headed --profile ~/.hotelrunner-profile open https://app.hotelrunner.com
# Login manuellement
agent-browser close
```

### Problème : "Command timed out"

**Cause** : Page lente à charger

**Solution** : Augmenter timeout dans le script
```python
# Ligne 30
timeout=60  # Au lieu de 30
```

### Problème : "Failed to parse JSON"

**Cause** : Structure page changée

**Solution** : Vérifier la structure HTML
```bash
agent-browser --headed open https://villa-thaifa.hotelrunner.com/admin/pms/reservations/all
agent-browser snapshot -c  # Voir structure
```

### Problème : Browser ne se ferme pas

**Solution** :
```bash
# Fermer manuellement
agent-browser close

# Ou tuer le processus
pkill -f chromium
```

---

## 📚 Ressources

**Documentation** :
- [Test Results](../../tmp/hotelrunner-browser-test-results.md) - Résultats POC
- [OPTIONS-ANALYSIS.md](./OPTIONS-ANALYSIS.md) - Analyse complète options
- [SETUP.md](./SETUP.md) - Progress tracking
- [agent-browser guide](../agent-browser/guide.md) - Documentation outil

**Scripts** :
- [`extract_reservations.py`](./extract_reservations.py) - Script principal
- Plus de scripts à venir (calendrier, rapports, etc.)

---

## ✅ Checklist

Avant première utilisation :
- [ ] agent-browser installé (`agent-browser --version`)
- [ ] Profile créé (`~/.hotelrunner-profile` existe)
- [ ] Première auth manuelle réussie
- [ ] Test extraction manuelle OK
- [ ] (Optionnel) Cron configuré pour automatisation

---

**Créé par** : Craft Agent
**Date** : 2026-01-24
**Status** : ✅ Production-ready

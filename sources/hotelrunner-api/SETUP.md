# HotelRunner API - Setup & Progress Tracking

## 🎯 Objectif

Intégrer l'API HotelRunner (HR-v1 REST API) pour automatiser la gestion de Villa Thaifa via AI agents.

## 📊 Statut Actuel

**Date de création**: 2026-01-24 13:24
**Statut**: ⏳ En cours - Attente credentials
**Progression**: 60%

## ✅ Étapes Complétées

### 1. Recherche et Documentation (✅ Fait)

- [x] Recherche de la section API dans le dashboard HotelRunner
- [x] Localisation: Custom Apps → Créez votre app
- [x] Identification des types d'intégration disponibles (HR-v1 vs OTA-2015b)
- [x] Décision: **HR-v1** (REST API moderne, JSON, plus simple pour AI automation)

### 2. Création du Dossier Source (✅ Fait - 2026-01-24 13:28)

- [x] Création de `/sources/hotelrunner-api/`
- [x] config.json créé avec structure API complète
- [x] guide.md créé avec documentation détaillée
- [x] README.md créé pour référence rapide
- [x] SETUP.md créé pour tracking (ce fichier)
- [x] Commit git: `feat: add HotelRunner REST API source configuration`

### 3. Formulaire de Création App (✅ Fait - 2026-01-24 13:21)

- [x] **Nom de l'application**: Villa Thaifa PMS - AI Automation
- [x] **E-mail technique**: omar@el-mountassir.com
- [x] **Utilisateur d'intégration**: Sélectionné dans dropdown
- [x] **URL de rappel**: <https://localhost/hotelrunner/callback>
- [x] **Enforce SSL**: ✅ Activé
- [x] **Type d'intégration**: HR-v1 (REST API)
- [x] **Permissions**: ✅ Toutes cochées
  - Récupérer la liste des chambres
  - Récupérer les réservations
  - Recevoir mises à jour push (Confirmé, Modifié, Annulé)
  - Mettre à jour le calendrier des chambres

## ⏳ Étapes En Cours

### 4. Génération des Credentials (🔄 En cours maintenant)

- [ ] Cliquer sur le bouton **"Créer"** dans le formulaire
- [ ] Attendre confirmation de création
- [ ] Naviguer vers l'onglet **"Identifiants"**
- [ ] Copier **TOKEN**
- [ ] Copier **HR_ID**

## 📋 Prochaines Étapes

### 5. Sauvegarde des Credentials

- [ ] Ouvrir `.env.local`
- [ ] Ajouter les valeurs:
  ```bash
  HOTELRUNNER_TOKEN=<valeur_copiée>
  HOTELRUNNER_HR_ID=<valeur_copiée>
  ```
- [ ] Sauvegarder le fichier
- [ ] ⚠️ **NE PAS COMMITER** .env.local (déjà dans .gitignore)

### 6. Test de Connexion

- [ ] Créer script de test `test_hotelrunner_api.py`
- [ ] Tester l'authentification
- [ ] Tester GET /rooms (liste des chambres)
- [ ] Vérifier la réponse API
- [ ] Documenter les résultats

### 7. Activation de la Source

- [ ] Modifier `config.json`: `"enabled": false` → `"enabled": true`
- [ ] Valider la configuration
- [ ] Commit: `feat: enable HotelRunner API source with credentials`

### 8. Documentation Agent

- [ ] Mettre à jour CLAUDE.md
- [ ] Mettre à jour AGENTS.md
- [ ] Mettre à jour docs/leadership/INDEX.md
- [ ] Créer exemples d'usage pour agents

### 9. Intégration Avancée

- [ ] Configurer webhooks pour notifications temps réel
- [ ] Créer scripts d'automatisation
- [ ] Tester les différents endpoints
- [ ] Documenter les cas d'usage Villa Thaifa

## 📝 Notes Importantes

### Credentials à Obtenir

```
TOKEN: <en attente>
HR_ID: <en attente>
```

### Rate Limits

- **250 requêtes / jour** maximum
- **5 requêtes / minute** maximum
- ⚠️ Planifier l'automatisation en conséquence

### Documentation Officielle

- **API Docs**: https://developers.hotelrunner.com/custom-apps/rest-api
- **Base URL**: https://am.hotelrunner.com/custom-apps/rest-api

### Contact Support

- **Omar**: omar@el-mountassir.com
- **HotelRunner**: integrations@hotelrunner.com

## 🔄 Historique des Changements

### 2026-01-24

- **13:24** - Recherche documentation HotelRunner API
- **13:21** - Remplissage formulaire création app (étapes 1-7)
- **13:24** - Choix confirmé: HR-v1 (REST API)
- **13:28** - Création dossier source complet avec config, guide, README
- **13:28** - Premier commit git
- **13:30** - Création SETUP.md pour tracking systématique

## ⚠️ Pour les Agents AI

### Où trouver les informations?

1. **Configuration**: `/sources/hotelrunner-api/config.json`
2. **Guide d'usage**: `/sources/hotelrunner-api/guide.md`
3. **Progress tracking**: `/sources/hotelrunner-api/SETUP.md` (ce fichier)
4. **Credentials**: `.env.local` (une fois ajoutés)

### Avant d'utiliser l'API

1. Vérifier que credentials existent dans `.env.local`
2. Lire le guide complet: `guide.md`
3. Respecter les rate limits (250/jour, 5/min)
4. Logger toutes les opérations importantes

### État Actuel

🔴 **Source désactivée** - En attente des credentials TOKEN et HR_ID

Une fois les credentials obtenus, la source sera activée et prête à l'usage.

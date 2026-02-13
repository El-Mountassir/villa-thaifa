# Developer Onboarding Guide: Expedia Connectivity API

Ce guide explique comment obtenir les accès nécessaires pour que l'agent puisse synchroniser automatiquement les données de la Villa Thaifa avec Expedia.

## 📋 Prérequis

- Avoir accès au compte **Expedia Partner Central (EPC)** de la propriété.
- Connaître l'**ID de la propriété** (Property ID).

---

## 🚀 Étape 1 : Activer la Connectivité Directe

1. Connectez-vous à [Expedia Partner Central](https://www.expediapartnercentral.com/).
2. Allez dans le menu **Chambres et Tarifs** (Rooms and Rates).
3. Cliquez sur **Paramètres de connectivité Expedia** (Expedia Connectivity Settings).
4. Vérifiez si vous pouvez sélectionner "Direct Connect" ou si vous devez désigner votre logiciel (certains comptes exigent un Channel Manager comme HotelRunner).
   > [!IMPORTANT]
   > Si la villa utilise déjà HotelRunner, informez l'agent. Nous devrons peut-être passer par l'API HotelRunner au lieu de l'API Expedia directe pour éviter les conflits.

---

## 🔑 Étape 2 : Obtenir les clés API (Portail EPS)

Le portail développeur est différent du portail de gestion habituel.

1. Rendez-vous sur le [Expedia Group Developer Hub (EPS Portal)](https://developers.expediagroup.com/).
2. Connectez-vous avec vos identifiants Partner Central (ou créez un compte développeur lié à votre propriété).
3. Dans le menu de gauche, cherchez **Connectivity** ou **API Keys**.
4. Vous devriez voir ou pouvoir générer :
   - **API Key**
   - **Shared Secret** (Notez-le bien, il ne s'affiche qu'une fois).
5. Récupérez également votre **Property ID** (souvent un numéro à 7-9 chiffres).

---

## 🛠️ Étape 3 : Configuration locale

Une fois les clés obtenues, créez (ou mettez à jour) le fichier `.env` à la racine du projet :

```env
EXPEDIA_API_KEY=votre_clé_ici
EXPEDIA_SHARED_SECRET=votre_secret_ici
EXPEDIA_PROPERTY_ID=votre_property_id
```

---

## ❓ FAQ & Aide

- **Je ne vois pas le menu Connectivity** : Contactez votre Market Manager Expedia pour demander l'activation des accès API pour votre compte.
- **Différence entre Rapid API et Connectivity API** :
  - _Rapid API_ : Utilisé pour vendre des chambres (affiliés).
  - _Connectivity API_ : Utilisé pour gérer les chambres (nous).

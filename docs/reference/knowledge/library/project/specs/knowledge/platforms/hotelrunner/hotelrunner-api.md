# 🏨 HotelRunner API Knowledge Base

> **Dernière mise à jour**: 12 Janvier 2026
> **Source**: https://developers.hotelrunner.com/

## 🔐 Authentification

- **Méthode**: En-têtes HTTP (Headers)
- **Paramètres Requis**:
  - `HR_ID`: Code identifiant la propriété.
  - `TOKEN`: Clé secrète.
- **Obtention**:
  - Directement dans le panneau "My Property" (admin) du dashboard HotelRunner.
  - **Verdict**: Disponible pour Villa Thaifa (Owner Access).

## 🚀 Capabilities (Capabilities)

### 1. Inventory (Rooms & Rates)

- **Read**: `Get Room List` (Codes `inv_code` des types de chambres).
- **Update**: Availability, Rates, Stop Sell.
- **Utilité**: Permet de mettre à jour tarifs/dispos depuis un fichier central (ex: Markdown ou Excel futur).

### 2. Channels (OTAs)

- **Read**: Liste des canaux connectés.
- **Update**: Activer/Désactiver un canal.
- **Limitations**: Ne permet pas forcément de _configurer_ un canal la première fois (souvent nécessite UI OAuth), mais utile pour le monitoring.

### 3. Reservations

- **Read**: Historique.
- **Push**: Webhooks pour nouvelles réservations (JSON/XML).

## ⚠️ Limites

- **Rate Limit**: 250 requêtes/jour (5/min).
- **Usage**: Suffisant pour synchronisation périodique, pas pour du temps réel haute fréquence.

## ✅ Plan d'Action API

1.  Récupérer `HR_ID` et `TOKEN` dans le dashboard (Manuellement ou Browser Agent).
2.  Stocker dans `.env.local` (ex: `HOTELRUNNER_token`).
3.  Créer des outils (Scripts Node ou MCP) pour lire l'inventaire sans browser.

![API Auth Details](hr_api_auth_details.png)

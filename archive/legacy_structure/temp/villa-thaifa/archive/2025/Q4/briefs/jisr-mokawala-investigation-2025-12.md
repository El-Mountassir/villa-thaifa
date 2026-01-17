# Prompt d’investigation et d’intégration — Portail **Jisr l’Mokawala** (Maroc PME)

## Contexte

Je prépare un projet pour une **maison d’hôtes** à Marrakech (**Villa Thaifa**). Le client vise deux priorités : **optimiser le chiffre d’affaires** et **maximiser le ROI**.

Un point de douleur majeur est la dépendance à **Booking.com**, avec des commissions perçues comme très élevées (ordre de grandeur : **~40%** selon le client). L’objectif est donc d’augmenter la part de **réservations directes** et d’améliorer la **marge nette** (mix canaux, conversion, upsell).

En parallèle, nous devons confirmer la faisabilité d’une connexion programmatique au portail public marocain **Jisr l’Mokawala** (Maroc PME), lié au programme **Go Siyaha**, afin d’automatiser le suivi/dépôt administratif quand cela apporte un gain opérationnel.

Nous disposons d’un accès **utilisateur** au portail (identifiant + mot de passe) fourni par le client.

> **Sécurité / conformité (strict)** :
>
> - Ne jamais inclure d’identifiants ou mots de passe dans les livrables, tickets, logs, captures, dépôts Git ou échanges non chiffrés.
> - Utiliser des variables d’environnement / gestionnaire de secrets.
> - Toute automatisation doit respecter CGU, sécurité du site, et obtenir un consentement explicite du client.

## Objectifs (business + techniques)

### Objectifs business (prioritaires)

- **Réduire la dépendance à Booking.com** : augmenter la part des **réservations directes** (site, WhatsApp, téléphone, réseaux sociaux), et diminuer le coût de distribution.
- **Améliorer la rentabilité** : réduire les commissions OTA, améliorer la **marge nette** et le **ROI** des actions marketing.
- **Augmenter le panier moyen** : upsell (petit-déjeuner, transferts, expériences), cross-sell, offres packagées.
- **Pilotage** : mettre en place une couche data/KPIs (taux de conversion direct, coût d’acquisition, part OTA vs direct, ADR/RevPAR, taux d’occupation, no-show/cancellation, NPS/notes).

### Objectifs techniques

- Vérifier si le portail **Jisr l’Mokawala** est **intégrable** (API Jira Service Management) pour automatiser les tâches administratives liées à Go Siyaha (création/suivi de demandes, pièces jointes, statuts, notifications).
- Mettre en place des **connecteurs** fiables (API si autorisée, sinon email en plan B; RPA en dernier recours) avec traçabilité et sécurité.
- Concevoir une **architecture agentique** orientée exécution : ingestion (emails/OTA/CRM), extraction, décision, génération de réponses/documents, orchestration, observabilité.

### Critères de succès (à préciser avec le client)

- +X% de réservations directes en N semaines/mois.
- -X points de part OTA (ou -X% de commissions payées) à volume constant.
- Amélioration mesurable de la marge et du ROI (tableau de bord + baseline).

## Rôles attendus (ton équipe IA)

- **Lead Architecte / Agentic Engineer** : stratégie d’intégration, architecture, risques.
- **Full‑stack Engineer** : tests techniques, exploration endpoints, POC minimal.
- **Security / Compliance** : règles de sécurité, gestion secrets, conformité.
- **Product / Ops** : parcours utilisateur, workflow métier, critères de succès.

## Données d’entrée (à renseigner sans exposer les secrets)

- URL portail : https://jisr.marocpme.gov.ma/
- Type de compte : (Customer / Agent / Autre) : [À préciser]
- Identifiant : [FOURNIR HORS PROMPT — via un canal sécurisé]
- Mot de passe : [FOURNIR HORS PROMPT — via un canal sécurisé]
- Objectif client : (suivi dossier, dépôt pièces, notifications, etc.) : [À préciser]

## Travail demandé (à réaliser maintenant)

### 1) Qualification fonctionnelle

1. Décrire le **parcours utilisateur** réel du portail :
   - inscription / connexion
   - création / dépôt de candidature
   - upload pièces jointes
   - messages / commentaires / demandes de compléments
   - consultation statut / historique
2. Clarifier le périmètre :
   - Le portail concerne-t-il uniquement les **candidatures / subventions / assistance** ?
   - Existe-t-il des flux « réservations » ? (probablement non).
   - Proposer une liste de questions à poser au client pour lever toute ambiguïté.

### 2) Cartographie technique du portail (Jira Service Management)

1. Confirmer la stack : **Atlassian Jira Service Management** (Server/Data Center) et identifier :
   - version / build si visible
   - endpoints typiques exposés (ex. `/rest/servicedeskapi/`, `/rest/api/2/`)
   - mécanismes anti‑bot : CSRF, CAPTCHA, MFA, rate limits, etc.
2. Identifier les objets / concepts :
   - service desk(s)
   - request types
   - customer requests
   - comments / attachments
   - transitions / statuts

### 3) Faisabilité API (priorité 1)

Conduire une exploration **non intrusive** (lecture et tests minimaux) :

- Déterminer si les REST APIs Jira/JSM sont accessibles depuis l’extérieur.
- Identifier l’authentification possible (Basic, cookie session, OAuth, token, SSO).
- Déterminer les permissions du compte client (lecture seule / création / ajout PJ / commentaires).

**Livrable attendu** :

- Liste d’endpoints confirmés + exemple de requêtes (cURL/Postman) **sans secrets**.
- Mapping “besoin → endpoint”.

### 4) Plan B — automatisation par email (priorité 2)

Si le portail envoie des emails de notifications :

- Décrire une architecture “email listener” :
  - ingestion (Gmail/IMAP), parsing robuste, déduplication, corrélation dossier, archivage
  - déclenchement workflows (relances, collecte documents, création tâches)
  - traçabilité et audit
- Définir un modèle de données minimal (dossier, statut, demandes, échéances, pièces).

### 5) Plan C — RPA/Browser automation (dernier recours)

Si aucune API exploitable et email insuffisant :

- Proposer une approche RPA **très encadrée** (Playwright) :
  - robustesse (sélecteurs, tests de non‑régression)
  - risques (changement UI, blocages, CGU)
  - gouvernance (désactivation rapide, monitoring)

### 6) Architecture agentique cible (solution intelligente)

Proposer une architecture en couches :

- **Connecteurs** : API JSM / Email / RPA
- **Orchestrateur** : planification, retries, idempotence, files
- **Agents** : extraction, classification, décision, rédaction (FR/AR), génération documents
- **Knowledge base** : documents du client, règles, statut dossiers
- **Observabilité** : logs structurés, traces, métriques, alertes
- **Sécurité** : secrets vault, chiffrement, RBAC, journaux d’accès

## Checklist de tests techniques (sans secrets)

1. Vérifier si `/rest/servicedeskapi/info` ou endpoints équivalents répondent.
2. Tester accès à `/rest/api/2/myself` (si Jira core exposé) pour confirmer auth.
3. Lister service desks (si autorisé) : `/rest/servicedeskapi/servicedesk`.
4. Lister request types : `/rest/servicedeskapi/servicedesk/{id}/requesttype`.
5. Créer une demande (si autorisé) : `/rest/servicedeskapi/request`.
6. Ajouter pièce jointe (si autorisé) : endpoint d’attachment JSM.
7. Capturer les contraintes : taille PJ, formats, timeouts, quotas.

## Livrables finaux exigés

1. **Feasibility memo** (1–2 pages) :
   - conclusion API : oui/non/partiel
   - risques et mitigations
   - recommandation (Go / No‑Go)
2. **Schéma d’architecture (texte)** MVP + version durcie.
3. **Plan d’implémentation** (milestones 2–6 semaines) + estimations.
4. **Liste de questions client** (tech + métier + sécurité).

## Contraintes de sortie

- Réponse en français.
- Orientée exécution (étapes concrètes, tests, décisions).
- Zéro secret dans la sortie.
- Si une hypothèse est faite, la signaler et proposer comment la valider.

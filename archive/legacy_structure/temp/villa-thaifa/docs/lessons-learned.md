# Leçons Apprises — Villa Thaifa

> Ce fichier documente les erreurs et apprentissages pour éviter de les répéter.
> À consulter par les futurs agents IA et humains travaillant sur ce dossier.

---

## [2025-12-19] Communication Client : Pattern Scout → Rapport → Action

### L'erreur

Envoyé un message à Said demandant des infos (nom invité, tarif, nb adultes) **SANS** d'abord lui faire un rapport de ce qu'on avait découvert en tant qu'éclaireur/scout.

**Contexte** : Mission de booking chambre 11 sur HotelRunner. On a réussi à se connecter, vérifié la disponibilité, préparé le formulaire — mais on a demandé des infos au client sans lui communiquer ces bonnes nouvelles d'abord.

**Impact** : Le client reçoit des questions sans contexte → impression qu'on ne maîtrise pas la situation.

### Ce qui aurait dû être fait

```text
1. SCOUT    → Explorer la plateforme, vérifier la faisabilité
2. RAPPORT  → Tenir Omar informé des découvertes, puis déterminer si Omar (qui fait donc office de passerelle / pont entre notre équipe IA et nos clients) s'il doit remonter l'information et/ou la garder pour nous (notre équipe IA)
3. QUESTIONS → Demander les infos manquantes (avec contexte)
4. ACTION   → Exécuter quand tout est clair
```

### Pattern correct

| Phase         | Action                 | Exemple                                |
| ------------- | ---------------------- | -------------------------------------- |
| **Scout**     | Explorer en éclaireur  | Se connecter, vérifier dispo           |
| **Rapport**   | Informer le client     | "Bonne nouvelle, la chambre est dispo" |
| **Questions** | Demander ce qui manque | "Pour finaliser, j'ai besoin de..."    |
| **Action**    | Exécuter               | Créer la réservation                   |

### Checklist communication client

Avant d'envoyer un message à Omar, vérifier :

- [ ] Ai-je TOUT le **contexte** pour comprendre la situtation ou pas ?
- [ ] Ai-je informé le Omar de ce que j'ai **découvert** ?
- [ ] Omar a-t-il le **contexte** pour comprendre mes questions ?
- [ ] Mon message montre-t-il qu'on **maîtrise** la situation ou pas ?
- [ ] Ai-je fait preuve d'**empathie** (me mettre à sa place) ?

### Message correctif envoyé

Après avoir réalisé l'erreur, message de suivi envoyé :

```
Au fait Omar, j'aurais dû commencer par ça :

Bonne nouvelle — on a réussi à se connecter à HotelRunner et la chambre 11
(suite familiale) est bien DISPONIBLE pour les 2 nuitées !

Le formulaire de réservation est prêt, il me manque juste les infos que
je t'ai demandées dans mon message précédent.

[Entity name]
```

### Leçon retenue

> **Ne jamais présumer que le client sait ce qu'on sait.**
> Toujours faire un rapport avant de demander des actions/infos.
> L'empathie client = se mettre à sa place et imaginer ce qu'il reçoit.

---

## [2025-12-19] Ton de communication : Adapter le registre au contexte

### L'erreur

Messages proposés avec un ton trop informel/familier ("tu", style décontracté) pour un client de +60 ans dans un contexte professionnel.

**Exemple problématique** :

```
Au fait Said, j'aurais dû commencer par ça...
```

**Ce qui aurait dû être écrit** :

```
Monsieur Thaifa,

Veuillez m'excuser, j'aurais dû commencer par vous informer que...
```

### Facteurs à considérer

| Facteur  | Impact sur le registre          |
| -------- | ------------------------------- |
| Relation | Nouveau client → formel         |
| Culture  | Maroc → respect des aînés       |
| Enjeu    | High-ticket → professionnalisme |

### Registre correct pour ce client

- ✅ **Vouvoiement** obligatoire
- ✅ **Respect** sans rigidité corporate
- ❌ Pas de : "Salut", "tu", abréviations familières

### Adaptation au canal (WhatsApp)

| Situation                        | Approche                             |
| -------------------------------- | ------------------------------------ |
| **1er message du jour**          | Salutation + signature               |
| **Messages suivants (même fil)** | Direct, fluide, pas de re-salutation |
| **Message important/formel**     | Salutation + signature               |

**Exemple fluide (message de suivi)** :

```
Excusez-moi, j'aurais dû commencer par là :
Bonne nouvelle — [contenu]
```

**Pas besoin de** : "Monsieur Thaifa" + "Cordialement, Omar" à CHAQUE message.

### Checklist avant envoi message client

- [ ] Ai-je utilisé le vouvoiement ?
- [ ] Le ton est-il adapté à l'âge et au statut du client ?
- [ ] Y a-t-il une formule de politesse appropriée ?
- [ ] Le message est-il structuré professionnellement ?

### Leçon retenue

> **Toujours adapter le registre de communication au contexte du client.**
> En cas de doute, opter pour le registre le plus formel.
> Un message trop formel est rarement mal perçu ; un message trop familier peut l'être.

---

## [2025-12-20] Livrables Client : Fichiers Prêts à l'Emploi

### L'erreur

Créé un fichier `.md` avec le message WhatsApp contenant des métadonnées, des sections d'explication, du contexte — alors qu'Omar avait besoin d'un fichier `.txt` prêt à copier-coller directement.

**Ce qui a été fait** :

```
draft-message-rapport-reservations.md  ← Markdown avec métadonnées
```

**Ce qui était attendu** :

```
2025-12-20-message-rapport-reservations.txt  ← Texte brut prêt à copier
```

### Impact

- Omar doit extraire manuellement le message du fichier markdown
- Perte de temps
- Friction inutile dans le workflow

### Ce qui aurait dû être fait

Quand on prépare un livrable pour envoi client (message, email, document) :

| Type                 | Format           | Nommage                          |
| -------------------- | ---------------- | -------------------------------- |
| Message WhatsApp/SMS | `.txt`           | `YYYY-MM-DD-message-[sujet].txt` |
| Email                | `.txt` ou `.eml` | `YYYY-MM-DD-email-[sujet].txt`   |
| Rapport/Document     | `.pdf`           | `rapport-[sujet]-YYYY-MM-DD.pdf` |
| Notes internes       | `.md`            | Libre                            |

### Structure livrables

```
communication/
├── whatsapp/
│   ├── 2025-12-20-message-rapport-reservations.txt  ← Prêt à copier
│   └── draft-*.md                                    ← Brouillons/notes
│
projects/[projet]/
└── deliverables/
    └── rapport-[sujet]-YYYY-MM-DD.pdf               ← PDF final
```

### Checklist avant création livrable client

- [ ] Le fichier est-il **directement utilisable** sans extraction ?
- [ ] Le format est-il adapté à l'usage (`.txt` pour copier, `.pdf` pour envoyer) ?
- [ ] Le nommage inclut-il la **date** et le **sujet** ?
- [ ] Le fichier est-il dans le **bon dossier** (deliverables/, whatsapp/) ?

### Leçon retenue

> **Un livrable client doit être prêt à l'emploi, pas un document de travail.**
> Toujours se demander : "Omar peut-il utiliser ce fichier immédiatement sans manipulation ?"
> Si non → mauvais format ou mauvaise structure.

---

## [2025-12-22] Confusion Dates : Vérifier les Années

### L'erreur

Dates mentionnées sans année explicite, créant confusion entre 2024 et 2025. Particulièrement problématique lors du passage d'année (décembre → janvier).

### Impact

- Mauvaise compréhension des délais
- Risque de planification incorrecte
- Confusion dans l'historique des réservations

### Ce qui doit être fait

| Situation                         | Action                     |
| --------------------------------- | -------------------------- |
| Client mentionne "le 20 décembre" | Demander/confirmer l'année |
| Date proche du Nouvel An          | Double-vérifier l'année    |
| Réservation pour "janvier"        | Clarifier 2025 ou 2026     |

**Pattern de vérification** :

- Toujours spécifier l'année complète (ex: "20 décembre 2025")
- Vérifier l'année quand un client mentionne juste le mois/jour
- Attention particulière au passage d'année (déc → jan)

### Leçon retenue

> **Toujours vérifier l'année.** "Le 20 décembre" peut être 2024 ou 2025.
> Ne jamais présumer — toujours expliciter.

---

## Template pour futures leçons

```markdown
## [YYYY-MM-DD] Titre court

### L'erreur

[Description factuelle de ce qui s'est passé]

### Impact

[Conséquences de l'erreur]

### Ce qui aurait dû être fait

[La bonne approche]

### Leçon retenue

[Principe généralisable]
```

## [2025-12-23] Room Structure Feedback from Said

**What happened**: After state-management restructuring, presented data to Said. He requested room-centric view instead of type-grouped.

**Why it matters**: Client's daily operations reference rooms by number. Our structure should match his workflow.

**Root cause**: Technical structure was based on data normalization (group by type) rather than user's mental model (individual rooms).

**Action taken**: Restructured to individual room files + facilities model.

**Future prevention**:

- Always validate data structure with primary user before finalizing
- Ask: "How do you talk about these entities in daily work?"
- Client-facing data should use client's vocabulary (ubiquitous language)

**Pattern recognized**: Client-Centric Data Modeling (documented in `shared/memory/patterns.md`)

---

## [2025-12-28] Économie des Commissions — CRITIQUE pour toutes les instances

### Contexte Business

| Canal                     | Commission | Sur 1000€  |
| ------------------------- | ---------- | ---------- |
| Booking.com               | **25%**    | Net: 750€  |
| Expedia, etc.             | ~15-25%    | Variable   |
| Direct (téléphone, email) | **0%**     | Net: 1000€ |

### Pourquoi c'est ÉNORME

```
Réservation directe = +33% de marge nette vs Booking.com
```

**Villa Thaifa va connecter 20+ plateformes** → L'impact des commissions est MASSIF.

### Implication pour les Agents IA

> **M. Thaifa préfère les réservations directes quand possible.**
> Ce n'est PAS juste une préférence personnelle — c'est une décision économique rationnelle.
> Même pour des clients qui ne sont pas amis/famille.

**TOUJOURS COMPRENDRE**:

- Réservation "directe" sur HotelRunner = client qui a contacté directement = 0% commission
- Réservation via Booking/Expedia = 25% de commission perdue
- Quand M. Thaifa dit "réservation directe" → c'est pour économiser les commissions

### Leçon retenue

> **Les plateformes de réservation sont un canal d'ACQUISITION, pas l'objectif.**
> L'objectif est de maximiser les revenus nets — les réservations directes y contribuent.

---

## [2025-12-28] Tunnel Vision — Cas Chambre 5 "Sync Bug"

### L'erreur (Tunnel Vision)

Une instance IA a vu:

- Chambre 5 réservée sur HotelRunner (Benchekroum)
- Mais pas visible sur Booking.com

**Conclusion hâtive**: "BUG DE SYNC! P0! INVESTIGATION URGENTE!"

### Ce qui a été manqué (ZOOM OUT)

La vraie question aurait dû être:

> "Cette réservation est-elle CENSÉE être sur Booking.com?"

**Réponse probable**: Non. C'est une réservation directe.

- Les réservations directes sont créées sur HotelRunner uniquement
- Elles ne sont PAS synchronisées vers Booking.com automatiquement
- Il faut bloquer manuellement les dates sur Booking.com

### Le vrai problème

Ce n'est pas un "bug de sync" — c'est:

1. Un gap de connaissance sur le fonctionnement des plateformes
2. Un workflow non documenté pour les réservations directes

### Pattern Anti-Tunnel Vision

Avant de créer une mission "investigation de bug", TOUJOURS demander:

```
1. Est-ce un bug ou un comportement que je ne comprends pas?
2. Ai-je ZOOM OUT sur le contexte business?
3. Ai-je vérifié les hypothèses de base?
```

### Documentation associée

- Stratégie complète: `docs/strategic/2025-12-28-platform-mastery-strategy.md`
- Skill: `.claude/skills/tunnel-vision-prevention/`

---

## [2025-12-28] Gap de Connaissance Plateformes

### Constat

Ni les agents IA ni Omar ne maîtrisent vraiment:

- HotelRunner (Channel Manager)
- Booking.com Extranet
- Le room mapping entre les deux
- Les flux de synchronisation

### Risque

Sans cette maîtrise:

- Erreurs de réservation possibles
- Problèmes de sync incompris
- Tunnel vision sur des "bugs" qui n'en sont pas

### Plan

Un projet "Platform Mastery" est documenté dans:
`docs/strategic/2025-12-28-platform-mastery-strategy.md`

### Leçon retenue

> **Avant d'opérer sur une plateforme, s'assurer qu'on la comprend.**
> Si on ne comprend pas → documenter le gap et planifier l'apprentissage.

---

## [2025-12-28] HotelRunner — Workflow Ajustement de Prix

### Découverte

Pour modifier le prix lors d'une réservation manuelle sur HotelRunner:

### Chemin

```
Réservations > Nouvelle réservation > 2. Sélectionner le type de chambre
```

### Étapes

1. Sélectionner le type de chambre (ex: "Chambre Double Superieur")
2. Cliquer sur le dropdown **"Nbre de chambres"**
3. Sélectionner le nombre de chambres (ex: 1)
4. Une fois sélectionné → un lien **"Ajustement de prix"** apparaît
5. Cliquer sur "Ajustement de prix"
6. Un menu pop-up s'ouvre permettant de modifier le prix

### Cas d'usage

- Réservations directes avec tarif négocié
- Promos spéciales non configurées dans le système
- Tarifs amis/famille

### Leçon retenue

> **Le prix n'est pas modifiable directement dans le champ.**
> Il faut passer par "Ajustement de prix" qui apparaît APRÈS avoir sélectionné le nombre de chambres.

---

## [2025-12-28] Extension Chrome — Problèmes avec HotelRunner

### Problème observé

L'extension Claude in Chrome perd fréquemment la connexion avec les onglets HotelRunner. Les onglets se "détachent" après quelques interactions.

### Impact

- Automatisation des réservations difficile
- Nécessite de recréer des onglets fréquemment
- Parfois impossible de compléter une tâche automatiquement

### Workaround actuel

- Fournir des instructions manuelles détaillées à Omar
- Omar exécute manuellement pendant que l'IA guide

### Investigation future

- Vérifier si c'est un problème de permissions de l'extension
- Tester avec d'autres navigateurs
- Explorer l'API HotelRunner comme alternative

---

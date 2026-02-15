# 🧪 TESTING SCENARIOS - Villa Thaifa

> **Purpose**: Scénarios de test pour valider les 17 agents
> **Created**: 2026-01-16
> **Status**: READY FOR TESTING
> **Data**: MOCK DATA (à confirmer avec Said Thaifa)

---

## 📋 OVERVIEW

**Objectif**: Valider le système d'agents sur des scénarios réalistes

**Approche**:

- ✅ Mock data réaliste pour tester immédiatement
- ⚠️ Marqueurs [CONFIRMER AVEC SAID] pour données critiques
- 🔍 Focus sur validation des workflows, pas la précision des données

**Scénarios**: 4 scénarios couvrant les principaux workflows

---

## 🎯 SCENARIO 1: Pricing Analysis (Unitaire)

### Agent Testé

**pricing-analyst** (Opus)

### Contexte

**Saison**: Haute saison (été)
**Occupancy**: 60% (7 chambres occupées sur 12)
**Concurrents**: 3 guesthouses similaires à Marrakech

### Input Data (MOCK)

```yaml
property:
  name: Villa Thaifa
  location: Marrakech, Maroc
  rooms: 12 chambres

  # [CONFIRMER AVEC SAID] Prix actuels
  current_rates:
    low_season: 300-400 MAD/nuit
    high_season: 500-700 MAD/nuit
    peak_season: 800-1000 MAD/nuit

  # [CONFIRMER AVEC SAID] Occupation actuelle
  occupancy:
    date: 2026-01-16
    occupied: 7/12 rooms
    checkouts_today: 2
    checkins_today: 1

competitors:
  - name: Riad Dar Jameel
    rate: 650 MAD/nuit
    occupancy: 75%

  - name: Guesthouse Mansour
    rate: 580 MAD/nuit
    occupancy: 68%

  - name: Riad Zyneb
    rate: 720 MAD/nuit
    occupancy: 82%
```

### Output Attendu

**pricing-analyst** doit générer:

1. **Analyse de marché**:

   - Positionnement vs concurrents
   - Opportunités de pricing

2. **Recommandations de prix**:

   - Prix suggérés pour les 7 prochains jours
   - Justification basée sur occupancy + concurrents

3. **Actions suggérées**:
   - Ajuster prix ?
   - Promotions ?
   - Last-minute offers ?

### Success Criteria

- ✅ Recommandations logiques (pas de prix aberrants)
- ✅ Justification claire avec données
- ✅ Actions spécifiques proposées
- ✅ Format structuré (pas de prose infinie)

### Test Execution

```bash
# Lancer pricing-analyst avec le mock data
# Observer la sortie
# Valider contre les success criteria
```

---

## 🎯 SCENARIO 2: Reservation Cycle (Intégré)

### Agents Testés

**reservation-manager** + **calendar-agent** (Sonnet)

### Contexte

**Nouvelle réservation**: Client veut réserver pour dates spécifiques

### Input Data (MOCK)

```yaml
guest:
  name: Jean Dupont
  email: jean.dupont@example.com # [CONFIRMER FORMAT]
  phone: "+33 6 12 34 56 78" # [CONFIRMER FORMAT]
  language: fr

reservation_request:
  check_in: 2026-02-01
  check_out: 2026-02-05
  guests: 2 people
  room_preference: "Chambre avec vue jardin"

  # [CONFIRMER AVEC SAID] Disponibilité réelle
  requested_room_type: "double"
```

### Workflow Attendu

**Step 1: calendar-agent vérifie disponibilité**

1. Check disponibilité pour dates demandées
2. Identify chambres disponibles
3. Return options

**Step 2: reservation-manager gère la réservation**

1. Crée la réservation
2. Envoie confirmation (template)
3. Met à jour le calendrier

### Output Attendu

**calendar-agent**:

- Liste de chambres disponibles
- Prix par chambre
- Recommandation

**reservation-manager**:

- Réservation créée avec ID
- Confirmation email/WhatsApp template
- Calendrier mis à jour

### Success Criteria

- ✅ Disponibilité vérifiée correctement
- ✅ Réservation créée sans erreur
- ✅ Confirmation générée (template)
- ✅ Pas de conflit de dates

### Test Execution

```bash
# Lancer calendar-agent pour vérifier disponibilité
# Lancer reservation-manager pour créer réservation
# Vérifier que les données sont cohérentes
```

---

## 🎯 SCENARIO 3: Multilingual Communication (Intégré)

### Agents Testés

**guest-communicator** + **translation-agent** (Sonnet + Haiku)

### Contexte

**Client anglais** pose une question, répondre en français

### Input Data (MOCK)

```yaml
guest:
  name: John Smith
  language: en
  message: "Hi, I would like to know if you have airport pickup service?"

# [CONFIRMER AVEC SAID] Services réels disponibles
services:
  airport_pickup: true # À CONFIRMER
  airport_pickup_cost: 150 MAD
  breakfast: true
  breakfast_included: false
  breakfast_cost: 50 MAD
```

### Workflow Attendu

**Step 1: guest-communicator recoit message**

1. Detect language (en)
2. Comprend question (airport pickup)
3. Prépare réponse

**Step 2: translation-agent traduit**

1. Traduit réponse de FR → EN
2. Garde tone professionnel
3. Vérifie qualité

### Output Attendu

**guest-communicator** (français):

```
Bonjour John,

Oui, nous proposons un service de navette aéroport.
Le coût est de 150 MAD par trajet.

Souhaitez-vous que nous réservions votre navette ?
Cordialement,
Villa Thaifa
```

**translation-agent** (anglais):

```
Hello John,

Yes, we offer airport pickup service.
The cost is 150 MAD per trip.

Would you like us to book your airport pickup?
Best regards,
Villa Thaifa
```

### Success Criteria

- ✅ Question comprise correctement
- ✅ Réponse adaptée au service
- ✅ Traduction naturelle (pas robotique)
- ✅ Tone professionnel conservé
- ✅ Information correcte (prix, service)

### Test Execution

```bash
# Envoyer message EN
# Lancer guest-communicator
# Lancer translation-agent
# Vérifier la qualité de la traduction
```

---

## 🎯 SCENARIO 4: Data Validation (Intégré)

### Agents Testés

**platform-validator** + **data-sync-checker** (Sonnet)

### Contexte

**Incohérence détectée**: Prix différents entre Booking.com et système interne

### Input Data (MOCK)

```yaml
inconsistency:
  source: "Booking.com vs Internal System"
  date: "2026-01-16"

booking_dot_com:
  room: "Chambre Double Vue Jardin"
  rate: 650 MAD/nuit
  availability: "Available"

internal_system:
  room: "Chambre Double Vue Jardin"
  rate: 580 MAD/nuit
  availability: "Available"

# [CONFIRMER AVEC SAID] Quelle est la source de vérité ?
truth_source: "unknown" # À définir
```

### Workflow Attendu

**Step 1: data-sync-checker détecte l'incohérence**

1. Compare les sources
2. Identify les différences
3. Alert sur l'incohérence

**Step 2: platform-validator analyse**

1. Détermine quelle source est fiable
2. Propose une résolution
3. Suggère des actions

### Output Attendu

**data-sync-checker**:

- Alert: Incohérence détectée
- Détails: Prix diffèrent (650 vs 580 MAD)
- Impact: Revenue impact

**platform-validator**:

- Analyse: Booking.com = source de vérité (probable)
- Recommandation: Mettre à jour système interne
- Action: Sync nécessaire

### Success Criteria

- ✅ Incohérence détectée
- ✅ Impact évalué (revenue loss)
- ✅ Recommandation claire
- ✅ Action spécifique proposée

### Test Execution

```bash
# Créer incohérence volontaire
# Lancer data-sync-checker
# Lancer platform-validator
# Vérifier que l'incohérence est bien détectée
```

---

## 📊 TEST EXECUTION PLAN

### Phase 1: Tests Unitaires (1-2 heures)

1. **Scenario 1**: Pricing Analysis

   - Lancer pricing-analyst
   - Valider output
   - Documenter résultats

2. **Scenario 2**: Reservation Cycle
   - Lancer calendar-agent
   - Lancer reservation-manager
   - Valider workflow

### Phase 2: Tests Intégrés (2-3 heures)

3. **Scenario 3**: Multilingual Communication

   - Lancer guest-communicator + translation-agent
   - Valider traduction
   - Checker qualité

4. **Scenario 4**: Data Validation
   - Lancer data-sync-checker + platform-validator
   - Valider détection
   - Checker recommendations

### Phase 3: Tests Complet (Optionnel)

5. **Full Workflow**: Réservation → Pricing → Communication
   - Enchaîner tous les agents
   - Valider system complet
   - Identifier problèmes d'intégration

---

## 🎯 SUCCESS CRITERIA (GLOBAL)

### Par Scenario

- ✅ Output conforme aux attentes
- ✅ Pas d'erreurs critiques
- ✅ Données cohérentes

### Global

- ✅ 3/4 scénarios passent
- ✅ 0 bloquant bugs
- ✅ Agents interagissent correctement
- ✅ Handover protocol fonctionne

---

## ⚠️ DATA A CONFIRMER AVEC SAID

### Critique

- [ ] Prix réels des chambres (low/high/peak season)
- [ ] Occupation actuelle
- [ ] Services disponibles (airport pickup, breakfast, etc.)
- [ ] Coûts des services
- [ ] Sources de vérité (Booking.com vs interne)
- [ ] Processus de réservation réel
- [ ] Templates de communication

### Important

- [ ] Préférences client (confirmation par email/WhatsApp)
- [ ] Langues supportées
- [ ] Payment methods
- [ ] Cancellation policy

### Optionnel

- [ ] Concurrents réels
- [ ] Pricing strategy actuelle
- [ ] Business goals (revenue targets)

---

## 📝 RESULTS TEMPLATE

Pour chaque scénario, documenter:

```markdown
### Scenario X: [Nom]

**Status**: ✅ PASS / ❌ FAIL

**Results**:

- Output conforme: OUI/NON
- Erreurs rencontrées: [Liste]
- Bugs découverts: [Liste]

**Notes**:

- [Observations]

**Next Steps**:

- [Actions requises]
```

---

## 🔄 FEEDBACK LOOP

### Si un scénario échoue

1. **Documenter l'erreur**
2. **Identifier la cause** (agent vs data)
3. **Proposer fix**
4. **Re-tester**

### Si un scénario réussit

1. **Documenter le succès**
2. **Créer template**
3. **Ajouter aux cas d'usage**
4. **Célébrer** 🎉

---

**END OF TESTING SCENARIOS**

> Quality > Speed
> Test with mock data, replace with real data later
> Focus on workflows, not data precision

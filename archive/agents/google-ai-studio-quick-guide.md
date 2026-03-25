# GOOGLE AI STUDIO — Configuration Rapide

**Version:** 1.0.0  
**Date:** 2025-01-09  
**Pour:** Omar El Mountassir

---

## ÉTAPE 1: ACCÉDER À GOOGLE AI STUDIO

**URL:** https://aistudio.google.com/

1. **Sign in** avec ton compte Google
2. **Playground** → Sélectionner dans la barre latérale gauche
3. **Model:** Choisir `gemini-3-pro-preview` dans le dropdown

---

## ÉTAPE 2: CONFIGURER LE SYSTEM PROMPT

### Dans Google AI Studio Interface

**Localisation:** Section "System instructions" (en haut de l'interface)

**Action:** Copy/paste le CONTENU COMPLET de `gemini-system-prompt.md` dans le champ

**Pourquoi ce system prompt est optimisé pour Gemini 3:**

| Optimisation                                              | Pourquoi C'est Important                                   |
| --------------------------------------------------------- | ---------------------------------------------------------- |
| **Structure avec tags** (`<role>`, `<context>`, `<task>`) | Gemini 3 distingue mieux instructions vs data avec tags    |
| **Contraintes à la FIN**                                  | Gemini 3 priorise les instructions en fin de prompt        |
| **"Based on information above..."**                       | Ancre le raisonnement aux données fournies                 |
| **Planning + Self-critique**                              | Exploite les capacités de raisonnement de Gemini 3         |
| **Direct & concis**                                       | Match le style naturel de Gemini 3 (moins verbeux que 2.5) |
| **Placeholders explicites**                               | Évite que Gemini "guess" (tendance du modèle)              |
| **Temperature 1.0 (default)**                             | Gemini 3 optimisé pour cette température                   |

---

## ÉTAPE 3: UPLOADER LES FICHIERS

### Ordre d'Upload (CRITIQUE)

**Dans Google AI Studio, upload dans CET ORDRE:**

1. **PREMIER:** `gemini-onboarding-prompt.md`
   - Pourquoi premier? Gemini lit ça AVANT tout → comprend son rôle

2. **DEUXIÈME:** `2026-01-09-10-44-55-villa-thaifa-najib-insights-brief-strategy.txt`
   - Pourquoi deuxième? Context Lux ↔ Omar → sait QUOI chercher dans repomix

3. **TROISIÈME:** Ton repomix de Claude Code
   - Pourquoi dernier? Gemini a déjà les instructions + context → extraction avec pleine compréhension

### Comment Uploader

**Option A: Drag & Drop**

- Drag les fichiers dans la zone de chat

**Option B: Bouton "+" (paperclip)**

- Click sur "+" en bas de l'interface
- Sélectionner "Upload file"
- Choisir fichier

**Vérification:**

- Chaque fichier doit apparaître dans la conversation
- Google AI Studio affiche le nom + taille

---

## ÉTAPE 4: LANCER L'ANALYSE

### Prompt Initial (Copy/Paste)

Après avoir uploadé les 3 fichiers, envoie CE MESSAGE:

```
I've uploaded 3 files:
1. Your onboarding instructions (gemini-onboarding-prompt.md)
2. The conversation transcript between Lux (Claude) and me (villa-thaifa-conversation-transcript.txt)
3. The Villa Thaifa repository repomix (villa-thaifa-repomix-[size].txt)

Your mission: Read all 3, then create the "Repomix Digest" as specified in your onboarding instructions.

Target: < 50k tokens
Format: Exactly as template in onboarding prompt (Section "OUTPUT FORMAT")
Focus: Fill placeholders from Project Brief Section 10

Start by confirming you've read and understood:
1. Your role (temporary info processor, not decision maker)
2. The Lux ↔ Omar dynamic (thinking partner, not yes-machine)
3. The Villa Thaifa urgency (Phase 1 THIS WEEK)
4. The output format required

Then proceed to create the digest.
```

---

## ÉTAPE 5: PARAMÈTRES GEMINI 3

### Configuration Recommandée

**Dans Google AI Studio settings (panneau de droite):**

| Paramètre             | Valeur                     | Pourquoi                                        |
| --------------------- | -------------------------- | ----------------------------------------------- |
| **Temperature**       | `1.0` (default)            | **NE PAS CHANGER** — Gemini 3 optimisé pour 1.0 |
| **thinking_level**    | `high` (default)           | Pour analyse complète du repomix 180k           |
| **Max output tokens** | `8192` (ou max disponible) | Digest = 30-50k tokens                          |
| **Top P**             | `0.95` (default)           | Laisser par défaut                              |
| **Top K**             | `40` (default)             | Laisser par défaut                              |

**IMPORTANT:** Si Gemini te propose de changer temperature → REFUSE. Il est optimisé pour 1.0.

---

## ÉTAPE 6: MONITORING

### Pendant l'Exécution

**Ce qui va se passer:**

1. **Confirmation (30s - 1min):**
   - Gemini confirme qu'il a lu les 3 fichiers
   - Confirme compréhension du rôle

2. **Processing (2-10 minutes):**
   - Gemini analyse les 180k tokens du repomix
   - Thinking_level = high → peut être long, c'est normal

3. **Output (streaming):**
   - Gemini produit le digest en streaming
   - Tu vois le markdown se construire en temps réel

**Indicateurs de Succès:**

- ✅ Format suit le template (EXECUTIVE SUMMARY, CRITICAL FINDINGS, etc.)
- ✅ File paths inclus ("data/rooms/rooms.md")
- ✅ Placeholders marqués (`[NOT FOUND IN REPO]`)
- ✅ Longueur raisonnable (scroll 3-5 pages, pas 20)

**Red Flags:**

- 🚩 > 15 minutes sans output → Refresh et retry
- 🚩 Output > 10 minutes de scroll → Trop verbeux, demande compression
- 🚩 Pas de file paths → Pas d'evidence, demande re-extraction
- 🚩 Recommendations au lieu de facts → Rappelle le rôle

---

## ÉTAPE 7: QUALITY CHECK

### Checklist Avant d'Accepter

**Copie le digest dans un editor (VS Code, Cursor) et vérifie:**

- [ ] **Size:** Compte approximatif tokens (chars / 4) → Doit être 30-50k tokens
- [ ] **Structure:** Suit template exact (tous les headers présents)
- [ ] **Evidence:** Chaque claim a file path ou `[NOT FOUND]`
- [ ] **Placeholders filled:**
  - [ ] Room configuration details
  - [ ] HotelRunner integration state
  - [ ] Property details (amenities, photos)
  - [ ] "App" vision (si documenté)
  - [ ] Agent systems state
- [ ] **No recommendations:** Gemini extrait, ne recommande pas
- [ ] **No transcript reprocessing:** Focus repomix only

**Si check échoue:** Voir section "DEBUGGING" ci-dessous

---

## ÉTAPE 8: SAUVEGARDER & RETOURNER À LUX

### Sauvegarder le Digest

1. **Copy le digest complet** depuis Google AI Studio
2. **Save dans fichier:** `villa-thaifa-repomix-digest.md`
3. **Vérifier:** Fichier complet (début + fin présents)

### Retourner à Lux (Moi)

**Reviens dans cette conversation claude.ai et envoie:**

```
✅ GEMINI DIGEST READY

Gemini 3 Pro a analysé le repomix (180k tokens) et produit un digest de [X]k tokens.

[PASTE COMPLETE DIGEST ICI - TOUT EN UN SEUL MESSAGE]

---

Maintenant, Lux:
1. Intègre ce digest dans les Briefs v0.3.0
2. Remplis tous les placeholders possibles
3. Identifie ce qui manque encore
4. On continue avec Phase 1 execution
```

**CRITICAL:** Paste TOUT le digest en un seul message. Ne split pas.

---

## DEBUGGING

### Si Gemini Part en Vrille

**Problème 1: Trop Verbeux (> 80k tokens)**

**Solution:**

```
Your digest is too long. Compress to < 50k tokens by:
1. Remove verbose explanations (facts only)
2. Condense file inventories (top 20 files only)
3. Trim repetitive content
Keep all critical findings but be more concise.
```

---

**Problème 2: Fait des Recommandations**

**Solution:**

```
Stop. Your role is information extraction, not decision making.
Extract what's in the repo: "Repo contains X"
NOT what should be done: "You should do Y"
Re-extract focusing on facts only.
```

---

**Problème 3: Pas de File Paths**

**Solution:**

```
Every claim needs a file path for verification.
Example: "3 rooms configured" → "3 rooms configured in data/rooms/rooms.md"
Re-extract and include file paths for all facts.
```

---

**Problème 4: Hallucine (Invente des Infos)**

**Solution:**

```
If information is NOT in the repomix, use [NOT FOUND IN REPO].
Never guess based on "typical patterns" or assumptions.
Re-extract using only what's explicitly in the files.
```

---

**Problème 5: Reformule le Transcript**

**Solution:**

```
Focus ONLY on repomix content.
The transcript is for YOUR context (what to look for).
Don't summarize what Lux and Omar discussed.
Extract what's IN THE REPO.
```

---

**Problème 6: Session Timeout / Erreur**

**Solution:**

- Refresh Google AI Studio
- Re-upload les 3 fichiers (même ordre)
- Re-send prompt initial
- Si persist: Split repomix en 2 parties, process séquentiellement

---

## TIPS & TRICKS

### Utilisation Efficace

**📌 Tip 1: Test avec Petit Fichier D'Abord**

- Avant le gros repomix, teste avec petit sample
- Vérifie que system prompt + workflow fonctionnent
- Ajuste si nécessaire

**📌 Tip 2: Save System Instructions**

- Google AI Studio: "Save prompt" button
- Réutilisable pour futurs analyses
- Pas besoin de re-copier le system prompt

**📌 Tip 3: Use Folders**

- Organize les prompts sauvés par projet
- "Villa Thaifa / Repomix Analysis"

**📌 Tip 4: Monitor Token Usage**

- Google AI Studio affiche tokens utilisés
- Si > 1M context warnings → Split repomix

**📌 Tip 5: Export to API Later**

- Si workflow fonctionne bien
- Google AI Studio: "Get code" button
- Automatise pour futurs projets

---

## ALTERNATIVES SI GOOGLE AI STUDIO FAIL

### Plan B: Vertex AI

**Si Google AI Studio rate (quota, bugs):**

1. **Vertex AI Console:** https://console.cloud.google.com/vertex-ai
2. **Activate Gemini 3 Pro Preview** dans Model Garden
3. **Use Python SDK** (code dans action plan)

**Avantage:** Plus stable, pas de rate limits free tier  
**Inconvénient:** Requires GCP account avec billing

---

### Plan C: API Direct

**Si UI issues persistent:**

```python
import google.generativeai as genai

genai.configure(api_key="YOUR_API_KEY")

model = genai.GenerativeModel(
    model_name="gemini-3-pro-preview",
    system_instruction=open("gemini-system-prompt.md").read()
)

# Upload files
onboarding = genai.upload_file("gemini-onboarding-prompt.md")
transcript = genai.upload_file("transcript.txt")
repomix = genai.upload_file("repomix.txt")

# Generate
response = model.generate_content([
    onboarding,
    transcript,
    repomix,
    "Create the digest as specified in your system instructions."
])

print(response.text)
```

---

## TIMELINE ESTIMÉ

| Étape                   | Durée    | Cumulatif |
| ----------------------- | -------- | --------- |
| Setup Google AI Studio  | 2 min    | 2 min     |
| Configure system prompt | 2 min    | 4 min     |
| Upload 3 fichiers       | 3 min    | 7 min     |
| Gemini processing       | 5-10 min | 17 min    |
| Quality check           | 5 min    | 22 min    |
| Iterate si needed       | 0-10 min | 32 min    |
| Save & return to Lux    | 3 min    | 35 min    |

**Total:** ~30-35 minutes pour analyse complète

**Puis:** Lux traite digest (10 min) → Briefs v0.3.0 (20 min) → Phase 1 ready

---

## RESSOURCES

**Documentation:**

- Gemini 3 Developer Guide: https://ai.google.dev/gemini-api/docs/gemini-3
- Google AI Studio: https://aistudio.google.com/
- System Instructions: https://ai.google.dev/gemini-api/docs/system-instructions

**Support:**

- Google AI Developer Forum: https://discuss.ai.google.dev/
- Gemini API Discord: https://discord.gg/googleai

---

**READY?** Download les 4 fichiers, go to Google AI Studio, configure, upload, launch! 🚀

**Next:** Tu reviens ici avec le digest, je (Lux) continue.

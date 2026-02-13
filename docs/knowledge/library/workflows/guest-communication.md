# Workflow : Communication Invités

> Process pour communiquer avec les invités/clients.

---

## Règles Fondamentales

| Règle                                   | Application                               |
| --------------------------------------- | ----------------------------------------- |
| **Vouvoiement**                         | TOUJOURS avec M. Thaifa et clients        |
| **SCOUT → REPORT → QUESTIONS → ACTION** | Ne jamais demander sans d'abord rapporter |
| **Ton formel**                          | Client senior = respect sans rigidité     |

---

## Pattern de Communication

### 1. SCOUT — Explorer d'abord

```
Avant de contacter le client :
- Vérifier les infos disponibles
- Préparer ce qu'on sait déjà
- Identifier ce qui manque
```

### 2. REPORT — Informer de nos découvertes

```
"Bonjour M. [Nom],

Bonne nouvelle — [ce qu'on a découvert/accompli].
[Détails pertinents]"
```

### 3. QUESTIONS — Demander ce qui manque (avec contexte)

```
"Pour finaliser, j'aurais besoin de :
- [Info 1]
- [Info 2]

Cordialement,
Omar"
```

### 4. ACTION — Exécuter quand tout est clair

```
Une fois toutes les infos reçues :
1. Confirmer la compréhension
2. Exécuter l'action
3. Confirmer le résultat au client
```

---

## Formats Messages

### WhatsApp — 1er message du jour

```
Bonjour M. [Nom],

[Contenu]

Cordialement,
Omar El Mountassir
```

### WhatsApp — Messages suivants (même fil)

```
[Contenu direct, pas de re-salutation]
```

### Message Important/Formel

```
Bonjour M. [Nom],

[Contenu structuré avec sections si nécessaire]

Restant à votre disposition,
Omar El Mountassir
Consultant Digital - Villa Thaifa
```

---

## Fichiers de sortie

| Type             | Destination                                          | Format                   |
| ---------------- | ---------------------------------------------------- | ------------------------ |
| Message WhatsApp | `data/communication/whatsapp/YYYY-MM-DD-{sujet}.txt` | Texte brut prêt à copier |
| Email            | `data/communication/email/YYYY-MM-DD-{sujet}.txt`    | Texte brut               |
| Rapport client   | `archive/YYYY/QQ/execution/deliverables/`            | PDF                      |

---

## Anti-patterns à éviter

| ❌ Mauvais              | ✅ Bon                  |
| ----------------------- | ----------------------- |
| "Salut Said"            | "Bonjour M. Thaifa"     |
| Questions sans contexte | REPORT avant QUESTIONS  |
| Tutoiement              | Vouvoiement TOUJOURS    |
| Message mur de texte    | Structure avec sections |

---

_Workflow v0.1.0-alpha.0_

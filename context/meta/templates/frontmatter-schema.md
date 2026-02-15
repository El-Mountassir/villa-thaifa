---
title: "Frontmatter Schema Standard"
description: "Métadonnées obligatoires pour tous les fichiers de documentation"
version: "1.0.0"
status: "published"
tags: [standards, frontmatter, schema]
---

# Frontmatter Schema Standard - Villa Thaifa Documentation

> **Version**: 1.0.0
> **Date**: 2026-01-16
> **Status**: Published
> **Applies to**: ALL markdown files in `docs/`

---

## Schema Complet

```yaml
---
# === IDENTIFIANTS ===
id: vt-<domain>-<entity>-<version>          # Ex: vt-ops-booking-manager-1-0-0
title: "Human Readable Title"                # Titre descriptif
description: "One-line description for search"  # SEO, preview

# === TYPOLOGIE ===
type: "agent|guide|process|reference|api|decision"  # Type de document
domain: "client|property|processes|communications|finance|platforms|system"
audience: ["agent", "human", "both"]         # Qui lit ce doc?

# === VERSIONING ===
version: "1.0.0"                             # Semantic versioning
created: 2026-01-16                          # Date de création
last_updated: 2026-01-16                     # Dernière modification
status: "draft|review|published|archived|deprecated"

# === RESPONSABILITÉ ===
author: "@claude|@omar|@client"              # Qui a écrit?
reviewer: "@omar|@client"                    # Qui doit reviewer?

# === ORGANISATION ===
tags: ["tag1", "tag2", "tag3"]               # Pour recherche/navigation
category: "operations|technical|strategic|compliance"
related: ["doc-id-1", "doc-id-2"]            # Liens vers docs connexes

# === AGENT-SPECIFIC (uniquement si type: agent) ===
agent_id: "booking-manager"                  # ID unique de l'agent
agent_name: "Booking Management Specialist"  # Nom lisible
orchestration:
  type: "specialist|generalist|coordinator"
  can_work_independently: true|false
  collaboration_style:
    - "lead_role_for_bookings"
    - "support_role_for_pricing"

capabilities: "docs/agents/booking-manager/capabilities.json"

context_mandatory:
  - docs/knowledge/mandatory/client-profile.md
  - docs/knowledge/mandatory/business-model.md

context_domain:
  - docs/knowledge/domain/operations/booking-policies.md
  - docs/knowledge/domain/operations/platform-workflows.md

context_mission: []                          # Vide si pas de mission assignée

dependencies:
  agents:
    - pricing-analyst
    - communication-manager
  tools:
    - booking_com_api
    - airbnb_api
    - google_calendar

# === TESTING & PERFORMANCE ===
testing:
  status: "in_progress|passing|failing"
  eval_suite: "tests/agents/booking-manager/"
  last_test: 2026-01-16
  pass_rate:
    unit: 0.85
    integration: 0.70
    regression: 0.90
  baseline:
    pass_at_1: 0.65
    pass_at_5: 0.85
---
```

---

## Champs Obligatoires vs Optionnels

### TOUJOURS Obligatoire (Tous les fichiers)

```yaml
---
id: vt-xxx-xxx-x-x-x
title: "Title"
description: "Description"
type: [agent|guide|process|reference|api|decision]
domain: [client|property|processes|communications|finance|platforms|system]
audience: ["agent", "human", "both"]
version: "1.0.0"
created: YYYY-MM-DD
last_updated: YYYY-MM-DD
status: [draft|review|published|archived|deprecated]
author: @username
tags: ["tag1", "tag2"]
---
```

### Optionnel (Recommandé)

```yaml
---
reviewer: @username
category: [operations|technical|strategic|compliance]
related: ["doc-id-1"]
---
```

### Optionnel (Agent-Seulement)

```yaml
---
agent_id: agent-name
agent_name: "Agent Name"
orchestration: {...}
capabilities: path/to/capabilities.json
context_mandatory: [...]
context_domain: [...]
context_mission: [...]
dependencies: {...}
testing: {...}
---
```

---

## Exemples Concrets

### Exemple 1: Agent Documentation

```yaml
---
id: vt-ops-booking-manager-1-0-0
title: "Booking Management Specialist Agent"
description: "Expert agent managing all booking operations across platforms"
type: agent
domain: operations
audience: ["agent", "human"]
version: "1.0.0"
created: 2026-01-16
last_updated: 2026-01-16
status: published
author: "@claude"
reviewer: "@omar"
tags: ["booking", "reservations", "multi-platform"]
category: operations
related: ["vt-ops-pricing-analyst-1-0-0", "vt-comms-communication-manager-1-0-0"]

agent_id: booking-manager
agent_name: Booking Management Specialist
orchestration:
  type: specialist
  can_work_independently: true
  collaboration_style:
    - "lead_role_for_bookings"
    - "support_role_for_pricing_decisions"

capabilities: docs/agents/booking-manager/capabilities.json

context_mandatory:
  - docs/knowledge/mandatory/client-profile.md
  - docs/knowledge/mandatory/operational-priorities.md

context_domain:
  - docs/knowledge/domain/operations/booking-policies.md
  - docs/knowledge/domain/operations/platform-workflows.md
  - docs/knowledge/domain/operations/seasonality-rules.md

dependencies:
  agents:
    - pricing-analyst
    - communication-manager
    - operations-manager
  tools:
    - booking_com_api
    - airbnb_api
    - hotelrunner_api
    - google_calendar
    - pricing_engine

testing:
  status: in_progress
  eval_suite: tests/agents/booking-manager/
  last_test: 2026-01-16
  pass_rate:
    unit: 0.85
    integration: 0.70
    regression: 0.90
---
```

### Exemple 2: Knowledge Base Article

```yaml
---
id: vt-client-said-thaifa-profile-1-0-0
title: "Client Profile: Said Thaifa"
description: "Profil complet du client Said Thaifa, propriétaire de Villa Thaifa"
type: guide
domain: client
audience: ["agent", "human"]
version: "1.0.0"
created: 2026-01-16
last_updated: 2026-01-16
status: published
author: "@omar"
reviewer: "@claude"
tags: ["client", "profile", "stakeholder"]
category: operations
related: ["vt-prop-villa-thaifa-1-0-0", "vt-ops-business-model-1-0-0"]
---
```

### Exemple 3: Process Documentation

```yaml
---
id: vt-proc-checkin-workflow-1-0-0
title: "Check-in Workflow Standard Operating Procedure"
description: "Processus complet de check-in des invités à Villa Thaifa"
type: process
domain: processes
audience: ["agent", "human"]
version: "1.0.0"
created: 2026-01-16
last_updated: 2026-01-16
status: published
author: "@claude"
reviewer: "@omar"
tags: ["checkin", "sop", "workflow", "guest-arrival"]
category: operations
related: ["vt-proc-checkout-workflow-1-0-0", "vt-prop-facilities-1-0-0"]
---
```

---

## Validation Rules

Les fichiers SONT valides si:

- ✅ Tous les champs obligatoires sont présents
- ✅ `id` suit le pattern `vt-<domain>-<entity>-<version>`
- ✅ `version` suit Semantic Versioning (X.Y.Z)
- ✅ `dates` sont en format ISO 8601 (YYYY-MM-DD)
- ✅ `type` est une des valeurs acceptées
- ✅ `domain` est une des valeurs acceptées
- ✅ `status` est une des valeurs acceptées
- ✅ `tags` est un tableau (même avec 1 seul élément)

Les fichiers NE SONT PAS valides si:

- ❌ Champ obligatoire manquant
- ❌ `id` ne suit pas le pattern
- ❌ `version` n'est pas en X.Y.Z
- ❌ `date` n'est pas en YYYY-MM-DD
- ❌ `type` ou `domain` ou `status` ont valeur invalide
- ❌ `tags` est une string (doit être tableau)

---

## Scripts de Validation

```bash
#!/bin/bash
# scripts/validate-frontmatter.sh

# Valide tous les fichiers .md dans docs/
find docs/ -name "*.md" -exec node scripts/validate-frontmatter.js {} \;

# Exit code 0 si tout est valide, 1 si erreur trouvée
```

```javascript
// scripts/validate-frontmatter.js
const fs = require('fs');
const yaml = require('yaml');

const REQUIRED_FIELDS = ['id', 'title', 'description', 'type', 'domain', 'audience', 'version', 'created', 'last_updated', 'status', 'author', 'tags'];

const VALID_TYPES = ['agent', 'guide', 'process', 'reference', 'api', 'decision'];
const VALID_DOMAINS = ['client', 'property', 'processes', 'communications', 'finance', 'platforms', 'system'];
const VALID_STATUSES = ['draft', 'review', 'published', 'archived', 'deprecated'];
const VALID_AUDIENCES = ['agent', 'human', 'both'];

function validateFrontmatter(filePath) {
    const content = fs.readFileSync(filePath, 'utf8');
    const frontmatterMatch = content.match(/^---\n(.*?)\n---/s);

    if (!frontmatterMatch) {
        console.error(`❌ ${filePath}: No frontmatter found`);
        return false;
    }

    let frontmatter;
    try {
        frontmatter = yaml.parse(frontmatterMatch[1]);
    } catch (e) {
        console.error(`❌ ${filePath}: Invalid YAML syntax`);
        return false;
    }

    // Check required fields
    for (const field of REQUIRED_FIELDS) {
        if (!frontmatter[field]) {
            console.error(`❌ ${filePath}: Missing required field '${field}'`);
            return false;
        }
    }

    // Validate type
    if (!VALID_TYPES.includes(frontmatter.type)) {
        console.error(`❌ ${filePath}: Invalid type '${frontmatter.type}'`);
        return false;
    }

    // Validate domain
    if (!VALID_DOMAINS.includes(frontmatter.domain)) {
        console.error(`❌ ${filePath}: Invalid domain '${frontmatter.domain}'`);
        return false;
    }

    // Validate status
    if (!VALID_STATUSES.includes(frontmatter.status)) {
        console.error(`❌ ${filePath}: Invalid status '${frontmatter.status}'`);
        return false;
    }

    // Validate audience is array
    if (!Array.isArray(frontmatter.audience)) {
        console.error(`❌ ${filePath}: 'audience' must be an array`);
        return false;
    }

    // Validate tags is array
    if (!Array.isArray(frontmatter.tags)) {
        console.error(`❌ ${filePath}: 'tags' must be an array`);
        return false;
    }

    console.log(`✅ ${filePath}: Valid`);
    return true;
}

// Get file path from command line
const filePath = process.argv[2];
if (!filePath) {
    console.error('Usage: node validate-frontmatter.js <file.md>');
    process.exit(1);
}

const isValid = validateFrontmatter(filePath);
process.exit(isValid ? 0 : 1);
```

---

## Migration: Ancien → Nouveau Format

### Avant (Format Inconsistant)

```markdown
# Booking Manager Agent

## Role
Manage bookings...

## Capabilities
- Booking.com
- Airbnb
```

### Après (Format Standardisé)

```markdown
---
id: vt-ops-booking-manager-1-0-0
title: "Booking Management Specialist Agent"
description: "Expert agent managing all booking operations across platforms"
type: agent
domain: operations
audience: ["agent", "human"]
version: "1.0.0"
created: 2026-01-16
last_updated: 2026-01-16
status: published
author: "@claude"
reviewer: "@omar"
tags: ["booking", "reservations", "multi-platform"]
category: operations
related: ["vt-ops-pricing-analyst-1-0-0"]

agent_id: booking-manager
agent_name: Booking Management Specialist
orchestration:
  type: specialist
  can_work_independently: true
capabilities: docs/agents/booking-manager/capabilities.json
context_mandatory:
  - docs/knowledge/mandatory/client-profile.md
context_domain:
  - docs/knowledge/domain/operations/booking-policies.md
dependencies:
  agents:
    - pricing-analyst
    - communication-manager
  tools:
    - booking_com_api
    - airbnb_api
testing:
  status: in_progress
  eval_suite: tests/agents/booking-manager/
  pass_rate:
    unit: 0.85
    integration: 0.70
---

# Booking Management Specialist Agent

## Role
Manage bookings...
```

---

## Ressources

- [YAML Specification](https://yaml.org/spec/)
- [Frontmatter on GitHub](https://docs.github.com/en/contributing/writing-for-github-docs/using-yaml-frontmatter)
- [Semantic Versioning](https://semver.org/)
- [ISO 8601 Date Format](https://www.iso.org/iso-8601-date-and-time-format.html)

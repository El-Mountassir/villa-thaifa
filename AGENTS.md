# AGENTS.md

> **Specification**: [AGENTS.md Standard](https://agents.md)
> **Identity**: Universal Agent Manifest.
> **Last Updated**: 2026-01-17

## 🤖 Manifest

- **Project**: Villa Thaifa - Digital Transformation
- **Owner**: Omar El Mountassir
- **Capabilities Required**: `fs_read`, `fs_write`, `cli_exec`.

## 🚨 PRIME DIRECTIVE (Governance)

> **RULE #1**: ALL WORK MUST BE REGISTERED IN `ROADMAP.md` FIRST.
> No agent shall execute a task that is not explicitly defined in the Project Roadmap.
> If a task is missing, **STOP**, update `ROADMAP.md`, and request user approval.

## 📌 References (The "Constitution")

| Concept             | Source                                                                                                               |
| :------------------ | :------------------------------------------------------------------------------------------------------------------- |
| **Stakeholders** ⭐ | [`docs/leadership/STAKEHOLDERS.md`](docs/leadership/STAKEHOLDERS.md) **READ FIRST**                                |
| **Team & Roles**    | [`docs/leadership/TEAM.md`](docs/leadership/TEAM.md)                                                                 |
| **Structure**       | [`docs/architecture/project_structure.md`](docs/architecture/project_structure.md)                                   |
| **Code of Conduct** | [`docs/project/standards/agents/code_of_conduct.md`](docs/project/standards/agents/code_of_conduct.md)               |
| **Collaboration**   | [`docs/project/standards/agents/collaboration_protocol.md`](docs/project/standards/agents/collaboration_protocol.md) |
| **🔴 Credentials**  | [`docs/operations/.env.rules.md`](docs/operations/.env.rules.md) **READ BEFORE MODIFYING .env**                     |

## 🚀 Active Context

- **Work**: [`tasks/active.md`](tasks/active.md)
- **Vision**: [`MISSION.md`](MISSION.md)

## 🚀 Active Plans & Status

- **Tasks**: `tasks/active.md` (The Kanban).
- **Architecture**: `docs/architecture/` (The Blueprints).
- **Rescue**: We are currently in "Phase 1: Stabilization & Cleanup".

## 🔧 Available Tools & Capabilities

### **Browser Automation** - `agent-browser`

**Status**: ✅ Installed & Operational (Jan 2026)

Agent-browser is a fast headless browser automation CLI available globally. Use it via Bash for web automation tasks.

**Installation**:
```bash
agent-browser --version  # Already installed globally
```

**Key Capabilities**:
- **Navigation**: Open URLs, click elements, fill forms, submit data
- **Extraction**: Snapshots with element refs (@e1, @e2...), get text/HTML/attributes
- **Actions**: Click, type, hover, drag-drop, upload files, scroll
- **Data Collection**: Screenshots (full-page), PDF export, JSON snapshots
- **Automation**: Search forms, login flows, data scraping
- **JavaScript**: Execute custom JS code on pages

**Quick Examples**:
```bash
# Navigate and extract interactive elements
agent-browser open https://example.com
agent-browser snapshot -i -c  # Interactive elements with refs

# Click by reference and capture
agent-browser click @e12
agent-browser screenshot --full output.png

# Form automation
agent-browser fill "input[name='search']" "query"
agent-browser press Enter

# Data extraction
agent-browser get text "h1"
agent-browser eval "document.title"
agent-browser pdf output.pdf

# Cleanup
agent-browser close
```

**Sessions & Profiles**:
- `--session <name>`: Isolated browser sessions
- `--profile <path>`: Persistent browser profiles (saved cookies, auth)

**Best Practices**:
- Always close the browser with `agent-browser close` when done
- Use snapshot refs (@eX) for reliable element targeting
- Combine multiple commands with `&&` for workflows
- Use `--json` flag for structured output parsing

**Documentation**: Run `agent-browser --help` for full command reference

### **HotelRunner Data Access** - Property Management System

**Status**: ✅ **Opérationnel via Browser Automation** - Jan 2026

Accès aux données de réservations, calendrier, et rapports de Villa Thaifa depuis HotelRunner.

**Méthode Active** : Browser Automation (agent-browser avec profile persistant)

**API Details**:
- **Base URL**: `https://am.hotelrunner.com/custom-apps/rest-api`
- **Authentication**: TOKEN + HR_ID (header-based)
- **Rate Limits**: 250 requests/day, 5 requests/minute
- **Integration Type**: HR-v1 (REST API with JSON)

**Key Capabilities**:
- **Rooms**: Get room list, manage inventory
- **Reservations**: Retrieve bookings, search by date/status
- **Calendar**: Update rates and availability for specific dates
- **Webhooks**: Real-time push notifications (confirmed, modified, cancelled)

**Credentials** (`.env.local`):
```bash
HOTELRUNNER_TOKEN=<pending>     # API authentication token
HOTELRUNNER_HR_ID=<pending>      # Hotel property ID
```

**Quick Example** (Python):
```python
import os
import requests

headers = {
    'Authorization': f'Bearer {os.getenv("HOTELRUNNER_TOKEN")}',
    'HR-ID': os.getenv('HOTELRUNNER_HR_ID')
}

# Get today's reservations
response = requests.get(
    'https://am.hotelrunner.com/custom-apps/rest-api/reservations',
    headers=headers
)
```

**App Configuration**:
- **Name**: Villa Thaifa AI Automation
- **Type**: PMS (Property Management System)
- **Created**: 2026-01-24
- **Permissions**: Full access (rooms, reservations, calendar, webhooks)

**Best Practices**:
- Cache room/rate data to minimize API calls
- Monitor daily/minute rate limits carefully
- Implement retry logic with exponential backoff
- Never log or commit credentials

**Documentation**:
- **Setup Progress**: [`sources/hotelrunner-api/SETUP.md`](sources/hotelrunner-api/SETUP.md) - **Check this for current status**
- **Usage Guide**: [`sources/hotelrunner-api/guide.md`](sources/hotelrunner-api/guide.md)
- **Quick Reference**: [`sources/hotelrunner-api/README.md`](sources/hotelrunner-api/README.md)
- **Official Docs**: https://developers.hotelrunner.com/custom-apps/rest-api

### **Browser Automation Method** (Active)

**Script**: [`sources/hotelrunner-api/extract_reservations.py`](sources/hotelrunner-api/extract_reservations.py)

**Quick Usage**:
```bash
cd sources/hotelrunner-api
python3 extract_reservations.py
```

**Output**: `data/reservations/latest.json` (96 réservations avec tous les détails)

**Données Disponibles**:
- Status, Canal, Nom client, Confirmation #
- Dates check-in/check-out
- Type chambre, Prix, Paiement
- Nationalité, Date réservation

**Avantages Confirmés** (Test POC 2026-01-24):
- ✅ Pas de rate limits (utilisation normale browser)
- ✅ Pas de callback URL requis
- ✅ Accès à toutes sections dashboard
- ✅ Extraction validée (96 réservations, 14 champs/réservation)

⚠️ **LIMITATION CRITIQUE DÉCOUVERTE** (Tests 2026-01-24 14:25):
- ❌ Le flag `--profile` d'agent-browser **NE PERSISTE PAS** les cookies de session
- ❌ Authentification manuelle requise à chaque extraction
- ❌ Script automatique (`extract_reservations.py`) bloqué sans intervention
- ⚠️ Automatisation complète en attente investigation/workaround

**Solution Actuelle** (Extraction Manuelle Fonctionnelle):
```bash
# 1. Ouvrir browser et s'authentifier
agent-browser --headed open https://villa-thaifa.hotelrunner.com/login
# (Login manuel - 2 min)

# 2. Extraire réservations (session active)
agent-browser open https://villa-thaifa.hotelrunner.com/admin/pms/reservations/all
agent-browser eval "document.querySelectorAll('table tbody tr').length"  # 96 confirmé

# 3. Sauvegarder et fermer
# ... extraction ...
agent-browser close
```

**Effort**: 5-10 minutes/jour pour extraction manuelle

**Guides Complets**:
- **[STATUS-FINAL.md](sources/hotelrunner-api/STATUS-FINAL.md)** - ⭐ Statut complet, limitation, recommandations
- [EXTRACTION-GUIDE.md](sources/hotelrunner-api/EXTRACTION-GUIDE.md) - Guide avec workarounds
- [TEST-RESULTS.md](sources/hotelrunner-api/TEST-RESULTS.md) - Tests détaillés + 4 solutions contournement

### **REST API Method** (Alternative disponible)

**Status**: ⏸️ En pause - Browser automation suffit pour l'instant

Si besoin de webhooks temps réel à l'avenir :
- **Base URL**: `https://am.hotelrunner.com/custom-apps/rest-api`
- **Rate Limits**: 250 requests/day, 5 requests/minute
- **Setup**: Créer Custom App, obtenir TOKEN + HR_ID
- **Blocage**: Callback URL HTTPS requis

**Current Progress** (as of 2026-01-24 14:12):
- ✅ Options analysis completed (6 options evaluated)
- ✅ **Browser automation POC successful** - 96 reservations extracted
- ✅ Production script created (`extract_reservations.py`)
- ✅ Screenshots captured (dashboard, reservations, calendar)
- ✅ Documentation complete (test results, extraction guide, options analysis)
- ⏸️ API setup paused - Not needed for current use case

**Recommendation**: Use browser automation for immediate value. Consider API later only if real-time webhooks become critical.

**Full Analysis**: [`sources/hotelrunner-api/OPTIONS-ANALYSIS.md`](sources/hotelrunner-api/OPTIONS-ANALYSIS.md)

---

_*Created during the "AI-First" Refactor - Jan 2026*_

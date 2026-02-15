.
├── AGENTS.md
├── CHANGELOG.md
├── CLAUDE.md
├── config
│   ├── agents
│   │   ├── browser.json
│   │   └── hotelrunner-api.json
│   ├── labels.json
│   └── planning.json
├── data
│   ├── core
│   │   └── property
│   │       └── inventory
│   │           ├── backups
│   │           │   └── rooms
│   │           │       └── archive
│   │           │           ├── rooms.md.backup-2026-02-13
│   │           │           ├── rooms.md.backup-2026-02-13-access-col
│   │           │           ├── rooms.md.backup-2026-02-13-booking-col
│   │           │           ├── rooms.md.backup-2026-02-13-meta-cols
│   │           │           ├── rooms.md.backup-2026-02-13-plan-exec
│   │           │           ├── rooms.md.backup-2026-02-13-rooms2-consolidation
│   │           │           ├── rooms.md.backup-2026-02-13-size-sync
│   │           │           ├── rooms.md.backup-2026-02-13-smoking-kitchen
│   │           │           ├── rooms.md.backup-2026-02-13-step0
│   │           │           ├── rooms-reconciliation-log.md.backup-2026-02-13-access-col
│   │           │           ├── rooms-reconciliation-log.md.backup-2026-02-13-booking-col
│   │           │           ├── rooms-reconciliation-log.md.backup-2026-02-13-meta-cols
│   │           │           ├── rooms-reconciliation-log.md.backup-2026-02-13-plan-exec
│   │           │           ├── rooms-reconciliation-log.md.backup-2026-02-13-rooms2-consolidation
│   │           │           ├── rooms-reconciliation-log.md.backup-2026-02-13-size-sync
│   │           │           └── rooms-reconciliation-log.md.backup-2026-02-13-smoking-kitchen
│   │           ├── pending
│   │           │   ├── amenities.md
│   │           │   ├── beds.md
│   │           │   ├── facilities.md
│   │           │   ├── inventory.md
│   │           │   ├── property-db-migration.md
│   │           │   └── property-db-migration.yaml
│   │           ├── rooms
│   │           │   ├── backup
│   │           │   │   └── rooms-backup-2026-02-13-pre-profile-schema.md
│   │           │   ├── exports
│   │           │   │   ├── booking-room-listings.csv
│   │           │   │   └── expedia-room-listings.csv
│   │           │   ├── rooms.md
│   │           │   └── rooms-reconciliation-log.md
│   │           ├── status
│   │           │   ├── archived.md
│   │           │   ├── backups.md
│   │           │   ├── canonical.md
│   │           │   └── pending.md
│   │           └── STATUS.md
│   ├── pending
│   │   └── finance
│   │       ├── billing.json
│   │       └── rates.json
│   └── README.md
├── docs
│   ├── agents
│   │   ├── AI-SESSION-STARTER.md
│   │   ├── browser
│   │   │   ├── EXAMPLES.md
│   │   │   ├── guide.md
│   │   │   └── README.md
│   │   ├── HANDOFF.md
│   │   ├── instructions
│   │   │   ├── AGENTS.md
│   │   │   ├── CLAUDE.md
│   │   │   └── GEMINI.md
│   │   ├── shared
│   │   │   └── managers
│   │   │       └── channels
│   │   │           ├── booking
│   │   │           │   └── capabilities.json
│   │   │           └── hotelrunner
│   │   │               ├── DECISION-BRIEF.md
│   │   │               ├── EXTRACTION-GUIDE.md
│   │   │               ├── guide.md
│   │   │               ├── logs
│   │   │               │   └── extract_20260124.log
│   │   │               ├── OPTIONS-ANALYSIS.md
│   │   │               ├── README.md
│   │   │               ├── SETUP.md
│   │   │               ├── STATUS-FINAL.md
│   │   │               └── TEST-RESULTS.md
│   │   ├── standards
│   │   │   ├── 2026-01-09-10-44-55-villa-thaifa-najib-insights-brief-strategy.txt
│   │   │   ├── claude-code-hotelrunner-investigation-prompt.md
│   │   │   ├── gemini-lux-action-plan.md
│   │   │   ├── gemini-onboarding-prompt.md
│   │   │   ├── gemini-system-prompt.md
│   │   │   ├── google-ai-studio-quick-guide.md
│   │   │   ├── lhcm-os-strategy-execution-plan-v0.1.0.md
│   │   │   ├── najib-conversation-part1-analysis-v0.1.0.md
│   │   │   ├── najib-mountassir-context-v0.1.0.md
│   │   │   ├── tech-stack-omar-v0.1.3-lux-annotated.md
│   │   │   ├── villa-thaifa-artifacts-inventory-v0.1.0.md
│   │   │   ├── villa-thaifa-client-brief-v0.1.0.md
│   │   │   ├── villa-thaifa-client-brief-v0.2.0.md
│   │   │   ├── villa-thaifa-decisions-log-v0.1.0.md
│   │   │   ├── villa-thaifa-execution-plan-2025-01-09-night.md
│   │   │   ├── villa-thaifa-internal-app-requirements-v0.1.0.md
│   │   │   ├── villa-thaifa-migration-plan-v0.1.0.md
│   │   │   ├── villa-thaifa-migration-progress-report-v0.1.0.md
│   │   │   ├── villa-thaifa-mission-lundi-12h00.md
│   │   │   ├── villa-thaifa-open-questions-v0.1.0.md
│   │   │   ├── villa-thaifa-project-brief-v0.2.0.md
│   │   │   ├── villa-thaifa-quick-start-v0.1.0.md
│   │   │   ├── villa-thaifa-repo-exploration-v0.1.0.md
│   │   │   ├── villa-thaifa-research-findings-v0.1.0.md
│   │   │   ├── villa-thaifa-technical-context-v0.1.0.md
│   │   │   └── villa-thaifa-workstream-master-v0.1.0.md
│   │   ├── templates
│   │   │   └── handovers
│   │   │       └── template.md
│   │   └── workflows
│   │       └── hotelrunner
│   │           └── README.md
│   ├── backups
│   │   └── project
│   │       ├── management
│   │       │   └── planning
│   │       │       ├── 2026-02-13-agentic-kiss-transformation-plan.md.backup-2026-02-13-jinja2
│   │       │       ├── 2026-02-13-agentic-kiss-transformation-plan.md.backup-2026-02-13-uv
│   │       │       ├── 2026-02-13-agentic-operating-playbook.md.backup-2026-02-13-jinja2
│   │       │       ├── 2026-02-13-agentic-operating-playbook.md.backup-2026-02-13-uv
│   │       │       ├── 2026-02-13-next-7-days.md.backup-2026-02-13-jinja2
│   │       │       └── 2026-02-13-next-7-days.md.backup-2026-02-13-uv
│   │       └── templates
│   │           └── README.md.backup-2026-02-13-jinja2
│   ├── client
│   │   ├── admin
│   │   │   └── CONTACT.md
│   │   ├── client-profile.md
│   │   ├── COMMUNICATION.md
│   │   ├── CONTACT.md
│   │   ├── DECISIONS.md
│   │   ├── email-intel-2026-02-09.md
│   │   ├── HISTORY.md
│   │   ├── OMAR.md
│   │   ├── PREFERENCES.md
│   │   ├── PRIORITIES.md
│   │   ├── PROFILE.json
│   │   ├── PROFILE.md
│   │   ├── profiles
│   │   │   ├── OMAR-EL-MOUNTASSIR.md
│   │   │   └── SAID-THAIFA.md
│   │   ├── README.md
│   │   ├── STAKEHOLDERS.md
│   │   ├── support
│   │   │   └── README.md
│   │   ├── TEAM.md
│   │   └── VISION.md
│   ├── content
│   │   ├── pending
│   │   │   └── reference
│   │   │       ├── facilities
│   │   │       │   ├── hall
│   │   │       │   │   ├── hall.md
│   │   │       │   │   └── images
│   │   │       │   │       ├── _DSC1586-HDR.jpg
│   │   │       │   │       ├── _DSC1589-HDR.jpg
│   │   │       │   │       ├── _DSC1592-HDR.jpg
│   │   │       │   │       ├── _DSC1598-HDR.jpg
│   │   │       │   │       ├── _DSC1613-HDR-Pano.jpg
│   │   │       │   │       ├── _DSC1622-HDR.jpg
│   │   │       │   │       ├── _DSC1628-HDR.jpg
│   │   │       │   │       ├── _DSC7410-HDR.jpg
│   │   │       │   │       ├── _DSC7413-HDR.jpg
│   │   │       │   │       ├── _DSC7416-HDR.jpg
│   │   │       │   │       ├── _DSC7419-HDR.jpg
│   │   │       │   │       ├── _DSC7422-HDR.jpg
│   │   │       │   │       ├── _DSC7425-HDR.jpg
│   │   │       │   │       ├── _DSC7428-HDR.jpg
│   │   │       │   │       ├── _DSC7434-HDR.jpg
│   │   │       │   │       ├── _DSC7567-HDR.jpg
│   │   │       │   │       ├── _DSC7570-HDR.jpg
│   │   │       │   │       └── _DSC7573-HDR.jpg
│   │   │       │   ├── pool-garden
│   │   │       │   │   ├── garden.md
│   │   │       │   │   ├── images
│   │   │       │   │   │   ├── _DSC1634-HDR-Modifier.jpg
│   │   │       │   │   │   ├── _DSC1640-HDR-Modifier.jpg
│   │   │       │   │   │   ├── _DSC1643-HDR-Modifier.jpg
│   │   │       │   │   │   ├── _DSC1652-HDR-Modifier.jpg
│   │   │       │   │   │   ├── _DSC1655-HDR-Modifier.jpg
│   │   │       │   │   │   ├── _DSC1661-HDR.jpg
│   │   │       │   │   │   ├── _DSC1916-HDR.jpg
│   │   │       │   │   │   ├── _DSC1931-HDR-Modifier.jpg
│   │   │       │   │   │   ├── _DSC7516-HDR.jpg
│   │   │       │   │   │   ├── _DSC7519-HDR.jpg
│   │   │       │   │   │   ├── _DSC7522-HDR.jpg
│   │   │       │   │   │   ├── _DSC7525-HDR.jpg
│   │   │       │   │   │   ├── _DSC7528-HDR.jpg
│   │   │       │   │   │   ├── _DSC7531-HDR.jpg
│   │   │       │   │   │   ├── _DSC7534-HDR.jpg
│   │   │       │   │   │   ├── _DSC7537-HDR.jpg
│   │   │       │   │   │   ├── _DSC7543-HDR.jpg
│   │   │       │   │   │   ├── _DSC7546-HDR.jpg
│   │   │       │   │   │   ├── _DSC7549-HDR.jpg
│   │   │       │   │   │   ├── _DSC7552-HDR.jpg
│   │   │       │   │   │   ├── _DSC7555-HDR.jpg
│   │   │       │   │   │   ├── _DSC7558-HDR.jpg
│   │   │       │   │   │   ├── _DSC7564-HDR.jpg
│   │   │       │   │   │   ├── _DSC7579-HDR.jpg
│   │   │       │   │   │   └── _DSC7582-HDR.jpg
│   │   │       │   │   └── pool.md
│   │   │       │   └── spa-hammam
│   │   │       │       ├── images
│   │   │       │       │   ├── _DSC1685-HDR.jpg
│   │   │       │       │   ├── _DSC1688-HDR.jpg
│   │   │       │       │   ├── _DSC1694-HDR.jpg
│   │   │       │       │   ├── _DSC1702-HDR.jpg
│   │   │       │       │   ├── _DSC1719-HDR.jpg
│   │   │       │       │   ├── _DSC1721-HDR.jpg
│   │   │       │       │   ├── _DSC1724-HDR.jpg
│   │   │       │       │   ├── _DSC1727-HDR.jpg
│   │   │       │       │   ├── _DSC1736-HDR-Modifier.jpg
│   │   │       │       │   └── _DSC1739-HDR.jpg
│   │   │       │       └── spa.md
│   │   │       ├── IMG_20260126_0001.pdf
│   │   │       ├── rooms
│   │   │       │   ├── 01
│   │   │       │   │   ├── 01-deluxe-triple.md
│   │   │       │   │   ├── images
│   │   │       │   │   │   ├── _DSC7200-HDR.jpg
│   │   │       │   │   │   ├── _DSC7203-HDR.jpg
│   │   │       │   │   │   ├── _DSC7206-HDR.jpg
│   │   │       │   │   │   ├── _DSC7209-HDR.jpg
│   │   │       │   │   │   ├── _DSC7212-HDR.jpg
│   │   │       │   │   │   ├── _DSC7215-HDR.jpg
│   │   │       │   │   │   ├── _DSC7218-HDR.jpg
│   │   │       │   │   │   ├── _DSC7221-HDR.jpg
│   │   │       │   │   │   ├── _DSC7224-HDR.jpg
│   │   │       │   │   │   ├── main.jpg
│   │   │       │   │   │   ├── photo-01.jpg
│   │   │       │   │   │   ├── photo-02.jpg
│   │   │       │   │   │   ├── photo-03.jpg
│   │   │       │   │   │   ├── photo-04.jpg
│   │   │       │   │   │   ├── photo-05.jpg
│   │   │       │   │   │   ├── photo-06.jpg
│   │   │       │   │   │   ├── photo-07.jpg
│   │   │       │   │   │   ├── photo-08.jpg
│   │   │       │   │   │   ├── WhatsApp Image 2025-12-29 at 17.53.11 (1).jpeg
│   │   │       │   │   │   ├── WhatsApp Image 2025-12-29 at 17.53.11 (2).jpeg
│   │   │       │   │   │   ├── WhatsApp Image 2025-12-29 at 17.53.11 (3).jpeg
│   │   │       │   │   │   ├── WhatsApp Image 2025-12-29 at 17.53.11.jpeg
│   │   │       │   │   │   ├── WhatsApp Image 2025-12-29 at 17.53.12 (1).jpeg
│   │   │       │   │   │   ├── WhatsApp Image 2025-12-29 at 17.53.12 (2).jpeg
│   │   │       │   │   │   ├── WhatsApp Image 2025-12-29 at 17.53.12 (3).jpeg
│   │   │       │   │   │   └── WhatsApp Image 2025-12-29 at 17.53.12.jpeg
│   │   │       │   │   └── R01_Deluxe_Triple.md
│   │   │       │   ├── 02
│   │   │       │   │   ├── 02-deluxe-double.md
│   │   │       │   │   ├── images
│   │   │       │   │   │   ├── _DSC7231-HDR.jpg
│   │   │       │   │   │   ├── _DSC7239-HDR.jpg
│   │   │       │   │   │   ├── _DSC7242-HDR.jpg
│   │   │       │   │   │   ├── _DSC7243-HDR.jpg
│   │   │       │   │   │   ├── _DSC7246-HDR.jpg
│   │   │       │   │   │   ├── _DSC7249-HDR.jpg
│   │   │       │   │   │   ├── _DSC7252-HDR.jpg
│   │   │       │   │   │   ├── _DSC7258-HDR.jpg
│   │   │       │   │   │   ├── _DSC7261-HDR.jpg
│   │   │       │   │   │   ├── main.jpg
│   │   │       │   │   │   ├── photo-01.jpg
│   │   │       │   │   │   ├── photo-02.jpg
│   │   │       │   │   │   ├── photo-03.jpg
│   │   │       │   │   │   ├── photo-04.jpg
│   │   │       │   │   │   ├── photo-05.jpg
│   │   │       │   │   │   ├── photo-06.jpg
│   │   │       │   │   │   ├── photo-07.jpg
│   │   │       │   │   │   ├── photo-08.jpg
│   │   │       │   │   │   ├── WhatsApp Image 2025-12-29 at 17.59.21 (1).jpeg
│   │   │       │   │   │   ├── WhatsApp Image 2025-12-29 at 17.59.21 (2).jpeg
│   │   │       │   │   │   ├── WhatsApp Image 2025-12-29 at 17.59.21 (3).jpeg
│   │   │       │   │   │   ├── WhatsApp Image 2025-12-29 at 17.59.21.jpeg
│   │   │       │   │   │   ├── WhatsApp Image 2025-12-29 at 17.59.22 (1).jpeg
│   │   │       │   │   │   ├── WhatsApp Image 2025-12-29 at 17.59.22 (2).jpeg
│   │   │       │   │   │   └── WhatsApp Image 2025-12-29 at 17.59.22.jpeg
│   │   │       │   │   └── R02_Deluxe_Double.md
│   │   │       │   ├── 03
│   │   │       │   │   ├── 03-deluxe-triple.md
│   │   │       │   │   ├── images
│   │   │       │   │   │   ├── _DSC7264-HDR.jpg
│   │   │       │   │   │   ├── _DSC7267-HDR.jpg
│   │   │       │   │   │   ├── _DSC7270-HDR.jpg
│   │   │       │   │   │   ├── _DSC7276-HDR.jpg
│   │   │       │   │   │   ├── _DSC7279-HDR.jpg
│   │   │       │   │   │   ├── _DSC7282-HDR.jpg
│   │   │       │   │   │   ├── _DSC7285-HDR.jpg
│   │   │       │   │   │   ├── _DSC7291-HDR.jpg
│   │   │       │   │   │   ├── main.jpg
│   │   │       │   │   │   ├── photo-01.jpg
│   │   │       │   │   │   ├── photo-02.jpg
│   │   │       │   │   │   ├── photo-03.jpg
│   │   │       │   │   │   ├── photo-04.jpg
│   │   │       │   │   │   ├── photo-05.jpg
│   │   │       │   │   │   ├── photo-06.jpg
│   │   │       │   │   │   ├── photo-07.jpg
│   │   │       │   │   │   ├── WhatsApp Image 2025-12-29 at 18.00.48 (1).jpeg
│   │   │       │   │   │   ├── WhatsApp Image 2025-12-29 at 18.00.48 (2).jpeg
│   │   │       │   │   │   ├── WhatsApp Image 2025-12-29 at 18.00.48.jpeg
│   │   │       │   │   │   ├── WhatsApp Image 2025-12-29 at 18.13.15.jpeg
│   │   │       │   │   │   ├── WhatsApp Image 2025-12-29 at 18.13.16 (1).jpeg
│   │   │       │   │   │   ├── WhatsApp Image 2025-12-29 at 18.13.16 (2).jpeg
│   │   │       │   │   │   ├── WhatsApp Image 2025-12-29 at 18.13.16 (3).jpeg
│   │   │       │   │   │   ├── WhatsApp Image 2025-12-29 at 18.13.16.jpeg
│   │   │       │   │   │   ├── WhatsApp Image 2025-12-29 at 18.13.17 (1).jpeg
│   │   │       │   │   │   ├── WhatsApp Image 2025-12-29 at 18.13.17 (2).jpeg
│   │   │       │   │   │   └── WhatsApp Image 2025-12-29 at 18.13.17.jpeg
│   │   │       │   │   └── R03_Deluxe_Triple.md
│   │   │       │   ├── 04
│   │   │       │   │   ├── 04-double-superior.md
│   │   │       │   │   ├── images
│   │   │       │   │   │   ├── _DSC7296-HDR.jpg
│   │   │       │   │   │   ├── _DSC7297-HDR.jpg
│   │   │       │   │   │   ├── _DSC7300-HDR.jpg
│   │   │       │   │   │   ├── _DSC7303-HDR.jpg
│   │   │       │   │   │   ├── _DSC7306-HDR.jpg
│   │   │       │   │   │   ├── _DSC7310-HDR.jpg
│   │   │       │   │   │   ├── _DSC7313-HDR.jpg
│   │   │       │   │   │   ├── _DSC7316-HDR.jpg
│   │   │       │   │   │   ├── _DSC7319-HDR.jpg
│   │   │       │   │   │   ├── main.jpg
│   │   │       │   │   │   ├── photo-01.jpg
│   │   │       │   │   │   ├── photo-02.jpg
│   │   │       │   │   │   ├── photo-03.jpg
│   │   │       │   │   │   ├── photo-04.jpg
│   │   │       │   │   │   ├── photo-05.jpg
│   │   │       │   │   │   ├── photo-06.jpg
│   │   │       │   │   │   ├── photo-07.jpg
│   │   │       │   │   │   ├── photo-08.jpg
│   │   │       │   │   │   ├── WhatsApp Image 2025-12-29 at 18.17.29 (1).jpeg
│   │   │       │   │   │   ├── WhatsApp Image 2025-12-29 at 18.17.29.jpeg
│   │   │       │   │   │   ├── WhatsApp Image 2025-12-29 at 18.17.30 (1).jpeg
│   │   │       │   │   │   ├── WhatsApp Image 2025-12-29 at 18.17.30 (2).jpeg
│   │   │       │   │   │   └── WhatsApp Image 2025-12-29 at 18.17.30.jpeg
│   │   │       │   │   └── R04_Double_Superior.md
│   │   │       │   ├── 05
│   │   │       │   │   ├── 05-double-superior.md
│   │   │       │   │   ├── images
│   │   │       │   │   │   ├── _DSC7296-HDR.jpg
│   │   │       │   │   │   ├── _DSC7297-HDR.jpg
│   │   │       │   │   │   ├── _DSC7300-HDR.jpg
│   │   │       │   │   │   ├── _DSC7303-HDR.jpg
│   │   │       │   │   │   ├── _DSC7306-HDR.jpg
│   │   │       │   │   │   ├── _DSC7310-HDR.jpg
│   │   │       │   │   │   ├── _DSC7313-HDR.jpg
│   │   │       │   │   │   ├── _DSC7316-HDR.jpg
│   │   │       │   │   │   ├── _DSC7319-HDR.jpg
│   │   │       │   │   │   ├── _DSC7325-HDR.jpg
│   │   │       │   │   │   ├── _DSC7328-HDR.jpg
│   │   │       │   │   │   ├── _DSC7334-HDR.jpg
│   │   │       │   │   │   ├── _DSC7343-HDR.jpg
│   │   │       │   │   │   ├── _DSC7347-HDR.jpg
│   │   │       │   │   │   ├── _DSC7350-HDR.jpg
│   │   │       │   │   │   ├── _DSC7353-HDR.jpg
│   │   │       │   │   │   ├── _DSC7356-HDR.jpg
│   │   │       │   │   │   ├── _DSC7359-HDR.jpg
│   │   │       │   │   │   ├── main.jpg
│   │   │       │   │   │   ├── photo-01.jpg
│   │   │       │   │   │   ├── photo-02.jpg
│   │   │       │   │   │   ├── photo-03.jpg
│   │   │       │   │   │   ├── photo-04.jpg
│   │   │       │   │   │   ├── photo-05.jpg
│   │   │       │   │   │   ├── photo-06.jpg
│   │   │       │   │   │   ├── photo-07.jpg
│   │   │       │   │   │   ├── photo-08.jpg
│   │   │       │   │   │   ├── photo-09.jpg
│   │   │       │   │   │   ├── photo-10.jpg
│   │   │       │   │   │   ├── photo-11.jpg
│   │   │       │   │   │   ├── photo-12.jpg
│   │   │       │   │   │   ├── photo-13.jpg
│   │   │       │   │   │   ├── photo-14.jpg
│   │   │       │   │   │   ├── photo-15.jpg
│   │   │       │   │   │   ├── photo-16.jpg
│   │   │       │   │   │   ├── photo-17.jpg
│   │   │       │   │   │   ├── WhatsApp Image 2025-12-29 at 18.19.21 (1).jpeg
│   │   │       │   │   │   ├── WhatsApp Image 2025-12-29 at 18.19.21 (2).jpeg
│   │   │       │   │   │   ├── WhatsApp Image 2025-12-29 at 18.19.21 (3).jpeg
│   │   │       │   │   │   ├── WhatsApp Image 2025-12-29 at 18.19.21.jpeg
│   │   │       │   │   │   └── WhatsApp Image 2025-12-29 at 18.19.22.jpeg
│   │   │       │   │   └── R05_Double_Superior.md
│   │   │       │   ├── 06
│   │   │       │   │   ├── 06-executive-suite.md
│   │   │       │   │   ├── images
│   │   │       │   │   │   ├── _DSC7296-HDR.jpg
│   │   │       │   │   │   ├── _DSC7297-HDR.jpg
│   │   │       │   │   │   ├── _DSC7300-HDR.jpg
│   │   │       │   │   │   ├── _DSC7303-HDR.jpg
│   │   │       │   │   │   ├── _DSC7306-HDR.jpg
│   │   │       │   │   │   ├── _DSC7310-HDR.jpg
│   │   │       │   │   │   ├── _DSC7313-HDR.jpg
│   │   │       │   │   │   ├── _DSC7316-HDR.jpg
│   │   │       │   │   │   ├── _DSC7319-HDR.jpg
│   │   │       │   │   │   ├── _DSC7365-HDR.jpg
│   │   │       │   │   │   ├── _DSC7374-HDR.jpg
│   │   │       │   │   │   ├── _DSC7377-HDR.jpg
│   │   │       │   │   │   ├── _DSC7380-HDR.jpg
│   │   │       │   │   │   ├── _DSC7383-HDR.jpg
│   │   │       │   │   │   ├── _DSC7386-HDR.jpg
│   │   │       │   │   │   ├── _DSC7389-HDR.jpg
│   │   │       │   │   │   ├── _DSC7392-HDR.jpg
│   │   │       │   │   │   ├── _DSC7398-HDR.jpg
│   │   │       │   │   │   ├── _DSC7401-HDR.jpg
│   │   │       │   │   │   ├── _DSC7404-HDR.jpg
│   │   │       │   │   │   ├── _DSC7407-HDR.jpg
│   │   │       │   │   │   ├── main.jpg
│   │   │       │   │   │   ├── photo-01.jpg
│   │   │       │   │   │   ├── photo-02.jpg
│   │   │       │   │   │   ├── photo-03.jpg
│   │   │       │   │   │   ├── photo-04.jpg
│   │   │       │   │   │   ├── photo-05.jpg
│   │   │       │   │   │   ├── photo-06.jpg
│   │   │       │   │   │   ├── photo-07.jpg
│   │   │       │   │   │   ├── photo-08.jpg
│   │   │       │   │   │   ├── photo-09.jpg
│   │   │       │   │   │   ├── photo-10.jpg
│   │   │       │   │   │   ├── WhatsApp Image 2025-12-29 at 18.22.09 (1).jpeg
│   │   │       │   │   │   ├── WhatsApp Image 2025-12-29 at 18.22.09 (2).jpeg
│   │   │       │   │   │   ├── WhatsApp Image 2025-12-29 at 18.22.09 (3).jpeg
│   │   │       │   │   │   ├── WhatsApp Image 2025-12-29 at 18.22.09.jpeg
│   │   │       │   │   │   └── WhatsApp Image 2025-12-29 at 18.22.10.jpeg
│   │   │       │   │   └── R06_Executive_Suite.md
│   │   │       │   ├── 07
│   │   │       │   │   ├── 07-deluxe-king-suite.md
│   │   │       │   │   ├── images
│   │   │       │   │   │   ├── _DSC7296-HDR.jpg
│   │   │       │   │   │   ├── _DSC7297-HDR.jpg
│   │   │       │   │   │   ├── _DSC7300-HDR.jpg
│   │   │       │   │   │   ├── _DSC7303-HDR.jpg
│   │   │       │   │   │   ├── _DSC7306-HDR.jpg
│   │   │       │   │   │   ├── _DSC7310-HDR.jpg
│   │   │       │   │   │   ├── _DSC7313-HDR.jpg
│   │   │       │   │   │   ├── _DSC7316-HDR.jpg
│   │   │       │   │   │   ├── _DSC7319-HDR.jpg
│   │   │       │   │   │   ├── _DSC7437-HDR-Modifier.jpg
│   │   │       │   │   │   ├── _DSC7440-HDR.jpg
│   │   │       │   │   │   ├── _DSC7443-HDR.jpg
│   │   │       │   │   │   ├── _DSC7446-HDR-Modifier.jpg
│   │   │       │   │   │   ├── _DSC7449-HDR.jpg
│   │   │       │   │   │   ├── _DSC7452-HDR.jpg
│   │   │       │   │   │   ├── _DSC7455-HDR.jpg
│   │   │       │   │   │   ├── _DSC7459-HDR.jpg
│   │   │       │   │   │   ├── _DSC7468-HDR.jpg
│   │   │       │   │   │   ├── _DSC7471-HDR.jpg
│   │   │       │   │   │   ├── _DSC7474-HDR.jpg
│   │   │       │   │   │   ├── _DSC7480-HDR.jpg
│   │   │       │   │   │   ├── _DSC7483-HDR.jpg
│   │   │       │   │   │   ├── _DSC7486-HDR.jpg
│   │   │       │   │   │   ├── _DSC7489-HDR.jpg
│   │   │       │   │   │   ├── main.jpg
│   │   │       │   │   │   ├── photo-01.jpg
│   │   │       │   │   │   ├── photo-02.jpg
│   │   │       │   │   │   ├── photo-03.jpg
│   │   │       │   │   │   ├── photo-04.jpg
│   │   │       │   │   │   ├── photo-05.jpg
│   │   │       │   │   │   ├── photo-06.jpg
│   │   │       │   │   │   ├── photo-07.jpg
│   │   │       │   │   │   ├── photo-08.jpg
│   │   │       │   │   │   ├── photo-09.jpg
│   │   │       │   │   │   ├── photo-10.jpg
│   │   │       │   │   │   ├── WhatsApp Image 2025-12-29 at 18.25.30 (1).jpeg
│   │   │       │   │   │   ├── WhatsApp Image 2025-12-29 at 18.25.30.jpeg
│   │   │       │   │   │   ├── WhatsApp Image 2025-12-29 at 18.25.31 (1).jpeg
│   │   │       │   │   │   ├── WhatsApp Image 2025-12-29 at 18.25.31 (2).jpeg
│   │   │       │   │   │   ├── WhatsApp Image 2025-12-29 at 18.25.31 (3).jpeg
│   │   │       │   │   │   └── WhatsApp Image 2025-12-29 at 18.25.31.jpeg
│   │   │       │   │   └── R07_Deluxe_King_Suite.md
│   │   │       │   ├── 08
│   │   │       │   │   ├── 08-deluxe-triple.md
│   │   │       │   │   ├── images
│   │   │       │   │   │   ├── _DSC7296-HDR.jpg
│   │   │       │   │   │   ├── _DSC7297-HDR.jpg
│   │   │       │   │   │   ├── _DSC7300-HDR.jpg
│   │   │       │   │   │   ├── _DSC7303-HDR.jpg
│   │   │       │   │   │   ├── _DSC7306-HDR.jpg
│   │   │       │   │   │   ├── _DSC7310-HDR.jpg
│   │   │       │   │   │   ├── _DSC7313-HDR.jpg
│   │   │       │   │   │   ├── _DSC7316-HDR.jpg
│   │   │       │   │   │   ├── _DSC7319-HDR.jpg
│   │   │       │   │   │   ├── _DSC7492-HDR.jpg
│   │   │       │   │   │   ├── _DSC7495-HDR.jpg
│   │   │       │   │   │   ├── _DSC7498-HDR.jpg
│   │   │       │   │   │   ├── _DSC7501-HDR.jpg
│   │   │       │   │   │   ├── _DSC7507-HDR.jpg
│   │   │       │   │   │   ├── _DSC7510-HDR.jpg
│   │   │       │   │   │   ├── _DSC7513-HDR.jpg
│   │   │       │   │   │   ├── main.jpg
│   │   │       │   │   │   ├── photo-01.jpg
│   │   │       │   │   │   ├── photo-02.jpg
│   │   │       │   │   │   ├── photo-03.jpg
│   │   │       │   │   │   ├── photo-04.jpg
│   │   │       │   │   │   ├── photo-05.jpg
│   │   │       │   │   │   ├── photo-06.jpg
│   │   │       │   │   │   ├── WhatsApp Image 2025-12-29 at 18.26.56 (1).jpeg
│   │   │       │   │   │   ├── WhatsApp Image 2025-12-29 at 18.26.56 (2).jpeg
│   │   │       │   │   │   └── WhatsApp Image 2025-12-29 at 18.26.56.jpeg
│   │   │       │   │   └── R08_Deluxe_Triple.md
│   │   │       │   ├── 09
│   │   │       │   │   ├── 09-family-suite.md
│   │   │       │   │   ├── images
│   │   │       │   │   │   ├── 16c97eec-db21-4e5e-be2d-2b05ac313f03.jpeg
│   │   │       │   │   │   ├── 22b6495c-4dc3-460f-8d4a-e7f1fb232d07.jpeg
│   │   │       │   │   │   ├── 2839f125-782d-4bc3-8be6-e49137b62603.jpeg
│   │   │       │   │   │   ├── 353c9e76-ce9d-4d6f-8c85-8ad0f68ef0b6.jpeg
│   │   │       │   │   │   ├── 3d45401f-d841-4b81-b790-58d57975fed2.jpeg
│   │   │       │   │   │   ├── 683872b2-5c03-406f-b55d-2d82c355fc6e.jpeg
│   │   │       │   │   │   ├── 69cff1e5-ceb3-4e74-af1d-3371fe3f0611.jpeg
│   │   │       │   │   │   ├── 6ec253c5-0d88-4307-9f98-a15b20c3e635.jpeg
│   │   │       │   │   │   ├── 9cc5df3b-fb13-48ee-893e-5b5cfb910e2d.jpeg
│   │   │       │   │   │   ├── a7fe10cb-124d-4f1d-98a4-3f06ba888084.jpeg
│   │   │       │   │   │   ├── _DSC1745-HDR.jpg
│   │   │       │   │   │   ├── _DSC1754-HDR.jpg
│   │   │       │   │   │   ├── _DSC1757-HDR.jpg
│   │   │       │   │   │   ├── _DSC1760-HDR.jpg
│   │   │       │   │   │   ├── _DSC1763-HDR.jpg
│   │   │       │   │   │   ├── _DSC1769-HDR.jpg
│   │   │       │   │   │   ├── _DSC1775-HDR.jpg
│   │   │       │   │   │   ├── _DSC1781-HDR.jpg
│   │   │       │   │   │   ├── _DSC1788-HDR.jpg
│   │   │       │   │   │   ├── _DSC7296-HDR.jpg
│   │   │       │   │   │   ├── _DSC7297-HDR.jpg
│   │   │       │   │   │   ├── _DSC7300-HDR.jpg
│   │   │       │   │   │   ├── _DSC7303-HDR.jpg
│   │   │       │   │   │   ├── _DSC7306-HDR.jpg
│   │   │       │   │   │   ├── _DSC7310-HDR.jpg
│   │   │       │   │   │   ├── _DSC7313-HDR.jpg
│   │   │       │   │   │   ├── _DSC7316-HDR.jpg
│   │   │       │   │   │   ├── _DSC7319-HDR.jpg
│   │   │       │   │   │   ├── main.jpg
│   │   │       │   │   │   ├── photo-07.jpg
│   │   │       │   │   │   ├── photo-14.jpg
│   │   │       │   │   │   ├── photo-15.jpg
│   │   │       │   │   │   ├── photo-16.jpg
│   │   │       │   │   │   ├── photo-17.jpg
│   │   │       │   │   │   ├── photo-23.jpg
│   │   │       │   │   │   ├── photo-24.jpg
│   │   │       │   │   │   ├── photo-30.jpg
│   │   │       │   │   │   ├── photo-31.jpg
│   │   │       │   │   │   ├── WhatsApp Image 2025-12-29 at 18.31.56.jpeg
│   │   │       │   │   │   ├── WhatsApp Image 2025-12-29 at 18.31.57 (1).jpeg
│   │   │       │   │   │   ├── WhatsApp Image 2025-12-29 at 18.31.57 (2).jpeg
│   │   │       │   │   │   ├── WhatsApp Image 2025-12-29 at 18.31.57 (3).jpeg
│   │   │       │   │   │   └── WhatsApp Image 2025-12-29 at 18.31.57.jpeg
│   │   │       │   │   └── R09_Family_Suite.md
│   │   │       │   ├── 10
│   │   │       │   │   ├── 10-suite.md
│   │   │       │   │   ├── images
│   │   │       │   │   │   ├── 16c97eec-db21-4e5e-be2d-2b05ac313f03.jpeg
│   │   │       │   │   │   ├── 2839f125-782d-4bc3-8be6-e49137b62603.jpeg
│   │   │       │   │   │   ├── 28edfbc6-3e6d-4a6f-8049-cd5704cd49f1.jpeg
│   │   │       │   │   │   ├── 353c9e76-ce9d-4d6f-8c85-8ad0f68ef0b6.jpeg
│   │   │       │   │   │   ├── 4faf97ea-3e4f-43bb-9948-efde5cee3024.jpeg
│   │   │       │   │   │   ├── 7d3fce83-5676-4702-a087-7794d7d62047.jpeg
│   │   │       │   │   │   ├── 99d08b81-b2cd-4f5c-bd96-500349b2267e.jpeg
│   │   │       │   │   │   ├── 9cc5df3b-fb13-48ee-893e-5b5cfb910e2d.jpeg
│   │   │       │   │   │   ├── b47cf4b3-e431-4b69-94a7-8938ce0d3cd7.jpeg
│   │   │       │   │   │   ├── d26235fc-3eac-4eb8-b17e-a35388846bca.jpeg
│   │   │       │   │   │   ├── dbf42976-0b0a-4428-8a32-accf7ab2c5e3.jpeg
│   │   │       │   │   │   ├── _DSC1790-HDR.jpg
│   │   │       │   │   │   ├── _DSC1799-HDR.jpg
│   │   │       │   │   │   ├── _DSC1841-HDR.jpg
│   │   │       │   │   │   ├── _DSC1844-HDR.jpg
│   │   │       │   │   │   ├── _DSC1847-HDR.jpg
│   │   │       │   │   │   ├── _DSC1850-HDR.jpg
│   │   │       │   │   │   ├── _DSC1856-HDR.jpg
│   │   │       │   │   │   ├── _DSC1859-HDR.jpg
│   │   │       │   │   │   ├── _DSC1862-HDR.jpg
│   │   │       │   │   │   ├── main.jpg
│   │   │       │   │   │   ├── photo-01.jpg
│   │   │       │   │   │   ├── photo-02.jpg
│   │   │       │   │   │   ├── photo-03.jpg
│   │   │       │   │   │   ├── photo-04.jpg
│   │   │       │   │   │   ├── photo-05.jpg
│   │   │       │   │   │   ├── photo-06.jpg
│   │   │       │   │   │   ├── photo-07.jpg
│   │   │       │   │   │   ├── photo-08.jpg
│   │   │       │   │   │   ├── photo-09.jpg
│   │   │       │   │   │   └── photo-10.jpg
│   │   │       │   │   └── R10_Suite.md
│   │   │       │   ├── 11
│   │   │       │   │   ├── 11-family-suite.md
│   │   │       │   │   ├── images
│   │   │       │   │   │   ├── 0d8c4561-6084-4df5-ac5c-27f54c93ff77.jpeg
│   │   │       │   │   │   ├── 154f7a31-c702-4335-a59c-e7e1aaa66bd1.jpeg
│   │   │       │   │   │   ├── 2542c4d5-03cb-42bf-84e0-fd1c4ca4d48b.jpeg
│   │   │       │   │   │   ├── 2fdaca0f-f2b6-4bef-a060-89b39b2f5047.jpeg
│   │   │       │   │   │   ├── 3457046e-7ccb-4a0d-989b-59c2e91a3289.jpeg
│   │   │       │   │   │   ├── 36c6ddb7-5a5d-4273-806b-4200e43b761f.jpeg
│   │   │       │   │   │   ├── 3a07ff24-547c-41c6-bc43-52d64b05fe0b.jpeg
│   │   │       │   │   │   ├── 57f8cbd5-821e-46ad-a044-8e52616bdc68.jpeg
│   │   │       │   │   │   ├── 6af9af24-56c9-4923-acf2-956ff3a4f443.jpeg
│   │   │       │   │   │   ├── 6d6a27f7-d063-47da-9e35-657993905df5.jpeg
│   │   │       │   │   │   ├── 8a9cd811-bb91-4941-ac46-a4cfca1eeca5.jpeg
│   │   │       │   │   │   ├── 8f2f8be2-0474-4c17-aa2f-703fa4d69bf7.jpeg
│   │   │       │   │   │   ├── df267932-da7a-4fb7-b129-a03a84e86b95.jpeg
│   │   │       │   │   │   ├── _DSC1877-HDR.jpg
│   │   │       │   │   │   ├── _DSC1880-HDR.jpg
│   │   │       │   │   │   ├── _DSC1883-HDR.jpg
│   │   │       │   │   │   ├── _DSC1886-HDR.jpg
│   │   │       │   │   │   ├── _DSC1892-HDR.jpg
│   │   │       │   │   │   ├── _DSC1895-HDR.jpg
│   │   │       │   │   │   ├── _DSC1898-HDR.jpg
│   │   │       │   │   │   ├── _DSC1901-HDR.jpg
│   │   │       │   │   │   ├── _DSC1904-HDR.jpg
│   │   │       │   │   │   ├── _DSC1910-HDR.jpg
│   │   │       │   │   │   ├── _DSC1913-HDR.jpg
│   │   │       │   │   │   ├── e4c9406a-3004-4ed9-bbe1-8279d75e4344.jpeg
│   │   │       │   │   │   ├── main.jpg
│   │   │       │   │   │   ├── photo-01.jpg
│   │   │       │   │   │   ├── photo-02.jpg
│   │   │       │   │   │   ├── photo-03.jpg
│   │   │       │   │   │   ├── photo-04.jpg
│   │   │       │   │   │   ├── photo-05.jpg
│   │   │       │   │   │   ├── photo-06.jpg
│   │   │       │   │   │   ├── photo-07.jpg
│   │   │       │   │   │   ├── photo-08.jpg
│   │   │       │   │   │   ├── photo-09.jpg
│   │   │       │   │   │   ├── photo-10.jpg
│   │   │       │   │   │   ├── photo-11.jpg
│   │   │       │   │   │   ├── photo-12.jpg
│   │   │       │   │   │   └── photo-13.jpg
│   │   │       │   │   └── R11_Family_Suite.md
│   │   │       │   └── 12
│   │   │       │       ├── 12-presidential-suite.md
│   │   │       │       ├── images
│   │   │       │       │   ├── 14ab27e3-a52d-4073-a065-42364299a8bf.jpeg
│   │   │       │       │   ├── 43e062e4-eec4-49cd-a74f-3c1293cb6dc4.jpeg
│   │   │       │       │   ├── 9f916def-bd85-445d-bc6c-a8b21c5c0130.jpeg
│   │   │       │       │   ├── a93c5caf-6dfe-4587-843b-2be731c4a59d.jpeg
│   │   │       │       │   ├── b5432b13-c317-4ab6-b878-a0319952b997.jpeg
│   │   │       │       │   ├── bad3ec5f-fdd2-44cc-85da-41783b7c247e.jpeg
│   │   │       │       │   ├── bd76b680-2fef-4f99-9c30-bd509cf31f24.jpeg
│   │   │       │       │   ├── d2e88491-f9a5-4631-af4e-1d753f47d7ff.jpeg
│   │   │       │       │   ├── f283b53b-938a-4884-abf1-5bb9927cd5f3.jpeg
│   │   │       │       │   ├── f84b0bbf-948f-4bac-97b1-7d1e7f6784bc.jpeg
│   │   │       │       │   ├── main.jpg
│   │   │       │       │   ├── photo-01.jpg
│   │   │       │       │   ├── photo-02.jpg
│   │   │       │       │   ├── photo-03.jpg
│   │   │       │       │   ├── photo-04.jpg
│   │   │       │       │   ├── photo-05.jpg
│   │   │       │       │   ├── photo-06.jpg
│   │   │       │       │   ├── photo-07.jpg
│   │   │       │       │   ├── photo-08.jpg
│   │   │       │       │   └── photo-09.jpg
│   │   │       │       └── R12_Presidential_Suite.md
│   │   │       └── Trip.com_GDA.pdf
│   │   └── README.md
│   ├── decisions
│   │   └── architecture
│   │       ├── ADR-001-structure.md
│   │       ├── README.md
│   │       ├── stack
│   │       │   ├── README.md
│   │       │   ├── tech-stack-decision.md
│   │       │   └── tech_stack.md
│   │       └── VERSION.txt
│   ├── drafts
│   │   └── client
│   │       └── admin
│   │           ├── kiss_principle_notes.md
│   │           ├── project_history_transcript_lux.md
│   │           └── syntax_brainstorming.md
│   ├── knowledge
│   │   └── property
│   │       └── policies
│   │           └── events
│   │               └── events-privatization.md
│   ├── library
│   │   ├── 2025-12-29-sync-investigation.md
│   │   ├── 2026-01-28-demande-anniversaire-30-personnes.html
│   │   ├── alignment
│   │   │   ├── 2026-01-08-claude-md-externalization.md
│   │   │   └── 2026-01-08-document-evaluation.md
│   │   ├── analysis
│   │   │   └── credential-management-evaluation.md
│   │   ├── artifacts
│   │   │   ├── agent-registry-overview.md
│   │   │   ├── app_readiness_audit.md
│   │   │   ├── gemini_task_history.md
│   │   │   └── gemini_walkthrough.md
│   │   ├── content
│   │   │   ├── booking
│   │   │   │   └── initial_scan_2026_01_13.json
│   │   │   └── MANIFEST.md
│   │   ├── facilities
│   │   │   └── README.md
│   │   ├── FICHE-MISSION-OMAR-29-JANVIER.md
│   │   ├── guest-testimonials.md
│   │   ├── history
│   │   │   └── context
│   │   │       └── client
│   │   │           ├── CLIENT.md
│   │   │           ├── client-profile.md
│   │   │           ├── context.md
│   │   │           └── README.md
│   │   ├── hotelrunner-browser-test-results.md
│   │   ├── incidents
│   │   │   ├── open
│   │   │   │   └── 2025-12-29-webfetch-access-errors.md
│   │   │   └── README.md
│   │   ├── inventory
│   │   │   └── sub-agent_registry.md
│   │   ├── knowledge
│   │   │   ├── analysis
│   │   │   │   └── credential-management-evaluation.md
│   │   │   ├── brand
│   │   │   │   ├── branding
│   │   │   │   │   └── logo-design-brief.md
│   │   │   │   └── .gitkeep
│   │   │   ├── communications
│   │   │   │   ├── channels.json
│   │   │   │   ├── logs
│   │   │   │   │   ├── WhatsApp Chat with Said Thaifa.txt
│   │   │   │   │   ├── WhatsApp Ptt 2026-02-06 at 13.03.07.ogg
│   │   │   │   │   └── WhatsApp Ptt 2026-02-06 at 13.03.07.txt
│   │   │   │   ├── protocols.md
│   │   │   │   └── README.md
│   │   │   ├── external
│   │   │   │   └── expedia
│   │   │   │       ├── expedia_central_partner.md
│   │   │   │       └── Expedia_Group_Partner_Central.md
│   │   │   ├── finance
│   │   │   │   ├── accounting.md
│   │   │   │   └── README.md
│   │   │   ├── journey
│   │   │   │   └── legacy_transfer.md
│   │   │   ├── processes
│   │   │   │   ├── check-in-out.json
│   │   │   │   ├── emergency.json
│   │   │   │   ├── housekeeping.json
│   │   │   │   ├── maintenance.json
│   │   │   │   └── README.md
│   │   │   ├── research
│   │   │   │   └── 2025-12-29-multi-agent-orchestration-patterns.md
│   │   │   └── strategic
│   │   │       └── 2025-12-28-platform-mastery-strategy.md
│   │   ├── lessons-learned.md
│   │   ├── logs
│   │   │   └── changes
│   │   │       ├── CHANGELOG.md
│   │   │       ├── changelog-promotions.md
│   │   │       └── changelog-reservations.md
│   │   ├── MESSAGE-POUR-SAID.txt
│   │   ├── meta
│   │   │   ├── Agentic Mastery.md
│   │   │   ├── BRIEFING-COMPLET-29-JANVIER-2026.md
│   │   │   └── INDEX-SESSION-28-JANVIER-2026.md
│   │   ├── OVERVIEW.md
│   │   ├── patterns
│   │   │   └── decision-evaluator-agent-pattern.md
│   │   ├── project
│   │   │   ├── audit
│   │   │   │   └── 2026-01-17_audit.md
│   │   │   ├── BRIEF.md
│   │   │   ├── briefs
│   │   │   │   ├── 2025-12-22-hws-introduction.md
│   │   │   │   ├── hotelrunner-poc-2025-12-19.md
│   │   │   │   └── jisr-mokawala-investigation-2025-12.md
│   │   │   ├── communication
│   │   │   │   ├── decisions_needed.md
│   │   │   │   └── general_inquiries.md
│   │   │   ├── legacy
│   │   │   │   └── villa-thaifa-reponse-said-2026-01-28.json
│   │   │   ├── meta
│   │   │   │   ├── MISSION.md
│   │   │   │   ├── STATE.md
│   │   │   │   └── VERSION
│   │   │   ├── onboarding
│   │   │   │   ├── Onboarding.md
│   │   │   │   └── Onboarding_-_Policies_and_Settings.md
│   │   │   ├── operations
│   │   │   │   ├── CREDENTIALS.md
│   │   │   │   ├── expedia
│   │   │   │   │   ├── amenities_gap_analysis_FR.md
│   │   │   │   │   ├── amenities_gap_analysis.md
│   │   │   │   │   ├── amenities_recommendation_FR.md
│   │   │   │   │   ├── amenities_recommendation.md
│   │   │   │   │   ├── developer_onboarding_guide.md
│   │   │   │   │   └── onboarding_capture_v1.md
│   │   │   │   ├── incidents
│   │   │   │   │   └── open
│   │   │   │   ├── linear-github-setup.md
│   │   │   │   ├── management
│   │   │   │   │   ├── engagement_audit
│   │   │   │   │   │   ├── audit_tracker.md
│   │   │   │   │   │   ├── comprehensive_work_log.md
│   │   │   │   │   │   ├── repository_tree.txt
│   │   │   │   │   │   ├── scope_audit.md
│   │   │   │   │   │   └── strategic_reframing.md
│   │   │   │   │   └── reports
│   │   │   │   │       └── status_report_v1.md
│   │   │   │   ├── requests
│   │   │   │   │   └── 2026-01-28-expedia-tax-correction.md
│   │   │   │   └── rules
│   │   │   │       ├── .env.rules.md
│   │   │   │       ├── git.md
│   │   │   │       ├── linear-workflow.md
│   │   │   │       ├── README.md
│   │   │   │       ├── verification.md
│   │   │   │       └── workspace.md
│   │   │   ├── planning
│   │   │   │   ├── 2026-01-08-core-loop-simplification.md
│   │   │   │   ├── 2026-01-13-room-mapping-investigation.md
│   │   │   │   ├── ANALYSIS-ARCHITECTURE.md
│   │   │   │   ├── audit
│   │   │   │   │   ├── ARCHITECTURE-PROPOSAL.md
│   │   │   │   │   ├── CONFLICT-MAP.md
│   │   │   │   │   ├── CONSOLIDATION-PLAN.md
│   │   │   │   │   ├── DATA-INVENTORY.md
│   │   │   │   │   └── REQUIREMENTS.md
│   │   │   │   ├── codebase
│   │   │   │   │   ├── ARCHITECTURE.md
│   │   │   │   │   ├── CONCERNS.md
│   │   │   │   │   ├── CONVENTIONS.md
│   │   │   │   │   ├── INTEGRATIONS.md
│   │   │   │   │   ├── STACK.md
│   │   │   │   │   └── TESTING.md
│   │   │   │   ├── comprehensive-transformation-plan.md
│   │   │   │   ├── generate-structure-map.md
│   │   │   │   ├── git-branching-strategy.md
│   │   │   │   ├── HANDOFF-EM-191.md
│   │   │   │   ├── implementation_plan_expedia.md
│   │   │   │   ├── NEXT_STEPS.md
│   │   │   │   ├── phases
│   │   │   │   │   └── 01-operational-urgency
│   │   │   │   │       ├── 01-01-PLAN.md
│   │   │   │   │       ├── 01-01-SUMMARY.md
│   │   │   │   │       ├── 01-02-PLAN.md
│   │   │   │   │       └── 01-RESEARCH.md
│   │   │   │   ├── PROJECT.md
│   │   │   │   ├── REQUIREMENTS.md
│   │   │   │   ├── ROADMAP-2.md
│   │   │   │   ├── ROADMAP.md
│   │   │   │   ├── STATE.md
│   │   │   │   ├── unified-workspace-governance.md
│   │   │   │   ├── vision_2026.md
│   │   │   │   ├── VISION-DRAFT.md
│   │   │   │   ├── VISION-ENRICHED.md
│   │   │   │   └── workspace-standardization-plan.md
│   │   │   ├── project_structure.md
│   │   │   ├── README.md
│   │   │   ├── reports
│   │   │   │   ├── 2025-12-19-exploration-reservations-hotelrunner.md
│   │   │   │   ├── 2025-12-19-rapport-reservations-said.md
│   │   │   │   ├── 2025-12-19-rapport-reservations-said.pdf
│   │   │   │   ├── 2025-12-20-rapport-reservations-v2.md
│   │   │   │   ├── 2025-12-20_resilience-erreurs-techniques.md
│   │   │   │   ├── 2025-12-29-sync-investigation.html
│   │   │   │   ├── 2026-01-08-property-type-scout-report.md
│   │   │   │   ├── 2026-01-28-migration-plan-completed.md
│   │   │   │   ├── BRUTAL-AUDIT-REPORT-2026-01-16.md
│   │   │   │   ├── client-profile-optimization
│   │   │   │   │   ├── final.md
│   │   │   │   │   ├── patterns.md
│   │   │   │   │   ├── sources.md
│   │   │   │   │   ├── step-back.md
│   │   │   │   │   └── synthesis.md
│   │   │   │   ├── hotelrunner-demo
│   │   │   │   │   ├── blocage-prix-booking.md
│   │   │   │   │   ├── Nouveau.md
│   │   │   │   │   └── rapport-demo-20-dec-2025.md
│   │   │   │   ├── MIGRATION-REPORT.md
│   │   │   │   ├── PHASE-2-COMPLETION-REPORT.md
│   │   │   │   ├── pm-template-selection
│   │   │   │   │   ├── final.md
│   │   │   │   │   ├── patterns.md
│   │   │   │   │   ├── project_standards.md
│   │   │   │   │   ├── prompt-en.md
│   │   │   │   │   ├── prompt.md
│   │   │   │   │   ├── sources.md
│   │   │   │   │   ├── step-back.md
│   │   │   │   │   └── synthesis.md
│   │   │   │   ├── pricing-strategy-session
│   │   │   │   │   ├── audit-promotions-booking.md
│   │   │   │   │   ├── execution-log-booking.md
│   │   │   │   │   ├── execution-log-hotelrunner.md
│   │   │   │   │   ├── grille-tarifaire-officielle.md
│   │   │   │   │   ├── plan-promotions-booking.md
│   │   │   │   │   ├── rapport-promotions-msaid.md
│   │   │   │   │   ├── rapport-promotions-msaid.pdf
│   │   │   │   │   └── rapport-session-20-dec-2025.md
│   │   │   │   ├── profile-reorganization
│   │   │   │   │   ├── final.md
│   │   │   │   │   ├── rdv-prep-agenda.md
│   │   │   │   │   └── rdv-prep-checklist.md
│   │   │   │   ├── rapport-audit-v2.md
│   │   │   │   ├── ULTIMATE-PROPOSAL-2026-01-16.html
│   │   │   │   └── verification-promotions-booking
│   │   │   │       ├── final.md
│   │   │   │       ├── patterns.md
│   │   │   │       ├── sources.md
│   │   │   │       ├── step-back.md
│   │   │   │       └── synthesis.md
│   │   │   ├── specs
│   │   │   │   ├── hotel
│   │   │   │   │   └── ROOM_DATA_SHEET_FOR_SAID.md
│   │   │   │   ├── knowledge
│   │   │   │   │   ├── booking_extranet_guide.md
│   │   │   │   │   ├── booking_extranet_incidents.md
│   │   │   │   │   ├── logs
│   │   │   │   │   │   └── pricing.md
│   │   │   │   │   ├── platforms
│   │   │   │   │   │   ├── booking
│   │   │   │   │   │   │   ├── booking-com-data.md
│   │   │   │   │   │   │   ├── ui-nuances.md
│   │   │   │   │   │   │   └── xml-lock.md
│   │   │   │   │   │   └── hotelrunner
│   │   │   │   │   │       ├── api-reference.md
│   │   │   │   │   │       ├── channel-mapping.md
│   │   │   │   │   │       ├── channels_codes.csv
│   │   │   │   │   │       ├── hotelrunner-api.md
│   │   │   │   │   │       ├── hotelrunner.md
│   │   │   │   │   │       ├── hr_airbnb_reqs.png
│   │   │   │   │   │       ├── hr_api_auth_details.png
│   │   │   │   │   │       ├── hr_channels_status.png
│   │   │   │   │   │       ├── hr_expedia_reqs.png
│   │   │   │   │   │       └── hr_rooms_list.png
│   │   │   │   │   ├── policies
│   │   │   │   │   │   ├── archive-policy.md
│   │   │   │   │   │   └── rules
│   │   │   │   │   │       └── rules.md
│   │   │   │   │   └── villa-thaifa
│   │   │   │   │       ├── baseline.md
│   │   │   │   │       ├── chambre_et_vue.md
│   │   │   │   │       ├── CLAUDE.md
│   │   │   │   │       ├── current.md
│   │   │   │   │       ├── platform-mapping.md
│   │   │   │   │       ├── README.md
│   │   │   │   │       ├── state
│   │   │   │   │       │   ├── current
│   │   │   │   │       │   │   ├── assignments
│   │   │   │   │       │   │   │   └── assignments.md
│   │   │   │   │       │   │   ├── blockers
│   │   │   │   │       │   │   │   └── blockers.md
│   │   │   │   │       │   │   ├── README.md
│   │   │   │   │       │   │   └── reserverations
│   │   │   │   │       │   │       └── reservations.md
│   │   │   │   │       │   ├── planned
│   │   │   │   │       │   │   ├── pricing.md
│   │   │   │   │       │   │   └── README.md
│   │   │   │   │       │   └── README.md
│   │   │   │   │       └── support
│   │   │   │   │           └── README.md
│   │   │   │   └── templates
│   │   │   │       └── ROOM_MASTER_TEMPLATE.md
│   │   │   ├── standards
│   │   │   │   ├── agent-capabilities.md
│   │   │   │   ├── agent-capability-schema.json
│   │   │   │   ├── agent-cheatsheet.md
│   │   │   │   ├── agents
│   │   │   │   │   ├── code_of_conduct.md
│   │   │   │   │   ├── collaboration_protocol.md
│   │   │   │   │   └── registry.md
│   │   │   │   ├── frontmatter-schema.md
│   │   │   │   └── scoring-system.json
│   │   │   ├── templates
│   │   │   └── testing
│   │   │       ├── decision-card-001.md
│   │   │       ├── execution-log-001.md
│   │   │       ├── execution-log-002.md
│   │   │       ├── FINAL-REPORT-2026-01-16.md
│   │   │       ├── OPTIMIZATION-PLAN.md
│   │   │       └── scenarios.md
│   │   ├── README.md
│   │   ├── REPRISE-APRES-MIGRATION.md
│   │   ├── services-transport.md
│   │   ├── sessions
│   │   │   ├── 2026-01-29-agent-unification.md
│   │   │   └── 2026-01-29-inter-agent-sync.md
│   │   ├── SESSION-SUMMARY-2026-01-24.md
│   │   ├── state
│   │   │   ├── baseline
│   │   │   │   ├── README.md
│   │   │   │   └── snapshots
│   │   │   │       └── 2025-12-20-pre-audit.md
│   │   │   ├── current
│   │   │   │   └── README.md
│   │   │   ├── execution
│   │   │   │   └── README.md
│   │   │   ├── history
│   │   │   │   └── README.md
│   │   │   └── planned
│   │   │       └── README.md
│   │   ├── templates
│   │   │   ├── canonical-domain-template.md
│   │   │   ├── deletion-safety-report-template.md
│   │   │   ├── README.md
│   │   │   ├── reconciliation-entry-template.md
│   │   │   ├── reservation-report-template.md
│   │   │   └── weekly-summary-template.md
│   │   ├── temporary_capture.md
│   │   ├── TODOs.md
│   │   └── workflows
│   │       ├── git-session-start.md
│   │       ├── guest-communication.md
│   │       ├── pricing.md
│   │       ├── README.md
│   │       └── reservation.md
│   ├── management
│   │   ├── briefs
│   │   │   ├── 2025-12-22-hws-introduction.md
│   │   │   └── BRIEF.md
│   │   ├── missions
│   │   │   ├── completed
│   │   │   │   ├── 2025-12-28-thaifa-chambre4-gouram.md
│   │   │   │   └── 2025-12-28-thaifa-chambre5-sync-investigation.md
│   │   │   ├── queue
│   │   │   │   ├── p0
│   │   │   │   │   └── .md
│   │   │   │   ├── p1
│   │   │   │   │   ├── 2025-12-23-thaifa-room-restructuring.md
│   │   │   │   │   └── 2025-12-29-thaifa-hotelrunner-admin-access.md
│   │   │   │   ├── p2
│   │   │   │   │   ├── 2025-12-23-thaifa-booking-data.md
│   │   │   │   │   ├── 2025-12-23-thaifa-image-organization.md
│   │   │   │   │   ├── 2025-12-28-thaifa-hotelrunner-api-scout.md
│   │   │   │   │   └── 2026-01-08-thaifa-property-type-investigation.md
│   │   │   │   ├── p3
│   │   │   │   │   └── 2025-12-23-thaifa-validation-pdf.md
│   │   │   │   └── tasks
│   │   │   │       ├── 2026-01-24-extend-pricing-2026.md
│   │   │   │       ├── 2026-01-24-stop-sell-mars.md
│   │   │   │       └── active.md
│   │   │   └── README.md
│   │   ├── planning
│   │   │   ├── 2026-02-13-agentic-kiss-transformation-plan.md
│   │   │   ├── 2026-02-13-agentic-operating-playbook.md
│   │   │   ├── 2026-02-13-next-7-days.md
│   │   │   └── 2026-02-14-room-modularization.md
│   │   └── tasks
│   │       └── README.md
│   └── README.md
├── GEMINI.md
├── .gitignore
├── Makefile
├── ops
│   ├── intake
│   │   └── unprocessed
│   │       ├── manifest.csv
│   │       ├── README.md
│   │       └── unprocessed-files.md
│   └── status
│       ├── 2026-02-13-isolation-report-full-depth.md
│       ├── 2026-02-13-isolation-report.md
│       ├── archived.md
│       ├── canonical.md
│       ├── inbox.md
│       ├── INDEX.md
│       ├── planned.md
│       └── working.md
├── pyproject.toml
├── README.md
├── ROADMAP.md
├── scripts
│   ├── check_unique_info.py
│   ├── domain_verify.py
│   ├── hotelrunner
│   │   └── extract_reservations.py
│   ├── inventory
│   │   └── export-ota.py
│   ├── organization
│   │   └── reorganize_room_images.py
│   └── validate_contracts.py
├── .secrets
│   ├── .env
│   └── .env.example
├── specs
│   ├── README.md
│   └── VILLA_THAIFA.json
├── src
│   └── villa_ops
│       └── README.md
├── STRUCTURE_CLEAN.txt
├── STRUCTURE.txt
├── tests
│   └── test_scripts.py
└── uv.lock

201 directories, 882 files

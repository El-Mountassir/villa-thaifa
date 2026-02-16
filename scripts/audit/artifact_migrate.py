#!/usr/bin/env python3
"""
Context Migration — Villa Thaifa Repository.

Centralizes context files into the `context/` directory tree using the
tri-state lifecycle taxonomy (source / meta / audit).

Target structure:
    context/
    ├── meta/
    │   ├── architecture/   ← decisions, ADRs
    │   ├── planning/       ← briefs, missions, roadmaps
    │   ├── knowledge/      ← workflows, research, patterns
    │   └── templates/      ← standards, reusable templates
    └── audit/
        ├── history/        ← session logs, changelogs
        ├── snapshots/      ← structure dumps, temp captures
        └── quality/        ← reports, audits, test results

Safety guarantees:
  - Dry-run by default (pass --execute to actually move)
  - Never deletes source files — uses shutil.copy2 then verifies
  - Generates a migration log with before/after paths
  - SHA-256 checksum verification after every copy

Usage:
    python3 scripts/artifact_migrate.py                       # dry-run
    python3 scripts/artifact_migrate.py --execute             # actual migration
    python3 scripts/artifact_migrate.py --category history    # single category
    python3 scripts/artifact_migrate.py --phase 1             # phase 1 only
    python3 scripts/artifact_migrate.py --phase 2             # phase 2 only
"""

import argparse
import hashlib
import os
import shutil
import sys
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path


# ── Migration Categories ─────────────────────────────────────────────

MIGRATION_CATEGORIES = {
    # ── Phase 1 (low-risk context files) ──
    "architecture": {
        "phase": 1,
        "target": "context/meta/architecture",
        "taxonomy": "meta:architecture",
        "files": [
            "docs/decisions/architecture/ADR-001-structure.md",
            "docs/decisions/architecture/README.md",
            "docs/decisions/architecture/VERSION.txt",
            "docs/decisions/architecture/stack/README.md",
            "docs/decisions/architecture/stack/tech-stack-decision.md",
            "docs/decisions/architecture/stack/tech_stack.md",
        ],
    },
    "history": {
        "phase": 1,
        "target": "context/audit/history",
        "taxonomy": "audit:history",
        "files": [
            "docs/library/SESSION-SUMMARY-2026-01-24.md",
            "docs/library/knowledge/communications/logs/WhatsApp Chat with Said Thaifa.txt",
            "docs/library/knowledge/communications/logs/WhatsApp Ptt 2026-02-06 at 13.03.07.ogg",
            "docs/library/knowledge/communications/logs/WhatsApp Ptt 2026-02-06 at 13.03.07.txt",
            "docs/library/logs/changes/CHANGELOG.md",
            "docs/library/logs/changes/changelog-promotions.md",
            "docs/library/logs/changes/changelog-reservations.md",
            "docs/library/meta/Agentic Mastery.md",
            "docs/library/meta/BRIEFING-COMPLET-29-JANVIER-2026.md",
            "docs/library/meta/INDEX-SESSION-28-JANVIER-2026.md",
            "docs/library/project/meta/MISSION.md",
            "docs/library/project/meta/STATE.md",
            "docs/library/project/meta/VERSION",
            "docs/library/project/specs/knowledge/logs/pricing.md",
            "docs/library/sessions/2026-01-29-agent-unification.md",
            "docs/library/sessions/2026-01-29-inter-agent-sync.md",
        ],
    },
    "snapshots": {
        "phase": 1,
        "target": "context/audit/snapshots",
        "taxonomy": "audit:snapshot",
        "files": [
            "ROADMAP.md",
            "STRUCTURE.txt",
            "STRUCTURE_CLEAN.txt",
            "docs/library/history/context/client/CLIENT.md",
            "docs/library/history/context/client/README.md",
            "docs/library/history/context/client/client-profile.md",
            "docs/library/history/context/client/context.md",
            "docs/library/project/legacy/villa-thaifa-reponse-said-2026-01-28.json",
            "docs/library/project/project_structure.md",
            "docs/library/project/specs/knowledge/villa-thaifa/state/README.md",
            "docs/library/project/specs/knowledge/villa-thaifa/state/current/README.md",
            "docs/library/project/specs/knowledge/villa-thaifa/state/current/assignments/assignments.md",
            "docs/library/project/specs/knowledge/villa-thaifa/state/current/blockers/blockers.md",
            "docs/library/project/specs/knowledge/villa-thaifa/state/current/reserverations/reservations.md",
            "docs/library/project/specs/knowledge/villa-thaifa/state/planned/README.md",
            "docs/library/project/specs/knowledge/villa-thaifa/state/planned/pricing.md",
            "docs/library/state/baseline/README.md",
            "docs/library/state/baseline/snapshots/2025-12-20-pre-audit.md",
            "docs/library/state/current/README.md",
            "docs/library/state/execution/README.md",
            "docs/library/state/history/README.md",
            "docs/library/state/planned/README.md",
            "docs/library/temporary_capture.md",
        ],
    },

    # ── Phase 2 (deep consolidation) ──
    "planning": {
        "phase": 2,
        "target": "context/meta/planning",
        "taxonomy": "meta:planning",
        "files": [
            "docs/library/FICHE-MISSION-OMAR-29-JANVIER.md",
            "docs/library/REPRISE-APRES-MIGRATION.md",
            "docs/library/TODOs.md",
            "docs/library/alignment/2026-01-08-claude-md-externalization.md",
            "docs/library/alignment/2026-01-08-document-evaluation.md",
            "docs/library/project/BRIEF.md",
            "docs/library/project/briefs/2025-12-22-hws-introduction.md",
            "docs/library/project/briefs/hotelrunner-poc-2025-12-19.md",
            "docs/library/project/briefs/jisr-mokawala-investigation-2025-12.md",
            "docs/library/project/operations/CREDENTIALS.md",
            "docs/library/project/operations/expedia/amenities_gap_analysis.md",
            "docs/library/project/operations/expedia/amenities_gap_analysis_FR.md",
            "docs/library/project/operations/expedia/amenities_recommendation.md",
            "docs/library/project/operations/expedia/amenities_recommendation_FR.md",
            "docs/library/project/operations/expedia/developer_onboarding_guide.md",
            "docs/library/project/operations/expedia/onboarding_capture_v1.md",
            "docs/library/project/operations/linear-github-setup.md",
            "docs/library/project/operations/management/engagement_audit/audit_tracker.md",
            "docs/library/project/operations/management/engagement_audit/comprehensive_work_log.md",
            "docs/library/project/operations/management/engagement_audit/repository_tree.txt",
            "docs/library/project/operations/management/engagement_audit/scope_audit.md",
            "docs/library/project/operations/management/engagement_audit/strategic_reframing.md",
            "docs/library/project/operations/requests/2026-01-28-expedia-tax-correction.md",
            "docs/library/project/operations/rules/.env.rules.md",
            "docs/library/project/operations/rules/README.md",
            "docs/library/project/operations/rules/git.md",
            "docs/library/project/operations/rules/linear-workflow.md",
            "docs/library/project/operations/rules/verification.md",
            "docs/library/project/operations/rules/workspace.md",
            "docs/library/project/planning/2026-01-08-core-loop-simplification.md",
            "docs/library/project/planning/2026-01-13-room-mapping-investigation.md",
            "docs/library/project/planning/ANALYSIS-ARCHITECTURE.md",
            "docs/library/project/planning/HANDOFF-EM-191.md",
            "docs/library/project/planning/NEXT_STEPS.md",
            "docs/library/project/planning/PROJECT.md",
            "docs/library/project/planning/REQUIREMENTS.md",
            "docs/library/project/planning/ROADMAP-2.md",
            "docs/library/project/planning/ROADMAP.md",
            "docs/library/project/planning/STATE.md",
            "docs/library/project/planning/VISION-DRAFT.md",
            "docs/library/project/planning/VISION-ENRICHED.md",
            "docs/library/project/planning/audit/ARCHITECTURE-PROPOSAL.md",
            "docs/library/project/planning/audit/CONFLICT-MAP.md",
            "docs/library/project/planning/audit/CONSOLIDATION-PLAN.md",
            "docs/library/project/planning/audit/DATA-INVENTORY.md",
            "docs/library/project/planning/audit/REQUIREMENTS.md",
            "docs/library/project/planning/codebase/ARCHITECTURE.md",
            "docs/library/project/planning/codebase/CONCERNS.md",
            "docs/library/project/planning/codebase/CONVENTIONS.md",
            "docs/library/project/planning/codebase/INTEGRATIONS.md",
            "docs/library/project/planning/codebase/STACK.md",
            "docs/library/project/planning/codebase/TESTING.md",
            "docs/library/project/planning/comprehensive-transformation-plan.md",
            "docs/library/project/planning/generate-structure-map.md",
            "docs/library/project/planning/git-branching-strategy.md",
            "docs/library/project/planning/implementation_plan_expedia.md",
            "docs/library/project/planning/phases/01-operational-urgency/01-01-PLAN.md",
            "docs/library/project/planning/phases/01-operational-urgency/01-01-SUMMARY.md",
            "docs/library/project/planning/phases/01-operational-urgency/01-02-PLAN.md",
            "docs/library/project/planning/phases/01-operational-urgency/01-RESEARCH.md",
            "docs/library/project/planning/unified-workspace-governance.md",
            "docs/library/project/planning/vision_2026.md",
            "docs/library/project/planning/workspace-standardization-plan.md",
            "docs/library/project/specs/hotel/ROOM_DATA_SHEET_FOR_SAID.md",
            "docs/management/briefs/2025-12-22-hws-introduction.md",
            "docs/management/briefs/BRIEF.md",
            "docs/management/missions/README.md",
            "docs/management/missions/completed/2025-12-28-thaifa-chambre4-gouram.md",
            "docs/management/missions/completed/2025-12-28-thaifa-chambre5-sync-investigation.md",
            "docs/management/missions/queue/p0/.md",
            "docs/management/missions/queue/p1/2025-12-23-thaifa-room-restructuring.md",
            "docs/management/missions/queue/p1/2025-12-29-thaifa-hotelrunner-admin-access.md",
            "docs/management/missions/queue/p2/2025-12-23-thaifa-booking-data.md",
            "docs/management/missions/queue/p2/2025-12-23-thaifa-image-organization.md",
            "docs/management/missions/queue/p2/2025-12-28-thaifa-hotelrunner-api-scout.md",
            "docs/management/missions/queue/p2/2026-01-08-thaifa-property-type-investigation.md",
            "docs/management/missions/queue/p3/2025-12-23-thaifa-validation-pdf.md",
            "docs/management/missions/queue/tasks/2026-01-24-extend-pricing-2026.md",
            "docs/management/missions/queue/tasks/2026-01-24-stop-sell-mars.md",
            "docs/management/missions/queue/tasks/active.md",
            "docs/management/planning/2026-02-13-agentic-kiss-transformation-plan.md",
            "docs/management/planning/2026-02-13-agentic-operating-playbook.md",
            "docs/management/planning/2026-02-13-next-7-days.md",
            "docs/management/planning/2026-02-14-room-modularization.md",
            "docs/management/tasks/README.md",
            "specs/README.md",
            "specs/VILLA_THAIFA.json",
        ],
    },
    "knowledge": {
        "phase": 2,
        "target": "context/meta/knowledge",
        "taxonomy": "meta:knowledge",
        "files": [
            "docs/agents/workflows/hotelrunner/README.md",
            "docs/knowledge/property/policies/events/events-privatization.md",
            "docs/library/OVERVIEW.md",
            "docs/library/knowledge/analysis/credential-management-evaluation.md",
            "docs/library/knowledge/brand/.gitkeep",
            "docs/library/knowledge/brand/branding/logo-design-brief.md",
            "docs/library/knowledge/communications/README.md",
            "docs/library/knowledge/communications/channels.json",
            "docs/library/knowledge/communications/protocols.md",
            "docs/library/knowledge/external/expedia/Expedia_Group_Partner_Central.md",
            "docs/library/knowledge/external/expedia/expedia_central_partner.md",
            "docs/library/knowledge/finance/README.md",
            "docs/library/knowledge/finance/accounting.md",
            "docs/library/knowledge/journey/legacy_transfer.md",
            "docs/library/knowledge/processes/README.md",
            "docs/library/knowledge/processes/check-in-out.json",
            "docs/library/knowledge/processes/emergency.json",
            "docs/library/knowledge/processes/housekeeping.json",
            "docs/library/knowledge/processes/maintenance.json",
            "docs/library/knowledge/research/2025-12-29-multi-agent-orchestration-patterns.md",
            "docs/library/knowledge/strategic/2025-12-28-platform-mastery-strategy.md",
            "docs/library/lessons-learned.md",
            "docs/library/patterns/decision-evaluator-agent-pattern.md",
            "docs/library/project/onboarding/Onboarding.md",
            "docs/library/project/onboarding/Onboarding_-_Policies_and_Settings.md",
            "docs/library/project/specs/knowledge/booking_extranet_guide.md",
            "docs/library/project/specs/knowledge/booking_extranet_incidents.md",
            "docs/library/project/specs/knowledge/platforms/booking/booking-com-data.md",
            "docs/library/project/specs/knowledge/platforms/booking/ui-nuances.md",
            "docs/library/project/specs/knowledge/platforms/booking/xml-lock.md",
            "docs/library/project/specs/knowledge/platforms/hotelrunner/api-reference.md",
            "docs/library/project/specs/knowledge/platforms/hotelrunner/channel-mapping.md",
            "docs/library/project/specs/knowledge/platforms/hotelrunner/channels_codes.csv",
            "docs/library/project/specs/knowledge/platforms/hotelrunner/hotelrunner-api.md",
            "docs/library/project/specs/knowledge/platforms/hotelrunner/hotelrunner.md",
            "docs/library/project/specs/knowledge/platforms/hotelrunner/hr_airbnb_reqs.png",
            "docs/library/project/specs/knowledge/platforms/hotelrunner/hr_api_auth_details.png",
            "docs/library/project/specs/knowledge/platforms/hotelrunner/hr_channels_status.png",
            "docs/library/project/specs/knowledge/platforms/hotelrunner/hr_expedia_reqs.png",
            "docs/library/project/specs/knowledge/platforms/hotelrunner/hr_rooms_list.png",
            "docs/library/project/specs/knowledge/policies/archive-policy.md",
            "docs/library/project/specs/knowledge/policies/rules/rules.md",
            "docs/library/project/specs/knowledge/villa-thaifa/CLAUDE.md",
            "docs/library/project/specs/knowledge/villa-thaifa/README.md",
            "docs/library/project/specs/knowledge/villa-thaifa/baseline.md",
            "docs/library/project/specs/knowledge/villa-thaifa/chambre_et_vue.md",
            "docs/library/project/specs/knowledge/villa-thaifa/current.md",
            "docs/library/project/specs/knowledge/villa-thaifa/platform-mapping.md",
            "docs/library/project/specs/knowledge/villa-thaifa/support/README.md",
            "docs/library/workflows/README.md",
            "docs/library/workflows/git-session-start.md",
            "docs/library/workflows/guest-communication.md",
            "docs/library/workflows/pricing.md",
            "docs/library/workflows/reservation.md",
        ],
    },
    "templates": {
        "phase": 2,
        "target": "context/meta/templates",
        "taxonomy": "meta:templates",
        "files": [
            "docs/agents/standards/2026-01-09-10-44-55-villa-thaifa-najib-insights-brief-strategy.txt",
            "docs/agents/standards/claude-code-hotelrunner-investigation-prompt.md",
            "docs/agents/standards/gemini-lux-action-plan.md",
            "docs/agents/standards/gemini-onboarding-prompt.md",
            "docs/agents/standards/gemini-system-prompt.md",
            "docs/agents/standards/google-ai-studio-quick-guide.md",
            "docs/agents/standards/lhcm-os-strategy-execution-plan-v0.1.0.md",
            "docs/agents/standards/najib-conversation-part1-analysis-v0.1.0.md",
            "docs/agents/standards/najib-mountassir-context-v0.1.0.md",
            "docs/agents/standards/tech-stack-omar-v0.1.3-lux-annotated.md",
            "docs/agents/standards/villa-thaifa-artifacts-inventory-v0.1.0.md",
            "docs/agents/standards/villa-thaifa-client-brief-v0.1.0.md",
            "docs/agents/standards/villa-thaifa-client-brief-v0.2.0.md",
            "docs/agents/standards/villa-thaifa-decisions-log-v0.1.0.md",
            "docs/agents/standards/villa-thaifa-execution-plan-2025-01-09-night.md",
            "docs/agents/standards/villa-thaifa-internal-app-requirements-v0.1.0.md",
            "docs/agents/standards/villa-thaifa-migration-plan-v0.1.0.md",
            "docs/agents/standards/villa-thaifa-migration-progress-report-v0.1.0.md",
            "docs/agents/standards/villa-thaifa-mission-lundi-12h00.md",
            "docs/agents/standards/villa-thaifa-open-questions-v0.1.0.md",
            "docs/agents/standards/villa-thaifa-project-brief-v0.2.0.md",
            "docs/agents/standards/villa-thaifa-quick-start-v0.1.0.md",
            "docs/agents/standards/villa-thaifa-repo-exploration-v0.1.0.md",
            "docs/agents/standards/villa-thaifa-research-findings-v0.1.0.md",
            "docs/agents/standards/villa-thaifa-technical-context-v0.1.0.md",
            "docs/agents/standards/villa-thaifa-workstream-master-v0.1.0.md",
            "docs/agents/templates/handovers/template.md",
            "docs/library/project/specs/templates/ROOM_MASTER_TEMPLATE.md",
            "docs/library/project/standards/agent-capabilities.md",
            "docs/library/project/standards/agent-capability-schema.json",
            "docs/library/project/standards/agent-cheatsheet.md",
            "docs/library/project/standards/agents/code_of_conduct.md",
            "docs/library/project/standards/agents/collaboration_protocol.md",
            "docs/library/project/standards/agents/registry.md",
            "docs/library/project/standards/frontmatter-schema.md",
            "docs/library/project/standards/scoring-system.json",
            "docs/library/templates/README.md",
            "docs/library/templates/canonical-domain-template.md",
            "docs/library/templates/deletion-safety-report-template.md",
            "docs/library/templates/reconciliation-entry-template.md",
            "docs/library/templates/reservation-report-template.md",
            "docs/library/templates/weekly-summary-template.md",
        ],
    },
    "quality": {
        "phase": 2,
        "target": "context/audit/quality",
        "taxonomy": "audit:quality",
        "files": [
            "docs/library/2025-12-29-sync-investigation.md",
            "docs/library/analysis/credential-management-evaluation.md",
            "docs/library/artifacts/agent-registry-overview.md",
            "docs/library/artifacts/app_readiness_audit.md",
            "docs/library/artifacts/gemini_task_history.md",
            "docs/library/artifacts/gemini_walkthrough.md",
            "docs/library/guest-testimonials.md",
            "docs/library/hotelrunner-browser-test-results.md",
            "docs/library/incidents/README.md",
            "docs/library/incidents/open/2025-12-29-webfetch-access-errors.md",
            "docs/library/project/audit/2026-01-17_audit.md",
            "docs/library/project/operations/management/reports/status_report_v1.md",
            "docs/library/project/reports/2025-12-19-exploration-reservations-hotelrunner.md",
            "docs/library/project/reports/2025-12-19-rapport-reservations-said.md",
            "docs/library/project/reports/2025-12-19-rapport-reservations-said.pdf",
            "docs/library/project/reports/2025-12-20-rapport-reservations-v2.md",
            "docs/library/project/reports/2025-12-20_resilience-erreurs-techniques.md",
            "docs/library/project/reports/2025-12-29-sync-investigation.html",
            "docs/library/project/reports/2026-01-08-property-type-scout-report.md",
            "docs/library/project/reports/2026-01-28-migration-plan-completed.md",
            "docs/library/project/reports/BRUTAL-AUDIT-REPORT-2026-01-16.md",
            "docs/library/project/reports/MIGRATION-REPORT.md",
            "docs/library/project/reports/PHASE-2-COMPLETION-REPORT.md",
            "docs/library/project/reports/ULTIMATE-PROPOSAL-2026-01-16.html",
            "docs/library/project/reports/client-profile-optimization/final.md",
            "docs/library/project/reports/client-profile-optimization/patterns.md",
            "docs/library/project/reports/client-profile-optimization/sources.md",
            "docs/library/project/reports/client-profile-optimization/step-back.md",
            "docs/library/project/reports/client-profile-optimization/synthesis.md",
            "docs/library/project/reports/hotelrunner-demo/Nouveau.md",
            "docs/library/project/reports/hotelrunner-demo/blocage-prix-booking.md",
            "docs/library/project/reports/hotelrunner-demo/rapport-demo-20-dec-2025.md",
            "docs/library/project/reports/pm-template-selection/final.md",
            "docs/library/project/reports/pm-template-selection/patterns.md",
            "docs/library/project/reports/pm-template-selection/project_standards.md",
            "docs/library/project/reports/pm-template-selection/prompt-en.md",
            "docs/library/project/reports/pm-template-selection/prompt.md",
            "docs/library/project/reports/pm-template-selection/sources.md",
            "docs/library/project/reports/pm-template-selection/step-back.md",
            "docs/library/project/reports/pm-template-selection/synthesis.md",
            "docs/library/project/reports/pricing-strategy-session/audit-promotions-booking.md",
            "docs/library/project/reports/pricing-strategy-session/execution-log-booking.md",
            "docs/library/project/reports/pricing-strategy-session/execution-log-hotelrunner.md",
            "docs/library/project/reports/pricing-strategy-session/grille-tarifaire-officielle.md",
            "docs/library/project/reports/pricing-strategy-session/plan-promotions-booking.md",
            "docs/library/project/reports/pricing-strategy-session/rapport-promotions-msaid.md",
            "docs/library/project/reports/pricing-strategy-session/rapport-promotions-msaid.pdf",
            "docs/library/project/reports/pricing-strategy-session/rapport-session-20-dec-2025.md",
            "docs/library/project/reports/profile-reorganization/final.md",
            "docs/library/project/reports/profile-reorganization/rdv-prep-agenda.md",
            "docs/library/project/reports/profile-reorganization/rdv-prep-checklist.md",
            "docs/library/project/reports/rapport-audit-v2.md",
            "docs/library/project/reports/verification-promotions-booking/final.md",
            "docs/library/project/reports/verification-promotions-booking/patterns.md",
            "docs/library/project/reports/verification-promotions-booking/sources.md",
            "docs/library/project/reports/verification-promotions-booking/step-back.md",
            "docs/library/project/reports/verification-promotions-booking/synthesis.md",
            "docs/library/project/testing/FINAL-REPORT-2026-01-16.md",
            "docs/library/project/testing/OPTIMIZATION-PLAN.md",
            "docs/library/project/testing/decision-card-001.md",
            "docs/library/project/testing/execution-log-001.md",
            "docs/library/project/testing/execution-log-002.md",
            "docs/library/project/testing/scenarios.md",
        ],
    },
}


# ── Data Structures ──────────────────────────────────────────────────

@dataclass
class MoveAction:
    source: Path
    destination: Path
    category: str
    status: str = "pending"  # pending, copied, verified, skipped, error
    error_msg: str = ""


# ── Core Logic ───────────────────────────────────────────────────────

def compute_destination(source_rel: str, target_dir: str) -> str:
    """
    Compute the destination path, flattening deep nesting while
    preserving the filename.
    """
    return os.path.join(target_dir, Path(source_rel).name)


def resolve_collisions(actions: list[MoveAction]) -> list[MoveAction]:
    """
    If multiple files map to the same destination filename,
    disambiguate by prefixing with parent directory segments.
    Iterates until all destinations are unique.
    """
    max_rounds = 5
    for _ in range(max_rounds):
        dest_groups: dict[str, list[MoveAction]] = {}
        for a in actions:
            key = str(a.destination)
            dest_groups.setdefault(key, []).append(a)

        has_collision = False
        for dest, group in dest_groups.items():
            if len(group) > 1:
                has_collision = True
                for a in group:
                    src_parts = a.source.parts
                    current_dest_name = a.destination.name
                    for i in range(len(src_parts) - 2, -1, -1):
                        candidate = src_parts[i]
                        if candidate not in current_dest_name:
                            new_name = f"{candidate}--{current_dest_name}"
                            a.destination = a.destination.parent / new_name
                            break
                    else:
                        short_hash = hashlib.md5(
                            str(a.source).encode()
                        ).hexdigest()[:6]
                        new_name = f"{short_hash}--{current_dest_name}"
                        a.destination = a.destination.parent / new_name

        if not has_collision:
            break

    return actions


def file_checksum(path: Path) -> str:
    """Compute SHA-256 of a file for verification."""
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(8192), b""):
            h.update(chunk)
    return h.hexdigest()


def build_actions(
    repo_root: Path,
    categories: list[str] | None = None,
    phase: int | None = None,
) -> list[MoveAction]:
    """Build the list of move actions for the specified categories/phase."""
    actions = []

    for cat_name, cat_info in MIGRATION_CATEGORIES.items():
        if phase is not None and cat_info["phase"] != phase:
            continue
        if categories and cat_name not in categories:
            continue

        target_dir = cat_info["target"]
        for rel_path in cat_info["files"]:
            source = repo_root / rel_path
            dest_rel = compute_destination(rel_path, target_dir)
            dest = repo_root / dest_rel
            actions.append(MoveAction(
                source=source,
                destination=dest,
                category=cat_name,
            ))

    return resolve_collisions(actions)


def dry_run(actions: list[MoveAction]) -> str:
    """Generate a dry-run report showing what would happen."""
    lines = []
    lines.append("=" * 70)
    lines.append("  CONTEXT MIGRATION — DRY RUN")
    lines.append("  Taxonomy: source / meta / audit")
    lines.append("=" * 70)
    lines.append("")

    by_cat: dict[str, list[MoveAction]] = {}
    for a in actions:
        by_cat.setdefault(a.category, []).append(a)

    missing = 0
    already_exists = 0
    for cat in sorted(by_cat.keys()):
        group = by_cat[cat]
        target_dir = MIGRATION_CATEGORIES[cat]["target"]
        taxonomy = MIGRATION_CATEGORIES[cat]["taxonomy"]
        phase = MIGRATION_CATEGORIES[cat]["phase"]
        lines.append(f"── P{phase} {taxonomy} → {target_dir}/ ({'─' * 30})")
        lines.append("")
        for a in sorted(group, key=lambda x: str(x.source)):
            if a.destination.exists():
                flag = "⟳ EXISTS"
                already_exists += 1
            elif a.source.exists():
                flag = "✓"
            else:
                flag = "✗ MISSING"
                missing += 1
            lines.append(f"  [{flag}] {a.source}")
            lines.append(f"       → {a.destination}")
        lines.append("")

    total = len(actions)
    ready = total - missing - already_exists
    lines.append(f"Total: {total} files ({ready} ready, {already_exists} already exist, {missing} missing)")
    lines.append("")
    lines.append("To execute: python3 scripts/artifact_migrate.py --execute")
    lines.append("")

    return "\n".join(lines)


def execute_migration(
    actions: list[MoveAction],
    repo_root: Path,
) -> tuple[list[MoveAction], str]:
    """Execute the migration: copy files, verify checksums, log results."""
    log_lines = []
    timestamp = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    log_lines.append(f"# Context Migration Log — {timestamp}")
    log_lines.append("")
    log_lines.append("| Status | Category | Source | Destination |")
    log_lines.append("|--------|----------|--------|-------------|")

    for a in actions:
        if not a.source.exists():
            a.status = "skipped"
            a.error_msg = "source file not found"
            log_lines.append(
                f"| ⚠️ SKIP | {a.category} | `{a.source}` | — (not found) |"
            )
            continue

        if a.destination.exists():
            # Check if it's already the same file
            src_hash = file_checksum(a.source)
            dst_hash = file_checksum(a.destination)
            if src_hash == dst_hash:
                a.status = "verified"
                log_lines.append(
                    f"| ⟳ SAME | {a.category} | `{a.source}` | `{a.destination}` |"
                )
                continue

        try:
            a.destination.parent.mkdir(parents=True, exist_ok=True)
            src_hash = file_checksum(a.source)
            shutil.copy2(a.source, a.destination)
            a.status = "copied"
            dst_hash = file_checksum(a.destination)

            if src_hash == dst_hash:
                a.status = "verified"
                log_lines.append(
                    f"| ✅ OK | {a.category} | `{a.source}` | `{a.destination}` |"
                )
            else:
                a.status = "error"
                a.error_msg = "checksum mismatch"
                log_lines.append(
                    f"| ❌ FAIL | {a.category} | `{a.source}` | checksum mismatch |"
                )

        except Exception as e:
            a.status = "error"
            a.error_msg = str(e)
            log_lines.append(f"| ❌ ERR | {a.category} | `{a.source}` | {e} |")

    verified = sum(1 for a in actions if a.status == "verified")
    skipped = sum(1 for a in actions if a.status == "skipped")
    errors = sum(1 for a in actions if a.status == "error")

    log_lines.append("")
    log_lines.append(f"**Results:** {verified} verified, {skipped} skipped, {errors} errors")
    log_lines.append("")
    log_lines.append(
        "> **Note:** Source files have NOT been deleted. "
        "They remain in their original locations as safe references. "
        "Delete them manually after confirming the migration is correct."
    )

    return actions, "\n".join(log_lines)


# ── CLI ──────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(
        description="Context migration (tri-state lifecycle taxonomy)."
    )
    parser.add_argument(
        "--execute",
        action="store_true",
        help="Actually perform migration (default: dry-run only)",
    )
    parser.add_argument(
        "--category",
        choices=list(MIGRATION_CATEGORIES.keys()),
        help="Migrate only a specific category",
    )
    parser.add_argument(
        "--phase",
        type=int,
        choices=[1, 2],
        help="Migrate only a specific phase (1 or 2)",
    )
    parser.add_argument(
        "--root",
        help="Repository root (default: auto-detect)",
        type=str,
        default=None,
    )
    args = parser.parse_args()

    if args.root:
        repo_root = Path(args.root).resolve()
    else:
        repo_root = Path(__file__).resolve().parent.parent

    if not (repo_root / "AGENTS.md").exists():
        print(f"Error: {repo_root} does not look like the villa-thaifa repo.")
        sys.exit(1)

    categories = [args.category] if args.category else None
    actions = build_actions(repo_root, categories, args.phase)

    if not args.execute:
        report = dry_run(actions)
        print(report)
    else:
        print("Executing context migration...", file=sys.stderr)
        actions, log = execute_migration(actions, repo_root)

        log_path = repo_root / "ops" / "status" / "migration-log.md"
        log_path.write_text(log, encoding="utf-8")
        print(f"Migration log saved to: {log_path}", file=sys.stderr)
        print(log)

        verified = sum(1 for a in actions if a.status == "verified")
        total = len(actions)
        print(
            f"\nDone. {verified}/{total} files migrated.",
            file=sys.stderr,
        )


if __name__ == "__main__":
    main()

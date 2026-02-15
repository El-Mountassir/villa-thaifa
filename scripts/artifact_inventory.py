#!/usr/bin/env python3
"""
Artifact Inventory Scanner for Villa Thaifa Repository.

Walks the repository tree, classifies every file using the tri-state
lifecycle taxonomy (source / meta / audit), and generates a categorized
manifest. Read-only — no files are moved or modified.

Taxonomy:
  source:*  — The product itself (code, config, data)
  meta:*    — What explains the product (planning, architecture, knowledge)
  audit:*   — What proves the product works (quality, history, snapshots)

Usage:
    python scripts/artifact_inventory.py [--output MANIFEST.md]
"""

import argparse
import os
import sys
from collections import defaultdict
from dataclasses import dataclass
from pathlib import Path
from typing import Optional


# ── Category Definitions ────────────────────────────────────────────

CATEGORIES = {
    # Source — the product itself
    "source:implementation": "Scripts, source code, tests",
    "source:configuration":  "Project configuration (pyproject.toml, Makefile, etc.)",
    "source:data":           "Source-of-truth data (rooms, property, etc.)",
    "source:data:pending":   "Data awaiting reconciliation/triage",

    # Meta — what explains the product
    "meta:planning":         "Planning docs, briefs, missions, roadmaps, TODOs",
    "meta:architecture":     "Architecture decisions, decision records (ADRs)",
    "meta:knowledge":        "Knowledge articles, workflows, patterns, research",
    "meta:templates":        "Reusable templates and standards",

    # Audit — what proves the product works
    "audit:quality":         "Reports, audits, test results, isolation snapshots",
    "audit:history":         "Session logs, summaries, handoffs, change logs",
    "audit:snapshot":        "Structure dumps, temporary captures, scratch files",

    # Operational
    "ops:status":            "Operational status and intake tracking",
    "agent:config":          "Agent instructions, contracts, workspace files",
    "content":               "Marketing content, guest-facing material, media refs",
    "client:data":           "Client/stakeholder profiles, communication records",

    # Fallback
    "unknown":               "Unclassified — needs manual review",
}

# Proposed centralized structure for context categories
CENTRALIZED_MAP = {
    "meta:planning":      "context/meta/planning/",
    "meta:architecture":  "context/meta/architecture/",
    "meta:knowledge":     "context/meta/knowledge/",
    "meta:templates":     "context/meta/templates/",
    "audit:quality":      "context/audit/quality/",
    "audit:history":      "context/audit/history/",
    "audit:snapshot":     "context/audit/snapshots/",
}


# ── Skip Patterns ───────────────────────────────────────────────────

SKIP_DIRS = {
    ".git", ".venv", "__pycache__", ".pytest_cache",
    "node_modules", ".secrets", "archives", ".claude",
}


# ── Classification Rules ────────────────────────────────────────────

@dataclass
class FileEntry:
    rel_path: str
    category: str
    size_bytes: int
    suggested_target: Optional[str] = None


def classify_file(rel_path: str, repo_root: Path) -> str:
    """Classify a file based on its path and naming conventions."""
    parts = Path(rel_path).parts
    name = Path(rel_path).name.lower()
    stem = Path(rel_path).stem.lower()
    ext = Path(rel_path).suffix.lower()

    # ── Agent config at root ────────────────────────────────────
    if len(parts) == 1 and name in {
        "agents.md", "claude.md", "gemini.md", "readme.md",
    }:
        return "agent:config"

    # ── Project config at root ──────────────────────────────────
    if len(parts) == 1 and name in {
        "pyproject.toml", "makefile", "uv.lock", ".gitignore",
        "changelog.md",
    }:
        return "source:configuration"

    # ── Root-level snapshots ────────────────────────────────────
    if len(parts) == 1 and ("structure" in stem or "roadmap" in stem):
        return "audit:snapshot"

    # ── data/core/ = canonical ──────────────────────────────────
    if _starts_with(parts, ("data", "core")):
        return "source:data"

    # ── data/pending/ = pending ─────────────────────────────────
    if _starts_with(parts, ("data", "pending")):
        return "source:data:pending"

    # ── ops/ = operational status ───────────────────────────────
    if parts[0] == "ops":
        return "ops:status"

    # ── scripts/, src/, tests/ = code ───────────────────────────
    if parts[0] in {"scripts", "src", "tests"}:
        return "source:implementation"

    # ── specs/ = specifications ─────────────────────────────────
    if parts[0] == "specs":
        return "meta:planning"

    # ── config/ = config ────────────────────────────────────────
    if parts[0] == "config":
        return "source:configuration"

    # ── docs/agents/ = agent config ─────────────────────────────
    if _starts_with(parts, ("docs", "agents")):
        if _any_part(parts, {"templates"}):
            return "meta:templates"
        if _any_part(parts, {"standards"}):
            return "meta:templates"
        if _any_part(parts, {"workflows"}):
            return "meta:knowledge"
        return "agent:config"

    # ── docs/client/ = client data ──────────────────────────────
    if _starts_with(parts, ("docs", "client")):
        return "client:data"

    # ── docs/decisions/ = decisions ──────────────────────────────
    if _starts_with(parts, ("docs", "decisions")):
        return "meta:architecture"

    # ── docs/drafts/ = content drafts ───────────────────────────
    if _starts_with(parts, ("docs", "drafts")):
        return "content"

    # ── docs/content/ = content ─────────────────────────────────
    if _starts_with(parts, ("docs", "content")):
        return "content"

    # ── docs/knowledge/ = knowledge ─────────────────────────────
    if _starts_with(parts, ("docs", "knowledge")):
        return "meta:knowledge"

    # ── docs/management/ ────────────────────────────────────────
    if _starts_with(parts, ("docs", "management")):
        return "meta:planning"

    # ── docs/library/ — the big mixed bag ───────────────────────
    if _starts_with(parts, ("docs", "library")):
        return _classify_library(parts, name, stem)

    # ── docs/ top-level README ──────────────────────────────────
    if _starts_with(parts, ("docs",)) and len(parts) == 2:
        return "agent:config" if name == "readme.md" else "unknown"

    return "unknown"


def _classify_library(parts: tuple, name: str, stem: str) -> str:
    """Sub-classifier for docs/library/ which has the most scattered content."""

    # Known subdirectories
    if _any_part(parts, {"artifacts"}):
        return "audit:quality"

    if _any_part(parts, {"sessions"}):
        return "audit:history"

    if _any_part(parts, {"logs", "changes"}):
        return "audit:history"

    if _any_part(parts, {"meta"}):
        return "audit:history"

    if _any_part(parts, {"state", "baseline", "execution", "history", "planned"}):
        return "audit:snapshot"

    if _any_part(parts, {"knowledge"}):
        return "meta:knowledge"

    if _any_part(parts, {"workflows"}):
        return "meta:knowledge"

    if _any_part(parts, {"patterns"}):
        return "meta:knowledge"

    if _any_part(parts, {"templates"}):
        return "meta:templates"

    if _any_part(parts, {"content"}):
        return "content"

    if _any_part(parts, {"incidents"}):
        return "audit:quality"

    if _any_part(parts, {"alignment"}):
        return "meta:planning"

    if _any_part(parts, {"analysis"}):
        return "audit:quality"

    if _any_part(parts, {"facilities"}):
        return "source:data"

    if _any_part(parts, {"inventory"}):
        return "source:data"

    # docs/library/project/ — large subtree
    if _any_part(parts, {"project"}):
        return _classify_project(parts, name, stem)

    # Loose files in docs/library/
    if "report" in stem or "audit" in stem or "test" in stem or "result" in stem:
        return "audit:quality"
    if "session" in stem or "summary" in stem or "briefing" in stem or "index" in stem:
        return "audit:history"
    if "todo" in stem or "plan" in stem or "mission" in stem or "fiche" in stem:
        return "meta:planning"
    if "sync" in stem or "investigation" in stem:
        return "audit:quality"
    if "lesson" in stem or "overview" in stem:
        return "meta:knowledge"
    if "temporary" in stem or "capture" in stem:
        return "audit:snapshot"
    if "message" in stem:
        return "content"
    if "testimonial" in stem or "transport" in stem or "guest" in stem:
        return "content"
    if "reprise" in stem or "migration" in stem:
        return "meta:planning"
    if stem == "readme":
        return "agent:config"

    # HTML files are typically content
    if name.endswith(".html"):
        return "content"

    return "unknown"


def _classify_project(parts: tuple, name: str, stem: str) -> str:
    """Sub-classifier for docs/library/project/ subtree."""
    if _any_part(parts, {"reports"}):
        return "audit:quality"
    if _any_part(parts, {"planning"}):
        return "meta:planning"
    if _any_part(parts, {"specs"}):
        return "meta:planning"
    if _any_part(parts, {"briefs"}):
        return "meta:planning"
    if _any_part(parts, {"operations"}):
        return "meta:planning"
    if _any_part(parts, {"onboarding"}):
        return "meta:knowledge"
    if _any_part(parts, {"communication"}):
        return "content"
    if _any_part(parts, {"testing"}):
        return "audit:quality"
    if _any_part(parts, {"standards"}):
        return "meta:templates"
    if _any_part(parts, {"templates"}):
        return "meta:templates"
    if _any_part(parts, {"audit"}):
        return "audit:quality"
    if _any_part(parts, {"meta"}):
        return "audit:history"
    if _any_part(parts, {"legacy"}):
        return "audit:snapshot"
    if "brief" in stem:
        return "meta:planning"
    if "readme" in stem:
        return "agent:config"
    if "structure" in stem:
        return "audit:snapshot"
    return "meta:planning"  # default for project docs


# ── Helpers ──────────────────────────────────────────────────────────

def _starts_with(parts: tuple, prefix: tuple) -> bool:
    return parts[:len(prefix)] == prefix


def _any_part(parts: tuple, candidates: set) -> bool:
    return bool(set(parts) & candidates)


# ── Scanner ──────────────────────────────────────────────────────────

def scan_repo(repo_root: Path) -> list[FileEntry]:
    """Walk the repo tree and classify every file."""
    entries = []

    for dirpath, dirnames, filenames in os.walk(repo_root):
        # Prune skipped directories
        dirnames[:] = [d for d in dirnames if d not in SKIP_DIRS]
        dirnames.sort()

        for fname in sorted(filenames):
            full_path = Path(dirpath) / fname
            rel_path = str(full_path.relative_to(repo_root))

            try:
                size = full_path.stat().st_size
            except OSError:
                size = 0

            category = classify_file(rel_path, repo_root)
            suggested = CENTRALIZED_MAP.get(category)

            entries.append(FileEntry(
                rel_path=rel_path,
                category=category,
                size_bytes=size,
                suggested_target=suggested,
            ))

    return entries


# ── Report Generator ─────────────────────────────────────────────────

def generate_manifest(entries: list[FileEntry]) -> str:
    """Generate a Markdown manifest from classified entries."""
    lines = []
    lines.append("# Artifact Inventory Manifest")
    lines.append("")
    lines.append(f"_Generated: {_now()}_")
    lines.append(f"_Total files scanned: {len(entries)}_")
    lines.append(f"_Taxonomy: Tri-State Lifecycle (source / meta / audit)_")
    lines.append("")

    # ── Summary table ───────────────────────────────────────────
    by_cat = defaultdict(list)
    for e in entries:
        by_cat[e.category].append(e)

    lines.append("## Summary")
    lines.append("")
    lines.append("| Category | Count | Total Size | Centralizable? |")
    lines.append("|---|---:|---:|:---:|")

    for cat in sorted(by_cat.keys()):
        files = by_cat[cat]
        total_size = sum(f.size_bytes for f in files)
        centralizable = "✅" if cat in CENTRALIZED_MAP else "—"
        lines.append(
            f"| `{cat}` | {len(files)} | {_fmt_size(total_size)} | {centralizable} |"
        )

    context_entries = [e for e in entries if e.category in CENTRALIZED_MAP]
    lines.append("")
    lines.append(
        f"**Total context files (meta + audit): {len(context_entries)}** "
        f"(out of {len(entries)} total)"
    )
    lines.append("")

    # ── Detailed listings per centralizable category ────────────
    lines.append("---")
    lines.append("")
    lines.append("## Context Files — Candidates for `context/`")
    lines.append("")

    for cat in sorted(CENTRALIZED_MAP.keys()):
        if cat not in by_cat:
            continue
        files = by_cat[cat]
        target = CENTRALIZED_MAP[cat]

        lines.append(f"### {cat}")
        lines.append(f"_Target: `{target}`_")
        lines.append("")
        for f in sorted(files, key=lambda x: x.rel_path):
            lines.append(f"- `{f.rel_path}` ({_fmt_size(f.size_bytes)})")
        lines.append("")

    # ── Non-centralizable categories (for reference) ────────────
    lines.append("---")
    lines.append("")
    lines.append("## Source & Operational Files (Stay in Place)")
    lines.append("")

    for cat in sorted(by_cat.keys()):
        if cat in CENTRALIZED_MAP:
            continue
        files = by_cat[cat]
        lines.append(f"### {cat}")
        lines.append(f"_{CATEGORIES.get(cat, '')}_")
        lines.append("")
        for f in sorted(files, key=lambda x: x.rel_path):
            lines.append(f"- `{f.rel_path}`")
        lines.append("")

    # ── Proposed centralized structure ──────────────────────────
    lines.append("---")
    lines.append("")
    lines.append("## Proposed Centralized Structure")
    lines.append("")
    lines.append("```")
    lines.append("context/")
    lines.append("├── meta/")

    meta_targets = sorted(
        {v for k, v in CENTRALIZED_MAP.items() if k.startswith("meta:")}
    )
    for t in meta_targets:
        subdir = t.replace("context/meta/", "│   ├── ")
        cat_name = [k for k, v in CENTRALIZED_MAP.items() if v == t][0]
        count = len(by_cat.get(cat_name, []))
        lines.append(f"{subdir.rstrip('/')}/ ({count} files)")

    lines.append("└── audit/")
    audit_targets = sorted(
        {v for k, v in CENTRALIZED_MAP.items() if k.startswith("audit:")}
    )
    for t in audit_targets:
        subdir = t.replace("context/audit/", "    ├── ")
        cat_name = [k for k, v in CENTRALIZED_MAP.items() if v == t][0]
        count = len(by_cat.get(cat_name, []))
        lines.append(f"{subdir.rstrip('/')}/ ({count} files)")

    lines.append("```")
    lines.append("")

    return "\n".join(lines)


def _fmt_size(size_bytes: int) -> str:
    if size_bytes < 1024:
        return f"{size_bytes} B"
    elif size_bytes < 1024 * 1024:
        return f"{size_bytes / 1024:.1f} KB"
    else:
        return f"{size_bytes / (1024 * 1024):.1f} MB"


def _now() -> str:
    from datetime import datetime, timezone
    return datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")


# ── CLI ──────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(
        description="Scan Villa Thaifa repo and generate artifact inventory."
    )
    parser.add_argument(
        "--output", "-o",
        help="Write manifest to a file (default: stdout)",
        type=str,
        default=None,
    )
    parser.add_argument(
        "--root",
        help="Repository root directory (default: auto-detect)",
        type=str,
        default=None,
    )
    args = parser.parse_args()

    # Auto-detect repo root
    if args.root:
        repo_root = Path(args.root).resolve()
    else:
        repo_root = Path(__file__).resolve().parent.parent

    if not (repo_root / "AGENTS.md").exists():
        print(f"Error: {repo_root} does not look like the villa-thaifa repo.")
        print("Use --root to specify the repository root.")
        sys.exit(1)

    print(f"Scanning {repo_root} ...", file=sys.stderr)
    entries = scan_repo(repo_root)

    manifest = generate_manifest(entries)

    if args.output:
        output_path = Path(args.output)
        output_path.write_text(manifest, encoding="utf-8")
        print(f"Manifest written to {output_path}", file=sys.stderr)
    else:
        print(manifest)

    # Quick stats to stderr
    context_count = sum(
        1 for e in entries if e.category in CENTRALIZED_MAP
    )
    print(
        f"\nDone. {len(entries)} files scanned, "
        f"{context_count} context files identified.",
        file=sys.stderr,
    )


if __name__ == "__main__":
    main()

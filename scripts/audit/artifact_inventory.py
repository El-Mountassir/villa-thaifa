#!/usr/bin/env python3
"""
Artifact Inventory Scanner for Villa Thaifa Repository.

Walks the repository tree, classifies every file using rules from
config/artifact-rules.yaml, and generates a categorized manifest.
Read-only — no files are moved or modified.

Usage:
    python scripts/artifact_inventory.py [--output MANIFEST.md] [--config RULES.yaml]
"""

import argparse
import fnmatch
import os
import sys
from collections import defaultdict
from dataclasses import dataclass, field
from pathlib import Path
from typing import Optional

import yaml


@dataclass
class Rule:
    pattern: str
    category: str


@dataclass
class FileEntry:
    rel_path: str
    category: str
    size_bytes: int
    suggested_target: Optional[str] = None


@dataclass
class Config:
    taxonomy: dict[str, str] = field(default_factory=dict)
    skip_dirs: set[str] = field(default_factory=set)
    rules: list[Rule] = field(default_factory=list)
    centralized_map: dict[str, str] = field(default_factory=dict)


DEFAULT_CONFIG = Config(
    taxonomy={
        "source:implementation": "Scripts, source code, tests",
        "source:configuration": "Project configuration",
        "source:data": "Canonical source-of-truth data",
        "source:data:pending": "Data awaiting reconciliation",
        "meta:planning": "Planning docs, briefs, roadmaps",
        "meta:architecture": "Architecture decisions, ADRs",
        "meta:knowledge": "Knowledge articles, workflows, patterns",
        "meta:templates": "Reusable templates and standards",
        "audit:quality": "Reports, audits, test results",
        "audit:history": "Session logs, summaries, change logs",
        "audit:snapshot": "Structure dumps, temporary captures",
        "ops:status": "Operational status and intake",
        "agent:config": "Agent instructions, workspace files",
        "content": "Guest-facing material, media",
        "client:data": "Client profiles, communications",
        "unknown": "Needs manual review",
    },
    skip_dirs={
        ".git",
        ".venv",
        "__pycache__",
        ".pytest_cache",
        "node_modules",
        ".secrets",
        "archives",
        ".claude",
    },
    rules=[
        Rule("AGENTS.md", "agent:config"),
        Rule("README.md", "agent:config"),
        Rule("*.toml", "source:configuration"),
        Rule("Makefile", "source:configuration"),
        Rule("*.lock", "source:configuration"),
        Rule(".gitignore", "source:configuration"),
        Rule("context/meta/planning/**", "meta:planning"),
        Rule("context/meta/architecture/**", "meta:architecture"),
        Rule("context/meta/knowledge/**", "meta:knowledge"),
        Rule("context/meta/templates/**", "meta:templates"),
        Rule("context/audit/quality/**", "audit:quality"),
        Rule("context/audit/history/**", "audit:history"),
        Rule("context/audit/snapshots/**", "audit:snapshot"),
        Rule("data/core/**", "source:data"),
        Rule("data/pending/**", "source:data:pending"),
        Rule("scripts/**", "source:implementation"),
        Rule("src/**", "source:implementation"),
        Rule("tests/**", "source:implementation"),
        Rule("config/**", "source:configuration"),
        Rule("ops/**", "ops:status"),
        Rule("docs/agents/**", "agent:config"),
        Rule("docs/client/**", "client:data"),
        Rule("docs/content/**", "content"),
        Rule("docs/drafts/**", "content"),
        Rule("~ADR~", "meta:architecture"),
    ],
    centralized_map={
        "meta:planning": "context/meta/planning/",
        "meta:architecture": "context/meta/architecture/",
        "meta:knowledge": "context/meta/knowledge/",
        "meta:templates": "context/meta/templates/",
        "audit:quality": "context/audit/quality/",
        "audit:history": "context/audit/history/",
        "audit:snapshot": "context/audit/snapshots/",
    },
)


def load_config(config_path: Optional[Path]) -> Config:
    """Load configuration from YAML file, falling back to defaults."""
    if config_path and config_path.exists():
        with open(config_path, "r", encoding="utf-8") as f:
            data = yaml.safe_load(f) or {}

        taxonomy = data.get("taxonomy", {})
        skip_dirs = set(data.get("skip_dirs", []))
        centralized_map = data.get("centralized_map", {})

        rules = []
        for r in data.get("rules", []):
            if "match" in r and "category" in r:
                rules.append(Rule(pattern=r["match"], category=r["category"]))

        return Config(
            taxonomy=taxonomy or DEFAULT_CONFIG.taxonomy,
            skip_dirs=skip_dirs or DEFAULT_CONFIG.skip_dirs,
            rules=rules or DEFAULT_CONFIG.rules,
            centralized_map=centralized_map or DEFAULT_CONFIG.centralized_map,
        )

    return DEFAULT_CONFIG


def match_pattern(rel_path: str, pattern: str) -> bool:
    """
    Match a file path against a pattern.

    Pattern types:
      - "path/prefix/**"  → path starts with prefix (any depth)
      - "*.ext"           → filename glob match
      - "exact.name"      → exact filename match
      - "~stem~"          → stem contains the text between tildes
    """
    name = Path(rel_path).name
    stem = Path(rel_path).stem

    # Stem contains pattern: ~TEXT~
    if pattern.startswith("~") and pattern.endswith("~"):
        needle = pattern[1:-1].lower()
        return needle in stem.lower()

    # Path prefix: path/** or path/*/sub/**
    if pattern.endswith("/**"):
        prefix = pattern[:-3]
        path_normalized = rel_path.replace("\\", "/")
        return path_normalized.startswith(prefix) or path_normalized.startswith(
            prefix + "/"
        )

    # Glob on filename
    if "/" not in pattern and ("*" in pattern or "?" in pattern):
        return fnmatch.fnmatch(name, pattern)

    # Exact filename match
    if "/" not in pattern:
        return name == pattern

    return False


def classify_file(rel_path: str, config: Config) -> str:
    """Classify a file using the loaded rules (first match wins)."""
    for rule in config.rules:
        if match_pattern(rel_path, rule.pattern):
            return rule.category
    return "unknown"


def scan_repo(repo_root: Path, config: Config) -> list[FileEntry]:
    """Walk the repo tree and classify every file."""
    entries = []

    for dirpath, dirnames, filenames in os.walk(repo_root):
        dirnames[:] = [d for d in dirnames if d not in config.skip_dirs]
        dirnames.sort()

        for fname in sorted(filenames):
            full_path = Path(dirpath) / fname
            rel_path = str(full_path.relative_to(repo_root))

            try:
                size = full_path.stat().st_size
            except OSError:
                size = 0

            category = classify_file(rel_path, config)
            suggested = config.centralized_map.get(category)

            entries.append(
                FileEntry(
                    rel_path=rel_path,
                    category=category,
                    size_bytes=size,
                    suggested_target=suggested,
                )
            )

    return entries


def generate_manifest(entries: list[FileEntry], config: Config) -> str:
    """Generate a Markdown manifest from classified entries."""
    lines = [
        "# Artifact Inventory Manifest",
        "",
        f"_Generated: {_now()}_",
        f"_Total files scanned: {len(entries)}_",
        "",
    ]

    by_cat: dict[str, list[FileEntry]] = defaultdict(list)
    for e in entries:
        by_cat[e.category].append(e)

    lines.extend(
        [
            "## Summary",
            "",
            "| Category | Count | Total Size | Centralizable? |",
            "|---|---:|---:|:---:|",
        ]
    )

    for cat in sorted(by_cat.keys()):
        files = by_cat[cat]
        total_size = sum(f.size_bytes for f in files)
        centralizable = "✅" if cat in config.centralized_map else "—"
        lines.append(
            f"| `{cat}` | {len(files)} | {_fmt_size(total_size)} | {centralizable} |"
        )

    context_entries = [e for e in entries if e.category in config.centralized_map]
    lines.extend(
        [
            "",
            f"**Context files (meta + audit): {len(context_entries)}** / {len(entries)} total",
            "",
            "---",
            "",
            "## Context Files — Candidates for `context/`",
            "",
        ]
    )

    for cat in sorted(config.centralized_map.keys()):
        if cat not in by_cat:
            continue
        files = by_cat[cat]
        target = config.centralized_map[cat]
        lines.extend(
            [
                f"### {cat}",
                f"_Target: `{target}`_",
                "",
            ]
        )
        for f in sorted(files, key=lambda x: x.rel_path):
            lines.append(f"- `{f.rel_path}` ({_fmt_size(f.size_bytes)})")
        lines.append("")

    lines.extend(
        [
            "---",
            "",
            "## Other Files",
            "",
        ]
    )

    for cat in sorted(by_cat.keys()):
        if cat in config.centralized_map:
            continue
        files = by_cat[cat]
        desc = config.taxonomy.get(cat, "")
        lines.extend(
            [
                f"### {cat}",
                f"_{desc}_" if desc else "",
                "",
            ]
        )
        for f in sorted(files, key=lambda x: x.rel_path):
            lines.append(f"- `{f.rel_path}`")
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


def main():
    parser = argparse.ArgumentParser(
        description="Scan repository and generate artifact inventory."
    )
    parser.add_argument(
        "--output",
        "-o",
        help="Write manifest to file (default: stdout)",
        type=str,
        default=None,
    )
    parser.add_argument(
        "--root",
        help="Repository root directory (default: auto-detect)",
        type=str,
        default=None,
    )
    parser.add_argument(
        "--config",
        "-c",
        help="Path to artifact-rules.yaml (default: config/artifact-rules.yaml)",
        type=str,
        default=None,
    )
    args = parser.parse_args()

    if args.root:
        repo_root = Path(args.root).resolve()
    else:
        repo_root = Path(__file__).resolve().parent.parent

    config_path: Optional[Path] = None
    if args.config:
        config_path = Path(args.config)
    elif (repo_root / "config" / "artifact-rules.yaml").exists():
        config_path = repo_root / "config" / "artifact-rules.yaml"

    config = load_config(config_path)

    print(f"Scanning {repo_root} ...", file=sys.stderr)
    if config_path:
        print(f"Using config: {config_path}", file=sys.stderr)

    entries = scan_repo(repo_root, config)
    manifest = generate_manifest(entries, config)

    if args.output:
        output_path = Path(args.output)
        output_path.write_text(manifest, encoding="utf-8")
        print(f"Manifest written to {output_path}", file=sys.stderr)
    else:
        print(manifest)

    context_count = sum(1 for e in entries if e.category in config.centralized_map)
    unknown_count = sum(1 for e in entries if e.category == "unknown")
    print(
        f"\nDone. {len(entries)} files: {context_count} context, {unknown_count} unknown",
        file=sys.stderr,
    )


if __name__ == "__main__":
    main()

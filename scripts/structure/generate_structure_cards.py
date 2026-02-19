#!/usr/bin/env python3
"""
Generate role-based structure cards for Villa Thaifa codebase.

This script reads agent definitions and role mappings to produce
token-efficient structure cards that highlight relevant paths for each role.

Usage:
    python scripts/structure/generate_structure_cards.py [--role ROLE] [--all]

Outputs:
    docs/core/STRUCTURE-card-{role}.md for each defined role
"""

import argparse
import re
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import yaml

# Repository root (assuming script is in scripts/structure/)
REPO_ROOT = Path(__file__).parent.parent.parent
AGENTS_DIR = REPO_ROOT / ".claude" / "agents"
MAPPINGS_FILE = REPO_ROOT / "scripts" / "structure" / "role_mappings.yaml"
OUTPUT_DIR = REPO_ROOT / "docs" / "core"


def load_role_mappings() -> dict[str, Any]:
    """Load role-to-path mappings from YAML file."""
    if not MAPPINGS_FILE.exists():
        raise FileNotFoundError(f"Role mappings file not found: {MAPPINGS_FILE}")

    with open(MAPPINGS_FILE, encoding="utf-8") as f:
        return yaml.safe_load(f)


def extract_paths_from_agent(agent_file: Path) -> list[str]:
    """
    Extract file paths mentioned in an agent markdown file.

    Looks for:
    - Markdown links: [text](path)
    - Code blocks with file paths
    - Quoted paths
    """
    if not agent_file.exists():
        return []

    content = agent_file.read_text(encoding="utf-8")
    paths = set()

    # Pattern for markdown links with file paths
    link_pattern = r'\[[^\]]+\]\(([^)]+)\)'
    for match in re.finditer(link_pattern, content):
        path = match.group(1)
        if not path.startswith('http') and not path.startswith('#'):
            paths.add(path)

    # Pattern for quoted file paths (common in agent instructions)
    quoted_path_pattern = r'["\`]([^"\`\s]+\.[a-z]+)["\`]'
    for match in re.finditer(quoted_path_pattern, content, re.IGNORECASE):
        path = match.group(1)
        if '/' in path or path.startswith('data/') or path.startswith('context/'):
            paths.add(path)

    return sorted(paths)


def count_files_in_path(path_pattern: str, repo_root: Path) -> dict[str, int]:
    """
    Count files matching a path pattern.

    Returns dict with 'files' and 'dirs' counts.
    """
    # Handle glob patterns
    if '*' in path_pattern:
        base_path = repo_root
        for part in path_pattern.split('/')[:3]:
            if '*' not in part:
                base_path = base_path / part

        if base_path.exists():
            files = list(base_path.rglob('*'))
            return {
                'files': len([f for f in files if f.is_file()]),
                'dirs': len([f for f in files if f.is_dir()])
            }
        return {'files': 0, 'dirs': 0}

    # Direct path
    full_path = repo_root / path_pattern
    if not full_path.exists():
        return {'files': 0, 'dirs': 0}

    if full_path.is_file():
        return {'files': 1, 'dirs': 0}

    files = list(full_path.rglob('*'))
    return {
        'files': len([f for f in files if f.is_file()]),
        'dirs': len([f for f in files if f.is_dir()])
    }


def should_ignore_path(path: str, ignore_patterns: list[str]) -> bool:
    """Check if a path matches any ignore pattern."""
    for pattern in ignore_patterns:
        # Convert glob pattern to regex
        regex_pattern = pattern.replace('*', '.*').replace('?', '.')
        if re.search(regex_pattern, path):
            return True
    return False


def generate_structure_card(
    role_name: str,
    role_config: dict[str, Any],
    repo_root: Path
) -> str:
    """Generate a structure card markdown for a specific role."""
    lines = [
        f"# Structure Card: {role_name}",
        "",
        f"> Role: {role_config.get('description', 'No description')}",
        "",
        f"_Generated: {datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M UTC')}_",
        "",
        "---",
        "",
        "## Critical Paths",
        "",
        "Paths essential for this role:",
        "",
    ]

    critical_paths = role_config.get('critical', [])
    for path in critical_paths:
        counts = count_files_in_path(path, repo_root)
        file_count = counts['files']
        if file_count > 0:
            lines.append(f"- `{path}` ({file_count} files)")
        else:
            lines.append(f"- `{path}`")

    lines.extend([
        "",
        "## Reference Paths",
        "",
        "Useful context (read as needed):",
        "",
    ])

    reference_paths = role_config.get('reference', [])
    for path in reference_paths:
        counts = count_files_in_path(path, repo_root)
        file_count = counts['files']
        if file_count > 0:
            lines.append(f"- `{path}` ({file_count} files)")
        else:
            lines.append(f"- `{path}`")

    ignore_patterns = role_config.get('ignore', [])
    if ignore_patterns:
        lines.extend([
            "",
            "## Ignored Paths",
            "",
            "Not relevant for this role:",
            "",
        ])
        for pattern in ignore_patterns:
            lines.append(f"- `{pattern}`")

    # Add quick reference section
    lines.extend([
        "",
        "---",
        "",
        "## Quick Commands",
        "",
        "```bash",
        f"# View critical structure for {role_name}",
        f"tree -L 3 {' '.join([p for p in critical_paths[:3]])}",
        "",
        "# Find specific file",
        "find . -name 'pattern' -type f",
        "```",
        "",
        "---",
        "",
        f"_Auto-generated by `scripts/structure/generate_structure_cards.py`_",
    ])

    return '\n'.join(lines)


def main():
    parser = argparse.ArgumentParser(
        description="Generate role-based structure cards"
    )
    parser.add_argument(
        '--role',
        type=str,
        help='Generate card for specific role only'
    )
    parser.add_argument(
        '--all',
        action='store_true',
        help='Generate cards for all defined roles'
    )
    parser.add_argument(
        '--dry-run',
        action='store_true',
        help='Print output without writing files'
    )

    args = parser.parse_args()

    # Load role mappings
    try:
        mappings = load_role_mappings()
    except FileNotFoundError as e:
        print(f"Error: {e}")
        return 1

    # Determine which roles to process
    if args.role:
        if args.role not in mappings:
            print(f"Error: Role '{args.role}' not found in mappings")
            print(f"Available roles: {', '.join(mappings.keys())}")
            return 1
        roles_to_process = {args.role: mappings[args.role]}
    elif args.all:
        roles_to_process = mappings
    else:
        # Default: process all
        roles_to_process = mappings

    # Generate cards
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    for role_name, role_config in roles_to_process.items():
        card_content = generate_structure_card(role_name, role_config, REPO_ROOT)

        if args.dry_run:
            print(f"\n{'='*60}")
            print(f"Structure Card: {role_name}")
            print('='*60)
            print(card_content)
            continue

        output_file = OUTPUT_DIR / f"STRUCTURE-card-{role_name}.md"
        output_file.write_text(card_content, encoding='utf-8')
        print(f"Generated: {output_file.relative_to(REPO_ROOT)}")

    return 0


if __name__ == "__main__":
    exit(main())

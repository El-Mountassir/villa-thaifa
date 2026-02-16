#!/usr/bin/env python3
"""Check if source markdown still contains room-scoped values missing from canonical markdown.

Usage:
    uv run python scripts/check_unique_info.py --source path --canonical path
"""

from __future__ import annotations

from pathlib import Path
import argparse
import re
import sys
import unicodedata

ROOM_HEADING_PATTERNS = [
    re.compile(r"^###\s+R(?P<num>\d{2})\b", flags=re.I),
    re.compile(r"^###\s+\[(?P<num>\d{2})\]\b", flags=re.I),
]
STOP_WORDS = {
    "x",
    "cm",
    "and",
    "with",
    "the",
    "de",
    "du",
    "des",
    "et",
    "a",
}


def strip_accents(text: str) -> str:
    return "".join(ch for ch in unicodedata.normalize("NFKD", text) if not unicodedata.combining(ch))


def normalize_text(text: str) -> str:
    s = strip_accents(text.lower())
    s = s.replace("**", "")

    aliases = [
        (r"\brez[\s-]*de[\s-]*chaussee\b", "ground floor"),
        (r"\brdc\b", "ground floor"),
        (r"\b1er\s+etage\b", "first floor"),
        (r"\b1er\b", "first floor"),
        (r"\bpiscine\b", "pool"),
        (r"\bjardin\b", "garden"),
        (r"\bcanape[\s-]*lit(s)?\b", "sofa bed"),
        (r"\blit\s+king\b", "king"),
        (r"\bpersons?\b", "adults"),
        (r"\bm2\b", "m²"),
        (r"\bacces\b", "access"),
    ]
    for pattern, repl in aliases:
        s = re.sub(pattern, repl, s)

    s = re.sub(r"\b(\d+)\s*x\s*(king|sofa\s*bed)s?\b", r"\1 \2", s)
    s = re.sub(r"\bsofa\s*beds\b", "sofa bed", s)
    s = re.sub(r"(\d+)\s*m2", r"\1 m2", s)
    s = re.sub(r"(\d+)m2", r"\1 m2", s)
    s = re.sub(r"\bm2\b", "m²", s)
    s = re.sub(r"(\d+)\s*m²", r"\1 m²", s)
    s = re.sub(r"(\d+)m²", r"\1 m²", s)
    s = s.replace("m²", " m² ")
    s = re.sub(r"[()\[\]{}]", " ", s)
    s = re.sub(r"\s+", " ", s)
    return s.strip(" .:-")


def parse_room_id_from_heading(line: str) -> str | None:
    for pattern in ROOM_HEADING_PATTERNS:
        match = pattern.search(line.strip())
        if match:
            return f"R{match.group('num')}"
    return None


def parse_room_id_from_table_cell(cell: str) -> str | None:
    raw = normalize_text(cell)
    if not raw:
        return None

    m_r = re.search(r"\br(?P<num>\d{2})\b", raw)
    if m_r:
        return f"R{m_r.group('num')}"

    m_n = re.search(r"\b(?P<num>0[1-9]|1[0-2])\b", raw)
    if m_n:
        return f"R{m_n.group('num')}"

    return None


def value_parts(value: str, include_full: bool) -> set[str]:
    full = normalize_text(value)
    if not full or full == "-":
        return set()

    parts: set[str] = set()
    if include_full:
        parts.add(full)

    for piece in re.split(r"[;,|+/]", full):
        p = piece.strip(" .:-")
        if len(p) >= 3 and p != "-":
            parts.add(p)

    return parts


def extract_room_tokens(text: str) -> dict[str, set[str]]:
    tokens: dict[str, set[str]] = {}
    current_room: str | None = None

    for raw in text.splitlines():
        line = raw.strip()
        if not line:
            continue

        heading_room = parse_room_id_from_heading(line)
        if heading_room:
            current_room = heading_room
            tokens.setdefault(current_room, set())
            continue

        if line.startswith("###"):
            current_room = None
            continue

        if line.startswith("|"):
            cells = [c.strip() for c in line.split("|")[1:-1]]
            if not cells:
                continue
            first = normalize_text(cells[0])
            if first in {"room id", "id"}:
                continue
            if set(first) <= {"-", " "}:
                continue

            row_room = parse_room_id_from_table_cell(cells[0])
            if not row_room:
                continue

            row_set = tokens.setdefault(row_room, set())
            for cell in cells[1:]:
                row_set.update(value_parts(cell, include_full=False))
            continue

        if current_room and line.startswith("- **") and ":" in line:
            _, value = line.split(":", 1)
            tokens[current_room].update(value_parts(value, include_full=True))

    return tokens


def words(token: str) -> set[str]:
    out = set(re.findall(r"[a-z0-9²]+", token))
    return {w for w in out if w not in STOP_WORDS}


def token_matches(source_token: str, canonical_token: str) -> bool:
    if source_token == canonical_token:
        return True
    if len(source_token) >= 4 and source_token in canonical_token:
        return True

    src_words = words(source_token)
    can_words = words(canonical_token)
    return bool(src_words) and src_words <= can_words


def find_missing(source_by_room: dict[str, set[str]], canonical_by_room: dict[str, set[str]]) -> list[str]:
    missing: list[str] = []

    for room_id in sorted(source_by_room):
        source_tokens = source_by_room.get(room_id, set())
        canonical_tokens = canonical_by_room.get(room_id, set())
        room_word_union: set[str] = set()
        for can in canonical_tokens:
            room_word_union.update(words(can))

        for src in sorted(source_tokens):
            if any(token_matches(src, can) for can in canonical_tokens):
                continue

            src_words = words(src)
            if src_words and src_words <= room_word_union:
                continue

            missing.append(f"{room_id}|{src}")

    return missing


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--source", required=True)
    parser.add_argument("--canonical", required=True)
    args = parser.parse_args()

    src = Path(args.source)
    can = Path(args.canonical)
    if not src.exists() or not can.exists():
        print("ERROR: source or canonical path missing")
        return 1

    source_by_room = extract_room_tokens(src.read_text(encoding="utf-8"))
    canonical_by_room = extract_room_tokens(can.read_text(encoding="utf-8"))
    source_count = sum(len(v) for v in source_by_room.values())
    canonical_count = sum(len(v) for v in canonical_by_room.values())
    missing = find_missing(source_by_room, canonical_by_room)

    print(f"SOURCE: {src}")
    print(f"CANONICAL: {can}")
    print(f"SOURCE_TOKENS: {source_count}")
    print(f"CANONICAL_TOKENS: {canonical_count}")
    print(f"MISSING_TOKENS: {len(missing)}")

    for token in missing[:120]:
        print(f"- {token}")

    return 0 if not missing else 2


if __name__ == "__main__":
    sys.exit(main())

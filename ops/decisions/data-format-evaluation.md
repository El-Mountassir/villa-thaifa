# Data Format Evaluation — Room Profiles

**Date**: 2026-02-22
**Author**: Nova (evaluation agent)
**Trigger**: Omar requested a comprehensive format decision before any structural changes to room profile data
**Status**: DECISION PENDING — Omar review required

---

## Table of Contents

- [Data Format Evaluation — Room Profiles](#data-format-evaluation--room-profiles)
  - [Table of Contents](#table-of-contents)
  - [Context \& Requirements](#context--requirements)
    - [Weighted Criteria (for Villa Thaifa)](#weighted-criteria-for-villa-thaifa)
  - [Format Candidates](#format-candidates)
    - [1. JSON](#1-json)
    - [2. YAML / YML](#2-yaml--yml)
    - [3. Pure Markdown](#3-pure-markdown)
    - [4. Markdown + Embedded YAML (current)](#4-markdown--embedded-yaml-current)
    - [5. TOML](#5-toml)
    - [6. CSV](#6-csv)
    - [7. XML](#7-xml)
    - [8. NDJSON / JSONL](#8-ndjson--jsonl)
    - [9. Parquet](#9-parquet)
    - [10. SQLite](#10-sqlite)
    - [11. GraphQL SDL](#11-graphql-sdl)
    - [12. Protocol Buffers](#12-protocol-buffers)
    - [13. XLSX / ODS](#13-xlsx--ods)
  - [Comparison Matrix](#comparison-matrix)
  - [Recommendation for Villa Thaifa](#recommendation-for-villa-thaifa)
    - [Why the current format wins](#why-the-current-format-wins)
    - [One structural improvement to implement](#one-structural-improvement-to-implement)
    - [What to reject and why](#what-to-reject-and-why)
  - [Migration Path](#migration-path)
    - [Current state](#current-state)
    - [Target state](#target-state)
    - [Migration cost](#migration-cost)
    - [Migration trigger](#migration-trigger)
    - [Schema enforcement (post-migration)](#schema-enforcement-post-migration)

---

## Context & Requirements

Villa Thaifa currently stores 12 room profiles as `.md` files with embedded YAML code blocks (NOT frontmatter — the YAML lives inside a fenced code block at the end of each file). Each profile contains:

- **Narrative text**: descriptions, taglines, marketing hooks in EN + FR
- **Structured fields**: price, capacity, bed types, size, view, bathroom, climate
- **OTA-specific fields**: Booking.com titles (FR), Expedia titles (EN), character-limited descriptions
- **Provenance metadata**: source files, confidence level, verification date

### Weighted Criteria (for Villa Thaifa)

| Criterion                 | Weight | Rationale                                                    |
| ------------------------- | ------ | ------------------------------------------------------------ |
| Human readability         | 25%    | Said Thaifa (owner, non-technical) reviews profiles directly |
| Mixed content support     | 20%    | Narrative + structured in same file is a hard requirement    |
| Agent queryability        | 15%    | AI agents must extract fields reliably and predictably       |
| Git friendliness          | 15%    | All changes version-controlled; clean diffs required         |
| Schema enforcement        | 10%    | Field validation prevents silent data drift                  |
| Extensibility             | 10%    | New fields added regularly (mini_bar added 2026-02)          |
| OTA integration readiness | 5%     | Downstream export to Booking.com/Expedia APIs                |

---

## Format Candidates

### 1. JSON

**Overview**: Key-value pairs, arrays, nested objects. The universal interchange format. Strict syntax. No comments. No multiline strings without escaping.

**Pros**:

- Universally parseable by every language and AI agent
- Strict spec = no ambiguity
- Schema enforcement via JSON Schema (Draft 7+)
- Direct OTA API payload format (Booking.com REST API expects JSON)

**Cons**:

- No comments allowed — provenance notes, conflict markers, `owner_pending` rationale disappear
- Multiline narrative text becomes unreadable escaped strings (`"description": "44 m\u00b2 ground-floor...\nFurnished patio access."`)
- No native support for mixed narrative + structured (must pick one or nest awkwardly)
- Trailing comma errors are a common footgun for manual editors
- Said Thaifa cannot meaningfully read or edit a JSON file

**Score**:

| Criterion                 | Score (1-5) |
| ------------------------- | ----------- |
| Human readability         | 2           |
| Agent queryability        | 5           |
| Mixed content support     | 1           |
| Git friendliness          | 3           |
| Schema enforcement        | 5           |
| Extensibility             | 4           |
| OTA integration readiness | 5           |

---

### 2. YAML / YML

**Overview**: Superset of JSON with human-friendly syntax. Supports comments, multiline strings, and complex nesting. Whitespace-significant.

**Pros**:

- Readable by non-technical stakeholders with minimal training
- Native multiline string support (`|` for literal, `>` for folded)
- Comments supported — inline rationale and `owner_pending` notes are possible
- Strong tooling (yamllint, pydantic, jsonschema can validate)
- Clean git diffs (line-per-field)

**Cons**:

- Whitespace-significant = easy to corrupt with copy-paste (indent shifts)
- Norway problem and other YAML footguns (NO parsed as false, ON as true)
- Narrative + structured in one file is possible but looks inconsistent
- YAML-only files lose the visual hierarchy that Markdown headers provide
- Not native OTA format — must transform to JSON for API calls

**Score**:

| Criterion                 | Score (1-5) |
| ------------------------- | ----------- |
| Human readability         | 4           |
| Agent queryability        | 4           |
| Mixed content support     | 3           |
| Git friendliness          | 4           |
| Schema enforcement        | 4           |
| Extensibility             | 5           |
| OTA integration readiness | 3           |

---

### 3. Pure Markdown

**Overview**: Text-first format with lightweight syntax for headers, lists, bold, tables. No native structured data — everything is prose or list items.

**Pros**:

- Maximum human readability — Said can read, edit, and review without training
- Supports narrative, descriptions, and formatted content natively
- Excellent git diffs (line-level changes in prose)
- Renders beautifully in GitHub, Obsidian, any Markdown viewer

**Cons**:

- Zero schema enforcement — nothing prevents missing the `Pricing` field
- AI agents must parse natural language lists, which is fragile and non-deterministic
- No native key-value semantics — `**Pricing**: 169 EUR` is a convention, not a contract
- OTA integration requires NLP extraction (lossy, unreliable)
- No validation tooling — silent data drift is undetectable

**Score**:

| Criterion                 | Score (1-5) |
| ------------------------- | ----------- |
| Human readability         | 5           |
| Agent queryability        | 2           |
| Mixed content support     | 4           |
| Git friendliness          | 5           |
| Schema enforcement        | 1           |
| Extensibility             | 3           |
| OTA integration readiness | 1           |

---

### 4. Markdown + Embedded YAML (current)

**Overview**: Markdown document containing a fenced YAML code block. Narrative content lives in Markdown sections; structured data lives in the YAML block. The current approach used in all 12 room profiles.

**Note on implementation**: Current profiles use embedded YAML code blocks (`yaml ... `) rather than true YAML frontmatter (---...--- at file top). This means the YAML is not parsed by standard frontmatter parsers — it requires explicit extraction of the fenced block.

**Pros**:

- Best of both worlds: human-readable narrative + machine-readable structured data
- Comments and `owner_pending` rationale live naturally in the Markdown prose
- Said can read the profile top-to-bottom and understand it fully
- AI agents can target the YAML block specifically for reliable extraction
- Excellent git diffs — narrative changes and structured changes are visually distinct
- No migration cost — already implemented across all 12 profiles

**Cons**:

- The YAML block is not auto-parsed by frontmatter libraries (requires custom extraction)
- Schema enforcement requires a custom validator (not off-the-shelf)
- Tooling is non-standard — no native IDE schema highlighting for embedded YAML
- Risk of narrative/YAML drift if a field is updated in one place but not the other
- Two sources of truth within one file (Markdown list at top + YAML block at bottom) — they must stay in sync manually

**Score**:

| Criterion                 | Score (1-5) |
| ------------------------- | ----------- |
| Human readability         | 5           |
| Agent queryability        | 4           |
| Mixed content support     | 5           |
| Git friendliness          | 5           |
| Schema enforcement        | 3           |
| Extensibility             | 5           |
| OTA integration readiness | 3           |

---

### 5. TOML

**Overview**: Tom's Obvious Minimal Language. Configuration-file format designed to be unambiguous and human-readable. Common in Rust, Python (pyproject.toml), Hugo.

**Pros**:

- Cleaner and less footgun-prone than YAML (explicit types, no indentation significance)
- Multiline strings supported
- Comments supported
- Excellent for structured config data

**Cons**:

- Poor support for mixed narrative + structured content
- Not widely known outside developer tooling circles — Said cannot read it without training
- No native OTA format — transforms required
- Limited AI tooling awareness compared to JSON/YAML
- Not a natural fit for content-heavy documents with marketing copy

**Score**:

| Criterion                 | Score (1-5) |
| ------------------------- | ----------- |
| Human readability         | 3           |
| Agent queryability        | 4           |
| Mixed content support     | 2           |
| Git friendliness          | 4           |
| Schema enforcement        | 4           |
| Extensibility             | 4           |
| OTA integration readiness | 3           |

---

### 6. CSV

**Overview**: Tabular flat-file format. Each row is one record; columns are fields. No nesting. No narrative text.

**Pros**:

- Universally readable in spreadsheet tools (Excel, Google Sheets)
- Said can open and review in familiar interface
- Simple validation (required columns present, no missing cells)

**Cons**:

- Fundamentally flat — nested data (beds: [{type: king, count: 1}, {type: sofa}]) requires serialization hacks or multiple files
- Multiline text (descriptions, marketing copy) breaks CSV semantics
- No per-record comments or provenance metadata
- One file for all 12 rooms means conflicts in git (multiple agents touching same file)
- Cannot represent mixed narrative + structured content at all

**Score**:

| Criterion                 | Score (1-5) |
| ------------------------- | ----------- |
| Human readability         | 3           |
| Agent queryability        | 3           |
| Mixed content support     | 1           |
| Git friendliness          | 2           |
| Schema enforcement        | 2           |
| Extensibility             | 2           |
| OTA integration readiness | 3           |

---

### 7. XML

**Overview**: eXtensible Markup Language. Hierarchical tag-based format. The predecessor to JSON for data interchange. Verbose but expressive.

**Pros**:

- Full nesting and hierarchy support
- Schema enforcement via XSD or RELAX NG
- Namespace support for OTA standards (OTA Alliance uses XML-based schemas)
- Both structured and narrative content possible (CDATA sections for free text)

**Cons**:

- Extremely verbose — a 40-field room profile becomes 200+ lines of tags
- Not human-readable for non-technical users
- Said would find it completely opaque
- Git diffs are noisy (closing tags on separate lines, attribute quoting)
- Modern OTA APIs (Booking.com, Expedia) have moved to JSON — XML is legacy
- No AI agent tooling advantage over JSON

**Score**:

| Criterion                 | Score (1-5) |
| ------------------------- | ----------- |
| Human readability         | 1           |
| Agent queryability        | 4           |
| Mixed content support     | 3           |
| Git friendliness          | 2           |
| Schema enforcement        | 5           |
| Extensibility             | 3           |
| OTA integration readiness | 2           |

---

### 8. NDJSON / JSONL

**Overview**: One JSON object per line. Used for streaming, log ingestion, and bulk data pipelines. No document structure — just a sequence of records.

**Pros**:

- Easy to append new records (just append a line)
- Streamable and pipeline-friendly
- Each line is independently valid JSON

**Cons**:

- Completely unreadable without tooling — one room profile = one very long line
- No narrative support at all
- Zero human readability
- Git diffs are worst-case: one changed field = entire line rewritten
- Designed for bulk data pipelines, not human-managed records

**Score**:

| Criterion                 | Score (1-5) |
| ------------------------- | ----------- |
| Human readability         | 1           |
| Agent queryability        | 5           |
| Mixed content support     | 1           |
| Git friendliness          | 1           |
| Schema enforcement        | 4           |
| Extensibility             | 3           |
| OTA integration readiness | 4           |

---

### 9. Parquet

**Overview**: Apache columnar binary storage format. Optimized for analytical queries on large datasets. Used in data warehousing (Spark, DuckDB, BigQuery).

**Pros**:

- Extremely fast columnar queries
- Excellent compression
- Schema embedded in file

**Cons**:

- Binary format — completely unreadable and non-editable by humans
- Cannot be version-controlled meaningfully (binary diffs)
- Said cannot open or read it without specialized tooling
- Designed for millions of rows, not 12
- Zero mixed content support
- Not appropriate for a property management system at this scale

**Score**:

| Criterion                 | Score (1-5) |
| ------------------------- | ----------- |
| Human readability         | 1           |
| Agent queryability        | 5           |
| Mixed content support     | 1           |
| Git friendliness          | 1           |
| Schema enforcement        | 5           |
| Extensibility             | 2           |
| OTA integration readiness | 2           |

---

### 10. SQLite

**Overview**: Embedded relational database. Single-file. SQL-queryable. Full ACID transactions. Used in mobile apps, browsers, embedded systems.

**Pros**:

- Full relational model — beds as a separate table with foreign key to rooms
- SQL queries for OTA export, pricing reports, availability checks
- Schema enforcement via table definitions and constraints
- Widely supported — Python, Node, SQLiteOnline, etc.

**Cons**:

- Binary file — git diffs are meaningless (entire file shown as binary changed)
- Said cannot read or edit without a GUI tool (DB Browser, TablePlus)
- Narrative text is awkward in relational cells — descriptions become VARCHAR(500) with no formatting
- Single file = merge conflicts for concurrent edits
- Overkill for 12 rooms — brings database complexity without database-scale benefits
- Literate comments and provenance metadata have no natural home

**Score**:

| Criterion                 | Score (1-5) |
| ------------------------- | ----------- |
| Human readability         | 2           |
| Agent queryability        | 5           |
| Mixed content support     | 2           |
| Git friendliness          | 1           |
| Schema enforcement        | 5           |
| Extensibility             | 4           |
| OTA integration readiness | 4           |

---

### 11. GraphQL SDL

**Overview**: GraphQL Schema Definition Language. Defines types, fields, and relationships. Used to describe API schemas, not store data.

**Pros**:

- Expressive type system with validation
- Human-readable schema definition
- Strong tooling ecosystem

**Cons**:

- SDL is a schema language, not a data storage format — it defines types, not values
- Cannot store actual room profile data (pricing: 169 EUR is not a SDL construct)
- Conflates schema definition with data storage (a category error)
- Would require a separate data layer (JSON, database) to store actual records
- Not appropriate for this use case at all

**Score**:

| Criterion                 | Score (1-5) |
| ------------------------- | ----------- |
| Human readability         | 2           |
| Agent queryability        | 1           |
| Mixed content support     | 1           |
| Git friendliness          | 3           |
| Schema enforcement        | 4           |
| Extensibility             | 3           |
| OTA integration readiness | 1           |

---

### 12. Protocol Buffers

**Overview**: Google's binary serialization format. Schema-first (`.proto` files define types). Used for gRPC APIs and high-performance service communication.

**Pros**:

- Extremely compact binary encoding
- Strong schema enforcement via `.proto` definitions
- Language-agnostic with generated code

**Cons**:

- Binary format — completely unreadable without protoc decode tooling
- No git diff support for the serialized data
- Said cannot interact with it at all
- Designed for high-throughput microservice communication at Google scale
- Zero mixed content support
- Massive toolchain overhead for 12 room profiles

**Score**:

| Criterion                 | Score (1-5) |
| ------------------------- | ----------- |
| Human readability         | 1           |
| Agent queryability        | 4           |
| Mixed content support     | 1           |
| Git friendliness          | 1           |
| Schema enforcement        | 5           |
| Extensibility             | 3           |
| OTA integration readiness | 3           |

---

### 13. XLSX / ODS

**Overview**: Microsoft Excel and LibreOffice Calc spreadsheet formats. Binary (XLSX is zipped XML). Familiar to non-technical users.

**Pros**:

- Said is likely comfortable with spreadsheets
- Tables, multiple sheets, color coding
- Formula support for derived fields (e.g., MAD from EUR auto-calculated)

**Cons**:

- Binary/ZIP format — git diffs are unusable
- Narrative descriptions in cells are severely limited in readability
- Merge conflicts are destructive (binary merge = file corruption)
- No schema enforcement — any value in any cell
- AI agents must use openpyxl or similar to extract — fragile compared to text formats
- No provenance comment system

**Score**:

| Criterion                 | Score (1-5) |
| ------------------------- | ----------- |
| Human readability         | 3           |
| Agent queryability        | 2           |
| Mixed content support     | 2           |
| Git friendliness          | 1           |
| Schema enforcement        | 1           |
| Extensibility             | 3           |
| OTA integration readiness | 2           |

---

## Comparison Matrix

Weights: Human readability (25%), Mixed content (20%), Agent queryability (15%), Git friendliness (15%), Schema enforcement (10%), Extensibility (10%), OTA integration (5%).

| Format                           | Human (×0.25) | Mixed (×0.20) | Agent (×0.15) | Git (×0.15) | Schema (×0.10) | Extend (×0.10) | OTA (×0.05) | **Weighted Score** |
| -------------------------------- | ------------- | ------------- | ------------- | ----------- | -------------- | -------------- | ----------- | ------------------ |
| **MD + embedded YAML (current)** | 5             | 5             | 4             | 5           | 3              | 5              | 3           | **4.50**           |
| YAML only                        | 4             | 3             | 4             | 4           | 4              | 5              | 3           | **3.80**           |
| Pure Markdown                    | 5             | 4             | 2             | 5           | 1              | 3              | 1           | **3.40**           |
| TOML                             | 3             | 2             | 4             | 4           | 4              | 4              | 3           | **3.25**           |
| JSON                             | 2             | 1             | 5             | 3           | 5              | 4              | 5           | **3.00**           |
| SQLite                           | 2             | 2             | 5             | 1           | 5              | 4              | 4           | **2.90**           |
| XML                              | 1             | 3             | 4             | 2           | 5              | 3              | 2           | **2.65**           |
| CSV                              | 3             | 1             | 3             | 2           | 2              | 2              | 3           | **2.25**           |
| XLSX / ODS                       | 3             | 2             | 2             | 1           | 1              | 3              | 2           | **2.10**           |
| NDJSON / JSONL                   | 1             | 1             | 5             | 1           | 4              | 3              | 4           | **2.10**           |
| GraphQL SDL                      | 2             | 1             | 1             | 3           | 4              | 3              | 1           | **1.90**           |
| Protocol Buffers                 | 1             | 1             | 4             | 1           | 5              | 3              | 3           | **2.10**           |
| Parquet                          | 1             | 1             | 5             | 1           | 5              | 2              | 2           | **2.25**           |

---

## Recommendation for Villa Thaifa

**Winner: Markdown + Embedded YAML (current format) — with one structural improvement.**

Score: **4.50 / 5.00** — clear margin over second place (YAML-only at 3.80).

### Why the current format wins

The current format was designed for exactly this problem: human-readable narrative content for a non-technical owner, combined with machine-queryable structured fields for AI agents and OTA exports. No other format in the matrix achieves this combination. The two nearest alternatives fail on key criteria:

- **YAML-only** drops to 3 on Mixed content — you lose the Markdown narrative structure, headers, and prose formatting that makes Said's reading experience coherent.
- **Pure Markdown** drops to 1 on Schema enforcement — without the YAML block, there is no contract, no validation, and no reliable agent extraction.

### One structural improvement to implement

The current implementation embeds YAML inside a fenced code block rather than using YAML frontmatter. This means the YAML is not parsed by standard tooling — it requires custom fenced-block extraction.

**Recommended change**: Migrate from embedded YAML code block to **YAML frontmatter** (--- delimiters at file top). This unlocks:

- Standard frontmatter parsers (python-frontmatter, gray-matter, Hugo, Jekyll, Obsidian)
- Off-the-shelf validation scripts using existing libraries
- Cleaner agent extraction with `python-frontmatter.load()` — no regex fenced-block parsing

**Structure after migration**:

```
---
room_id: R01
category_code: DELUXE_TRIPLE
size_m2: 44
base_rate_eur: 169
beds:
  - type: king
    count: 1
  - type: sofa_bed
    count: 1
# ... all structured fields
---

# R01: Deluxe Triple Room

[Narrative content, OTA fields, provenance — all Markdown]
```

Said reads the document from the first `#` header onward. Agents parse the frontmatter block. Both work independently. No sync risk between two sections containing the same field.

### What to reject and why

- **JSON**: Fails on human readability and mixed content — the two highest-weighted criteria. Said cannot use it.
- **SQLite**: Binary format destroys git workflow. Merge conflicts on a binary file in an AI-agent-heavy workspace are catastrophic.
- **Parquet / Protocol Buffers**: Appropriate for data pipelines at scale. Wrong tool for 12 human-managed profiles.
- **CSV**: Cannot model nested data (beds array) without losing fidelity.
- **XLSX**: Binary + no git diffs + no schema = fails on 3 of 7 criteria.
- **GraphQL SDL**: Category error — it's a schema language, not a data format. Cannot store values.

---

## Migration Path

### Current state

- 12 profiles in `data/rooms/R01/` through `data/rooms/R12/`
- Format: Markdown prose at top + YAML embedded in fenced code block at bottom
- Status: Working, agent-queryable via custom fenced-block extraction

### Target state

- Same 12 files, same content
- Format: YAML frontmatter at top + Markdown prose below
- Status: Parseable by standard frontmatter libraries, same agent and human UX

### Migration cost

**Low.** The YAML content already exists. The migration is mechanical:

1. Extract the YAML block from each file (remove `yaml ... ` fences)
2. Move it to the top of the file with `---` delimiters
3. Remove the now-redundant structured data from the Markdown prose section (the bulleted list at the top duplicates several YAML fields)
4. Update any extraction scripts to use `python-frontmatter` instead of fenced-block regex

**Estimate**: 1 sub-agent task, ~30 minutes. Low risk — git history preserves rollback path.

### Migration trigger

This migration is recommended but **not urgent**. The current format is functional. Migrate when:

- A new validation script is being written (write it for frontmatter from the start)
- A new room profile is being created (create it in frontmatter format)
- OR Omar explicitly prioritizes the migration

### Schema enforcement (post-migration)

With frontmatter in place, add a JSON Schema or Pydantic model defining required fields. Run validation via `make validate-rooms` or as a pre-commit hook. Required fields minimum: `room_id`, `category_code`, `size_m2`, `base_rate_eur`, `capacity`, `beds`, `status`.

---

_Decision record created 2026-02-22. Review with Omar before any migration action._

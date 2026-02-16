# Structure

```sh
# Directories
├── data/         canonical source-of-truth (rooms, finance, pending domains)
├── docs/         operational docs, agent configs, client info, media
│   └── core/     foundational definitions (PRINCIPLES, MISSION, STRUCTURE)
├── context/      reference material — architecture, planning, audits (read-only)
├── ops/          status dashboards, intake queue, migration logs
├── scripts/      validation and tooling utilities
├── tests/        pytest suite
├── logs/         log files
├── .claude/      Claude Code configuration
├── .secrets/     credentials storage

# Root files (MUST stay at root)
├── AGENTS.md     AI agent workspace contract
├── CLAUDE.md     Claude Code project instructions
├── GEMINI.md     Gemini AI project instructions
├── README.md     Repository documentation
├── CHANGELOG.md  Version history
├── Makefile      build and convenience tasks
├── pyproject.toml Python project config
├── uv.lock       dependency lock file
├── .gitignore    git ignore patterns
└── .labels.json  label definitions
```

**File organization rules:** See AGENTS.md "File Organization Rules" section.

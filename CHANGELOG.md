# Changelog

All notable changes to this workspace will be documented in this file.

The format is based on Keep a Changelog.

## [Unreleased]

### Added

- Root governance baseline files: `AGENTS.md`, `README.md`, `CHANGELOG.md`.
- Operational status system under `ops/status/`.
- Unprocessed intake manifest at `ops/intake/unprocessed/manifest.csv`.
- Full-depth isolation snapshot: `ops/status/2026-02-13-isolation-report-full-depth.md`.

### Changed

- Repository now has explicit operating principles for canonicalization, reconciliation, and archive safety.
- `AGENTS.md` now enforces contestability-by-default for unprocessed items and mandatory clarification workflow.
- Git has been initialized locally and connected to GitHub origin.
- Baseline synced to remote branch: `bootstrap/2026-02-13-baseline`.

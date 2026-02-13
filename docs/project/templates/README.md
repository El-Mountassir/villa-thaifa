# Project Templates (Minimal Pack)

This folder provides reusable templates for recurring, high-impact project artifacts.

## Templates

1. `canonical-domain-template.md`
2. `reconciliation-entry-template.md`
3. `deletion-safety-report-template.md`
4. `weekly-summary-template.md`

Use these templates when quality and consistency matter. Avoid templating one-off exploratory notes.

## Rendering Mode

Templates are designed to work in two modes:

1. Manual fill-in (copy, replace placeholders)
2. Programmatic render with Jinja2 from structured input data

Recommended automation pattern:

1. Store source data in JSON/YAML
2. Render template with Jinja2
3. Save generated markdown to target domain path
4. Run verification scripts before approving changes

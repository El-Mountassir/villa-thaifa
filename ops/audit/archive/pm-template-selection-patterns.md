# Pattern Extraction

**Date**: 2025-12-21

## Extracted Patterns

### Pattern 1: Methodology-First Selection

- **Observed In**: Source 2 (Research), Source 3 (Hospitality)
- **Underlying Principle**: The underlying work methodology (Agile, Waterfall, Kanban) determines optimal template more than industry label. A marketing team using sprints needs Agile templates, not "Marketing" templates.
- **Generalization Test**: Would apply to any industry choosing PM tools → **Yes**
- **Confidence**: High

### Pattern 2: Iteration Frequency as Primary Discriminator

- **Observed In**: Source 2 (Research), Source 1 (Tool comparisons)
- **Underlying Principle**: How often priorities/requirements change determines workflow structure:
  - **Daily/weekly changes** → Kanban (continuous flow)
  - **Bi-weekly cycles** → Scrum/Agile (sprint-based)
  - **Stable requirements** → Waterfall (sequential phases)
- **Generalization Test**: Construction vs software vs support → **Yes**
- **Confidence**: High

### Pattern 3: Work Type Taxonomy

- **Observed In**: All sources (implicit)
- **Underlying Principle**: Three fundamental work types drive template choice:
  | Type | Characteristics | Best Template Family |
  |------|-----------------|---------------------|
  | **Project** | Start/end, deliverable-focused | PM General, Software Dev |
  | **Process** | Recurring, optimization-focused | Operations, Kanban |
  | **Request** | Reactive, SLA-focused | IT Support, Service Desk |
- **Generalization Test**: Applies across industries → **Yes**
- **Confidence**: High

### Pattern 4: Trial-Before-Commit

- **Observed In**: Source 1, Source 3
- **Underlying Principle**: Import a real project into 2-3 tool trials, let the team vote. Adoption matters more than features.
- **Generalization Test**: Any tool selection decision → **Yes**
- **Confidence**: High

### Pattern 5: Start Small, Scale Proven

- **Observed In**: Source 3 (Hospitality)
- **Underlying Principle**: Pilot with one team/project before enterprise rollout. Resistance and training needs emerge during pilots.
- **Generalization Test**: Any organizational change → **Yes**
- **Confidence**: High

### Pattern 6: Visual Boards for Service Industries

- **Observed In**: Source 2, Source 3
- **Underlying Principle**: Industries with high request volume and multi-team coordination benefit from Kanban-style visualization (status columns, WIP limits).
- **Generalization Test**: Hospitality, support, creative agencies → **Yes**
- **Confidence**: High

### Pattern 7: Compliance Drives Structure

- **Observed In**: Source 2 (Research)
- **Underlying Principle**: Industries with audit/regulatory requirements (healthcare, finance, construction) need Waterfall-style documentation trails, even if daily work is Agile.
- **Generalization Test**: Any regulated industry → **Yes**
- **Confidence**: Medium (limited hospitality validation)

### Pattern 8: Hybrid as Norm, Not Exception

- **Observed In**: Source 1, Source 2
- **Underlying Principle**: Most real teams use hybrid approaches (Waterfall planning + Agile execution, Scrumban). Templates should be starting points, not constraints.
- **Generalization Test**: Any team with mixed project types → **Yes**
- **Confidence**: High

---

## Anti-Patterns Identified

### Anti-Pattern 1: Industry Label Matching

- **What**: Choosing "Marketing" template because you're in marketing
- **Why It Fails**: Industry label doesn't capture workflow type. A marketing ops team handling requests needs IT Support-style queues, not content calendars.
- **Better Approach**: Match by work type (project/process/request) first

### Anti-Pattern 2: Feature Checklist Selection

- **What**: Choosing tool with most features
- **Why It Fails**: Unused features add complexity, hurt adoption. "Best tool is the one you actually use"
- **Better Approach**: Trial with real work, measure actual usage

### Anti-Pattern 3: One Template Fits All

- **What**: Rolling out same template to all departments
- **Why It Fails**: Different teams have different work types. Engineering ≠ HR ≠ Sales
- **Better Approach**: Allow department-specific templates within unified tool

### Anti-Pattern 4: Big Bang Implementation

- **What**: Full company rollout on day one
- **Why It Fails**: Resistance, training gaps, workflow mismatches surface too late
- **Better Approach**: Pilot → refine → scale

### Anti-Pattern 5: Template Lock-In Assumption

- **What**: Treating initial template choice as permanent
- **Why It Fails**: Most tools allow template switching/customization. Fear of "wrong choice" causes analysis paralysis.
- **Better Approach**: Pick best current fit, plan for iteration

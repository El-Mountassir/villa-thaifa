# PM Template Selection Guide

**Generated**: 2025-12-21
**Pipeline**: `.claude/output/2025/Q4/reports/pm-template-selection/`

## Summary

Choosing a project management template by industry label ("Marketing", "IT Support") is backwards. This guide provides a characteristic-based framework: identify your work type, assess change frequency, apply constraints—then select. Validated against 3 source categories with 8 generalizable patterns extracted.

---

## Quick Decision (30 Seconds)

```
Q1: What's your primary work type?
├─ Requests (reactive, queue-based) ────────────→ IT Support
├─ Recurring processes (optimize flow) ─────────→ Operations
└─ Projects (start → end, deliverable) ─────────→ Q2

Q2: How often do requirements change?
├─ Daily/weekly ────────────────────────────────→ Kanban (Operations)
├─ Every 2 weeks ───────────────────────────────→ Software Dev (Agile)
└─ Rarely (fixed scope) ────────────────────────→ Project Management (Waterfall)

Q3: Special constraints?
├─ Need campaign calendars ─────────────────────→ Marketing
├─ Need design review cycles ───────────────────→ Design
├─ Need product roadmaps ───────────────────────→ Product Management
└─ None / unsure ───────────────────────────────→ Keep Q2 answer
```

---

## Key Insights

| Insight                                                      | Confidence | Sources                               |
| ------------------------------------------------------------ | ---------- | ------------------------------------- |
| Methodology fit matters more than tool features              | High       | Research, Hospitality, Comparisons    |
| Work type (project/process/request) is primary discriminator | High       | All 3 source categories               |
| "Safe choice" (generic PM) can miss specialized workflows    | Medium     | Research vs Practitioner disagreement |
| Hybrid approaches are the norm, not exception                | High       | Research, Comparisons                 |
| Trial with real project > feature comparison                 | High       | Comparisons, Hospitality              |
| Visual boards suit service industries                        | High       | Research, Hospitality                 |

---

## Full Framework

### Step 1: Identify Work Type

| Type        | Characteristics                     | Examples                                       |
| ----------- | ----------------------------------- | ---------------------------------------------- |
| **Project** | Has start/end, produces deliverable | Website launch, event, construction            |
| **Process** | Recurring, optimization-focused     | Monthly reporting, content production          |
| **Request** | Reactive, SLA-driven, queue-based   | Support tickets, IT help desk, client requests |

**Test**: Does your work have a natural "done" state (project), or does it flow continuously (process/request)?

### Step 2: Assess Iteration Frequency

| Frequency        | Description                                  | Implication                   |
| ---------------- | -------------------------------------------- | ----------------------------- |
| **Daily/Weekly** | Priorities shift constantly, quick pivots    | Kanban (no fixed sprints)     |
| **Bi-weekly**    | Regular planning cycles, some predictability | Scrum/Agile (sprint-based)    |
| **Stable**       | Requirements fixed upfront, sequential       | Waterfall (phases/milestones) |

**Test**: If something urgent came in today, would you restructure this week's work?

### Step 3: Apply Constraints

| Constraint           | Impact                                                         |
| -------------------- | -------------------------------------------------------------- |
| **Compliance/Audit** | Need Waterfall-style documentation, even if execution is Agile |
| **Multi-department** | Need cross-team visibility, Kanban boards help                 |
| **Client-facing**    | Need milestone tracking, deliverable focus                     |
| **Creative cycles**  | Need review/approval stages                                    |

### Step 4: Select Template Family

| If...                     | Then Template                          |
| ------------------------- | -------------------------------------- |
| Request + Daily           | **IT Support**                         |
| Process + Weekly          | **Operations**                         |
| Project + Bi-weekly       | **Software Development** (Agile)       |
| Project + Stable          | **Project Management** (Waterfall)     |
| Project + Creative cycles | **Design**                             |
| Project + Roadmaps needed | **Product Management**                 |
| Project + Campaigns       | **Marketing**                          |
| Genuinely unsure          | **Project Management** (most flexible) |

### Step 5: Trial & Validate

1. **Short-list 2-3 tools** based on template family
2. **Import a real project** (not a demo)
3. **Run for 1-2 weeks** with actual team
4. **Team votes** on usability
5. **Pilot one department** before company rollout

---

## Template Deep-Dives

### Software Development

**Use when**: Building software, managing sprints, tracking bugs
**Key features**: Scrum/Kanban boards, sprint planning, issue types (bug, story, epic), developer tool integrations
**Anti-pattern**: Using for non-software projects (overhead without benefit)

### Product Management

**Use when**: Planning what to build, managing feature backlogs, roadmap communication
**Key features**: Roadmap views, idea prioritization, requirements management
**Anti-pattern**: Confusing with Software Dev (PM = what to build, Dev = how to build)

### Marketing

**Use when**: Managing campaigns, content calendars, multi-channel coordination
**Key features**: Calendar views, asset management, campaign tracking
**Anti-pattern**: Using for one-off projects (overhead of calendar for single launch)

### Design

**Use when**: Creative team with request intake, review cycles, asset delivery
**Key features**: Request forms, review stages (draft → review → final), asset library
**Anti-pattern**: Using for strategy work (design template = execution-focused)

### Project Management (General)

**Use when**: Traditional projects, fixed scope, milestone-driven
**Key features**: Gantt charts, dependencies, milestones, resource allocation
**Anti-pattern**: Using for highly iterative work (Gantt breaks with constant changes)

### Operations

**Use when**: Recurring processes, optimizing throughput, managing ongoing work
**Key features**: Kanban boards, WIP limits, recurring task templates
**Anti-pattern**: Using for one-time projects (lacks deliverable focus)

### IT Support

**Use when**: Handling tickets, requests, SLA management
**Key features**: Request portal, queues, priority levels, SLA tracking
**Anti-pattern**: Using for proactive projects (template assumes reactive work)

### Other / Blank

**Use when**: Truly unique needs, want to build from scratch
**Pro**: No template assumptions to fight against
**Con**: More setup work, no best-practice guardrails

---

## Industry Considerations

### Hospitality (Hotels, Guesthouses)

| Work Type           | Recommendation                                                  |
| ------------------- | --------------------------------------------------------------- |
| Daily operations    | **Operations** (Kanban) — housekeeping, maintenance, front desk |
| Guest requests      | **IT Support** style queues — track, assign, resolve            |
| Renovation projects | **Project Management** — milestones, contractors                |
| Marketing campaigns | **Marketing** — booking promotions, content                     |

**Key insight**: Hospitality is multi-type. Consider using different templates per function within same tool.

**Recommended approach**: Start with Operations/Kanban for day-to-day, add project boards for discrete initiatives.

### Other Common Industries

| Industry         | Typical Pattern                                            |
| ---------------- | ---------------------------------------------------------- |
| **Agencies**     | Request intake (Design/IT Support) + Project delivery (PM) |
| **Construction** | Project Management (Waterfall) with strict milestones      |
| **Healthcare**   | Operations + Compliance-heavy documentation                |
| **E-commerce**   | Marketing (campaigns) + Operations (fulfillment)           |
| **SaaS**         | Software Dev + Product Management                          |

---

## Implementation Playbook

### Phase 1: Trial (Week 1-2)

- [ ] Short-list 2-3 tools matching template family
- [ ] Create accounts on free tiers
- [ ] Import ONE real project (not test data)
- [ ] Assign 3-5 team members to try each
- [ ] Collect feedback: what worked, what frustrated?

### Phase 2: Pilot (Week 3-6)

- [ ] Pick winning tool/template
- [ ] Roll out to ONE team/department
- [ ] Customize template (don't force-fit)
- [ ] Document changes made (for scaling)
- [ ] Track: adoption rate, task completion, team satisfaction

### Phase 3: Scale (Week 7+)

- [ ] Train additional teams
- [ ] Allow department-specific template customization
- [ ] Establish cross-team visibility rules
- [ ] Schedule quarterly review

### Adoption Metrics

- **Leading**: Daily active users / Total users
- **Lagging**: % tasks managed in tool vs elsewhere (email, sticky notes)
- **Quality**: Time to complete tasks, SLA hit rate

---

## Anti-Patterns to Avoid

| Anti-Pattern             | Why It Fails                  | Better Approach                    |
| ------------------------ | ----------------------------- | ---------------------------------- |
| Industry label matching  | Doesn't capture work type     | Use characteristic-based selection |
| Feature checklist        | Unused features hurt adoption | Trial with real work               |
| One template for all     | Teams have different needs    | Department templates, unified tool |
| Big bang rollout         | Problems surface too late     | Pilot → refine → scale             |
| Permanent choice anxiety | Templates can be changed      | Pick best current fit, iterate     |

---

## Limitations & Gaps

- **Migration costs**: No data on effort to switch templates post-implementation
- **Team size thresholds**: Unclear when simple tools become insufficient
- **Multi-project portfolios**: Single template may not serve program management
- **Quantified productivity**: No studies comparing productivity across template choices

---

## Sources

**Tool Comparisons**

- [Asana vs Trello vs Monday - Appvizer](https://www.appvizer.com/magazine/operations/project-management/asana-vs-trello-vs-monday)
- [Best PM Tools Compared - CSMIS](https://csmis.org/2025/10/01/best-project-management-tools-compared-jira-asana-trello-ms-project/)
- [Asana vs Jira - Plaky](https://plaky.com/blog/asana-vs-jira/)

**Methodology Research**

- [Agile vs Waterfall Decision Model - ScienceDirect](https://www.sciencedirect.com/science/article/pii/S1877050921002702)
- [Agile vs Waterfall - Lucidchart](https://www.lucidchart.com/blog/agile-vs-waterfall-vs-kanban-vs-scrum)
- [PM Methodologies - Teamwork](https://www.teamwork.com/project-management-guide/project-management-methodologies/)

**Hospitality-Specific**

- [Agile in Hospitality - CRR Hospitality](https://crrhospitality.com/blog/implementing-agile-project-management-in-the-hospitality-industry/)
- [PM for Hotels - Glide](https://www.glideapps.com/solutions/hotels/project-management-software)
- [Hospitality PM Software - Wrike](https://www.wrike.com/blog/enterprise-hospitality-project-management-software/)

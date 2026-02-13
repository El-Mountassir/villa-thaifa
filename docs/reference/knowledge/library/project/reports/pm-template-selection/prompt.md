Notre proposition capture bien l'essence du "Physics of Work", mais elle est incomplète par rapport au framework validé. Voici mon analyse détaillée :

Ce qui est bien capturé ✓

| Élément                                      | Status    |
| -------------------------------------------- | --------- |
| Work Type taxonomy (Project/Process/Request) | ✓ Présent |
| Iteration Frequency (3 niveaux)              | ✓ Présent |
| Trial-Before-Commit                          | ✓ Présent |
| Hybrid acknowledgment                        | ✓ Présent |
| Visual boards pour service                   | ✓ Présent |

Ce qui manque ✗

| Élément manquant                  | Impact                                                                                                             | Source             |
| --------------------------------- | ------------------------------------------------------------------------------------------------------------------ | ------------------ |
| Step 3: Constraints layer         | Les contraintes (Compliance, Multi-dept, Client-facing) raffinent le choix APRÈS Work Type + Frequency             | final.md:69-76     |
| Pilot → Scale pattern             | Critical pour adoption — pas juste "trial", mais "pilot one dept THEN scale"                                       | patterns.md:43-48  |
| Industry Overlay ≠ Primary Driver | Ta version mentionne l'idée, mais le framework insiste que l'industrie est un overlay, pas un facteur de sélection | synthesis.md:36-46 |

Sur la question des Anti-Patterns

Je partage ton instinct : garder prescriptif. Mais je propose un compromis :

Une phrase "Why" au début qui encapsule l'anti-pattern principal sans le nommer.

## 4. Work Management Protocols

**We** use a characteristic-based framework (...) Instead of relying on industry labels ← cette phrase est déjà là et suffit!

Ta phrase "Instead of relying on industry labels" fait le travail de l'anti-pattern #1 (Industry Label Matching) sans créer une section négative. Keep it.

---

Diagram(s)

Le Framework de Sélection (3 Steps + Overlay)

flowchart TD
subgraph Step1["Step 1: Work Type"]
Q1{{"What's the nature<br/>of your work?"}}
Q1 -->|"Has start/end,<br/>produces deliverable"| PROJECT[("🎯 PROJECT")]
Q1 -->|"Recurring,<br/>optimization-focused"| PROCESS[("🔄 PROCESS")]
Q1 -->|"Reactive,<br/>queue/SLA-driven"| REQUEST[("📥 REQUEST")]
end

      subgraph Step2["Step 2: Iteration Frequency"]
          PROJECT --> Q2P{{"How often do<br/>requirements change?"}}
          Q2P -->|Daily/Weekly| KANBAN["Kanban"]
          Q2P -->|Bi-weekly| AGILE["Agile/Scrum"]
          Q2P -->|Stable/Fixed| WATERFALL["Waterfall"]

          PROCESS --> PROC_KANBAN["Kanban / Operations"]
          REQUEST --> REQ_SUPPORT["IT Support / Service Desk"]
      end

      subgraph Step3["Step 3: Constraints (Refinement)"]
          KANBAN --> C1{Constraints?}
          AGILE --> C2{Constraints?}
          WATERFALL --> C3{Constraints?}
          PROC_KANBAN --> C4{Constraints?}
          REQ_SUPPORT --> C5{Constraints?}

          C1 -->|"Creative cycles"| DESIGN["Design Template"]
          C1 -->|"None"| OPS["Operations"]
          C2 -->|"Tech/Bugs"| SWDEV["Software Dev"]
          C2 -->|"Roadmaps"| PRODMGMT["Product Mgmt"]
          C2 -->|"Campaigns"| MKT["Marketing"]
          C3 -->|"Compliance"| PM["Project Mgmt + Docs"]
          C3 -->|"None"| PM2["Project Mgmt"]
          C4 -->|"Multi-dept"| OPS2["Operations + Kanban Boards"]
          C5 -->|"SLA"| SUPPORT["IT Support + Priority Queues"]
      end

      subgraph Overlay["Industry Overlay (Optional Nuance)"]
          direction LR
          IND["Industry Context"]
          IND -.->|"Hospitality"| NOTE1["Multi-type (Process + Request)"]
          IND -.->|"SaaS"| NOTE2["Software Dev + Product Mgmt"]
          IND -.->|"Agency"| NOTE3["Request intake + Project delivery"]
      end

      style Step1 fill:#e1f5fe
      style Step2 fill:#fff3e0
      style Step3 fill:#e8f5e9
      style Overlay fill:#f3e5f5,stroke-dasharray: 5 5

La Progression Standards (Versioning → Describing → Logging → Organizing)

graph LR
subgraph Standards["Project Standards Evolution"]
S1["1. SemVer<br/><i>How to VERSION</i>"]
S2["2. Dublin Core<br/><i>How to DESCRIBE</i>"]
S3["3. Changelog<br/><i>How to LOG</i>"]
S4["4. Work Mgmt<br/><i>How to ORGANIZE</i>"]

          S1 --> S2 --> S3 --> S4
      end

      subgraph Coverage["Coverage"]
          C1["Releases"]
          C2["Resources"]
          C3["History"]
          C4["Workflows"]

          S1 -.-> C1
          S2 -.-> C2
          S3 -.-> C3
          S4 -.-> C4
      end

      style S4 fill:#fff9c4,stroke:#f9a825,stroke-width:2px

---

Proposed Revision

Voici une version améliorée de ta Section 4, intégrant les éléments manquants :

## 4. Work Management Protocols

**We** use a characteristic-based framework to select and configure our project management workflows. Instead of relying on industry labels (e.g., "Marketing Template"), **we** analyze **Work Type**, **Iteration Frequency**, and **Constraints** to determine the optimal structure.

### 4.1 Core Selection Framework

**We** categorize every initiative through a 3-step process:

#### Step 1: Work Type

| Type        | Characteristics                     | Default Template Family      |
| ----------- | ----------------------------------- | ---------------------------- |
| **Project** | Has start/end, produces deliverable | Project Mgmt or Software Dev |
| **Process** | Recurring, optimization-focused     | Operations (Kanban)          |
| **Request** | Reactive, queue-based, SLA-driven   | IT Support / Service Desk    |

#### Step 2: Iteration Frequency

| Frequency        | Description                 | Implication                   |
| ---------------- | --------------------------- | ----------------------------- |
| **Daily/Weekly** | Priorities shift constantly | Kanban (continuous flow)      |
| **Bi-weekly**    | Regular planning cycles     | Scrum/Agile (sprint-based)    |
| **Stable**       | Requirements fixed upfront  | Waterfall (phases/milestones) |

#### Step 3: Constraints (Refinement)

| Constraint           | Adjustment                                                 |
| -------------------- | ---------------------------------------------------------- |
| **Compliance/Audit** | Add Waterfall-style documentation, even if execution Agile |
| **Multi-department** | Add cross-team visibility (Kanban boards)                  |
| **Client-facing**    | Add milestone tracking, deliverable focus                  |
| **Creative cycles**  | Add review/approval stages                                 |

### 4.2 Implementation Guidelines

1. **Trial with Real Data:** **We** validate choices by running a "Zero-State" pilot with actual project data for 1-2 weeks. Team votes on usability.

2. **Pilot → Scale:** **We** roll out to ONE team/department first, document customizations, then scale to others.

3. **Hybrid as Norm:** **We** acknowledge most work is hybrid (e.g., Waterfall planning + Agile execution). Templates are starting points, not constraints.

4. **Visual Boards Default:** For service-heavy or multi-department coordination, **we** default to Kanban boards with WIP limits.

### 4.3 Industry Overlay (Optional)

Industry context adds nuance **after** characteristic-based selection:

| Industry     | Typical Pattern                            |
| ------------ | ------------------------------------------ |
| Hospitality  | Multi-type (Process + Request)             |
| SaaS         | Software Dev + Product Mgmt                |
| Agencies     | Request intake (Design) + Project delivery |
| Construction | Waterfall with strict milestones           |

---

References

- .claude/output/2025/Q4/reports/pm-template-selection/final.md — Full framework, decision tree
- .claude/output/2025/Q4/reports/pm-template-selection/synthesis.md — Integration strategy, industry overlay
- .claude/output/2025/Q4/reports/pm-template-selection/patterns.md — 8 validated patterns, 5 anti-patterns
- .claude/output/2025/Q4/reports/pm-template-selection/project_standards.md — Current standards (Sections 1-3)

---

Additional Context

Réponses directes à tes questions :

1. Est-ce que ton draft capture l'essence "Physics of Work" ?
   → Partiellement. Tu as le cœur (Work Type + Frequency), mais il manque le Step 3 (Constraints) et le pattern "Pilot → Scale" qui sont validés par les sources.
2. Anti-patterns : inclure ou non ?
   → Non, garde prescriptif. Ta phrase "Instead of relying on industry labels" fait déjà le travail de l'anti-pattern principal. Ajouter une section négative alourdirait le standard. Le guide complet (final.md) reste disponible pour ceux qui veulent comprendre les pièges.

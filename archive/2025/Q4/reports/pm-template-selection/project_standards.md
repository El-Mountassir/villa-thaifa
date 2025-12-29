## Title: Project Standards & Protocols

```yaml
Creator: Team (Humans & AI Agents)

Subject: Semantic Versioning, Dublin Core Metadata, Changelog Standards, Work Management Protocols

Description: The central reference for our team's versioning logic, resource description, history tracking, and work management standards.

Date: 2025-12-21

Type: Text

Format: Markdown

Identifier: project_standards.md

Language: en

Rights: Internal Team Standard
```

# Project Standards & Protocols

This document outlines the core standards **we use** to maintain consistency, interoperability, and clarity across all our projects, software, and documents.

## 1. Semantic Versioning 2.0.0 (SemVer)

**Semantic Versioning 2.0.0 (SemVer)** is a standardized versioning scheme for **all our work—software, documents, and projects**—that **we use**—employing a comprehensive version string **MAJOR.MINOR.PATCH-PRERELEASE**—to communicate the nature of changes in a release.

### Standard Compliance

It is important for **our team (Humans & AI Agents)** to understand that while **we** apply these rules to non-software assets and enforce a strict **"Zero-State"** workflow, this policy remains **fully compliant** with the official Semantic Versioning 2.0.0 specification.

- **Broad Application:** The standard permits us to define our own "Public API" (or "Public Scope"), allowing us to validly apply these rules to documents and projects.
- **Strict Workflow:** Our choice to use pre-release tags for every step is a workflow policy we layer _on top_ of the standard, not a deviation from it.

### The Core Rules

When updating **our** work, **we** increment the version number based on these specific criteria:

- **MAJOR version (X.y.z):** Incremented when **we** make **incompatible changes** that break backward compatibility or fundamentally alter the structure/scope. **MINOR and PATCH version numbers must be reset to 0** (e.g., `1.1.3-rc.1` -> `2.0.0-alpha.0`).
- **MINOR version (x.Y.z):** Incremented when **we** add functionality or substantial content in a **backward-compatible manner**. This also includes marking parts of the scope as deprecated. **PATCH version number must be reset to 0** (e.g., `1.1.3-rc.1` -> `1.2.0-alpha.0`).
- **PATCH version (x.y.Z):** Incremented for **backward-compatible fixes** (typos, bug fixes, minor edits) that do not change the public scope or meaning (e.g., `1.1.3-rc.1` -> `1.1.4-alpha.0`).
- **Pre-release Identifier (x.y.z-tag.N):** Incremented for **successive unstable builds** of the same target version (e.g., `1.0.0-alpha.0` -> `1.0.0-alpha.1`).

### Additional Version Components

Beyond the standard three-part number, SemVer 2.0.0 allows **us** to use:

- **Pre-release Tags:** Denoted by a hyphen (e.g., `1.0.0-alpha.0`). These indicate that the version is unstable and might not meet compatibility requirements.
- **Build Metadata:** Denoted by a plus sign (e.g., `1.0.0+20130313`). This is used for diagnostic information like build numbers, dates, or commit hashes and does not affect version precedence.

### Key Operational Guidelines

1. **Public Scope Declaration:** To use SemVer, **we** must first define a "public API" or "Public Scope" (via documentation, code, or outline) so consumers know which parts of the work are subject to these rules.
2. **Initial Development (0.y.z):** Versions starting with `0` are for initial development where everything can change at any time; the scope is not considered stable.

   - **Zero-State (0.0.0-alpha.0):** **We** start specifically at `0.0.0-alpha.0` to denote the absolute beginning of the repository or project before functional content exists.
   - **Strict Pre-release Tagging:** **We** maintain the full pre-release structure even for early increments to distinguish work-in-progress drafts from "finished" 0.x milestones.
     - _Example:_ `0.0.1-alpha.0` (Work started on first patch/edit)
     - _Example:_ `0.0.1-alpha.1` (Interim draft)
     - _Example:_ `0.0.1-mc.1` (Milestone complete)

3. **Stable Release (1.0.0-osr.1):** This milestone signals that the public scope is stable and all subsequent changes must follow the increment rules.

   - **Pre-release to Stable:** **We** apply the same strict tagging to prepare for the major release.
     - _Example:_ `1.0.0-alpha.0` (Work started on stable release)
     - _Example:_ `1.0.0-rc.1` (Release Candidate / Final Proof)
     - _Example:_ `1.0.0-osr.1` (Official Stable Release)

4. **Immutability:** Once a version is released, the contents of that specific version **must not** be modified. Any changes must be released under a new version number.

For the full specification, visit the official [Semantic Versioning website](https://semver.org/ "null").

## 2. Dublin Core Metadata Initiative (DCMI)

**Dublin Core** is a simple, widely-used standard of 15 core metadata elements that **we use** to describe our digital and physical resources. It is maintained by the [DCMI](https://www.dublincore.org/resources/glossary/dublin_core/ "null") and serves as a common vocabulary for resource description, ensuring consistency and interoperability across our projects.

### The 15 Core Elements

**We** apply these elements to categorize and describe our assets:

- **Title:** The name of the resource.
- **Creator:** The person or organization responsible for the content (e.g., Team (Humans & AI Agents)).
- **Subject:** The topic covered.
- **Description:** A textual outline or summary.
- **Publisher:** Those making the resource available.
- **Contributor:** Those who added to the content.
- **Date:** When the resource was created or made available.
- **Type:** The category or nature of the resource (e.g., image, text, software).
- **Format:** The physical or digital medium (e.g., PDF, MP3, Markdown).
- **Identifier:** A unique ID (e.g., URL, ISBN, Filepath).
- **Source:** Where the resource originated.
- **Language:** The language of the content.
- **Relation:** How it relates to other resources.
- **Coverage:** The spatial or temporal scope.
- **Rights:** Information about intellectual property.

### Key Concepts

- **Simplicity:** Designed to be understandable and usable by any team member (Human or AI).
- **Cross-Domain:** Applicable to all our resource types (code, docs, media).
- **Extendability:** The base 15 elements can be enhanced with qualifiers for greater detail (Qualified Dublin Core).
- **Standardization:** Formally recognized as ISO 15836.

### Purpose

To facilitate information discovery on the growing web (and within our internal archives) by embedding simple, catalog-like metadata directly with resources, making them easier for **us** to find and manage.

For the full specification, visit the official [Dublin Core Element Set](https://www.dublincore.org/specifications/dublin-core/dces/ "null").

## 3. Changelog Standards (Keep a Changelog)

**Keep a Changelog** is the standard **we use** to maintain a curated, chronologically ordered history of notable changes for each project. It is designed to be read by **humans**, not machines, ensuring clarity for all stakeholders (Humans & AI Agents).

### Guiding Principles

**We** adhere to these core principles to ensure our history is readable and useful:

- **Humans First:** The log is a communication tool, not a raw dump of git commits.
- **Reverse Chronological Order:** The latest version must always be at the top.
- **Versioned Entries:** Every released version (matching our **SemVer** rules) must have its own entry, including the version number and release date.
- **ISO Date Format:** **We** use the `YYYY-MM-DD` format (e.g., `2025-12-21`) to avoid regional ambiguity.

### Standard Change Categories

To make logs easy to scan, **we** group changes into these specific subsections:

- **Added:** New features or capabilities.
- **Changed:** Changes in existing functionality.
- **Deprecated:** Soon-to-be removed features to warn users.
- **Removed:** Features that were actually deleted.
- **Fixed:** Bug fixes and error corrections.
- **Security:** Important updates regarding vulnerabilities.

### Implementation Guidelines

1. **File Naming:** The file must be named `CHANGELOG.md` and located in the project's root directory.
2. **Curation vs. Automation:** While tools (like Standard Version) can help, **we** value manual curation to filter out noise. If using automation via **Conventional Commits** (e.g., `feat:`, `fix:`, `docs:`), the output must still be reviewed to ensure it meets the "Humans First" principle.
3. **Antipatterns to Avoid:**

   - **Dumping Git Logs:** We do not simply list every commit; we summarize the value.
   - **Missing Dates:** Every version must be dated.
   - **Silent Removals:** We do not remove public features without a prior "Deprecated" warning phase.

For the full specification, visit the official [Keep a Changelog website](https://keepachangelog.com/).

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

**Test**: Does your work have a natural "done" state (project), or does it flow continuously (process/request)?

#### Step 2: Iteration Frequency

| Frequency        | Description                 | Implication                   |
| ---------------- | --------------------------- | ----------------------------- |
| **Daily/Weekly** | Priorities shift constantly | Kanban (continuous flow)      |
| **Bi-weekly**    | Regular planning cycles     | Scrum/Agile (sprint-based)    |
| **Stable**       | Requirements fixed upfront  | Waterfall (phases/milestones) |

**Test**: If something urgent came in today, would you restructure this week's work?

#### Step 3: Constraints (Refinement)

| Constraint           | Adjustment                                                          |
| -------------------- | ------------------------------------------------------------------- |
| **Compliance/Audit** | Add Waterfall-style documentation trail, even if execution is Agile |
| **Multi-department** | Add cross-team visibility (Kanban boards)                           |
| **Client-facing**    | Add milestone tracking, deliverable focus                           |
| **Creative cycles**  | Add review/approval stages                                          |

### 4.2 Definition of Ready (DoR)

**We** verify these criteria before starting any task (based on the INVEST framework):

| Criterion       | Check                                       |
| --------------- | ------------------------------------------- |
| **Independent** | No external blockers; dependencies resolved |
| **Valuable**    | Clear stakeholder value articulated         |
| **Estimable**   | Scope understood enough to estimate         |
| **Small**       | Completable within time-box (sprint/day)    |
| **Testable**    | Acceptance criteria defined                 |

#### DoR by Work Type

| Work Type   | Additional DoR Criteria                                           |
| ----------- | ----------------------------------------------------------------- |
| **Project** | Goals, scope, acceptance criteria, dependencies mapped            |
| **Process** | Process flow clear, inputs defined, success metrics known         |
| **Request** | Request is actionable, urgency/impact clear, resources identified |

### 4.3 Definition of Done (DoD)

**We** verify these criteria before marking work complete:

| Category          | Check                                               |
| ----------------- | --------------------------------------------------- |
| **Clarity**       | All tasks completed, acceptance criteria verified   |
| **Quality**       | Meets defined standards (format, content, accuracy) |
| **Documentation** | Relevant outputs captured and attached              |
| **Review**        | Peer/stakeholder review conducted (if required)     |
| **Handoff**       | Ready for next phase or delivery                    |

#### DoD by Work Type

| Work Type   | DoD Criteria                                                     |
| ----------- | ---------------------------------------------------------------- |
| **Project** | Deliverables complete, quality gate passed, stakeholder sign-off |
| **Process** | Process executed per standard, outputs verified, documented      |
| **Request** | Request resolved, confirmation from requestor, closed in system  |

#### DoD by Deliverable Type (Examples)

| Deliverable Type           | DoD Checklist                                        |
| -------------------------- | ---------------------------------------------------- |
| **Messaging (Copy-Paste)** | TXT format, tone appropriate, recipient-ready        |
| **Formal Report (PDF)**    | Professional styling, structured sections, metadata  |
| **Internal Doc (MD)**      | Dublin Core metadata, proper hierarchy, correct path |

### 4.4 Task Lifecycle

**We** track tasks through these states:

```
[Ready] → [In Progress] → [Review] → [Done]
    ↓           ↓
[Blocked] ← [Blocked]
    ↓
[Escalated]
```

| State       | Entry Criteria              | Exit Criteria                 |
| ----------- | --------------------------- | ----------------------------- |
| Ready       | DoR met                     | Work started                  |
| In Progress | Work started                | Work complete OR blocked      |
| Blocked     | Dependency/issue identified | Blocker resolved OR escalated |
| Review      | Work complete               | Approved OR revision needed   |
| Done        | DoD met + approved          | —                             |
| Escalated   | All alternatives exhausted  | Resolution from escalation    |

#### Priority Matrix

| Priority | MoSCoW | Eisenhower       | Action            |
| -------- | ------ | ---------------- | ----------------- |
| P0       | Must   | Urgent+Important | Do immediately    |
| P1       | Must   | Important        | Do today          |
| P2       | Should | Urgent           | Delegate/schedule |
| P3       | Could  | Neither          | Batch for later   |
| P4       | Won't  | —                | Backlog/defer     |
| P5       | —      | —                | Archive           |

### 4.5 Communication Pattern

**We** follow this sequence for stakeholder-facing work:

| Phase         | Purpose                            | Output          |
| ------------- | ---------------------------------- | --------------- |
| **Scout**     | Explore, verify feasibility        | Notes, findings |
| **Rapport**   | Inform stakeholder of discoveries  | Status update   |
| **Questions** | Gather missing info (with context) | Clarifications  |
| **Action**    | Execute when all is clear          | Deliverable     |

**Rule**: Never request information without first reporting what was discovered.

**Anti-pattern**: Asking questions without context ("What's X?") vs. proper form ("I found Y and Z, but need X to proceed because...")

### 4.6 Implementation Guidelines

1. **Trial with Real Data**: **We** validate workflow choices by running a pilot with actual project data for 1-2 weeks before committing.

2. **Pilot → Scale**: **We** roll out to ONE team/project first, document customizations, then scale to others.

3. **Hybrid as Norm**: **We** acknowledge most real work is hybrid (e.g., Waterfall planning + Agile execution). Templates are starting points, not constraints.

4. **Visual Boards Default**: For service-heavy or multi-department coordination, **we** default to Kanban boards with WIP limits.

5. **Review Cadence**: **We** review workflow effectiveness quarterly and adjust as needed.

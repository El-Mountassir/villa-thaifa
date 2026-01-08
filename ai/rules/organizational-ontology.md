# Organizational Ontology

> **Pattern**: One [Container], One [Defining Element], One Purpose
>
> Everything we create follows this rule. No exceptions.

## Core Ontology (Daily Use)

These 15 levels are our working vocabulary. Memorize them.

### Strategic Tier

| Level          | Element    | One-Liner                                   | Example (sovereign-bootstrap)                               |
| -------------- | ---------- | ------------------------------------------- | ----------------------------------------------------------- |
| **Mission**    | Truth      | One mission, one truth, one purpose         | "Sovereign infrastructure for carbon-silicon collaboration" |
| **Portfolio**  | Strategy   | One portfolio, one strategy, one purpose    | All of Omar's tech initiatives                              |
| **Initiative** | Hypothesis | One initiative, one hypothesis, one purpose | "Pop!\_OS 24.04 migration"                                  |

### Delivery Tier

| Level          | Element  | One-Liner                             | Example                            |
| -------------- | -------- | ------------------------------------- | ---------------------------------- |
| **Project**    | Outcome  | One project, one outcome, one purpose | sovereign-bootstrap repo           |
| **Repository** | Boundary | One repo, one boundary, one purpose   | This repo = workstation automation |

### Execution Tier

| Level            | Element      | One-Liner                                       | Example                   |
| ---------------- | ------------ | ----------------------------------------------- | ------------------------- |
| **Orchestrator** | Coordination | One orchestrator, one coordination, one purpose | Lead Claude instance      |
| **Agent**        | Prompt       | One agent, one prompt, one purpose              | Explore agent, Plan agent |
| **Session**      | Context      | One session, one context, one purpose           | Single conversation       |
| **Attempt**      | Question     | One attempt, one question, one purpose          | Experimental try          |

### Structure Tier

| Level        | Element        | One-Liner                                 | Example                                |
| ------------ | -------------- | ----------------------------------------- | -------------------------------------- |
| **Folder**   | Domain         | One folder, one domain, one purpose       | `docs/rules/` = governance rules       |
| **File**     | Responsibility | One file, one responsibility, one purpose | `workflow.md` = workflow rules only    |
| **Function** | Operation      | One function, one operation, one purpose  | `check_thermal()` = thermal check only |

### Work Tier

| Level     | Element | One-Liner                         | Example                      |
| --------- | ------- | --------------------------------- | ---------------------------- |
| **Epic**  | Theme   | One epic, one theme, one purpose  | Thermal management system    |
| **Story** | Need    | One story, one need, one purpose  | "User needs quiet operation" |
| **Task**  | Action  | One task, one action, one purpose | "Set CPU limit to 70W"       |

---

## Extended Reference

Full ontology for completeness. Reference as needed.

### Tier 1: Strategic (Why we exist)

| Level      | Element    | One-Liner                                                                 |
| ---------- | ---------- | ------------------------------------------------------------------------- |
| Mission    | Truth      | One mission, one truth, one purpose - the unchanging reason for existence |
| Vision     | Future     | One vision, one future, one purpose - the desired end state               |
| Portfolio  | Strategy   | One portfolio, one strategy, one purpose - investment allocation          |
| Program    | Capability | One program, one capability, one purpose - coordinated delivery           |
| Initiative | Hypothesis | One initiative, one hypothesis, one purpose - strategic bet               |

### Tier 2: Tactical (What we achieve)

| Level      | Element     | One-Liner                                                         |
| ---------- | ----------- | ----------------------------------------------------------------- |
| Objective  | Outcome     | One objective, one outcome, one purpose - what success looks like |
| Key Result | Measure     | One key result, one measure, one purpose - proof of progress      |
| Project    | Deliverable | One project, one deliverable, one purpose - bounded effort        |
| Milestone  | Gate        | One milestone, one gate, one purpose - checkpoint validation      |

### Tier 3: Operational (How we work)

| Level      | Element  | One-Liner                                                          |
| ---------- | -------- | ------------------------------------------------------------------ |
| Epic       | Theme    | One epic, one theme, one purpose - large business initiative       |
| Capability | Function | One capability, one function, one purpose - what the system can do |
| Feature    | Value    | One feature, one value, one purpose - user-facing capability       |
| Story      | Need     | One story, one need, one purpose - user requirement                |
| Task       | Action   | One task, one action, one purpose - atomic unit of work            |
| Sprint     | Timebox  | One sprint, one timebox, one purpose - delivery cadence            |

### Tier 4: Architectural (How we design)

| Level           | Element     | One-Liner                                                        |
| --------------- | ----------- | ---------------------------------------------------------------- |
| System          | Mission     | One system, one mission, one purpose - complete solution         |
| Subsystem       | Function    | One subsystem, one function, one purpose - major capability      |
| Bounded Context | Model       | One context, one model, one purpose - semantic boundary          |
| Service         | Contract    | One service, one contract, one purpose - API boundary            |
| Module          | Cohesion    | One module, one cohesion, one purpose - logical grouping         |
| Component       | Interface   | One component, one interface, one purpose - deployable unit      |
| Layer           | Abstraction | One layer, one abstraction, one purpose - separation of concerns |

### Tier 5: Code (What we build)

| Level      | Element        | One-Liner                                                   |
| ---------- | -------------- | ----------------------------------------------------------- |
| Repository | Boundary       | One repo, one boundary, one purpose - deployable ownership  |
| Package    | Namespace      | One package, one namespace, one purpose - code organization |
| Folder     | Domain         | One folder, one domain, one purpose - file grouping         |
| File       | Responsibility | One file, one responsibility, one purpose - atomic unit     |
| Class      | Entity         | One class, one entity, one purpose - object definition      |
| Function   | Operation      | One function, one operation, one purpose - single action    |

### Tier 6: Data (What we store)

| Level    | Element   | One-Liner                                               |
| -------- | --------- | ------------------------------------------------------- |
| Database | Domain    | One database, one domain, one purpose - data ownership  |
| Schema   | Context   | One schema, one context, one purpose - logical grouping |
| Table    | Entity    | One table, one entity, one purpose - structured storage |
| Record   | Instance  | One record, one instance, one purpose - single entry    |
| Field    | Attribute | One field, one attribute, one purpose - atomic value    |

### Tier 7: Infrastructure (Where we run)

| Level       | Element  | One-Liner                                                    |
| ----------- | -------- | ------------------------------------------------------------ |
| Environment | Stage    | One environment, one stage, one purpose - deployment context |
| Cluster     | Workload | One cluster, one workload, one purpose - compute boundary    |
| Node        | Capacity | One node, one capacity, one purpose - compute resource       |
| Namespace   | Tenant   | One namespace, one tenant, one purpose - isolation boundary  |
| Pod         | Unit     | One pod, one unit, one purpose - scheduling unit             |
| Container   | Process  | One container, one process, one purpose - runtime isolation  |

### Tier 8: Version Control (How we evolve)

| Level   | Element | One-Liner                                                |
| ------- | ------- | -------------------------------------------------------- |
| Release | Version | One release, one version, one purpose - published state  |
| Branch  | Intent  | One branch, one intent, one purpose - parallel evolution |
| Commit  | Change  | One commit, one change, one purpose - atomic snapshot    |
| Tag     | Marker  | One tag, one marker, one purpose - reference point       |

### Tier 9: Quality (How we verify)

| Level      | Element     | One-Liner                                                 |
| ---------- | ----------- | --------------------------------------------------------- |
| Test Suite | Scope       | One suite, one scope, one purpose - test collection       |
| Test Case  | Scenario    | One case, one scenario, one purpose - verification path   |
| Assertion  | Expectation | One assertion, one expectation, one purpose - truth check |

### Tier 10: Knowledge (What we preserve)

| Level    | Element | One-Liner                                                  |
| -------- | ------- | ---------------------------------------------------------- |
| Corpus   | Domain  | One corpus, one domain, one purpose - knowledge collection |
| Document | Topic   | One document, one topic, one purpose - knowledge unit      |
| Section  | Aspect  | One section, one aspect, one purpose - focused content     |

### Tier 11: Execution (How AI works)

| Level        | Element      | One-Liner                                                          |
| ------------ | ------------ | ------------------------------------------------------------------ |
| Orchestrator | Coordination | One orchestrator, one coordination, one purpose - agent management |
| Session      | Context      | One session, one context, one purpose - conversation boundary      |
| Agent        | Prompt       | One agent, one prompt, one purpose - focused execution             |
| Wave         | Batch        | One wave, one batch, one purpose - parallel execution              |
| Attempt      | Question     | One attempt, one question, one purpose - experimental try          |

### Tier 12: Mental (How we think)

| Level     | Element     | One-Liner                                                     |
| --------- | ----------- | ------------------------------------------------------------- |
| Model     | Perspective | One model, one perspective, one purpose - reality abstraction |
| Framework | Lens        | One framework, one lens, one purpose - analysis structure     |
| Principle | Truth       | One principle, one truth, one purpose - guiding rule          |
| Pattern   | Solution    | One pattern, one solution, one purpose - reusable approach    |

---

## Application Rules

1. **Before creating anything**: Identify which level it belongs to
2. **If it spans multiple levels**: Split it
3. **If you can't name the "One Element"**: It's not focused enough
4. **If you need "and" to describe it**: It violates the pattern

---

## Sources

- [SAFe Hierarchy](https://www.enov8.com/blog/the-hierarchy-of-safe-scaled-agile-framework-explained/)
- [PMI Portfolio Management](https://www.pmi.org/learning/library/integrated-portfolio-program-management-7409)
- [Martin Fowler - Test Pyramid](https://martinfowler.com/articles/practical-test-pyramid.html)
- [DDD Wikipedia](https://en.wikipedia.org/wiki/Domain-driven-design)
- [TOGAF](https://pubs.opengroup.org/togaf-standard/introduction/chap03.html)
- [Kubernetes Architecture](https://kubernetes.io/docs/concepts/architecture/)
- [OKR Guide - Atlassian](https://www.atlassian.com/agile/agile-at-scale/okr)
- [Gitflow Workflow](https://www.atlassian.com/git/tutorials/comparing-workflows/gitflow-workflow)
- [Multi-Agent Orchestration](https://docs.swarms.world/en/latest/swarms/structs/multi_agent_orchestration/)

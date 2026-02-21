# Handover Template

> **Version**: 1.0
> **Date**: 2026-01-15
> **Usage**: This template is to be used FOR EACH agent session end

---

## Instructions

COPY this template and fill out all sections at the end of each session.

**File Name**: `<agent>-<timestamp>.md`
**Example**: `pricing-analyst-20260115-1430.md`

---

## YAML Template

```yaml
---
handover_version: '1.0'
agent: <agent_name>
timestamp: <YYYY-MM-DD HH:mm>
session_id: <claude_session_id>

tasks_completed:
  - <task_1_description>
  - <task_2_description>
  # Add as many tasks as necessary

tasks_in_progress:
  - <task_if_any_1>
  - <task_if_any_2>
  # Set "None" if no task is in progress

blocking_points:
  - <blocker_if_any_1>
  - <blocker_if_any_2>
  # Set "None" if no blocker

next_actions_for_next_agent:
  - <action_1>
  - <action_2>
  # Concrete actions for the next agent

files_modified:
  - <file_path_1>
  - <file_path_2>
  # Complete list of modified files

files_created:
  - <file_path_1>
  - <file_path_2>
  # Complete list of created files

context_for_next_agent: |
  <Detailed context for next agent>
  - Explain what was done
  - Explain what is left to do
  - Give context on the decisions made
  - Mention any gotchas or known issues

findings_for_cto: |
  <Technical findings, architectural decisions, system improvements>
  - Technical decisions made
  - Suggested improvements
  - Discovered issues
  - Lessons learned
---
```

---

## Explanations of Sections

### 1. `tasks_completed`

List of all **completed** tasks during this session.

**Example**:

```yaml
tasks_completed:
  - 'Created CLAUDE.md with 3-minute read format'
  - 'Standardized frontmatter for all 17 agents'
  - 'Created docs/agents/registry.json with all agent metadata'
```

### 2. `tasks_in_progress`

List of tasks **in progress** but not yet completed.

**Example**:

```yaml
tasks_in_progress:
  - 'Fixing obsolete paths (el-mountassir → omar-el-mountassir)'
  - 'Creating handover templates for agents'
```

### 3. `blocking_points`

List of **blockers** preventing further progress.

**Example**:

```yaml
blocking_points:
  - 'Missing client information for Said Thaifa profile'
  - 'Cannot access Booking.com API - credentials needed'
```

### 4. `next_actions_for_next_agent`

**Concrete** actions that the next agent must take.

**Example**:

```yaml
next_actions_for_next_agent:
  - 'Complete fixing obsolete paths in all .md files'
  - 'Validate that all symlinks in docs/agents/context/mandatory/ work'
  - 'Create capabilities JSON files for each agent'
```

### 5. `files_modified`

**Complete** list of modified files.

**Example**:

```yaml
files_modified:
  - '.claude/agents/pricing-analyst.md'
  - '.claude/agents/reservation-manager.md'
  # ... all 17 agents
```

### 6. `files_created`

**Complete** list of created files.

**Example**:

```yaml
files_created:
  - 'CLAUDE.md'
  - 'docs/agents/registry.json'
  - 'docs/knowledge/client/PROFILE.json'
  # ... etc
```

### 7. `context_for_next_agent`

**Detailed** context for the next agent. Use the `|` format for multi-line.

**Example**:

```yaml
context_for_next_agent: |
  Session Context:
  - We created the agentic prompt system for Villa Thaifa
  - 17 agents now have a standardized frontmatter with:
    * agent_id, version, status, created, modified, created_by
    * context_to_load (mandatory, domain_specific, mission_specific)
    * dependencies, tools, output_format, domain, tags, changelog
  - The registry.json is created with all agent metadata
  - Placeholders are created in docs/knowledge/ (client, property, processes, communications, finance, leadership)

  What remains to be done:
  - Fix obsolete paths (el-mountassir → omar-el-mountassir)
  - Restore 10 unique files from archive/
  - Organize the archive (legacy/history/restored)
  - Final validation

  Gotchas:
  - The browser-agent.md file has an obsolete path in instructions
  - The claude-md-agent.md file references /home/omar/el-mountassir/ instead of /home/omar/omar-el-mountassir/
  - Verify all paths before validation
```

### 8. `findings_for_cto`

Technical decisions and improvements for the CTO (Claude).

**Example**:

```yaml
findings_for_cto: |
  Technical decisions made:
  - Standardized frontmatter with coherent YAML structure
  - $DOCS/ variables for referencing relative paths
  - JSON Registry for programmatic querying
  - Standardized handover system for continuity

  Suggested improvements:
  - Implement a variable resolution system for $DOCS/
  - Create a dedicated agent for link validation
  - Automate handover creation

  Discovered issues:
  - Obsolete el-mountassir paths in multiple files
  - Some .md files in archive/ are not yet organized
  - Multiple agents reference data/rooms/ and data/operations/ files that may not exist yet

  Lessons learned:
  - Standardize frontmatter BEFORE creating future agents
  - Use absolute paths or variables to avoid issues
  - Document the expected handover format early on
```

---

## Complete Example

```yaml
---
handover_version: '1.0'
agent: claude-sonnet-4.5
timestamp: 2026-01-15 14:30
session_id: b07900e4-2b83-4f37-aeb4-3edd794addc2

tasks_completed:
  - 'Created complete backup of villa-thaifa project'
  - 'Created docs/agents/ structure (context, handovers, capabilities)'
  - 'Created CLAUDE.md as single entry point (3 min read)'
  - 'Created docs/agents/registry.json with all 17 agents metadata'
  - 'Created all knowledge folders with placeholders (client, property, processes, communications, finance)'
  - 'Created leadership folder with VISION.md, DECISIONS.md, PRIORITIES.md, TEAM.md'
  - 'Standardized frontmatter for all 17 agents'

tasks_in_progress:
  - 'Fixing obsolete paths (el-mountassir → omar-el-mountassir)'
  - 'Creating handover templates'

blocking_points:
  - 'None'

next_actions_for_next_agent:
  - "Fix all obsolete paths containing 'el-mountassir' to 'omar-el-mountassir'"
  - 'Validate all symlinks work correctly'
  - 'Run validation tests per plan'
  - 'Archive old files properly (legacy/history/restored)'

files_modified:
  - '.claude/agents/pricing-analyst.md'
  - '.claude/agents/reservation-manager.md'
  - '.claude/agents/calendar-agent.md'
  - '.claude/agents/platform-validator.md'
  - '.claude/agents/browser-agent.md'
  - '.claude/agents/guest-communicator.md'
  - '.claude/agents/meta-agent.md'
  - '.claude/agents/research-agent.md'
  - '.claude/agents/auditor.md'
  - '.claude/agents/security-auditor.md'
  - '.claude/agents/translation-agent.md'
  - '.claude/agents/data-sync-checker.md'
  - '.claude/agents/incident-reporter.md'
  - '.claude/agents/html-report-generator.md'
  - '.claude/agents/claude-md-agent.md'
  - '.claude/agents/smart-contract-auditor.md'
  - '.claude/agents/decision-evaluator.md'

files_created:
  - 'CLAUDE.md'
  - 'docs/agents/registry.json'
  - 'docs/agents/handovers/template.md'
  - 'docs/knowledge/INDEX.md'
  - 'docs/knowledge/client/README.md'
  - 'docs/knowledge/client/PROFILE.json'
  - 'docs/knowledge/client/PREFERENCES.md'
  - 'docs/knowledge/client/HISTORY.md'
  - 'docs/knowledge/client/COMMUNICATION.md'
  - 'docs/knowledge/property/README.md'
  - 'docs/knowledge/property/VILLA_THAIFA.json'
  - 'docs/knowledge/processes/README.md'
  - 'docs/knowledge/processes/check-in-out.json'
  - 'docs/knowledge/processes/housekeeping.json'
  - 'docs/knowledge/processes/maintenance.json'
  - 'docs/knowledge/processes/emergency.json'
  - 'docs/knowledge/communications/README.md'
  - 'docs/knowledge/communications/channels.json'
  - 'docs/knowledge/communications/protocols.md'
  - 'docs/knowledge/finance/README.md'
  - 'docs/knowledge/finance/rates.json'
  - 'docs/knowledge/finance/billing.json'
  - 'docs/knowledge/finance/accounting.md'
  - 'docs/leadership/README.md'
  - 'docs/leadership/VISION.md'
  - 'docs/leadership/DECISIONS.md'
  - 'docs/leadership/PRIORITIES.md'
  - 'docs/leadership/TEAM.md'

context_for_next_agent: |
  We have finished creating the agentic prompt system for Villa Thaifa.

  What was done:
  1. Complete backup of the project
  2. docs/agents/ structure created (context, handovers, capabilities)
  3. CLAUDE.md created as a single entry point (3 min read)
  4. Registry.json created with all metadata of the 17 agents
  5. Knowledge folders created with placeholders (client, property, processes, communications, finance)
  6. Leadership folder created with VISION, DECISIONS, PRIORITIES, TEAM
  7. Standardized frontmatter for all 17 agents with:
     - agent_id, version, status, created, modified, created_by
     - context_to_load (mandatory, domain_specific, mission_specific)
     - dependencies, tools, output_format, domain, tags, changelog

  What remains to be done:
  1. Fix obsolete paths (el-mountassir → omar-el-mountassir)
  2. Validate all symlinks are working
  3. Restore 10 unique files from archive/
  4. Organize the archive (legacy/history/restored)
  5. Final validation

  Gotchas:
  - Some files still have el-mountassir paths
  - Symlinks in docs/agents/context/mandatory/ are not created yet
  - The capabilities JSON files do not exist yet

findings_for_cto: |
  Implemented Architecture:
  - Modular system with standardized frontmatter
  - $DOCS/ variables for flexible reference
  - JSON Registry for programmatic querying
  - Standardized handover system

  Positives:
  - Coherent frontmatter allows automated parsing
  - Clear structure with 3 context levels
  - Registry allows automated inventory generation

  Possible improvements:
  - Implement $DOCS/ variable resolver
  - Create validation-links agent
  - Automate handover creation

  Identified problems:
  - Obsolete paths in browser-agent.md and claude-md-agent.md
  - Multiple nonexistent data/rooms/ and data/operations/ files referenced
  - Archive of 103 files to organize

  Lessons learned:
  - Standardize BEFORE creating
  - Use absolute paths or variables
  - Document handover format from the start
---
```

---

## Validation Checklist

Before saving the handover, check:

- [ ] All sections are filled
- [ ] `tasks_completed` lists all competed tasks
- [ ] `files_modified` lists ALL modified files
- [ ] `files_created` lists ALL created files
- [ ] `context_for_next_agent` is detailed and useful
- [ ] `findings_for_cto` contains technical decisions
- [ ] File name follows the format `<agent>-<timestamp>.md`

---

**Tags**: `handover` `template` `agent` `session`

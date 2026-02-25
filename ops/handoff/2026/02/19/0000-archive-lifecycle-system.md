# Handoff: Design Archive/Lifecycle System for Completed Work

## Status
Pending. Omar's major frustration: completed work never moves to archives. Everything stays in active directories making it impossible to distinguish done vs in-progress vs pending.

## Problem Statement
When agents complete tasks, research, decisions, or any time-bound work:
- Files stay in their original location forever
- No archival flow exists
- Decision docs marked "DECIDED" sit next to pending ones
- Research files from weeks ago clutter active directories
- Handoff files persist after they've been consumed
- Task graphs accumulate completed items
- No temporal dimension to file organization

This creates cognitive overload for Omar and confusion for agents about what's current vs historical.

## Scope
This is NOT just about file cleanup. It's about designing a SYSTEM that handles the full lifecycle:
1. Creation → Active use → Completion → Archive → (optional) Deletion
2. Applies to: research files, decision docs, handoff files, task graphs, session artifacts, HTML dashboards
3. Must work across ALL projects (not just villa-thaifa)
4. Must be automated where possible (hooks, post-task archival)

## Required Thinking Frameworks
Omar explicitly requested these skills be used:
- /systems-thinking — understand feedback loops, emergent behavior, system dynamics
- /sequential-thinking — step-by-step lifecycle design
- /brainstorming — explore creative archival approaches
- /decide — structured decision on the best approach

## Key Questions to Answer
1. Where do archived items go? (~/omar/archive/? project-local archive/? both?)
2. What triggers archival? (manual? hook-based on task completion? time-based?)
3. How do we preserve findability? (index files? search? tags?)
4. How do we distinguish "done and archived" from "done but still referenced"?
5. Should there be a retention policy? (auto-delete after N months?)
6. How does this interact with git? (archived files still in git history)

## Current Pain Points (Specific Examples)
- villa-thaifa/docs/repo-organization-decision.md has both completed and pending items
- ~/omar/knowledge/research/ has files from multiple sessions, no temporal organization
- villa-thaifa/docs/plans/ will accumulate handoff files that are consumed but never cleaned
- Task graphs have 30+ items mixing completed and pending
- ~/omar/artifacts/dashboards/ will grow unbounded

## Constraints
- Must follow rules.md "Preserve First" — archive, never delete without approval
- Must follow "Don't Delete Empty Taxonomy Dirs" — empty archive dirs are OK
- English only
- Delegate research to Gemini (hard rule)
- Complex output → HTML dashboard (output routing rule)

## Reference Files
- ~/.claude/rules/rules.md (Preserve First, Don't Delete Empty Taxonomy Dirs)
- ~/omar/knowledge/research/ (example of unmanaged research files)
- villa-thaifa/docs/plans/ (handoff files that will need lifecycle management)

## Instructions for Next Session
1. Read this file and rules.md
2. Run /systems-thinking to map the lifecycle system
3. Run /sequential-thinking to design the step-by-step flow
4. Run /brainstorming to explore approaches
5. Run /decide to choose the best approach
6. Implement the chosen approach (hooks, directory structure, automation)
7. Test on villa-thaifa as pilot

OUTPUT: Write the file. Report back file path only.

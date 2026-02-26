# Handoff — Villa Thaifa — 2026-02-26 01:54

## Summary

Massive governance + infrastructure session. Diagnosed and resolved Linear MCP integration (wrong tool prefix, plugin disabled), researched plugin vs manual setup (chose plugin), applied Linear-as-SOT decision globally (purged all TASKS.md references from universal.md, rules.md, project files), added Linear delegation rule to all 3 CLAUDE.md files. One manual fix remains (line 113 of ~/.claude/CLAUDE.md — hooks block agent edits).

## Open Work

- VT-94: Restructure data/ completely before app build — Phase 1 prerequisite, not started. No blockers.
- VT-95: Create VT app PRD/SRS — Phase 1, depends on data restructure completion.
- VT-96: Build VT app MVP (Said validation dashboard) — Phase 2, depends on PRD.
- ~/.claude/CLAUDE.md line 113: Last TASKS.md reference needs manual edit by Omar (hooks block agents).
- linear-ops.md prefix: After restart with plugin active, verify tool prefix and update agent definition if needed (may change from mcp**linear-server**_ to mcp**linear**_).

## Completed Work

- Diagnosed linear-ops agent failure: wrong MCP tool prefix (mcp**linear** vs mcp**linear-server**)
- Fixed linear-ops.md: corrected prefix to mcp**linear-server**\*, removed unnecessary ToolSearch step
- Tested fix: read tools work, write tools still fail (server-side auth issue with manual setup)
- Researched Linear MCP: plugin vs manual — comprehensive comparison (22+ tools, SSE deprecated, npm packages deprecated)
- Decision: switch to official plugin (linear@claude-plugins-official)
- Omar enabled plugin in settings.json + removed manual server from ~/.claude.json
- Audited global vs VT scope: found 2 P0 gaps (missing global delegation rule, stale TASKS.md refs)
- Fixed all 6 remaining TASKS.md references in universal.md
- Added Linear delegation rule to ~/.claude/CLAUDE.md and ~/omar/CLAUDE.md
- Verified rules.md has zero TASKS.md references
- Committed fixes to ~/omar/ repo (35b99f5)
- Generated HTML contradiction audit report
- Prior session (pre-compaction): Booking.com merge + Said corrections committed, handoff system designed + implemented, .agents/ migration, /end skill fix, behavioral self-improvement

## Decisions Made

- **Plugin over manual Linear MCP**: Plugin provides auto-lifecycle management, OAuth handling, auto-updates. Manual setup had auth issues with write operations. Same endpoint, same 22+ tools. Plugin wins.
- **Linear-as-SOT enforcement**: All TASKS.md references purged. Two-tier model: Linear (persistent) + TaskList (session-only). No third option.
- **Global scope for Linear rules**: Delegation rule added to all 3 CLAUDE.md files (VT, global, omar) — ensures any project gets Linear routing.

## Blockers

- **Linear MCP write operations**: Plugin enabled but requires restart + OAuth auth (`/mcp` command). Unblocks: restart Claude Code, run `/mcp`, authenticate.
- **~/.claude/CLAUDE.md line 113**: Hooks prevent agent edits. Unblocks: Omar edits manually (change `TASKS.md` → `Linear (persistent) or TaskList (session-only)`).

## Files Modified (uncommitted)

None in villa-thaifa repo (clean). Changes were in global files:

- ~/omar/CLAUDE.md — Added Linear delegation rule (committed: 35b99f5)
- ~/omar/core/resources/rules/universal.md — Fixed last TASKS.md reference (committed: 35b99f5)
- ~/.claude/agents/linear-ops.md — Fixed MCP tool prefix (not in git repo)
- ~/.claude/settings.json — Omar enabled linear plugin (not in git repo)
- ~/.claude.json — Omar removed manual linear-server (not in git repo)

## Files Read (key context)

- ~/.claude/agents/linear-ops.md — Root cause of create_issue failure
- ~/.claude/settings.json — Plugin status, allow patterns, deny patterns
- ~/.claude.json — Manual MCP server configuration
- /home/director/villa-thaifa/.claude/settings.local.json — VT-specific allow patterns
- ~/omar/core/resources/rules/universal.md — TASKS.md reference audit
- ~/.claude/rules/rules.md — TASKS.md reference verification
- ~/.claude/CLAUDE.md — Global config audit + last remaining TASKS.md ref
- ~/omar/core/context/domains/dev/linear-mcp-comparison.md — Research output from comparison agent
- ~/omar/core/context/domains/dev/linear-global-scope-audit.md — Audit output

## Artifacts

- ~/omar/artifacts/dashboards/linear-sot-contradiction-audit.html — Interactive HTML report of all 15 TASKS.md→Linear contradictions
- ~/omar/core/context/domains/dev/linear-mcp-comparison.md — 213-line comprehensive Linear MCP research
- ~/omar/core/context/domains/dev/linear-global-scope-audit.md — Global vs VT scope audit results

## Next Step

1. Restart Claude Code to activate Linear plugin
2. Run `/mcp` to authenticate Linear OAuth
3. Omar manually fixes ~/.claude/CLAUDE.md line 113: `TASKS.md` → `Linear (persistent) or TaskList (session-only)`
4. Test `linear-ops` agent with plugin prefix (verify create_issue works)
5. If prefix changed: update ~/.claude/agents/linear-ops.md accordingly
6. Then resume VT roadmap: VT-94 (data restructure) is Phase 1 priority

## Context for Resume

This session completed the Linear-as-SOT migration across all governance files. The root cause of linear-ops agent failures was a tool prefix mismatch (mcp**linear** vs mcp**linear-server**) compounded by the manual Linear MCP server having auth issues for write operations. Decision: switch to official Claude Code plugin. Omar enabled the plugin and removed the manual server — requires restart to activate. All TASKS.md references have been purged from universal.md and rules.md (zero remaining). Linear delegation rule added globally. One manual fix remains: ~/.claude/CLAUDE.md line 113 still says TASKS.md (hooks block agent edits). After restart + OAuth, linear-ops should be fully functional for the first time. The VT roadmap (Phase 1: data restructure, Phase 2: app MVP) can then proceed with proper Linear tracking.

## Metadata

| Field       | Value                                                                            |
| ----------- | -------------------------------------------------------------------------------- |
| Project     | Villa Thaifa                                                                     |
| Branch      | main                                                                             |
| Last Commit | dd40829 — feat(booking): sync elisabeth delacarte april reservations to local db |
| Session ID  | f36c6e80-1213-45da-9160-3d918d893f92                                             |
| Created     | 2026-02-26 01:54                                                                 |
| Type        | end                                                                              |

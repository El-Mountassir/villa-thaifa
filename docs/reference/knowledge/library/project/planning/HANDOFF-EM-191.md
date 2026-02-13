# Handoff: EM-191 Codebase Architecture Audit

**Updated**: 2026-01-30 23:10
**Linear Issue**: <https://linear.app/el-mountassir/issue/EM-191>
**Status**: Phase 1 COMPLETE — Ready for Phase 2

---

## ⚠️ READ SOUL.md FIRST

You are an **ORCHESTRATOR** — this is your IDENTITY, not a rule.

```
/gsd:execute-phase  # Delegate Phase 2 to agents
```

Do NOT write code yourself. Do NOT ask obvious questions. Just delegate and verify.

---

## Progress Summary

| Phase                   | Status  | Output                           |
| ----------------------- | ------- | -------------------------------- |
| Audit                   | ✅ DONE | `.planning/audit/*.md` (4 files) |
| Phase 1: Create SSOT    | ✅ DONE | `ssot/rooms.yaml`                |
| Phase 2: Sync script    | 🔄 NEXT | `scripts/sync-rooms.ts`          |
| Phase 3: Deprecate      | ⏳      | Add headers to old files         |
| Phase 4: Update imports | ⏳      | Point code to SSOT               |
| Phase 5: Placeholders   | ⏳      | Fill facilities data             |

---

## Key Files Created This Session

| File                                                    | Purpose                                      |
| ------------------------------------------------------- | -------------------------------------------- |
| `ssot/rooms.yaml`                                       | **THE SSOT** — 12 rooms, EUR+MAD, rate 10.72 |
| `.planning/audit/DATA-INVENTORY.md`                     | Complete data inventory                      |
| `.planning/audit/CONFLICT-MAP.md`                       | 4 conflicts identified                       |
| `.planning/audit/ARCHITECTURE-PROPOSAL.md`              | SSOT design                                  |
| `.planning/audit/CONSOLIDATION-PLAN.md`                 | 5-phase migration                            |
| `.planning/audit/REQUIREMENTS.md`                       | Owner requirements                           |
| `~/grid/memory/knowledge/patterns/currency-handling.md` | Currency patterns                            |

---

## Critical Findings

1. **EUR→MAD rate is 10.72** (not 11.0) — DB prices were inflated
2. **SSOT location**: `ssot/` at project root (not `data/ssot/`)
3. **Dual currency required** — store both EUR and MAD explicitly

---

## Next Instance: Start Here

```bash
# 1. Check Linear
/linear "show EM-191"

# 2. Use GSD to continue
/gsd:progress

# 3. Execute Phase 2
/gsd:execute-phase
```

Phase 2 task: Create `scripts/sync-rooms.ts` that:

- Reads `ssot/rooms.yaml`
- Generates `data/generated/rooms.json`
- Updates `property.db`

---

## Cleanup Needed (Manual)

- Delete `data/ssot/` (draft location, superseded by `ssot/`)

---

_Handoff by Claude instance, 2026-01-30 23:10_

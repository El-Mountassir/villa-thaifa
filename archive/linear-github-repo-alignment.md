# Linear-GitHub Repo Alignment Problem

**Discovered**: 2026-02-19
**Priority**: High — Linear links point to wrong repos
**Status**: Resolved

## Problem

Linear's GitHub integration and issue attachments reference repos that no longer match reality.

### Current GitHub State

| Repo                                             | Status               | Purpose                                              |
| ------------------------------------------------ | -------------------- | ---------------------------------------------------- |
| `omar-elmountassir/villa-thaifa`                 | **Active** (public)  | Current VT workspace (data + ops)                    |
| `El-Mountassir/villa-thaifa-property-management` | **Stale** (exists)   | Old VT repo, Linear links here                       |
| `omar-elmountassir/villa-thaifa-pms`             | **Active** (private) | Next.js PMS app (separate)                           |
| `omar-elmountassir/grid`                         | **Stale** (exists)   | Old monorepo, now `~/omar/` (NOT a git repo locally) |

### Issues

1. **Linear VT attachment links** point to `El-Mountassir/villa-thaifa-property-management` (VT-26 links to issue #3 there)
2. **GitHub issues** still open on old repos (#3, #4, #5 on old VT; #75, #76, #98 on grid)
3. **Linear GitHub integration** may be connected to the old repo, not the current one
4. **`~/omar/`** is not a git repo — grid repo exists on GitHub but local workspace is disconnected
5. **Org vs personal**: `El-Mountassir` (org?) vs `omar-elmountassir` (personal) — unclear relationship

### Decisions Needed

1. Archive or redirect `El-Mountassir/villa-thaifa-property-management`?
2. Archive or update `omar-elmountassir/grid`? Make `~/omar/` a repo?
3. Update Linear GitHub integration to point to `omar-elmountassir/villa-thaifa`?
4. Migrate/close stale GitHub issues on old repos?
5. Clarify `El-Mountassir` org relationship to `omar-elmountassir` account

### Approach

This needs a dedicated session with Linear + GitHub API investigation. Not blocking the current audit but blocks clean Linear-GitHub sync going forward.

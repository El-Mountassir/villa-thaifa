# GitHub Migration: Move villa-thaifa to El-Mountassir Org

**Decision**: Option B — Migrate repo to org (confirmed 2026-02-19)
**Linear Issues**: VT-42, VT-51, VT-55

---

## Pre-Flight Checks

- [x] Confirm you're logged into GitHub as `omar-elmountassir`
- [x] Confirm you have owner access to `El-Mountassir` org
- [x] Ensure no open PRs or active CI on the repo

---

## Step 1: Transfer Repo to Org

**Where**: https://github.com/omar-elmountassir/villa-thaifa/settings

1. Scroll to "Danger Zone"
2. Click "Transfer repository"
3. New owner: `El-Mountassir`
4. Confirm by typing the repo name
5. GitHub auto-creates a redirect from old URL

**CLI alternative**:

```bash
gh api repos/omar-elmountassir/villa-thaifa/transfer \
  -f new_owner=El-Mountassir \
  -f new_name=villa-thaifa
```

**Status: COMPLETED** (2026-02-19) — Repo now at https://github.com/El-Mountassir/villa-thaifa

---

## Step 2: Update Local Git Remote

```bash
cd ~/villa-thaifa
git remote set-url origin https://github.com/El-Mountassir/villa-thaifa.git
git remote -v  # verify
git fetch      # test connection
```

**Status: COMPLETED** (2026-02-19) — Remote updated and verified

---

## Step 3: Reconnect Linear GitHub Integration

**Where**: https://linear.app/el-mountassir/settings/integrations/github

1. Linear is already authorized on `El-Mountassir` org
2. The transferred repo should appear automatically
3. If not: disconnect and reconnect the GitHub integration
4. Select `El-Mountassir/villa-thaifa` as the linked repo

**Status: PARTIALLY VERIFIED** (2026-02-19)
- VT team correctly linked to `El-Mountassir/villa-thaifa` (confirmed via Linear settings page)
- Bi-directional issue sync WORKING (new Linear issues appear in GitHub)
- Branch auto-linking NOT confirmed — test branch `omar/vt-42-test` didn't show on VT-42 (likely because VT-42 was already synced with GitHub issue #2, causing a conflict)
- `omar-elmountassir` personal account also connected (redundant but harmless)
- EM team still linked to archived `villa-thaifa-property-management` — Omar should remove this connection

**Verify**: Create a test branch `omar/vt-42-test`, push it, check it shows in Linear VT-42, then delete it:

```bash
git checkout -b omar/vt-42-test
git push -u origin omar/vt-42-test
# Check Linear VT-42 for branch link
git checkout main
git push origin --delete omar/vt-42-test
git branch -d omar/vt-42-test
```

---

## Step 4: Archive Old Repo

**Where**: https://github.com/El-Mountassir/villa-thaifa-property-management/settings

1. Scroll to "Danger Zone"
2. Click "Archive this repository"
3. Confirm

**CLI alternative**:
```bash
gh repo archive El-Mountassir/villa-thaifa-property-management --yes
```

**Status: COMPLETED** (2026-02-19) — Old repo archived via `gh repo archive`

---

## Step 5: Update References

After migration, these files reference the old URL and need updating:

- `ops/intake/linear-github-repo-alignment.md` — mark as resolved
- `~/omar/knowledge/research/development/vt-42-github-integration-investigation.md` — mark as resolved
- `~/omar/knowledge/research/development/vt-51-github-identity-strategy.md` — mark decision as implemented

---

## Post-Migration Verification

- [x] `git push` works to new remote
- [~] Linear issue sync working, branch linking untested on clean issue
- [x] Old repo is archived (read-only)
- [x] GitHub redirect from old URL works

---

## Cleanup Remaining

1. **Remove old repo from EM team**: In Linear settings, disconnect `El-Mountassir/villa-thaifa-property-management` from EM team (repo is archived)
2. **Clean up test branch**: Run `git checkout main && git push origin --delete omar/vt-42-test && git branch -d omar/vt-42-test`
3. **Test branch linking on a clean issue**: Try pushing a branch referencing a NEW VT issue (not VT-42 which has a GitHub #2 conflict)
4. **Update Step 5 references**: Mark `ops/intake/linear-github-repo-alignment.md` as resolved
5. **Create Trip.com issue**: Trip.com GDA contract is still relevant — create new VT issue (VT-2 was canceled during audit)

---

## Linear Issues to Close After

- VT-42: Fix Linear GitHub integration — close as Done
- VT-51: GitHub identity strategy — close as Done
- VT-55: Archive old repo — close as Done

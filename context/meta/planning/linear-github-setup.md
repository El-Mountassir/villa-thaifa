# Linear ↔ GitHub Integration Setup Guide

> **Purpose**: Connect Villa Thaifa Linear issues to GitHub repo for automatic sync
> **Time Required**: 5 minutes
> **Created**: 2026-02-09

## Quick Setup (5 Steps)

### Step 1: Open Linear Settings

1. Go to [linear.app/el-mountassir](https://linear.app/el-mountassir)
2. Click **Settings** (gear icon, bottom left)
3. Navigate to **Integrations** → **GitHub**

### Step 2: Connect GitHub

1. Click **Connect GitHub**
2. Authorize Linear to access your GitHub account
3. Select **El-Mountassir** organization

### Step 3: Link Repository

1. Find `villa-thaifa-property-management` in the repo list
2. Click **Connect**
3. Map to **El Mountassir** team (or create a Villa Thaifa team)

### Step 4: Configure Auto-Linking

Enable these options:

- [x] **Auto-link branches** — Creates link when branch contains issue ID
- [x] **Auto-update status** — Moves issues through workflow on PR events
- [x] **Auto-close issues** — Closes issue when PR merges

### Step 5: Verify Connection

1. Create a test branch: `git checkout -b omar/test-LIN-279`
2. Push the branch
3. Check Linear issue LIN-279 — should show linked branch

---

## How Agents Use This

Once connected, agents follow this workflow:

```bash
# 1. Get issue from Linear
# Issue: EM-279 "Sign Trip.com GDA Contract"

# 2. Create branch with issue ID
git checkout -b agent/gemini/2026-02-09-EM-279

# 3. Make changes, commit
git commit -m "docs: add Trip.com GDA checklist

Fixes EM-279"

# 4. Push and create PR
git push -u origin agent/gemini/2026-02-09-EM-279
gh pr create --title "Add Trip.com GDA checklist" --body "Fixes EM-279"

# 5. Linear automatically:
#    - Links branch to issue
#    - Moves issue to "In Progress" on branch push
#    - Moves issue to "In Review" on PR open
#    - Moves issue to "Done" on PR merge
```

---

## Benefits for AI Agents

| Feature                | Benefit                           |
| ---------------------- | --------------------------------- |
| Auto-link branches     | No manual tracking needed         |
| Auto-update status     | Linear always reflects true state |
| Commit message parsing | `Fixes EM-XXX` auto-closes issues |
| PR comments visible    | Context flows both directions     |

---

## Troubleshooting

**Issue not linking?**

- Ensure branch name contains issue ID (e.g., `EM-279`)
- Or use commit message: `Fixes EM-279`

**Status not updating?**

- Check GitHub app has correct permissions
- Verify repo is connected in Linear settings

**Need to reconnect?**

- Settings → Integrations → GitHub → Disconnect → Reconnect

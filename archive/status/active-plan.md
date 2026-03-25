# Active Plan: Playwright Scout — Test Booking.com Access

> **Phase**: Step 1 — Access Test (IN PROGRESS)
> **Updated**: 2026-02-21

## Context

Scrape Booking.com Villa Thaifa to resolve open Said items. Before full extraction, test if Playwright can reach the page.

**Assets**:
- `playwright-cli` skill + Playwright 1.58.2
- URL: `https://www.booking.com/hotel/ma/riad-salim-amp-spa.html`
- Existing Dec 2025 scrape: `context/meta/knowledge/booking-com-data.md` (247 lines)
- ~30 open Said items in `data/admin/said-pending-questions.md`

**Output**: Enriched `booking-com-data.md`

---

## Step 1 — Access Test (GATE)

- [ ] Open browser via playwright-cli
- [ ] Navigate to Booking.com listing
- [ ] Verify real content (not CAPTCHA/block)

**PASS**: Snapshot has "Villa Thaifa", substantial content → proceed to Step 2.
**FAIL**: CAPTCHA/403/empty → STOP. Fallback: Chrome MCP or keep Dec 2025 data.

## Step 2 — Scout + Extract

- [ ] Snapshot full page, map sections
- [ ] Compare against Dec 2025 data (review count, scores, facilities, room details)
- [ ] Navigate to detail sections as needed
- [ ] Update `booking-com-data.md` via Edit
- [ ] Cross-ref `said-pending-questions.md`, mark resolvable items

## Follow-up

After this plan completes, next priorities are:
- Create `/audit` skill (generalize ssot-audit beyond YAML-only)
- Create `/consolidate` skill (audit → plan → gated execution)
- New repo audit cycle using the above skills

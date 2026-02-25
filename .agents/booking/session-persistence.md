# Booking.com Extranet — Session Persistence & Playwright Auth

> Research date: 2026-02-21
> Context: Villa Thaifa automation — avoid 2FA re-authentication on every Playwright run.

---

## 1. Booking.com 2FA Behavior

**Confirmed facts (multiple sources):**
- 2FA is mandatory on every login to `admin.booking.com` / `extranet.booking.com`.
- Booking.com may prompt 2FA **multiple times within 24 hours** depending on actions taken.
- Login uses credentials + PIN (via Pulse app or SMS).
- There IS a **"Remember me"** checkbox on the login form — reported by UpperKey/Lodgify guides.
  - Effect: unclear duration. Likely sets a persistent cookie to skip password re-entry but NOT 2FA.
- No documented "Trust this device / browser" option that bypasses the 2FA PIN step entirely.
- Session timeout is described as "aggressive" — the extranet logs out after inactivity.

**Implication for automation:** A fresh headless browser context (no cookies) triggers full login + 2FA
every time. You cannot automate away the 2FA PIN entry unless you have a TOTP secret (not the case
with SMS-based 2FA).

---

## 2. Playwright Session Persistence — Two Approaches

### Approach A: storageState JSON (recommended)

Save full browser state (cookies + localStorage + IndexedDB) after a manual login:

```javascript
// After successful manual login:
await page.context().storageState({ path: 'playwright/.auth/booking.json' });
```

Load that state in subsequent automated runs:

```javascript
const context = await browser.newContext({
  storageState: 'playwright/.auth/booking.json'
});
```

**CLI equivalent (codegen workflow):**
```bash
# Step 1: Login manually, save state
playwright codegen --save-storage=playwright/.auth/booking.json https://admin.booking.com

# Step 2: Reuse in subsequent recordings/runs
playwright codegen --load-storage=playwright/.auth/booking.json https://admin.booking.com
```

**storageState file structure:**
```json
{
  "cookies": [
    {
      "name": "...",
      "value": "...",
      "domain": ".booking.com",
      "path": "/",
      "expires": 1234567890,
      "httpOnly": true,
      "secure": true,
      "sameSite": "None"
    }
  ],
  "origins": [
    {
      "origin": "https://admin.booking.com",
      "localStorage": [{ "name": "...", "value": "..." }]
    }
  ]
}
```

### Approach B: Persistent User Data Directory (most reliable for MFA)

Playwright official recommendation for MFA/2FA accounts:

```bash
# Launch with persistent profile directory (headed, manual 2FA)
playwright open --user-data-dir=/home/director/villa-thaifa/tmp/booking-profile \
  https://admin.booking.com

# Subsequent automated runs reuse the same profile (cookies persist on disk)
playwright open --user-data-dir=/home/director/villa-thaifa/tmp/booking-profile \
  https://admin.booking.com/hotel/hoteladmin/...
```

In code:
```javascript
const context = await chromium.launchPersistentContext(
  '/home/director/villa-thaifa/tmp/booking-profile',
  { headless: false }  // headed for first login; can switch to true after
);
```

**Advantage over storageState:** The browser profile persists ALL state automatically on disk
between runs — no explicit save step needed after the initial login.

---

## 3. Specific Booking.com Cookie Names

No official documentation found for specific cookie names. From general observation:
- `OptanonConsent` — consent management cookie (CMP)
- Session auth cookies are likely scoped to `.booking.com` or `admin.booking.com`
- The "Remember me" feature likely sets a long-lived cookie (days to weeks)

**To discover actual cookie names:** After a manual login, inspect
`playwright/.auth/booking.json` or browser DevTools → Application → Cookies → `admin.booking.com`.

---

## 4. Recommended Workflow for Villa Thaifa

```
Step 1 (once): Manual login with 2FA
  → playwright open --user-data-dir=tmp/booking-profile https://admin.booking.com
  → Complete login + 2FA manually in the browser window
  → Close browser (profile saved to disk)

Step 2 (every run): Load profile, skip login
  → Launch with same --user-data-dir path
  → Session cookies from Step 1 are loaded automatically
  → If session expired: browser shows login page → repeat Step 1

Step 3 (session expiry): Re-authenticate
  → Booking.com sessions appear to expire within hours to ~1 day
  → No confirmed "remember for 30 days" mechanism found
  → Budget for periodic manual 2FA re-authentication
```

---

## 5. Key Limitations

| Limitation | Detail |
|---|---|
| 2FA cannot be fully automated | SMS-based PIN requires human intervention |
| Session duration unknown | Booking.com docs say "may prompt multiple times in 24h" — implies short sessions |
| Anti-bot measures | Booking.com blocks headless mode for public scraping; extranet may differ (you're authenticated) |
| Profile directory security | `tmp/booking-profile` contains live session — add to `.gitignore`, never commit |

---

## 6. Security Notes

- `playwright/.auth/booking.json` and `tmp/booking-profile/` contain live session credentials.
- Both are already in `.gitignore` conventions (`tmp/` is gitignored per repo config).
- Never commit session state files.

---

## Sources

- [Playwright Authentication Docs](https://playwright.dev/docs/auth)
- [Playwright CLI Docs (Python)](https://playwright.bootcss.com/python/docs/cli)
- [Playwright storageState Guide — BrowserStack](https://www.browserstack.com/guide/playwright-storage-state)
- [Playwright Cookies Guide — BrowserStack](https://www.browserstack.com/guide/playwright-cookies)
- [Booking.com Securing Your Account](https://partner.booking.com/en-us/help/legal-security/security/securing-your-account)
- [Booking.com Extranet Login Guide](https://partner.booking.com/en-us/help/account-and-log/settings/logging-bookingcom-extranet)
- [Booking.com What is 2FA](https://partner.booking.com/en-gb/help/legal-security/security/what-2-factor-authentication-2fa)
- [Playwright Login & Session Handling — ProsperaSoft](https://prosperasoft.com/blog/web-scrapping/playwright/playwright-login-session-scraping/)
- [Playwright Authentication — Checkly](https://www.checklyhq.com/docs/learn/playwright/authentication/)
- [Booking.com Extranet Complete Guide — UpperKey](https://www.theupperkey.com/post/booking-com-extranet-the-complete-guide)

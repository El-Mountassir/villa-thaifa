# Platform Credentials Guide

> **For AI Agents**: How to access and use platform credentials
> **Last Updated**: 2026-01-24

---

## 🔐 Credentials Location

**ALL platform credentials are stored in:** `.secrets/.env`

```bash
# File path (from project root)
/home/omar/omar-el-mountassir/projects/clients/villa-thaifa/.secrets/.env

# Read credentials
Read tool: .secrets/.env
```

**Reference structure:** `.env.example` (contains documentation and example format)

---

## 📋 Available Platforms

### 1. HotelRunner (Channel Manager)

**URL**: https://app.hotelrunner.com

**Admin Account (Omar)** - ⭐ USE THIS BY DEFAULT

```env
HOTELRUNNER_URL=https://app.hotelrunner.com
HOTELRUNNER_ADMIN_EMAIL=omar@el-mountassir.com
HOTELRUNNER_ADMIN_PASSWORD=[stored in .secrets/.env]
```

**Owner Account (Said)** - ⚠️ DO NOT USE unless explicitly requested

```env
HOTELRUNNER_OWNER_EMAIL=said_thaifa@hotmail.fr
HOTELRUNNER_OWNER_PASSWORD=[stored in .secrets/.env]
```

**Why use Admin account:**

- Avoids disturbing client with login notifications
- Maintains audit trail under consultant identity
- Client retains full owner privileges

### 2. Booking.com (OTA Extranet)

**URL**: https://admin.booking.com

**Admin Account (Omar)** - ⭐ USE THIS BY DEFAULT

```env
BOOKING_URL=https://admin.booking.com
BOOKING_ADMIN_EMAIL=omar@el-mountassir.com
BOOKING_ADMIN_PASSWORD=[stored in .secrets/.env]
```

**Owner Account (Said)** - ⚠️ DO NOT USE unless explicitly requested

```env
BOOKING_OWNER_EMAIL=said_thaifa@hotmail.fr
BOOKING_OWNER_PASSWORD=[stored in .secrets/.env]
```

---

## 🚨 Critical Rules for AI Agents

### Account Selection

**ALWAYS use ADMIN (Omar) accounts unless:**

- ❗ Omar explicitly requests using owner account
- ❗ Operation requires owner-level permissions
- ❗ Admin account is unavailable/locked

**NEVER use owner (Said) accounts for:**

- ❌ Routine operations
- ❌ Testing or exploration
- ❌ Data extraction or analysis
- ❌ Any non-critical operation

**Reason**: Owner receives login notifications → Avoids disturbing 78-year-old client unnecessarily

### Credential Security

**DO:**

- ✅ Read credentials from `.secrets/.env` at runtime
- ✅ Keep credentials in memory only during operation
- ✅ Never log credentials in output or files
- ✅ Never commit credentials to git

**DON'T:**

- ❌ Store credentials in variables across sessions
- ❌ Write credentials to any file
- ❌ Include credentials in screenshots or reports
- ❌ Share credentials in any form

---

## 🔑 How to Read Credentials

### Step 1: Read .secrets/.env file

```bash
# Using Read tool
Read(".secrets/.env")

# Parse environment variables
# Format: KEY=value (one per line)
```

### Step 2: Extract needed credentials

**Example for HotelRunner Admin:**

```
1. Read .secrets/.env
2. Find line starting with "HOTELRUNNER_ADMIN_EMAIL="
3. Extract value after "="
4. Repeat for HOTELRUNNER_ADMIN_PASSWORD
5. Use credentials for login
```

### Step 3: Use in automation

**With agent-browser:**

```bash
# Navigate to login
agent-browser open "$HOTELRUNNER_URL"

# Fill credentials (read from .secrets/.env)
agent-browser fill "input[name='email']" "$ADMIN_EMAIL"
agent-browser fill "input[type='password']" "$ADMIN_PASSWORD"

# Submit
agent-browser click "button[type='submit']"
```

---

## 🔐 Authentication Challenges

### OTP (One-Time Password)

**Both platforms send OTP via email on login**

**Process:**

1. Agent fills email/password
2. Platform sends OTP to email
3. **STOP** - Agent must request OTP from Omar
4. Omar provides OTP code
5. Agent fills OTP and continues

**Agent behavior:**

```
1. Detect OTP input field
2. Output: "OTP required. Check email: [email]"
3. WAIT for user to provide OTP
4. Continue with provided code
```

### reCAPTCHA

**May appear on login**

**Process:**

1. Agent detects reCAPTCHA
2. **STOP** - Cannot be solved by AI
3. Request Omar to solve manually
4. Continue after solved

**Agent behavior:**

```
1. Check for reCAPTCHA iframe/challenge
2. Output: "reCAPTCHA detected. Manual intervention required."
3. WAIT for user to solve
4. Continue after confirmation
```

---

## 📖 Credential Structure Reference

### .secrets/.env Format

```bash
# Platform credentials (real values)
HOTELRUNNER_URL=https://app.hotelrunner.com
HOTELRUNNER_ADMIN_EMAIL=omar@el-mountassir.com
HOTELRUNNER_ADMIN_PASSWORD=actual_password_here

HOTELRUNNER_OWNER_EMAIL=said_thaifa@hotmail.fr
HOTELRUNNER_OWNER_PASSWORD=actual_password_here

BOOKING_URL=https://admin.booking.com
BOOKING_ADMIN_EMAIL=omar@el-mountassir.com
BOOKING_ADMIN_PASSWORD=actual_password_here

BOOKING_OWNER_EMAIL=said_thaifa@hotmail.fr
BOOKING_OWNER_PASSWORD=actual_password_here
```

### .env.example (Documentation only)

**DO NOT use values from .env.example for real operations**

- Contains example/placeholder values only
- Serves as documentation and structure reference
- Real credentials are ONLY in .secrets/.env

---

## 🛡️ Security Best Practices

### For AI Agents

1. **Read on demand**: Only load credentials when needed
2. **Memory only**: Never persist to disk
3. **Scrub output**: Never include credentials in logs/reports
4. **Clear after use**: Don't retain in memory across operations
5. **Validate source**: Always read from `.secrets/.env`, never user input

### For Platform Operations

1. **Log actions**: Document what was done, not credentials used
2. **Admin account default**: Use Omar's account unless specified
3. **Audit trail**: All operations traceable to consultant
4. **Owner notification**: Avoid using Said's account unnecessarily
5. **Emergency access**: Owner accounts available if admin locked

---

## 🚀 Quick Reference for Agents

### Checklist Before Platform Operation

- [ ] Read `.secrets/.env` to get credentials
- [ ] Verify using ADMIN (Omar) account
- [ ] Understand OTP/reCAPTCHA may be required
- [ ] Prepare to request user input for challenges
- [ ] Never log or output credentials

### Common Tasks

**Task: Login to HotelRunner**

```bash
1. Read .secrets/.env
2. Extract HOTELRUNNER_ADMIN_EMAIL and HOTELRUNNER_ADMIN_PASSWORD
3. Navigate to HOTELRUNNER_URL
4. Fill credentials
5. Submit
6. Handle OTP if prompted
7. Confirm successful login
```

**Task: Login to Booking.com**

```bash
1. Read .secrets/.env
2. Extract BOOKING_ADMIN_EMAIL and BOOKING_ADMIN_PASSWORD
3. Navigate to BOOKING_URL
4. Fill credentials
5. Submit
6. Handle OTP if prompted
7. Confirm successful login
```

---

## 📚 Related Documentation

| Document                                                                         | Purpose                        |
| -------------------------------------------------------------------------------- | ------------------------------ |
| [`.env.example`](../../.env.example)                                             | Credential structure reference |
| [`.secrets/.env`](../../.secrets/.env)                                                 | Actual credentials (read-only) |
| [`STAKEHOLDERS.md`](../leadership/STAKEHOLDERS.md)                               | Account usage policy           |
| [`profiles/OMAR-EL-MOUNTASSIR.md`](../leadership/profiles/OMAR-EL-MOUNTASSIR.md) | Admin account ownership        |

---

## ❓ FAQ for AI Agents

**Q: Where are the credentials?**
A: In `.secrets/.env` at project root

**Q: Which account should I use?**
A: ADMIN (Omar) by default, OWNER (Said) only if explicitly requested

**Q: What if I need OTP?**
A: Stop and request code from Omar

**Q: Can I store credentials for reuse?**
A: No. Read fresh from `.secrets/.env` each time

**Q: What if admin account is locked?**
A: Ask Omar. Owner account available as backup.

**Q: How do I test without real credentials?**
A: You can't. `.env.example` values are placeholders only.

---

## 🔄 Maintenance

**File owner**: Omar El Mountassir
**Update frequency**: As needed when platforms/credentials change
**Last reviewed**: 2026-01-24

**When to update:**

- New platform added
- Credentials rotated
- Account structure changes
- Security policy updates

---

_Credential management guide for AI agents_
_Part of docs/operations/ - Operational procedures_
_Last updated: 2026-01-24_

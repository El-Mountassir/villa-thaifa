# Agent-Browser - Browser Automation CLI

**Status**: ✅ Installed & Operational
**Type**: CLI Tool (via Bash)
**Version**: Latest (installed Jan 2026)
**Installation**: Global (`npm install -g agent-browser`)

---

## Overview

Agent-browser is a fast headless browser automation CLI built with Rust + Node.js. It provides AI agents with full browser control capabilities via simple command-line interface.

**Key Features**:

- 🌐 Full browser automation (Chromium-based)
- 🎯 Semantic element targeting with refs (@e1, @e2...)
- 📸 Screenshots and PDF export
- 🔍 Accessibility tree snapshots for AI
- 📝 Form filling and interaction
- ⚡ Fast Rust performance with Node.js fallback
- 🔐 Session isolation and persistent profiles

---

## Quick Start

```bash
# Basic navigation
agent-browser open https://example.com

# Get page info
agent-browser get title
agent-browser get url

# Take screenshot
agent-browser screenshot output.png

# Close browser
agent-browser close
```

---

## Core Commands

### Navigation

```bash
# Open URL
agent-browser open https://example.com

# Navigate
agent-browser back
agent-browser forward
agent-browser reload

# Wait
agent-browser wait 2000        # Wait 2 seconds
agent-browser wait "button"    # Wait for element
```

### Element Interaction

```bash
# Click elements
agent-browser click "button.submit"
agent-browser click @e12              # Click by ref from snapshot

# Type and fill
agent-browser type "input" "Hello"
agent-browser fill "input" "Replace"  # Clear first, then type

# Other interactions
agent-browser hover "a.menu"
agent-browser focus "textarea"
agent-browser dblclick ".item"

# Checkboxes and dropdowns
agent-browser check "#agree"
agent-browser uncheck "#newsletter"
agent-browser select "select[name='country']" "France"

# File upload
agent-browser upload "input[type='file']" "/path/to/file.pdf"

# Drag and drop
agent-browser drag ".item" ".dropzone"
```

### Keyboard

```bash
# Press keys
agent-browser press Enter
agent-browser press Tab
agent-browser press "Control+a"
agent-browser press Escape

# Advanced
agent-browser mouse move 100 200
agent-browser mouse down left
agent-browser mouse up
```

### Scroll

```bash
agent-browser scroll down 500
agent-browser scroll up 200
agent-browser scrollintoview "footer"
```

---

## Data Extraction

### Get Information

```bash
# Get text content
agent-browser get text "h1"
agent-browser get text @e5

# Get HTML
agent-browser get html "article"

# Get attributes
agent-browser get attr href "a.link"
agent-browser get attr src "img"

# Get form values
agent-browser get value "input[name='email']"

# Get page info
agent-browser get title
agent-browser get url
agent-browser get count "div.item"    # Count elements

# Get element box (position/size)
agent-browser get box "button"

# Get computed styles
agent-browser get styles "div.card"
```

### Check State

```bash
agent-browser is visible "button"
agent-browser is enabled "input"
agent-browser is checked "#checkbox"
```

### Snapshots (AI-Optimized)

**The most powerful feature for AI agents:**

```bash
# Get interactive elements with refs
agent-browser snapshot -i

# Compact output (remove empty elements)
agent-browser snapshot -i -c

# Limit depth
agent-browser snapshot -i -c -d 2

# Scope to specific area
agent-browser snapshot -i -s ".main-content"

# JSON output for parsing
agent-browser snapshot -i --json
```

**Example output:**

```
- link "Home" [ref=e1]
- button "Submit" [ref=e2]
- textbox [ref=e3]
- link "Sign Up" [ref=e4]
```

**Then use refs to interact:**

```bash
agent-browser click @e2
agent-browser fill @e3 "user@example.com"
```

---

## Screenshots & Export

```bash
# Screenshot (viewport)
agent-browser screenshot output.png

# Full page screenshot
agent-browser screenshot --full page.png

# PDF export
agent-browser pdf document.pdf
```

---

## JavaScript Execution

```bash
# Execute JavaScript
agent-browser eval "document.title"
agent-browser eval "document.querySelectorAll('p').length"
agent-browser eval "window.scrollTo(0, 0)"

# Complex operations
agent-browser eval "Array.from(document.querySelectorAll('a')).map(a => a.href)"
```

---

## Advanced Features

### Sessions (Isolated Contexts)

```bash
# Named sessions for parallel automation
agent-browser --session user1 open https://site.com
agent-browser --session user2 open https://site.com

# Each session is completely isolated
```

### Persistent Profiles (Auth & Cookies)

```bash
# Use profile to persist login state
agent-browser --profile ~/.browser-profiles/work open https://gmail.com

# Login once, then reuse profile:
agent-browser --profile ~/.browser-profiles/work open https://gmail.com
# Already logged in!
```

⚠️ **KNOWN LIMITATION** (Discovered 2026-01-24):

**Issue**: Profile persistence may NOT work reliably for all websites

- Tested with HotelRunner: Session cookies NOT saved between executions
- Profile directory remains empty after browser close
- Re-authentication required each time

**Affected**: Complex auth systems, sites with specific cookie policies

**Workaround**: Keep browser session active OR use cookie export/import manually

**Status**: Under investigation - may be site-specific or tool limitation

**See**: [`sources/hotelrunner-api/TEST-RESULTS.md`](../hotelrunner-api/TEST-RESULTS.md) for detailed case study

### Network & Storage

```bash
# Manage cookies
agent-browser cookies get
agent-browser cookies set name=value
agent-browser cookies clear

# Local/session storage
agent-browser storage local
agent-browser storage session

# Network routing (mock responses)
agent-browser network route "*/api/*" --abort
agent-browser network route "*/data" --body '{"mock": true}'
agent-browser network unroute

# View requests
agent-browser network requests
agent-browser network requests --clear
```

### Tabs

```bash
agent-browser tab new
agent-browser tab list
agent-browser tab 2        # Switch to tab 2
agent-browser tab close
```

### Debugging

```bash
# Console logs
agent-browser console
agent-browser console --clear

# Page errors
agent-browser errors
agent-browser errors --clear

# Highlight element
agent-browser highlight "button"

# Record trace
agent-browser trace start trace.zip
# ... perform actions ...
agent-browser trace stop

# Record video
agent-browser record start video.webm
# ... perform actions ...
agent-browser record stop
```

### Browser Settings

```bash
# Viewport size
agent-browser set viewport 1920 1080

# Device emulation
agent-browser set device "iPhone 13"

# Geolocation
agent-browser set geo 48.8566 2.3522  # Paris

# Offline mode
agent-browser set offline on

# Custom headers
agent-browser set headers '{"Authorization": "Bearer token"}'

# Basic auth
agent-browser set credentials user pass

# Dark mode / reduced motion
agent-browser set media dark reduced-motion
```

---

## Complete Workflow Examples

### 1. Web Scraping

```bash
# Open page
agent-browser open https://news.ycombinator.com

# Get interactive elements
agent-browser snapshot -i -c > /tmp/elements.txt

# Click first article
agent-browser click @e12

# Get article content
agent-browser get text "article"

# Take screenshot
agent-browser screenshot --full /tmp/article.png

# Export PDF
agent-browser pdf /tmp/article.pdf

# Close
agent-browser close
```

### 2. Form Automation

```bash
# Open form
agent-browser open https://example.com/contact

# Get form elements
agent-browser snapshot -i

# Fill form
agent-browser fill @e3 "John Doe"
agent-browser fill @e4 "john@example.com"
agent-browser fill @e5 "Hello, this is a test message"

# Submit
agent-browser click @e6

# Wait for success
agent-browser wait ".success-message"

# Verify
agent-browser get text ".success-message"

# Close
agent-browser close
```

### 3. Login & Persistent Session

```bash
# First time - login and save profile
agent-browser --profile ~/.profiles/twitter open https://twitter.com
agent-browser snapshot -i
agent-browser fill @e_username "myusername"
agent-browser fill @e_password "mypassword"
agent-browser click @e_submit
agent-browser wait 5000  # Wait for login
agent-browser close

# Next time - already logged in
agent-browser --profile ~/.profiles/twitter open https://twitter.com
# Already authenticated!
```

### 4. Data Collection with JSON

```bash
# Open page
agent-browser open https://example.com/products

# Get structured data
agent-browser snapshot -i --json > /tmp/products.json

# Process with jq or Python
cat /tmp/products.json | jq '.data.refs'

# Extract specific data via JS
agent-browser eval "Array.from(document.querySelectorAll('.price')).map(p => p.textContent)"

# Close
agent-browser close
```

### 5. Monitoring & Screenshots

```bash
# Open site
agent-browser --session monitor open https://status.example.com

# Take screenshot
agent-browser --session monitor screenshot --full /tmp/status-$(date +%s).png

# Get status text
agent-browser --session monitor get text ".status"

# Keep session open for next check
# (don't close, reuse session)
```

---

## Best Practices

### 1. Always Close Sessions

```bash
# Bad
agent-browser open https://site.com
# ... work ...
# (browser left open)

# Good
agent-browser open https://site.com
# ... work ...
agent-browser close
```

### 2. Use Refs for Reliability

```bash
# Less reliable (CSS selectors can change)
agent-browser click "button.submit"

# More reliable (semantic refs from snapshot)
agent-browser snapshot -i -c
agent-browser click @e12  # Button labeled "Submit"
```

### 3. Chain Commands

```bash
# Efficient - single bash invocation
agent-browser open https://example.com && \
  agent-browser get title && \
  agent-browser screenshot output.png && \
  agent-browser close

# Less efficient - multiple calls
agent-browser open https://example.com
agent-browser get title
agent-browser screenshot output.png
agent-browser close
```

### 4. Use Sessions for Parallel Tasks

```bash
# Monitor multiple sites simultaneously
agent-browser --session site1 open https://site1.com &
agent-browser --session site2 open https://site2.com &
agent-browser --session site3 open https://site3.com &
wait
```

### 5. Persistent Profiles for Auth

```bash
# Reuse authentication across sessions
agent-browser --profile ~/.profiles/gmail open https://gmail.com
# No need to login every time
```

### 6. JSON Output for Parsing

```bash
# Get structured data
agent-browser snapshot -i --json | jq '.data.refs | length'
agent-browser get text "h1" --json
```

---

## Environment Variables

```bash
# Set default session
export AGENT_BROWSER_SESSION="my-session"

# Custom browser executable
export AGENT_BROWSER_EXECUTABLE_PATH="/usr/bin/chromium"

# User agent
export AGENT_BROWSER_USER_AGENT="Custom Bot 1.0"

# Proxy
export AGENT_BROWSER_PROXY="http://proxy.example.com:8080"
export AGENT_BROWSER_PROXY_BYPASS="localhost,*.internal.com"
```

---

## Troubleshooting

### Browser Not Found

```bash
# Reinstall Chromium
agent-browser install
agent-browser install --with-deps  # Linux
```

### Element Not Found

```bash
# Use snapshot to see available elements
agent-browser snapshot -i -c

# Wait for element to appear
agent-browser wait "button.submit"
agent-browser click "button.submit"
```

### Timeouts

```bash
# Increase wait time
agent-browser wait 10000  # 10 seconds

# Or use multiple waits
agent-browser wait ".loading"
agent-browser wait 5000
agent-browser snapshot -i
```

### Session Conflicts

```bash
# Use unique session names
agent-browser --session task1 open https://site.com
agent-browser --session task2 open https://site.com

# Or clear sessions
pkill -f agent-browser
```

---

## Performance Tips

1. **Reuse sessions** instead of opening/closing repeatedly
2. **Use headless mode** (default) for faster execution
3. **Limit snapshot depth** with `-d` flag for faster parsing
4. **Use compact snapshots** with `-c` for less output
5. **Scope snapshots** with `-s` to specific areas

---

## Integration with Craft Agent

### Via Bash Tool

```typescript
// In Craft Agent, use Bash tool:
Bash({
  command:
    "agent-browser open https://example.com && agent-browser snapshot -i -c",
  description: "Open site and get interactive elements",
});
```

### Common Patterns

```bash
# Pattern 1: Quick data extraction
agent-browser open URL && agent-browser get text SELECTOR && agent-browser close

# Pattern 2: Form automation
agent-browser open URL && \
  agent-browser snapshot -i && \
  agent-browser fill @eX "value" && \
  agent-browser click @eY && \
  agent-browser close

# Pattern 3: Screenshot capture
agent-browser open URL && \
  agent-browser screenshot --full output.png && \
  agent-browser close

# Pattern 4: Persistent monitoring
agent-browser --session monitor --profile ~/.profiles/monitor open URL
# Keep open, check periodically
```

---

## Resources

- **CLI Help**: `agent-browser --help`
- **Website**: https://agent-browser.dev
- **GitHub**: https://github.com/vercel-labs/agent-browser
- **Installation**: `npm install -g agent-browser`

---

**Last Updated**: January 24, 2026
**Status**: Production Ready ✅

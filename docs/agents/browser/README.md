# 🌐 Agent Browser - CLI Tool

**Headless browser automation for AI agents**

## Status

✅ **Installed & Operational** (Jan 24, 2026)

## What is it?

Agent-browser is a fast CLI for browser automation built by Vercel Labs. It gives Craft Agent full control over a headless Chromium browser via simple bash commands.

## Quick Test

```bash
agent-browser open https://example.com
agent-browser get title
agent-browser screenshot test.png
agent-browser close
```

## Usage in Craft Agent

Use via the **Bash** tool:

```typescript
Bash({
  command:
    "agent-browser open https://site.com && agent-browser snapshot -i -c",
  description: "Get interactive elements from site",
});
```

## Key Features

- 🌐 Navigate web pages
- 🖱️ Click, type, fill forms
- 📸 Take screenshots & export PDFs
- 🎯 Semantic element targeting (@e1, @e2...)
- 🔐 Persistent sessions & profiles
- ⚡ Fast Rust + Node.js implementation

## Documentation

See [`guide.md`](./guide.md) for complete documentation with examples and best practices.

## Installation

Already installed globally:

```bash
npm install -g agent-browser
agent-browser install --with-deps
```

## Resources

- **Help**: `agent-browser --help`
- **Website**: https://agent-browser.dev
- **GitHub**: https://github.com/vercel-labs/agent-browser

---

**Installed**: January 24, 2026
**Version**: Latest
**Location**: `/usr/local/bin/agent-browser`

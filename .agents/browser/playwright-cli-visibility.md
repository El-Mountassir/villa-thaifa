# Playwright CLI Visibility Research

## Question
Can Playwright CLI run in headed/visible mode to show the browser?

## Answer: YES

### Headed Mode Flag

**`playwright open` is HEADLESS by default.** To see the browser, pass the `--headed` flag:

```bash
playwright-cli open https://example.com --headed
```

### Key Findings

1. **Default behavior**: `playwright-cli open` runs headless (no visible browser)
2. **Headed mode**: `--headed` flag enables browser visibility
3. **Session persistence**: Browsers use dedicated persistent profiles by default (cookies/storage preserved between commands)
4. **Environment variable**: Can set `PLAYWRIGHT_CLI_SESSION=session-name` to manage sessions

### Playwright CLI vs Chrome MCP

| Tool | Browser Visibility | Use Case |
|------|-------------------|----------|
| **playwright-cli** | Headless by default, `--headed` for visible | Token-efficient for agents, CLI-focused |
| **Chrome MCP** | Always visible to user | Visual feedback, interactive inspection |

**Token efficiency**: playwright-cli avoids loading large DOM trees into LLM context (more efficient for agents working with large codebases).

### Related Configuration

Headed mode can also be set in `playwright-cli.json`:
```json
{
  "browser": {
    "launchOptions": {
      "headless": false
    }
  }
}
```

---

**Source**: Playwright CLI GitHub docs (microsoft/playwright-cli) §Headed operation

# 🤖 Villa Thaifa Agent Fleet (Registry)

> **Location**: `.claude/agents/` > **Framework**: **Claude Code CLI** (Sub-agents)
> **Orchestrator**: Antigravity (via Terminal)

---

## 🛠️ Specialized Agents (The "Special Forces")

> **Note**: These agents are strictly **Claude Code** configurations.
> **Invocation**: `claude -p "Use @agent-name to..."` or `claude @agent-name`

### 🏢 Operations & Business

| Agent                     | Role            | Capabilities                       | Model  |
| :------------------------ | :-------------- | :--------------------------------- | :----- |
| **`pricing-analyst`**     | Revenue Manager | Market analysis, Rate optimization | Opus   |
| **`reservation-manager`** | Booking Agent   | Reservation lifecycle, Upsell      | Sonnet |
| **`calendar-agent`**      | Scheduler       | Availability checks, Gap analysis  | Sonnet |
| **`guest-communicator`**  | Concierge       | Drafting messages, Welcome guides  | Sonnet |

### ⚙️ Technical & Audit

| Agent                    | Role       | Capabilities                         | Model  |
| :----------------------- | :--------- | :----------------------------------- | :----- |
| **`platform-validator`** | Gatekeeper | Pre-flight checks, Safety validation | Sonnet |
| **`data-sync-checker`**  | Integrity  | SSOT vs Platform discrepancy check   | Sonnet |
| **`security-auditor`**   | SecOps     | Vulnerability scanning, Auth review  | Opus   |
| **`incident-reporter`**  | Logger     | Error tracking, Post-mortems         | Haiku  |

### 🚀 Utility & Meta

| Agent                 | Role      | Capabilities                                | Model  |
| :-------------------- | :-------- | :------------------------------------------ | :----- |
| **`meta-agent`**      | Architect | **Creating NEW agents (Self-replication)**  | Opus   |
| **`browser-agent`**   | Navigator | Web scraping, UI testing (Antigravity Core) | Sonnet |
| **`research-agent`**  | Scout     | Documentation search, Fast info gathering   | Haiku  |
| **`claude-md-agent`** | Librarian | Maintaining `CLAUDE.md` / `GEMINI.md`       | Opus   |

---

## 📜 Usage Protocol

1.  **Define the Task**: "I need to check room availability."
2.  **Select the Agent**: "`calendar-agent` is best for this."
3.  **Context Injection**: `claude @.claude/agents/calendar-agent.md "Check availability for..."`
4.  **Verification**: Antigravity reviews the output.

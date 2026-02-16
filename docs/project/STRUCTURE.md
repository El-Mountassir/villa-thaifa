# Project Structure (v5)

```sh
thaifa/
├── .claude/              # 🎭 Orchestrator config
├── ai/                   # 🤖 AI systems
│   ├── agentic/core/     # Contexts, models, prompts, tools
│   ├── pieplines/        # Pipelines (RAG, etc)
│   ├── knowledge/        # Knowledge graphs
│   ├── memory/           # Vector stores

├── archive/              # 📦 Historical data (YYYY/QQ/)
├── data/                 # 📊 All data
│   ├── admin/client/     # Credentials, contacts, profile
│   ├── specs/            # Business specs (hotel, promotions, platform)
│   └── communication/    # WhatsApp messages
├── docs/                 # 📚 Documentation, workflows
├── infra/                # 🏗️ Docker, environments (on peut focus en local pour l'instant..)
├── project/              # 🎯 TODOs, milestones
└── src/                  # 💻 Source code (apps, packages, tools) (│   └── analytics/        # Business dashboards)
```

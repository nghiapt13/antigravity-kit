# Antigravity Kit 🚀

> **The "Native Gemini" Agentic Framework.**
> Built to turn your IDE into an autonomous coding partner.

**Antigravity Kit** activates a suite of specialized AI Agents directly within your editor. It leverages Gemini's 2M context window to understand your entire project at once.

---

## ⚡ Quick Start

### 1. Installation

We have simplified the setup process into a single command.

Run inside your project directory:

```bash
npx @nghiapt/kit
```

This interactive wizard will:
1.  **Install Global (Recommended)**: Installs workflows globally (`~/.gemini/antigravity/global_workflows`), making them available in ALL your projects.
2.  **Install Local**: Installs workflows only into the current project's `.agent/workflows` folder.


### 2. Using Agents (The "Slash" Workflow)
Use the **Slash Command** menu in your IDE chat (type `/`) to summon specialized agents.

| Command | Agent Specialist | Task Examples |
| :--- | :--- | :--- |
| **`/orchestrator`** | **The Project Manager** | "Build a Todo App from scratch", "Refactor the auth system" |
| **`/frontend-development`** | **UI/UX Engineer** | "Create a responsive navbar", "Fix mobile layout issues" |
| **`/backend-development`** | **Backend Engineer** | "Set up a FastAPI server", "Design a Postgres schema" |
| **`/fix-bugs`** | **Debugger** | "Why is the screen white?", "Fix the API 500 error" |

---

## 🤖 "God Mode" (Auto-Automation)

To let agents code, run tests, and fix bugs without asking for permission every step:

1.  **Recommended**: Install the **Auto Accept Agent** extension (by MunKhin).
2.  **Manual**: Set **Terminal & File Edits** to `Always Allow` in your Agent settings.

> **⚠️ Warning:** Only enable these settings if you trust the agent.

---

## 📂 Architecture
- **Workflows**: 30+ Agent Personas available via slash commands.
- **Core**: Powered by Google Gemini.

## ⚠️ Credits & Disclaimer
**Inspiration**: This project acknowledges the architectural patterns from **ClaudeKit**.
**Native Implementation**: **Antigravity Kit** is a clean-room implementation written **from scratch** to optimize for Google Gemini.

**License**: MIT.

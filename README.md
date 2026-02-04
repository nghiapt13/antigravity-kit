# Antigravity Kit 🚀

> **The "Native Gemini" Agentic Framework.**
> Built to turn your IDE into an autonomous coding partner.

**Antigravity Kit** activates a suite of specialized AI Agents directly within your editor. It leverages Gemini's 2M context window to understand your entire project at once.

---

## ⚡ Quick Start

### 1. Installation
1.  **Clone this repo** into your workspace.
2.  **Install Dependencies**:
    ```powershell
    pip install -r requirements.txt
    ```
3.  **Initialize Reference**:
    ```powershell
    .\at init
    ```
    ```
    *(This creates the necessary config for the agents)*

### 1.5. Configure API Key (Required)
You need a Google Gemini API Key to power the agents.
1.  Get a key from [Google AI Studio](https://aistudio.google.com/).
2.  Open `.antigravity/config.json` and paste your key:
    ```json
    {
      "api_key": "YOUR_GEMINI_API_KEY_HERE",
      "model": "gemini-2.0-flash-exp",
      ...
    }
    ```


### 2. Using Agents (The "Slash" Workflow)
Use the **Slash Command** menu in your IDE chat (type `/`) to summon specialized agents.

| Command | Agent Specialist | Task Examples |
| :--- | :--- | :--- |
| **`/orchestrator`** | **The Project Manager** | "Build a Todo App from scratch", "Refactor the auth system" |
| **`/frontend-development`** | **UI/UX Engineer** | "Create a responsive navbar", "Fix mobile layout issues" |
| **`/backend-development`** | **Backend Engineer** | "Set up a FastAPI server", "Design a Postgres schema" |
| **`/fix-bugs`** | **Debugger** | "Why is the screen white?", "Fix the API 500 error" |
| **`/code-review`** | **Security Auditor** | "Review this file for security holes" |
| **`/devops`** | **SRE / DevOps** | "Write a Dockerfile", "Create a CI pipeline" |

> **💡 Pro Tip:** You don't need to explain *how* to code. Just select the right agent and tell them *what* you want. They have read the manual.

### 3. "God Mode" (Auto-Automation)
To let agents code, run tests, and fix bugs without asking for permission every step:
1.  Install the **auto-accept-agent** extension (Recommended).
2.  Or manually set **Terminal & File Edits** to `Always Allow` in settings.

> **[👉 READ THE FULL INSTALLATION & SETTINGS GUIDE](INSTALL.md)**

---

## 📂 Architecture
- **`workflows/`**: The "Brains". Contains 30+ Agent Personas available via slash commands.
- **`core/`**: The "Engine". Powered by Python and Google Gemini.
- **`at.bat`**: CLI wrapper (for power users who prefer terminal).

---

## ⚠️ Credits & Disclaimer
**Inspiration**: This project acknowledges the architectural patterns from **ClaudeKit** (Codestory).
**Native Implementation**: **Antigravity Kit** is a clean-room implementation written **from scratch** to optimize for Google Gemini's distinct capabilities. It shares workflow naming conventions for familiarity but contains **zero** proprietary code from the original kit.

**License**: MIT.

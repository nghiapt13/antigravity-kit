# 🚀 Installation & Setup Guide

**Antigravity Kit** is a "Native Gemini" agentic framework, built from scratch to leverage the 2M+ token context window of Google Gemini.

> **Note & Disclaimer:**
> This project is inspired by the architecture of **ClaudeKit** (by Codestory/Goon Nguyen). However, **Antigravity Kit** is a completely independent, clean-room implementation written from scratch (`from scratch`) to optimize for Gemini's specific capabilities (Multimodality & Long Context). It shares the *spirit* and *workflow names* for familiarity but contains **zero** proprietary code from the original kit.

---

## ⚡ 1. The "One Command" Setup

We believe in speed. To start a new project with a full team of AI Agents:

1.  **Clone this repo** (or download the release).
2.  **Run the Installer** to set up the `at` command globally:
    ```powershell
    .\install.ps1
    ```

### Start a Project
Open your terminal in your empty project folder and run:

```powershell
.\at init
```

*That's it.* This will:
- Scanner the directory.
- Create `.antigravity/` config.
- Create `memory-bank/` for agent memory.

---

## 🤖 2. Enable "God Mode" (Full Automation)

To let Antigravity Agents work at 100% speed (coding, testing, fixing bugs automatically), you need to configure your IDE (Antigravity / Cline) to **Stop Asking for Permission**.

### A. Recommended Extension (Optional but Faster)
We recommend installing the **Auto Accept Agent** extension to quickly toggle these settings.
1.  Open **Extensions** in your IDE.
2.  Search for **`MunKhin.auto-accept-agent`**.
3.  **Right-click** on the Antigravity file/window -> Install.

### B. Manual Configuration (The "Pro" Setup)
If you prefer manual setup, match these settings in **Settings > Agent**:

| Setting | Value | Why? |
| :--- | :--- | :--- |
| **Secure Mode** | **OFF** ⚪ | Allows the agent to run complex chains without blocking. |
| **Review Policy** | **Always Proceed** | Agent won't nag you to review every markdown file. |
| **Terminal Auto Exec** | **Always Proceed** | **Critical.** Allows the agent to run tests, git, and installs autonomously. |
| **Browser Tools** | **Enabled** 🔵 | Allows the agent to "see" your web app and verify UI. |
| **Browser JS Policy** | **Always Proceed** | Allows full DOM interaction for testing. |

> **⚠️ Warning:** Only enable these settings if you trust the agent (which is running *your* API key). This turns the AI into a fully autonomous engineer.

---

## 🎮 3. Usage Examples

Once installed, use the `at` command to summon agents:

**Complex Task (Use the Orchestrator):**
```bash
.\at orchestrator "Build a Landing Page with Tailwind and framer-motion"
```
*(The Orchestrator will plan, then call the Coder, then the Reviewer automatically)*

**Quick Fix:**
```bash
.\at debugging "Fix the white screen error on startup"
```

**Architectural Plan:**
```bash
.\at planning "How should we structure the database for high scale?"
```

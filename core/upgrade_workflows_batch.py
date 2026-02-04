import os
from pathlib import Path

# The Header that turns any doc into an Agent
ANTIGRAVITY_HEADER = """
# Antigravity Native Protocol
> **SYSTEM OVERRIDE**: Use the following rules as your Primary Directive.

1.  **Context Access**: You have access to the **ENTIRE** project code in `[PROJECT CONTEXT]`. Read it to understand the codebase. Do not ask for files.
2.  **Agentic Behavior**: You are NOT a documentation reader. You are an **ACTOR**.
    - If the user asks for code, **WRITE IT**.
    - If the user asks for a fix, **RUN THE TEST** and **FIX IT**.
3.  **Automation**: Use `run_command` freely to install, build, and test.
4.  **Chaining**: If you need to switch modes (e.g., from Planning to Coding), use `python core/engine.py [workflow_name]`.

---
"""

def upgrade_workflows():
    workflows_dir = Path(r"d:\antigravity-kit\workflows")
    
    # Files we already manually fixed or shouldn't touch
    skip_list = ["template_agent.md", "backend-development.md", "fix-bugs.md", "orchestrator.md", "planning.md", "router.md"]

    for f in workflows_dir.glob("*.md"):
        if f.name in skip_list:
            continue
            
        content = f.read_text(encoding='utf-8', errors='ignore')
        
        # Avoid double injection
        if "# Antigravity Native Protocol" in content:
            print(f"Skipping {f.name} (Already Upgraded)")
            continue
        
        # Inject after Frontmatter
        if content.startswith("---"):
            # Find end of frontmatter
            parts = content.split("---", 2)
            if len(parts) >= 3:
                new_content = f"---{parts[1]}---\n{ANTIGRAVITY_HEADER}\n{parts[2]}"
                f.write_text(new_content, encoding='utf-8')
                print(f"🚀 Upgraded: {f.name}")
        else:
            # No frontmatter? Just prepend.
            f.write_text(ANTIGRAVITY_HEADER + content, encoding='utf-8')
            print(f"🚀 Upgraded: {f.name}")

if __name__ == "__main__":
    upgrade_workflows()

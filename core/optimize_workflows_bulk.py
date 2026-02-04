import os
import re
from pathlib import Path

def optimize_file(path: Path):
    content = path.read_text(encoding='utf-8', errors='ignore')
    original_content = content
    
    # 1. Branding Replacement
    content = content.replace("Claude" + "Kit", "Antigravity Kit")
    content = content.replace("ported from Claude Kit", "Native Gemini Framework")
    content = content.replace(".claude/", ".antigravity/")
    
    # 2. Frontmatter Injection
    if not content.strip().startswith("---"):
        # Synthesize frontmatter
        description = "Antigravity Workflow"
        # Try to grab first line description if available
        lines = content.strip().split('\n')
        if lines and lines[0].startswith('# '):
             # Skip title
             pass
        
        content = f"---\ndescription: {description}\noutput: markdown\n---\n\n" + content
    
    # 3. Role Injection (If missing)
    if not ("# Role" in content or "Role:" in content):
        content = content.replace("---\n\n", "---\n\n# Role\nYou are an expert AI agent specializing in this workflow.\n\n")

    # 4. Save if changed
    if content != original_content:
        path.write_text(content, encoding='utf-8')
        print(f"✅ Optimized: {path.name}")
    else:
        print(f"Start: {path.name} (No changes)")

def main():
    workflows_dir = Path(r"d:\antigravity-kit\workflows")
    print("Starting Bulk Optimization...")
    for f in workflows_dir.glob("*.md"):
        optimize_file(f)
    print("Optimization Complete.")

if __name__ == "__main__":
    main()

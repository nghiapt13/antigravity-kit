import os
import sys
import json
from pathlib import Path

def init_project(target_dir: str = "."):
    root = Path(target_dir).resolve()
    print(f"Initializing Antigravity Project in: {root}")
    
    # 1. Create .antigravity config dir
    config_dir = root / ".antigravity"
    config_dir.mkdir(exist_ok=True)
    
    # 2. Create config file
    config_file = config_dir / "config.json"
    if not config_file.exists():
        config = {
            "model": "gemini-2.0-flash-exp",
            "context_ignore": [],
            "memory_bank_path": "memory-bank"
        }
        with open(config_file, 'w') as f:
            json.dump(config, f, indent=2)
        print("Created .antigravity/config.json")
        
    # 3. Create Memory Bank (Generic Best Practice)
    bank_dir = root / "memory-bank"
    bank_dir.mkdir(exist_ok=True)
    
    files = {
        "projectbrief.md": "# Project Brief\n\n[Describe the project goals here]",
        "activeContext.md": "# Active Context\n\n[Current work in progress]",
        "progress.md": "# Progress\n\n- [ ] Init project"
    }
    
    for filename, content in files.items():
        p = bank_dir / filename
        if not p.exists():
            with open(p, 'w') as f:
                f.write(content)
            print(f"Created memory-bank/{filename}")

    # 4. Create .gitignore if needed
    gitignore = root / ".gitignore"
    if gitignore.exists():
        current_content = gitignore.read_text()
        if ".antigravity" not in current_content:
            with open(gitignore, 'a') as f:
                f.write("\n.antigravity/\n")
            print("Added .antigravity to .gitignore")
    else:
        with open(gitignore, 'w') as f:
            f.write(".antigravity/\n")
        print("Created .gitignore")

    print("\n✅ Antigravity Project Initialized!")
    print("Run `python path/to/antigravity-kit/core/engine.py plan 'Your Goal'`")

if __name__ == "__main__":
    target = sys.argv[1] if len(sys.argv) > 1 else "."
    init_project(target)

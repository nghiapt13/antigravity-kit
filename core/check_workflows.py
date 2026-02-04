import os
import re
from pathlib import Path

def check_workflows():
    workflows_dir = Path(r"d:\antigravity-kit\workflows")
    print(f"Checking workflows in {workflows_dir}...")
    
    passed = 0
    failed = 0
    
    for f in workflows_dir.glob("*.md"):
        content = f.read_text(encoding='utf-8', errors='ignore')
        
        # Check for Frontmatter
        has_frontmatter = content.strip().startswith("---")
        
        # Check for Role/Task (Antigravity Native indicators)
        has_role = "# Role" in content or "Role:" in content
        has_task = "# Task" in content or "Task:" in content or "# Process" in content
        
        if has_frontmatter:
            # print(f"✅ {f.name}: Valid Frontmatter")
            passed += 1
        else:
            print(f"⚠️  {f.name}: MISSING Frontmatter (Legacy?)")
            failed += 1
            
    print(f"\nSummary: {passed} Passed, {failed} Potential Legacy Format")

if __name__ == "__main__":
    check_workflows()

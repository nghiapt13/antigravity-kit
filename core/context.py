import os
from pathlib import Path
from typing import List, Set
# No external deps if possible, or use standard lib

# Default ignores
IGNORED_DIRS = {
    '.git', '.idea', '.vscode', '__pycache__', 'node_modules', 
    'venv', 'env', 'dist', 'build', 'coverage', '.next', '.nuxt',
    '.output', 'target', 'bin', 'obj'
}

IGNORED_EXTS = {
    '.pyc', '.pyo', '.pyd', '.so', '.dll', '.exe', '.bin', 
    '.jpg', '.jpeg', '.png', '.gif', '.ico', '.svg', '.mp4', 
    '.mp3', '.pdf', '.zip', '.tar', '.gz', '.7z', '.rar',
    '.db', '.sqlite', '.sqlite3', '.pkl', '.lock'
}

IGNORED_FILES = {
    'package-lock.json', 'yarn.lock', 'pnpm-lock.yaml', 'poetry.lock',
    'Gemfile.lock', 'composer.lock', 'cargo.lock'
}

def is_ignored(path: Path) -> bool:
    if path.name in IGNORED_FILES:
        return True
    if path.suffix in IGNORED_EXTS:
        return True
    # Check parts for ignored dirs
    if any(part in IGNORED_DIRS for part in path.parts):
        return True
    return False

def get_project_files(root_dir: str) -> List[Path]:
    """Scans the project for text files, respecting ignore rules."""
    root = Path(root_dir)
    files = []
    
    # Simple walk
    for dirpath, dirnames, filenames in os.walk(root):
        # Modify dirnames in-place to prune ignored dirs
        dirnames[:] = [d for d in dirnames if d not in IGNORED_DIRS and not d.startswith('.')]
        
        for f in filenames:
            p = Path(dirpath) / f
            if not is_ignored(p):
                files.append(p)
                
    return files

def get_context_string(root_dir: str) -> str:
    """Generates a massive string containing all project code."""
    files = get_project_files(root_dir)
    context = []
    
    context.append(f"Project Context (Root: {root_dir})\n")
    context.append("="*50 + "\n")
    
    for f in files:
        try:
            relative_path = f.relative_to(root_dir)
            content = f.read_text(encoding='utf-8', errors='ignore')
            
            context.append(f"\n--- FILE: {relative_path} ---\n")
            context.append(content)
        except Exception:
            pass # Skip unreadable
            
    return "\n".join(context)

import os
import subprocess
from pathlib import Path

def read_file(path: str) -> str:
    """Reads a file and returns its content. Returns error string if failed."""
    try:
        with open(path, 'r', encoding='utf-8') as f:
            return f.read()
    except Exception as e:
        return f"Error reading {path}: {e}"

def write_file(path: str, content: str) -> bool:
    """Writes content to a file. Creates parent directories if needed."""
    try:
        p = Path(path)
        p.parent.mkdir(parents=True, exist_ok=True)
        with open(p, 'w', encoding='utf-8') as f:
            f.write(content)
        return True
    except Exception as e:
        print(f"Error writing {path}: {e}")
        return False

def run_command(command: str, cwd: str = ".") -> tuple[str, str, int]:
    """Runs a shell command and returns (stdout, stderr, return_code)."""
    try:
        result = subprocess.run(
            command,
            cwd=cwd,
            shell=True,
            capture_output=True,
            text=True,
            encoding='utf-8',
            errors='replace'
        )
        return result.stdout, result.stderr, result.returncode
    except Exception as e:
        return "", str(e), -1

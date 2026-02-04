import os
import json
import tempfile
from pathlib import Path

STATE_FILE = Path(tempfile.gettempdir()) / "antigravity_state.json"

def load_state():
    if not STATE_FILE.exists():
        return {}
    try:
        with open(STATE_FILE, 'r') as f:
            return json.load(f)
    except:
        return {}

def save_state(state):
    with open(STATE_FILE, 'w') as f:
        json.dump(state, f, indent=2)

def set_active_plan(plan_path):
    state = load_state()
    state["active_plan"] = str(Path(plan_path).resolve())
    save_state(state)
    print(f"Active plan set to: {state['active_plan']}")

def get_active_plan():
    state = load_state()
    return state.get("active_plan")

if __name__ == "__main__":
    import sys
    if len(sys.argv) > 2 and sys.argv[1] == "set":
        set_active_plan(sys.argv[2])
    elif len(sys.argv) > 1 and sys.argv[1] == "get":
        print(get_active_plan() or "None")
    else:
        print("Usage: python state_manager.py [set <path> | get]")

import re
import json
import os
import argparse
from google import genai
from google.genai import types
from pathlib import Path

try:
    from .context import get_context_string
    from .ops import read_file, write_file
except ImportError:
    from context import get_context_string
    from ops import read_file, write_file

def clean_json(text: str) -> str:
    # Remove markdown fences ```json ... ```
    text = re.sub(r"^```json\s*", "", text, flags=re.MULTILINE)
    text = re.sub(r"^```\s*", "", text, flags=re.MULTILINE)
    text = re.sub(r"```$", "", text, flags=re.MULTILINE)
    return text.strip()


# Load Config
CONFIG_PATH = Path(__file__).parent.parent / ".antigravity" / "config.json"
try:
    with open(CONFIG_PATH, 'r') as f:
        CONFIG = json.load(f)
    API_KEY = CONFIG.get("api_key") or os.getenv("GEMINI_API_KEY")
    MODEL_NAME = CONFIG.get("model", "gemini-2.0-flash-exp")
except Exception:
    API_KEY = os.getenv("GEMINI_API_KEY")
    MODEL_NAME = "gemini-2.0-flash-exp"

def parse_workflow(content: str) -> tuple[dict, str]:
    if content.startswith("---"):
        parts = re.split(r"^---$", content, maxsplit=2, flags=re.MULTILINE)
        if len(parts) >= 3:
            try:
                metadata = {}
                for line in parts[1].strip().split('\n'):
                    if ':' in line:
                        k, v = line.split(':', 1)
                        metadata[k.strip()] = v.strip()
                return metadata, parts[2].strip()
            except Exception:
                pass
    return {}, content.strip()


# RUNTIME INJECTION: Turns Docs into Agents
ANTIGRAVITY_PROTOCOL = """
# ANTIGRAVITY AGENT PROTOCOL (SYSTEM OVERRIDE)

You are an autonomous AI Agent running inside the Antigravity Kit.
The text below is not just documentation; it is your **OPERATIONAL MANUAL**.

## YOUR MANDATE:
1.  **ACT, DON'T JUST READ**: If the user instruction is a command (e.g., "Build this"), execute it using the Manual's best practices.
2.  **CONTEXT ACCESS**: You have full access to `[PROJECT CONTEXT]`. Read it to understand the codebase.
    - **Do NOT** ask for file permissions.
    - **Do NOT** hallucinate paths. Use `list_dir` to confirm.
3.  **TOOLS**: Use `run_command` to install/build, `write_to_file` to code.
4.  **CHAINING**: If a task is too complex, output a request to chain another agent using `python core/engine.py [workflow]`.

## MANUAL CONTENT START
--------------------------------------------------
{workflow_content}
--------------------------------------------------
## MANUAL CONTENT END
"""

def load_workflow(name: str) -> tuple[dict, str]:
    base_dir = Path(__file__).parent.parent
    path = base_dir / "workflows" / f"{name}.md"
    if not path.exists():
        return {}, f"Error: Workflow '{name}' not found."
    
    raw_content = read_file(str(path))
    metadata, stripped_content = parse_workflow(raw_content)
    
    # INJECT PROTOCOL
    system_prompt = ANTIGRAVITY_PROTOCOL.format(workflow_content=stripped_content)
    
    return metadata, system_prompt


def call_gemini(system_instruction: str, user_prompt: str, json_mode: bool = False) -> str:
    if not API_KEY:
        return "Error: GEMINI_API_KEY environment variable not set."
    try:
        client = genai.Client(api_key=API_KEY)
        
        config = types.GenerateContentConfig(
            system_instruction=system_instruction
        )
        
        if json_mode:
            config.response_mime_type = "application/json"

        response = client.models.generate_content(
            model=MODEL_NAME,
            contents=user_prompt,
            config=config
        )
        return response.text
    except Exception as e:
        return f"Error calling Gemini: {e}"

def execute_workflow(workflow_name: str, user_request: str, project_context: str) -> str:
    print(f"\n🚀 Executing Workflow: {workflow_name}...")
    metadata, system_prompt = load_workflow(workflow_name)
    if "Error" in system_prompt:
        return system_prompt

    full_prompt = f"""
    [PROJECT CONTEXT]
    {project_context}
    
    [USER REQUEST]
    {user_request}
    """
    
    json_mode = metadata.get("output", "").lower() == "json"
    response = call_gemini(system_prompt, full_prompt, json_mode=json_mode)
    print(f"✅ {workflow_name} Completed.")
    return response

def main():
    parser = argparse.ArgumentParser(description="Antigravity Universal Runner")
    parser.add_argument("workflow", help="Name of the workflow (or 'orchestrator')")
    parser.add_argument("prompt", help="User Input")
    args = parser.parse_args()
    
    cwd = os.getcwd()
    print(f"Loading Context from {cwd}...")
    context = get_context_string(cwd)
    
    # ORCHESTRATOR LOGIC
    if args.workflow == "orchestrator":
        plan_json = execute_workflow("orchestrator", args.prompt, context)
        try:
            # Clean before parsing
            cleaned_json = clean_json(plan_json)
            plan = json.loads(cleaned_json)
            
            print(f"\n📋 Orchestrator Plan: {plan.get('thought_process', '')}")
            
            # Chain Execution
            previous_output = ""
            for step in plan.get("steps", []):

                step_workflow = step.get("workflow")
                step_instruction = step.get("instruction")
                
                # Append previous output to history/instruction
                if previous_output:
                    step_instruction += f"\n\n[PREVIOUS AGENT OUTPUT]\n{previous_output}"
                
                output = execute_workflow(step_workflow, step_instruction, context)
                previous_output = output # Chain it
                
                print(f"\n--- Output of {step_workflow} ---\n{output[:500]}...\n")
                
        except json.JSONDecodeError:
            print("Error: Orchestrator failed to return valid JSON.")
            print(plan_json)
    else:
        # SINGLE RUN
        print(execute_workflow(args.workflow, args.prompt, context))

if __name__ == "__main__":
    main()

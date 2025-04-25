def analyze_prompt(prompt: str):
    prompt = prompt.lower()
    tasks = []

    if "environment" in prompt:
        tasks.append({"type": "environment", "description": "Create environment assets"})
    if "model" in prompt:
        tasks.append({"type": "model", "description": "Create character or object models"})
    if "animation" in prompt:
        tasks.append({"type": "animation", "description": "Generate animation sequences"})
    if "shader" in prompt:
        tasks.append({"type": "shader", "description": "Write visual shader logic"})
    if "combat" in prompt:
        tasks.append({"type": "combat", "description": "Simulate combat system"})

    # Default catch-all if no keyword found
    if not tasks:
        tasks.append({"type": "generic", "description": prompt})

    return tasks

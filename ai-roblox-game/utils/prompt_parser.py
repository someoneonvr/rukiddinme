def parse_prompt(prompt):
    # Dummy parser for now, can be replaced with an AI-based one
    parts = prompt.lower().split(":")
    return {
        "agent": parts[0].strip(),
        "description": parts[1].strip() if len(parts) > 1 else prompt.strip()
    }

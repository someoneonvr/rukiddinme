AGENT_ALIASES = {
    "environment": "EnvironmentAI",
    "model": "ModelAI",
    "animation": "AnimationAI",
    "shader": "ShaderAI",
    "combat": "CombatAI",
    "ui": "UIAI",
    "scripting": "ScriptingAI",
    "filemanager": "FileManagerAI"
}

def get_agent_name(alias):
    return AGENT_ALIASES.get(alias.lower(), None)

# dispatcher.py

from agents.environment_ai import EnvironmentAI
from agents.model_ai import ModelAI
from agents.animation_ai import AnimationAI
from agents.shader_ai import ShaderAI
from agents.combat_ai import CombatAI
from agents.ui_ai import UIAI
from agents.scripting_ai import ScriptingAI
from agents.filemanager import FileManagerAI

class Dispatcher:
    def __init__(self):
        self.agents = {
            "environment": EnvironmentAI(),
            "model": ModelAI(),
            "animation": AnimationAI(),
            "shader": ShaderAI(),
            "combat": CombatAI(),
            "ui": UIAI(),
            "scripting": ScriptingAI(),
        }
        self.file_manager = FileManagerAI()  # Add FileManagerAI to handle organization

    def dispatch(self, tasks):
        results = []
        for task in tasks:
            agent_type = task["agent"]
            agent = self.agents.get(agent_type)

            if agent:
                print(f"[Dispatcher] Dispatching task to {agent_type}")
                # Let agent handle its task
                agent.accept_task(task)
                # After task completion, report to FileManager
                result = self.file_manager.accept_task({
                    "description": task["description"],
                    "target": agent_type.capitalize() + "Assets"  # Set folder name based on agent type
                })
                results.append(result)
            else:
                print(f"[Dispatcher] No agent found for: {agent_type}")
                results.append({
                    "agent": agent_type,
                    "error": "Agent not found"
                })
        return results

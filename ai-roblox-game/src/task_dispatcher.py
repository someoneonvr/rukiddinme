from agents import (
    EnvironmentAI, ModelAI, AnimationAI, ShaderAI,
    CombatAI, UIAI, ScriptingAI
)

class TaskDispatcher:
    def __init__(self, task_manager):
        self.task_manager = task_manager
        self.agents = {
            "environment": EnvironmentAI(),
            "model": ModelAI(),
            "animation": AnimationAI(),
            "shader": ShaderAI(),
            "combat": CombatAI(),
            "ui": UIAI(),
            "scripting": ScriptingAI(),
        }

    def dispatch(self):
        results = []
        pending_tasks = self.task_manager.get_pending_tasks()

        for task in pending_tasks:
            agent_type = task.agent
            agent = self.agents.get(agent_type)

            if agent:
                self.task_manager.update_task(task, "In Progress")
                agent.accept_task({
                    "agent": agent_type,
                    "description": task.description
                })
                result = agent.return_result()
                self.task_manager.update_task(task, "Completed")
                results.append({
                    "agent": agent_type,
                    "result": result
                })
            else:
                self.task_manager.update_task(task, "Error")
                print(f"[Dispatcher] No agent found for: {agent_type}")
                results.append({
                    "agent": agent_type,
                    "error": "Agent not found"
                })

        return results

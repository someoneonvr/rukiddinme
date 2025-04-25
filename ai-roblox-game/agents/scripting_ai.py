class ScriptingAI:
    def __init__(self):
        self.last_task = None

    def accept_task(self, task):
        self.last_task = task
        print(f"[ScriptingAI] Accepted task: {task}")

    def return_result(self):
        return {
            "agent": "ScriptingAI",
            "task": self.last_task,
            "result": f"Wrote script logic for: {self.last_task['description']}"
        }

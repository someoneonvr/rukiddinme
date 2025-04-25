class ShaderAI:
    def __init__(self):
        self.last_task = None

    def accept_task(self, task):
        self.last_task = task
        print(f"[ShaderAI] Accepted task: {task}")

    def return_result(self):
        return {
            "agent": "ShaderAI",
            "task": self.last_task,
            "result": f"Created shader logic for: {self.last_task['description']}"
        }

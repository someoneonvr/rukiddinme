class ModelAI:
    def __init__(self):
        self.last_task = None

    def accept_task(self, task):
        self.last_task = task
        print(f"[ModelAI] Accepted task: {task}")

    def return_result(self):
        return {
            "agent": "ModelAI",
            "task": self.last_task,
            "result": f"Created model for: {self.last_task['description']}"
        }

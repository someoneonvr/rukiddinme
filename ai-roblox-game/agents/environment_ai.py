class EnvironmentAI:
    def __init__(self):
        self.last_task = None

    def accept_task(self, task):
        self.last_task = task
        print(f"[EnvironmentAI] Accepted task: {task}")

    def return_result(self):
        return {
            "agent": "EnvironmentAI",
            "task": self.last_task,
            "result": f"Generated environment for: {self.last_task['description']}"
        }

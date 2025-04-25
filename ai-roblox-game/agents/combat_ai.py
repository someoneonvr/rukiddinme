class CombatAI:
    def __init__(self):
        self.last_task = None

    def accept_task(self, task):
        self.last_task = task
        print(f"[CombatAI] Accepted task: {task}")

    def return_result(self):
        return {
            "agent": "CombatAI",
            "task": self.last_task,
            "result": f"Simulated combat logic for: {self.last_task['description']}"
        }

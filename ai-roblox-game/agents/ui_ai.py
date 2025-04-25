class UIAI:
    def __init__(self):
        self.last_task = None

    def accept_task(self, task):
        self.last_task = task
        print(f"[UIAI] Accepted task: {task}")

    def return_result(self):
        return {
            "agent": "UIAI",
            "task": self.last_task,
            "result": f"Designed UI for: {self.last_task['description']}"
        }

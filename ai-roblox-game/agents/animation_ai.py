class AnimationAI:
    def __init__(self):
        self.last_task = None

    def accept_task(self, task):
        self.last_task = task
        print(f"[AnimationAI] Accepted task: {task}")

    def return_result(self):
        return {
            "agent": "AnimationAI",
            "task": self.last_task,
            "result": f"Generated animation for: {self.last_task['description']}"
        }

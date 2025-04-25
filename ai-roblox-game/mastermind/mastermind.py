from .task_analyzer import analyze_prompt
from .dispatcher import dispatch_tasks

class MastermindAI:
    def __init__(self):
        self.history = []

    def process_prompt(self, prompt: str):
        print(f"[Mastermind] Received prompt: {prompt}")
        self.history.append(prompt)

        tasks = analyze_prompt(prompt)
        print(f"[Mastermind] Analyzed into tasks: {tasks}")

        results = dispatch_tasks(tasks)
        print(f"[Mastermind] Received results from agents.")
        
        return results

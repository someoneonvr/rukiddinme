class Task:
    def __init__(self, agent, description):
        self.agent = agent
        self.description = description
        self.status = "Pending"  # Initial status

    def update_status(self, status):
        """
        Update the status of the task.
        """
        self.status = status

    def __str__(self):
        return f"Task for {self.agent}: {self.description} - Status: {self.status}"


class TaskManager:
    def __init__(self):
        self.tasks = []

    def create_task(self, agent, description):
        """
        Create a new task and add it to the task list.
        """
        new_task = Task(agent, description)
        self.tasks.append(new_task)
        print(f"Created new task: {new_task}")
        return new_task

    def update_task(self, task, status):
        """
        Update the status of an existing task.
        """
        task.update_status(status)
        print(f"Updated task: {task}")

    def get_pending_tasks(self):
        """
        Get all tasks that are still pending.
        """
        return [task for task in self.tasks if task.status == "Pending"]

    def get_completed_tasks(self):
        """
        Get all completed tasks.
        """
        return [task for task in self.tasks if task.status == "Completed"]

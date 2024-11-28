from datetime import datetime

from enums import Status
from models import Task
from storage.json_handler import JsonHandler


class TaskManager:
    def __init__(self, storage: JsonHandler) -> None:
        self.storage = storage

    def add_task(self, description: str) -> Task:
        tasks: dict = self.storage.read()
        task_id: int = len(tasks) + 1
        task: Task = Task(id=task_id, description=description, status=Status.TODO, createdAt=str(datetime.now()))
        self.storage.write(task_id, task.model_dump())
        return task

    def update_description(self, task_id: int, description: str) -> bool:
        tasks: dict = self.storage.read()
        key: str = str(task_id)
        if key in tasks:
            tasks[key]["description"]: str = description
            tasks[key]["updatedAt"]: str = str(datetime.now())
            self.storage.write(task_id, tasks[key])
            return True
        return False

    def delete_task(self, task_id: int) -> bool:
        tasks: dict = self.storage.read()
        key: str = str(task_id)
        if key in tasks:
            self.storage.delete(task_id)
            return True
        return False

    def check_availability(self, description: str = "", task_id: int = 0) -> bool:
        tasks: dict = self.storage.read()
        if task_id:
            return str(task_id) in tasks
        return any(task['description'] == description for task in tasks.values())

    def check_exact(self, task_id: int, description: str) -> bool:
        tasks: dict = self.storage.read()
        return tasks[str(task_id)]['description'] == description
        # return self.check_availability(description)

    def check_status(self, task_id: int, status: Status) -> bool:
        tasks: dict = self.storage.read()
        return tasks[str(task_id)]['status'] == status

    def update_status(self, task_id: int, status: Status) -> bool:
        tasks: dict = self.storage.read()
        key = str(task_id)
        if key in tasks:
            tasks[key]["status"]: Status = status
            tasks[key]["updatedAt"]: str = str(datetime.now())
            self.storage.write(task_id, tasks[key])
            return True
        return False

    def list_tasks(self) -> dict:
        tasks: dict = self.storage.read()
        return tasks

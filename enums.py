from enum import Enum


class Action(str, Enum):
    """Enum for defining supported actions in the task manager."""
    ADD: str = "add"
    DELETE: str = "delete"
    UPDATE: str = "update"
    LIST: str = "list"
    MARK_IN_PROGRESS: str = "mark-in-progress"
    MARK_DONE: str = "mark-done"


class Status(str, Enum):
    """Enum for defining the status of tasks."""
    DONE: str = "done"
    TODO: str = "todo"
    IN_PROGRESS: str = "in-progress"

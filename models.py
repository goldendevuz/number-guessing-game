from pydantic import BaseModel


class Task(BaseModel):
    id: int
    description: str
    status: str
    createdAt: str
    updatedAt: str | None = None

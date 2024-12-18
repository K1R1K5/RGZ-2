from pydantic import BaseModel
from typing import Optional, List

class TaskCreate(BaseModel):
    name: str
    dependencies: Optional[List[int]] = None  # Список ID задач, от которых зависит текущая

class TaskUpdate(BaseModel):
    status: str

class Task(BaseModel):
    id: int
    name: str
    status: str
    logs: Optional[str] = None
    dependencies: Optional[List[int]] = None  # Вернём список ID как массив

    class Config:
        orm_mode = True

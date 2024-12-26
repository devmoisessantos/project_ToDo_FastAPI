from pydantic import BaseModel, Field
from uuid import UUID
from typing import Optional
from datetime import datetime


class TaskCreate(BaseModel):
    title: str = Field(..., title="Titulo",
                       min_length=3, max_length=50)
    description: str = Field(..., title="Descricão",
                             min_length=5, max_length=255)
    status: Optional[bool] = False


class TaskUpdate(BaseModel):
    title: Optional[str]
    description: Optional[str]
    status: Optional[bool] = False


class TaskDetail(BaseModel):
    task_id: UUID
    title: str
    description: str
    status: bool
    created_at: datetime  # Alterado de `float` para `datetime`
    updated_at: datetime  # Alterado de `float` para `datetime`

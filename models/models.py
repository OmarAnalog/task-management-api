from sqlmodel import SQLModel,Field
from typing import Optional
from enums import TaskStatus,TaskPriority
from datetime import datetime

class Task(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    title: str = Field(max_length=200, min_length=1)
    description: Optional[str] = Field(None, max_length=1000)
    status: TaskStatus = Field(default=TaskStatus.PENDING, index=True)
    priority: TaskPriority = Field(default=TaskPriority.MEDIUM, index=True)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: Optional[datetime] = None
    due_date: Optional[datetime] = None
    assigned_to: Optional[str] = Field(None, max_length=100)
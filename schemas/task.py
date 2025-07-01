from pydantic import BaseModel,Field,field_validator,ValidationError
from typing import Optional
from enums import TaskPriority,TaskStatus
from datetime import datetime,timezone

# This model is used for creating a new task.
class TaskCreate(BaseModel):
    title: str = Field(max_length=200, min_length=1)
    description: Optional[str] = Field(None, max_length=1000)
    status: TaskStatus = Field(default=TaskStatus.PENDING, index=True)
    priority: TaskPriority = Field(default=TaskPriority.MEDIUM, index=True)
    due_date: Optional[datetime] = None
    assigned_to: Optional[str] = Field(None, max_length=100)

    @field_validator("title", mode="before")
    @classmethod
    def strip_title(cls, v: str) -> str:
        if v is None:
            return v
        return v.strip()

    @field_validator("due_date", mode="after")
    @classmethod
    def validateDueDate(cls, dDate: Optional[datetime]) -> datetime:
        if dDate is None:
            return dDate
        currentTime = datetime.now(timezone.utc).replace(tzinfo=None)
        if dDate <= currentTime:
            raise ValueError("Due date must be in the future")
        return dDate    
# This model is used for updating an existing task.
class TaskUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    status: Optional[TaskStatus] = None
    priority: Optional[TaskPriority] = None
    due_date: Optional[datetime] = None
    assigned_to: Optional[str] = None

    @field_validator("title", mode="before")
    @classmethod
    def strip_title(cls, v: str) -> str:
        if v is None:
            return v
        return v.strip()
    @field_validator("due_date",mode="after")
    @classmethod
    def validateDueDate(cls,dDate:Optional[datetime])->datetime:
        if dDate is None:
            return dDate
        currentTime=datetime.now(timezone.utc).replace(tzinfo=None)
        if currentTime<=dDate:
            raise ValueError("Due date must be in the future")
        return dDate
    
# This will be returned from some Apis.
class TaskResponse(BaseModel):
    id: int
    title: str
    description: Optional[str]
    status: TaskStatus
    priority: TaskPriority
    created_at: datetime
    updated_at: Optional[datetime]
    due_date: Optional[datetime]
    assigned_to: Optional[str]
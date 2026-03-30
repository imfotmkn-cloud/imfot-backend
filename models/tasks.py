from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class TaskCreate(BaseModel):
    title: str
    description: Optional[str] = None
    assigned_to: str
    priority: str  # low, medium, high
    status: str = "pending"

class TaskUpdate(BaseModel):
    title: Optional[str]
    description: Optional[str]
    assigned_to: Optional[str]
    priority: Optional[str]
    status: Optional[str]

class TaskResponse(BaseModel):
    task_id: str
    title: str
    description: Optional[str]
    assigned_to: str
    priority: str
    status: str
    created_at: datetime

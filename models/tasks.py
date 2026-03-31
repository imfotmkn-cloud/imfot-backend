from pydantic import BaseModel
from typing import Optional
from datetime import datetime

# ------------------------
# TASK CREATE
# ------------------------

class TaskCreate(BaseModel):
    title: str
    description: Optional[str] = None
    priority: str = "medium"   # low, medium, high
    status: str = "todo"       # todo, in_progress, completed
    assigned_to: Optional[str] = None
    created_by: Optional[str] = None
    due_date: Optional[datetime] = None


# ------------------------
# TASK UPDATE
# ------------------------

class TaskUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    priority: Optional[str] = None
    status: Optional[str] = None
    assigned_to: Optional[str] = None
    due_date: Optional[datetime] = None


# ------------------------
# TASK RESPONSE
# ------------------------

class TaskResponse(BaseModel):
    task_id: str
    title: str
    description: Optional[str]
    priority: str
    status: str
    assigned_to: Optional[str]
    created_by: Optional[str]
    due_date: Optional[datetime]
    created_at: datetime


# ------------------------
# TASK LOGS (IMPORTANT)
# ------------------------

class TaskLogResponse(BaseModel):
    log_id: str
    task_id: str
    user_id: Optional[str]
    action: str  # created, updated, completed
    details: Optional[str]
    created_at: datetime

from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class ComplianceCreate(BaseModel):
    title: str
    description: Optional[str] = None
    regulation_type: str  # NABH, NABL, ISO, etc.
    assigned_to: Optional[str]
    status: str = "pending"  # pending, in_progress, completed
    due_date: Optional[datetime]

class ComplianceUpdate(BaseModel):
    title: Optional[str]
    description: Optional[str]
    regulation_type: Optional[str]
    assigned_to: Optional[str]
    status: Optional[str]
    due_date: Optional[datetime]

class ComplianceResponse(BaseModel):
    compliance_id: str
    title: str
    description: Optional[str]
    regulation_type: str
    assigned_to: Optional[str]
    status: str
    due_date: Optional[datetime]
    created_at: datetime

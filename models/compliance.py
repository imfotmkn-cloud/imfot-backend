from pydantic import BaseModel
from typing import Optional
from datetime import datetime

# Create Model
class ComplianceCreate(BaseModel):
    title: str
    description: Optional[str] = None
    regulation_type: str  # NABH, NABL, ISO, etc.
    assigned_to: Optional[str] = None
    status: str = "pending"  # pending, in_progress, completed
    due_date: Optional[datetime] = None


# Update Model
class ComplianceUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    regulation_type: Optional[str] = None
    assigned_to: Optional[str] = None
    status: Optional[str] = None
    due_date: Optional[datetime] = None


# Response Model
class ComplianceResponse(BaseModel):
    compliance_id: str
    title: str
    description: Optional[str] = None
    regulation_type: str
    assigned_to: Optional[str] = None
    status: str
    due_date: Optional[datetime] = None
    created_at: datetime

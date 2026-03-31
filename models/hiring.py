from pydantic import BaseModel
from typing import Optional
from datetime import datetime

# ------------------------
# EMPLOYEE MODELS
# ------------------------

class EmployeeCreate(BaseModel):
    full_name: str
    position: str
    department: Optional[str] = None
    status: str = "active"  # active, inactive, exited
    joined_at: Optional[datetime] = None


class EmployeeResponse(BaseModel):
    employee_id: str
    full_name: str
    position: str
    department: Optional[str]
    status: str
    joined_at: Optional[datetime]
    exit_date: Optional[datetime] = None
    created_at: datetime


# ------------------------
# CANDIDATE MODELS
# ------------------------

class CandidateCreate(BaseModel):
    full_name: str
    email: Optional[str] = None
    phone: Optional[str] = None
    position_applied: str
    status: str = "applied"  # applied, shortlisted, interviewed, selected, rejected
    resume_url: Optional[str] = None
    notes: Optional[str] = None


class CandidateResponse(BaseModel):
    candidate_id: str
    full_name: str
    email: Optional[str]
    phone: Optional[str]
    position_applied: str
    status: str
    resume_url: Optional[str]
    notes: Optional[str]
    applied_at: datetime

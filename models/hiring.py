from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class HiringCreate(BaseModel):
    job_title: str
    department: str
    description: Optional[str] = None
    required_skills: list[str]
    experience_required: str
    location: str
    salary_range: Optional[str] = None
    status: str = "open"  # open, closed

class HiringUpdate(BaseModel):
    job_title: Optional[str]
    department: Optional[str]
    description: Optional[str]
    required_skills: Optional[list[str]]
    experience_required: Optional[str]
    location: Optional[str]
    salary_range: Optional[str]
    status: Optional[str]

class HiringResponse(BaseModel):
    job_id: str
    job_title: str
    department: str
    description: Optional[str]
    required_skills: list[str]
    experience_required: str
    location: str
    salary_range: Optional[str]
    status: str
    created_at: datetime

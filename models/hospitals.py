from pydantic import BaseModel
from typing import Optional
from datetime import datetime

# ------------------------
# ORGANIZATION MODELS
# ------------------------

class OrganizationCreate(BaseModel):
    name: str
    type: str  # hospital, startup, clinic, etc.
    location: Optional[str] = None


class OrganizationResponse(BaseModel):
    org_id: str
    name: str
    type: str
    location: Optional[str]
    created_at: datetime


# ------------------------
# BRANCH MODELS
# ------------------------

class BranchCreate(BaseModel):
    org_id: str
    name: str
    location: Optional[str] = None
    status: str = "active"  # active, inactive


class BranchResponse(BaseModel):
    branch_id: str
    org_id: str
    name: str
    location: Optional[str]
    status: str
    opened_at: Optional[datetime]
    created_at: datetime


# ------------------------
# EXPANSION PROJECT MODELS
# ------------------------

class ExpansionProjectCreate(BaseModel):
    org_id: str
    name: str
    type: str  # hospital, franchise, center
    location: Optional[str] = None
    status: str = "planning"  # planning, in_progress, completed


class ExpansionProjectResponse(BaseModel):
    project_id: str
    org_id: str
    name: str
    type: str
    location: Optional[str]
    status: str
    target_completion: Optional[datetime]
    created_at: datetime

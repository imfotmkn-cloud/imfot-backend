from pydantic import BaseModel
from typing import Optional
from datetime import datetime

# ------------------------
# INVESTOR MODELS
# ------------------------

class InvestorCreate(BaseModel):
    name: str
    type: str  # angel, vc, government
    contact_email: Optional[str] = None
    contact_phone: Optional[str] = None
    status: str = "prospective"  # prospective, interested, invested, rejected
    notes: Optional[str] = None


class InvestorResponse(BaseModel):
    investor_id: str
    name: str
    type: str
    contact_email: Optional[str]
    contact_phone: Optional[str]
    status: str
    notes: Optional[str]
    created_at: datetime


# ------------------------
# FUNDING ROUND MODELS
# ------------------------

class FundingRoundCreate(BaseModel):
    round_name: str  # Pre-seed, Seed, Series A
    investor_id: Optional[str] = None
    amount: float
    status: str = "in_progress"  # in_progress, closed, failed
    closed_at: Optional[datetime] = None


class FundingRoundResponse(BaseModel):
    round_id: str
    round_name: str
    investor_id: Optional[str]
    amount: float
    status: str
    closed_at: Optional[datetime]
    created_at: datetime


# ------------------------
# GRANT MODELS
# ------------------------

class GrantCreate(BaseModel):
    name: str
    organization: str  # BIRAC, Govt, etc.
    amount: float
    status: str = "applied"  # applied, approved, rejected
    applied_at: Optional[datetime] = None
    decision_date: Optional[datetime] = None


class GrantResponse(BaseModel):
    grant_id: str
    name: str
    organization: str
    amount: float
    status: str
    applied_at: Optional[datetime]
    decision_date: Optional[datetime]
    created_at: datetime

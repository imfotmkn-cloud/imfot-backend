from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class FundingCreate(BaseModel):
    investor_name: str
    amount: float
    funding_type: str  # seed, series A, grant, etc.
    equity_given: Optional[float] = None
    status: str = "pending"  # pending, approved, rejected
    notes: Optional[str] = None

class FundingUpdate(BaseModel):
    investor_name: Optional[str]
    amount: Optional[float]
    funding_type: Optional[str]
    equity_given: Optional[float]
    status: Optional[str]
    notes: Optional[str]

class FundingResponse(BaseModel):
    funding_id: str
    investor_name: str
    amount: float
    funding_type: str
    equity_given: Optional[float]
    status: str
    notes: Optional[str]
    created_at: datetime

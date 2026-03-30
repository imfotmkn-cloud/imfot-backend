from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime

class HospitalCreate(BaseModel):
    name: str
    address: str
    city: str
    state: str
    pincode: str
    contact_number: str
    email: Optional[str] = None
    departments: List[str]  # ICU, OPD, Emergency, etc.

class HospitalUpdate(BaseModel):
    name: Optional[str]
    address: Optional[str]
    city: Optional[str]
    state: Optional[str]
    pincode: Optional[str]
    contact_number: Optional[str]
    email: Optional[str]
    departments: Optional[List[str]]

class HospitalResponse(BaseModel):
    hospital_id: str
    name: str
    address: str
    city: str
    state: str
    pincode: str
    contact_number: str
    email: Optional[str]
    departments: List[str]
    created_at: datetime

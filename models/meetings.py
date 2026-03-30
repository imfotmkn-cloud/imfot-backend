from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class MeetingCreate(BaseModel):
    title: str
    description: Optional[str] = None
    participants: list[str]
    scheduled_time: datetime
    meeting_link: Optional[str] = None
    status: str = "scheduled"  # scheduled, completed, cancelled

class MeetingUpdate(BaseModel):
    title: Optional[str]
    description: Optional[str]
    participants: Optional[list[str]]
    scheduled_time: Optional[datetime]
    meeting_link: Optional[str]
    status: Optional[str]

class MeetingResponse(BaseModel):
    meeting_id: str
    title: str
    description: Optional[str]
    participants: list[str]
    scheduled_time: datetime
    meeting_link: Optional[str]
    status: str
    created_at: datetime

from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime

# ------------------------
# MEETING MODELS
# ------------------------

class MeetingCreate(BaseModel):
    title: str
    description: Optional[str] = None
    meeting_type: Optional[str] = None  # internal, investor, hospital, etc.
    scheduled_at: datetime
    duration_minutes: int = 60
    participants: Optional[List[str]] = []


class MeetingResponse(BaseModel):
    meeting_id: str
    title: str
    description: Optional[str]
    meeting_type: Optional[str]
    scheduled_at: datetime
    duration_minutes: int
    created_by: Optional[str]
    created_at: datetime


# ------------------------
# PARTICIPANTS MODEL
# ------------------------

class ParticipantResponse(BaseModel):
    participant_id: str
    meeting_id: str
    user_id: str
    added_at: datetime


# ------------------------
# FOLLOW-UP MODELS
# ------------------------

class FollowUpCreate(BaseModel):
    meeting_id: str
    description: str
    task_id: Optional[str] = None
    status: str = "pending"


class FollowUpResponse(BaseModel):
    followup_id: str
    meeting_id: str
    task_id: Optional[str]
    description: str
    status: str
    created_at: datetime

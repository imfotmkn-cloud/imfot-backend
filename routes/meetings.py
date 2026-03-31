from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List
from uuid import uuid4

router = APIRouter(prefix="/meetings", tags=["Meetings"])

# 📦 Models
class Meeting(BaseModel):
    title: str
    description: str = ""
    scheduled_at: str
    participants: List[str] = []
    notes: str = ""

# 🧠 Fake DB
meetings_db = {}

# ➕ Create Meeting
@router.post("/")
def create_meeting(meeting: Meeting):
    meeting_id = str(uuid4())

    meetings_db[meeting_id] = {
        "id": meeting_id,
        "title": meeting.title,
        "description": meeting.description,
        "scheduled_at": meeting.scheduled_at,
        "participants": meeting.participants,
        "notes": meeting.notes,
        "ai_summary": ""   # future use
    }

    return {
        "message": "Meeting created",
        "meeting": meetings_db[meeting_id]
    }

# 📋 Get All Meetings
@router.get("/")
def get_meetings():
    return {
        "meetings": list(meetings_db.values())
    }

# 🔍 Get Single Meeting
@router.get("/{meeting_id}")
def get_meeting(meeting_id: str):
    if meeting_id not in meetings_db:
        raise HTTPException(status_code=404, detail="Meeting not found")

    return meetings_db[meeting_id]

# 🔄 Update Meeting
@router.put("/{meeting_id}")
def update_meeting(meeting_id: str, meeting: Meeting):
    if meeting_id not in meetings_db:
        raise HTTPException(status_code=404, detail="Meeting not found")

    meetings_db[meeting_id].update({
        "title": meeting.title,
        "description": meeting.description,
        "scheduled_at": meeting.scheduled_at,
        "participants": meeting.participants,
        "notes": meeting.notes
    })

    return {
        "message": "Meeting updated",
        "meeting": meetings_db[meeting_id]
    }

# ❌ Delete Meeting
@router.delete("/{meeting_id}")
def delete_meeting(meeting_id: str):
    if meeting_id not in meetings_db:
        raise HTTPException(status_code=404, detail="Meeting not found")

    deleted = meetings_db.pop(meeting_id)

    return {
        "message": "Meeting deleted",
        "meeting": deleted
    }

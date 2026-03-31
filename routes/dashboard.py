from fastapi import APIRouter

router = APIRouter(prefix="/dashboard", tags=["Dashboard"])

@router.get("/")
def get_dashboard():
    return {
        "message": "IMFOT Dashboard",
        "data": {
            "total_users": 19,
            "total_tasks": 45,
            "completed_tasks": 20,
            "pending_tasks": 25,
            "total_meetings": 12,
            "total_hospitals": 5,
            "hiring_openings": 8,
            "funding_rounds": 2,
            "compliance_items": 10
        }
    }

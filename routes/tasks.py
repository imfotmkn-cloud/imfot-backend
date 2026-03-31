[4:06 am, 1/4/2026] Firdaus Khan: from fastapi import APIRouter

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
[4:09 am, 1/4/2026] Firdaus Khan: from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List
from uuid import uuid4

router = APIRouter(prefix="/tasks", tags=["Tasks"])

# 📦 Task Model
class Task(BaseModel):
    title: str
    description: str = ""
    status: str = "todo"   # todo / in_progress / done

# 🧠 Fake Database (temporary)
tasks_db = {}

# ➕ Create Task
@router.post("/")
def create_task(task: Task):
    task_id = str(uuid4())

    tasks_db[task_id] = {
        "id": task_id,
        "title": task.title,
        "description": task.description,
        "status": task.status
    }

    return {
        "message": "Task created",
        "task": tasks_db[task_id]
    }

# 📋 Get All Tasks
@router.get("/")
def get_tasks():
    return {
        "tasks": list(tasks_db.values())
    }

# 🔄 Update Task
@router.put("/{task_id}")
def update_task(task_id: str, task: Task):
    if task_id not in tasks_db:
        raise HTTPException(status_code=404, detail="Task not found")

    tasks_db[task_id].update({
        "title": task.title,
        "description": task.description,
        "status": task.status
    })

    return {
        "message": "Task updated",
        "task": tasks_db[task_id]
    }

# ❌ Delete Task
@router.delete("/{task_id}")
def delete_task(task_id: str):
    if task_id not in tasks_db:
        raise HTTPException(status_code=404, detail="Task not found")

    deleted_task = tasks_db.pop(task_id)

    return {
        "message": "Task deleted",
        "task": deleted_task
    }

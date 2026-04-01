from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List
from uuid import uuid4

router = APIRouter(prefix="/tasks", tags=["Tasks"])

class Task(BaseModel):
    title: str
    description: str = ""
    status: str = "todo"

tasks_db = {}

@router.post("/")
def create_task(task: Task):
    task_id = str(uuid4())

    tasks_db[task_id] = {
        "id": task_id,
        "title": task.title,
        "description": task.description,
        "status": task.status
    }

    return {"message": "Task created", "task": tasks_db[task_id]}

@router.get("/")
def get_tasks():
    return {"tasks": list(tasks_db.values())}

@router.put("/{task_id}")
def update_task(task_id: str, task: Task):
    if task_id not in tasks_db:
        raise HTTPException(status_code=404, detail="Task not found")

    tasks_db[task_id].update({
        "title": task.title,
        "description": task.description,
        "status": task.status
    })

    return {"message": "Task updated", "task": tasks_db[task_id]}

@router.delete("/{task_id}")
def delete_task(task_id: str):
    if task_id not in tasks_db:
        raise HTTPException(status_code=404, detail="Task not found")

    deleted_task = tasks_db.pop(task_id)

    return {"message": "Task deleted", "task": deleted_task}

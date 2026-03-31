from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List
from uuid import uuid4

router = APIRouter(prefix="/hospitals", tags=["Hospitals"])

# 📦 Models
class Organization(BaseModel):
    name: str
    type: str = "hospital"
    location: str = ""

class Branch(BaseModel):
    org_id: str
    name: str
    location: str
    status: str = "active"

# 🧠 Fake DB
organizations_db = {}
branches_db = {}

# ➕ Create Organization
@router.post("/organization")
def create_organization(org: Organization):
    org_id = str(uuid4())

    organizations_db[org_id] = {
        "id": org_id,
        "name": org.name,
        "type": org.type,
        "location": org.location
    }

    return {
        "message": "Organization created",
        "organization": organizations_db[org_id]
    }

# 📋 Get Organizations
@router.get("/organization")
def get_organizations():
    return {
        "organizations": list(organizations_db.values())
    }

# ➕ Create Branch
@router.post("/branch")
def create_branch(branch: Branch):
    if branch.org_id not in organizations_db:
        raise HTTPException(status_code=404, detail="Organization not found")

    branch_id = str(uuid4())

    branches_db[branch_id] = {
        "id": branch_id,
        "org_id": branch.org_id,
        "name": branch.name,
        "location": branch.location,
        "status": branch.status
    }

    return {
        "message": "Branch created",
        "branch": branches_db[branch_id]
    }

# 📋 Get All Branches
@router.get("/branch")
def get_branches():
    return {
        "branches": list(branches_db.values())
    }

# 🔍 Get Branch by Organization
@router.get("/organization/{org_id}/branches")
def get_org_branches(org_id: str):
    org_branches = [
        b for b in branches_db.values() if b["org_id"] == org_id
    ]

    return {
        "organization_id": org_id,
        "branches": org_branches
    }

# ❌ Delete Branch
@router.delete("/branch/{branch_id}")
def delete_branch(branch_id: str):
    if branch_id not in branches_db:
        raise HTTPException(status_code=404, detail="Branch not found")

    deleted = branches_db.pop(branch_id)

    return {
        "message": "Branch deleted",
        "branch": deleted
    }

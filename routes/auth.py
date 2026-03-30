from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

class LoginRequest(BaseModel):
    email: str
    password: str

class SignupRequest(BaseModel):
    name: str
    email: str
    password: str

@router.post("/login")
def login(data: LoginRequest):
    return {
        "message": "Login successful",
        "user": data.email
    }

@router.post("/signup")
def signup(data: SignupRequest):
    return {
        "message": "Signup successful",
        "user": data.email
    }

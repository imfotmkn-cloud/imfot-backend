from pydantic import BaseModel, EmailStr
from datetime import datetime

# Request Models
class UserCreate(BaseModel):
    email: EmailStr
    name: str
    password: str

class UserLogin(BaseModel):
    email: EmailStr
    password: str

# Response Model (IMPORTANT: no password)
class UserResponse(BaseModel):
    user_id: str
    email: EmailStr
    name: str
    is_active: bool
    created_at: datetime

# Token Model (NEW - required for login)
class TokenResponse(BaseModel):
    access_token: str
    token_type: str

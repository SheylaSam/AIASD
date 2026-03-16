from pydantic import BaseModel, EmailStr
from datetime import datetime


# --- User ---

class UserCreate(BaseModel):
    name: str
    email: EmailStr

class UserResponse(BaseModel):
    id: int
    name: str
    email: str

    class Config:
        from_attributes = True


# --- Document ---

class DocumentCreate(BaseModel):
    title: str
    file_path: str
    owner_id: int

class DocumentResponse(BaseModel):
    id: int
    title: str
    file_path: str
    owner_id: int
    uploaded_at: datetime | None

    class Config:
        from_attributes = True

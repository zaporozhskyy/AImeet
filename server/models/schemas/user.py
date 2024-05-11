from pydantic import (EmailStr,
                Field
                      )
from models.schemas.base import BaseSchemaModel
from datetime import datetime
from typing import List
from models.schemas.form import Form

class UserCreate(BaseSchemaModel):
    name: str = Field(min_length=2, max_length=256)
    email: EmailStr = Field(min_length=5, max_length=256)
    password: str = Field(min_length=5, max_length=256)
    
class UserRead(BaseSchemaModel):
    id: int
    name: str
    email: EmailStr
    forms: List[Form]
    
class UserUpdate(BaseSchemaModel):
    name: str | None
    email: EmailStr | None
    password: str | None

class UserLogged(BaseSchemaModel):
    token: str
    name: str 
    email: EmailStr
    is_logged_in: bool
    created_at: datetime
    updated_at: datetime | None 
    
class UserResponse(BaseSchemaModel):
    id: int
    account: UserLogged
    
    
from pydantic import (EmailStr,
                Field
                      )
from models.schemas.base import BaseSchemaModel
from datetime import datetime
from typing import List
from models.schemas.form import Form

class UserCreate(BaseSchemaModel):
    name: str 
    email: EmailStr
    password: str
    
class UserLogin(BaseSchemaModel):
    email: EmailStr
    password: str
    
class UserRead(BaseSchemaModel):
    id: int
    name: str
    email: EmailStr
    forms: List[Form]
    
class UserUpdate(BaseSchemaModel):
    name: str | None
    email: EmailStr | None
    
class UserUpdated(BaseSchemaModel):
    token: str
    name: str
    email: str
    
class UserPasswordUpdate(BaseSchemaModel):
    password: str

class UserPasswordUpdated(BaseSchemaModel):
    token: str
    
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
    
    
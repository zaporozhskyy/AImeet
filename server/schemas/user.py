from pydantic import (EmailStr,
                Field
                      )
from schemas.base import BaseSchemaModel


class UserCreate(BaseSchemaModel):
    name: str = Field(min_length=2, max_length=256)
    email: EmailStr = Field(min_length=5, max_length=256)
    password: str = Field(min_length=5, max_length=256)
    
class UserRead(BaseSchemaModel):
    id: int
    name: str
    email: EmailStr
    
class UserUpdate(BaseSchemaModel):
    name: str | None
    email: str | None
    password: str | None
    
    

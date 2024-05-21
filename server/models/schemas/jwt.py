import datetime

from pydantic import BaseModel, EmailStr


class JWToken(BaseModel):
    exp: datetime.datetime


class JWTAccount(BaseModel):
    email: EmailStr

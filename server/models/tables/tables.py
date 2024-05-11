from models.tables.base import BaseModel
import datetime
from typing import List
from sqlalchemy import Column, Integer, String, Boolean, ARRAY, DateTime, ForeignKey
from sqlalchemy.sql import functions
from sqlalchemy.schema import FetchedValue
from sqlalchemy.orm import Mapped as SQLAlchemyMapped, mapped_column
from sqlalchemy.orm import relationship

class User(BaseModel):
    __tablename__ = 'users'
    
    name: SQLAlchemyMapped[str] = mapped_column(String(256), unique=True, nullable=False)
    email: SQLAlchemyMapped[str] = mapped_column(String(256), unique=True, nullable=False, index=True)
    hashed_password: SQLAlchemyMapped[str] = mapped_column(String(1024), nullable=False)
    token: SQLAlchemyMapped[str] = mapped_column(String, nullable=True)
    is_logged_in: SQLAlchemyMapped[bool] = mapped_column(Boolean, nullable=False, default=False)
    created_at: SQLAlchemyMapped[datetime.datetime] = mapped_column(DateTime(timezone=True), nullable=False, server_default=functions.now())
    updated_at: SQLAlchemyMapped[datetime.datetime] = mapped_column(DateTime(timezone=True), nullable=True, server_onupdate=FetchedValue(for_update=True))
    
    forms: SQLAlchemyMapped[List["Form"]] = relationship(backref="users")
    
class Form(BaseModel):
    __tablename__ = 'forms'
    
    name: SQLAlchemyMapped[str] = mapped_column(String(256), unique=False, nullable=False)
    created_at: SQLAlchemyMapped[datetime.datetime] = mapped_column(DateTime(timezone=True), nullable=False, server_default=functions.now())
    updated_at: SQLAlchemyMapped[datetime.datetime] = mapped_column(DateTime(timezone=True), nullable=True, server_onupdate=FetchedValue(for_update=True))
    
    owner_id: SQLAlchemyMapped[int] = mapped_column(Integer, ForeignKey("users.id"), unique=False)
from pydantic import (EmailStr,
                Field
                      )
from models.schemas.base import BaseSchemaModel
from datetime import datetime
from typing import List
from fastapi import FastAPI, File, UploadFile


class Form(BaseSchemaModel):
    id: int
    owner_id: int
    
class VoiceText(BaseSchemaModel):
    text: str
    
class PydanticFile(BaseSchemaModel):
    file: UploadFile
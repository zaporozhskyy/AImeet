from pydantic import (EmailStr,
                Field
                      )
from models.schemas.base import BaseSchemaModel
from datetime import datetime
from typing import List


class Form(BaseSchemaModel):
    id: int
    owner_id: int
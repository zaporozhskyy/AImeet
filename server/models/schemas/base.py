import datetime
import typing

import pydantic

class BaseSchemaModel(pydantic.BaseModel):
    class Config(pydantic.ConfigDict):
        from_attributes: bool = True
        validate_assignment: bool = True

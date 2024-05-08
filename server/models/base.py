from sqlalchemy import MetaData, Integer, Column
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped as SQLAlchemyMapped, mapped_column

Base = DeclarativeBase

class BaseModel(Base):
    metadata = MetaData()
    
    id: SQLAlchemyMapped[int] = mapped_column(
        Integer,
        primary_key=True,
        autoincrement=True,
        unique=True
    )
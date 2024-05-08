from fastapi import Depends
from typing import Annotated
from sqlalchemy.orm import Session
from database import SessionLocal

def get_db():
    db = SessionLocal()
    try:
        yield db
    except Exception as Exc:
        print(Exc)
        db.rollback()
    finally:
        db.close()

db_dependency = Annotated[Session, Depends(get_db)]
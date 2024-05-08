from fastapi import FastAPI, HTTPException, Depends
from typing import Annotated
from sqlalchemy.orm import Session
from database import SessionLocal, engine
import models.base
import models.models
import uvicorn
from fastapi.middleware.cors import CORSMiddleware
from api.endpoints import router as api_router

app = FastAPI()

origins = [
    'http://localhost:3000'
]

app.add_middleware(
    CORSMiddleware, 
    allow_origins=origins, 
)

app.include_router(router=api_router)


models.base.BaseModel.metadata.drop_all(bind=engine)
models.models.User.metadata.drop_all(bind=engine)
models.models.Form.metadata.drop_all(bind=engine)
models.base.BaseModel.metadata.create_all(bind=engine)
models.models.User.metadata.create_all(bind=engine)
models.models.Form.metadata.create_all(bind=engine)

if __name__ == "__main__":
    uvicorn.run(
        app="main:app"
    )
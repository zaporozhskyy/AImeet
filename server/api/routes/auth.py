import fastapi
from fastapi import Depends, HTTPException, status
from api.dependencies.session import db_dependency
from sqlalchemy.ext.asyncio import AsyncSession
from models.tables.tables import User
from models.schemas.user import UserCreate, UserRead
from repository.crud.account import AccountCRUDRepository as crud

router = fastapi.APIRouter(prefix="/auth", tags=["authentification"])


@router.post("/signup", response_model=UserRead, status_code=status.HTTP_201_CREATED)
async def create_user(user: UserCreate, session: db_dependency):
    db_user = await crud.get_user_by_email(email=user.email, session=session)
    if db_user:
        raise HTTPException(status_code=400, detail=f"Email {db_user} already exists!")
    db_user = await crud.get_user_by_name(name=user.name, session=session)
    if db_user:
        raise HTTPException(status_code=400, detail=f"Name {db_user} already exists!")
    return await crud.create_user(user=user, session=session)
    
    
    
    
    
    
    # db_user = User(**user.model_dump())
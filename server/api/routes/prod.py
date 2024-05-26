import fastapi
from fastapi import Depends, HTTPException, status
from api.dependencies.session import db_dependency
from sqlalchemy.ext.asyncio import AsyncSession
from models.tables.tables import User
import json
from models.schemas.user import UserCreate, UserRead, UserResponse, UserLogged, UserLogin
from repository.crud.account import AccountCRUDRepository as crud
from securities.authorizations.jwt import jwt_generator


router = fastapi.APIRouter(prefix="/prod", tags=["production"])

@router.post("/users", response_model=list[UserRead], status_code=status.HTTP_200_OK)
async def read_users(session: db_dependency):
    db_users = await crud.read_users(session)
    if not db_users:
        raise HTTPException(status_code=404, detail=f"No users found!")

    db_user_list = []

    for db_user in db_users:
        account = UserRead(
            id=db_user.id,
            name=db_user.name,
            email=db_user.email,
            forms=db_user.forms
        )
        db_user_list.append(account)

    return db_user_list

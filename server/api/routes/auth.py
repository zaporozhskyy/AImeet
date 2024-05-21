import fastapi
from fastapi import Depends, HTTPException, status
from api.dependencies.session import db_dependency
from sqlalchemy.ext.asyncio import AsyncSession
from models.tables.tables import User
from models.schemas.user import UserCreate, UserRead, UserResponse, UserLogged, UserLogin
from repository.crud.account import AccountCRUDRepository as crud
from securities.authorizations.jwt import jwt_generator

router = fastapi.APIRouter(prefix="/auth", tags=["authentification"])


@router.post("/sign-up", response_model=UserRead, status_code=status.HTTP_201_CREATED)
async def create_user(user: UserCreate, session: db_dependency):
    db_user = await crud.get_user_by_email(email=user.email, session=session)
    if db_user:
        raise HTTPException(status_code=400, detail=f"Email already exists!")
    db_user = await crud.get_user_by_name(name=user.name, session=session)
    if db_user:
        raise HTTPException(status_code=400, detail=f"Name already exists!")
    
    # new_user = await crud.create_user(user=user, session=session)
    return await crud.create_user(user=user, session=session)


@router.post("/sign-in", response_model=UserResponse, status_code=status.HTTP_202_ACCEPTED)
async def login_user(user_login: UserLogin, session: db_dependency):
    db_user = await crud.check_user_auth(user=user_login, session=session)
    if not db_user:
        raise HTTPException(status_code=400, detail=f"Bad sign in request!")
    
    access_token = jwt_generator.generate_access_token(user=db_user)

    db_user = await crud.set_user_token(user=user_login, token=access_token, session=session)
    
    return UserResponse(
        id=db_user.id,
        account=UserLogged(
            token=db_user.token,
            name=db_user.name,
            email=db_user.email,
            is_logged_in=db_user.is_logged_in,
            created_at=db_user.created_at,
            updated_at=db_user.updated_at
        )
    )
import fastapi
from fastapi import Depends, HTTPException, status
from api.dependencies.session import db_dependency
from pydantic import EmailStr
from sqlalchemy.ext.asyncio import AsyncSession
from models.tables.tables import User
import json
from models.schemas.user import UserCreate, UserRead, UserResponse, UserLogged, UserLogin, UserUpdate, UserPasswordUpdate, UserUpdated, UserPasswordUpdated
from repository.crud.account import AccountCRUDRepository as crud
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from securities.authorizations.jwt import jwt_generator
from config.manager import settings


router = fastapi.APIRouter(prefix="/me", tags=["users"])

@router.get("/", response_model=UserRead, status_code=status.HTTP_200_OK)
async def read_me(session: db_dependency, credentials: HTTPAuthorizationCredentials = Depends(HTTPBearer()) ):
    token = credentials.credentials
    if not token: 
        raise HTTPException(status_code=401, detail=f"No token or token expired, log in!")
    try:
        user_email = jwt_generator.retrieve_details_from_token(token=token, secret_key=settings.JWT_SECRET_KEY)
    except:
        raise HTTPException(status_code=401, detail=f"Incorrect token or expired, log in!")
    user = await crud.get_user_by_email(user_email, session)
    if not user:
        raise HTTPException(status_code=404, detail=f"No account found!")
    
    return user
    
@router.patch("/new-data", response_model=UserUpdated, status_code=status.HTTP_200_OK)
async def change_me(session: db_dependency, 
                    update_name: str | None = None,
                    update_email: EmailStr | None = None,
                    credentials: HTTPAuthorizationCredentials = Depends(HTTPBearer())):
    token = credentials.credentials
    if not token: 
        raise HTTPException(status_code=401, detail=f"No token or token expired, log in!")
    try:
        user_email = jwt_generator.retrieve_details_from_token(token=token, secret_key=settings.JWT_SECRET_KEY)
    except:
        raise HTTPException(status_code=401, detail=f"Incorrect token or expired, log in!")
    user_update = UserUpdate(name=update_name, email=update_email)
    new_user = await crud.patch_user_by_email(user_email, user_update, session)
    
    access_token = jwt_generator.generate_access_token(user=new_user)
    
    return UserUpdated(
        token=access_token,
        name=new_user.name,
        email=new_user.email
    )

@router.patch("/new-pass", response_model=UserPasswordUpdated, status_code=status.HTTP_200_OK)
async def change_me(session: db_dependency, 
                    update_pass: str | None,
                    credentials: HTTPAuthorizationCredentials = Depends(HTTPBearer())):
    token = credentials.credentials
    if not token: 
        raise HTTPException(status_code=401, detail=f"No token or token expired, log in!")
    try:
        user_email = jwt_generator.retrieve_details_from_token(token=token, secret_key=settings.JWT_SECRET_KEY)
    except:
        raise HTTPException(status_code=401, detail=f"Incorrect token or expired, log in!")
    if update_pass is None:
        raise HTTPException(status_code=400, detail=f"Bad request!")
    user_update = UserPasswordUpdate(password=update_pass)
    new_user = await crud.patch_password(user_email, user_update, session)
    if new_user is None:
        raise HTTPException(status_code=404, detail=f"No user with this email!")
    
    access_token = jwt_generator.generate_access_token(user=new_user)
    
    return UserPasswordUpdated(
        token=access_token
    )


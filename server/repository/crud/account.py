from sqlalchemy import select, update
from werkzeug.security import generate_password_hash
from sqlalchemy.ext.asyncio import AsyncSession
from models.tables.tables import User
from models.schemas.user import UserCreate, UserLogin, UserUpdate, UserPasswordUpdate
import datetime
import bcrypt

class AccountCRUDRepository():

    async def read_users(session: AsyncSession):
        stmt = select(User)
        query = await session.execute(statement=stmt)
        return query.scalars().all()
    
    async def get_user_by_id(id: int, session: AsyncSession):
        stmt = select(User).where(User.id == id)
        query = await session.execute(statement=stmt)
        return query.scalar()
    
    async def get_user_by_name(name: str, session: AsyncSession):
        stmt = select(User).where(User.name == name)
        query = await session.execute(statement=stmt)
        return query.scalar()
    
    async def get_user_by_email(email: str, session: AsyncSession):
        stmt = select(User).where(User.email == email)
        query = await session.execute(statement=stmt)
        return query.scalar()
    
    async def check_user_auth(user: UserLogin, session: AsyncSession):
        stmt = select(User).where(User.email == user.email)
        query = await session.execute(statement=stmt)
        db_account = query.scalar()
        bytes_pass = user.password.encode('utf-8')
        if not db_account or not bcrypt.checkpw(bytes_pass, db_account.hashed_password):
            return None
        return db_account

    async def create_user(user: UserCreate, session: AsyncSession):
        db_user = User(name=user.name,
                       email=user.email,
                       is_logged_in=True)
        bytes_pass = user.password.encode('utf-8')
        db_user.set_hashed_password(hashed_password=bcrypt.hashpw(bytes_pass, bcrypt.gensalt()))
        session.add(instance=db_user)
        await session.commit()
        await session.refresh(instance=db_user)
        return db_user
    
    async def patch_user_by_email(email: str, user: UserUpdate, session: AsyncSession):
        new_user_data = user.model_dump()

        select_stmt = select(User).where(User.email == email)
        query = await session.execute(statement=select_stmt)
        update_account = query.scalar()

        if not update_account:
            return None

        update_stmt = update(table=User).where(User.email == email).values(updated_at=datetime.datetime.now())  

        if new_user_data["email"]:
            update_stmt = update_stmt.values(email=new_user_data["email"])
        
        if new_user_data["name"]:
            update_stmt = update_stmt.values(name=new_user_data["name"])

        await session.execute(statement=update_stmt)
        await session.commit()
        await session.refresh(instance=update_account)
        
        return update_account  
    
    
    async def patch_password(email: str, user: UserPasswordUpdate, session: AsyncSession):
        select_stmt = select(User).where(User.email == email)
        query = await session.execute(statement=select_stmt)
        update_account = query.scalar()

        if not update_account:
            return None
        
        update_stmt = update(table=User).where(User.email == email).values(updated_at=datetime.datetime.now())
        
        bytes_pass = user.password.encode('utf-8')
        update_account.set_hashed_password(hashed_password=bcrypt.hashpw(bytes_pass, bcrypt.gensalt()))
        
        await session.execute(statement=update_stmt)
        await session.commit()
        await session.refresh(instance=update_account)
        
        return update_account  
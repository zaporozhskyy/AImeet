from sqlalchemy import select, update
from werkzeug.security import generate_password_hash
from sqlalchemy.ext.asyncio import AsyncSession
from models.tables.tables import User
from models.schemas.user import UserCreate, UserLogin
import bcrypt

class AccountCRUDRepository():

    async def read_accounts(session: AsyncSession):
        stmt = select(User)
        query = await session.execute(statement=stmt)
        return query.scalars().all()
    
    async def get_user_by_id(id: int, session: AsyncSession):
        stmt = select(User).where(User.id == id)
        query = await session.execute(statement=stmt)
        return query.scalar()

    async def get_user_by_token(token: str, session: AsyncSession):
        stmt = select(User).where(User.token == token)
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
    
    async def set_user_token(user: UserLogin, token: str, session: AsyncSession):
        update_stmt = update(table=User).where(User.email == user.email).values(token=token)
        
        await session.execute(statement=update_stmt)
        
        select_stmt = select(User).where(User.email == user.email)
        query = await session.execute(statement=select_stmt)
        update_account = query.scalar()
        
        await session.commit()
        await session.refresh(instance=update_account)
        
        return update_account  

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
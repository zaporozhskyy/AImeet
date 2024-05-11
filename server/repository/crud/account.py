from sqlalchemy import select
from werkzeug.security import generate_password_hash
from sqlalchemy.ext.asyncio import AsyncSession
from models.tables.tables import User
from models.schemas.user import UserCreate

class AccountCRUDRepository():

    async def get_user_by_id(self, id: int, session: AsyncSession):
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

    async def create_user(user: UserCreate, session: AsyncSession):
        db_user = User(name=user.name,
                       email=user.email,
                            hashed_password=generate_password_hash(user.password))
        session.add(instance=db_user)
        session.commit()
        session.refresh(instance=db_user)
        return db_user

# async def create_user(user: UserCreate, db: db_dependency):
#     db_user = User(**user.model_dump())
#     db.add(db_user)
#     db.commit()
#     db.refresh(db_user)
#     return db_user
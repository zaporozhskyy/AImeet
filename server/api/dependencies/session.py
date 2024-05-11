from fastapi import Depends
import typing
from sqlalchemy.ext.asyncio import AsyncSession
from repository.database import db

async def get_session() -> typing.AsyncGenerator[AsyncSession, None]:
    # try:
    yield db.session
    # except Exception as exc:
    #     print(exc)
    #     await db.session.rollback()
    # finally:
    #     await db.session.close()

db_dependency = typing.Annotated[AsyncSession, Depends(get_session)]
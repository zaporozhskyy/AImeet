import pydantic
from sqlalchemy import create_engine 
from sqlalchemy.ext.asyncio import (
    async_sessionmaker,
    AsyncEngine,
    AsyncSession,
    create_async_engine
)
from sqlalchemy.ext.declarative import declarative_base
from config.manager import settings

class AsyncDatabase: 
    def __init__(self):
        self.postgres_url: pydantic.PostgresDsn = pydantic.PostgresDsn(
            url=f"{settings.POSTGRES_SCHEMA}://{settings.POSTGRES_USERNAME}:{settings.POSTGRES_PASSWORD}@{settings.POSTGRES_HOST}:{settings.POSTGRES_PORT}/{settings.POSTGRES_DB}"
        )
        self.engine: AsyncEngine = create_async_engine(settings.POSTGRES_URL)
        self.session: AsyncSession = AsyncSession(autocommit=False, autoflush=False, bind=self.engine)


db: AsyncDatabase = AsyncDatabase()
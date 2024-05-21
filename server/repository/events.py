from fastapi import FastAPI
import typing
from models.tables.tables import Form, User
from repository.database import db
from sqlalchemy.ext.asyncio import AsyncConnection, AsyncSession, AsyncEngine

async def init_db_tables(conn: AsyncEngine) -> None:
    await conn.run_sync(User.metadata.drop_all)
    await conn.run_sync(Form.metadata.drop_all)
    await conn.run_sync(User.metadata.create_all)
    await conn.run_sync(Form.metadata.create_all)
    
async def init_db_connection(backend_app: FastAPI) -> None:
    async with db.engine.begin() as connection:
        await init_db_tables(connection)
    
async def dispose_db_connection() -> None:
    await db.engine.dispose()
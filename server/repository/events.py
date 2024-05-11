from fastapi import FastAPI
import typing
from models.tables.tables import Form, User
from api.dependencies.session import db_dependency
from sqlalchemy.ext.asyncio import AsyncConnection, AsyncSession
async def init_db_tables(connection: AsyncConnection) -> None:
    await connection.run_sync(User.metadata.drop_all)
    await connection.run_sync(Form.metadata.drop_all)
    await connection.run_sync(User.metadata.create_all)
    await connection.run_sync(Form.metadata.create_all)
    
# async def init_db_connection(backend_app: FastAPI) -> None:
#     backend_app.state.db = database
    
#     async with backend_app.state.db.engine.begin() as connection:
#         await init_db_tables(connection=connection)
          
# async def dispose_db_connection(backend_app: FastAPI) -> None:
#     await backend_app.state.db.engine.dispose()
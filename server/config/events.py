import typing

import fastapi
from api.dependencies.session import db_dependency
from repository.events import init_db_tables

def execute_backend_server_event_handler(backend_app: fastapi.FastAPI) -> typing.Any:
    async def launch_backend_server_events() -> None:
        await init_db_tables(db_dependency.connection)

    return launch_backend_server_events


# def terminate_backend_server_event_handler(backend_app: fastapi.FastAPI) -> typing.Any:
#     async def stop_backend_server_events() -> None:
#         await dispose_db_connection(backend_app=backend_app)

#     return stop_backend_server_events

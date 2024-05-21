import typing
import fastapi
from repository.events import init_db_connection, dispose_db_connection

def execute_backend_server_event_handler(backend_app: fastapi.FastAPI) -> typing.Any:
    async def launch_backend_server_events() -> None:
        await init_db_connection(backend_app=backend_app)

    return launch_backend_server_events

def terminate_backend_server_event_handler(backend_app: fastapi.FastAPI) -> typing.Any:
    async def stop_backend_server_events() -> None:
        await dispose_db_connection()

    return stop_backend_server_events

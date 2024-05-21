from fastapi import FastAPI
import asyncio
import uvicorn
from fastapi.middleware.cors import CORSMiddleware
from api.endpoints import router as api_router
from config.manager import settings
from config.events import execute_backend_server_event_handler as db_execute, terminate_backend_server_event_handler as db_terminate

def init_backend_app() -> FastAPI:
    app = FastAPI()
    app.add_middleware(
        CORSMiddleware, 
        allow_origins=settings.ALLOWED_ORIGINS, 
    )
    
    app.add_event_handler(
        "startup",
        db_execute(backend_app=app),
    )
    
    app.add_event_handler(
        "shutdown",
        db_terminate(backend_app=app),
    )
    
    app.include_router(router=api_router)
    
    return app

if __name__ == "__main__":
    uvicorn.run(
        app="main:backend_app"
    )

backend_app: FastAPI = init_backend_app()

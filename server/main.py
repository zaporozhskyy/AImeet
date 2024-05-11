from fastapi import FastAPI
import uvicorn
from fastapi.middleware.cors import CORSMiddleware
from api.endpoints import router as api_router
from config.manager import settings
from config.events import execute_backend_server_event_handler

def init_backend_app() -> FastAPI:
    app = FastAPI()

    app.add_middleware(
        CORSMiddleware, 
        allow_origins=settings.ALLOWED_ORIGINS, 
    )

    app.include_router(router=api_router)
    
    return app

backend_app: FastAPI = init_backend_app()

if __name__ == "__main__":
    uvicorn.run(
        app="main:backend_app"
    )
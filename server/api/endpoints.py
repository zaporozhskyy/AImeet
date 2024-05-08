import fastapi

from api.routes.auth import router as auth_router

router = fastapi.APIRouter()

router.include_router(router=auth_router)
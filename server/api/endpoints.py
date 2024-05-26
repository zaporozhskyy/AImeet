import fastapi

from api.routes.auth import router as auth_router
from api.routes.prod import router as prod_router
from api.routes.user import router as user_router

router = fastapi.APIRouter()

router.include_router(router=auth_router)
router.include_router(router=user_router)
router.include_router(router=prod_router)
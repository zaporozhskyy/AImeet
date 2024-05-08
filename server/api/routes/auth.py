import fastapi
from api.dependencies.session import db_dependency
import models.models
from schemas.user import UserCreate, UserRead

router = fastapi.APIRouter(prefix="/auth", tags=["authentification"])


@router.post("/signup", response_model=UserRead) 
async def create_user(user: UserCreate, db: db_dependency):
    db_user = models.models.User(**user.model_dump())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
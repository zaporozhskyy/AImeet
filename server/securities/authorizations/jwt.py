import datetime
from jose import jwt as jose_jwt, JWTError as JoseJWTError
import pydantic
from fastapi import HTTPException
from config.manager import settings
from models.tables.tables import User
from models.schemas.jwt import JWTAccount, JWToken

class JWTGenerator:
    def __init__(self):
        pass
    def _generate_jwt_token(
        self,
        *,
        jwt_data: dict[str, str],
        expires_delta: datetime.timedelta | None = None,
    ) -> str:
        to_encode = jwt_data.copy()

        if expires_delta:
            expire = datetime.datetime.now() + expires_delta

        else:
            expire = datetime.datetime.now() + datetime.timedelta(minutes=60)

        to_encode.update(JWToken(exp=expire).model_dump())

        return jose_jwt.encode(to_encode, key=settings.JWT_SECRET_KEY, algorithm=settings.JWT_ALGORITHM)

    def generate_access_token(self, user: User) -> str:
        if not user:
            raise HTTPException(status_code=400, detail=f"Cannot generate JWT token without user entity!")

        return self._generate_jwt_token(
            jwt_data=JWTAccount(email=user.email).model_dump(), 
            expires_delta=datetime.timedelta(minutes=60),
        )

    def retrieve_details_from_token(self, token: str, secret_key: str) -> str:
        try:
            payload = jose_jwt.decode(token=token, key=secret_key, algorithms=[settings.JWT_ALGORITHM])
            jwt_account = JWTAccount(email=payload["email"])

        except JoseJWTError as token_decode_error:
            raise ValueError("Unable to decode JWT Token") from token_decode_error

        except pydantic.ValidationError as validation_error:
            raise ValueError("Invalid payload in token") from validation_error

        return jwt_account.email


def get_jwt_generator() -> JWTGenerator:
    return JWTGenerator()


jwt_generator: JWTGenerator = get_jwt_generator()

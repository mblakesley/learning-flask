from fastapi import Depends
from fastapi_jwt_auth import AuthJWT
from pydantic.main import BaseModel

from src.models.users import User, fake_users_db


class Settings(BaseModel):
    authjwt_secret_key: str = 'lulz'


@AuthJWT.load_config
def get_config():
    return Settings()


async def validate_token(auth_jwt: AuthJWT = Depends()) -> User:
    auth_jwt.jwt_required()
    user_str: str = auth_jwt.get_raw_jwt()['sub']
    return User(**fake_users_db[user_str])

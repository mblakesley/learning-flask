from fastapi import Depends, HTTPException, APIRouter
from fastapi_jwt_auth import AuthJWT
from starlette import status

# this import needed so JWT knows about the JWT config
from src.auth.jwt import get_config
from src.models.users import fake_users_db, User, shit_hash

router = APIRouter()


@router.post('/login')
async def login(user: User, auth_config: AuthJWT = Depends()):
    user_db: dict = fake_users_db.get(user.user, {})
    if not user_db or shit_hash(user.password) != user_db['password']:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='wrong user or pass, BITCH!')
    access_token: str = auth_config.create_access_token(subject=user.user)
    return {'access token': access_token}

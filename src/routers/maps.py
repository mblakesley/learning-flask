from fastapi import status, Depends
from fastapi.routing import APIRouter

from src.auth.jwt import validate_token
from src.models.users import User
from src.models.maps import Maps, MapData

router = APIRouter()


# PLURAL
@router.get('/maps')
async def get_maps(user: User = Depends(validate_token)):
    return Maps.get_all()


@router.post('/maps', status_code=status.HTTP_201_CREATED)
async def post_maps(map_data: MapData, user: User = Depends(validate_token)):
    Maps.create(map_data)
    return {'message': 'map posted'}


# SINGULAR
@router.get('/maps/{map_id}')
async def get_map(map_id: int, user: User = Depends(validate_token)):
    return Maps.get(map_id)


@router.put('/maps/{map_id}')
async def put_map(map_id: int, map_data: MapData, user: User = Depends(validate_token)):
    Maps.update(map_id, map_data)
    return {'message': 'map updated'}


@router.delete('/maps/{map_id}')
async def delete_map(map_id: int, user: User = Depends(validate_token)):
    Maps.delete(map_id)
    return {'message': 'map deleted'}

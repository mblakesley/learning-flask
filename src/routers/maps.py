from fastapi import status
from fastapi.routing import APIRouter

from src.models.maps import Maps, MapData

router = APIRouter()


# PLURAL
@router.get('/maps')
async def get_maps():
    return Maps.get_all()


@router.post('/maps', status_code=status.HTTP_201_CREATED)
async def post_maps(map_data: MapData):
    Maps.create(map_data)
    return {'message': 'map posted'}


# SINGULAR
@router.get('/maps/{map_id}')
async def get_map(map_id: int):
    return Maps.get(map_id)


@router.put('/maps/{map_id}')
async def put_map(map_id: int, map_data: MapData):
    Maps.update(map_id, map_data)
    return {'message': 'map updated'}


@router.delete('/maps/{map_id}')
async def delete_map(map_id: int):
    Maps.delete(map_id)
    return {'message': 'map deleted'}

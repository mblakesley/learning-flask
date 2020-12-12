from typing import Optional, List, Tuple

from fastapi import HTTPException, status
from pydantic import BaseModel


class MapData(BaseModel):
    id: Optional[int]
    name: str
    author: str
    published: str


class Maps:
    _maps_db: list = [
        {
            'id': 1,
            'name': 'Four Square',
            'author': 'overthought',
            'published': '2019-05-03',
        },
        {
            'id': 2,
            'name': 'Tunnel Slide',
            'user': 'overthought',
            'published': '2019-06-11',
        },
        {
            'id': 3,
            'name': 'sil vous plait',
            'author': 'freedom fries',
            'published': '2019-07-25',
        },
    ]

    @classmethod
    def get_all(cls) -> List[dict]:
        return cls._maps_db

    @classmethod
    def _get_enum(cls, map_id: int) -> Tuple[int, dict]:
        for i, mapp in enumerate(cls._maps_db):
            if mapp.get('id', 0) == map_id:
                return i, mapp
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)

    @classmethod
    def create(cls, map_data: MapData) -> None:
        # can't get last_id via len() since some IDs may have been deleted
        last_id: int = cls._maps_db[-1]['id']
        map_data.id = last_id + 1
        cls._maps_db.append(map_data.dict())

    @classmethod
    def get(cls, map_id: int) -> dict:
        return cls._get_enum(map_id)[1]

    @classmethod
    def update(cls, map_id: int, map_data: MapData) -> None:
        i, mapp = cls._get_enum(map_id)
        cls._maps_db[i] = map_data.dict()

    @classmethod
    def delete(cls, map_id: int) -> None:
        i, mapp = cls._get_enum(map_id)
        del cls._maps_db[i]

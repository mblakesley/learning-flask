from typing import Optional

from fastapi import HTTPException, status
from pydantic import BaseModel


class MapData(BaseModel):
    id: Optional[int]
    name: str
    author: str
    published: str


class Maps:
    maps: list = [
        {
            'id': 1,
            'name': 'Four Square',
            'author': 'overthought',
            'published': '2019-05-03',
        },
        # {
        #     'user': 'overthought',
        #     'name': 'Tunnel Slide',
        #     'published': '2019-06-11',
        # },
        {
            'id': 2,
            'name': 'The Anals of Science',
            'author': 'queefburglar69',
            'published': '2019-07-25',
        },
    ]

    @classmethod
    def get(cls, map_id: int):
        for mappy in cls.maps:
            if mappy.get('id', 0) == map_id:
                return mappy
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)

    @classmethod
    def insert(cls, mapdata: MapData):
        mapdata.id = len(cls.maps) + 1
        cls.maps.append(mapdata)
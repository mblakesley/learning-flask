from fastapi import HTTPException, status
from fastapi.routing import APIRouter

from src.models.maps import Maps

router = APIRouter()


@router.get('/maps')
async def get_maps():
    return Maps.maps


@router.get('/maps/{map_id}')
async def get_map(map_id: int):
    return Maps.get_by_id(map_id)


@router.delete('/maps/{map_id}')
async def delete_map(map_id: int):
    mappy: dict = Maps.get_by_id(map_id)
    Maps.maps.remove(mappy)
    return {'message': 'map deleted'}


# from flask import request, jsonify
# from flask_jwt import jwt_required
# from flask_restful import Resource
#
#
# class Games(Resource):
#     @jwt_required()
#     def get(self):
#         return games_list
#
#     def post(self):
#         new_game = request.get_json()
#         if get_game(new_game['name']):
#             return 'resource already exists. I\'m on to you!', 400
#         games_list.append(new_game)
#         return new_game, 201
#
#
# class Game(Resource):
#     @jwt_required()
#     def get(self, name):
#         # I don't like that every method here repeats the pattern of calling get_game, then checking result
#         # but I don't know how to simplify it, since even if I package the 404, these methods still must check result
#         # django seems to get out of this via `raise`, so runner must automatically try/catch. Doesn't help me here :-/
#         game = get_game(name)
#         if game:
#             return jsonify(game)
#         return 'resource not found. you gonna cry about it?', 404
#
#     def put(self, name):
#         updated_game = request.get_json()
#         if name != updated_game['name']:
#             return 'mismatched names. whaddya tryin\' to pull, anyway?', 400
#         game = get_game(name)
#         if game:
#             game.update(updated_game)
#             return jsonify(game)
#         return 'resource not found. now scram!', 404
#
#     def delete(self, name):
#         game = get_game(name)
#         if game:
#             games_list.remove(game)
#             return 'we deleted it so good', 200
#         return 'resource not found. also you\'re ugly.', 404
#
#
# def get_game(name):
#     for game in games_list:
#         if game['name'] == name:
#             return game

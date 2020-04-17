from flask import Flask, request, jsonify
from flask_restful import Resource, Api

games_list = [
    {
        "name": "dead-space",
        "genre": "survival horror",
    },
    {
        "name": "portal-2",
        "genre": "puzzle platformer",
    },
]


class Games(Resource):
    def get(self):
        return games_list

    def post(self):
        new_game = request.get_json()
        for game in games_list:
            if game["name"] == new_game["name"]:
                return "resource already exists. I'm on to you!"
        games_list.append(new_game)
        return new_game, 201


class Game(Resource):
    def get(self, name):
        for game in games_list:
            if game["name"] == name:
                return game
        return "resource not found. you gonna cry about it?", 404


app = Flask(__name__)
api = Api(app)
api.add_resource(Games, '/games')
api.add_resource(Game, '/games/<string:name>')

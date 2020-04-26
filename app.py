from flask import Flask
from flask_jwt import JWT
from flask_restful import Api

from src import auth
from controllers.games import Games, Game


app = Flask(__name__)
app.secret_key = 'lulz'
api = Api(app)
api.add_resource(Games, '/games')
api.add_resource(Game, '/games/<string:name>')

# this maps authenticate() to /auth AND uses identity() to map JWT to user (via ID)
jwt = JWT(app, auth.authenticate, auth.identity)

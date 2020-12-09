from flask import Flask 
from flask_restful import Api, Resource, reqparse

app = Flask(__name__)
api = Api(app)

'''
@app.route('/')
def first_page():
	return "<h1> hello world </h1> <br> <p> this is the firs page</p>"
'''

games = {
	"1": {'name': 'Cyberpunk2077', 'release_date': '2021'},
	"2": {'name': 'GodOfWar', 'release_date': '2018'}
}

game_arguments = reqparse.RequestParser()
game_arguments.add_argument("name", type=str, help="the game title")
game_arguments.add_argument("release_date", type=str, help = "release date parameter")

class GameStore(Resource):
	def get(self, game_id):
		return games[game_id]

	def post(self, game_id):
		arguments = game_arguments.parse_args()
		games[game_id] = arguments
		print({game_id: arguments})

class GameStore(Resource):
	def get(self):
		return games

	def post(self):
		arguments = game_arguments.parse_args()
		games = arguments
		print(arguments)


api.add_resource(GameStore, "/game/<int:game_id>")
if __name__ == "__main__":
	app.run(debug=True)

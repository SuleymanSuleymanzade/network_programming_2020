from flask import Flask 
from flask_restful import Resource, Api 
import flask_sqlalchemy 
#from .database_manager import 

app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQL(app)

class GameEntity(db.Model):
	id = db.Column(db.Integer, primary_key = True)
	title = db.Column(db.String(64), nullable=False)
	release_date = db.Column(db.String(32), nullable=False)
	person_id = db.Column(db.Integer, db.ForeignKey('personentity.id'))
	def __repr__(self):
		return f"{self.__class__.__name__}({self.title}, {self.release_date})"

class PersonEntity(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(64), nullable=False)
	surname = db.Column(db.String(64), nullable=False)
	email = db.Column(db.String(64), nullable=False, unique=True)
	games = db.relationship('Deals', backref='owner')

	def __repr__(self):
		return f"{self.__class__.__name__}({self.name}, {self.surname}, {self.email})"



class Person:
	def __init__(self, name, surname, email):
		self.name = name 
		self.surname = surname 
		self.email = email 

class Game:
	def __init__(self, title, release_date, platform):
		self.title = title
		self.release_date = release_date 
		self.platform = platform 





class GameStore(Resource):
	def get(self, title):
		pass 

	def delete(self, title):
		pass 


class Client(Resource):
	def get(self, email):
		pass

	def post(self, email):
		pass


app.add_resource(GameStore, "/game_ops")
app.add_resource(Client, "user_ops")

if __name__ == "__main__":
	app.run(debug=True)
from flask import Flask 
from flask_sqlalchemy import SQLAlchemy 

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///local_db.db'
db = SQLAlchemy(app)


class User(db.Model):

	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(64), nullable=False)
	surname = db.Column(db.String(64), nullable=False)
	pc_s = db.relationship('PC', backref='owner')

	def __init__(self, name, surname):
		self.name = name 
		self.surname = surname

	def __repr__(self):
		return f"{self.__class__.name}(name= {self.name}, surname = {self.surname})"


class PC(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	title=db.Column(db.String(64), nullable=False)
	owner_id = db.Column(db.Integer, db.ForeignKey('user.id'))

	def __str__(str):
		return f"{title}"

	def __repr__(self):
		return f"{self.__class__.name}(name= {self.name}, surname = {self.surname})"




if __name__ == "__main__":
	app.run(debug = True)
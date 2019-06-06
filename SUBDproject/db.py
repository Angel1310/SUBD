from flask import Flask 
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)

class Movie(db.Model):
	id = db.Column(db.Integer, primary_key = True, autoincrement = True, nullable = False)
	name = db.Column(db.String(100), nullable = False) 
	year = db.Column(db.Integer, nullable = False)
	director = db.Column(db.String(100), nullable = False)
	producer = db.Column(db.Integer, db.ForeignKey('producer.id'))

class Actor(db.Model):
	id = db.Column(db.Integer, primary_key = True, autoincrement = True, nullable = False)
	name = db.Column(db.String(100), nullable = False) 
	nationality = db.Column(db.String(100), nullable = False)
	film = db.Column(db.Integer, db.ForeignKey('movie.id'))

class Producer(db.Model):
	id = db.Column(db.Integer, primary_key = True, autoincrement = True, nullable = False)
	name = db.Column(db.String(100), nullable = False) 
	capital = db.Column(db.Integer, nullable = False)	
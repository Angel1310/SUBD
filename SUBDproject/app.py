from flask import Flask, render_template, flash, request, redirect, url_for
import sqlite3

app = Flask(__name__)

@app.route('/movie_form')
def movie_form():

@app.route('/actor_form')
def movie_form():

@app.route('/producer_form')
def movie_form():

@app.route('/create_movie', methods = ['POST', 'GET'])
def create_movie():
	if request.method == 'POST':

		try:
			name = request.form['name']
			year = request.form['year']
			director = request.form['director']

			with sqlite3.connect("database.db") as con:
   				cur = con.cursor()
   				cur.execute("INSERT INTO movie (name, year, director) VALUES (?, ?, ?)", (name, year, director))
   				con.commit()
   		except:
   			con.rollback()
   		finally:
   			con.close()

@app.route('/create_actor', methods = ['POST', 'GET'])
def create_actor():
	if request.method == 'POST':

		try:
			name = request.form['name']
			nationality = request.form['nationality']
			

			with sqlite3.connect("database.db") as con:
   				cur = con.cursor()
   				cur.execute("INSERT INTO actor (name, nationality) VALUES (?, ?)", (name, nationality))
   				con.commit()
   		except:
   			con.rollback()
   		finally:
   			con.close()

@app.route('/create_producer', methods = ['POST', 'GET'])
def create_producer():
		if request.method == 'POST':

		try:
			name = request.form['name']
			capital = request.form['capital']

			with sqlite3.connect("database.db") as con:
   				cur = con.cursor()
   				cur.execute("INSERT INTO producer (name, capital) VALUES (?, ?, ?)", (name, capital))
   				con.commit()
   		except:
   			con.rollback()
   		finally:
   			con.close()
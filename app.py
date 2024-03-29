from flask import Flask, render_template, flash, request, redirect, url_for, flash
import sqlite3

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
	return render_template('msg.html')

@app.route('/movie_form')
def movie_form():
   return render_template('film.html')

@app.route('/actor_form', methods = ['POST', 'GET'])
def actor_form():
   return render_template('actors.html')

@app.route('/producer_form', methods = ['POST', 'GET'])
def producer_form():
   return render_template("company.html")

@app.route('/create_movie', methods = ['POST', 'GET'])
def create_movie():
	if request.method == 'POST':
		try:
			name = request.form['name']
			year = request.form['year']
			director = request.form['director']
			producer = request.form['producer']
			
			with sqlite3.connect("database.db") as con:
				cur = con.cursor()
				cur.execute("INSERT INTO movie (name, year, director, producer_id) VALUES (?, ?, ?, ?)", (name, int(year), director, int(producer)))
				con.commit()
		except Exception as e:
			con.rollback()
			return str(e)
		finally:
			con.close()

	return redirect('/show_movies')

@app.route('/create_actor', methods = ['POST', 'GET'])
def create_actor():
	if request.method == 'POST':
		try:

			name = request.form['name']
			nationality = request.form['nationality']
			with sqlite3.connect("database.db") as con:
				cur = con.cursor()			
				cur.execute("INSERT INTO actor (name, nationality) VALUES (?, ?, ?)", (name, nationality))
				con.commit()
		except:
			con.rollback()
		finally:
			con.close()

	return render_template('msg.html')

@app.route('/create_producer', methods = ['POST', 'GET'])
def create_producer():
	if request.method == 'POST':
		try:
			name = request.form['name']
			capital = request.form['capital']

			with sqlite3.connect("database.db") as con:
				cur = con.cursor()
				cur.execute("INSERT INTO producer(name, capital) VALUES (?, ?)", (name, int(capital)))
				con.commit()
		except Exception as e:
			return e
			con.rollback()
		finally:
			con.close()

	return render_template('msg.html')

@app.route('/show_movies')
def show_movies():
	try:
		with sqlite3.connect("database.db") as con:
			cur = con.cursor()
			cur.execute("SELECT * from movie")
			con.commit()
			movies = cur.fetchall()
	except:
		con.rollback()
	finally:
		con.close()

	return render_template('movies.html', movies = movies)

@app.route('/show_actors')
def show_actors():
	try:
		with sqlite3.connect("database.db") as con:
			cur = con.cursor()
			cur.execute("SELECT * from actor")
			con.commit()
			actors = cur.fetchall()
	except:
		con.rollback()
	finally:
		con.close()

	return render_template('movies.html', movies = actors)

@app.route('/show_producers')
def show_producers():
	try:
		with sqlite3.connect("database.db") as con:
			cur = con.cursor()
			cur.execute("SELECT * from producer")
			con.commit()
			producers = cur.fetchall()
	except:
		con.rollback()
	finally:
		con.close()

	return render_template('movies.html', movies = producers)

@app.route('/movie/<int:movie_id>')
def movie(movie_id):
	movie = [1, 2, 3, 4, 5]
	try:
		with sqlite3.connect("database.db") as con:
			cur = con.cursor()
			cur.execute("SELECT * FROM movie WHERE id = ?", str(movie_id))
			movie = cur.fetchone()
			con.commit()
	except:
		con.rollback()
	finally:
		con.close()
		return render_template("movie.html", movie = movie)

@app.route('/actor/<int:actor_id>')
def actor(actor_id):
	actor = [1, 2, 3, 4, 5]
	try:
		with sqlite3.connect("database.db") as con:
			cur = con.cursor()
			cur.execute("SELECT * FROM actor WHERE id = ?", str(actor_id))
			movie = cur.fetchone()
			con.commit()
	except:
		con.rollback()
	finally:
		con.close()
		return render_template("actor.html", actor = actor)

@app.route('/producer/<int:producer_id>')
def producer(producer_id):
	producer = [1, 2, 3, 4, 5]
	try:
		with sqlite3.connect("database.db") as con:
			cur = con.cursor()
			cur.execute("SELECT * FROM producer WHERE id = ?", str(producer_id))
			movie = cur.fetchone()
			con.commit()
	except:
		con.rollback()
	finally:
		con.close()
		return render_template("producer.html", producer = producer)

@app.route('/delete_movie/<int:movie_id>')
def delete_movie(movie_id):
	try:
		with sqlite3.connect("database.db") as con:
			cur = con.cursor()
			cur.execute("DELETE FROM movie WHERE id = ?", str(movie_id))
			con.commit()
	except Exception as e:
			con.rollback()
			return str(e)
	finally:
		con.close()
		
	return redirect('/show_movies')

@app.route('/delete_actor/<int:actor_id>')
def delete_actor(actor_id):
	try:
		with sqlite3.connect("database.db") as con:
			cur = con.cursor()
			cur.execute("DELETE FROM actor WHERE id = ?", str(actor_id))
			con.commit()
	except Exception as e:
			con.rollback()
			return str(e)
	finally:
		con.close()
		
	return redirect('/show_actors')

@app.route('/delete_producer/<int:producer_id>')
def delete_producer(producer_id):
	try:
		with sqlite3.connect("database.db") as con:
			cur = con.cursor()
			cur.execute("DELETE FROM actor WHERE id = ?", str(producer_id))
			con.commit()
	except Exception as e:
			con.rollback()
			return str(e)
	finally:
		con.close()
		
	return redirect('/show_producers')	

@app.route('/edit_movie/<int:movie_id>', methods = ['POST', 'GET'])
def edit_movie(movie_id):

	if request.method == 'POST':
		try:
			name = request.form['name']
			year = request.form['year']
			director = request.form['director']

			with sqlite3.connect("database.db") as con:
				cur = con.cursor()
				cur.execute("UPDATE movies SET name = ?, year = ?, director = ? WHERE id = ?", (name, year, director, str(movie_id)))
				con.commit()
		except:
			con.rollback()
		finally:
			con.close()

		redirect("/movie/" + movie_id)

@app.route('/edit_actor/<int:actor_id>', methods = ['POST', 'GET'])
def edit_actor(actor_id):

	if request.method == 'POST':
		try:
			name = request.form['name']
			nationality = request.form['nationality']

			with sqlite3.connect("database.db") as con:
				cur = con.cursor()
				cur.execute("UPDATE actors SET name = ?, nationality = ? WHERE id = ?", (name, nationality, str(actor_id)))
				con.commit()
		except:
			con.rollback()
		finally:
			con.close()

		redirect("/movie/" + movie_id)

@app.route('/edit_producer/<int:producer_id>', methods = ['POST', 'GET'])
def edit_producer(producer_id):

	if request.method == 'POST':
		try:
			name = request.form['name']
			capital = request.form['capital']

			with sqlite3.connect("database.db") as con:
				cur = con.cursor()
				cur.execute("UPDATE producers p SET p.name = ?, p.capital = ? WHERE p.id = ?", (name, capital, producer_id))
				con.commit()
		except:
			con.rollback()
		finally:
			con.close()

@app.route('/chose_movie_act/<int:actor_id>/<int:movie_id>')
def chose_movie_act(actor_id, movie_id):
	try:
		with sqlite3.connect("database.db") as con:
			cur = con.cursor()
			cur.execute("UPDATE actors a SET a.film = ? WHERE a.id = ?", (movie_id, actor_id))
			con.commit()
	except:
		con.rollback()
	finally:
		con.close()


if __name__ == '__main__':
	app.run(debug = True)
